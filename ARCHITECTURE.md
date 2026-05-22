# Architecture & Design Philosophy

The Claude Skills Library is built on principles of clarity, modularity, and institutional quality. This document outlines the design philosophy, patterns, and standards that all skills should follow.

---

## 🎯 Core Principles

### 1. Clarity Over Cleverness
Every word in a skill must earn its place. Remove filler, hedging, and ambiguity.

**Bad:** "It would be helpful if you could perhaps consider analyzing this fund..."
**Good:** "Analyze the fund across these 10 dimensions: [list]"

### 2. Role + Context + Task + Format + Constraints (5 Pillars)
Every skill must define all five:
- **Role:** Who is Claude? What expertise?
- **Context:** What background or situation is relevant?
- **Task:** What exactly must be done? (imperative)
- **Format:** What should the output look like?
- **Constraints:** What must NOT happen?

### 3. Imperative Voice
Skills are instructions, not requests. Use commanding language.

**Bad:** "It would be nice if you could..."
**Good:** "Generate / Analyze / Write / Create / Extract / Compare..."

### 4. Specificity Beats Generality
The more specific the prompt, the more accurate the output.

**Generic:** "Write about investing."
**Specific:** "Write a portfolio recommendation for a 35-year-old moderate investor in India with ₹50k/month SIP budget, 15-year horizon, focusing on tax-efficient asset allocation with 8 specific fund picks ranked by suitability."

### 5. Constraints Are As Important As Instructions
Tell Claude what NOT to do. This prevents hallucination and scope creep.

```
Do not:
- Recommend funds based solely on recent 1-3 year returns
- Suggest >8 instruments total
- Use vague language ("might," "could," "perhaps")
- Ignore tax implications for the specific investor profile
```

### 6. Show the Output Shape
Describe or demonstrate exact output structure (XML, tables, numbered lists, JSON).

### 7. Explicit Quality Gates
Before delivering output, verify criteria have been met:
- All required metrics assessed
- No anti-patterns present
- Constraints respected
- Output format followed

---

## 🏗️ Skill Anatomy

Every skill has three layers:

### Layer 1: SKILL.md (Required)
The instructions Claude reads. Contains:
- Metadata (name, description)
- Role definition
- Task specification
- Output format
- Constraints
- Quality gates
- Behavioral rules

**Must be self-contained:** A user could apply the skill without reading references.

### Layer 2: References (Required)
Domain-specific knowledge files in `references/`:
- Frameworks, methodologies, best practices
- Evaluation criteria and metrics
- Red flags and edge cases
- Real-world examples
- Reference data tables

**Lazy-loaded:** Claude reads only relevant files based on detected context.

### Layer 3: Evaluations (Recommended)
Test cases in `evals/eval_set.json`:
- Real user inputs
- Success criteria
- Difficulty classification
- Category tags

**Enables automated testing** and quality gates.

---

## 📐 SKILL.md Template

```yaml
---
name: skill-name
description: >
  [1-2 sentences: what it does]
  [When to trigger: specific user phrases/contexts]
  [Domain/use cases: be pushy about when to use]
---

# Skill Instructions

<role>
[1 paragraph: expertise, background, persona]
</role>

<constraints>
[Bulleted list: what NOT to do, hard rules]
</constraints>

<task>
[2-3 paragraphs: specific instruction, steps if multi-step]
</task>

<output_format>
[Exact format specification, examples, structure]
</output_format>

<quality_gates>
[Checklist: what must be true before delivery]
</quality_gates>

<tone>
[Describe voice: analytical, creative, empathetic, etc.]
</tone>
```

### Name Field
- Kebab-case (lowercase, hyphens, no spaces)
- Descriptive, not cute
- Examples: `investment-analyst`, `code-reviewer`, `fitness-advisor`

### Description Field
**Most important for triggering.** Include:
1. What the skill does (verb + object)
2. Specific contexts/triggers ("whenever user mentions X, Y, Z")
3. Be "pushy" — tell Claude exactly when to use this

