# Curation Policy

Rules for adding an **external** skill to `skills/curated/`. Skills you author
yourself belong in `skills/contributed/`.

## License

The upstream source must use an open, permissive license compatible with this
repo's MIT license. Acceptable:

- MIT
- Apache 2.0
- BSD (2-clause or 3-clause)
- ISC
- CC0 / Public Domain

Reject GPL, AGPL, custom non-commercial, or unlicensed sources.

## Maintenance criteria

The upstream source must show at least one of:

- A commit within the last 12 months
- An active maintainer responding to issues
- Clear "stable / archived" signal from the author

If the upstream is abandoned and the skill is still valuable, fork it into
`contributed/` instead and accept maintenance ownership.

## Required files

In addition to the standard skill layout:

```
skills/curated/<skill-name>/
├── SKILL.md
├── metadata.yaml          # MUST include source.url and source.last_sync
├── README.md
├── UPSTREAM_SOURCE.md     # attribution, license, sync notes
└── evals/evals.json
```

### UPSTREAM_SOURCE.md template

```markdown
# Upstream Source

- **Repository:** https://github.com/<owner>/<repo>
- **Author:** Name (@handle)
- **License:** MIT
- **Last sync:** 2026-05-25
- **Commit pinned:** <git sha>

## Changes from upstream

- [List any modifications made when importing]
- [If none, write "None — verbatim copy"]

## Sync history

- 2026-05-25: initial import at <sha>
```

### metadata.yaml source block

```yaml
source:
  url: https://github.com/<owner>/<repo>
  commit: <git sha>
  last_sync: 2026-05-25
  license: MIT
```

## PR process

1. Open a GitHub issue: "Curate: <skill name>" with upstream link, license
   verification, and use case
2. Wait for a maintainer ack before opening the PR
3. PR must include UPSTREAM_SOURCE.md and pass
   `python tools/skill_validator.py skills/curated/<name>/ --curated`
4. Two maintainer reviews required for curated skills (one extra check vs
   contributed)
5. Once merged, the skill is tracked by `tools/skill_updater.py` for upstream
   drift

## Ongoing responsibility

Curated skills are reviewed quarterly. See
[MAINTENANCE_SCHEDULE.md](MAINTENANCE_SCHEDULE.md).
