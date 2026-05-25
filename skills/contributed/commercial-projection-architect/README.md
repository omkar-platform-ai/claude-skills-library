# commercial-projection-architect

Build executive-ready commercial projections and investment justifications for
new platforms, SaaS tools, infrastructure capabilities, and engineering
initiatives. Combines assumption mapping, financial modelling, risk
quantification, and a soft-savings framework.

## When it triggers

Use this skill when the user asks for:

- A business case, ROI model, or commercial justification
- A 3-year financial projection for a new tool, platform, or initiative
- Pushback on (or defence of) an existing case challenged by finance
- Quantifying hard vs soft savings on an internal investment
- Investment committee or steering group briefing material

## Inputs it expects

- Initial investment (build cost) and ongoing run cost
- Affected population (e.g., engineers, teams, customers)
- Baseline cost or process being replaced (or a flag that it's unknown)
- Audience for the output (CFO, steering committee, technical leadership)

## Output

- 3-year financial table (investment, run, hard savings, soft savings, net)
- Named assumptions with sensitivity flags
- Payback period and ROI
- Executive summary suitable for a leadership audience
- Risk register tied to the model, not generic disclaimers

## Files

- `SKILL.md` — Claude instructions
- `metadata.yaml` — version, author, status, tags
- `evals/evals.json` — 3 test cases (easy/medium/hard)
