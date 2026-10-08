---
name: prompt-pack-delegation-of-authority-matrix-sboghossian
title: Delegation of Authority Matrix
description: Use when a company needs to draft or update a Delegation of Authority (DoA) Matrix specifying approval levels for key decisions — contracts, capital expenditure, hiring, litigation, banking, and other material matters — with escalation paths and documentation requirements. A critical internal governance control tool. MENA-aware for UAE, KSA, LB, EG corporate governance requirements, family business governance, and DIFC/ADGM regulated entity board approval standards.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-delegation-of-authority-matrix
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Delegation of Authority Matrix

A Delegation of Authority (DoA) Matrix is the internal governance instrument that prevents two of the most common corporate failures: unauthorised commitments (someone signing something they had no power to sign) and decision paralysis (every minor decision requires CEO approval). Done well, it scales governance with the company.

## When to use this

- A company is growing and informal approvals are no longer adequate as financial commitments increase.
- An audit, investor, or regulatory review has identified the absence of a formal DoA as a control gap.
- A company has experienced an unauthorized contract commitment or expenditure and needs to formalise controls.
- A publicly listed company or regulated entity is required to maintain documented approval authorities.
- A family business is transitioning from founder-controlled decision-making to a more structured governance model.
- A company operating across multiple MENA jurisdictions needs a uniform authorization framework.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction(s) | Determines the legal backdrop (company law, powers of directors, PoA requirements) | Ask the user |
| Organisational levels | The DoA maps authority to roles; must know the hierarchy | Ask the user to describe: Board / CEO / C-suite / VP / Manager / etc. |
| Categories of decisions to be covered | The matrix must cover all material decision types | Ask the user; default list below covers the standard categories |
| Financial thresholds | The monetary limits that trigger escalation | Ask the user — thresholds should reflect actual deal sizes |
| Whether the company has foreign entities or subsidiaries | Sub-entities may need their own authority levels | Ask the user |

## Optional inputs

- Whether powers of attorney are used for third-party transactions (common in MENA).
- Whether the DoA is being adopted by the board as a formal resolution.
- Whether the DoA will be shared with external parties (banks, counterparties) or is purely internal.
- Whether the company has a Sharia board or audit committee whose approval is separate from the DoA levels.

## Matrix structure

The DoA Matrix is typically presented as a table or spreadsheet with:
- Rows: decision categories and subcategories.
- Columns: role levels (Board, CEO, CFO/COO, VP/Head of Function, Manager, Department Lead).
- Cells: "A" (Approve), "R" (Recommend), "N" (Notify), or "—" (Not involved).

### Standard decision categories

**Category 1 — Contracts and commitments**

| Decision | Threshold | Board | CEO | CFO/COO | VP/HOF | Manager |
|---|---|---|---|---|---|---|
| New contract — purchase of goods/services | > USD 1M | A | — | R | — | — |
| New contract — purchase of goods/services | USD 250K–1M | — | A | R | — | — |
| New contract — purchase of goods/services | USD 50K–250K | — | — | A | R | — |
| New contract — purchase of goods/services | < USD 50K | — | — | — | A | R |
| Revenue contracts / sales agreements | All values | — | A | R | R | — |
| Contract renewal | As above by value | Follow new contract thresholds | — | — | — | — |
| Contract amendment (material) | As above by value | Follow new contract thresholds | — | — | — | — |
| Power of attorney (third-party PoA) | All | A | R | — | — | — |

**Category 2 — Capital expenditure (CapEx)**

| Decision | Threshold | Board | CEO | CFO | VP/HOF | Manager |
|---|---|---|---|---|---|---|
| Unbudgeted CapEx | > USD 500K | A | R | — | — | — |
| Unbudgeted CapEx | USD 100K–500K | — | A | R | — | — |
| Unbudgeted CapEx | < USD 100K | — | — | A | R | — |
| Budgeted CapEx (approved in annual budget) | Within budget line | — | — | A | — | — |

**Category 3 — Human resources**

| Decision | Threshold | Board | CEO | CHRO/HR | Line Manager |
|---|---|---|---|---|---|
| Hire C-suite executives | All | A | R | — | — |
| Hire VP / Head of Function | All | — | A | R | — |
| Hire Senior Manager | All | — | — | A | R |
| Hire all other staff | All | — | — | — | A |
| Redundancy / termination — C-suite | All | A | R | — | — |
| Redundancy / termination — VP / HOF | All | — | A | R | — |
| Salary increase > 15% | All | — | A | R | — |
| Bonus / incentive payment | As per remuneration policy | Board/Remco | — | — | — |

