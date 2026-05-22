# Tools & Scripts

## skill-validator.py
Validates skill structure and YAML syntax.
```bash
python tools/skill-validator.py skills/my-skill/
```

## eval-runner.py
Runs evaluation test cases against Claude API.
Requires: `ANTHROPIC_API_KEY` environment variable
```bash
ANTHROPIC_API_KEY=sk-... python tools/eval-runner.py skills/my-skill/evals/eval_set.json
```

## skill-packager.py
Packages a skill folder into a .skill file for distribution.
```bash
python tools/skill-packager.py skills/my-skill --output ./dist/
```

## More tools coming soon
- migration-assistant.py (convert old prompts to skills)
- eval-viewer.py (visualize eval results)
