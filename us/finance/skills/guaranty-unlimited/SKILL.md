---
name: guaranty-unlimited
title: Unlimited Guaranty
description: Drafts a U.S. Unlimited Guaranty for commercial lending transactions. Triggers when user needs an uncapped personal or entity guaranty, credit enhancement, or unlimited recourse instrument for a loan closing. Produces an absolute guaranty of payment (not collection) with comprehensive waivers, subrogation subordination, and continuing-guaranty coverage.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/guaranty-unlimited
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Unlimited Guaranty

Generates a complete Unlimited Guaranty giving the Lender direct, uncapped recourse against a Guarantor for all present and future Borrower obligations.

## Quick Start

Collect before drafting:

1. **Credit documents** — loan agreement, note, or facility defining the guaranteed Obligations
2. **Parties** — full legal names of Guarantor, Borrower, and Lender
3. **Guarantor type** — individual or entity (drives signature block and authority recitals)
4. **Financial reporting** — whether Lender requires ongoing financials from Guarantor

## Document Sections

| # | Section | Key Content |
|---|---------|-------------|
| 1 | Definitions | Obligations (all present/future amounts), Credit Documents, parties |
| 2 | Guaranty of Payment | Absolute, unconditional; payment not collection — Lender may proceed directly against Guarantor |
| 3 | Unlimited Liability | No cap; covers principal, interest, fees, costs, expenses, indemnities |
| 4 | Waivers | Full checklist below |
| 5 | Subrogation & Reimbursement | Subordinated/waived until indefeasible payment in full |
| 6 | Continuing Guaranty | Survives modifications, renewals, extensions; covers post-execution obligations |
| 7 | Financial Covenants *(if required)* | Annual financials, MAC notice, other reporting |
| 8 | Governing Law & Jurisdiction | Match underlying loan documents |
| 9 | Jury Trial Waiver | Standard commercial waiver |
| 10 | Signature Block | Individual: name + date; Entity: officer title + authority recital |

### Required Waivers (Section 4)

Guarantor must waive all of the following:

- Presentment, demand for payment, protest, notice of dishonor
- Notice of acceptance of Guaranty
- Notice of creation or incurrence of new Obligations
- Notice of any Borrower or Lender action or inaction
- Right to require Lender to proceed first against Borrower or exhaust collateral
- Defense based on modification, extension, renewal, or amendment of Obligations
- All suretyship defenses (collateral impairment, co-guarantor release, etc.)
- Right to require marshaling of assets

### Subrogation Language (Section 5)

> Until all Obligations are indefeasibly paid in full and all Lender commitments are terminated, Guarantor waives and subordinates: (i) any subrogation right to Lender's claims against Borrower; (ii) any reimbursement or indemnity right from Borrower; and (iii) any right to participate in Lender-held security.

## Pitfalls & Checks

- **Payment not collection** — Section 2 must expressly allow Lender to proceed against Guarantor without exhausting Borrower remedies or collateral
- **"Indefeasibly paid in full"** — always use this phrase, not merely "paid in full," to protect against bankruptcy preference/clawback
- **Governing law** — must match the underlying loan documents' choice of law and forum
- **Entity authority** — for entity Guarantors, include officer certificate or board resolution recital if Lender requires
- **Continuing guaranty** — confirm language covers obligations arising after execution
- **[VERIFY]** US jurisdiction only; state suretyship statutes may impose additional requirements
- **[VERIFY]** Anti-deficiency statutes (CA, AZ, others) may limit enforceability of certain waivers — flag for attorney review

---
