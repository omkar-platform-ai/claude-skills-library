# Conventional Commits Specification

The Conventional Commits specification is a lightweight convention on top of
commit messages. It provides a standardized way to communicate intent in
commit history and enables automated tooling.

## Structure

```text
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

## Allowed Types

| Type | Purpose | SemVer Bump |
|---|---|---|
| `feat` | New user-visible feature | MINOR |
| `fix` | Bug fix | PATCH |
| `perf` | Performance improvement | PATCH |
| `refactor` | Code change that neither fixes a bug nor adds a feature | None |
| `docs` | Documentation only | None |
| `test` | Add or correct tests | None |
| `build` | Build system or external dependency change | None |
| `ci` | CI configuration change | None |
| `chore` | Maintenance, tooling, non-code change | None |
| `revert` | Revert a previous commit | Depends |

## Scope Guidance

- Scope identifies the affected subsystem, module, or package
- Use kebab-case nouns (`api`, `auth`, `cloud-run`, `terraform`)
- Omit scope when change spans many modules or is repo-wide
- Never invent scopes that don't exist in the codebase

## Description Rules

- Imperative mood ("add", "fix", "remove" — not "added", "fixes", "removing")
- Lowercase first letter (unless proper noun)
- No trailing period
- Hard limit: 72 characters total subject line
- Soft target: 50 characters

## Breaking Changes

Two ways to signal a breaking change:

1. **Footer**: `BREAKING CHANGE: <description>` (preferred)
2. **Bang suffix**: `feat(api)!: remove deprecated endpoint`

Both trigger a MAJOR version bump in SemVer.

## Body and Footer

- Body explains *why*, not *what* — the diff already shows what
- Separate subject from body with one blank line
- Footers follow git trailer format: `Token: Value`
- Common footers: `BREAKING CHANGE:`, `Refs:`, `Closes:`

## Forbidden in This Repository

- `Co-authored-by:` trailers
- `Signed-off-by:` trailers
- `Generated-by:` trailers
- Any AI attribution (Claude, ChatGPT, Copilot, etc.)
- Emojis in subject lines
- Uppercase commit types

## Reference Examples

### Single-line subject

```text
feat(billing): add stripe webhook retry handler
```

### With body

```text
fix(auth): prevent session fixation on login

The previous flow reused the pre-auth session ID after successful login,
allowing an attacker to hijack the session if they could plant a known SID
before the user authenticated. Rotate the session on credential validation.
```

### With breaking change footer

```text
refactor(api): collapse v1 and v2 user endpoints

BREAKING CHANGE: `/v1/users` now redirects to `/v2/users`. Clients that
depend on v1 response shape must migrate to the v2 schema documented in
docs/api/users.md.
```

## Tooling Compatibility

Conventional Commits messages must parse cleanly with:

- `commitlint` (Node.js validation)
- `semantic-release` (automated release pipeline)
- `release-please` (Google's release automation)
- `conventional-changelog` (changelog generator)
- `git-cliff` (Rust-based changelog generator)

## Specification Source

The canonical specification is maintained at
<https://www.conventionalcommits.org/en/v1.0.0/>.
