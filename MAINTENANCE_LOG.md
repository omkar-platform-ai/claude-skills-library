# Maintenance Log

## 2026-05-25 — Architecture Refactor v0.2.0
- Type: Structural refactor
- Scope: Two-tier skills/ structure, tooling rewrite, CI/CD overhaul
- Skills migrated: 12 from `skills/<name>/` to the new tiers
  - **Contributed (6):** commercial-projection-architect, commit-message, executive-deck-specialist, fitness-advisor, investment-analyst, it-company-due-diligence-advisor
  - **Curated (6):** defuddle, json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown (upstream: kepano/obsidian-skills, MIT); session-handoff (upstream: nateherkai/a-bunch-of-skills, license unspecified — flagged for verification)
- Skills created: 0 (README's phantom skills were removed instead — see CHANGELOG)
- Tools: `skill_validator.py`, `generate_index.py`, `skill_updater.py` (stub), `requirements.txt`
- Workflows: replaced `validate-pr.yml` / `publish-release.yml` with `validate-skills.yml` and `publish-index.yml`
- Docs added: `docs/SKILLS_DEV_GUIDE.md`, `docs/CURATION_POLICY.md`, `docs/MAINTENANCE_SCHEDULE.md`
- Validator strengthened: curated mode now requires `UPSTREAM_SOURCE.md` and warns on missing `source.license`
- Validation status: 12/12 skills pass `skill_validator --validate-all`
- Open items: session-handoff upstream license is unspecified; resolve per CURATION_POLICY.md by next quarterly review
- Next review: 2026-08-15
