---
name: proration-schedule
title: Proration Schedule
description: Drafts a legally compliant proration schedule for real estate closings, allocating taxes, HOA fees, rent, utilities, and other obligations between buyer and seller. Triggered when preparing settlement documents, closing prorations, asset purchase closings, or real estate closing statements requiring expense allocation by closing date.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/proration-schedule
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Proration Schedule

Drafts a mathematically precise proration schedule allocating property expenses, income, and obligations between buyer and seller at closing.

## Prerequisites

Collect before drafting:

1. **Purchase agreement** — closing date, closing-date-charge convention, proration terms
2. **Property tax records** — current/prior year bills, assessment notices, pending appeals
3. **HOA documents** — governing docs, statements, special assessments
4. **Lease agreements** (if tenant-occupied) — rent rolls, security deposits, prepaid rent
5. **Utility bills** — water, sewer, trash, property-linked services
6. **Title commitment** — legal description, parcel ID, encumbrances
7. **Insurance policies** (if transferring) — premiums and coverage periods

## Quick Start

1. Gather all prerequisite documents
2. Set closing date and day-count convention (365-day default or 360-day if jurisdictionally required)
3. Determine closing-date allocation (buyer or seller bears closing date)
4. Identify all proration items from the checklist
5. Calculate daily rates and allocations for each item
6. Draft post-closing adjustment provision for estimated amounts
7. Verify net proration ties to settlement statement / Closing Disclosure

## Document Header

Include: document title ("Proration Schedule"), preparation date, closing date, property (address + legal description + parcel ID), escrow/file number, seller(s) and buyer(s) full legal names and addresses, applicable jurisdiction, and day-count convention used.

## Proration Items Checklist

Identify all applicable items:

- Real property taxes (actual or estimated)
- HOA regular fees and special assessments
- Rental income and security deposit transfers
- Water/sewer, trash, other property-linked utilities
- Prepaid insurance premiums (if policy transfers)
- Improvement district / special district charges

## Calculation Table

For each proration item, present:

| Column | Description |
|--------|-------------|
| Item | Description of charge |
| Total Amount | Full periodic amount |
| Period Covered | Start–end dates |
| Daily Rate | Total ÷ days in period |
| Seller Days / Amount | Days responsible × daily rate |
| Buyer Days / Amount | Days responsible × daily rate |
| Credit To | Buyer or Seller |

### Day-Count Convention

- **Default:** 365-day year (actual days per period)
- **Alternative:** 360-day year / 30-day months — apply local convention and document which is used

### Closing-Date Allocation

1. Check purchase agreement for explicit allocation
2. If silent, apply prevailing jurisdictional custom
3. Document the convention in the schedule header

## Property Tax Rules

- State whether based on **actual** or **estimated** (prior-year) bill
- Disclose pending reassessments or tax appeals and explain impact
- Arrears jurisdictions: seller credited for prepayment or debited for accrued liability
- Advance-payment jurisdictions: seller credited for post-closing prepaid portion
- Always include post-closing true-up provision

## Rental Income Rules

- Prorate collected rent as of closing date
- Advance rent beyond closing → credit to buyer
- Security deposits: **transfer** to buyer (not prorated); seller receives corresponding debit
- Note partial-month rent calculations

## Summary

Net proration must appear as:

- Total credits to seller
- Total credits to buyer
- Net proration adjustment (credit to buyer or seller)

This net figure must tie exactly to the proration line on the settlement statement / Closing Disclosure.

## Post-Closing Adjustment Provision

Include clauses for:

1. **Property taxes** — true-up if actual bill differs from estimate by more than $[threshold]; buyer obtains final bill; adjustment within [X] days
2. **Utilities** — final meter readings post-closing; seller liable through closing date; 60-day adjustment deadline
3. **Retroactive assessments** — seller liable for charges attributable to seller's ownership period
4. **Refunds** — buyer remits to seller any refund/credit for seller's ownership period
5. **Settlement method** — direct payment between parties unless otherwise agreed

## Regulatory Compliance

- **TILA-RESPA** (residential + federally related mortgage): proration figures must match Closing Disclosure entries; this schedule is backup documentation
- **State-specific rules:** verify jurisdiction-mandated calculation methods, required disclosures, and statutory allocation requirements
- Note applicable jurisdiction in document header

## Execution Block

Signature lines for all buyers and sellers: printed name, signature, date, and acknowledgment that parties reviewed calculations and agree to allocations. Label as exhibit to settlement statement / Closing Disclosure.

## Pitfalls and Checks

- Show all math — every daily rate derivation must be visible
- Match name/entity references to title documents exactly
- Number all pages; include property address and closing date in footer
- Flag estimated amounts and tie to post-closing adjustment provision
- Never assume tax amounts — use prior-year estimate if bills unavailable and label accordingly
- Add notary blocks if required by lender or local custom
- **Final check:** net proration must reconcile to settlement statement line item
