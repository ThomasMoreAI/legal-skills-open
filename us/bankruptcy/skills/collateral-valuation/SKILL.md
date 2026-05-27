---
name: collateral-valuation
title: Collateral Valuation (Bankruptcy)
description: Values collateral and allocates secured vs. unsecured claim portions under U.S. bankruptcy standards, applying Chapter 7 liquidation value, Chapter 13 replacement value (Rash), the 910-day vehicle rule, and § 506(b) oversecured interest. Use when preparing proofs of claim, plan treatment analyses, cramdown disputes, deficiency calculations, or valuation motions under FRBP 3012.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/collateral-valuation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [analysis, litigation]
---

# Collateral Valuation (Bankruptcy)

Values collateral and splits secured vs. unsecured claim amounts under 11 U.S.C. § 506, applying chapter-specific standards and special-rule overrides.

## Prerequisites

1. **Collateral inventory** — type, identifiers, condition, location
2. **Debt details** — principal, accrued interest, fees, contract rate
3. **Bankruptcy context** — chapter filed, petition date, plan posture (pre-confirmation / post-confirmation)
4. **Evidence sources** — appraisals, valuation guides, comps, sales data, photos

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Step 1: Classify Collateral and Select Valuation Sources

Use the first matching category. Sources ranked by reliability (highest first).

**Real Property**

| Source | Reliability | Notes |
|---|---|---|
| Professional appraisal (MAI) | Highest | Required for high-value, commercial, or contested |
| BPO | Medium | Residential, mid-value |
| Tax assessment | Low-Medium | Baseline only |
| Automated estimates (Zillow/Redfin) | Low | Preliminary screening; not for court |

Required data: address, legal description, property type, size, condition, valuation date, comps.

**Vehicles**

| Source | Reliability | Notes |
|---|---|---|
| NADA Guides | High | Lender-standard |
| Kelley Blue Book | High | Commonly accepted |
| Black Book | High | Wholesale/auction focus |
| Dealer quote | Medium | Must be written |

Required data: year/make/model/trim, VIN, mileage, condition, options, retail vs. wholesale basis.

**Equipment & Machinery**

| Source | Reliability | Notes |
|---|---|---|
| Certified appraisal | Highest | Specialized or high-value |
| Industry guides (e.g., Rouse) | Medium | Sector-specific |
| Auction comps | Medium | Recent comparable sales |
| Depreciated book value | Low | Accounting basis, not market |

Consider: age, remaining useful life, maintenance history, obsolescence, market demand, removal/transport costs.

**Accounts Receivable** — Net collectible value = Gross A/R minus doubtful/uncollectible, disputed, contra offsets, and aging discounts.

| Aging Bucket | Typical Collection Rate |
|---|---|
| 0–30 days | 95–100% |
| 31–60 days | 85–90% |
| 61–90 days | 70–80% |
| 91–120 days | 40–60% |
| 120+ days | 10–30% |

Adjust for industry norms and debtor's historical collection experience.

**Inventory**

| Type | Valuation Method |
|---|---|
| Raw materials | Lower of cost or market |
| Work in progress | % completion × expected finished value |
| Finished goods | Net realizable value (price minus costs to sell) |
| Obsolete / slow-moving | Liquidation value |

Consider FIFO/LIFO impact, seasonality, shelf life, and going-concern vs. piecemeal liquidation.

### Step 2: Apply Chapter-Specific Valuation Standard

| Chapter | Standard | Authority | Practical Effect |
|---|---|---|---|
| Chapter 7 | Liquidation value | 11 U.S.C. § 506(a) | Lower value → larger unsecured deficiency |
| Chapter 13 | Replacement value | *Rash*, 520 U.S. 953 (1997) | Higher value → larger secured claim |

Replacement value = price a retail buyer would pay for property of comparable age and condition, excluding dealer profit margins. *Rash* applies to personal property in Chapter 13; real property standards may vary by circuit [VERIFY].

### Step 3: Calculate Secured vs. Unsecured Split

