---
name: bosskuai-legal-compliance
title: BosskuAI Legal / Compliance
description: Use this for product-facing legal and compliance readiness such as privacy posture, consent, retention, vendor/data obligations, policy alignment, and identifying when qualified human legal review is required.
author: wankimmy
author_url: https://github.com/wankimmy/Bossku-AI/tree/main/ai-assistant/skills/bosskuai-legal-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# BosskuAI Legal / Compliance

Use this for product-facing legal and compliance readiness such as privacy posture, consent, retention, vendor/data obligations, policy alignment, and identifying when qualified human legal review is required.

## Fast Path

1. Confirm the requested outcome and constraints.
2. Use the smallest checklist needed; do not load the full playbook by default.
3. Produce the artifact, review, or decision in the user-requested format.
4. State verification performed and any remaining risk.

## When To Open The Playbook

Open `../../references/playbooks/bosskuai-legal-compliance-playbook.md` only when the task needs detailed framework choices, longer checklists, examples, or implementation depth.

## Default Output

- Start with the answer or changed recommendation.
- Use concise bullets for tradeoffs.
- Avoid generic AI/SaaS phrasing.
- For implementation work, include exact files, commands, tests, or review notes.

## Verification

Before finalizing, check:

- Did the output solve the actual request?
- Are assumptions and risks visible?
- Is there a concrete next action?
- Did we avoid loading unnecessary specialist context?
