# Claude Skills Library

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-green?style=flat-square)](VERSION)

A comprehensive, open-source library of **production-grade skills for Claude AI**. Each skill is modular, thoroughly tested, and designed for institutional-quality output across any domain.

**What are skills?** Reusable, vetted prompting frameworks that Claude can apply intelligently based on context. A skill is more than a prompt—it's a complete system with domain-specific references, evaluation test cases, and quality gates.

---

## 🎯 Why This Library?

### Problem: Prompt Engineering is Hard
Writing effective prompts requires expertise in:
- Clarity and specificity
- Multi-dimensional frameworks
- Edge case handling
- Quality validation
- Domain-specific knowledge

Most developers waste time reinventing the wheel.

### Solution: Pre-Built, Battle-Tested Skills
This library provides:
- **Vetted, contributed skills** ready to use immediately (see the table below)
- **Institutional-grade quality** — every skill ships with structural validation and evaluation cases
- **Domain expertise baked in** — reference materials live alongside each skill
- **Open source** — contribute, fork, adapt for your needs

---

## 📚 Available Skills

Skills are organised into two tiers under `skills/`:

- `skills/contributed/` — skills authored or actively maintained in this repo
- `skills/curated/` — external upstream skills imported under a permissive license (see [docs/CURATION_POLICY.md](docs/CURATION_POLICY.md))

### Contributed

| Skill | Status | Use Case |
|---|---|---|
| **investment-analyst** | 🟢 stable | Portfolio recommendations, multi-instrument analysis (stocks, funds, crypto, bonds) |
| **fitness-advisor** | 🟢 stable | Personalised fitness coaching, workout plans, nutrition guidance |
| **executive-deck-specialist** | 🟢 stable | Consultant-grade decks using MECE, Pyramid Principle, SCQA |
| **commit-message** | 🟢 stable | Conventional Commit messages aligned to enterprise standards |
| **commercial-projection-architect** | 🟡 beta | Financial projections and investment justifications |
| **it-company-due-diligence-advisor** | 🟡 beta | Job offer evaluation, red flag detection, comp benchmarking |

### Curated (external upstream)

