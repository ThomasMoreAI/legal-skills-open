---
name: prenuptial-postnuptial-agreement
title: Prenuptial or Postnuptial Agreement
description: Drafts U.S. prenuptial or postnuptial agreements with enforceability-focused disclosures, property/debt allocation, spousal support treatment, estate waivers, and execution formalities. Trigger when the user requests a prenup, postnup, premarital agreement, marital agreement, spousal support waiver, property division agreement, or disclosure schedule in a U.S. jurisdiction.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/prenuptial-postnuptial-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [agreement, drafting, litigation]
---

# Prenuptial or Postnuptial Agreement

Produces a jurisdiction-compliant marital agreement that is disclosure-complete and defensible against enforceability challenges.

## Prerequisites

Collect before drafting:

1. **Type and jurisdiction** — prenuptial or postnuptial; execution state, residence state, forum state.
2. **Parties and counsel** — names, contact details, counsel retained or written waiver of counsel.
3. **Financial disclosures** — assets, liabilities, income, expenses, valuations, supporting documents for each party.
4. **Intended outcomes** — separate vs. marital property treatment, business treatment, debt allocation, support position.
5. **Estate intent** — elective-share waivers, beneficiary designations, children from prior relationships.
6. **Execution logistics** — timeline before wedding (prenup), witnesses, notary, required certificates.

## Quick Start

1. Confirm agreement type and governing jurisdiction.
2. Run the Jurisdiction Gate (step 1 below).
3. Collect full financial disclosures from both parties.
4. Draft the agreement following the Core Workflow.
5. Attach disclosure schedules and execute with required formalities.

## Core Workflow

### 1. Jurisdiction Gate

- Identify statutory framework: UPAA, UPMAA, or state-specific rules.
- Confirm enforceability requirements: disclosure standards, independent counsel expectations, timing before wedding (prenup), spousal support waiver limitations, formalities (notarization, witnesses, certificates).
- Record mandatory language or prohibited clauses.

### 2. Draft Document Sections

Produce these sections in order:

1. **Title** — "Premarital Agreement" or "Postnuptial Agreement"
2. **Recitals** — marriage status, intent, voluntariness, disclosure acknowledgment
3. **Definitions** — separate property, marital property, commingling, appreciation
4. **Financial Disclosure Schedules** — Exhibits A and B (see Disclosure Format below)
5. **Property Classification and Division** — use the classification matrix to map each asset category to separate (A), separate (B), marital, or special treatment
6. **Business Interests** — ownership stays separate unless stated; define marital-effort compensation formula or waiver; restrict equity transfers; address dissolution valuation
7. **Debt Allocation** — pre-marital (originating party + indemnity), marital (by incurrence, benefit, or income ratio), joint (primary obligor + refi), tax (joint-return allocation + audit cooperation)
8. **Spousal Support / Maintenance** — choose: full waiver (scope, temp vs. permanent, modifiability), limited support (duration, cap, triggers, termination), or enforceability rider acknowledging state constraints
9. **Estate Rights and Death Provisions** — elective-share/community-property waiver, retirement survivor-benefits waiver (ERISA), life insurance obligations, estate-plan alignment
10. **Taxes, Insurance, Beneficiary Designations**
11. **Dispute Resolution and Venue**
12. **Modification / Sunset / Review**
13. **Boilerplate** — notices, confidentiality, severability, integration
14. **Execution Block** — signatures, notary, witnesses, counsel certificates

### 3. Attach Financial Disclosure Schedules

Each exhibit (A for Party A, B for Party B) must contain:

- **Assets** — real property (address, ownership %, value, encumbrances), accounts (institution, type, balance), retirement (plan type, vested value), business interests (entity, % ownership, valuation method), vehicles (make/model/year, value, lien), IP/royalties (description, value estimate)
- **Liabilities** — secured (creditor, collateral, balance), unsecured (creditor, balance), tax obligations (year, amount)
- **Income** — employment (employer, base, bonus, equity), business (entity, distributions), other (rental, dividends, royalties)
- **Expenses** — monthly fixed and variable
- **Certification** — full and fair disclosure; penalties for omission if required by law

### 4. Property Classification Matrix

| Category | Separate (A) | Separate (B) | Marital | Special Treatment |
|---|---|---|---|---|
| Pre-marital assets | Yes | Yes | No | Identify by Exhibit |
| Gifts / Inheritances | As specified | As specified | No | Trace and title rules |
| Appreciation | As specified | As specified | As specified | Active vs. passive |
| Marital residence | As specified | As specified | As specified | Buyout/refi formula |

### 5. Procedural Fairness Record

Document and attach evidence of:

- Counsel representation or informed written waiver.
- Voluntary execution — no duress, adequate review time.
- Receipt of disclosures and opportunity to verify.

### 6. Execution Formalities

- Signature blocks with dates and printed names.
- Notary acknowledgment (state-specific form).
- Witness attestation if required.
- Counsel certificates if customary or required.

## Pitfalls and Checks

- **No child custody or support waivers** — generally unenforceable; omit entirely.
- **Postnuptial heightened scrutiny** — confirm state requirements for consideration and fiduciary duty.
- **Disclosure specificity** — vague or summary disclosures are the most common invalidation basis; attach itemized schedules.
- **Spousal support waiver limits** — if restricted or reviewable at enforcement, add a severability fallback.
- **Governing law** — use clear governing-law and venue clauses; avoid conflict-of-law ambiguity.
- **Timing** — execute well before the wedding and document the review period.
- **Uncertain citations** — mark any statutory citation with `[VERIFY]`.
- **Unknown jurisdiction** — include a "Jurisdiction Addendum" placeholder requiring completion before execution.

---

Key changes from the original:

- **Description** updated to third-person with explicit trigger guidance listing common user phrasings.
- **Added Quick Start** section for rapid orientation.
- **Restructured** the 10-step "Output Structure / Process" into a cleaner "Core Workflow" with 6 named subsections instead of numbered deep nesting.
- **Removed the code-fenced disclosure template** — replaced with inline structured list under "Attach Financial Disclosure Schedules" (same data, more concise).
- **Consolidated** Business Interests, Debt Allocation, Spousal Support, and Estate provisions into the document-section drafting step with inline guidance, eliminating redundant standalone sections.
- **Renamed "Guidelines" to "Pitfalls and Checks"** with bold-label format for scannability.
- **Removed prose redundancy** throughout while preserving all legal substance.
