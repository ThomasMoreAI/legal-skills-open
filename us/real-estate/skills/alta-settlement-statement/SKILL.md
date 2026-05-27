---
name: alta-settlement-statement
title: ALTA Settlement Statement
description: Drafts a mathematically balanced ALTA Settlement Statement for U.S. real estate closings, allocating debits and credits between buyer and seller with prorations, payoffs, lender fees, title charges, and transfer taxes. Enforces balance verification (seller credits minus debits equals cash to seller; buyer debits minus credits equals cash from buyer) and cross-references title commitment, loan documents, and purchase agreement. Use when preparing closing financials, settlement statements, HUD-equivalent documents, or real estate closing allocations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/alta-settlement-statement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, summary, transactional]
---

# ALTA Settlement Statement

Drafts a mathematically balanced, ALTA-compliant settlement statement allocating all transaction costs between buyer and seller at closing.

## Prerequisites

1. **Purchase and Sale Agreement** — sales price, earnest money, seller concessions, cost allocation.
2. **Title Commitment** — premiums, endorsements, exception items requiring payoff.
3. **Loan Documents** — new loan amount, lender fees, prepaid items.
4. **Payoff Statements** — existing mortgage(s) and lien balances with per diem rates.
5. **Closing/Disbursement Dates** — both required for proration calculations.
6. **Tax Records** — current year amount, payment status (arrears vs. advance), last paid date.
7. **HOA Documents** — dues, transfer fees, special assessments.
8. **Commission Instructions** — total amount and brokerage split.

## Output Structure

### Header Block

| Field | Content |
| --- | --- |
| Settlement Date | Date documents are signed |
| Disbursement Date | Date funds are distributed |
| Settlement Agent | Name, firm, address, phone |
| Property Address | Street address + legal description reference |
| Buyer/Borrower | Full legal name(s) |
| Seller | Full legal name(s) |

### Seller's Transaction

**Credits to Seller:** Gross sales price; seller financing; prorated items in seller's favor; earnest money (if seller-held).

**Debits against Seller:** Existing mortgage payoff(s) + per diem interest; second liens and judgment payoffs; commissions (listing + selling); seller-paid closing costs per contract; owner's title insurance (if seller-paid); transfer taxes; recording fees; repair credits / concessions to buyer; HOA dues, transfer fees, estoppel fees; prorated property taxes (seller's share through closing).

**Net:** Cash Due to Seller (or Cash Required from Seller if negative).

### Buyer's Transaction

**Debits to Buyer:** Gross sales price; lender origination fees, points, underwriting; appraisal, credit report, flood cert; prepaid interest (closing through month-end); initial escrow deposit (tax + insurance reserves); hazard insurance premium; owner's title insurance (if buyer-paid); lender's title insurance + endorsements; recording fees (deed + mortgage); transfer taxes; HOA transfer fees, working capital; prorated items owed to seller.

**Credits to Buyer:** Earnest money deposit(s); new loan proceeds; seller concessions / closing cost credits; assumed loans or seller financing; prorated items in buyer's favor.

**Net:** Cash Required from Buyer (or Cash Due to Buyer if negative).

## Proration Calculations

| Charge Type | Method |
| --- | --- |
| Annual charges (taxes, HOA annual) | 365-day year; seller responsible through day before disbursement |
| Monthly charges (HOA monthly) | Actual days in month |
| Existing mortgage interest | Per diem rate from payoff statement |
| Prepaid lender interest | Daily rate × days from closing through month-end |

Tax proration: Confirm whether jurisdiction collects in arrears (seller credits buyer for elapsed year) or advance (buyer credits seller for prepaid period). If current year bills are not yet issued, use prior year as estimate and mark `[ESTIMATE — SUBJECT TO FINAL TAX BILL]`.

## Balance Verification

- [ ] Seller credits − seller debits = cash to seller
- [ ] Buyer debits − buyer credits = cash from buyer
- [ ] Loan proceeds + cash from buyer = sales price + all buyer-side charges
- [ ] Payoff figures match current payoff statements to the penny
- [ ] Prorations use confirmed disbursement date (not estimated)
- [ ] Lender fees match Closing Disclosure line-for-line (if applicable)
- [ ] Title charges match title company invoice
- [ ] Commission amounts match executed commission instructions
- [ ] Earnest money appears as buyer credit only (not duplicated as seller debit)

## Guidelines

- Mark unconfirmed figures `[ESTIMATE — CONFIRM BEFORE CLOSING]`.
- All amounts to two decimal places; no rounding mid-calculation.
- Allocate transfer taxes per contract; default to jurisdictional custom if silent.
- Recording fee allocation (deed vs. mortgage) varies by state — follow contract, then local custom.
- For simultaneous-issue title rates, confirm premium split with title company before using schedule rates.
- ALTA Settlement Statement does not replace CFPB Closing Disclosure on residential consumer mortgage transactions — both may be required.
- Payoff statements typically expire in 30 days; do not finalize until current payoff is confirmed.

## Troubleshooting

- **Statement does not balance:** Re-verify that every charge appears on exactly one side. Check that earnest money is a buyer credit only and not also deducted from seller. Recompute prorations from scratch using disbursement date.
- **Proration dispute:** Confirm arrears vs. advance collection method for the jurisdiction. Verify whether the contract specifies a proration method or cutoff date that overrides default.
- **Payoff mismatch:** Request a refreshed payoff statement; per diem interest may have shifted the total. Confirm the payoff good-through date matches the disbursement date.
- **Lender fees do not match Closing Disclosure:** Compare line-by-line; lender may have updated fees after initial disclosure. Flag discrepancies as `[VERIFY]` and resolve with lender before closing.