```yaml
description: >
  Institutional-grade investment analysis and portfolio recommendations
  for any financial instrument. Triggers on: analyze this stock,
  recommend mutual funds, build me a portfolio, review my investments,
  should I buy [instrument], evaluate this fund, crypto portfolio,
  compare these investments, asset allocation advice, investment
  horizon planning, and any request to analyze, evaluate, compare,
  or recommend any financial instrument or build/review any
  investment portfolio. Use this skill whenever the user mentions
  investing, instruments, funds, stocks, crypto, bonds, ETFs, SIPs,
  lump sum deployment, or portfolio construction — even if they don't
  use the words "analyze" or "recommend."
```

---

## 📚 References: Content Standards

Each reference file should:

### 1. Be Substantive (300+ words minimum)
Provide real value, not fillers or generic information.

### 2. Use Clear Structure
```markdown
# Domain Name — Reference Guide

## Topic 1
[Content, explanation, best practices]

### Subtopic 1.1
[Details, examples]

## Topic 2
[Red flags, edge cases, anti-patterns]

### Comparison Table
| Factor | Option A | Option B |
|---|---|---|
```

### 3. Include Frameworks & Methods
Not just facts — show HOW to evaluate/decide/analyze.

Example:
```markdown
## Fundamental Analysis Framework

**Valuation:**
- P/E ratio vs sector median
- EV/EBITDA vs peers
- PEG ratio (P/E ÷ earnings growth)

**Profitability:**
- ROE: >15% consistently preferred
- ROCE vs WACC

**Financial Health:**
- Debt/Equity ratio
- Interest coverage ratio
- Free Cash Flow trends
```

### 4. Document Red Flags
What should Claude avoid recommending? What are warning signs?

```markdown
## Red Flags — Avoid Stocks With:
- Negative FCF for 3+ years without clear path to profitability
- Excessive share dilution (>5% annual)
- Declining revenue with no turnaround thesis
- SEC investigation or restatement
- Debt/Equity >3x
```

### 5. Include Real Examples
Where possible, show application with real data.

```markdown
## Example: Tax-Loss Harvesting Strategy

Investor situation:
- Cost basis: ₹1,00,000
- Current value: ₹85,000
- Unrealized loss: ₹15,000

Strategy:
1. Sell losing position, realize loss
2. Immediately buy similar (not identical) fund
3. Offset loss against gains in other holdings
4. Result: Tax savings of ₹15,000 × 30% = ₹4,500
```

### 6. Cross-Reference Related Material
Link to other reference files: "See `debt-bonds.md` for duration matching strategy."

---

## ✅ Quality Rubric (5 Dimensions)

Every skill is scored on these dimensions. All must score 4+/5 to be accepted.

### 1. Clarity (Is every instruction unambiguous?)
**5:** Every word is necessary; zero confusion possible
**4:** Very clear; one reading is sufficient
**3:** Mostly clear; some re-reading needed
**2:** Ambiguous; multiple interpretations possible
**1:** Confusing; reader can't understand intent

**How to improve:**
- Remove hedging ("might," "could," "perhaps")
- Use imperative voice ("Create X" not "You could consider creating X")
- Define all acronyms on first use
- Break long sentences into short ones

### 2. Specificity (Is scope, format, audience defined?)
**5:** Highly specific; no generalization needed
**4:** Specific; clear boundaries on scope
**3:** Somewhat specific; could be more detailed
**2:** Vague; unclear what's in/out of scope
**1:** Generic; could apply to anything

**How to improve:**
- Name the audience: "for a 35-year-old Indian investor"
- Define boundaries: "cover equity only, not debt"
- Specify format: "JSON with these exact fields"
- Give examples: "e.g., SIP, lump sum, DCA"

### 3. Efficiency (Minimum tokens for maximum precision?)
**5:** Every token earns its place; densely written
**4:** Efficient; no obvious waste
**3:** Some verbosity but acceptable
**2:** Redundant phrases, examples, or structure
**1:** Bloated; half the content could be cut

**How to improve:**
- Remove filler ("In this skill, we will...")
- Cut obvious examples (assumed knowledge)
- Use tables instead of paragraphs where appropriate
- Reference external docs instead of embedding everything