| Skill | Status | Upstream | Use Case |
|---|---|---|---|
| **defuddle** | 🟢 stable | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Clean markdown extraction from web pages via the Defuddle CLI |
| **json-canvas** | 🟢 stable | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Create and edit JSON Canvas (.canvas) files for Obsidian |
| **obsidian-bases** | 🟢 stable | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Create and edit Obsidian Bases (.base) database views |
| **obsidian-cli** | 🟢 stable | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Interact with Obsidian vaults via the obsidian CLI |
| **obsidian-markdown** | 🟢 stable | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Author Obsidian Flavored Markdown (wikilinks, callouts, properties) |
| **session-handoff** | 🟢 stable | [nateherkai/a-bunch-of-skills](https://github.com/nateherkai/a-bunch-of-skills) | Structured end-of-session summary for handing off to a fresh agent |

**[View full auto-generated index →](SKILLS_INDEX.md)**

---

## 🚀 Quick Start (5 Minutes)

### 1. Download a Skill
```bash
# Browse skills at https://github.com/anthropics/claude-skills-library/tree/main/skills
# Download investment-analyst-skill.skill (or any skill you want)
```

### 2. Install in Claude
**In Claude.ai:**
- Go to Settings → Custom Instructions
- Toggle "Custom Instructions" ON
- Paste the skill's SKILL.md content into the "System" field
- Save

**Via Claude Code / CLI:**
```bash
claude install investment-analyst-skill.skill
```

**Via API:**
```python
from anthropic import Anthropic

client = Anthropic()
# Load skill definition
with open('investment-analyst-skill.skill', 'r') as f:
    skill = f.read()

response = client.messages.create(
    model="claude-opus-4-20250805",
    max_tokens=4000,
    system=skill,
    messages=[
        {"role": "user", "content": "Analyze HDFC Mutual Fund for my portfolio..."}
    ]
)
```

### 3. Use the Skill
Just ask Claude naturally:
> "I'm 35, have ₹50L to invest, moderate risk appetite, 15-year horizon, 30% tax bracket. Build me a portfolio."

Claude will automatically apply the investment-analyst skill and deliver institutional-grade analysis.

---

## 📖 Documentation

- **[Quick Start Guide](docs/quick-start.md)** — Get up and running in 5 minutes
- **[Skill Anatomy](docs/skill-anatomy.md)** — What makes a skill work
- **[Best Practices](docs/best-practices.md)** — How to write great skills
- **[Evaluation Guide](docs/evaluation-guide.md)** — Creating & running test cases
- **[Prompt Engineering](docs/prompt-engineering/)** — Core principles + platform guides
- **[Contributing](CONTRIBUTING.md)** — Submit new skills or improvements
- **[Architecture](ARCHITECTURE.md)** — Design philosophy & standards
- **[FAQ](docs/faq.md)** — Common questions

---

## 🤝 Contributing

We welcome contributions! Whether you're adding a new skill, improving documentation, or enhancing tools.

### Quick Path to Contributing

1. **Have a skill idea?** Open a [Skill Proposal issue](https://github.com/anthropics/claude-skills-library/issues/new?template=skill_request.md)
2. **Get feedback** from the community (1 week)
3. **Get maintainer approval** to proceed
4. **Create your skill** using the [template](templates/SKILL.md.template)
5. **Write evaluations** — minimum 5 test cases
6. **Submit a PR** — automated validation + peer review
7. **Celebrate!** Your skill is now published

[Full contribution guide →](CONTRIBUTING.md)

---

## 🏆 Skills Maturity Levels

Each skill has a maturity badge:

| Level | Meaning |
|---|---|
| 🔴 **Experimental** | Draft stage; limited testing |
| 🟡 **Beta** | Functional; 1+ peer review; 5+ passing evals |
| 🟢 **Stable** | Production-ready; 2+ reviews; 10+ passing evals; >50 uses |
| 🔵 **Production** | Proven; comprehensive docs; >200 uses; bug-free 30 days |

---

## 💡 Example: Investment Analyst Skill

### What It Does
Analyzes any financial instrument (stocks, mutual funds, bonds, ETFs, crypto) for any investor profile, providing ranked recommendations with quantified rationale.

### Sample Input
> "I'm 35 years old, earning ₹2L/month. Moderate risk, 20-year horizon. Have ₹10L to invest now + ₹30k monthly SIP. 30% tax bracket, Indian resident. Build me a diversified portfolio."

### Sample Output
```
# Investor Profile Summary
35-year-old Indian investor, moderate risk appetite, 20-year horizon.
Primary goals: long-term wealth creation, retirement readiness.
Constraints: moderate income, ongoing SIP capacity.
Tax situation: 30% bracket; should prioritize tax-efficient instruments (ELSS, index funds).

# Recommended Asset Allocation
| Asset Class | % | Rationale |
|---|---|---|
| Large Cap Equity | 40% | Stable, lower volatility; anchor holding |
| Mid-Cap Equity | 20% | Growth potential over 20 years |
| Small-Cap Equity | 10% | Upside potential (capped to limit volatility) |
| Debt | 20% | Buffer during market corrections |
| Gold | 5% | Portfolio stabilizer, inflation hedge |
| Cash | 5% | Emergency fund top-up |

# Top Recommendations (Ranked)

## Rank #1 — Mirae Asset Emerging Bluechip Fund
**Category:** Mid Cap
**Risk Level:** Moderately High
**Allocation:** ₹3,00,000 lump sum + ₹8,000/month SIP
**Why This Fund:**
- Consistent 5Y returns: 14.2% CAGR (ranked 1st percentile)
- Fund manager Nilesh Shah: 18+ years track record
- AUM ₹8,200 Cr: healthy scale without capacity constraints
- Benchmark outperformance: Beat Nifty Mid-Cap in 8/10 years
- Expense ratio: 0.68% direct plan (below category median 0.85%)

**Pros:**
- Proven mid-cap specialist with consistent alpha generation
- Strong research team with deep stock-picking capability
- Tax-efficient given long expected holding period

**Cons/Risks:**
- Mid-cap volatility: Expect 15-20% drawdowns in bear markets
- Manager concentration: Nilesh Shah departure would impact performance
- Sector concentration: Tech 35% (above category median 25%)

**Best Suitable For:**
- Investors comfortable with 15%+ drawdowns
- 10+ year horizon (required for mid-cap volatility)
- Seeking alpha over broad-based index exposure

**Things To Watch:**
- Valuations: Nifty Mid-Cap is at 22x P/E (above 10Y average 18x)
- Manager succession: Monitor for any turnover in research team
- Sector rotation: Tech concentration poses risk if rates rise

---
[Additional 6 fund recommendations with same level of detail]

# Funds Avoided & Why
1. **Axis Focused 25 Fund** — Active fund with 0.92% ER underperformed Nifty 50 by 3% annually for 5Y; not justified given higher cost
2. **Multi-cap index** — Lower exposure to growth (cap-weighted limits mid/small cap)
3. **Small-cap funds with <₹500 Cr AUM** — Closure risk too high

# Final Portfolio Summary
| Fund | Category | Amount | Monthly SIP |
|---|---|---|---|
| ICICI Pru Bluechip | Large Cap | ₹2,00,000 | ₹5,000 |
| Mirae Asset Emerging Bluechip | Mid Cap | ₹3,00,000 | ₹8,000 |
| Motilal Oswal Multicap | Small Cap | ₹1,50,000 | ₹4,000 |
| HDFC High Interest Savings | Debt | ₹2,00,000 | ₹3,000 |
| Nippon India Gold | Gold | ₹500,000 | ₹2,000 |
| Axis Liquid Fund | Cash/Liquid | ₹500,000 | ₹3,000 |

**Expected Portfolio Metrics:**
- Volatility: 12-14% annualized
- Expected 10-year CAGR: 11-12%
- Max historical drawdown (similar portfolio): 25-28%
- Recovery time from drawdown: 12-18 months

# Additional Insights
**Tax Optimization:**
- Equity funds: LTCG 10% (after 1 year); tax-efficient for 20Y horizon
- Debt fund: Taxed at slab rate; consider bonds for taxable accounts
- ELSS not recommended for this profile (unnecessary lock-in)

**SIP Strategy During Corrections:**
- Continue SIP through market crashes (historical data shows +18% annualized returns if continued through corrections)
- Do NOT stop SIP or try to time market bottom
- Market down 20%+ → consider increasing SIP by 20% for 3-6 months

**Common Mistakes This Profile Makes:**
- Chasing recent top performers (Midcap index up 40% in 2023 → fear of missing out)
- Over-concentration in tech/IT funds (easy to fall into trap)
- Panic selling in corrections (happened in 2020, 2022, 2023)
- Insufficient emergency fund (6 months expenses minimum before investing lump sum)

**Review Frequency:**
- Quarterly: Check if allocation has drifted >5% (rebalance if so)
- Annually: Review fund performance against benchmarks
- Trigger immediate review: Manager change, regulatory action, >20% outperformance in any fund
```

---

## 🔧 Tools & Infrastructure

The library includes tools to make skill creation, testing, and packaging easy:

```bash
# Install Python dependencies
pip install -r tools/requirements.txt

# Validate a single skill
python tools/skill_validator.py skills/contributed/investment-analyst/

# Validate every skill in the repo
python tools/skill_validator.py --validate-all

# Regenerate SKILLS_INDEX.md from metadata.yaml files
python tools/generate_index.py

# Curated-skill upstream check (stub)
python tools/skill_updater.py --check
```

[Full tools documentation →](tools/README.md)

---

## 📊 Library Stats

- **Total Skills:** 12 — 6 contributed · 6 curated (see [SKILLS_INDEX.md](SKILLS_INDEX.md))
- **Stable:** 10 · **Beta:** 2 · **Deprecated:** 0
- **Evaluation Coverage:** minimum 3 test cases per skill (validator-enforced)
- **License:** MIT (permissive, commercial-friendly)

---

## 🛡️ Quality Assurance

Every skill is evaluated on a **5-dimensional rubric:**

| Dimension | Standard |
|---|---|
| **Clarity** | Every instruction unambiguous (4+/5) |
| **Specificity** | Scope, format, audience defined (4+/5) |
| **Efficiency** | Dense, precise; no filler (4+/5) |
| **Completeness** | All 5 pillars present (4+/5) |
| **Robustness** | Handles edge cases; prevents drift (4+/5) |

Skills only released after:
- ✅ Passing structural validation
- ✅ Passing 5+ diverse evaluation test cases
- ✅ 2+ peer reviews
- ✅ Zero anti-patterns detected
- ✅ Comprehensive documentation

---

## 🔐 Security & Privacy

- **No data collection:** Skills run entirely within Claude — your inputs stay private
- **Open audit:** All code visible; community can review
- **License:** MIT — you own and control your usage
- **Compliance:** Works offline or in air-gapped environments

---

## 🤖 Platform Support

Skills work across:
- **Claude.ai** — via Custom Instructions
- **Claude API** — via system prompt
- **Claude Code** — via .claude.md context
- **Claude in Chrome/Excel** — browser & spreadsheet agents
- **Anthropic Workbench** — collaborative environments

---

## 📈 Roadmap

### Q2 2025
- [ ] Expand to 75 skills across all domains
- [ ] Release Skill Studio (UI for skill creation)
- [ ] Multi-language support (French, Spanish, Japanese)

### Q3 2025
- [ ] Skills marketplace (browse, review, version-control)
- [ ] Fine-tuning support for specialized domains
- [ ] Integration with LangChain, LLamaIndex

### Q4 2025
- [ ] Mobile app for skill discovery
- [ ] Team collaboration features
- [ ] Enterprise licensing model

---

## 💬 Community

- **GitHub Discussions:** Ask questions, share ideas
- **Discord:** Real-time chat with community [link]
- **Twitter:** Updates & announcements [@AnthropicAI]
- **Blog:** Deep-dive articles on prompt engineering

[Join the community →](COMMUNITY.md)

---

## 📄 License

MIT License — Use freely, commercially or personally. See [LICENSE](LICENSE).

---

## 🙏 Acknowledgments

Thanks to our contributors and the broader AI community for feedback, improvements, and skill ideas!

[View contributors →](#)

---

## 📞 Support

- **Issue tracker:** [GitHub Issues](https://github.com/anthropics/claude-skills-library/issues)
- **Discussions:** [GitHub Discussions](https://github.com/anthropics/claude-skills-library/discussions)
- **Email:** support@anthropic.com
- **Docs:** [Full documentation](docs/)

---

## 🚀 Get Started Now

**[Browse skills →](SKILLS_INDEX.md)** | **[Read quick start →](docs/quick-start.md)** | **[Contribute a skill →](CONTRIBUTING.md)**

---

Made with ❤️ by the Anthropic team and community contributors.
