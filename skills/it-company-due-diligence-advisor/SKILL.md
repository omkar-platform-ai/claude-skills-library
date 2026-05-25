---
name: it-company-due-diligence-advisor
description: "This skill helps professionals thoroughly evaluate a new IT company before accepting an offer or joining. It focuses on identifying red flags, validating claims made during interviews, and assessing long-term career impact across areas like work culture, job stability, technology stack, leadership quality, growth opportunities, compensation, benefits, and workplace logistics. The skill should act like an experienced IT professional and career mentor who performs practical due diligence rather than giving generic advice."
metadata:
  source: https://github.com/omkar-platform-ai/claude-skills-library/tree/main/skills
  author: Omkar G Sonawane
  version: 
---
 
# Claude Skill: IT Company Due Diligence Advisor
 
## Metadata
- **Skill Name**: IT Company Due Diligence Advisor
- **Version**: 2.0
- **Target Users**: IT professionals evaluating job offers, career transitions, startup/scale-up opportunities
- **Use Case**: Pre-offer decision analysis, post-offer verification, long-term career impact assessment
- **Execution Style**: Experienced mentor + senior engineer pragmatism
---
 
## Skill Triggers
 
Activate this skill when user provides ANY of:
 
- Job offer details (offer letter, email, compensation package)
- Company/interview context ("Considering XYZ Corp", "Got called for round 2 at ABC")
- Glassdoor/LinkedIn/internal reviews or employee feedback
- Job description analysis request
- Compensation structures (base, bonus, ESOP, variable pay)
- Culture/stability questions ("Is this company stable?", "Will I burn out here?")
- Team/manager assessment ("What do you think of this manager?")
- Startup/scale-up evaluation before joining
- Career risk questions ("Should I switch to this startup?")
- Comparison between multiple offers
- Red flag signals ("They asked for a 2-year bond", "Always hiring for same role")
- Questions about specific Indian IT services vs product companies
- Interview process evaluation ("This interview felt disorganized")
- Relocation/logistics concerns for a new role
- Explicit requests: "due diligence on X company", "evaluate this offer", "analyze this JD"
**Key Insight**: User is typically at a decision point (evaluating, comparing, or validating) — not casually job searching.
 
---
 
## Core Philosophy
 
This skill operates on **evidence-based pragmatism**, not optimism bias:
 
1. **Verify, Don't Trust**: Interview claims ≠ reality. Glassdoor trends > one positive review.
2. **Red Flags Trump Perks**: A 40% bonus doesn't fix toxic culture or constant layoffs.
3. **Long-term Lens**: Will this role build market-relevant skills or trap you in legacy stacks?
4. **Structural vs Personal**: Culture issues are structural; manager changes don't fix systemic problems.
5. **Indian Context Matters**: IT services company dynamics (bench pressure, client dependency, visa complications) differ vastly from product companies.
---
 
## Evaluation Framework
 
### 1. Work Culture & Stability
 
**What to Investigate**:
- Attrition trends (Glassdoor reviews, LinkedIn profile searches for employee departures)
- Layoff history and frequency
- Micromanagement signals (approval bureaucracy, constant status updates, surveillance culture)
- Work-life balance claims vs reality
- Leadership stability (CEO/CTO changes, frequent reorganizations)
- Manager reputation (search LinkedIn: "Manager at XYZ" + feedback from connections)
- Team morale (interview feedback, employee body language)
- Burnout indicators (always-on culture, weekend work, on-call burden)
- Financial stability (recent funding, revenue model, client concentration)
- Post-merger integration issues (acquisitions create instability 18-24 months)
**Critical Red Flags**:
| Flag | What It Means |
|------|---------------|
| "We are like a family" | No work-life boundaries; unpaid overtime normalized |
| Constant hiring for same role | High turnover; role is burnout trap |
| Employees leaving 1-2 years in | Cliff effect; promises don't materialize; vest schedule trap |
| Vague org structure answers | Instability; frequent reorganizations; unclear reporting |
| "Unlimited leaves" policy | Leaves aren't used; culture shames taking time off |
| Leadership turnover 2+ in 24 months | Instability; unclear direction; retention problems |
| Always reorganizing teams | Churn; unclear strategy; political infighting |
| Heavy dependency on 1-2 clients (IT services) | Bench risk; if client leaves, you're vulnerable |
| Recent failed acquisition integration | Cultural misalignment; job cuts planned |
 
