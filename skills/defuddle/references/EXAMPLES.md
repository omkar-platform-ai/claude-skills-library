# Defuddle Usage Examples

Concrete patterns for common Defuddle workflows.

## Read an Article Before Summarizing

```bash
defuddle parse https://example.com/post --md -o /tmp/article.md
```

Then read `/tmp/article.md` with your model. Avoids dragging 10KB+ of nav
markup into the context window.

## Extract Just the Title for a Bookmark

```bash
defuddle parse https://example.com/post -p title
```

Returns the title as a single line — useful for scripting a bookmark or
citation list.

## Build a Reading List Index

```bash
for url in $(cat urls.txt); do
  title=$(defuddle parse "$url" -p title)
  echo "- [$title]($url)"
done > reading-list.md
```

Produces a Markdown list of titled links.

## Batch Convert URLs to Markdown Files

```bash
mkdir -p articles
while read -r url; do
  slug=$(echo "$url" | sed 's|^https\?://||; s|[/?&=]|-|g')
  defuddle parse "$url" --md -o "articles/${slug}.md"
done < urls.txt
```

Each URL becomes its own Markdown file with a slug derived from the URL.

## Get JSON for Programmatic Processing

```bash
defuddle parse https://example.com/post --json > post.json
```

JSON output contains both the cleaned HTML and the Markdown plus all
metadata. Parse with `jq`:

```bash
jq -r '.title, .author, .wordCount' post.json
```

## Compare Word Count Across Multiple Sources

```bash
for url in "$@"; do
  count=$(defuddle parse "$url" -p wordCount)
  printf '%6s words  %s\n' "$count" "$url"
done
```

Pipe-friendly summary of how much content lives behind each URL before you
choose which to read.

## Handle Errors Gracefully

```bash
if ! defuddle parse "$url" --md -o "$out"; then
  echo "Defuddle failed for $url, falling back to raw fetch" >&2
  curl -sL "$url" > "$out.html"
fi
```

Defuddle can't render JavaScript-only pages — fall back to a different
fetcher (or skip the URL) when extraction fails.

## Workflow: Research Brief

1. Collect URLs in `sources.txt`.
2. Run Defuddle on each, saving to `briefs/<slug>.md`.
3. Concatenate the briefs into a single context file.
4. Pass the context to the model with a synthesis prompt.

Each step is a single bash one-liner. Defuddle does the heavy lifting of
content cleaning so the model gets the signal, not the chrome.