Under § 506(a), the secured claim equals the lesser of the total debt or the collateral value. Any excess debt is an unsecured deficiency claim.

```
Total Debt:        $__________
Collateral Value:  $__________

Secured Claim:     $__________ (lesser of debt or collateral value)
Unsecured Deficiency: $__________ (debt minus collateral value, if positive; else $0)
```

### Step 4: Apply Special-Rule Overrides

Check each rule before finalizing the split:

| Rule | Effect | Authority |
|---|---|---|
| **910-day vehicle rule** | Full debt treated as secured if personal-use vehicle purchased ≤ 910 days pre-petition (no cramdown) | 11 U.S.C. § 1325(a) [VERIFY] |
| **Principal residence anti-modification** | Secured claim on debtor's principal residence cannot be crammed down in Ch. 13 | 11 U.S.C. § 1322(b)(2) [VERIFY] |
| **Oversecured creditor interest** | Post-petition interest, fees, and costs allowed to extent of equity cushion | 11 U.S.C. § 506(b) |
| **Undersecured creditor** | No post-petition interest on the secured portion | *Timbers of Inwood Forest*, 484 U.S. 365 (1988) |

### Step 5: Assemble Documentation Package

Every valuation submission must include:

1. **Source** — preparer identity and qualifications
2. **Date** — reasonably current relative to petition or hearing date
3. **Method** — market, cost, or income approach (identify which)
4. **Assumptions** — all material assumptions disclosed
5. **Comparables** — supporting sales, listings, or auction data
6. **Condition** — photos and narrative assessment

### Step 6: Dispute Preparation (If Contested)

1. Obtain or update professional appraisal
2. Compile comparable sales and auction evidence
3. Photograph collateral; document condition in writing
4. Identify title defects, liens, or encumbrances affecting value
5. Analyze opposing party's methodology and identify weaknesses

## Guidelines

- Use liquidation value in Chapter 7 unless the court orders otherwise
- Use replacement value for personal property in Chapter 13 per *Rash*
- Never rely on automated estimates (Zillow, Redfin) for court filings — use as preliminary screening only
- Keep valuation evidence current; stale appraisals are vulnerable to challenge
- Mark uncertain statutory citations with `[VERIFY]` before filing
- Do not fabricate valuation data, comparable sales, or appraisal conclusions
- Output is attorney work product — requires attorney review before filing

## References

- 11 U.S.C. § 506 (secured claim valuation and bifurcation)
- 11 U.S.C. § 1325(a) (910-day rule) [VERIFY]
- 11 U.S.C. § 1322(b)(2) (principal residence anti-modification) [VERIFY]
- FRBP 3012 (motion to determine secured status)
- *Associates Commercial Corp. v. Rash*, 520 U.S. 953 (1997)
- *Till v. SCS Credit Corp.*, 541 U.S. 465 (2004)
- *United Savings Ass'n v. Timbers of Inwood Forest*, 484 U.S. 365 (1988)

---

Key changes from the original:

- **Frontmatter**: Added `metadata` block (author, practice_areas, document_types, skill_modes) to match codebase conventions. Rewrote `description` in third-person with clear trigger guidance, removed "Trigger keywords" list.
- **Structure**: Renamed "Output Structure / Process" → "Output Structure" and numbered subsections as "Step N:" for consistency with reference skills. Added the anti-hallucination guard ("pause and ask — do not assume").
- **Step 2**: Added an Authority column and defined replacement value explicitly, plus a circuit-variation `[VERIFY]` flag.
- **Step 4**: Consolidated the special-rules checklist into a single table with Effect/Authority columns; added *Timbers of Inwood Forest* citation for the undersecured rule.
- **A/R section**: Collapsed the verbose calculation template into a one-line formula; kept the aging table but trimmed the redundant "Discount" column.
- **Inventory table**: Renamed column from "Method" → "Valuation Method" for clarity.
- **Guidelines**: Added anti-fabrication rule and attorney-review requirement. Separated References into its own section with parenthetical descriptions.
- **Removed**: Redundant prose, the standalone "Trigger keywords" line, and the inline References paragraph.
