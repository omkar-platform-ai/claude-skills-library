# claude-skills-library

An open-source collection of high-quality, production-ready skills for Claude AI. Each skill is modular, testable, and designed for institutional-grade output.

---

## 📁 Repository Structure

```
claude-skills-library/
│
├── README.md                          # Repository overview, quick start, contribution guide
├── CONTRIBUTING.md                    # Detailed contribution guidelines
├── LICENSE                            # MIT or Apache 2.0
├── .gitignore                         # Standard Git ignores
├── ARCHITECTURE.md                    # Design philosophy, patterns, standards
│
├── skills/                            # All skills live here
│   │
│   ├── investment-analyst/            # Example: Investment analysis skill
│   │   ├── SKILL.md                   # Skill definition & instructions
│   │   ├── references/                # Domain-specific reference files
│   │   │   ├── indian-mutual-funds.md
│   │   │   ├── us-etfs-funds.md
│   │   │   ├── direct-equity-india.md
│   │   │   ├── direct-equity-us.md
│   │   │   ├── debt-bonds.md
│   │   │   ├── arbitrage-funds.md
│   │   │   ├── index-funds.md
│   │   │   └── crypto.md
│   │   ├── evals/
│   │   │   ├── eval_set.json          # Test cases for skill evaluation
│   │   │   └── README.md              # How to run evals
│   │   ├── scripts/                   # Optional: automation scripts
│   │   │   └── validate.py            # Skill-specific validation
│   │   ├── tests/                     # Optional: unit tests for reference data
│   │   └── README.md                  # Skill-specific documentation
│   │
│   ├── fitness-advisor/               # Example: Fitness & nutrition skill
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── exercise-science.md
│   │   │   ├── nutrition.md
│   │   │   ├── periodization.md
│   │   │   └── common-injuries.md
│   │   ├── evals/
│   │   │   └── eval_set.json
│   │   └── README.md
│   │
│   ├── executive-deck-specialist/     # Example: Presentation design skill
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── mckinsey-frameworks.md
│   │   │   ├── mece-principle.md
│   │   │   ├── pyramid-principle.md
│   │   │   ├── design-best-practices.md
│   │   │   └── audience-mapping.md
│   │   ├── assets/                    # Static files (icons, templates, fonts)
│   │   │   ├── templates/
│   │   │   │   ├── slide-template.json
│   │   │   │   └── color-palette.json
│   │   │   └── icons/
│   │   ├── evals/
│   │   │   └── eval_set.json
│   │   └── README.md
│   │
│   ├── code-reviewer/                 # Example: Code review skill
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── python-patterns.md
│   │   │   ├── typescript-patterns.md
│   │   │   ├── testing-strategies.md
│   │   │   ├── security-checklist.md
│   │   │   └── performance-optimization.md
│   │   ├── scripts/
│   │   │   ├── lint_python.py
│   │   │   └── lint_typescript.js
│   │   ├── evals/
│   │   │   └── eval_set.json
│   │   └── README.md
│   │
│   └── ...                            # More skills follow same pattern
│
├── templates/                         # Boilerplate for creating new skills
│   ├── SKILL.md.template              # Standard SKILL.md template
│   ├── references/                    # Template reference files
│   │   └── domain-reference.md.template
│   ├── evals/
│   │   ├── eval_set.json.template
│   │   └── README.md.template
│   └── README.md.template             # Skill-specific README template
│
├── docs/                              # Documentation hub
│   ├── index.md                       # Main documentation
│   ├── quick-start.md                 # 5-minute onboarding
│   ├── skill-anatomy.md               # What makes a good skill
│   ├── best-practices.md              # Writing & organizing skills
│   ├── evaluation-guide.md            # How to create & run evals
│   ├── prompt-engineering/
│   │   ├── core-principles.md         # 10 universal principles
│   │   ├── prompt-types.md            # 14 prompt type patterns
│   │   ├── platform-guides/
│   │   │   ├── claude.md
│   │   │   ├── gemini.md
│   │   │   ├── openai-gpt4o.md
│   │   │   ├── langchain.md
│   │   │   └── claude-code.md
│   │   └── frameworks/
│   │       ├── risen-framework.md
│   │       ├── costar-framework.md
│   │       ├── xml-tags-claude.md
│   │       └── react-prompting.md
│   ├── evaluation-framework/
│   │   ├── quality-rubric.md          # 5-dimensional quality scoring
│   │   ├── eval-examples.md           # Real eval cases
│   │   └── grading-rubric.json        # Structured eval schema
│   ├── faq.md                         # Common questions
│   └── glossary.md                    # Terms & definitions
│
├── tools/                             # Community tools & utilities
│   ├── skill-validator.py             # Validates SKILL.md structure
│   ├── skill-packager.py              # Packages skills into .skill files
│   ├── eval-runner.py                 # Runs evaluations in batch
│   ├── eval-viewer.py                 # Generates eval result HTML
│   ├── migration-assistant.py         # Convert old prompts to skills
│   └── README.md                      # Tools documentation
│
├── scripts/                           # Repository maintenance
│   ├── install-dependencies.sh        # Set up dev environment
│   ├── validate-all-skills.sh         # Lint all skills
│   ├── run-all-evals.sh               # Run full eval suite
│   ├── generate-index.sh              # Build skills index/sitemap
│   ├── create-skill.sh                # Scaffold new skill
│   └── README.md                      # Script documentation
│
├── .github/                           # GitHub-specific configuration
│   ├── workflows/
│   │   ├── validate-pr.yml            # PR validation pipeline
│   │   ├── run-evals.yml              # Run evals on new skills
│   │   ├── update-docs.yml            # Auto-generate docs
│   │   └── publish-release.yml        # Release new version
│   ├── PULL_REQUEST_TEMPLATE.md       # PR submission template
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── skill_request.md
│   │   └── documentation.md
│   └── dependabot.yml                 # Dependency updates
│
├── CHANGELOG.md                       # Version history
├── ROADMAP.md                         # Future plans
├── SKILLS_INDEX.md                    # Auto-generated skill registry
└── pyproject.toml / requirements.txt  # Python dependencies (for tools)

```

