# Contributing to Claude Skills Library

Thank you for your interest in contributing! This guide will walk you through the process of adding skills, improving documentation, or enhancing the library.

---

## 🎯 What You Can Contribute

- **New Skills** — Portfolio recommendations, fitness coaching, code reviews, etc.
- **Skill Improvements** — Better reference data, more test cases, expanded coverage
- **Documentation** — Guides, tutorials, examples
- **Tools & Scripts** — Validators, packagers, eval runners
- **Bug Reports & Fixes** — Issues, pull requests
- **Community** — Discussions, feedback, usage examples

---

## 📋 Before You Start

### Check Existing Skills
Browse `SKILLS_INDEX.md` and `skills/` directory to avoid duplicates.

### Check Open Issues
Look at GitHub Issues for:
- Skill requests others are already working on
- Planned improvements
- Known bugs

### Skill Proposal (for new skills)
Create a GitHub Issue using the **Skill Request** template:

```markdown
## Skill Proposal: [Skill Name]

**What:** Brief description of what the skill does

**Why:** Use case, problems it solves, target audience

**Scope:** What will it cover? (be specific)

**Examples:** 1-2 concrete inputs the skill should handle

**Related Skills:** Any existing skills this relates to?

**Domain Expertise:** Are you the right person to write this?
```

Wait for **maintainer approval** before investing time in implementation.

---

## ✅ Skill Quality Checklist

Before submitting a PR, ensure your skill meets ALL criteria:

### Structure
- [ ] Valid SKILL.md with `name` and `description` fields
- [ ] README.md in skill root
- [ ] At least 2 reference files in `references/`
- [ ] No syntax errors (YAML, JSON, Markdown)
- [ ] Passes `python tools/skill-validator.py`

### Content Quality (5-point scoring)
- [ ] **Clarity (4+/5)** — Every instruction unambiguous
- [ ] **Specificity (4+/5)** — Scope, format, audience clearly defined
- [ ] **Efficiency (4+/5)** — Dense and precise; no filler
- [ ] **Completeness (4+/5)** — All 5 pillars: role, context, task, format, constraints
- [ ] **Robustness (4+/5)** — Edge cases addressed; constraints prevent drift

### References
- [ ] Each reference file is >300 words of substantive content
- [ ] Clear headings and organization
- [ ] Tables, code examples where appropriate
- [ ] Red flags and edge cases documented

### Evaluations
- [ ] Minimum 5 test cases in `evals/eval_set.json`
- [ ] Mix of easy, medium, hard difficulty
- [ ] At least 1 edge case test
- [ ] All tests pass: `python tools/eval-runner.py evals/eval_set.json`

### Documentation
- [ ] README.md explains what skill does & when to use it
- [ ] Examples of good/bad inputs provided
- [ ] Related skills listed
- [ ] Any special instructions (dependencies, setup, etc.)

### No Anti-Patterns
- [ ] Vague language ("perhaps," "might," "could") removed
- [ ] Passive voice minimized
- [ ] Generic disclaimers replaced with specific analysis
- [ ] No hedging; recommendations are definitive

---

## 🚀 Step-by-Step: Creating a New Skill

### Step 1: Get Approval
Open a Skill Proposal issue. Wait for maintainer to give thumbs up.

### Step 2: Fork & Branch
```bash
git clone https://github.com/YOUR_USERNAME/claude-skills-library.git
cd claude-skills-library
git checkout -b add/my-skill-name
```

### Step 3: Create Skill Structure
```bash
./scripts/create-skill.sh my-skill-name
```

This creates:
```
skills/my-skill-name/
├── SKILL.md              (template)
├── README.md             (template)
├── references/
│   ├── domain1.md
│   ├── domain2.md
│   └── README.md
├── evals/
│   ├── eval_set.json
│   └── README.md
└── tests/
    └── test_references.py
```

### Step 4: Write SKILL.md
Follow the structure in `templates/SKILL.md.template`:

