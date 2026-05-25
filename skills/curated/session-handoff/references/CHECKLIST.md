# Session Handoff Checklist

A pre-flight checklist to run through before emitting a handoff. Skipping
items here is the most common cause of a broken next-session pickup.

## Coverage Checklist

- [ ] Scanned the *full* conversation, not just the last few turns
- [ ] Listed every file created or modified this session (with absolute
      paths)
- [ ] Recorded every background process (shell ID + kill command)
- [ ] Recorded every dev server / port still bound
- [ ] Listed open git branches and worktrees with their state
- [ ] Captured every decision the user locked in, with the *why*
- [ ] Captured every decision *deferred*, with the blocker
- [ ] Noted any unresolved question the user asked or that you asked them
- [ ] Named the plan file (if a plan drove the session)
- [ ] Listed memory files written or updated
- [ ] Wrote verification commands the next agent can actually run
- [ ] Single "Pick up here" line, not a roadmap

## Structure Checklist

- [ ] Used the exact template — every section present, even if "none"
- [ ] Output is in chat only — no file written, no memory updated
- [ ] All paths are absolute
- [ ] No emojis, no hype, no retrospective language
- [ ] Tone matches an engineer handing off at end-of-shift
- [ ] Plan file (if any) listed *first* under "Key files"

## Anti-Pattern Checklist

Confirm none of these appear in the handoff:

- [ ] "Today we accomplished a lot" (no hype)
- [ ] "Let me summarize the last few messages" (it's not a recap)
- [ ] "Next time we should consider X, Y, Z" (one action, not a list)
- [ ] Relative paths anywhere
- [ ] Code blocks with embedded analysis (handoff is structured prose, not a
      diff)
- [ ] "I think the user wants..." (state what was *decided*, not what was
      inferred)
- [ ] Missing background process IDs when shells were started
- [ ] "Nothing to report" used to skip a section instead of writing "none"

## Source Priority When Compiling

When pulling state for the handoff, walk these sources in order:

1. **Plan files** referenced in the session (`~/.claude/plans/`)
2. **TodoWrite state** — in-progress and pending tasks
3. **Background shells** you spawned with `run_in_background`
4. **Files** you created or modified (you know what you touched)
5. **Memory files** you wrote or updated
6. **Unresolved questions** — yours to the user, theirs to you

Do *not* run `git log`, `Glob`, or filesystem audits to "rediscover" what
happened. If you didn't touch it this session, it doesn't belong in the
handoff.

## Verification Section Quality Bar

Each verification command should be:

- **Runnable** — copy-paste with no edits
- **Specific** — points at the change made this session, not the whole repo
- **Fast** — under 30 seconds where possible

Good: `pytest tests/billing/test_dedup.py -v` (targets the change)

Bad: `pytest` (re-runs the whole suite, slow and unfocused)

Good: `psql -c "SELECT COUNT(*) FROM webhook_events"`

Bad: "Check the database to make sure things look right" (not a command)
