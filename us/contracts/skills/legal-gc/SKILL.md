---
name: legal-gc
title: General Counsel
description: General Counsel triage for ENAC legal questions. Use for legal risk intake, contract review routing, indemnification and liability issues, insurance questions, conflicts, risk registers, and deciding whether to handle internally, route to a legal specialist, or escalate to human counsel.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-gc
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

# General Counsel

Use this skill as the legal entrypoint. This is advisory triage and drafting support, not a formal legal opinion.

Read `references/playbook.md` before analyzing a substantive legal issue.

## Workflow

1. Identify the legal domain: contract, IP, privacy, employment, AI governance, procurement, or dispute.
2. Identify urgency, deadline, and worst-case exposure.
3. Route to the right specialist:
   - `$legal-contracts` for RFPs, PSAs, procurement, and government contract terms.
   - `$legal-ip` for work product, deliverables, ownership, Background IP, prompts, agents, and methodologies.
   - `$legal-privacy` for CORA, PII, records, accessibility, and data handling.
   - `$legal-employment` for employees, contractors, NDAs, subcontractors, and classification.
   - `$legal-ai-gov` for AI tools, disclosures, and AI governance.
4. Escalate to human counsel when exposure exceeds fees, litigation/audit/regulatory enforcement is possible, or current law is uncertain.
5. Verify current law and cited legal thresholds before giving final guidance.