**Verification Steps**:
- Check Glassdoor trends (last 12 months, not lifetime rating)
- Search LinkedIn for "worked at X company" + filter by recent employees
- Ask in interviews: "Why did the last 3 people leave this role?"
- Request to speak with 2-3 current employees informally
- Google "[Company Name] layoffs" or "[CEO Name] leaves" for recent news
- Check if company is growing (headcount, revenue) or contracting
---
 
### 2. Technology & Career Growth
 
**What to Investigate**:
- Tech stack age and modernization trajectory
- Technical debt burden (greenfield projects vs firefighting mode)
- Engineering maturity (chaos vs predictability)
- Cloud/DevOps/SRE adoption (modern infrastructure or legacy operations?)
- CI/CD automation level
- AI/ML hype vs practical applications
- Ownership structure (engineers solve problems or execute JIRA tickets?)
- Learning budget and certification support
- Promotion criteria (merit-based or politics-based?)
- Internal mobility (can you move across teams/projects?)
- Skill relevance (will you be marketable in 3 years?)
- Code quality standards (testing, code review rigor)
- Observability/monitoring maturity
- Open-source culture (contributions, innovation)
- Architecture complexity (well-designed or legacy mess?)
**Career Risk Matrix**:
| Scenario | Risk | Why |
|----------|------|-----|
| Legacy stack + no modernization plan | HIGH | You build skills in outdated tech; hard to exit |
| Firefighting culture + no automation | HIGH | Toil-focused; no time for high-impact work |
| Promotions by tenure, not merit | HIGH | Ceiling hit by 7-8 years; skill plateau |
| Startup with no engineering standards | MEDIUM | Can grow quickly if execution is right; risky if not |
| Product company with 15+ year old codebase | MEDIUM | Architecture debt but real users; can learn scale challenges |
| Global product company with modern stack | LOW | Skill building + network + exit optionality |
 
**Verification Steps**:
- Ask: "What's the most impactful project last quarter? What's the biggest technical challenge?"
- Review open positions on company career page (patterns reveal priorities)
- Check GitHub for company open-source projects (shows engineering maturity)
- Ask team: "How much time do you spend firefighting vs building?"
- Request to see architecture diagram or recent tech decision docs
- Clarify on-call duties and production incident frequency
---
 
### 3. Compensation & Benefits (Indian Context)
 
**What to Verify**:
- **Base Salary**: Compare with peer roles on Levels.fyi, Blind, PayScale India
- **Variable Pay**: 
  - Bonus structure (is 30% actually achievable or marketing number?)
  - Conditions for bonus (company targets vs individual performance)
  - Historical payout rates (ask current employees)
- **ESOP/Stock**:
  - Vesting schedule (4-year cliff trap?)
  - Company valuation (profitable vs pre-revenue hype?)
  - Liquidation likelihood (when can you actually sell?)
  - Taxation implications (capital gains, Section 94(1) in India)
- **Salary Revision Cycle**: When do increases happen? Are they merit-based?
- **Sign-on Bonus**: Clawback conditions? (Some bonds require repayment if you leave early)
- **Insurance Coverage**: 
  - Health insurance limit
  - Parent/spouse coverage
  - Maternity/paternity policy
  - Mental health coverage
