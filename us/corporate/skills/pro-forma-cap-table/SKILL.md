---
name: pro-forma-cap-table
title: Pro Forma Capitalization Table
description: Drafts a pro forma capitalization table modeling ownership before and after a financing event or corporate transaction. Calculates dilution, conversion mechanics, option pool impacts, and ownership on as-converted and fully-diluted bases. Use when modeling seed rounds, Series A/B/C financings, convertible note or SAFE conversions, option pool expansions, stock splits, or cap table restructurings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pro-forma-cap-table
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [analysis, drafting]
---

# Pro Forma Capitalization Table

Models a company's ownership structure before and after a contemplated transaction, showing dilution effects and economic implications for all stakeholders.

## Prerequisites

1. **Corporate documents** — certificate of incorporation, stockholder agreements, option plans, convertible note/SAFE agreements, prior cap tables
2. **Current share register** — all holders by name, class, share count; outstanding options with exercise prices and vesting; warrants with terms
3. **Preferred stock terms** — liquidation preferences (multiple, participating/non-participating), anti-dilution provisions, conversion ratios, dividend rights per series
4. **Transaction terms** — investment amount, pre-money valuation, price per share, new investor allocations, option pool target, conversion mechanics (caps, discounts, interest)

## Output Structure

### Section 1: Header & Assumptions

| Element | Detail |
|---|---|
| Company legal name | As registered with Secretary of State |
| Date of preparation | Current date |
| Designation | "PRO FORMA — not final or binding" |
| Reference date | Baseline capitalization date |
| Transaction type | Seed, Series [X], note conversion, pool expansion, etc. |

**Assumptions table:**

| Assumption | Value |
|---|---|
| Pre-money valuation | $ amount + derivation method |
| New capital raised | $ amount |
| Post-money valuation | $ amount |
| Price per share | Calculation: pre-money ÷ pre-money fully-diluted shares |
| Liquidation preference | Multiple + participating/non-participating |
| Anti-dilution | Weighted average / full ratchet / none |
| Option pool timing | Pre-money or post-money inclusion |
| Option pool target | % of post-transaction fully-diluted |
| Convertible instrument terms | Cap, discount, interest rate, MFN |

### Section 2: Pre-Transaction Capitalization

| Holder / Category | Class | Shares Held | As-Converted % | Fully-Diluted % |
|---|---|---|---|---|

**Row order:**
1. Preferred stock — reverse chronological by series
2. Common stockholders — founders, employees, other
3. Option pool: outstanding grants (exercise price range), exercised (now common), available for future grants
4. Warrants / other derivatives (exercise price, expiration)

Footnote each preferred series with liquidation preference amount, participation rights, accrued dividends.

**Definitions:**
- **As-converted** = all preferred converts to common; excludes unissued pool shares
- **Fully-diluted** = as-converted + all outstanding options/warrants + entire unissued pool

### Section 3: Transaction Adjustments

Present each adjustment sequentially.

**New equity issuance:**

| Investor | Shares Issued | Price/Share | Investment ($) |
|---|---|---|---|

**Convertible note conversion:**

| Holder | Principal | Accrued Interest | Total Converting | Conversion Price | Shares Issued |
|---|---|---|---|---|---|

Conversion price = min(cap-based price, discounted price). Show derivation.

**SAFE conversion:**

| Holder | Investment | Valuation Cap | Discount | Conversion Price | Shares Issued |
|---|---|---|---|---|---|

**Option pool expansion:**

| Item | Shares |
|---|---|
| Pre-transaction pool | X |
| New shares added | X |
| Post-transaction pool | X |
| Pool as % of post-transaction FD | X% |

Note whether expansion is pre-money (dilutes existing holders) or post-money (dilutes all including new investors).

**Repurchases / cancellations** (if applicable): holder, shares, price, reason.

### Section 4: Post-Transaction Capitalization

| Holder / Category | Class | Pre-Txn Shares | New / Converted | Post-Txn Shares | As-Converted % | Fully-Diluted % |
|---|---|---|---|---|---|---|

Same row order as Section 2; new series listed first. Include subtotals per class and grand total.

**Verification checklist:**
- [ ] All FD ownership percentages sum to 100.00%
- [ ] All as-converted percentages sum to 100.00%
- [ ] Post-txn shares = pre-txn + new issuances + conversions + pool expansion − repurchases
- [ ] Price per share × new shares = total new investment

### Section 5: Exit Waterfall (if multi-series preferred)

Model distribution at illustrative exit values:

| Exit Value | Series [Latest] Pref | Series [Earlier] Pref | Common + Options | Total |
|---|---|---|---|---|
| 1× post-money | | | | |
| 2× post-money | | | | |
| 3× post-money | | | | |

Show how liquidation preference stacks and participation caps affect each class.

### Section 6: Notes & Disclaimers

- Methodology disclosure (option pool in/out of FD denominator)
- Anti-dilution mechanics explanation (weighted average formula if applicable)
- Contingencies: board/stockholder/regulatory approval required
- Standard disclaimer: pro forma only, not legal/financial/tax advice, review with counsel

## Guidelines

- Share counts as whole numbers; percentages to two decimal places
- Bold subtotals and grand totals; mark every section "PRO FORMA — CONFIDENTIAL"
- Define terms on first use ("Fully-Diluted Capitalization," "As-Converted Basis") and use consistently
- Flag missing or estimated data with `[ESTIMATED]` or `[TBD]` and explain basis
- Anti-dilution: weighted average is standard; full ratchet is rare — confirm which applies
- Option pool convention: Silicon Valley standard is pre-money inclusion (dilution borne by existing holders); note if post-money convention is used
- Do not provide tax, securities compliance, or accounting treatment analysis
