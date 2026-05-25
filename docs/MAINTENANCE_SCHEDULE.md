# Maintenance Schedule

How often we touch the repo and what each cadence covers.

## Weekly (automated)

- CI runs on every push and PR (`validate-skills.yml`)
- `SKILLS_INDEX.md` regenerates on push to main (`publish-index.yml`)
- No manual action required

## Monthly

- Triage open issues and PRs
- Cut a patch release if any bug fixes merged
- Update `MAINTENANCE_LOG.md` with the month's activity summary

## Quarterly

Scheduled for the 15th of January, April, July, October.

- Run the full eval suite against the active Claude model and record pass rates
  in `metadata.yaml` (`eval_pass_rate`, `eval_count`)
- Re-run `tools/skill_updater.py --check` for curated skills and sync any with
  upstream drift
- Dependency audit (`tools/requirements.txt`)
- Review skill statuses: anything still `beta` after two quarters either
  promotes to `stable` or moves to `archived`
- Append a quarterly summary entry to `MAINTENANCE_LOG.md`

## Triggered

- Curated skill PR → triggers an UPSTREAM_SOURCE.md check
- Claude model migration → triggers a full eval re-run and version bump
- Security report → immediate response, patch release within 48 hours
