---
name: asset-purchase-agreement
title: Asset Purchase Agreement
description: Drafts a U.S. Asset Purchase Agreement for deals where a buyer acquires specified business assets while avoiding unwanted liabilities. Enforces itemized asset/liability schedules, purchase price mechanics with working capital true-ups, IRS Form 8594 tax allocation, seller and buyer reps and warranties with disclosure schedules, pre- and post-closing covenants, closing conditions and deliveries, and indemnification with basket/cap limits. Use when drafting an asset purchase agreement, APA, asset acquisition, purchase and sale of assets, asset deal, or excluded liabilities agreement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/asset-purchase-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [transactional, agreement, drafting]
---

# Asset Purchase Agreement

Draft a transaction-ready APA that precisely allocates assets, liabilities, and post-closing risk between buyer and seller.

## Prerequisites

1. **Parties and structure** — legal names, entity types, jurisdictions, signing authority, deal structure
2. **Asset and liability inventory** — preliminary lists for Purchased Assets, Excluded Assets, Assumed Liabilities, Excluded Liabilities
3. **Economic terms** — purchase price, payment form, adjustments, earnouts, escrow/holdback, allocation
4. **Key deal risks** — regulatory approvals, consents, IP chain of title, material contracts, employee transition, environmental exposure
5. **Timeline** — signing/closing schedule, deliverables, conditions

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Step 1: Document Skeleton

Draft in this order:

1. Parties; Effective Date; Recitals
2. Definitions
3. Purchase and Sale of Assets
4. Excluded Assets
5. Assumed Liabilities
6. Excluded Liabilities
7. Purchase Price; Payment; Adjustments; Allocation
8. Closing; Closing Deliveries
9. Representations and Warranties of Seller
10. Representations and Warranties of Buyer
11. Covenants (Pre-Closing; Post-Closing)
12. Non-Competition / Non-Solicitation (if applicable)
13. Conditions to Closing
14. Indemnification
15. Miscellaneous; Signatures; Exhibits and Schedules

### Step 2: Exhibits and Schedules

| Label | Purpose | Must Include |
|---|---|---|
| Exhibit A | Purchased Assets | Detailed categories and itemized lists |
| Exhibit B | Excluded Assets | Cash, A/R (if excluded), retained contracts, corporate records |
| Exhibit C | Assumed Liabilities | Specific obligations, amounts, contract IDs |
| Exhibit D | Purchase Price Allocation | IRS Form 8594 class allocation |
| Disclosure Schedules | R&W exceptions | Numbered to match each R&W subsection |

### Step 3: Asset Scope and Exclusions

- Define "Purchased Assets" by category; cross-reference Exhibit A
- "As is, where is" only if consistent with negotiated reps/warranties
- Include books/records, data, IP, goodwill, domain names, social accounts if intended
- Catch-all exclusion: anything not in Exhibit A is excluded
- List retained corporate records, tax returns, insurance policies, non-assigned contracts

### Step 4: Liability Allocation

- "Assumed Liabilities" strictly limited to Exhibit C items
- "Excluded Liabilities" covers pre-closing operations, taxes, employee obligations, litigation, environmental

### Step 5: Price, Adjustments, and Tax Allocation

- Payment timing, wire instructions, escrow/holdback terms
- Working capital or inventory true-up: baseline, measurement method, dispute process, timing
- IRS Form 8594 allocation; covenant for consistent reporting by both parties

### Step 6: Reps and Warranties

**Seller R&W**: Organization/authority; title to assets; financials; compliance; material contracts; litigation; taxes; IP; employees/benefits; environmental. Apply materiality and knowledge qualifiers where negotiated.

**Buyer R&W**: Organization/authority; enforceability; funds/financing; no conflicting approvals; governmental consents.

Number each R&W subsection to match its corresponding disclosure schedule.

### Step 7: Covenants

- **Pre-closing**: ordinary-course operation; no asset transfers; no new debt; no material contract changes
- **Post-closing**: preserve goodwill; restrict Seller use of transferred name/marks
- **Non-compete / non-solicit** (if applicable): define restricted business, geography, duration, consideration; include reformation/severability clause

### Step 8: Closing Conditions and Deliveries

| Party | Conditions | Deliveries |
|---|---|---|
| Seller | Accuracy of reps, covenant performance, no MAE, consents received | Bill of sale, assignments, lien releases, officer's certificate, good standing |
| Buyer | Accuracy of reps, covenant performance | Payment, assumption agreement, officer's certificate |

### Step 9: Indemnification

- Seller indemnifies for breaches, excluded liabilities, pre-closing operations
- Buyer indemnifies for breaches and assumed liabilities
- Include notice procedures, defense control, cooperation obligations
- **Limits**: basket (deductible vs. tipping), cap, survival periods, fraud carve-out, insurance offset

### Step 10: Assignment and Assumption

- Reference separate assignment agreements for contracts and IP
- Identify third-party consent requirements; state non-assignment where prohibited by law or contract
- Carve out non-assignable items at closing

## Guidelines

- Keep asset and liability schedules itemized and cross-referenced; never use "all assets" without categories
- Confirm third-party consent requirements before drafting assignment language
- Match disclosure schedule numbering to each R&W subsection exactly
- Use defined terms consistently; avoid duplicate definitions across exhibits
- Non-compete enforceability varies by state — tailor duration and geography to local law [VERIFY]
- Tax allocation must align with economics and both parties' reporting obligations
- If regulated assets or licenses are involved, add specific regulatory approval conditions
- If data or IP is included, confirm chain of title and include transfer instruments
- Output is draft work product requiring attorney review — not legal advice
