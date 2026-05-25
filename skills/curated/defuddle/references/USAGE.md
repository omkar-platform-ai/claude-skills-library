# Defuddle CLI Usage Reference

Defuddle extracts the main readable content from a web page and strips
navigation, ads, footers, and other clutter. Use it before piping page
content into the model — it cuts token usage by 60–90% on typical articles.

## Installation

```bash
npm install -g defuddle
```

Verify the install:

```bash
defuddle --version
```

## Command Forms

| Command | Output |
|---|---|
| `defuddle parse <url>` | Cleaned HTML (default) |
| `defuddle parse <url> --md` | Markdown (preferred for LLM input) |
| `defuddle parse <url> --json` | JSON with both HTML and Markdown |
| `defuddle parse <url> -p <name>` | A single metadata property |

## Saving Output

Use `-o` to write to a file instead of stdout:

```bash
defuddle parse https://example.com/article --md -o article.md
```

Pipe to clipboard on macOS:

```bash
defuddle parse https://example.com/article --md | pbcopy
```

## Metadata Properties

The `-p` flag returns a single property without the full body:

| Property | Description |
|---|---|
| `title` | Page title |
| `description` | Meta description |
| `author` | Article author when available |
| `date` | Publication date |
| `domain` | Source domain |
| `siteName` | Site name from OpenGraph |
| `wordCount` | Estimated word count |

Example:

```bash
defuddle parse https://example.com/article -p title
defuddle parse https://example.com/article -p wordCount
```

## When to Use Defuddle vs WebFetch

| Situation | Tool |
|---|---|
| Article, blog post, documentation page | Defuddle |
| News site with heavy ads/nav | Defuddle |
| Raw `.md` file on GitHub or similar | WebFetch |
| API response (JSON, XML) | WebFetch / curl |
| PDF or binary asset | Neither — use a parser |
| Page behind login or paywall | Neither — extraction will fail |

## Error Handling

Defuddle exits with non-zero on:

- Invalid URL
- Network failure (timeout, DNS error)
- Page returns non-2xx status
- Page has no extractable content (e.g., a single-page app rendered only by
  JavaScript that Defuddle's fetcher cannot execute)

Catch failures and fall back to WebFetch when the content is essential.

## Token Savings Estimate

On a typical news article (`~50KB` of HTML):

- Raw HTML via WebFetch: `~12,000` tokens
- Defuddle `--md` output: `~1,500–3,000` tokens

The exact savings depend on the page; expect 60–90% reduction for
content-heavy pages with standard layouts.
