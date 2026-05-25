#!/usr/bin/env python3
"""
Detect skills whose metadata.yaml version bumped vs a previous commit, then
package and publish a per-skill GitHub Release.

Tag scheme:    <skill-name>-v<version>
Title:         <skill-name> v<version>
Artifact:      dist/<skill-name>-v<version>.zip  (the entire skill directory)

Usage:
    # Auto: diff every skill's metadata.yaml against <before-sha> and release bumps
    python tools/release_skills.py --before-sha <SHA>

    # Manual: force-release one skill at its current version
    python tools/release_skills.py --skill-path skills/contributed/<name>

    # Bootstrap: release every skill at its current version (skips existing tags)
    python tools/release_skills.py --release-all

    # Dry run: print what would be released without invoking gh
    python tools/release_skills.py --before-sha <SHA> --dry-run

Requires the `gh` CLI on PATH and an authenticated token (`GH_TOKEN` env var in
CI). Skipped silently if no bumps are detected.
"""

import argparse
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
DIST_ROOT = REPO_ROOT / "dist"
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
NULL_SHA = "0" * 40


def git_show(ref, path):
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def load_yaml(text):
    if text is None:
        return None
    try:
        return yaml.safe_load(text) or {}
    except yaml.YAMLError:
        return None


def collect_current_skills():
    skills = []
    for tier in ("contributed", "curated"):
        tier_dir = SKILLS_ROOT / tier
        if not tier_dir.exists():
            continue
        for skill_dir in sorted(tier_dir.iterdir()):
            meta_path = skill_dir / "metadata.yaml"
            if meta_path.is_file():
                skills.append((skill_dir, tier, meta_path))
    return skills


def detect_bumped(before_sha):
    bumped = []
    use_diff = before_sha and before_sha != NULL_SHA
    for skill_dir, tier, meta_path in collect_current_skills():
        rel = meta_path.relative_to(REPO_ROOT).as_posix()
        current = load_yaml(meta_path.read_text(encoding="utf-8")) or {}
        previous = load_yaml(git_show(before_sha, rel)) if use_diff else None
        cur_v = str(current.get("version", "")).strip()
        prev_v = str((previous or {}).get("version", "")).strip()
        if not cur_v or not SEMVER_RE.match(cur_v):
            continue
        if cur_v == prev_v:
            continue
        bumped.append({
            "name": current.get("name", skill_dir.name),
            "path": skill_dir.relative_to(REPO_ROOT).as_posix(),
            "tier": tier,
            "version": cur_v,
            "previous_version": prev_v or None,
        })
    return bumped


def all_targets():
    targets = []
    for skill_dir, tier, meta_path in collect_current_skills():
        meta = load_yaml(meta_path.read_text(encoding="utf-8")) or {}
        version = str(meta.get("version", "")).strip()
        if not SEMVER_RE.match(version):
            print(f"SKIP {skill_dir.name}: invalid version '{version}'", file=sys.stderr)
            continue
        targets.append({
            "name": meta.get("name", skill_dir.name),
            "path": skill_dir.relative_to(REPO_ROOT).as_posix(),
            "tier": tier,
            "version": version,
            "previous_version": None,
        })
    return targets


def manual_target(skill_path):
    skill_dir = (REPO_ROOT / skill_path).resolve()
    meta_path = skill_dir / "metadata.yaml"
    if not meta_path.is_file():
        raise SystemExit(f"No metadata.yaml at {meta_path}")
    meta = load_yaml(meta_path.read_text(encoding="utf-8")) or {}
    version = str(meta.get("version", "")).strip()
    if not SEMVER_RE.match(version):
        raise SystemExit(f"Invalid semver in {meta_path}: '{version}'")
    return [{
        "name": meta.get("name", skill_dir.name),
        "path": skill_dir.relative_to(REPO_ROOT).as_posix(),
        "tier": skill_dir.parent.name,
        "version": version,
        "previous_version": None,
    }]


def package(skill_dir, name, version):
    DIST_ROOT.mkdir(parents=True, exist_ok=True)
    zip_path = DIST_ROOT / f"{name}-v{version}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file():
                arcname = f.relative_to(skill_dir.parent).as_posix()
                zf.write(f, arcname)
    return zip_path


def tag_exists(tag):
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"],
        cwd=REPO_ROOT,
        capture_output=True,
    )
    if result.returncode == 0:
        return True
    try:
        result = subprocess.run(
            ["gh", "release", "view", tag],
            cwd=REPO_ROOT,
            capture_output=True,
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False  # gh not installed (local dry-run); rely on git tag check above


def gh_release(tag, title, body, files, dry_run):
    cmd = ["gh", "release", "create", tag, "--title", title, "--notes", body]
    cmd.extend(str(f) for f in files)
    if dry_run:
        print(f"DRY RUN: {' '.join(cmd)}")
        return
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def release_one(entry, dry_run):
    skill_dir = REPO_ROOT / entry["path"]
    tag = f"{entry['name']}-v{entry['version']}"
    if tag_exists(tag):
        print(f"SKIP {tag} — tag already exists")
        return
    zip_path = package(skill_dir, entry["name"], entry["version"])
    title = f"{entry['name']} v{entry['version']}"
    prev = entry["previous_version"] or "first release"
    body = (
        f"Automated per-skill release.\n\n"
        f"- **Skill:** `{entry['name']}`\n"
        f"- **Tier:** {entry['tier']}\n"
        f"- **Version:** {entry['version']} (previous: {prev})\n"
        f"- **Path:** `{entry['path']}`\n\n"
        f"See [SKILLS_INDEX.md](../blob/main/SKILLS_INDEX.md) for the full catalog."
    )
    gh_release(tag, title, body, [zip_path], dry_run)
    verb = "WOULD RELEASE" if dry_run else "RELEASED"
    print(f"{verb} {tag} ({zip_path.name})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before-sha", help="Previous commit SHA to diff against")
    parser.add_argument("--skill-path", help="Release a single skill by its directory path")
    parser.add_argument(
        "--release-all",
        action="store_true",
        help="Release every skill at its current version (skips existing tags)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.release_all:
        targets = all_targets()
    elif args.skill_path:
        targets = manual_target(args.skill_path)
    elif args.before_sha:
        targets = detect_bumped(args.before_sha)
    else:
        parser.error("provide --before-sha, --skill-path, or --release-all")

    if not targets:
        print("No version bumps detected. Nothing to release.")
        return

    print(f"Detected {len(targets)} skill(s) to release:")
    for t in targets:
        prev = t["previous_version"] or "—"
        print(f"  - {t['name']}: {prev} -> {t['version']} ({t['tier']})")

    for t in targets:
        release_one(t, args.dry_run)


if __name__ == "__main__":
    main()
