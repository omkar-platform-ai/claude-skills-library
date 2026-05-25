# Obsidian CLI Command Reference

A curated reference of the most common `obsidian` CLI commands. For the
complete list including developer-only commands, run `obsidian help` against
your installed version.

## Note Reading

| Command | What It Does |
|---|---|
| `obsidian read file="Name"` | Print the note's content |
| `obsidian read path="folder/x.md"` | Read by exact vault path |
| `obsidian read` | Read the currently active note |
| `obsidian preview file="Name"` | Render markdown to terminal |

## Note Writing

| Command | What It Does |
|---|---|
| `obsidian create name="X"` | Create note `X.md` at vault root |
| `obsidian create name="X" content="..."` | Create with body |
| `obsidian create name="X" template="T"` | Apply template `T` |
| `obsidian append file="X" content="..."` | Append to existing note |
| `obsidian prepend file="X" content="..."` | Insert at the top |
| `obsidian replace file="X" find="a" replace="b"` | In-place replace |
| `obsidian delete file="X"` | Move note to trash |

Useful flags: `silent` (don't open the file), `overwrite` (replace if
exists), `--copy` (copy command output to clipboard).

## Search

| Command | What It Does |
|---|---|
| `obsidian search query="text"` | Full-text search |
| `obsidian search query="..." limit=10` | Cap result count |
| `obsidian search query="..." total` | Return count only |
| `obsidian backlinks file="X"` | Notes that link to `X` |
| `obsidian forwardlinks file="X"` | Notes that `X` links to |

## Properties (Frontmatter)

| Command | What It Does |
|---|---|
| `obsidian property:get name="status" file="X"` | Read one property |
| `obsidian property:set name="status" value="done" file="X"` | Write one |
| `obsidian property:delete name="status" file="X"` | Remove property |
| `obsidian property:list file="X"` | List all properties on a note |

## Tags

| Command | What It Does |
|---|---|
| `obsidian tags` | All tags in vault |
| `obsidian tags sort=count counts` | Tags ordered by frequency |
| `obsidian tags file="X"` | Tags on a specific note |

## Daily Notes

| Command | What It Does |
|---|---|
| `obsidian daily:read` | Today's daily note |
| `obsidian daily:append content="..."` | Append to today's note |
| `obsidian daily:read date="2026-05-20"` | Specific past daily |

## Tasks

| Command | What It Does |
|---|---|
| `obsidian tasks` | All tasks across vault |
| `obsidian tasks daily todo` | Today's open tasks |
| `obsidian tasks file="X" done` | Completed tasks in note `X` |

## Vault Selection

When multiple vaults are open, the most recently focused vault is targeted
by default. Override with `vault=<name>` as the first parameter:

```bash
obsidian vault="Work Vault" search query="meeting notes"
```

## Common Flags

| Flag | Effect |
|---|---|
| `silent` | Don't open the affected file in Obsidian |
| `overwrite` | Replace existing file or property without prompting |
| `total` | Return result count instead of full results (list commands) |
| `--copy` | Copy the command's stdout to the system clipboard |
| `json` | Emit results as JSON instead of plain text (where supported) |
