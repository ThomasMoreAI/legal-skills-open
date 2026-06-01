---
name: legal-industry-workflows
title: Legal industry workflows
description: Build reusable, practice-specific legal workflows with Claude by collecting context via a short setup interview and producing grounded, verifiable work product across documents and tools.
author: uygnoey
author_url: https://github.com/uygnoey/skills-from-claude-blog/tree/main/2026.05.12_claude-for-the-legal-industry/skills/legal-industry-workflows
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal industry workflows

## Instructions

Use this skill to convert a recurring legal task into a repeatable workflow that:

1) **Collects context once** via a short setup interview.
2) **Runs a structured task checklist** (draft/redline/triage/etc.).
3) **Produces a verifiable work product** with citations to authoritative sources and an explicit escalation path.

### Setup interview (required)
Ask the user for the items in [templates/setup-interview.md](./templates/setup-interview.md), then confirm:
- What you will do and what you will not do.
- The risk calibration and when to escalate.
- The preferred deliverable format (email, memo, redline notes, checklist).

### Work product requirements
Follow the “trusted legal work product” style in [output-styles/trusted-legal-work-product.md](./output-styles/trusted-legal-work-product.md).

### Common workflows (pick one)
Use the checklists in [references/workflow-checklists.md](./references/workflow-checklists.md):
- Contract drafting / redlining
- Matter intake triage
- Regulatory update sweep
- Product launch review

### Bundled resources
- Setup interview template: [templates/setup-interview.md](./templates/setup-interview.md)
- Workflow checklists: [references/workflow-checklists.md](./references/workflow-checklists.md)
- Sample deliverables: [examples/sample-outputs.md](./examples/sample-outputs.md)

## Examples

### Example: matter intake triage
1) Run the setup interview.
2) Apply “Matter intake triage” checklist.
3) Deliver:
- Summary for the business
- Legal risk classification
- Missing information requests
- Escalation recommendation

### Example: contract redline support
1) Run the setup interview.
2) Apply “Contract drafting / redlining” checklist.
3) Deliver:
- Clause-by-clause issues list
- Proposed fallback language locations (by playbook section)
- Rationale for each change
- Final send-ready checks (formatting, comment scrubbing)

## Source
- https://claude.com/blog/claude-for-the-legal-industry
