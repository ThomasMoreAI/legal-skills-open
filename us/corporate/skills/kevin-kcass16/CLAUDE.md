# Kevin — Repo Guide for Claude

This is the GitHub repository for **Kevin**, an open-source agent skill that serves as an AI legal sidekick for AI startups. This file tells you how the repo is organized and how to make changes correctly.

## Repo Structure

```
kevin/
├── SKILL.md                          # Core skill file — personality, workflow router, quick references, model clauses
├── references/
│   ├── knowledge-base.md             # Deep legal knowledge base (~875 lines)
│   └── workflows.md                  # 10 structured legal workflows (~1,536 lines)
├── assets/                           # Logo, social preview card, screenshots
├── README.md                         # Public-facing documentation
├── CONTRIBUTING.md                   # Contributor guidelines and style guide
├── CHANGELOG.md                      # Version history (Keep a Changelog format, SemVer)
├── CODE_OF_CONDUCT.md                # Contributor Covenant v2.1
├── SECURITY.md                       # Responsible disclosure policy
├── LICENSE                           # MIT
├── .gitignore
└── .github/
    ├── FUNDING.yml                   # GitHub Sponsors (kevincassidy)
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        ├── feature_request.md
        └── regulatory_update.md
```

## How the Skill Works

Kevin is an agent skill that follows the open [Agent Skills](https://github.com/vercel-labs/skills) standard. Agents load it in three layers:

1. **Always in context:** The YAML frontmatter in SKILL.md (`name` and `description`, ~100 words). This is what tells the agent when to activate Kevin.
2. **On trigger:** The full SKILL.md body (~250 lines). This gives Kevin his personality, workflow selection table, contract checklist, regulatory quick references, model clauses, and threat model summary.
3. **On demand:** The reference files (`references/workflows.md` and `references/knowledge-base.md`) are read only when Kevin needs deeper detail for a specific workflow or question.

## How to Make Changes

### Adding a new regulatory framework or jurisdiction

1. Add the substantive legal content to `references/knowledge-base.md` in the appropriate section (regulatory landscape, privacy, etc.)
2. If the regulation affects any of the 10 workflows, update the relevant workflow in `references/workflows.md` — specifically the "Legal Framework" and "Process" steps
3. Add a quick-reference entry to `SKILL.md` if the regulation is important enough to surface at the top level (e.g., a new entry in the EU AI Act Quick Reference, a new row in the Key Definitions table, or a new threat in the Threat Model Quick Reference)
4. Update `CHANGELOG.md` under the next version heading with what was added
5. Update the "Regulatory Coverage" section of `README.md` if it's a major framework

### Adding a new workflow

1. Add the workflow to `references/workflows.md` following the exact structure of existing workflows: **Trigger → Input → Legal Framework → Process → Output → Validation Criteria → Escalation Triggers**
2. Add a row to the workflow selection table in `SKILL.md` (the "Workflow Selection" section)
3. Add any new legal knowledge needed by the workflow to `references/knowledge-base.md`
4. Update `CHANGELOG.md`
5. Update the workflow count in `README.md` if it changes (currently "10 structured workflows")

### Updating an existing workflow

1. Edit the workflow in `references/workflows.md`
2. If the change affects the quick references in `SKILL.md` (e.g., a new contract review checklist item, updated risk scores, new model clause), update those too
3. Update `CHANGELOG.md`

### Updating model contract clauses

1. Edit the clause in `SKILL.md` under the "Model Contract Clauses" section
2. If the clause is referenced in a workflow process, check that `references/workflows.md` still aligns
3. Update `CHANGELOG.md`

### Updating regulatory deadlines

1. Update the deadline in `references/knowledge-base.md`
2. Update the timeline in `SKILL.md` (EU AI Act Quick Reference section) if applicable
3. Update the "Key Regulatory Deadlines" table in `README.md`
4. Check `references/workflows.md` for any hardcoded dates that need updating
5. Update `CHANGELOG.md`

### Adding or updating threat model entries

1. Update the threat in `references/knowledge-base.md` Section 6 (the full threat model)
2. Update the summary table in `SKILL.md` under "AI Threat Model Quick Reference" (the 18-row table)
3. Update `CHANGELOG.md`

## Style Rules

These rules are defined in `CONTRIBUTING.md` and must be followed in all files:

- **Plain English first.** Translate legalese. If you must use a legal term, define it.
- **Always cite authority.** Every legal claim must reference a specific article, section, or regulation number. Never make unsourced legal assertions.
- **Risk-tag everything.** Use `LOW` / `MEDIUM` / `HIGH` / `CRITICAL` consistently per the scoring framework in SKILL.md.
- **Provide model language.** Don't just describe what a clause should do — write the actual clause text.
- **Be honest about uncertainty.** If the law is unsettled, say so. Kevin never fabricates certainty.
- **Startup-aware.** Balance legal protection with business velocity.

## File Size Guidelines

- **SKILL.md** should stay under 500 lines. It's loaded into context on every trigger, so keep it to quick references and summaries. Deep content belongs in the reference files.
- **references/knowledge-base.md** and **references/workflows.md** have no hard limits — they're only read on demand when Kevin needs the detail.

## Versioning

This project uses [Semantic Versioning](https://semver.org/):

- **PATCH** (1.0.x): Regulatory date corrections, typo fixes, clarifications that don't change advice
- **MINOR** (1.x.0): New workflows, new jurisdiction coverage, new model clauses, significant knowledge base additions
- **MAJOR** (x.0.0): Breaking changes to workflow structure, major restructuring of SKILL.md, changes to the skill's name or description frontmatter

Update `CHANGELOG.md` with every change. Follow [Keep a Changelog](https://keepachangelog.com/) format.

## Things to Never Do

- Remove or weaken the legal disclaimer ("I'm Kevin, your AI legal sidekick — not a licensed attorney...")
- Fabricate legal citations, case law, or regulatory requirements
- Add advice designed to help users evade regulations
- Change the `name` field in SKILL.md frontmatter without updating the README
- Add external dependencies (API keys, binaries, network calls) — Kevin works entirely within the agent's context

## Contact

- Maintainer: Kevin Cassidy
- Email: kcass16@gmail.com
- GitHub: github.com/kcass16/kevin
