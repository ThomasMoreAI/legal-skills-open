# Closing Disclosure — Page-by-Page Data Intake

Complete data set for the five-page CFPB Form H-25 Closing Disclosure. Use this as the intake checklist during Step 1 of the SKILL.md loop. Any field that cannot be sourced is recorded as `MISSING`; do not fabricate.

| Page | Section | Required Inputs |
|------|---------|-----------------|
| 1 | Closing/transaction/loan info | Issue date, closing/disbursement dates, borrower(s), seller(s), property address, sale price, lender, loan term, purpose, product, loan ID |
| 1 | Loan terms | Loan amount, rate, P&I, prepay penalty, balloon |
| 1 | Projected payments | P&I, MI, escrow, totals by period |
| 1 | Costs at closing | Total closing costs, lender credits, cash to close |
| 2 | Loan costs (A–C) | Origination, lender-required services, shopped services |
| 2 | Other costs (E–H) | Government fees, prepaids, escrows, commissions, owner's title |
| 2 | Totals (D, I, J) | Subtotals and lender credits |
| 3 | Cash to close | LE vs CD comparison with change reasons |
| 3 | Summaries (K–N) | Borrower/seller transaction summaries, credits, payoffs |
| 4 | Loan disclosures | Assumption, demand, late fee, neg-am, partial payments |
| 4 | Escrow account | Escrowed vs non-escrowed costs, waiver fee |
| 4 | ARM tables | AP/AIR tables (if ARM) |
| 5 | Loan calculations | Total of payments, finance charge, amount financed, APR, TIP |
| 5 | Other disclosures | Appraisal, contract details, liability, refinance, tax |
| 5 | Contact info | Lender / broker / RE agent / settlement agent identifiers |

## What to flag as MISSING vs `[VERIFY]`

- **MISSING** — the field has no source value at all. Settlement agent has not yet supplied the prorations; the lender has not stated the loan ID; the survey came in but the parcel ID is not in the file. Block finalization until resolved.
- **`[VERIFY]`** — the field has a value but the source is ambiguous, contradicted by another document, or jurisdiction-dependent. Surface in the review memo and require attorney/closer confirmation.

## Cross-document reconciliation

Several Page 3 / Page 5 figures must reconcile against other documents in the file:

- **Cash to close** vs the wire instructions and the borrower's funding source.
- **Seller proceeds / payoffs** vs the existing-mortgage payoff letter(s) and any recorded liens (UCC, mechanics', tax).
- **Recording fees / transfer taxes** vs the title commitment's required-cure items and the relevant state/county fee schedule.
- **Escrow / prepaids** vs the insurance binder, tax bill, and (if HOA) the estoppel.
- **APR + TIP** vs the lender's loan-program disclosures and the truth-in-lending math.

Discrepancies are not edited silently into the CD; they are listed in the review memo for the responsible party to resolve.

## Relationship to ALTA settlement statements

The CD is the federally-mandated TRID disclosure for federally-related residential mortgage transactions. The ALTA Settlement Statement is the title-industry settlement disclosure and is the operational close-out document for non-TRID transactions (cash deals, commercial, certain assumptions). For deals that have both, the figures must match. See `alta-settlement-statement` for the ALTA workflow.

## Citations

- 12 CFR 1026.38 — Form H-25 content requirements `[VERIFY]`
- 12 CFR 1026.19(f) — CD timing and delivery `[VERIFY]`
- 12 CFR 1026.19(e)(3) — LE good-faith determination `[VERIFY]`

For tolerance bucket math, see `closing-disclosure-tolerance`. For the 3-business-day waiting period and re-disclosure timing, see `closing-disclosure-timing-reference`.
