#!/usr/bin/env python3
"""
Skill Updater — checks curated skills for upstream updates.

Currently a stub. Full implementation in Phase 3.

Usage:
    python tools/skill_updater.py --check
    python tools/skill_updater.py --log-only
"""

import argparse
from datetime import datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CURATED_DIR = REPO_ROOT / "skills" / "curated"
LOG_PATH = REPO_ROOT / "MAINTENANCE_LOG.md"


def iter_curated_metadata():
    if not CURATED_DIR.exists():
        return
    for skill_dir in sorted(CURATED_DIR.iterdir()):
        meta_path = skill_dir / "metadata.yaml"
        if meta_path.exists():
            try:
                meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError:
                continue
            yield skill_dir.name, meta


def append_log(entry):
    if not LOG_PATH.exists():
        LOG_PATH.write_text("# Maintenance Log\n\n", encoding="utf-8")
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Stub: check curated skills for upstream updates")
    parser.add_argument("--check", action="store_true", help="List curated skills and their last_sync")
    parser.add_argument("--log-only", action="store_true", help="Append a check entry to MAINTENANCE_LOG.md")
    args = parser.parse_args()

    skills = list(iter_curated_metadata())
    print(f"Curated skills tracked: {len(skills)}")

    for name, meta in skills:
        source = (meta.get("source") or {}) if isinstance(meta.get("source"), dict) else {}
        print(f"  - {name}: url={source.get('url', '—')} last_sync={source.get('last_sync', '—')}")

    if args.log_only or args.check:
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        append_log(
            f"\n## {timestamp} — skill_updater run\n"
            f"- Mode: {'check' if args.check else 'log-only'}\n"
            f"- Curated skills examined: {len(skills)}\n"
            f"- Action: stub only; no external API calls performed\n"
        )
        print(f"Logged run to {LOG_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