**Category 4 — Financial and banking**

| Decision | Threshold | Board | CEO | CFO | Finance Director |
|---|---|---|---|---|---|
| Open / close bank accounts | All | A | R | R | — |
| Authorised bank signatories | All | A | — | R | — |
| Payment approval | > USD 500K | — | A | R | — |
| Payment approval | USD 50K–500K | — | — | A | R |
| Payment approval | < USD 50K | — | — | — | A |
| Loan / debt facility | All | A | R | R | — |
| Treasury investment | > USD 1M | A | R | R | — |

**Category 5 — Legal and regulatory**

| Decision | Threshold | Board | CEO | GC/Legal | Dept Head |
|---|---|---|---|---|---|
| Initiate litigation | All | A | R | R | — |
| Settle litigation | > USD 500K | A | R | R | — |
| Settle litigation | USD 100K–500K | — | A | R | — |
| Settle litigation | < USD 100K | — | — | A | R |
| Engage external legal counsel | > USD 100K/year | — | A | R | — |
| Regulatory filing / notification | All material | — | A | R | — |
| IP registration (new) | All | — | — | A | R |
| Regulatory fine / enforcement response | All | A | R | R | — |

**Category 6 — Strategic decisions**

| Decision | Board | CEO |
|---|---|---|
| Annual budget and business plan | A | R |
| Entry into new market / jurisdiction | A | R |
| Major corporate restructuring | A | R |
| Acquisition or disposal of significant assets | A | R |
| Related party transactions (above materiality threshold) | A | R (with independent director approval) |
| Material change to business model | A | R |

### Joint approval / dual signature requirements
For high-value transactions, require joint approval (e.g., CEO + CFO both sign for payments above USD 1M). State this explicitly in the matrix.

### Escalation protocol
- Any decision not covered by the matrix escalates to the next level above.
- Any decision where a conflict of interest exists must be escalated to the next level and the interested party recused.
- In MENA family businesses, related party transactions must be escalated to the board (or a committee with independent members) regardless of value.

## Powers of attorney — MENA context

In MENA jurisdictions, many third-party actions (government filings, real estate transactions, banking, court representation) require a formal Power of Attorney (PoA) that is notarised and sometimes apostilled:
- **UAE:** PoAs must be notarized by a UAE Notary Public; general PoAs should be limited to a specific scope and validity period.
- **KSA:** PoAs must be notarized before a Saudi Notary Public; English-language PoAs must be translated to Arabic.
- **Lebanon:** Notarized PoAs (authenticated by the Bar Association for legal matters or by a Lebanese Notary).
- **Egypt:** Notarized and potentially apostilled PoAs for cross-border use.

The DoA Matrix should specify: (a) who may grant PoAs; (b) the maximum scope and duration; and (c) the register in which PoAs are recorded.

## Documentation requirements

For each approved decision, the following documentation should be maintained:
- Written approval (email confirmation sufficient for lower tiers; board minute for board-level decisions).
- Signed approval form for contract commitments above the middle thresholds.
- Board resolution for all board-level approvals.
- The DoA itself should be adopted by a board resolution; amendments require a further board resolution.

## Review and update

The DoA Matrix must be reviewed:
- Annually (align with annual budget approval cycle).
- Upon any significant change in the company's structure, size, or regulatory environment.
- Upon any significant event (acquisition, IPO, regulatory action) that changes the risk profile.

## Common mistakes

- Financial thresholds set so high that essentially all operational decisions require board approval — this is governance by paralysis.
- No distinction between purchase contracts (outgoing commitment) and revenue contracts (incoming cash) — different risk profiles warrant different approval levels.
- Related party transactions not subject to a specific, stringent approval requirement — this is the most common governance failure in MENA family businesses and public company scandals.
- No joint-approval requirement for high-value payments — creates single-point-of-failure fraud risk.
- The DoA is adopted once and never updated — an outdated DoA with thresholds from five years ago that no longer reflect business scale is misleading and creates liability.

## Related skills

- [[prompt-pack-corporate-governance-policy]]
- [[prompt-pack-code-of-conduct]]
- [[prompt-pack-director-indemnification-agreement]]
- [[prompt-pack-contract-playbook]]
- [[prompt-pack-client-intake-form]]
