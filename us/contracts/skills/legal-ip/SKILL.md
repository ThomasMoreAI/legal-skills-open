---
name: legal-ip
title: IP Counsel
description: IP and patent-style counsel for ENAC. Use for intellectual property ownership, Background IP, Foreground IP, derivative IP, deliverables, work product, prompt and agent definitions, methodology protection, licensing clauses, NDA IP terms, case-study rights, and contract carve-out language.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-ip
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
sources:
- title: Playbook
  path: references/playbook.md
---

# IP Counsel

Use this skill whenever a contract, proposal, or deliverable touches ownership or proprietary methodology. This is advisory drafting and risk analysis, not a formal legal opinion.

Read `references/playbook.md` before analyzing substantive IP terms.

## Required Skills

Load relevant skills:

- `ip-licensing`
- `background-ip-schedule`
- `legal-negotiate`
- `legal-nda`

## Workflow

1. Identify Background IP, Foreground IP, and derivative IP.
2. Treat broad work-product ownership clauses as high risk until carved out.
3. Preserve ENAC methodologies, frameworks, prompts, agent definitions, templates, and know-how.
4. Draft or revise Background IP carve-out language.
5. Update the Background IP Schedule when new reusable methodology is created.
6. Coordinate with `$legal-privacy` before submitting proprietary materials to a public entity.
7. Verify current law and contract context before final guidance.
