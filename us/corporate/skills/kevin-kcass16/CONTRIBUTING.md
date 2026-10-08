# Contributing to Kevin

Thanks for wanting to make Kevin smarter. AI law is moving fast and Kevin needs all the help he can get.

## What We Need Most

**Regulatory updates** are the highest-impact contributions. When a new AI law passes, an enforcement action drops, or a court issues a ruling that affects AI startups, Kevin needs to know about it. If you spot something before we do, open a PR.

**Contract clause improvements** from real-world negotiations are gold. If you've battled through an AI vendor contract and came out with better language than what Kevin currently suggests, share it.

**New jurisdiction coverage** is critical as AI regulation goes global. Kevin currently covers EU, US (federal + key states), UK, and Dubai/DIFC. If you can add Singapore, Australia, Japan, South Korea, Brazil, India, or others — that's a meaningful contribution.

**New workflows** for common legal tasks Kevin doesn't yet cover (e.g., AI-specific terms of service, AI model cards, algorithmic impact assessments, AI procurement RFP language).

**Bug fixes** — if Kevin cites the wrong article number, applies an outdated deadline, or gives advice that's just wrong, please flag it.

## How to Contribute

### Using an AI agent (recommended for legal professionals)

This repo includes a `CLAUDE.md` file that teaches AI agents the repo structure, style rules, and exactly which files to update for any type of change. You don't need to know the codebase — just describe the legal change and the agent handles the rest.

1. **Fork** the repository and clone it locally
2. Open the repo in **Claude Code**, **Cursor**, **Codex**, **OpenCode**, or any [supported agent](https://skills.sh)
3. Tell the agent what to change in plain English, for example:
   - *"Add Singapore PDPA coverage to Kevin's knowledge base"*
   - *"Update the EU AI Act high-risk deadline to reflect the Digital Omnibus extension"*
   - *"Add a new workflow for AI model cards"*
   - *"The indemnification clause in Section 4 should also cover algorithmic discrimination claims"*
4. The agent will read `CLAUDE.md`, identify the right files, apply the style guide, and make the changes
5. Review the changes, test by running a few prompts, and submit a PR

### Manual contribution

1. **Fork** the repository
2. **Create a branch** with a descriptive name:
   - `add/singapore-pdpa-coverage`
   - `update/eu-ai-act-august-2026-deadline`
   - `fix/caia-effective-date`
   - `workflow/ai-terms-of-service`
3. **Make your changes** following the style guide below
4. **Test locally** by installing the skill and running a few prompts
5. **Submit a PR** with a clear description of what changed and why

## Style Guide

Kevin has a voice. Please match it:

- **Plain English first.** Translate legalese. If you must use a legal term, define it.
- **Always cite authority.** Every legal claim must reference a specific article, section, or regulation number. Never make unsourced legal assertions.
- **Risk-tag everything.** Use `LOW` / `MEDIUM` / `HIGH` / `CRITICAL` consistently.
- **Provide model language.** Don't just say "add an indemnification clause" — write the actual clause text.
- **Be honest about uncertainty.** If the law is unsettled, say so. Kevin never fabricates certainty.
- **Startup-aware.** Balance legal protection with business velocity. Perfect is the enemy of shipped.

## File-Specific Guidelines

### SKILL.md
This is the main file loaded into context. Keep it under 500 lines. It should contain quick references, not deep analysis. If you're adding significant content, it probably belongs in a reference file instead.

### references/knowledge-base.md
Kevin's deep knowledge. Organized by topic (regulatory landscape, contracts, privacy, security, IP, etc.). Add new sections or expand existing ones. Always include the legal authority and practical guidance.

### references/workflows.md
The 10 structured workflows. Each follows the same format: Trigger → Input → Legal Framework → Process → Output → Validation Criteria → Escalation Triggers. If you're adding a new workflow, follow this structure exactly. If you're improving an existing one, maintain the structure.

## What NOT to Submit

- Promotional content for specific legal tech products or law firms
- Advice designed to help users evade regulations or deceive regulators
- Fabricated legal citations or made-up case law
- Content copied from copyrighted legal publications without permission
- Changes that remove the legal disclaimer or weaken Kevin's "I'm not a lawyer" messaging

## Questions?

Open an issue. We're friendly.
