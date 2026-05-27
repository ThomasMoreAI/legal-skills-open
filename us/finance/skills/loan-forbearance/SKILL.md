---
name: loan-forbearance
title: Loan Forbearance Agreement
description: Drafts lender-protective U.S. commercial loan forbearance agreements that temporarily suspend remedies while preserving all lender rights, capturing existing defaults, payment deferrals, conditions precedent, and borrower releases. Use when drafting or reviewing a forbearance agreement, loan workout, payment deferral, temporary modification, default standstill, lender-borrower restructuring, or cure-period extension.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/loan-forbearance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Loan Forbearance Agreement

Produce a lender-protective, temporary forbearance agreement for a commercial loan default.

## Prerequisites

1. **Loan documents** — note, loan agreement, security agreement, mortgages, guaranties, prior amendments
2. **Parties** — legal names, entity types, state of formation, addresses, signing authority, guarantors
3. **Default facts** — specific defaults, dates, amounts, covenant breaches, notices given
4. **Payoff data** — principal, accrued interest, fees, default interest, protective advances
5. **Collateral** — description, perfection status, valuations, insurance
6. **Forbearance terms** — start/end dates, payment schedule, deferred amount treatment, fees
7. **Reporting** — required financials, frequency, format, deadlines
8. **Governing law/venue** — per existing loan documents unless business reason to change
9. **Approvals** — lender credit approval, borrower board/consents if required

## Output Structure / Process

### 1. Title and Parties

| Role | Legal Name | Entity Type/State | Address | Defined Term |
| --- | --- | --- | --- | --- |
| Lender |  |  |  | "Lender" |
| Borrower |  |  |  | "Borrower" |
| Guarantor(s) |  |  |  | "Guarantor" |

### 2. Recitals (Contractual)

- Original loan documents with dates and principal
- Current outstanding balance and maturity
- Collateral summary
- Specific defaults (list each)
- Borrower request; lender discretionary accommodation
- Acknowledgment of debt, lien validity, and no defenses
- State that recitals are contractual and incorporated

### 3. Defined Terms

Define at minimum: "Forbearance Period," "Forbearance Payments," "Existing Defaults," "Deferred Amounts," "Forbearance Termination Date," "Loan Documents."

### 4. Forbearance Terms

| Item | Term |
| --- | --- |
| Effective Date |  |
| Forbearance Period Start/End |  |
| Forbearance Fee |  |
| Payment Amounts/Dates |  |
| Interest Rate During Period |  |
| Default Rate Applies? |  |
| Late Fees During Period |  |
| Deferred Amount Treatment |  |
| Maturity Extension |  |
| Application of Payments |  |

Required clauses:
- Scope: only specific listed remedies are suspended
- No waiver of rights; all rights reserved
- Forbearance applies only to Existing Defaults

### 5. Conditions Precedent

- [ ] Execution and delivery by all parties
- [ ] Payment of forbearance fee and costs
- [ ] Current financial statements delivered
- [ ] Evidence of insurance; lender as loss payee/additional insured
- [ ] UCC/real property perfection status confirmed
- [ ] All required consents/authorizations delivered

### 6. Ongoing Covenants

- [ ] Timely forbearance payments, no grace period
- [ ] Taxes and insurance current
- [ ] No additional debt or liens without consent
- [ ] No asset sales outside ordinary course
- [ ] Maintain legal existence and good standing
- [ ] Periodic financial reporting (define cadence and deadline)
- [ ] Collateral preservation and inspection access

### 7. Representations and Acknowledgments

**Borrower:** authority and enforceability; no defenses, offsets, or counterclaims; accuracy of financials; no undisclosed MAC; debt and liens are valid and enforceable.

**Lender:** authority to enter; holder of note (if applicable).

### 8. Events of Default and Termination

| Trigger | Notice/Cure? |
| --- | --- |
| Missed forbearance payment |  |
| Breach of covenant |  |
| New default under loan docs |  |
| Misrepresentation |  |
| Insolvency/bankruptcy/receivership |  |
| Attachment/levy |  |
| Unauthorized transfer |  |

Consequences: forbearance terminates immediately; all amounts due; lender may exercise all remedies under loan documents and law.

### 9. Releases, Waivers, Reaffirmations

- Borrower release of claims through Effective Date
- Waiver of defenses and counterclaims
- Reaffirmation of all loan documents and liens
- No novation

### 10. Miscellaneous

- Governing law; venue; jurisdiction
- Attorneys' fees to prevailing party (if consistent with loan docs)
- Integration; amendments in writing only
- Notices (method and addresses)
- Counterparts; electronic signatures
- Assignment limits (borrower restricted)

### 11. Exhibits

- Exhibit A: Payment Schedule
- Exhibit B: Payoff Statement
- Exhibit C: Collateral Schedule
- Exhibit D: Guarantor Acknowledgment

### 12. Signature Blocks

Provide blocks for Lender, Borrower, Guarantor(s), and Notary (if required by governing law or real property rules).

## Guidelines

- Align governing law, venue, and arbitration with existing loan documents unless there is a specific reason to change
- Do not convert forbearance into a permanent modification unless expressly approved
- Ensure release and waiver language is enforceable under the governing state — `[VERIFY]` if unsure
- If collateral includes real property, confirm notarization and recording requirements
- If borrower is in bankruptcy or imminently filing, flag that court approval and automatic stay analysis may be required
- If any consumer lending elements exist, add applicable consumer compliance terms and disclosures
- Keep scope limited to Existing Defaults; reserve all remedies for new defaults
- Avoid representations about future lender accommodations
- Verify default interest, late fees, and usury limits for the governing state with `[VERIFY]`
