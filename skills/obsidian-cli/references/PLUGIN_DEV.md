# Obsidian Plugin & Theme Development Reference

The Obsidian CLI exposes a `dev:` namespace and a `plugin:` namespace that
together support a tight edit-reload-verify loop for plugin and theme
development.

## Edit-Reload-Verify Loop

1. **Edit** plugin source (`main.ts`, `styles.css`, etc.).
2. **Build** if you use a bundler (`npm run build`, `esbuild`, etc.).
3. **Reload** the plugin in the running Obsidian instance:

   ```bash
   obsidian plugin:reload id=my-plugin
   ```

4. **Check for errors** raised during reload or runtime:

   ```bash
   obsidian dev:errors
   ```

5. **Verify visually** with a screenshot or DOM inspection:

   ```bash
   obsidian dev:screenshot path=screenshot.png
   obsidian dev:dom selector=".workspace-leaf" text
   ```

6. **Inspect logs** at the desired level:

   ```bash
   obsidian dev:console level=error
   ```

If errors appear, fix and return to step 1. Never publish a plugin without a
clean `dev:errors` and `dev:console level=error` pass.

## Plugin Lifecycle Commands

| Command | What It Does |
|---|---|
| `obsidian plugin:list` | All installed plugins with status |
| `obsidian plugin:enable id=X` | Enable a plugin |
| `obsidian plugin:disable id=X` | Disable a plugin |
| `obsidian plugin:reload id=X` | Disable + enable (hot reload) |
| `obsidian plugin:settings id=X` | Read plugin settings JSON |

## Theme Commands

| Command | What It Does |
|---|---|
| `obsidian theme:list` | All installed themes |
| `obsidian theme:set name="X"` | Switch to theme `X` |
| `obsidian theme:reload` | Reload the active theme's CSS |

## Visual Verification

```bash
obsidian dev:screenshot path=before.png
# ... make change, reload ...
obsidian dev:screenshot path=after.png
```

Diff the two screenshots externally to confirm the visual change matches
intent.

## DOM Inspection

| Command | What It Does |
|---|---|
| `obsidian dev:dom selector=".cm-editor"` | Outer HTML of matched element |
| `obsidian dev:dom selector=".cm-editor" text` | Text content only |
| `obsidian dev:dom selector=".cm-editor" attrs` | Attributes as JSON |
| `obsidian dev:css selector=".x" prop=color` | Computed CSS value |

Use CSS selectors exactly as you would in browser devtools.

## JavaScript Eval

Run code in Obsidian's app context (full `app` global available):

```bash
obsidian eval code="app.vault.getFiles().length"
obsidian eval code="app.workspace.getActiveFile()?.path"
```

Wrap multi-statement code in an IIFE:

```bash
obsidian eval code="(() => { const f = app.vault.getFiles(); return f.filter(x => x.extension === 'md').length; })()"
```

## Mobile Emulation

```bash
obsidian dev:mobile on
obsidian dev:mobile off
```

Toggles mobile layout in the desktop app — useful for verifying responsive
behavior without an actual device.

## CDP / Debugger

Advanced commands expose Chrome DevTools Protocol. Run `obsidian help` for
the full list. Common entry points:

```bash
obsidian dev:cdp method=Runtime.evaluate params='{"expression":"1+1"}'
obsidian dev:debug:break file=main.js line=42
```

Treat these as an escape hatch — prefer the higher-level `dev:` commands
when they exist.

## Common Pitfalls

- **Forgetting to rebuild before reload.** `plugin:reload` re-runs the
  installed JS bundle; if you skip the build step you'll reload the previous
  version.
- **Stale CSS.** Theme CSS may need `theme:reload` (not just plugin reload).
- **Vault context.** When multiple vaults are open, prefix with
  `vault="X"` or the CLI may target the wrong instance.
- **Headless mode.** Many `dev:` commands require an actual running window —
  they won't work if Obsidian is closed.
