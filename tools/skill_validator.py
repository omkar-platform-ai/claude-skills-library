#!/usr/bin/env python3
"""
Skill validator for the claude-skills-library.

Validates skill directory structure, SKILL.md frontmatter, metadata.yaml fields,
evals, secrets, and referenced file paths.

Usage:
    python tools/skill_validator.py skills/contributed/<skill>/
    python tools/skill_validator.py --validate-all
    python tools/skill_validator.py --validate-all --json
    python tools/skill_validator.py skills/curated/<skill>/ --curated
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SECRET_PATTERNS = [
    re.compile(r"\bapi[_-]?key\s*=\s*['\"][^'\"]+['\"]", re.IGNORECASE),
    re.compile(r"\btoken\s*=\s*['\"][^'\"]+['\"]", re.IGNORECASE),
    re.compile(r"\bpassword\s*=\s*['\"][^'\"]+['\"]", re.IGNORECASE),
    re.compile(r"\bsk_[a-zA-Z0-9]{20,}"),
    re.compile(r"\bsk-[a-zA-Z0-9]{20,}"),
    re.compile(r"\bghp_[a-zA-Z0-9]{20,}"),
    re.compile(r"\bgithub_pat_[a-zA-Z0-9_]{20,}"),
]
VALID_STATUS = {"stable", "beta", "deprecated", "archived"}
REQUIRED_METADATA_FIELDS = [
    "name", "version", "author", "created_date",
    "last_updated", "status", "tags", "maintainer",
]
REQUIRED_EVAL_FIELDS = ["id", "prompt", "description", "expected_output_criteria"]
SKILL_MD_LINE_SOFT_LIMIT = 500

PATH_REF_RE = re.compile(r"`([a-zA-Z0-9_./-]+\.(md|json|yaml|yml|py|sh|js|ts))`")


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def scan_for_secrets(content):
    hits = []
    for pat in SECRET_PATTERNS:
        for m in pat.finditer(content):
            hits.append(m.group(0)[:60])
    return hits


def validate_skill(skill_path, curated=False):
    skill_path = Path(skill_path).resolve()
    errors = []
    warnings = []

    skill_md = skill_path / "SKILL.md"
    metadata_yaml = skill_path / "metadata.yaml"
    evals_json = skill_path / "evals" / "evals.json"

    # 1. SKILL.md exists + frontmatter
    if not skill_md.exists():
        errors.append("SKILL.md is missing")
    else:
        text = skill_md.read_text(encoding="utf-8")
        frontmatter, body = split_frontmatter(text)
        if frontmatter is None:
            errors.append("SKILL.md is missing YAML frontmatter (--- delimiters)")
        else:
            try:
                fm = yaml.safe_load(frontmatter) or {}
            except yaml.YAMLError as e:
                errors.append(f"SKILL.md frontmatter is invalid YAML: {e}")
                fm = {}
            if "name" not in fm:
                errors.append("SKILL.md frontmatter missing 'name'")
            if "description" not in fm:
                errors.append("SKILL.md frontmatter missing 'description'")

        line_count = text.count("\n") + 1
        if line_count > SKILL_MD_LINE_SOFT_LIMIT:
            warnings.append(
                f"SKILL.md is {line_count} lines (soft limit {SKILL_MD_LINE_SOFT_LIMIT}); "
                "consider moving content to references/"
            )

        # 10. Path references in SKILL.md must exist
        for match in PATH_REF_RE.finditer(text):
            rel = match.group(1)
            if rel.startswith(("http", "/", "#")) or rel in ("SKILL.md", "metadata.yaml"):
                continue
            candidate = (skill_path / rel).resolve()
            if not candidate.exists() and not (skill_path / Path(rel).name).exists():
                warnings.append(f"SKILL.md references missing path: {rel}")

        # 9. Secrets scan
        for hit in scan_for_secrets(text):
            errors.append(f"SKILL.md may contain a secret: {hit}")

    # 4-6. metadata.yaml exists + required fields + version + status
    if not metadata_yaml.exists():
        errors.append("metadata.yaml is missing")
    else:
        try:
            meta = yaml.safe_load(metadata_yaml.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            errors.append(f"metadata.yaml is invalid YAML: {e}")
            meta = {}

        for field in REQUIRED_METADATA_FIELDS:
            if field not in meta:
                errors.append(f"metadata.yaml missing required field: {field}")

        version = str(meta.get("version", ""))
        if version and not SEMVER_RE.match(version):
            errors.append(f"metadata.yaml version '{version}' is not semver (X.Y.Z)")

        status = meta.get("status")
        if status and status not in VALID_STATUS:
            errors.append(
                f"metadata.yaml status '{status}' must be one of {sorted(VALID_STATUS)}"
            )

        tags = meta.get("tags")
        if tags is not None and not isinstance(tags, list):
            errors.append("metadata.yaml 'tags' must be a list")

        if curated:
            source = meta.get("source") or {}
            if not isinstance(source, dict) or "url" not in source:
                errors.append("curated skill must have metadata.source.url")
            if "last_sync" not in source:
                warnings.append("curated skill missing metadata.source.last_sync")
            if "license" not in source:
                warnings.append("curated skill missing metadata.source.license")
            if not (skill_path / "UPSTREAM_SOURCE.md").exists():
                errors.append("curated skill must include UPSTREAM_SOURCE.md")

        for hit in scan_for_secrets(metadata_yaml.read_text(encoding="utf-8")):
            errors.append(f"metadata.yaml may contain a secret: {hit}")

    # 7-8. evals/evals.json exists + 3+ items + required fields
    if not evals_json.exists():
        errors.append("evals/evals.json is missing")
    else:
        try:
            evals_data = json.loads(evals_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"evals/evals.json is invalid JSON: {e}")
            evals_data = {}

        cases = evals_data.get("evals") or evals_data.get("eval_cases") or []
        if len(cases) < 3:
            errors.append(
                f"evals/evals.json must contain at least 3 eval items (found {len(cases)})"
            )
        for i, case in enumerate(cases):
            for field in REQUIRED_EVAL_FIELDS:
                if field not in case:
                    errors.append(f"eval #{i + 1} missing field: {field}")

    return {
        "skill": skill_path.name,
        "path": str(skill_path.relative_to(REPO_ROOT)),
        "errors": errors,
        "warnings": warnings,
        "ok": not errors,
    }


def discover_skills():
    skills = []
    for tier in ("contributed", "curated"):
        tier_dir = SKILLS_ROOT / tier
        if not tier_dir.exists():
            continue
        for p in sorted(tier_dir.iterdir()):
            if p.is_dir() and (p / "SKILL.md").exists():
                skills.append((p, tier == "curated"))
    return skills


def format_human(results):
    lines = []
    for r in results:
        status = "PASS" if r["ok"] else "FAIL"
        lines.append(f"[{status}] {r['path']}")
        for err in r["errors"]:
            lines.append(f"  ERROR: {err}")
        for warn in r["warnings"]:
            lines.append(f"  WARN:  {warn}")
    total = len(results)
    failures = sum(1 for r in results if not r["ok"])
    lines.append("")
    lines.append(f"Summary: {total - failures}/{total} passed, {failures} failed")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Validate claude-skills-library skills")
    parser.add_argument("path", nargs="?", help="Path to a single skill directory")
    parser.add_argument("--validate-all", action="store_true", help="Validate every skill")
    parser.add_argument("--curated", action="store_true", help="Mark target as a curated skill")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    if args.validate_all:
        targets = discover_skills()
    elif args.path:
        targets = [(Path(args.path), args.curated)]
    else:
        parser.error("Provide a skill path or --validate-all")

    if not targets:
        print("No skills found to validate.")
        sys.exit(0)

    results = [validate_skill(p, curated=c) for p, c in targets]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_human(results))

    sys.exit(0 if all(r["ok"] for r in results) else 1)


if __name__ == "__main__":
    main()
