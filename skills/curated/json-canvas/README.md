# JSON Canvas Skill

Create and edit JSON Canvas files (`.canvas`) with nodes, edges, groups, and
connections — following the JSON Canvas Spec 1.0 used by Obsidian and other
canvas-aware tools.

## Skill Structure

```text
json-canvas/
├── SKILL.md
├── README.md
└── references/
    ├── EXAMPLES.md         ← Full canvases: mind maps, flowcharts, boards
    └── SPEC_REFERENCE.md   ← Condensed Spec 1.0 data model + invariants
```

## How to Trigger

Invoke naturally by saying things like:

- "Create a new canvas for this project plan"
- "Add a node to my mind map"
- "Connect these two nodes with an arrow"
- "Edit this `.canvas` file to group the related ideas"

## What You Get

Valid `.canvas` JSON with unique node IDs, resolved edge references, correct
coordinate layout, and proper z-ordering — ready to drop into an Obsidian
vault or any JSON Canvas Spec 1.0 compatible app.

## References

- [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/)
- [JSON Canvas GitHub](https://github.com/obsidianmd/jsoncanvas)
