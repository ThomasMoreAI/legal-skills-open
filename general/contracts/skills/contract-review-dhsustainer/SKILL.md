---
name: contract-review-dhsustainer
title: Contract Review
description: Analyze contracts to identify risks, unfavorable clauses, missing protections, and ambiguous language — from the perspective of a specified party.
author: DHsustainer
author_url: https://github.com/DHsustainer/gnostor/tree/main/skills/legal/contract-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Review

Read contracts critically and flag what matters — the risks you're taking, the protections you're missing, and the clauses worth negotiating.

> **Disclaimer:** This skill is a drafting and analysis aid. For contracts with material legal or financial consequences, engage a licensed attorney.

## When to Use

- "Review this contract from my perspective as [role]"
- "What are the risks in this agreement?"
- "What clauses should I push back on?"
- "Is anything missing from this contract?"
- "Explain what this clause actually means"

## What to Give Me

- The contract text (paste it in full)
- **Your role**: buyer / seller / service provider / client / employer / employee / licensor / licensee
- **Your concern**: red flags only, full review, negotiation points, or plain-language explanation

## What I Analyze

### High-Risk Clauses
- **Unlimited liability** — is your exposure capped?
- **Indemnification** — are you indemnifying the other party for their own negligence?
- **IP ownership** — do you retain rights to your work product?
- **Exclusivity** — does this lock you out of other clients/vendors?
- **Auto-renewal with short notice window** — can you get trapped?
- **Unilateral change rights** — can they change terms without your consent?
- **Termination for convenience** — who can exit and on what terms?
- **Non-compete / non-solicitation scope** — is it reasonable in time, geography, activity?

### Missing Protections
- Limitation of liability (yours)
- Payment terms and late payment penalties
- Dispute resolution process (arbitration vs. litigation, jurisdiction)
- Change order / scope creep provisions
- Confidentiality obligations on both sides
- Warranties and representations you should get
- Exit rights and what happens on termination

### Ambiguous Language
- Clauses that could be read two ways
- Undefined terms used in operative clauses
- "Reasonable efforts" vs. "best efforts" vs. "commercially reasonable efforts"
- Timelines without a starting reference point

## Output Format

```markdown
## Contract Review: [Document Name]
**Reviewing as:** [Your role]
**Risk Level:** 🔴 High / 🟡 Medium / 🟢 Low

---

## 🔴 Critical Issues
Issues that create serious risk or should block signing as-is.

### Issue: [Clause name / section]
**What it says:** [plain language]
**Why it's a problem:** [risk explained]
**Recommended action:** [redline or ask]

---

## 🟡 Issues to Negotiate
Clauses that are unfavorable but not dealbreakers.

---

## 🟢 Missing Protections
Standard clauses absent from this contract.

---

## ℹ️ Neutral Observations
Context or clarifications without a risk component.

---

## Suggested Redlines
Key clauses rewritten in your favor.
```
