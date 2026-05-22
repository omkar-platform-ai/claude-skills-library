# CLAUDE.md - Claude Skills Library Development Guide

This file provides Claude Code with the context, standards, and patterns for developing and improving the Claude Skills Library.

---

## 🎯 Project Purpose

Build an open-source, production-grade skills library for Claude AI where:
- **Skills** = Reusable prompting systems (instructions + domain references + test cases)
- **Quality** = Institutional-grade output across all domains
- **Community** = Easy contribution path for 200+ developers
- **Scale** = Support 50-100+ skills with consistent standards

**Repository:** https://github.com/omkar-platform-ai/claude-skills-library

---

## 📐 Architecture & Design Principles

### Core Principles (Always Follow)

1. **Clarity Over Cleverness** — Every word earns its place; no filler or hedging
2. **5-Pillar Framework** — Every skill must have: Role, Context, Task, Format, Constraints
3. **Imperative Voice** — Use commanding language: "Generate," "Analyze," "Create"
4. **Specificity Beats Generality** — Define scope, format, audience precisely
5. **Constraints Prevent Drift** — Hard rules prevent hallucination and scope creep
6. **Quality Gates** — Verify 10 gates before delivering any output
7. **Anti-Pattern Detection** — Flag and remove: hedging ("might," "could"), vague language, generic disclaimers

### 5-Pillar Framework (Apply to Every Skill)

Every SKILL.md must explicitly define:

```yaml
<role>
You are a [specific expert] with [background/expertise].
</role>

<context>
[Relevant situation, data, investor/user profile, constraints]
</context>

<task>
[Specific imperative instruction: Analyze / Generate / Build / Recommend / Compare]
</task>

<format>
[Exact output structure with examples, headers, tables, fields]
</format>

<constraints>
[Specific "do not" rules that prevent hallucination and scope creep]
</constraints>
```

---

## 📁 Repository Structure (Current State)

```
claude-skills-library/
├── skills/
│   └── investment-analyst/          # Production-ready skill
│       ├── SKILL.md
│       ├── README.md
│       ├── references/              # 8 domain reference files
│       │   ├── indian-mutual-funds.md
│       │   ├── us-etfs-funds.md
│       │   ├── direct-equity-india.md
│       │   ├── direct-equity-us.md
│       │   ├── debt-bonds.md
│       │   ├── arbitrage-funds.md
│       │   ├── index-funds.md
│       │   └── crypto.md
│       └── evals/
│           └── eval_set.json
├── templates/
│   ├── SKILL.md.template
│   └── references/
├── docs/
│   ├── quick-start.md
│   ├── skill-anatomy.md
│   ├── best-practices.md
│   └── prompt-engineering/
├── tools/
│   ├── skill-validator.py
│   ├── skill-packager.py
│   ├── eval-runner.py
│   └── README.md
├── .github/
│   ├── workflows/
│   │   └── validate-pr.yml
│   └── ISSUE_TEMPLATE/
├── README.md
├── CONTRIBUTING.md
├── ARCHITECTURE.md
└── pyproject.toml
```

---

## 🎯 Quality Rubric (5 Dimensions)

Every skill must score **4+/5** on ALL dimensions before acceptance.

### 1. Clarity (Is every instruction unambiguous?)
- **5:** Zero confusion; one reading sufficient
- **4:** Very clear; minimal re-reading
- **3:** Mostly clear; some ambiguity
- **2:** Ambiguous; multiple interpretations
- **1:** Confusing; intent unclear

**How to improve:** Remove hedging ("might," "could"), use imperative voice, break long sentences.

### 2. Specificity (Is scope, format, audience defined?)
- **5:** Highly specific; no generalization needed
- **4:** Scope, format, audience clearly defined
- **3:** Somewhat specific; could be more detailed
- **2:** Vague; unclear boundaries
- **1:** Generic; applies to anything

**How to improve:** Name audience, define boundaries, specify format with examples.