### 4. Completeness (All 5 pillars present?)
**5:** Role, context, task, format, constraints all strong
**4:** All five present; at least 3 are strong
**3:** 4 of 5 present; some are weak
**2:** 3 of 5 present; major gaps
**1:** <3 pillars present

**How to check:**
- Role: "You are a [expertise] with [background]" ✓
- Context: "Given [situation/data/investor profile]" ✓
- Task: "Your task is to [imperative verb] [what]" ✓
- Format: "Return output as [structure]" ✓
- Constraints: "Do not [X], do not [Y]" ✓

### 5. Robustness (Handles edge cases? Prevents drift?)
**5:** Comprehensive constraints; addresses all foreseeable edge cases
**4:** Good constraints; handles most cases
**3:** Basic constraints; some gaps
**2:** Minimal constraints; easily drifts off-task
**1:** No constraints; hallucinates freely

**How to improve:**
- Add specific "do not" rules: "Do not recommend more than 8 funds"
- Handle edge cases: "If investor hasn't provided tax bracket, assume 20%"
- Define success: "Output must include X, Y, Z"
- Set boundaries: "Avoid funds with <₹500 Cr AUM"

---

## 🎭 Tone & Voice

Skills should sound:
- **Analytical** — evidence-driven, quantified
- **Confident** — definitive (not hedging)
- **Practical** — actionable (not theoretical)
- **Professional** — institutional-grade (not casual)
- **Clear** — no jargon unless domain-specific

**Good tone example:**
"This fund underperformed the benchmark in 7 of the past 10 years, ranking in the 35th percentile for 5-year rolling returns. The higher expense ratio (1.2% vs 0.9% category median) is not justified by outperformance. Avoid."

**Bad tone example:**
"This fund, um, kind of underperformed the benchmark, and you might want to consider the expense ratio, which could be higher, so maybe it's not the best choice?"

---

## 🔐 Constraint Patterns

Effective constraints follow these patterns:

### Pattern 1: Scope Limitation
```
- Do not recommend more than 8 instruments total
- Do not analyze non-equity components unless relevant to asset allocation
- Do not suggest changes without quantified rationale
```

### Pattern 2: Quality Gates
```
- Do not recommend instruments with <3 years track record
- Do not recommend funds with AUM <₹500 Cr
- Do not include expense ratio in recommendation without comparing to category median
```

### Pattern 3: Behavior Enforcement
```
- Never use vague language ("might," "could," "perhaps")
- Always quantify claims with data, percentiles, or historical examples
- Always specify tax implications for the investor's jurisdiction
```

### Pattern 4: Anti-Hallucination
```
- Do not invent fund names, historical returns, or metrics not verified
- Do not claim data beyond current date
- Do not recommend unknown/unverified instruments
```

---

## 📊 Output Format Specification

Always define exact structure:

### Option 1: Markdown Structure
```
# Section 1
[Content]

## Subsection 1.1
[Content]

# Section 2
[Content with table]
| Col1 | Col2 |
|---|---|
| Data | Data |
```

### Option 2: JSON Schema
```json
{
  "recommendation": {
    "fund_name": "string",
    "category": "string",
    "risk_level": "Low|Moderate|High",
    "allocation_percentage": "number (0-100)",
    "rationale": "string"
  }
}
```

### Option 3: XML Tags
```xml
<recommendation>
  <fund_name>...</fund_name>
  <category>...</category>
  <risk_level>...</risk_level>
</recommendation>
```

**Rule:** Show exactly what the output should look like, including field names, types, and examples.

---

## 🧪 Evaluation Test Design

Good evals are:

### 1. Realistic
Real inputs users would actually ask: "Analyze HDFC Balanced for a 35-year-old..."
NOT: "Rate this mutual fund on a scale of 1-10"

### 2. Difficulty-Stratified
```json
{
  "easy": "Basic single-instrument analysis with complete investor profile",
  "medium": "Multi-instrument comparison with incomplete data",
  "hard": "Edge case: conflicting goals, unusual constraints"
}
```

### 3. Specific Success Criteria
```json
"expected_output_criteria": [
  "Addresses all 10 evaluation dimensions",
  "Includes 3+ funds ranked by suitability",
  "Specifies exact tax treatment for India",
  "Acknowledges conflicting goals",
  "Avoids recommending unsuitable instruments"
]
```

