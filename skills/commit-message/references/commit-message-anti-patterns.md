# Commit Message Anti-Patterns

Common commit message mistakes that should be flagged and rewritten. Each
anti-pattern includes the bad form, why it fails, and the correct
replacement.

## Vague Summaries

| Bad | Why It Fails | Better |
|---|---|---|
| `update stuff` | Tells reviewer nothing | `feat(api): add rate limit headers` |
| `fix bug` | Which bug? | `fix(auth): reject empty bearer tokens` |
| `wip` | Not shippable | Squash before merging |
| `final fix` | History will repeat | Describe the actual fix |
| `changes` | Diff already shows changes | State the *intent* |
| `misc` | Hides real change | Pick the dominant change |

## Wrong Tense

The Conventional Commits spec mandates imperative mood. Past tense and
present continuous are both wrong.

- Bad: `fixed login bug` → Good: `fix login bug`
- Bad: `adding new endpoint` → Good: `add new endpoint`
- Bad: `fixes #123` → Good: `fix(api): resolve #123 timeout`

Mnemonic: the subject should complete the sentence "If applied, this commit
will ___".

## Wrong Type

- Using `fix` for a refactor with no bug → use `refactor`
- Using `feat` for a docs-only change → use `docs`
- Using `chore` for a user-visible feature → use `feat`
- Using `perf` for a refactor with no measured speedup → use `refactor`

## Scope Abuse

- Inventing scopes that don't match any module (e.g., `feat(misc)`)
- Using vendor names as scope when the change is internal
  (`fix(stripe)` for a refactor that doesn't touch Stripe)
- Using the file path as scope (`fix(src-utils-helpers-format-js)`)
- Mixing case: `feat(API)` instead of `feat(api)`

## Subject Line Hygiene

| Anti-pattern | Fix |
|---|---|
| Trailing period | Remove |
| Capitalized type (`Feat:`) | Lowercase |
| Subject > 72 chars | Move detail to body |
| Issue ref in subject | Move to footer (`Refs: #123`) |
| Emojis (`🐛 fix:`) | Remove |

## Forbidden Trailers

The following trailers must never be auto-added by tooling or AI:

- `Co-authored-by:` — implies the AI is a co-author
- `Signed-off-by:` — implies legal sign-off
- `Generated-by: <tool>` — adds noise
- `Reviewed-by:` (when the reviewer didn't actually review)
- Any "🤖 Generated with X" suffix

These violate enterprise governance and pollute `git log` output. Strip them
before committing.

## Breaking Change Mistakes

- Putting breaking-change details in the subject:
  `feat: BREAKING add new auth flow` ← wrong
- Using `BREAKING:` instead of `BREAKING CHANGE:` (token must match)
- Marking a non-breaking change as breaking (forces unnecessary MAJOR bump)
- Missing breaking marker on an actual API removal (silently breaks
  consumers)

## Multi-Change Commits

If one commit message tries to describe two unrelated changes, split the
commit. Bad form:

```text
feat(auth): add OAuth and fix billing webhook
```

Better:

```text
feat(auth): add OAuth provider
```

```text
fix(billing): retry stripe webhook on 5xx
```

When commits cannot be split (already merged), pick the dominant change and
mention the secondary one in the body.

## Body and Footer Mistakes

- No blank line between subject and body (parsers will treat body as
  continuation of subject)
- Footer keys with spaces (`Refs to: #123` — must be `Refs: #123`)
- Markdown formatting in the body (commits are plain text in `git log`)
- Linking to ephemeral resources (Slack threads, private wiki pages) that
  will rot

## Repository-Specific Smells

- Reverting a revert without explaining why
- "Fix typo" commits on merged code instead of amending the PR
- Force-pushed commit messages that no longer match the actual diff
- Hundred-character commit messages auto-generated from PR titles
