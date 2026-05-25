# executive-deck-specialist

Turn any document, PDF, report, or topic into a consultant-grade PowerPoint
deck with speaker notes, delivery coaching, and an optional LinkedIn carousel.
Uses MECE logic, the Pyramid Principle, the SCQA framework, and data
visualisation.

## When it triggers

- "Build a deck", "turn this into a presentation", "create slides"
- McKinsey-style strategy decks, executive briefings, ghost decks
- Document-to-deck (PDF, doc, report) and topic-to-deck (prompt-only) modes
- Audience adaptation (board, exec, technical, customer)

## Inputs it expects

- A source document OR a topic prompt
- Target audience and seniority (board, exec, eng all-hands, sales)
- Slide count / time budget if known
- Any specific framing constraints (e.g., "CFO is sceptical of soft numbers")

## Output

- Slide-by-slide outline with takeaway-style slide titles
- SCQA opening, Pyramid Principle structure, MECE topic decomposition
- Speaker notes written for verbal delivery, not as on-slide transcript
- Optional LinkedIn carousel version

## Files

- `SKILL.md` — Claude instructions (The Architect persona, six-phase method)
- `metadata.yaml`
- `evals/evals.json`