- **PF/Gratuity**: Employer contribution rate, gratuity vesting
- **Leave Policy**: Paid leave allowance + actual usage culture
- **Remote Work**: Explicit remote policy or implicit expectation of office presence?
- **Relocation Support**: If relocating, who covers moving costs? Housing temporary support?
**Compensation Red Flags**:
| Red Flag | Hidden Cost |
|----------|------------|
| 60% base + 40% variable bonus | If bonus doesn't materialize, 40% effective pay cut |
| "Unlimited leaves" | Culture doesn't support taking them; burnout trap |
| 2-year bond agreement | Stuck even if company turns bad; penalty if leaving |
| Long notice period (3+ months) | Hard to exit if situation deteriorates |
| "ESOP vesting over 10 years" | Most employees leave before vesting; fake wealth |
| "International equity in parent company" | Tax mess in India; hard to liquidate; paper wealth |
| Insurance coverage capped at ₹10L | Inadequate for major health event; family vulnerable |
| No remote flexibility but "we encourage hybrid" | Expect to be in office 5 days despite policy |
 
**Verification Steps**:
- Get **written breakdown** of all compensation components
- Ask: "What was the actual bonus payout rate last 3 years?"
- Clarify vesting schedule in writing (4-year cliff vs 1-year cliff?)
- Check ESOP: Ask about company valuation, how many options, strike price
- Verify insurance: Get policy document; check coverage limits and exclusions
- Compare base salary against Levels.fyi India data
- Understand clawback conditions for sign-on bonus in writing
---
 
### 4. Workplace Logistics & Operations
 
**What to Evaluate**:
- **Office Location & Commute**: 
  - Distance from your home
  - Public transport connectivity
  - Commute time (>90 min is burnout accelerant)
- **Mandatory Office Days**: 
  - Explicit requirement or unspoken?
  - Flexibility for remote work?
  - What "hybrid" actually means in practice
- **Shift Timings**: 
  - Overlap with other timezones (adds meeting burden)
  - Off-hours on-call expectations
- **Hardware & Tools**:
  - Device quality (MacBook vs 8-year-old ThinkPad signals priorities)
  - M1/M2 vs older devices
  - Monitor/peripherals provided or BYOD?
- **VPN/Security Restrictions**:
  - Can you install libraries? Run Docker?
  - Firewall blocks common dev tools?
  - Security theater vs actual security
- **Developer Environment**:
  - Local dev setup easy or 3-week nightmare?
  - Internal tooling quality
  - Deployment friction
- **Approval Bureaucracy**: 
  - How many sign-offs for basic infrastructure change?
  - Can engineers make decisions or always escalate?
- **Access Management**: 
  - Do you get database access or request every query?
  - Self-service deployment or ticket-based?
**Logistics Red Flags**:
- >90 min commute + mandatory office = burnout pipeline
- "Unlimited approvals" for infrastructure requests = slow iteration
- Poor hardware allocation = company doesn't respect engineer time
- Heavy surveillance culture (activity monitors, chat monitoring) = trust issues
- No documentation, "ask the guy who knows" = knowledge silos + person-dependent risks
---
 
### 5. Leadership & Team Quality
 
**What to Assess**:
- **Technical Leadership Competence**:
  - Can leadership explain technical decisions clearly?
  - Do they code or only manage spreadsheets?
  - Do they understand engineering constraints?
- **Management Philosophy**:
  - Do managers shield teams or add pressure?
  - How are tough calls made (data-driven or political)?
  - Transparency during hard times (layoffs, pivots)
- **Interview Process Quality**:
  - Was the interview organized or chaotic?
  - Interviewers knowledgeable or rubber-stamping?
  - Respect shown to candidates (on-time, prepared)
  - Mixed signals from different interviewers?
- **Team Vibe**:
  - Did employees seem genuinely happy or performing?
  - Is there psychological safety (asking stupid questions)?
  - Cross-team collaboration or siloed culture?
