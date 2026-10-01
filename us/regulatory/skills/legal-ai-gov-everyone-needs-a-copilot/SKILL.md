---
name: legal-ai-gov-everyone-needs-a-copilot
title: AI Governance Counsel
description: AI Governance and Ethics Counsel for ENAC. Use for AI-assisted consulting disclosures, Colorado AI Act assessment, AI vendor terms, government proposal AI language, high-risk AI triage, human review checkpoints, model/tool inventories, and AI clauses in contracts.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-ai-gov
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
sources:
- title: Playbook
  path: references/playbook.md
---

# AI Governance Counsel

Use this skill for AI governance in client work. This is advisory drafting and risk analysis, not a formal legal opinion.

Read `references/playbook.md` before analyzing substantive AI governance issues.

## Required Skills

Load relevant skills:

- `legal-compliance`
- `colorado-ai-act`
- `legal-review`

## Workflow

1. Identify the AI tools, use cases, data inputs, outputs, and human review points.
2. Assess whether the use could be high-risk or tied to a consequential decision.
3. Draft proposal disclosure language when government clients are involved.
4. Document tool inventory, model versions, review checkpoints, and data handling.
5. Route ownership issues to `$legal-ip` and data issues to `$legal-privacy`.
6. Verify current statutes, effective dates, and vendor terms before final guidance.
