# WealthSeva — Frontend Engineering Conventions

Assign to: **shreya-frontend-engineer**

---

## Project stack

Next.js 14 (App Router) + TypeScript + Tailwind CSS + next-intl.
Working root: `$WEALTHSEVA_ROOT/frontend/`.
Never touch `backend/` or `ai/` unless the ticket explicitly requires it.

## Directory layout (don't deviate)

```
frontend/
  app/
    [locale]/             # locale-aware layout
      advisor/page.tsx    # AvatarChat page
      dashboard/page.tsx  # Dashboard
      demo/page.tsx       # Scripted judge demo
      (auth)/page.tsx     # Onboarding / RiskQuiz
  components/
    AvatarChat.tsx
    LanguageSwitcher.tsx
    RiskQuiz.tsx
    PortfolioCard.tsx
    GoalPlanner.tsx
  messages/               # en.json hi.json mr.json ta.json bn.json
  lib/
    format.ts             # formatINR() and other utilities
```

## Required coding patterns

### i18n — never hardcode user-visible strings
Always use `useTranslations()`:
```tsx
const t = useTranslations('advisor')
// then: t('welcomeMessage'), t('sendButton'), etc.
```
Namespaces: `onboarding` · `risk` · `advisor` · `dashboard` · `goals` · `portfolio` · `nav` · `common`

### Indian number formatting
Use `formatINR()` from `frontend/lib/format.ts` for every monetary display:
- `formatINR(5432)` → `"₹5,432"`
- `formatINR(1050000)` → `"₹10.5 लाख"`
- `formatINR(50000000)` → `"₹5 करोड़"`
Labels (लाख/crore) must be locale-aware (active locale drives which script).

### Charts — Recharts only
Use `PieChart`, `BarChart`, or `LineChart` from Recharts. No other chart library.
Always wrap in `<ResponsiveContainer width="100%" height={300}>`.

### Streaming responses
Chat responses must stream word-by-word using the Fetch Streams API or EventSource — never buffer and display all at once.

### Language switcher rules
- Switch must complete in **under 2 seconds** — if `router.push` causes a full-page reload, switch to client-side locale update
- On switch: clear chat history, show `advisor.welcomeMessage` in the **new** language
- Toast after switch must be in the **new** language (not the old one)
- Show a 2-second fixed-position toast (`div`, no library)

### Backend calls
Always use `process.env.NEXT_PUBLIC_BACKEND_URL` as the base URL — never hardcode `localhost:8000`.

### Mobile-first layout (375px baseline)
- No fixed widths on cards — use `w-full`
- Default Tailwind classes = mobile; use `md:` for desktop overrides
- Hamburger navbar on mobile: `useState` open/close, no external library
- Test every new page at 375×667 (iPhone SE) before marking done

### Error boundaries
Wrap every `[locale]/*/page.tsx` in an error boundary that shows:
`common.shreya_break` message (from i18n) on crash — never show a raw stack trace.

### Demo mode
Pages must check for `?demo=true` query param and skip real API calls in favour of hard-coded constants when in demo mode.

## Build gate

Run both before TASK_COMPLETE — both must pass clean:
```bash
npm run type-check   # zero TypeScript errors
npm run lint         # zero lint errors
```
A broken build blocks the entire team.

## TASK_COMPLETE steps

When all criteria in the ticket are met and the build gate passes:

**Step 1** — Commit and push:
```bash
git add -A
git commit -m "feat(<scope>): <short description> [WEA-XX]"
git push origin dev
```

**Step 2** — Post your completion comment:
```
TASK_COMPLETE
Build: type-check ✓  lint ✓
Manual tests passed:
  - <describe what you clicked/tested>
  - Language switch in <Xs> (must be <2s)
Files changed: <list>
Commit: <hash>
```
Use: `mcp__paperclip__add_issue_comment(issueId="<this-issue-id>", body="...")`

**Step 3** — Mark this issue as `done`:
```
mcp__paperclip__update_issue(issueId="<this-issue-id>", status="done")
```
The runtime will intercept, move the issue to `in_review`, and assign shreya-reviewer
automatically. You do not need to set `in_review` yourself.