NOT vague: "output is good" or "analysis is comprehensive"

### 4. Edge Cases Included
- Conflicting goals (need returns + liquidity)
- Incomplete data (missing tax bracket, income, etc.)
- Unusual constraints (short horizon, unique industry)
- Stress scenarios (market crash, rate hike)

---

## 🚫 Anti-Patterns to Avoid

### In SKILL.md

❌ Generic role: "You are a helpful assistant"
✅ Specific role: "You are a Senior Investment Research Analyst with 15+ years analyzing the Indian mutual fund market"

❌ Vague task: "Analyze the investment"
✅ Specific task: "Analyze these 3 funds across 10 dimensions: mandate fit, risk metrics, return consistency, risk-adjusted returns, management quality, operational health, tax efficiency, peer comparison, portfolio fit, market cycle suitability"

❌ No constraints: (anything goes)
✅ Strong constraints: "Do not recommend funds with <3Y track record, <₹500 Cr AUM, or recent manager changes"

❌ Implied format: (hope Claude guesses)
✅ Explicit format: "Return as markdown with sections: Profile Summary, Asset Allocation, Fund Recommendations (ranked), Avoided Funds, Final Portfolio, Additional Insights"

### In References

❌ Generic information: "Mutual funds have different types"
✅ Specific frameworks: "SEBI categorization rules (post-2018), each category's mandate, typical return ranges, appropriate investor profiles, red flags"

❌ Vague guidance: "Choose funds carefully"
✅ Specific criteria: "Prefer funds ranked in top quartile (25th percentile) on 3Y/5Y rolling returns vs category, with AUM >₹1,000 Cr, consistent fund manager (no change in past 2Y)"

❌ No edge cases: (assume happy path)
✅ Documented edge cases: "Red flags: AUM >₹30,000 Cr for mid/small cap (capacity constraint), manager changed in past 12M, returns dominated by single hot year, etc."

### In Tone

❌ Hedging: "This fund might possibly be considered for your portfolio, if you're interested"
✅ Definitive: "Recommend this fund for: [specific investor profile]. Not suitable for: [profile]."

❌ Passive voice: "It has been recommended that X could be evaluated"
✅ Active voice: "Analyze X across these 10 dimensions: [list]"

---

## 🔄 Version Control & Evolution

Skills evolve. Track changes:

### Versioning
- Major (v1.0 → v2.0): Breaking changes to SKILL.md structure
- Minor (v1.0 → v1.1): New reference files, expanded evals
- Patch (v1.0 → v1.0.1): Bug fixes, clarifications

### Backwards Compatibility
- Maintain compatibility unless major version bump
- Deprecate features 1 version before removal
- Document migration path for users

### Reference Updates
Update references when:
- Market conditions change significantly
- New regulations implemented
- Best practices evolve
- Errors discovered

Test extensively before release.

---

## 📈 Maturity Levels

Track skill maturity with badges:

| Level | Requirements |
|---|---|
| **Experimental** 🔴 | Draft SKILL.md, <5 evals, 0 reviews |
| **Beta** 🟡 | Complete SKILL.md, 5+ evals passing, 1 review |
| **Stable** 🟢 | All above + 10+ passing evals, 2+ reviews, >50 uses |
| **Production** 🔵 | Stable + comprehensive docs, >200 uses, bug-free 30 days |

Display in skill README:
```markdown
![Status: Stable](https://img.shields.io/badge/status-stable-brightgreen)
```

---

## 🎯 Design Review Checklist

Before merging a skill PR:

- [ ] SKILL.md follows template structure
- [ ] Description is pushy about when to trigger
- [ ] All 5 pillars (role, context, task, format, constraints) strong
- [ ] References have substantive content (300+ words each)
- [ ] Evaluation evals are specific with clear success criteria
- [ ] No anti-patterns present (hedging, vague language, etc.)
- [ ] Quality scores 4+/5 on all dimensions
- [ ] README has examples of good inputs
- [ ] No duplicate of existing skill
- [ ] Passes all automated validation

---

This architecture ensures skills are clear, modular, maintainable, and high-quality.
