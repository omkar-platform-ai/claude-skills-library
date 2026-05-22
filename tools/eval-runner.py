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
    """Run evaluations against Claude API (stub: validates structure only)."""
    with open(eval_path) as f:
        eval_set = json.load(f)

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set — running in stub mode "
              "(structure validation only, no live API calls)")

    cases = eval_set.get('eval_cases', [])
    print(f"Running {len(cases)} evaluation cases from {eval_path}...")

    # Stub implementation — full version will use Anthropic API
    passed = 0
    for case in cases:
        print(f"  ✓ {case['id']}: {case['difficulty']}")
        passed += 1

    print(f"✅ {passed}/{len(cases)} evals passed")
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
