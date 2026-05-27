---
name: reaffirmation-agreement
title: Reaffirmation Agreement
description: Drafts Reaffirmation Agreements under 11 U.S.C. § 524(c) for U.S. bankruptcy proceedings. Produces Official Form 240A-compliant documents with agreement summary, original/modified loan terms, debtor and attorney certifications, and court approval sections. Use when a debtor reaffirms a dischargeable debt to retain secured collateral such as vehicles or homes.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/reaffirmation-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
---

# Reaffirmation Agreement

Drafts a court-ready reaffirmation agreement allowing a debtor to retain secured collateral by voluntarily reaffirming a dischargeable debt under 11 U.S.C. § 524(c). Must comply with Bankruptcy Rule 4008 and Official Form 240A.

## Prerequisites

Collect before drafting:

1. **Parties** — debtor/creditor legal names, addresses, case number, chapter filed
2. **Original loan** — date, principal, interest rate, payment amount/frequency, maturity
3. **Current status** — outstanding balance (principal + accrued interest + fees), payment history, default status
4. **Collateral** — description, current fair market value, lien position
5. **Modified terms** (if any) — reduced rate, extended term, principal reduction
6. **Schedule I and J** — debtor's current income and expenses for undue hardship analysis
7. **Representation status** — whether debtor has counsel (determines court approval requirement)

## Document Structure

### Part A: Agreement Summary

Present as a table:

| Field | Value |
|---|---|
| Debtor Name | {name} |
| Case Number | {case no.} |
| Creditor Name | {name} |
| Total Debt Reaffirmed | ${amount} |
| — Principal | ${amount} |
| — Accrued Interest | ${amount} |
| — Fees/Costs | ${amount} |
| Collateral Description | {description} |
| Collateral Fair Market Value | ${amount} |
| Annual Percentage Rate | {rate}% |
| Monthly Payment | ${amount} |
| Payment Duration | {months/years} |
| Total of Payments | ${amount} |

### Part B: The Agreement

1. **Party identification** — full legal names, addresses
2. **Original loan terms** — date, principal, rate, payment, frequency, maturity
3. **Reaffirmed terms** — state whether original or modified terms apply
4. **If modified**, include side-by-side comparison:

| Term | Original | Reaffirmed |
|---|---|---|
| Interest Rate | {orig}% | {new}% |
| Monthly Payment | ${orig} | ${new} |
| Remaining Term | {orig} | {new} |
| Total Remaining | ${orig} | ${new} |

### Part C: Debtor Certification

Debtor certifies under penalty of perjury:

- Agreement is voluntary and not required
- Debtor can make required payments
- Agreement does not impose undue hardship on debtor or dependents
- Debtor understands right to rescind within 60 days after filing or before discharge, whichever is later (§ 524(c)(4))
- Debtor understands default allows repossession AND deficiency pursuit

### Part D: Attorney Certification

Required when debtor is represented. Attorney certifies:

- Agreement fully explained to debtor
- Debtor entered agreement voluntarily with informed consent
- Debtor advised of legal effect, consequences, and default consequences
- Attorney believes debtor can afford payments
- Agreement does not impose undue hardship

### Part E: Court Approval

Required when:
- Debtor is **not represented by counsel**, OR
- Schedule I/J shows income minus expenses **insufficient** to cover reaffirmed payments

Include notice of scheduled hearing; court must find (1) no undue hardship and (2) agreement is in debtor's best interest.

### Signature Block

Include signature lines for:
- **Debtor** — signature, printed name, date
- **Creditor** — signature, printed name, title, date
- **Debtor's attorney** (if applicable) — signature, printed name, bar number, date
- **Notarization block** — include if required by local rules

## Pitfalls and Checks

- **Rescission rights are mandatory** — omission renders the agreement unenforceable under § 524(c)(4)
- **No coercion language** — agreement must affirmatively state the debtor is not required to reaffirm
- **Default consequences** — prominently warn: creditor may repossess collateral AND pursue deficiency balance
- **Collateral-to-debt ratio** — if debt substantially exceeds collateral value, flag for additional disclosure; vulnerable to judicial scrutiny under undue hardship standard
- **U.S. Trustee review** — draft anticipating objection; economic justification must be apparent on the face of the document
- **Local rules** — verify whether the bankruptcy court requires notarization or additional local forms
- **Plain language** — maintain legal precision while ensuring the debtor can actually understand the obligation

---
