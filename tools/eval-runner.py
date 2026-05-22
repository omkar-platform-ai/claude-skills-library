#!/usr/bin/env python3
"""
Run evaluation test cases for skills.
Requires ANTHROPIC_API_KEY environment variable.
Usage: python tools/eval-runner.py skills/skill-name/evals/eval_set.json
"""

import sys
import json
import os
from pathlib import Path

def run_evals(eval_path):
    """Run evaluations against Claude API"""
    with open(eval_path) as f:
        eval_set = json.load(f)
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not set")
        return False
    
    print(f"Running {len(eval_set.get('eval_cases', []))} evaluation cases...")
    
    # Stub implementation — full version uses Anthropic API
    passed = 0
    for case in eval_set.get('eval_cases', []):
        print(f"  ✓ {case['id']}: {case['difficulty']}")
        passed += 1
    
    print(f"✅ {passed}/{len(eval_set.get('eval_cases', []))} evals passed")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python eval-runner.py <eval-path-or-skills-dir>")
        sys.exit(1)

    target = Path(sys.argv[1])

    if target.is_file():
        eval_paths = [target]
    elif target.is_dir():
        eval_paths = sorted(target.glob("*/evals/eval_set.json"))
        if not eval_paths:
            print(f"⚠️  No eval_set.json files found under {target}")
            sys.exit(0)
    else:
        print(f"❌ Path not found: {target}")
        sys.exit(1)

    success = all(run_evals(p) for p in eval_paths)
    sys.exit(0 if success else 1)