### 3. Efficiency (Minimum tokens for maximum precision?)
- **5:** Every token earns place; densely written
- **4:** Efficient; no obvious waste
- **3:** Some verbosity but acceptable
- **2:** Redundant phrases/examples
- **1:** Bloated; half could be cut

**How to improve:** Remove filler, use tables instead of prose, cut obvious examples.

### 4. Completeness (All 5 pillars present and strong?)
- **5:** Role, context, task, format, constraints all strong
- **4:** All five present; 3+ are strong
- **3:** 4 of 5 present; some weak
- **2:** 3 of 5 present; major gaps
- **1:** <3 pillars present

**How to improve:** Check each pillar explicitly defined.

### 5. Robustness (Handles edge cases? Prevents drift?)
- **5:** Comprehensive constraints; all foreseeable cases covered
- **4:** Good constraints; handles most cases
- **3:** Basic constraints; some gaps
- **2:** Minimal constraints; easily drifts
- **1:** No constraints; hallucinates freely

**How to improve:** Add specific "do not" rules, handle edge cases, set boundaries.

---

## 📝 Skill Creation Workflow

### Step 1: Validate Idea
- Check SKILLS_INDEX.md for duplicates
- Open GitHub Issue with skill proposal
- Get community feedback (1 week minimum)
- Obtain maintainer approval before starting

### Step 2: Create Skill Structure
```bash
mkdir -p skills/skill-name/{references,evals}
cp templates/SKILL.md.template skills/skill-name/SKILL.md
cp templates/README.md.template skills/skill-name/README.md
```

### Step 3: Write SKILL.md
- Fill in 5 pillars explicitly
- Use XML tags: `<role>`, `<context>`, `<task>`, `<format>`, `<constraints>`
- Add quality gates (10-point checklist)
- Include examples
- **Always score 4+/5 on all 5 dimensions**

### Step 4: Write References (2+ files, 300+ words each)
- Domain-specific knowledge
- Frameworks, methodologies, evaluation criteria
- Red flags and anti-patterns
- Real-world examples
- Clear headings and organization

### Step 5: Create Evaluations (5+ test cases)
```json
{
  "eval_cases": [
    {
      "id": "eval-001",
      "difficulty": "easy|medium|hard",
      "category": "category-name",
      "input": "User input that skill should handle",
      "expected_output_criteria": [
        "Specific criterion 1",
        "Specific criterion 2",
        "Specific criterion 3"
      ]
    }
  ]
}
```

### Step 6: Test Locally
```bash
python tools/skill-validator.py skills/skill-name/
python tools/eval-runner.py skills/skill-name/evals/eval_set.json
```

### Step 7: Submit PR
- Link to skill proposal issue
- Explain what skill does & why
- Reference eval results
- Request review from maintainers

### Step 8: Code Review
- 2+ maintainer reviews required
- Quality gates verified
- Anti-patterns flagged
- Once approved: merge & auto-package

---

## 🚫 Anti-Patterns (Never Do This)

### In SKILL.md
- ❌ Generic role: "helpful assistant"
- ❌ Vague task: "analyze the thing"
- ❌ No constraints (anything goes)
- ❌ Implied format (hope Claude guesses)
- ❌ Hedging language: "might," "could," "perhaps"
- ❌ Passive voice: "it is recommended that"

### In References
- ❌ Generic information: "there are many types"
- ❌ No frameworks or methodologies
- ❌ No red flags or edge cases
- ❌ Vague guidance: "choose carefully"

### In Tone
- ❌ Uncertain: "this might be good"
- ❌ Passive: "could be considered"
- ❌ Indirect: "you might want to think about"

### In Evaluations
- ❌ Vague criteria: "output is good"
- ❌ Unrealistic inputs
- ❌ No edge cases
- ❌ Too few test cases (<5)

---

## ✅ Quality Gates (Before Shipping)

**All 10 gates must be verified:**

