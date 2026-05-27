---
name: letter-of-intent-loi
title: Letter of Intent (LOI)
description: 'Drafts U.S. corporate transaction Letters of Intent (LOI) for mergers, acquisitions, investments, and strategic alliances. Separates non-binding intent from enforceable obligations and defines deal structure, key economics, and closing path. Use when converting deal terms into a preliminary transaction document. Trigger keywords: "LOI", "letter of intent", "M&A LOI", "merger term sheet", "no-shop", "exclusivity", "deal letter".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/letter-of-intent-loi
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Letter of Intent (LOI)

Drafts a transaction LOI that advances execution while preserving negotiating flexibility. Default posture: non-binding except explicitly designated provisions.

## Prerequisites

1. Party identities, entity forms, and governing jurisdictions.
2. Transaction type and structure (asset sale, stock sale, merger, investment, JV, option).
3. Agreed economics: price, payment schedule, earn-outs, escrows, caps.
4. Timeline: signing target, exclusivity window, diligence period, closing date.
5. Conditions precedent and responsibility allocation (regulatory, financing, consents).
6. Binding vs non-binding designation for each term set.
7. Known constraints: antitrust, sector regulations, board/lender approvals.

## Output Structure / Process

Produce an audit-ready LOI in business-letter format using this sequence.

### 1) Intake Validation

- [ ] Party names and addresses complete.
- [ ] Transaction purpose stated in one unambiguous sentence.
- [ ] Economic terms fully defined and internally consistent.
- [ ] Timeline mapped to conditions precedent.
- [ ] Definitive documents identified (SPA, merger agreement, ancillaries).
- [ ] Binding clause set explicitly chosen by user.
- [ ] Governing law and jurisdictional basis confirmed.

### 2) Clause Matrix

| Section | Required? | Binding? |
|---|---|---|
| Date / Parties / Purpose | Yes | Non-binding |
| Transaction Overview | Yes | Non-binding |
| Principal Terms (price, structure, adjustments) | Yes | Non-binding unless stated |
| Conditions Precedent | Yes | Non-binding |
| Definitive Agreement Process | Yes | Mixed |
| Exclusivity / No-Shop | Optional | Usually binding |
| Confidentiality | Optional/Yes | Usually binding |
| Expenses / Costs | Optional | Usually binding |
| Liability Limitation / No-Action | Optional | Usually binding |
| Governing Law / Disputes | Yes | Binding |
| Signatures / Counterparts | Yes | Binding |

### 3) Drafting Rules

- Always include a plain-language binding-effect section with an enumerated list of binding carve-outs.
- Include no-liability clause for failure to close and good-faith negotiation language for definitive agreements.
- Keep conditions precedent objective, verifiable, and assigned to a responsible party.
- Do not embed tax opinions; use a placeholder for tax allocations.
- Definitive agreement controls if conflict with LOI.

### 4) Template Skeleton

```text
[Date]
[Party A Name]
[Party B Name]

RE: Letter of Intent – Proposed [Transaction Type]

[Opening: parties + transaction purpose]

1. Transaction Overview
2. Transaction Structure
3. Principal Terms
4. Conditions Precedent
5. Binding Commitments (Confidentiality / Exclusivity / Costs / Governing Law)
6. Definitive Agreements and Timeline
7. Termination and Liability
8. Miscellaneous (integration, notices, counsel, no assignment)
9. Signature Blocks
```

### 5) Quality Gate

- [ ] Defined terms consistent throughout (Transaction, Closing Date, Effective Date, CPs).
- [ ] All amounts specify currency, basis, and payment schedule.
- [ ] Non-compete references included only if jurisdictionally supportable and requested.
- [ ] Public-company-sensitive language flagged with compliance review placeholder.

## Guidelines

- Use clean drafting style; avoid overcommitment language in non-binding portions.
- Do not omit remedies for breach of expressly binding clauses.
- If existing NDA is signed, state LOI is supplemental and preserve NDA hierarchy.
- For regulated sectors, add counsel review notes on approvals and filing requirements.
- For cross-border transactions, flag foreign-law and conflict-of-laws risk.
- If anti-circumvention concern exists, add carve-outs and enforcement language for exclusivity.
