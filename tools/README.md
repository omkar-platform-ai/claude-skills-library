# Tools & Scripts

Install dependencies:

```bash
pip install -r tools/requirements.txt
```

## skill_validator.py

Validates skill directory structure, SKILL.md frontmatter, metadata.yaml fields, and evals.

```bash
# Validate a single skill
python tools/skill_validator.py skills/contributed/investment-analyst/

# Validate every skill in the repo
python tools/skill_validator.py --validate-all

# JSON output for tooling
python tools/skill_validator.py --validate-all --json

# Curated skills require source tracking
python tools/skill_validator.py skills/curated/<skill>/ --curated
```

Exit code is `0` on success and `1` on any failure.

## generate_index.py

Reads every `metadata.yaml` under `skills/` and writes `SKILLS_INDEX.md`.

```bash
python tools/generate_index.py
```

## skill_updater.py

Stub for the curated-skill update workflow. Lists curated skills and appends a
timestamped entry to `MAINTENANCE_LOG.md`. No external API calls yet.

```bash
python tools/skill_updater.py --check
python tools/skill_updater.py --log-only
```
