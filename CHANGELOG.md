# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.2.0] - 2026-05-25
### Added
- Two-tier `skills/` structure: `contributed/` (6) and `curated/` (6), all moved via `git mv` to preserve history
- `tools/skill_validator.py`, `generate_index.py`, `skill_updater.py` (stub), `requirements.txt`
- GitHub Actions: `.github/workflows/validate-skills.yml`, `publish-index.yml`
- Root tracking files: `SKILLS_INDEX.md` (auto-generated), `MAINTENANCE_LOG.md`, `VERSION`
- `docs/SKILLS_DEV_GUIDE.md`, `docs/CURATION_POLICY.md`, `docs/MAINTENANCE_SCHEDULE.md`
- `metadata.yaml` and `evals/evals.json` for all 12 skills
- `UPSTREAM_SOURCE.md` for the 6 curated skills with license + sync metadata
- README.md for `commercial-projection-architect`, `executive-deck-specialist`, `fitness-advisor`, `it-company-due-diligence-advisor`

### Changed
- README.md: split skills table into contributed vs curated; removed phantom skill references
- CONTRIBUTING.md: documents `contributed/` vs `curated/` tiers and links to the new docs
- Stripped non-standard `metadata:` block from 12 SKILL.md frontmatters (data moved to `metadata.yaml`)
- `skill_validator.py --curated` now requires `UPSTREAM_SOURCE.md` and warns on missing `source.license`

### Removed
- `tools/skill-validator.py`, `eval-runner.py`, `skill-packager.py` (replaced by underscored versions)
- `.github/workflows/validate-pr.yml`, `publish-release.yml` (replaced by new workflows)
- `skills/contributed/investment-analyst/evals/eval_set.json` (replaced by `evals.json`)

## [0.1.0] - 2025-05-21
### Added
- Initial release
- Investment analyst skill
- Documentation and templates