- [ ] Every instrument/domain has 3+ years data (except crypto: 1+ year)
- [ ] No recommendations solely on 1-3 year recent performance
- [ ] Expense ratios/fees compared to category median with justification
- [ ] Management/issuer tenure assessed (prefer 3+ years)
- [ ] No single instrument >40% portfolio (unless explicitly justified)
- [ ] Sector/theme concentration risk explicitly addressed
- [ ] Tax implications stated for investor's specific jurisdiction
- [ ] Liquidity requirements matched to instrument lock-in periods
- [ ] Portfolio overlap checked across all recommendations
- [ ] Downside scenario acknowledged for every recommendation

---

## 📊 Skill Maturity Levels

Track progression with badges:

| Level | Requirements |
|---|---|
| 🔴 **Experimental** | Draft SKILL.md, <5 evals, 0 reviews |
| 🟡 **Beta** | Complete SKILL.md, 5+ evals passing, 1 review |
| 🟢 **Stable** | All above + 10+ passing evals, 2+ reviews, >50 uses |
| 🔵 **Production** | Stable + comprehensive docs, >200 uses, bug-free 30 days |

---

## 🛠️ Tools & Automation

### skill-validator.py
Validates SKILL.md structure and YAML syntax.
```bash
python tools/skill-validator.py skills/skill-name/
```

### eval-runner.py
Runs evaluation test cases against Claude API.
```bash
ANTHROPIC_API_KEY=sk-... python tools/eval-runner.py skills/skill-name/evals/eval_set.json
```

### skill-packager.py
Packages skill folder into .skill file for distribution.
```bash
python tools/skill-packager.py skills/skill-name --output ./dist/
```

---

## 📚 Documentation Structure

When working on docs, follow this organization:

```
docs/
├── quick-start.md              # 5-minute onboarding
├── skill-anatomy.md            # Components of a skill
├── best-practices.md           # How to write great skills
├── evaluation-guide.md         # Creating test cases
├── prompt-engineering/
│   ├── core-principles.md      # 7 universal principles
│   ├── prompt-types.md         # 14 prompt patterns
│   └── platform-guides/
│       ├── claude.md
│       ├── gemini.md
│       └── openai.md
└── faq.md
```

---

## 🔄 Workflow for Improvements

### To Improve Existing Skill

```bash
# 1. Create feature branch
git checkout -b improve/skill-name-improvement

# 2. Make changes (don't modify SKILL.md name)
# Edit: references/*.md, evals/eval_set.json, README.md

# 3. Test
python tools/skill-validator.py skills/skill-name/
python tools/eval-runner.py skills/skill-name/evals/eval_set.json

# 4. Commit & push
git add .
git commit -m "Improve skill-name: [specific improvement]"
git push origin improve/skill-name-improvement

# 5. Open PR
```

### To Add New Skill

```bash
# 1. Get approval on GitHub Issue first
# 2. Create feature branch
git checkout -b add/new-skill-name

# 3. Create skill following workflow above
# 4. Test thoroughly
# 5. Open PR linking to proposal issue
```

---

## 🎯 Current Priorities

### Phase 1: Foundation (Current)
- ✅ Repository structure in place
- ✅ investment-analyst skill (production-ready)
- ✅ Documentation & contributing guidelines complete
- ⏳ Fix git push issue (skills/ directory)
- ⏳ Launch repository

### Phase 2: Growth (Next 2 weeks)
- Add 3-5 more skills (code-reviewer, fitness-advisor, business-analyst, etc.)
- Set up GitHub Discussions for community support
- Announce on ProductHunt, HN, Twitter, Reddit

### Phase 3: Scale (Next month)
- Reach 15-20 production skills
- Onboard first 10-15 external contributors
- Establish skill review process
- Create contributor dashboard

---

## 🔐 Security & Best Practices

### When Working with Sensitive Data
- Never include real API keys, credentials, or secrets
- Use placeholder examples (e.g., `sk-...`)
- Store sensitive instructions in separate docs (not in skills)

