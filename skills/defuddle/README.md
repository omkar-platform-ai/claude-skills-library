# Defuddle Skill

Extract clean markdown content from web pages using the Defuddle CLI.
Removes navigation, ads, and clutter so the model sees the signal, not the
chrome — typically saving 60–90% of tokens vs. raw HTML.

## Skill Structure

```text
defuddle/
├── SKILL.md
├── README.md
└── references/
    ├── USAGE.md     ← CLI flags, metadata properties, error handling
    └── EXAMPLES.md  ← Common workflows and bash patterns
```

## Prerequisites

```bash
npm install -g defuddle
```

## How to Trigger

This skill activates when you provide a URL to read or analyze:

- "Read this article: `https://example.com/post`"
- "Summarize this blog post"
- "Pull the documentation at this URL"

Defuddle is preferred over `WebFetch` for any standard web page. Skip
Defuddle for raw `.md` URLs — use `WebFetch` directly there.

## What You Get

Clean Markdown output via:

```bash
defuddle parse <url> --md
```

Plus convenience flags for metadata extraction (title, author, word count)
and JSON output for programmatic processing.
