#!/usr/bin/env python3
"""
Validate skill structure and content.
Usage: python tools/skill-validator.py skills/
"""

import sys
import json
import yaml
from pathlib import Path

def validate_skill(skill_path):
    """Validate a single skill"""
    skill_path = Path(skill_path)
    
    # Check required files
    required = [
        skill_path / "SKILL.md",
        skill_path / "README.md"
    ]
    
    for f in required:
        if not f.exists():
            print(f"❌ Missing required file: {f.relative_to(skill_path.parent)}")
            return False
    
    # Check for references
    refs_dir = skill_path / "references"
    if not refs_dir.exists() or len(list(refs_dir.glob("*.md"))) < 2:
        print(f"❌ Missing references/ directory or <2 reference files")
        return False
    
    # Validate SKILL.md YAML
    try:
        with open(skill_path / "SKILL.md") as f:
            content = f.read()
            # Extract YAML frontmatter
            intent.startswith("---"):
                _, yaml_text, _ = content.split("---", 2)
                yaml.safe_load(yaml_text)
    except Exception as e:
        print(f"❌ Invalid SKILL.md YAML: {e}")
        return False
    
    print(f"✅ Skill '{skill_path.name}' is valid")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python skill-validator.py <skill-path>")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    if skill_path.is_dir() and (skill_path / "SKILL.md").exists():
        success = validate_skill(skill_path)
    else:
        # Validate all skills in directory
        success = True
        for skill in Path("skills").glob("*/"):
            if not validate_skill(skill):
                success = False
    
    sys.exit(0 if success else 1)
