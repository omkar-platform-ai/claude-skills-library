# WealthSeva — Utility Engineering Conventions

Assign to: **shreya-utility-engineer**

---

## Scope

You handle: i18n translation files, AI system prompts, documentation, submission assets, test scaffolding, and security checks.
Do **not** touch `backend/routers/`, `backend/services/`, or `frontend/components/` unless the ticket explicitly says to.

## Five supported languages — always complete the full set

Never create or edit a translation for one language without completing all five:

| Code | Language | Script |
|------|----------|--------|
| `en` | English | Latin |
| `hi` | Hindi | Devanagari |
| `mr` | Marathi | Devanagari |
| `ta` | Tamil | Tamil script |
| `bn` | Bengali | Bengali script |

## i18n files (`frontend/messages/*.json`)

### Required namespaces and keys
Every file must contain ALL keys across these namespaces:
`onboarding` · `risk` · `advisor` · `dashboard` · `goals` · `portfolio` · `nav` · `common`

`en.json` is the source of truth — no key present in `en.json` may be missing from any other locale file.

### Hard-coded welcome messages (use exactly these)
```json
"en": "Hello! I'm Shreya, your IDBI wealth advisor. How can I help you today?"
"hi": "नमस्ते! मैं श्रेया हूं, आपकी IDBI वेल्थ एडवाइज़र। आज मैं आपकी कैसे मदद कर सकती हूं?"
"mr": "नमस्कार! मी श्रेया आहे, तुमची IDBI वेल्थ अॅडव्हायझर. आज मी तुम्हाला कशी मदत करू शकते?"
"ta": "வணக்கம்! நான் ஸ்ரேயா, உங்கள் IDBI செல்வ ஆலோசகர். இன்று நான் உங்களுக்கு எப்படி உதவலாம்?"
"bn": "নমস্কার! আমি শ্রেয়া, আপনার IDBI ওয়েলথ অ্যাডভাইজার। আজ আমি আপনাকে কীভাবে সাহায্য করতে পারি?"
```

### Verification
```bash
npm run dev
# Zero next-intl missing-key warnings in console = pass
```

## System prompts (`ai/system_prompts/`)

### `wealth_advisor_{lang}.md` — required sections (all 8 must be present)
1. **Identity** — "You are Shreya, an expert wealth advisor for IDBI Bank."
2. **Language instruction** — always respond in [language], never mix languages
3. **Tone** — simple, conversational, avoid jargon
4. **Numerals** — Indian number system (लाख/lakh, करोड़/crore)
5. **Length** — 3-4 sentences unless user asks for detail
6. **Grounding** — reference IDBI account data when using it
7. **Constraints** — no specific stock tickers; focus on fund categories and SIP amounts
8. **Return assumptions** — equity SIP ~12% CAGR, debt ~7%, FD ~6.5%

### `risk_profiler.md`
Instructions for scoring the 5-question quiz and returning a 1-sentence profile explanation in the user's language.

### Verification
```python
python3 -c "
from backend.services.language_service import get_system_prompt, Language
for lang in Language:
    p = get_system_prompt(lang)
    assert len(p) > 100, f'{lang} prompt too short'
    print(f'{lang}: OK ({len(p)} chars)')
"
```
All 5 must print OK.

## Security check (mandatory before every TASK_COMPLETE)

Run this from the repo root:
```bash
grep -r "ANTHROPIC_API_KEY=sk\|sk-ant-\|hf_\|PINECONE_API_KEY=pc-" \
  --include="*.py" --include="*.ts" --include="*.json" --include="*.md" .
```
**Output must be empty.** If any secret is found: stop immediately, do not mark TASK_COMPLETE, post a comment flagging it to the board. The secret must be rotated before the ticket can close.

## Documentation style

- `docs/solution_document.md` — prose only, no bullet points, 800-1,000 words
- `demo/demo_checklist.md` — numbered list, exactly 20 items, imperative phrasing
- `README.md` — replace all `your-username` and `your-ec2-ip` placeholders with actual values before committing
- `.env.example` — must list every env var used anywhere in the codebase, with a comment explaining each

## TASK_COMPLETE steps

When all criteria in the ticket are met and verification passes:

**Step 1** — Commit and push:
```bash
git add -A
git commit -m "feat(<scope>): <short description> [WEA-XX]"
git push origin dev
```

**Step 2** — Set this issue to `in_review` — **not** `done`:
```
mcp__paperclip__update_issue(issueId="WEA-XX", status="in_review")
```
Do NOT mark your own issue as `done`. shreya-reviewer closes it to `done` after approving.

**Step 3** — Post this as your final comment on the issue:
```
TASK_COMPLETE
Files created/modified: <list>
Verification output:
  <paste the full output of the verification command>
Security scan: clean ✓
Setting to in_review for code review.
```