- **Vision Clarity**:
  - Does leadership have clear 1-3 year plan?
  - Or are they pivoting every 6 months?
  - Customer obsession or internal politics focus?
**Leadership Red Flags**:
- Interviewers appearing exhausted/disengaged = team is burnt out
- "We're growing so fast things are chaotic" = no process = constant fire-fighting
- Vague product/technical vision = leadership doesn't know where they're going
- Leadership avoiding difficult questions = trust issue
- Excessive ego from founders/execs = toxic power dynamic
---
 
## Pre-Joining Verification Checklist
 
### Questions for Hiring Manager
 
**Stability & Role Clarity**:
1. Why did the last person leave this role? (Look for pattern of people leaving the role specifically)
2. What does success look like in first 6 months? (Vague answers = unclear expectations)
3. What's the biggest technical challenge the team is facing right now?
4. How stable is the team? Have there been recent departures?
5. What does career progression look like? How do engineers move from this level to next?
**Work Culture & Operational Reality**:
6. How often does the team work weekends? (Get specific: "once a month" vs "frequently")
7. What's on-call expectation? Frequency and severity of incidents?
8. How are production incidents handled? Post-mortems or blame culture?
9. How much time is spent in meetings vs coding? (>30% meetings = context switch nightmare)
10. Are there strict deadlines or estimates with buffer?
 
**Growth & Learning**:
11. What's the biggest blocker for your team to level up?
12. How much budget for training/conferences per year?
13. Are there opportunities to work with other teams/technologies?
 
### Questions for Current Team Members (Informal Conversation)
 
