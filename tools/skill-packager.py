#!/usr/bin/env python3
"""
Package a skill folder into a .skill file (zip).
Usage: python tools/skill-packager.py skills/skill-name --output ./dist/
"""

import sys
import zipfile
from pathlib import Path

def package_skill(skill_path, output_dir=None):
    """Package skill into .skill file"""
    skill_path = Path(skill_path)
    output_dir = Path(output_dir or ".")
    
    output_file = output_dir / f"{skill_path.name}-skill.skill"
    
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in skill_path.rglob('*'):
            if file.is_file():
                arcname = file.relative_to(skill_path.parent)
                zf.write(file, arcname)
    
    print(f"✅ Packaged to: {output_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python skill-packager.py <skill-path-or-skills-dir> [--output <dir>]")
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    output_dir = "."

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        output_dir = sys.argv[idx + 1]

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    if (skill_path / "SKILL.md").exists():
        targets = [skill_path]
    elif skill_path.is_dir():
        targets = sorted(p for p in skill_path.iterdir() if (p / "SKILL.md").exists())
        if not targets:
            print(f"⚠️  No skills found under {skill_path}")
            sys.exit(0)
    else:
        print(f"❌ Path not found: {skill_path}")
        sys.exit(1)

    success = all(package_skill(t, output_dir) for t in targets)
    sys.exit(0 if success else 1)
