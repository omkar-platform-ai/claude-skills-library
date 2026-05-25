# Obsidian Bases Skill

Create and edit Obsidian Bases (`.base` files) — database-like views over
your vault, with filters, formulas, summaries, and multiple view types
(table, cards, list, map).

## Skill Structure

```text
obsidian-bases/
├── SKILL.md
├── README.md
└── references/
    ├── FUNCTIONS_REFERENCE.md   ← Full function reference by type
    └── EXAMPLES.md              ← Worked `.base` files for common patterns
```

## How to Trigger

Invoke naturally by saying things like:

- "Create a base that lists all my project notes"
- "Add a formula to compute days until due"
- "Build a Reading List base grouped by status"
- "Filter this base to show only notes tagged #task"

## What You Get

Valid YAML `.base` files with:

- Global and per-view filters
- Computed formula properties (with Duration arithmetic, date math,
  conditionals)
- Table / cards / list / map views
- Summaries (Sum, Average, Min, Max, Median, etc.)
- Group-by and sort directives

## References

- [Bases Syntax](https://help.obsidian.md/bases/syntax)
- [Functions](https://help.obsidian.md/bases/functions)
- [Views](https://help.obsidian.md/bases/views)
- [Formulas](https://help.obsidian.md/formulas)
