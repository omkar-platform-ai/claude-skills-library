# Obsidian CLI Skill

Interact with a running Obsidian vault from the command line — read, create,
search, and manage notes, tasks, properties, tags, and daily notes. Also
supports the plugin/theme developer loop (reload, dev:errors, screenshots,
DOM/CSS inspection, JS eval).

## Skill Structure

```text
obsidian-cli/
├── SKILL.md
├── README.md
└── references/
    ├── COMMANDS.md    ← Common command reference (read, write, search, etc.)
    └── PLUGIN_DEV.md  ← Edit-reload-verify loop for plugin/theme development
```

## Prerequisites

- The `obsidian` CLI installed and on `PATH`
- Obsidian must be **running** — the CLI talks to a live instance

## How to Trigger

Invoke naturally by saying things like:

- "Read my note titled 'Sprint Planning'"
- "Append today's standup notes to the daily note"
- "Search the vault for 'OKR'"
- "Reload my custom Obsidian plugin and check for errors"
- "Take a screenshot of the workspace"

## What You Get

Shell commands you can run directly against your vault. The CLI returns
content to stdout (or to clipboard with `--copy`); use `silent` to avoid
opening modified files in the UI.

## Reference

- [Obsidian CLI docs](https://help.obsidian.md/cli)
