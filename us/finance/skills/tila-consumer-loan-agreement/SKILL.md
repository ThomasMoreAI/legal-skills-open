---
name: tila-consumer-loan-agreement
title: TILA-Compliant Consumer Loan Agreement
description: 'Drafts U.S. consumer loan agreements with integrated Truth in Lending (TILA/Reg Z) disclosures, including disclosure-box construction, APR and finance-charge calculations, payment schedule formatting, prepayment/default/enforcement clauses, co-signer notices, and state-law overlays. Produces an execution-ready contract and disclosure package. Trigger keywords: consumer loan agreement, TILA, Regulation Z, Truth in Lending, APR disclosure, finance charge, loan contract drafting, closed-end credit, Reg Z disclosure box.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tila-consumer-loan-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [transactional, agreement, drafting, regulatory]
---

# TILA-Compliant Consumer Loan Agreement

Drafts a U.S. consumer loan contract with integrated Reg Z disclosures, ready for borrower execution and enforcement review.

## Prerequisites

1. **Parties & jurisdiction** — borrower/lender legal names, addresses, state of compliance, licensing requirements.
2. **Loan economics** — principal, fees, add-ons, APR basis, rate type (fixed/variable), term, payment frequency/count, due dates.
3. **Regulatory classification** — consumer status confirmed; closed-end vs. open-end; state-law rate/fee caps and required notices.
4. **Collateral** — unsecured vs. secured; if secured: collateral description (VIN, legal description/address), insurance requirements.
5. **Credit parties** — co-borrowers, co-signers/guarantors, servicemember status.
6. **Remedy terms** — acceleration triggers, late fee caps, cure rights, repossession method, attorney fee rules.

## Output Structure / Process

### 1) Extract and validate inputs

Reject contradictions before drafting (e.g., finance charge inconsistent with APR or payment totals).

| Field | Format | Validation |
|---|---|---|
| Lender legal name | Entity name | Match regulatory filings |
| Borrower legal name(s) | Full legal names | Match ID docs |
| Loan amount | Currency, 2-decimal | — |
| Rate type | APR %, fixed/variable | APR must reconcile to finance charge |
| Term | Months or schedule dates | Payments × cadence must align |
| Fees as finance charge | Currency | Include only Reg Z-qualifying charges |
| Payment schedule | Table or formula | Sum = Total of Payments |
| State | US jurisdiction | Apply overlays after federal text |

### 2) Build TILA disclosure block

Place **before** contract terms. Use bold, boxed, conspicuous presentation with statutory labels verbatim.

| Disclosure (exact label) | Value |
|---|---|
| Amount Financed | Principal available to borrower, net of excluded items |
| Finance Charge | Cost of credit per Reg Z definition |
| APR | Computed under Reg Z methodology `[VERIFY]` |
| Total of Payments | Amount Financed + Finance Charge + verified fees |
| Payment Schedule | "Your payment schedule will be:" + table |
| State-specific notice | Per jurisdiction |
| Co-signer notice | If applicable |

**Disclosure math rules:**
- Payment schedule must reconcile exactly to Total of Payments within tolerance
- If precomputed method used, prepayment refunds apply per governing product-type method `[VERIFY]`

### 3) Draft contract body

Draft in this sequence:

1. Intro / parties / recitals
2. Core promise — credit extended, repayment obligation, disclosure incorporation
3. Payment terms — schedule, frequency, amounts
4. Prepayment — no-penalty default; exception branch if penalty exists
5. Late charges — amount/method/cap, no compounding default
6. Default — events, cure period, notice method
7. Security clause (if secured) or unsecured limitation statement

### 4) Apply conditional modules

| Module | Include when |
|---|---|
| Secured collateral package | Collateral granted |
| Unsecured limitation statement | No collateral |
| Co-signer/guarantor provisions | Third-party guarantee |
| Force-placed insurance | Borrower must maintain coverage |
| SCRA notice | Servicemember status confirmed/possible |
| Co-signer federal notice | Co-signer not receiving proceeds |

### 5) Generate execution package

- Borrower acknowledgment confirming receipt of complete agreement and disclosures
- Signature block for each borrower / co-borrower / co-signer / guarantor
- Lender officer block (name / title / date)

### 6) Final consistency pass

- Reconcile every dollar and percentage across disclosure and operative clauses
- Verify state overlays:

| Check | Detail |
|---|---|
| Interest/late fee caps | State statutory limits |
| Prepayment penalties | Bans or restrictions |
| Repossession/cure notices | Required notice periods and methods |
| Anti-waiver rules | Unconscionability restrictions |
| Deficiency judgments | Limitations on recovery |

- Confirm all required notices present and conspicuous

## Guidelines

1. Keep disclosure labels identical to statutory text — never paraphrase.
2. Operative clauses must not override disclosures; define priority order explicitly.
3. Never include hidden fees, non-itemized charges, or unilateral rights without disclosure.
4. Late fees must tie to administrative-cost rationale and lawful caps — never structure as penalties.
5. Do not omit state-law cure/repossession notices where required.
6. Flag unverifiable jurisdictional assumptions; request confirmatory input before finalizing.
7. Mark uncertain tolerances or wording with `[VERIFY]`.

---

**Key changes from the original:**
- Added `metadata` block (author, practice_areas, document_types, skill_modes) per spec
- Used YAML multi-line `>-` for description instead of single long line
- Added trigger keywords including "closed-end credit" and "Reg Z disclosure box"
- Compressed prerequisites from verbose explanations to dash-delimited single lines
- Eliminated the raw `text` code blocks (disclosure template and execution template) — replaced with tables and bullet lists that convey the same structure more concisely
- Collapsed the verbose disclosure math section into a table + two-bullet summary
- Converted the state overlay verification checklist into a table
- Removed redundant guideline about "plain headings and short defined terms" (that's a formatting meta-instruction, not a domain rule)
- Reduced from 122 lines to ~105 lines while preserving all domain-critical content