### When Updating Skills
- Maintain backwards compatibility (don't break existing usage)
- Version major changes (CHANGELOG.md)
- Test before merging

### When Reviewing PRs
- Verify all 10 quality gates pass
- Check for anti-patterns
- Ensure 2+ reviewers approve
- Run automated tests before merge

---

## 🚀 Common Tasks

### Generate a New Skill Scaffold
```bash
./scripts/create-skill.sh my-new-skill
# Creates: skills/my-new-skill/ with templates
```

### Validate All Skills
```bash
python tools/skill-validator.py skills/
```

### Run All Evaluations
```bash
for skill in skills/*/; do
    echo "Testing $(basename $skill)..."
    python tools/eval-runner.py "$skill/evals/eval_set.json"
done
```

### Package a Skill for Distribution
```bash
python tools/skill-packager.py skills/investment-analyst --output ./dist/
# Output: dist/investment-analyst-skill.skill
```

### Check Git Status Before Push
```bash
git status
git diff --cached | head -50
git log --oneline | head -5
```

---

## 📖 Key Documents to Reference

- **ARCHITECTURE.md** — Design philosophy & quality standards
- **CONTRIBUTING.md** — Contributor guidelines
- **templates/SKILL.md.template** — Skill boilerplate
- **skills/investment-analyst/SKILL.md** — Example production skill
- **skills/investment-analyst/README.md** — Example README

---

## 💡 Tips for Claude Code Usage

1. **Before making changes**, review the relevant section in this file
2. **Always validate** with `skill-validator.py` after changes
3. **Test evaluations** with `eval-runner.py` for new/modified skills
4. **Reference ARCHITECTURE.md** for quality standards
5. **Check CONTRIBUTING.md** before accepting PRs
6. **Run git status** before commits to avoid unintended changes
7. **Keep anti-patterns in mind** — flag them if you see them

---

## 🎯 Your Role in Claude Code

You are acting as a **development assistant** for the Claude Skills Library. You should:

✅ **DO:**
- Create new skills following the 5-pillar framework
- Improve existing skills (references, evals, README)
- Add documentation and guides
- Validate changes before committing
- Suggest improvements based on quality rubric
- Flag anti-patterns and suggest fixes
- Help debug git issues

❌ **DON'T:**
- Commit code without validating first
- Create skills without linking to proposal issue
- Accept PRs without 2+ reviews
- Modify SKILL.md structure (only content)
- Push directly to main (always use feature branches)
- Ignore quality gates

---

## 📞 Current Issues & TODOs

### Known Issues
- [ ] skills/ directory not pushing to GitHub (git + .gitignore issue)
- [ ] Need to verify GitHub Actions workflow is working

### In Progress
- [ ] Launching repository
- [ ] Initial announcement & community outreach

### Upcoming
- [ ] Add code-reviewer skill
- [ ] Add fitness-advisor skill
- [ ] Create skill marketplace documentation
- [ ] Set up community Discord

---

## 🎉 Success Criteria

The library is successful when:
- ✓ 50+ production-ready skills
- ✓ 200+ community contributors
- ✓ 100,000+ monthly downloads
- ✓ <1 week median PR merge time
- ✓ Zero critical bugs
- ✓ Cited in prompt engineering guides

---

## 📞 Quick Reference

**Repository:** https://github.com/omkar-platform-ai/claude-skills-library
**Local Path:** `/Users/sonaw/Library/CloudStorage/OneDrive-Henkel/Personal/Tech-Learnings/Personal-Learning-Projects/AI-Agent-Builder/claude-skills-library`

**Key Commands:**
```bash
# Validate
python tools/skill-validator.py skills/skill-name/

# Test
python tools/eval-runner.py skills/skill-name/evals/eval_set.json

# Package
python tools/skill-packager.py skills/skill-name --output ./dist/

# Git push
git add .
git commit -m "message"
git push origin branch-name
```

**Key Files:**
- ARCHITECTURE.md — Design bible
- CONTRIBUTING.md — Contributor guide
- templates/SKILL.md.template — Skill template
- skills/investment-analyst/ — Example skill

---

**Last Updated:** May 22, 2025
**Version:** 1.0.0
**Status:** Production-Ready

This CLAUDE.md provides all context Claude Code needs to develop and improve the skills library.