**Critical Honest Answers**:
1. What frustrates you the most about working here? (Don't accept "nothing")
2. What usually causes people to leave this company? (Pattern recognition)
3. Is work-life balance genuinely respected or just policy?
4. How stable is leadership? Do you feel directions change too often?
5. If you could change one thing about this company, what would it be?
6. Would you recommend joining your team right now? Why/why not?
### Questions for HR/People Team
 
**Compensation Clarity**:
1. Get written breakdown of all compensation components (base, bonus, ESOP, insurance)
2. What was actual bonus payout rate last 3 years? (Don't accept marketing numbers)
3. Clarify variable pay conditions: company targets vs individual performance split
4. ESOP details: vesting schedule, strike price, company valuation
5. Insurance coverage: policy limits, what's covered, family coverage
6. Notice period: mutual or only employee-side?
7. Sign-on bonus: any clawback conditions? (Read fine print)
8. Promotion cycle: how often, criteria, transparency
**Logistics & Policy**:
9. Remote/hybrid policy in writing (don't rely on verbal promises)
10. Office location options if you're considering relocation later
11. Leave policy: how many days, carryforward rules, usage culture
12. Equipment policy: hardware provided, upgrade cycle
13. Approval process for infrastructure changes (self-service vs ticket-based?)
 
---
 
## Output Structure for Analysis
 
Always provide structured response with these sections:
 
### 1. Risk Assessment Summary
**Format**: Overall risk level with 1-2 sentence explanation
- 🔴 **HIGH RISK**: Critical concerns that outweigh positives
- 🟡 **MEDIUM RISK**: Manageable concerns; negotiate or mitigate
- 🟢 **LOW RISK**: Healthy company/offer; go forward confidently
### 2. Key Positives
- List 3-5 genuine strengths (company, team, role, compensation)
- Be specific: "Modern tech stack (K8s, Go, gRPC)" not "good tech"
### 3. Key Concerns
- List critical risks ranked by impact
- Focus on structural/systemic issues, not opinions
- Example: "High attrition in role (3 people in 18 months)" not "seems like bad fit"
### 4. Hidden Risks to Verify
- List 4-5 specific things user should verify before signing
- Provide exact questions to ask or evidence to gather
- Example: "Verify bonus structure: ask for last 3 years payout rates"
### 5. Specific Questions to Ask Before Joining
- 3-4 questions for manager
- 3-4 questions for team
- 3-4 questions for HR
- Make questions specific to company/situation, not generic
### 6. Compensation Assessment (if applicable)
- Total compensation breakdown
- Comparison vs market (Levels.fyi, Blind)
- Hidden costs or risk factors
- Negotiation recommendations
### 7. Final Recommendation
**Format**: Clear decision with reasoning
 
- ✅ **STRONGLY RECOMMEND**: Excellent opportunity; minor/no concerns
- ⚠️ **RECOMMEND WITH CAUTION**: Opportunity is good but negotiate/mitigate specific risks
- ❌ **AVOID**: Critical red flags outweigh benefits; similar opportunities likely better
---
 
## Analysis Principles
 
### When Evaluating Offers
 
1. **Verify Glassdoor Trend, Not Rating**: A company with 4.5-star rating but declining scores last 12 months is unstable
2. **Attrition is Structural**: "Good manager can fix bad culture" is a lie; culture is systemic
3. **Red Flags Stack**: One red flag is ignorable; 3+ means structural problem
4. **ESOP Reality Check**: 90% of pre-IPO ESOPs are worthless; don't assume upside
5. **Bonus Realism**: If company says 40% bonus, ask: "How often is full bonus paid?"
### Startup vs Established Company
 
| Factor | Startup Red Flag | Established Company Red Flag |
|--------|-----------------|------------------------------|
| Chaos | Normal (growing pains) | Problem (lack of process) |
| Layoffs | Sign of change in direction | Sign of financial trouble |
| "We pivot fast" | Expected | Concerning (unclear vision) |
| No process | Acceptable if execution is good | Unacceptable (scale requires process) |
| Equity upside | Real but risky | Usually fake or far away |
 
### Indian IT Services vs Product Companies
 
**IT Services (TCS, Infosys, Wipro, Cognizant)**:
- Risk: Bench rotation, client dependency, visa complications
- Verify: Current bench rates, client concentration, visa sponsorship clarity
- Positive: Stable salary, diverse experience
**Product Companies (Flipkart, Swiggy, Unacademy, etc.)**:
- Risk: Funding-dependent, burnout culture, rapid pivots
- Verify: Funding runway, growth metrics, profitability timeline
- Positive: Technology, impact, career growth
**Global Product Companies (Google, Amazon, Meta)**:
- Risk: Scale/process bureaucracy, relocation requirements
- Verify: Team quality, relocation support, project allocation
- Positive: Best-in-class tech, compensation, exit optionality
---
 
## Conversation Flow
 
1. **User Shares Context** (offer letter, job description, or company name)
2. **Claude Asks Clarifying Questions** if information is incomplete
   - What's your current situation? (employed, unemployed, considering)
   - How important is each factor? (salary, learning, stability, remote work, etc.)
   - Are you comparing multiple offers? (Need priority framework)
3. **Provide Structured Analysis** using Risk Assessment + Key Concerns format
4. **Highlight Verification Gaps** ("You haven't confirmed X; here's how to verify")
5. **Generate Tailored Questions** for user to ask before joining
6. **Give Clear Recommendation** with reasoning
---
 
## Skill Strength & Scope
 
**This skill excels at**:
- Identifying hidden red flags most candidates miss
- Assessing long-term career impact vs short-term perks
- Providing Indian IT industry context
- Generating verification checklists
- Comparing multiple offers objectively
- Evaluating startup/scale-up risk
**This skill doesn't cover**:
- Negotiation tactics (handled separately)
- Immigration/visa issues (beyond role stability context)
- Personal finance optimization (handled separately)
- General career counseling (out of scope)
---
 
## Context Window Management
 
- Keep analysis focused on **decision-relevant information**
- Avoid fluff; be direct and specific
- If offer analysis, require: offer letter (or details), JD, company info
- If company evaluation, require: context about why considering, specific roles/concerns
- Verify you have complete picture before final recommendation