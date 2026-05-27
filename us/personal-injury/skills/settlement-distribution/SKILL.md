---
name: settlement-distribution
title: Settlement Distribution Statement
description: Drafts settlement distribution statements for personal injury cases with itemized accounting of gross proceeds, attorney fees, litigation costs, lien satisfactions, and net client payout. Enforces trust accounting compliance and reconciliation checks per Rules of Professional Conduct. Use when closing a PI matter, preparing disbursement sheets, or generating final case accounting.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-distribution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Settlement Distribution Statement

Produces the final financial accounting of PI settlement proceeds — gross recovery through all deductions to net client payout — for client delivery, trust accounting compliance, and regulatory review.

## Prerequisites

Gather before drafting:

- Executed settlement agreement (gross amount, allocation terms)
- Fee agreement (contingency %, sliding scales, caps, cost-advancement terms)
- Litigation cost ledger (date, vendor, description, amount per item)
- Lien resolution summary (original claim, negotiated amount, payment instructions per lienholder)
- Trust account confirmation (funds cleared and available)
- Client payment instructions (delivery method, split directions)

## Distribution Table Template

```
SETTLEMENT DISTRIBUTION STATEMENT
Matter: [Client Name] v. [Defendant(s)]
Matter No.: [#]
Date of Settlement: [Date]
Date of Statement: [Date]

ITEM                                          AMOUNT
─────────────────────────────────────────────────────
Gross Settlement Proceeds                 $__________

DEDUCTIONS:
  Attorney's Fees ([__]% per Fee Agreement
    dated [Date], ¶[__])                 ($__________)
  Litigation Costs (see Exhibit A)       ($__________)

  Lien Satisfactions:
    [Provider 1] — [type]               ($__________)
    [Provider 2] — [type]               ($__________)
  Subtotal Liens                         ($__________)

  Other Deductions:
    [Co-counsel referral / case funding] ($__________)

TOTAL DEDUCTIONS                         ($__________)
                                          ───────────
NET TO CLIENT                             $__________
═════════════════════════════════════════════════════
```

### Exhibit A — Litigation Costs

| Date | Vendor/Payee | Description | Amount |
|------|-------------|-------------|--------|
| | | | |
| | | **Total Costs** | **$____** |

## Output Format

Formal letter on firm letterhead addressed to client (full legal name, current address).

| Section | Content |
|---|---|
| **Opening** | Acknowledge resolution, transition to financial accounting (2-3 sentences) |
| **Distribution Table** | Completed template above |
| **Payment Details** | Check number/wire confirmation, delivery method, expected date |
| **Attachments** | Cost breakdown, lien satisfaction letters, fee agreement excerpts |

## Workflow

```
- [ ] Extract gross amount, fee terms, all costs, and all liens from source documents
- [ ] Calculate attorney fees per fee agreement (verify %, base, caps, sliding scales)
- [ ] Sum all deductions; compute net to client
- [ ] Reconcile: Gross = Total Deductions + Net to Client (must balance to the penny)
- [ ] Draft statement using template
- [ ] Attach cost breakdown, lien satisfaction letters, fee agreement excerpts
- [ ] Include payment delivery details (check #, wire confirmation, dates)
- [ ] Verify no bracketed placeholders remain in final output
```

## Critical Checks

- **Reconciliation is mandatory** — flag any discrepancy before finalizing; every dollar must be accounted for
- **Lien completeness** — cross-check every lien from resolution summary appears in statement; a missing lien exposes client to future liability
- **Fee agreement fidelity** — apply the exact contracted percentage/rate; honor all caps, sliding scales, and special provisions
- **Plain language** — avoid jargon the client won't understand; add brief context for each line item
- **Ethical compliance** — satisfy Rules of Professional Conduct re: client property (Model Rule 1.15), trust accounting, and fee transparency
- **Tax awareness** — flag structured or allocated amounts the client should discuss with a tax professional; do not provide tax advice
- **Confidentiality** — if delivered electronically, note document should be encrypted with password communicated separately
- **Retention** — flag for archival per firm policy for applicable statute of limitations plus professional responsibility retention period
