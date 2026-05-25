# JSON Canvas Spec 1.0 Reference

The full JSON Canvas Spec 1.0 lives at <https://jsoncanvas.org/spec/1.0/>.
This file is a condensed, copy-friendly reference of the data model so you
don't have to round-trip to the spec while editing `.canvas` files.

## File Shape

A `.canvas` file is a single JSON object with two optional top-level arrays:

```json
{
  "nodes": [],
  "edges": []
}
```

Both arrays default to empty. A file with no nodes and no edges is valid
but renders as a blank canvas.

## Node Types

| Type | Required Fields | Purpose |
|---|---|---|
| `text` | `text` | Markdown content rendered inline |
| `file` | `file` | Embed a file from the vault |
| `link` | `url` | Embed an external URL |
| `group` | none | Visual container for other nodes |

All nodes also require: `id`, `type`, `x`, `y`, `width`, `height`.

## Common Node Fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | 16-char lowercase hex, unique across file |
| `type` | string | yes | One of: text, file, link, group |
| `x` | integer | yes | Top-left X in pixels; can be negative |
| `y` | integer | yes | Top-left Y in pixels; can be negative |
| `width` | integer | yes | Pixels |
| `height` | integer | yes | Pixels |
| `color` | canvasColor | no | Preset `"1"`–`"6"` or hex `"#RRGGBB"` |

## Type-Specific Fields

### text

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Markdown; use `\n` (not `\\n`) for newlines |

### file

| Field | Type | Required | Notes |
|---|---|---|---|
| `file` | string | yes | Path from vault root |
| `subpath` | string | no | `#heading` or `#^block-id` |

### link

| Field | Type | Required | Notes |
|---|---|---|---|
| `url` | string | yes | Any absolute URL |

### group

| Field | Type | Required | Notes |
|---|---|---|---|
| `label` | string | no | Text label rendered on the group |
| `background` | string | no | Path to background image |
| `backgroundStyle` | string | no | `cover`, `ratio`, or `repeat` |

## Edge Fields

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| `id` | string | yes | — | Unique across file |
| `fromNode` | string | yes | — | ID of source node |
| `toNode` | string | yes | — | ID of target node |
| `fromSide` | string | no | — | top, right, bottom, left |
| `toSide` | string | no | — | top, right, bottom, left |
| `fromEnd` | string | no | `none` | `none` or `arrow` |
| `toEnd` | string | no | `arrow` | `none` or `arrow` |
| `color` | canvasColor | no | — | Preset or hex |
| `label` | string | no | — | Text displayed on edge |

## Color Type (`canvasColor`)

Either a hex string `"#FF0000"` or a preset:

| Preset | Conventional Color |
|---|---|
| `"1"` | Red |
| `"2"` | Orange |
| `"3"` | Yellow |
| `"4"` | Green |
| `"5"` | Cyan |
| `"6"` | Purple |

Preset values are intentionally undefined in the spec — each app uses its
own brand palette. Don't depend on exact RGB values.

## Z-Order

Nodes render in array order: index 0 is the bottom layer, last index is on
top. To bring a node to the front, move its object to the end of the
`nodes` array.

## Coordinate System

- Origin at `(0, 0)`; positive X extends right, positive Y extends down
- Negative coordinates are valid — the canvas is conceptually infinite
- `x`, `y` always refer to the **top-left corner** of the node
- All measurements are in pixels

## Validation Invariants

A `.canvas` file is well-formed when:

1. JSON parses without error
2. All `id` values are unique (across both nodes and edges)
3. Every `fromNode` and `toNode` references an existing node `id`
4. `type` is one of: `text`, `file`, `link`, `group`
5. Type-specific required fields are present
6. `fromSide` / `toSide` (if set) ∈ {top, right, bottom, left}
7. `fromEnd` / `toEnd` (if set) ∈ {none, arrow}
8. `color` (if set) is a valid preset or hex
9. `x`, `y`, `width`, `height` are integers

If any invariant fails, Obsidian may silently drop the malformed element or
refuse to open the file.

## Minimal Valid Examples

### Empty canvas

```json
{ "nodes": [], "edges": [] }
```

### One text node

```json
{
  "nodes": [
    {
      "id": "6f0ad84f44ce9c17",
      "type": "text",
      "x": 0, "y": 0, "width": 200, "height": 80,
      "text": "Hello"
    }
  ],
  "edges": []
}
```

### Two nodes connected by an arrow

```json
{
  "nodes": [
    {"id":"aaaaaaaaaaaaaaaa","type":"text","x":0,"y":0,
     "width":200,"height":80,"text":"A"},
    {"id":"bbbbbbbbbbbbbbbb","type":"text","x":300,"y":0,
     "width":200,"height":80,"text":"B"}
  ],
  "edges": [
    {"id":"cccccccccccccccc","fromNode":"aaaaaaaaaaaaaaaa",
     "toNode":"bbbbbbbbbbbbbbbb","toEnd":"arrow"}
  ]
}
```
