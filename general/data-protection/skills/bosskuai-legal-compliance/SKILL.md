---
name: bosskuai-legal-compliance
title: BosskuAI Legal / Compliance
description: Use this for product-facing legal and compliance readiness such as privacy posture, consent, retention, vendor/data obligations, policy alignment, and identifying when qualified human legal review is required.
author: wankimmy
author_url: https://github.com/wankimmy/Bossku-AI/tree/main/skills/bosskuai-legal-compliance
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# BosskuAI Legal / Compliance

Use this skill when the main question is **whether product, data, or operational behavior creates policy, privacy, or compliance obligations** that need to be surfaced early.

## How this differs from nearby skills

- **`bosskuai-cybersecurity-risk`**: focuses on security, abuse, and trust boundaries; this skill focuses on policy, regulatory, and contractual obligations around the product.
- **`bosskuai-product-strategy`**: decides what to ship; this skill checks which compliance constraints shape that decision.
- **`bosskuai-prompt-injection-defense`**: secures the AI workspace itself; this skill reviews legal/compliance implications in the product or business process.
- **`bosskuai-malaysia-pdpa-privacy`**: Malaysian PDPA specifics (breach notice, DPO, portability); this skill is jurisdiction-neutral issue-spotting.

## Mindset

- This is not legal advice; it is structured issue-spotting and readiness analysis.
- The goal is to surface obligations early enough that the team can involve qualified humans before shipping.
- Privacy, consent, retention, and vendor commitments are product requirements, not paperwork after launch.
- Ambiguous jurisdiction, data category, or contractual duty should trigger escalation, not confident guesswork.

## Compliance lenses

**Data and privacy**
- What personal, sensitive, or regulated data is collected or inferred?
- What is the lawful basis, consent model, or user expectation?
- Are retention and deletion behaviors defined?

**User-facing obligations**
- Are notices, consent, age gates, disclosures, or terms required?
- Do product flows behave consistently with published policy?
- Are user rights flows operationally possible?

**Operational and vendor obligations**
- Which vendors process data and under what terms?
- Are cross-border transfers, subprocessors, or DPAs relevant?
- Do internal roles and approvals exist for compliance-critical changes?

**Product and market scope**
- Which geographies, industries, or customer segments trigger stronger obligations?
- Are there regulated workflows such as health, finance, education, employment, or children’s data?
- What is intentionally unsupported and should be stated clearly?

**Escalation triggers**
- Is there ambiguity about jurisdiction, regulated data, contract commitments, or enforcement risk?
- Would a mistake materially affect user rights, revenue, or launch timing?
- If yes, escalate to qualified legal/compliance humans.

## Workflow

1. **Read the actual product and policy surface** — flows, forms, data handling docs, privacy copy, vendor lists, and security/compliance docs if present.
2. **Identify the regulated or policy-sensitive data and workflows** — collection, storage, sharing, retention, deletion, and consent.
3. **Map obligations to product behavior** — what the product says, what it does, and where they diverge.
4. **Review vendor and operational dependencies** — processors, transfers, contracts, approvals, and auditability.
5. **Identify escalation triggers** — what must go to qualified humans before launch or contract signature.
6. **Recommend the smallest compliance-hardening slice** — policy alignment, retention control, consent fix, documentation gap, or review gate.

## Guardrails

- Do not present this skill as legal advice.
- Do not guess jurisdiction-specific obligations when the facts are unclear.
- Do not assume a privacy policy fixes product behavior that contradicts it.
- Do not recommend shipping through unresolved high-risk compliance ambiguity.

## Output format

```text
Compliance summary:
  Product/workflow in scope: [summary]
  Data categories: [list]
  Likely obligation areas: [privacy / retention / consent / vendor / contracts / market-specific]

Observed gaps:
  [gap] — [why it matters] — [risk if unresolved]

Escalation triggers:
  [issue] — [who should review]

Recommended next step:
  [smallest safe compliance-hardening action]

Non-legal-advice note:
  [explicit reminder to escalate where needed]
```

## References

- `../../references/checklists/legal-compliance-checklist.md`
