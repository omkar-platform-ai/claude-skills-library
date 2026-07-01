# WealthSeva — Backend Engineering Conventions

Assign to: **shreya-backend-engineer**

---

## Project stack

FastAPI (Python 3.12) + Uvicorn. Working root: `$WEALTHSEVA_ROOT/backend/`.
All backend work stays inside `backend/` and `ai/` — never touch `frontend/` unless the ticket explicitly requires it.

## Directory layout (don't deviate)

```
backend/
  routers/      # one file per domain: chat.py, portfolio.py, risk.py, goals.py, insights.py, idbi.py
  services/     # claude_service.py, language_service.py, rag_service.py, risk_service.py
  models/
    schemas.py  # ALL Pydantic request/response models live here
  tests/        # one test file per router: test_chat.py, test_portfolio.py, etc.
  main.py       # FastAPI app, CORS, router registration, /health endpoint
ai/
  system_prompts/   # wealth_advisor_{lang}.md, risk_profiler.md
  rag/              # index_datasets.py
data/               # mock_index.json, sample_transactions.csv
```

## Required coding patterns

### IDBI response envelope
Every IDBI endpoint must wrap its payload:
```python
# Live call:
return {"data": response.json(), "source": "live"}
# Mock fallback:
return {"data": MOCK_DATA, "source": "mock"}
```
Gate on `IDBI_SANDBOX_BASE_URL` env var — empty = use mock.
Pattern is documented in `references/backend-patterns.md` line 157.

### Claude API calls
- Model: always `claude-sonnet-4-6`
- Timeout: always 10 seconds on every Anthropic call
- Missing key: if `ANTHROPIC_API_KEY` is absent, return a mock string — **never raise 500**
- History: trim to `MAX_HISTORY = 10` messages before sending to Claude

### Language service
- `detect_language()` must wrap `langdetect` in try/except — fall back to user's `preferred_language` on any error
- `get_system_prompt(lang)` reads from `ai/system_prompts/wealth_advisor_{lang}.md`
- `get_voice_id(lang)` returns from `VOICE_MAP` dict

### RAG service
`rag_service.retrieve_context()` must **never** propagate exceptions.
Catch all errors, log a warning, and `return ""`. RAG failure must be invisible to the caller.

### Structured JSON from Claude
When asking Claude to return JSON (portfolio analysis, goal plan):
```python
# Always include this in the prompt:
"Return ONLY valid JSON. No markdown, no explanation."
```
Parse the response and validate structure before returning.

## Testing gate

Run `pytest backend/tests/<relevant_test_file>.py -v` after every implementation.
**TASK_COMPLETE is only valid when all tests in the ticket's test file pass.**
Never mark done with skipped, xfailed, or errored tests.

## Commit convention

```
feat(<scope>): <short description>
# Examples:
feat(chat): add POST /api/chat with language routing and streaming
fix(idbi): wrap live API returns with source: live envelope
```
Always commit before posting TASK_COMPLETE.

## TASK_COMPLETE steps

When all criteria in the ticket are met and all tests pass:

**Step 1** — Commit and push:
```bash
git add -A
git commit -m "feat(<scope>): <short description> [WEA-XX]"
git push origin dev
```

**Step 2** — Post your completion comment:
```
TASK_COMPLETE
Tests passed: <list the test function names>
Commit: <hash> — <message>
Files changed: <list>
```
Use: `mcp__paperclip__add_issue_comment(issueId="<this-issue-id>", body="...")`

**Step 3** — Mark this issue as `done`:
```
mcp__paperclip__update_issue(issueId="<this-issue-id>", status="done")
```
The runtime will intercept, move the issue to `in_review`, and assign shreya-reviewer
automatically. You do not need to set `in_review` yourself.