```yaml
---
name: my-skill
description: >
  [Clear trigger conditions + what it does]
---

# Skill Instructions

<role>
You are a [specific expert] with [background].
</role>

<constraints>
- Do not [X]
- Always [Y]
</constraints>

<task>
[Specific instruction with imperative verb]
</task>

<output_format>
[Exact format specification with examples]
</output_format>
```

**Key points:**
- Name must be kebab-case (no spaces, lowercase)
- Description is the PRIMARY trigger mechanism — make it pushy
- Instructions must be clear, specific, unambiguous
- Output format should show exact schema/structure

### Step 5: Write References
Create 2+ files in `references/`:

```markdown
# Domain Name — Reference Guide

## Topic 1
[Content, frameworks, best practices]

### Subtopic 1.1
[Details, tables, examples]

## Topic 2
[Red flags, edge cases]
```

**Quality bar:**
- Substantive content (>300 words per file)
- Frameworks, methodologies, decision trees
- Red flags and anti-patterns
- Real-world examples where possible
- Clear, organized with good headings

### Step 6: Write README.md
Structure (use `templates/README.md.template`):

```markdown
# [Skill Name]

**Status:** Beta 🟡

## What It Does
1-2 sentence overview.

## When to Use It
- Use case 1
- Use case 2

## Who Should Use It
Target audience description.

## Example Inputs
"Analyze this mutual fund for a 30-year-old with ₹50,000/month SIP budget"
"Review this TypeScript code for performance issues"

## Example Outputs
[Show 1-2 representative outputs]

## How It Works
Brief explanation of the skill's approach.

## Related Skills
- [Link to other skills]

## Contributing
Found an issue? Have improvements? See CONTRIBUTING.md
```

### Step 7: Create Evaluations
Edit `evals/eval_set.json`:

```json
{
  "eval_cases": [
    {
      "id": "eval-001",
      "difficulty": "easy",
      "category": "basic-usage",
      "input": "Analyze HDFC Balanced Advantage Fund for a 35-year-old moderate investor with 20-year horizon",
      "expected_output_criteria": [
        "Provides fund category assessment",
        "Discusses risk metrics",
        "Includes tax treatment for India",
        "Gives specific allocation recommendation",
        "Cites historical performance data"
      ]
    },
    {
      "id": "eval-002",
      "difficulty": "hard",
      "category": "edge-case",
      "input": "I have ₹50L to invest but also need ₹15L liquidity in 6 months. Conservative investor, 30 years old. Build me a portfolio.",
      "expected_output_criteria": [
        "Acknowledges conflicting goals (invest vs liquidity need)",
        "Separates emergency fund from investment portfolio",
        "Avoids locking 50L in long-term instruments",
        "Suggests liquid fund component",
        "Provides specific split recommendation"
      ]
    }
  ]
}
```

**Evaluation tips:**
- Minimum 5 cases; aim for 10
- Mix difficulty levels (easy, medium, hard)
- Include 1+ edge cases (conflicting goals, incomplete data, etc.)
- Specify exact success criteria
- Avoid vague criteria ("output is good")

### Step 8: Validate Locally

```bash
# Check structure
python tools/skill-validator.py skills/my-skill-name/

# Run evaluations
python tools/eval-runner.py skills/my-skill-name/evals/eval_set.json

# Expected output:
# ✅ Skill structure valid
# ✅ 10/10 evals passed
```

### Step 9: Submit PR

```bash
git add skills/my-skill-name/
git commit -m "Add my-skill: [description]. Fixes #123"
git push origin add/my-skill-name
```

Then open PR with this template:

