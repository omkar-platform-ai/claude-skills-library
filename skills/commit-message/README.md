# Commit Message Skill

Generate strict Conventional Commit compliant git commit messages aligned
with enterprise engineering standards and semantic versioning practices.

## Skill Structure

```text
commit-message/
├── SKILL.md
├── README.md
└── references/
    ├── conventional-commits.md         ← Spec + SemVer mapping
    └── commit-message-anti-patterns.md ← Common mistakes to avoid
```

## How to Trigger

Naturally invoke this skill by saying things like:

- "Write a commit message for these changes"
- "Generate a conventional commit"
- "Commit the staged changes"
- "Create a semantic commit for this fix"
- "Summarize these changes into a commit message"

## What You Get

A single line (or line + breaking-change footer) in the form:

```text
type(scope): summary
```

With no AI attribution, no `Co-Authored-By`, no emojis, and no trailing
period — ready to paste into `git commit -m`.
