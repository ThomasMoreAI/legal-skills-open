---
name: consumer-loan-tila
title: Consumer Loan Agreement (TILA Compliant)
description: Drafts TILA-compliant consumer loan agreements with Regulation Z disclosure boxes, APR/finance charge calculations, and enforceable terms for secured and unsecured consumer credit. Use when drafting consumer loan agreements, TILA disclosure documents, promissory notes for consumer credit, or Reg Z compliant financing contracts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/consumer-loan-tila
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, regulatory, transactional]
---

# Consumer Loan Agreement (TILA Compliant)

Generates a consumer loan agreement satisfying Truth in Lending Act (15 U.S.C. § 1601 et seq.) and Regulation Z (12 CFR Part 1026) disclosure requirements.

## Prerequisites

Gather before drafting:

1. **Borrower** — full legal names, addresses, co-borrowers/guarantors
2. **Lender** — legal entity name, DBA, address, regulatory filings
3. **Loan terms** — principal, interest rate, term, payment frequency
4. **Fees** — origination, points, doc prep, service charges
5. **Collateral** (if secured) — make/model/VIN for personal property; legal description for real property
6. **State/institutional requirements** — notice clauses, jurisdictional restrictions
7. **Ancillary products** — credit insurance or debt protection elections

## Document Architecture

| Section | Purpose |
|---|---|
| TILA Disclosure Box | Mandatory Reg Z disclosures — **must appear first on page 1** |
| Loan Terms & Conditions | Substantive contractual provisions |
| Default, Acceleration & Remedies | Events of default, cure rights, lender remedies |
| Insurance & Payment Application | Collateral insurance, force-placed coverage, payment waterfall |
| Special Notices | SCRA, FTC co-signer, state-specific notices |
| Execution & Signatures | Acknowledgments, signature blocks, copy delivery |

## Core Workflow

### Step 1 — TILA Disclosure Box

Heading: **"FEDERAL TRUTH IN LENDING DISCLOSURES"** — bold, ≥2pt larger than body, visually segregated, page 1 before all other terms.

Use these **exact Reg Z labels**:

| Label (verbatim) | Content |
|---|---|
| "Annual Percentage Rate (The cost of your credit as a yearly rate)" | Actuarial/US Rule method; ≥2 decimals; accurate within ⅛ of 1% `[VERIFY tolerance for transaction type]` |
| "Amount Financed (The amount of credit provided to you or on your behalf)" | Net credit minus prepaid finance charges; include financed ancillary products |
| "Finance Charge (The dollar amount the credit will cost you)" | Total dollar cost: interest + fees + points + charges; itemize major components |
| "Total of Payments (The amount you will have paid after you have made all payments as scheduled)" | Amount Financed + Finance Charge |
| "Payment Schedule (Your payment schedule will be)" | Uniform: number × amount × frequency + first date. Irregular/balloon: full table |

**Cross-verify**: Amount Financed + Finance Charge = Total of Payments. Payment schedule must sum to Total of Payments.

### Step 2 — Substantive Loan Terms

- [ ] **Parties and promise** — full legal names, fundamental obligation
- [ ] **Loan purpose** — "personal, family, or household purposes" or state-required specific purpose
- [ ] **Prepayment rights** — penalty-free or penalty terms (conditions, duration, calculation, maximum, state compliance)
- [ ] **Late charges** — amount/percentage, grace period (10–15 days typical), single-assessment rule, no compounding, state caps
- [ ] **Collateral** (secured) — personal property: make/model/year/serial/VIN/location; real property: legal description + street address; borrower covenants: maintain condition, no liens, maintain insurance, no unauthorized transfer
- [ ] **Unsecured statement** (unsecured) — affirmative disclosure that no collateral secures the obligation

### Step 3 — Default & Remedies

Events of default: (1) missed payment, (2) failure to maintain required insurance, (3) bankruptcy/insolvency, (4) material misrepresentation, (5) borrower death if loan does not survive, (6) collateral impairment.

Include:
- State-required notice of default and right to cure (period + delivery method)
- Acceleration clause with applicable notice requirements
- Collateral remedies: repossession (judicial/self-help per state law), commercially reasonable sale, proceeds waterfall (costs → interest → principal → surplus to borrower), deficiency rights
- Attorney's fees and collection costs where state law permits

### Step 4 — Payment Application Waterfall

> "We will apply each payment first to unpaid late charges, then to accrued but unpaid interest, then to principal, and finally to any other charges or fees owed under this Agreement."

### Step 5 — Regulatory Notices

| Trigger | Notice |
|---|---|
| All transactions | Borrower acknowledgment of receipt of agreement and TILA disclosures |
| Servicemember borrower | SCRA notice — potential 6% rate cap on pre-service obligations |
| Co-signer/guarantor not receiving proceeds | FTC co-signer notice (verbatim): *"You are being asked to guarantee this debt. Think carefully before you do. If the borrower does not pay the debt, you will have to. Be sure you can afford to pay if you have to, and that you want to accept this responsibility. You may have to pay up to the full amount of the debt if the borrower does not pay. You may also have to pay late fees or collection costs, which increase this amount."* |
| State-specific | Right-to-cure, pre-repossession, redemption rights — use verbatim statutory language |

### Step 6 — Execution

- Acknowledgment above signatures: receipt of completed copy, opportunity to seek counsel, agreement to be bound
- Separate signature blocks (printed name, signature, date) for each borrower, co-borrower, guarantor (with FTC notice), and authorized lender officer (name + title)
- Lender delivers executed copy at signing

## Pitfalls & Checks

- **APR calculation**: Use actuarial method per Reg Z Appendix J; verify tolerance for transaction type
- **State law overlay**: Check usury limits, prepayment penalty restrictions, deficiency judgment limitations, force-placed insurance rules, additional disclosure requirements
- **Force-placed insurance**: Disclose that lender-placed coverage may cost more than borrower-obtained coverage
- **Formatting**: ≥10pt body; ≥12pt bold TILA heading; numbered provisions; consecutive pages; header/footer with document title, borrower name, date
- **Do not** include jury-trial waiver, class-action waiver, or mandatory arbitration without explicit instruction and state-law permissibility analysis
- **Tag `[VERIFY]`** on any statutory citation or regulatory reference you cannot independently confirm
