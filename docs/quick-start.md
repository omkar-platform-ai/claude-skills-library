# Quick Start Guide

## Installation (1 minute)

### Option 1: Claude.ai Custom Instructions
1. Go to Settings → Custom Instructions
2. Toggle ON
3. Paste skill content into System field
4. Done!

### Option 2: Claude Code / API
```python
from anthropic import Anthropic

with open("investment-analyst-skill.skill") as f:
    skill = f.read()

response = Anthropic().messages.create(
    model="claude-opus-4-20250805",
    system=skill,
    messages=[{"role": "user", "content": "..."}]
)
```

## First Use (2 minutes)

Ask Claude naturally:
> "I'm 35, have ₹50L to invest, moderate risk, 15-year horizon. Build me a portfolio."

Claude automatically applies the investment-analyst skill and delivers analysis.

## Tips
- Skills work best with clear, specific inputs
- Provide complete investor/context information
- Ask follow-up questions to refine recommendations

[More guides →](index.md)
