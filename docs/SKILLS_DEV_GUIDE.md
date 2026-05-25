# Skills Dev Guide

Practical guide to writing a skill in this repo. For the design philosophy and
quality rubric, see [ARCHITECTURE.md](../ARCHITECTURE.md).

## Directory layout

Every skill lives in `skills/contributed/<skill-name>/` and has:

```
skills/contributed/<skill-name>/
├── SKILL.md              # required — Claude instructions with YAML frontmatter
├── metadata.yaml         # required — version, author, status, tags
├── README.md             # required — human-facing summary
├── evals/
│   └── evals.json        # required — 3+ test cases
├── references/           # optional — domain knowledge files (create when SKILL.md > 500 lines)
└── scripts/              # optional — helper scripts
```

Curated (external upstream) skills live in `skills/curated/<skill-name>/` with
the same layout plus a `source.url` and `source.last_sync` in `metadata.yaml`
and an `UPSTREAM_SOURCE.md`. See [CURATION_POLICY.md](CURATION_POLICY.md).

## SKILL.md

Must start with YAML frontmatter containing at minimum `name` and `description`.

```markdown
---
name: skill-name
description: >
  One or two sentences describing what the skill does and when Claude should
  use it. Be specific about trigger keywords and the domain.
---

# Skill Name

[Real Claude instructions: role, context, task, output format, constraints.]
[Imperative voice. No "you could consider".]
[Under 500 lines — move overflow to references/.]
```

## metadata.yaml

```yaml
name: skill-name
version: 1.0.0          # semver
author: Author Name
created_date: 2026-05-25
last_updated: 2026-05-25
description: One-line description
tags: [tag1, tag2, tag3]
status: stable          # stable | beta | deprecated | archived
maintainer: github-handle
quality_score: 0.0
eval_count: 3
eval_pass_rate: 0.0
dependencies: []
compatibility:
  mcp_required: false
source:
  url: https://github.com/<owner>/<repo>
```

For curated skills, `source` must include `last_sync` (ISO date).

## evals/evals.json

Minimum 3 cases (`easy`, `medium`, `hard` is a good target spread).

```json
{
  "skill_name": "skill-name",
  "evals": [
    {
      "id": "eval_001",
      "prompt": "A realistic prompt a real user would type",
      "description": "What this test covers",
      "difficulty": "easy",
      "expected_output_criteria": [
        "Specific, verifiable criterion",
        "Another verifiable criterion"
      ]
    }
  ]
}
```

Each criterion must be something a human reviewer (or future automated eval
runner) can mark pass/fail without ambiguity.

## Run the validator locally

```bash
pip install -r tools/requirements.txt

# Single skill
python tools/skill_validator.py skills/contributed/my-skill/

# All skills
python tools/skill_validator.py --validate-all
```

The validator exits 0 on success and 1 on any failure. SKILL.md over 500 lines
emits a warning (not a failure) — fix it before submitting if you can.

## PR checklist

- [ ] SKILL.md frontmatter has `name` and `description`
- [ ] metadata.yaml has all required fields and a semver version
- [ ] evals.json has 3+ cases with concrete criteria
- [ ] README.md describes triggers, inputs, outputs, files
- [ ] `python tools/skill_validator.py --validate-all` exits 0
- [ ] No secrets in any file (the validator scans, but double-check)
