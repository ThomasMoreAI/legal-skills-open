---
name: convertible-note-purchase-agreement
title: Convertible Note Purchase Agreement
description: Drafts a company-side Convertible Note Purchase Agreement for U.S. early-stage convertible debt financings. Structures note economics, conversion mechanics, reps and warranties, closing conditions, covenants, default provisions, and miscellaneous terms. Use when drafting a convertible note purchase agreement, bridge note, convertible debt financing, or SAFE alternative for a startup or early-stage company.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/convertible-note-purchase-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Convertible Note Purchase Agreement

Drafts a company-side CNPA for U.S. early-stage convertible debt financings. Covers the full agreement from preamble through miscellaneous provisions.

## Prerequisites

Gather before drafting:

1. **Parties** — legal names, jurisdictions, authorized signatories (issuer + each purchaser)
2. **Economics** — aggregate principal, purchase price, interest rate (simple/compound), maturity date, valuation cap, discount rate
3. **Conversion mechanics** — qualified financing threshold, optional conversion triggers, conversion price formula
4. **Cap table** — all outstanding equity and debt (for rep accuracy)
5. **Authorization** — term sheet or board resolution confirming deal economics
6. **Use of proceeds** — stated business purpose

## Drafting Workflow

### 1. Preamble

Date, full legal names, recitals stating financing purpose and issuance authority.

### 2. Purchase and Sale of Notes

- Note description: aggregate principal, per-note denomination, series designation
- Purchase price: face value or specify OID if issued at discount
- Closing mechanics: date, wire instructions, deliverables (executed notes to Purchasers; funds to Company)

### 3. Company Representations and Warranties

Include reps for: organization and good standing, corporate authority (board authorization, no charter/bylaw conflicts), capitalization (fully-diluted cap table with all convertible instruments), no material litigation, compliance with law, financial statement accuracy, no default under material agreements, and use of proceeds.

### 4. Purchaser Representations and Warranties

Include reps for: accredited investor status under Rule 501 [VERIFY], investment intent (own account, not for distribution), restricted securities acknowledgment, sophistication and ability to bear loss, and independent investigation.

### 5. Conditions to Closing

- Reps and warranties true as of closing
- All pre-closing covenants performed
- No material adverse change
- Legal opinion from Company counsel (if required)
- All ancillary documents executed (side letters, ROFR waivers)
- Board/stockholder approvals obtained
- No injunction or legal prohibition

### 6. Post-Closing Covenants

- Use of proceeds restricted to stated purpose
- Financial reporting to Noteholders (specify frequency/format)
- Additional indebtedness: parity or subordination rules
- Maintain corporate existence; no dissolution without majority Noteholder consent
- Prompt default notice to Noteholders
- Inspection rights (if negotiated)

### 7. Note Terms

| Term | Detail |
|---|---|
| Interest | Annual rate; simple vs. compound; accrual start date |
| Maturity | Date principal + accrued interest due |
| Automatic conversion | Triggers on Qualified Financing exceeding threshold (e.g., $1M+ equity) |
| Optional conversion | Noteholder election at/after maturity or upon Change of Control |
| Conversion price | Lesser of: (i) Valuation Cap / Fully-Diluted Shares; (ii) Next Round Price x (1 - Discount Rate) |
| Anti-dilution | Broad-based weighted-average; specify excluded share carve-outs |
| Change of Control | Cash repayment at premium, or Noteholder election to convert |
| MFN | If applicable, match superior terms offered to later note purchasers |

### 8. Events of Default and Remedies

| Default | Remedy |
|---|---|
| Failure to pay at maturity | Acceleration; default interest rate |
| Breach of rep/warranty | Acceleration after notice + cure period |
| Breach of covenant | Acceleration after notice + cure period |
| Insolvency/bankruptcy | Automatic acceleration; no notice required |
| Unapproved Change of Control | Convert at cap price or cash repayment at premium |

### 9. Indemnification

Company indemnifies Purchasers for breach of Company reps, warranties, or covenants. Specify: claim notice procedure, rep survival period, indemnification cap (if any), and basket/deductible (if any).

### 10. Miscellaneous

Governing law (typically Delaware), dispute resolution and venue, notice provisions, amendment (Company + majority-in-interest by principal), entire agreement/integration, severability, counterpart execution with electronic signatures, and jury trial waiver (confirm enforceability).

## Critical Checks

- **Securities exemption**: Issue under Reg D 506(b) or 506(c) [VERIFY]; confirm all Purchasers are accredited; file Form D within 15 days of first sale [VERIFY]
- **State blue sky**: Confirm notice/exemption filings for each Purchaser's state
- **Authorized shares**: Verify sufficient authorized but unissued shares for full conversion at cap price; flag if stockholder approval needed to increase
- **Cap vs. discount**: Both apply simultaneously — use whichever yields lower per-share price (more favorable to Noteholder) unless negotiated otherwise
- **OID/tax**: If issued below face value, flag for tax counsel review of original issue discount rules
- **Subordination**: Confirm senior, pari passu, or subordinated status; obtain required lender consents
- **Outstanding SAFEs**: Address priority and interaction at conversion; check for MFN or pro-rata rights affecting this issuance
- **Jurisdiction**: U.S. transactions only; non-U.S. elements require local counsel