---

## 🏗️ Directory Breakdown

### `skills/`
Each subdirectory is a **complete, self-contained skill**. Standard structure:

```
skill-name/
├── SKILL.md                 # Required: Main skill definition
├── README.md                # Required: Skill overview & usage
├── references/              # Required: Domain knowledge files (2+ files minimum)
│   ├── *.md
│   └── ...
├── evals/                   # Recommended: Test cases
│   ├── eval_set.json
│   └── README.md
├── scripts/                 # Optional: Automation, validation
├── tests/                   # Optional: Unit tests for references
└── assets/                  # Optional: Icons, templates, fonts
```

**Minimum viable skill:** 3 files
- SKILL.md
- README.md
- At least 1 reference file

---

### `docs/`
**Comprehensive documentation** for users and contributors:
- Quick start guides
- Best practices for skill writing
- Prompt engineering principles (universal + platform-specific)
- Evaluation framework details
- FAQ & troubleshooting

---

### `tools/`
**Community utilities** to make skill creation easier:
- **skill-validator.py** — Checks SKILL.md structure & completeness
- **skill-packager.py** — Converts skill folder → .skill file
- **eval-runner.py** — Batch runs evals across all skills
- **migration-assistant.py** — Converts legacy prompts to skills

---

### `.github/workflows/`
**Automated CI/CD pipeline:**
- Validate PR structure
- Run evals on new/modified skills
- Auto-generate skill index
- Publish releases

---

## 📋 Key Files Explained

### `SKILL.md` (in each skill)
```yaml
---
name: investment-analyst
description: >
  [Skill metadata, triggers, what it does]
---

# Skill Instructions

[Step-by-step instructions]
[Quality gates]
[Output format specification]
```

**Always required.** This is what Claude reads.

---

### `README.md` (in each skill)
Human-readable guide:
- What the skill does
- When to use it
- Who should use it
- Examples of good inputs
- Related skills
- Contribution notes

---

### `references/*.md`
Domain-specific knowledge files:
- Frameworks, methodologies, best practices
- Reference data tables
- Evaluation criteria
- Red flags & edge cases

Claude loads these on-demand based on instrument/domain detected.

---

### `evals/eval_set.json`
```json
{
  "eval_cases": [
    {
      "id": "eval-001",
      "input": "User prompt here",
      "expected_output_criteria": [
        "Output contains X",
        "Format matches Y",
        "Avoids Z"
      ],
      "difficulty": "easy|medium|hard",
      "category": "category-name"
    }
  ]
}
```

Tests the skill against known inputs. Enables automated quality gates.

---

## 🎯 Quality Standards