```markdown
## Skill Submission: [Skill Name]

**Fixes:** #123 (link to skill proposal issue)

**What:** Brief description of skill

**Changes:**
- New skill: my-skill-name
- 2 reference files covering [X] and [Y]
- 10 evaluation test cases
- Comprehensive README

**Quality Gates:**
- [x] Passes `skill-validator.py`
- [x] All 10 evals passing
- [x] No anti-patterns detected
- [x] Reference files substantive (>300 words each)
- [x] README includes examples

**Testing:** 
Tested with inputs like:
- "User input example 1"
- "User input example 2"

**Related Work:**
- Related to skill X (linked)
- Complements skill Y

**Checklist:**
- [x] Follows ARCHITECTURE.md standards
- [x] No unnecessary filler language
- [x] Constraints prevent hallucination
- [x] Output format is explicit
- [x] References are specific, not generic
```

### Step 10: Code Review
- Maintainers will review for quality
- May request clarifications or improvements
- Once approved (2+ reviewers), PR is merged
- Automated workflow packages the skill as `.skill` file

---

## 🔄 Improving an Existing Skill

### To Suggest Changes
Open an issue with the skill name + suggestion:

```markdown
**Skill:** investment-analyst

**Suggestion:** Add cryptocurrency evaluation framework

**Why:** Users asking for crypto analysis; current skill covers only traditional instruments

**Scope:** New reference file with crypto-specific metrics
```

### To Submit Improvements
1. Fork, create branch: `improve/skill-name-improvement`
2. Make changes following same quality standards
3. Test improvements: `python tools/eval-runner.py`
4. Submit PR describing what you improved & why

---

## 🛠️ Contributing to Tools & Infrastructure

### To Improve Tools
```bash
git checkout -b enhance/tool-name-improvement
# Edit tools/*.py
# Test: python tools/tool-name.py --help
# Commit & PR
```

### To Improve Documentation
```bash
git checkout -b improve/docs-topic
# Edit docs/*.md
# Submit PR
```

No formal eval needed for docs; just ensure accuracy & clarity.

---

## 📋 PR Review Checklist (for Maintainers)

Before approving, verify:

- [ ] Skill solves a real problem
- [ ] Proposal was discussed & approved
- [ ] All quality gates pass
- [ ] Evals are comprehensive & passing
- [ ] References are substantive
- [ ] No anti-patterns (vague language, hedging, etc.)
- [ ] No duplicate of existing skill
- [ ] Maturity level is appropriate
- [ ] Documentation is complete
- [ ] No blocking issues from automated checks

---

## 🏆 Recognition

Contributors will be:
- Credited in skill's README.md
- Listed in monthly `CONTRIBUTORS.md`
- Recognized in release notes
- Eligible for "Contributor" GitHub badge
- Potential co-maintainer of their skill (if active)

---

## ❓ Questions?

- **General questions:** GitHub Discussions
- **Skill-specific:** Open an issue
- **Architecture/design:** Ping maintainers
- **Discord:** Join our community server (link in README)

---

## 🎁 Bonus: How to Get Feedback Pre-Submission

### Option 1: Draft PR
Push your skill to a branch and open PR as **Draft**. 
Maintainers will provide early feedback.

```bash
git push origin add/my-skill-name
# Open PR → mark as Draft
# Maintainers review & suggest improvements
# Convert to Ready when done
```

### Option 2: Discussion Thread
Create a GitHub Discussion:
```
Title: "Feedback wanted: My Skill Name"
Description: Share your skill draft, ask for feedback
```

Community will review & provide suggestions.

---

## 🚫 Anti-Patterns We Reject

- Generic skills ("helpful AI assistant")
- Vague output specifications
- No evaluation test cases
- Reference files <200 words
- Skills that duplicate existing ones
- Hedging language throughout ("might," "could")
- Missing constraints (prevents hallucination)
- No mention of limitations or edge cases

---

## 📚 Resources

- **ARCHITECTURE.md** — Design philosophy & patterns
- **docs/skill-anatomy.md** — What makes a great skill
- **docs/best-practices.md** — Writing tips
- **templates/** — Boilerplate to start from
- **examples/** — Real skills to learn from

---

Happy contributing! 🎉
