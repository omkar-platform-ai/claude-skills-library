# Session Handoff Skill

Produce a repeatable end-of-session summary so the user can `/clear` and
start a fresh agent without losing continuity. The summary is **chat-only**
and structured so the next agent can pick up cold.

## Skill Structure

```text
session-handoff/
├── SKILL.md
├── README.md
└── references/
    ├── EXAMPLE_HANDOFF.md   ← Annotated good-handoff example
    └── CHECKLIST.md         ← Pre-flight checklist for coverage and tone
```

## How to Trigger

Invoke naturally by saying things like:

- "Session handoff"
- "Wrap up session"
- "Hand off before I /clear"
- "Summarize before I clear"

The skill also self-invokes proactively if the user says they're about to
`/clear` without having run it yet.

## What You Get

A single chat message (no file written, no memory updated) using a fixed
template with these sections:

- Where it started
- Decisions locked + what shipped
- Key files for next session
- Running state (background processes, dev servers, branches)
- Verification commands
- Deferred + open questions
- Pick up here

The next agent should be able to read just the handoff and continue working
without re-reading prior conversation.