Every skill **must** pass:

### Structure Validation
- [ ] Valid SKILL.md with name + description
- [ ] At least 1 README.md
- [ ] At least 2 reference files in `references/`
- [ ] No syntax errors in YAML/JSON/Markdown

### Content Quality (5-point rubric)
- **Clarity (4+/5):** Every instruction unambiguous
- **Specificity (4+/5):** Scope, format, audience defined
- **Efficiency (4+/5):** Minimum tokens for maximum precision
- **Completeness (4+/5):** All 5 pillars present (role/context/task/format/constraints)
- **Robustness (4+/5):** Handles edge cases; constraints prevent drift

### Evaluation Coverage
- Minimum 5 test cases per skill
- Mix of easy/medium/hard difficulty
- At least 1 edge case test

---

## 🚀 Quick Start for Contributors

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/claude-skills-library.git
cd claude-skills-library
```

### 2. Create a New Skill
```bash
./scripts/create-skill.sh my-skill-name
```

This scaffolds:
```
skills/my-skill-name/
├── SKILL.md              (template with examples)
├── README.md             (template)
├── references/
│   ├── domain1.md
│   ├── domain2.md
│   └── README.md
├── evals/
│   ├── eval_set.json     (template)
│   └── README.md
└── tests/
    └── test_references.py
