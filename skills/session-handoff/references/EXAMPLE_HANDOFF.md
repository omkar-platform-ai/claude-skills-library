# Example: A Good Session Handoff

A reference example showing the structure and tone of a well-formed handoff.

The next agent should be able to read this and pick up the work cold,
without needing to scan prior conversation history.

## Annotated Sample

```text
# Session Handoff — Migrate billing webhook to idempotent handler

## Where it started
User flagged duplicate Stripe webhook charges in production. Goal: rewrite
the handler so retries are safe, then backfill missing webhook events from
the last 7 days. Constraint: cannot drop or replay events outside a
maintenance window.

## Decisions locked + what shipped
- Idempotency key: `stripe_event.id` stored in `webhook_events` table —
  /Users/me/repo/billing/handlers/stripe.py:42
- Deduplication uses Postgres `INSERT ... ON CONFLICT DO NOTHING` (not
  Redis) — durable, no extra infra — /Users/me/repo/billing/dedup.py
- Added integration test against a real Postgres container, not mocked —
  /Users/me/repo/tests/integration/test_stripe_dedup.py
- Deferred: backfill script. Scaffolded but not run — needs prod DB
  credentials.

## Key files for next session
- `/Users/me/repo/billing/handlers/stripe.py` — entry point, read first
- `/Users/me/repo/billing/dedup.py` — dedup helper, contains the unique
  index migration
- `/Users/me/repo/migrations/0042_webhook_events.sql` — new table; not yet
  applied to prod
- Plan file: `/Users/me/.claude/plans/2026-05-stripe-dedup.md`

## Running state
- Background processes: shell 7c4 — `docker compose up postgres` for tests.
  Kill: `kill $(lsof -ti:5432)`
- Dev servers / ports: none
- Open worktrees / branches: `fix/stripe-dedup` (3 commits ahead of main,
  not pushed)

## Verification — how to confirm things still work
- `pytest tests/integration/test_stripe_dedup.py -v` — all 6 tests pass
- `psql -h localhost -U postgres -c '\d webhook_events'` — table exists
  with unique index on `stripe_event_id`
- `git log --oneline main..fix/stripe-dedup` — should show 3 commits

## Deferred + open questions
- Deferred: run backfill against prod — needs ops to provide credentials
  and a maintenance window
- Open: should we alert on duplicate-attempt count, or silently drop?
  Asked in #billing-eng, no answer yet

## Pick up here
Push `fix/stripe-dedup` to GitHub and open a PR. Migration runs as part of
the PR's deploy workflow — verify the staging deploy applies it before
merging.
```

## What Makes This Good

- **Concrete paths.** Every file reference is absolute. The next agent can
  open them without guessing.
- **Why captured alongside what.** Each decision says *why* (durable vs.
  extra infra; mocked vs. real Postgres).
- **Running state surfaced.** Background shell ID `7c4` is recorded with a
  kill command — without it, the next agent can't shut down the test DB.
- **Deferrals named, not hidden.** Backfill script is explicitly deferred
  with the blocker. Future agent doesn't waste time looking for it.
- **No retrospective.** No "what went well" — just facts.
- **One "Pick up here" action.** Not a roadmap, just the single next move.

## What Would Make It Bad

- "Worked on the billing thing today" (vague)
- "Made some changes to fix the bug" (no files, no decisions)
- Relative paths (`./handlers/stripe.py`)
- Omitting "Running state" because nothing seemed to be running
- Listing every commit in the session instead of decisions
- Recommending three different next steps — the next agent decides