```

### 3. Write Your Skill
Edit SKILL.md, references, README.
Follow `ARCHITECTURE.md` patterns.

### 4. Validate & Test
```bash
python tools/skill-validator.py skills/my-skill-name
python tools/eval-runner.py skills/my-skill-name/evals/eval_set.json
```

### 5. Submit PR
- Link to skill proposal issue
- Explain what the skill does & why
- Link to any evals/test results
- Request review from maintainers

---

## 📦 Distribution

Skills are packaged as `.skill` files (zipped) for easy installation:

```bash
python tools/skill-packager.py skills/investment-analyst/ --output ./dist/
# Output: investment-analyst-skill.skill
```

Users download → install in Claude → ready to use.

---

## 🏆 Skill Maturity Levels

Track each skill's maturity:

| Level | Requirements |
|---|---|
| **Experimental** 🔴 | Draft SKILL.md, minimal evals |
| **Beta** 🟡 | Complete SKILL.md, 5+ evals, 1 contributor review |
| **Stable** 🟢 | All above + 10+ passing evals, 2+ reviews, >50 uses |
| **Production** 🔵 | Stable + comprehensive docs, >200 uses, bug-free 30 days |

Display badge in each skill's README:
```
![Maturity: Stable](https://img.shields.io/badge/maturity-stable-brightgreen)
```

---

## 📊 Skills Index

Auto-generated file listing all skills:

**SKILLS_INDEX.md**
```markdown
# Skills Library Index

## By Category

### Finance
- **investment-analyst** (Production) — Portfolio recommendations, multi-instrument analysis
- **business-analyst** (Stable) — Market analysis, competitive intelligence
- ...

### Engineering
- **code-reviewer** (Stable) — Code review, best practices
- **architecture-designer** (Beta) — System design, trade-off analysis
- ...

### Content
- **executive-deck-specialist** (Production) — Presentation design, storytelling
- **blog-writer** (Experimental) — Long-form writing, SEO optimization
- ...

[Full table with descriptions, maturity levels, tags]
```

Auto-updated by GitHub Action on each merge.

---

## 🤝 Governance

### Maintainers
- Lead architect (1–2 people)
- Domain maintainers (1 per 5–10 skills)
- Community moderators

### Decision Process
1. Feature request / skill proposal issue
2. Community discussion (1 week minimum)
3. Maintainer approval
4. PR submission & review (2 approvals required)
5. Merge + auto-publish

### Backwards Compatibility
- Skills are versioned (CHANGELOG.md)
- Breaking changes in major versions only
- 1-version deprecation period before removal

---

## 📈 Metrics & Analytics

Track in `METRICS.md`:
```json
{
  "total_skills": 42,
  "by_maturity": {
    "production": 15,
    "stable": 20,
    "beta": 5,
    "experimental": 2
  },
  "total_downloads": 50000,
  "community_contributors": 127,
  "issues_open": 8,
  "avg_eval_coverage": 8.3
}
```

Updated monthly in CI/CD.

---

## 🔐 Security & License

- **License:** MIT or Apache 2.0
- **Code of Conduct:** Enforce community standards
- **Security Policy:** Report vulnerabilities privately
- **Skill Audit:** Monthly review of new/modified skills

---

## 📝 Contribution Workflow

```
Issue Created (Skill Proposal)
        ↓
Community Feedback (1 week)
        ↓
Maintainer Approval
        ↓
Fork → Branch → Write Skill
        ↓
Validate + Eval Locally
        ↓
Open PR
        ↓
Automated Tests (GitHub Action)
        ↓
Peer Review (2+ approvals)
        ↓
Merge → Auto-publish .skill file
        ↓
Update Index & Metrics
        ↓
Released in next version
```

---

## 🎁 Example: Adding Investment Analyst Skill

```bash
# 1. Create from template
./scripts/create-skill.sh investment-analyst

# 2. Edit files
vim skills/investment-analyst/SKILL.md
vim skills/investment-analyst/README.md
# ... add references/*.md files ...

# 3. Add evals
vim skills/investment-analyst/evals/eval_set.json

# 4. Validate
python tools/skill-validator.py skills/investment-analyst/
# ✅ All checks passed

# 5. Run evals
python tools/eval-runner.py skills/investment-analyst/evals/eval_set.json
# ✅ 8/8 eval cases passed

# 6. Submit PR
git checkout -b add/investment-analyst-skill
git add skills/investment-analyst/
git commit -m "Add investment-analyst skill: portfolio recommendations for any instrument"
git push origin add/investment-analyst-skill

# 7. PR submitted → reviewed → merged
# 8. Auto-packaged & published
# 9. Available for download
```

---

## 🔗 GitHub Links Setup

```yaml
# .github/settings.yml
repository:
  name: claude-skills-library
  description: Production-grade skills library for Claude AI
  homepage: https://claude-skills-library.io
  topics:
    - claude
    - prompt-engineering
    - skills
    - llm
    - ai
  
  has_wiki: true
  has_discussions: true
  has_projects: true
```

---

## 📚 Documentation To Create

```
docs/
├── index.md                           # Landing page
├── quick-start.md                     # "Get started in 5 min"
├── skill-anatomy.md                   # What makes a skill
├── best-practices.md                  # How to write great skills
├── evaluation-guide.md                # Creating evals
├── prompt-engineering/
│   ├── core-principles.md
│   ├── prompt-types.md
│   ├── platform-guides/               # Claude, Gemini, GPT-4, etc.
│   ├── frameworks/                    # RISEN, COSTAR, ReAct, etc.
│   └── anti-patterns.md
├── contribution-guide/
│   ├── skill-submission.md
│   ├── review-process.md
│   └── code-of-conduct.md
├── examples/
│   ├── simple-skill.md
│   ├── complex-skill.md
│   └── skill-with-automation.md
└── faq.md
```

---

## 🎯 Launch Checklist

- [ ] GitHub repo created, configured
- [ ] README.md written & polished
- [ ] CONTRIBUTING.md finalized
- [ ] ARCHITECTURE.md documented
- [ ] Templates scaffolded (SKILL.md, references, evals)
- [ ] 3–5 foundational skills added (investment-analyst, fitness-advisor, code-reviewer, etc.)
- [ ] CI/CD workflows configured
- [ ] Documentation site deployed (GitHub Pages or ReadTheDocs)
- [ ] Initial issue templates created
- [ ] Code of Conduct adopted
- [ ] License chosen (MIT recommended for broad adoption)
- [ ] Community channels set up (Discussions, Discord, etc.)
- [ ] First release tagged (v0.1.0)
- [ ] Announcement posted (ProductHunt, HN, Reddit, etc.)

---

## 🌟 Why This Structure Works

1. **Scalable:** Add skills independently without touching core
2. **Modular:** Each skill is self-contained; can be tested in isolation
3. **Discoverable:** Clear categorization + auto-generated index
4. **Maintainable:** Consistent structure → easy to lint & validate
5. **Community-friendly:** Clear contribution path; low barrier to entry
6. **Quality-gated:** Automated validation + evals + peer review
7. **Well-documented:** Comprehensive guides for users & contributors
8. **Distributed:** .skill files can be installed anywhere, not locked to repo
9. **Versionable:** Changelog + maturity levels track evolution
10. **Permissionless:** MIT/Apache license → anyone can fork, enhance, redistribute

---

This structure is **production-grade**, **open-source-ready**, and **Claude-optimized**.
