---
name: equity-term-sheet
title: Equity Financing Term Sheet
description: Drafts a U.S. equity financing term sheet for preferred stock rounds (Series A/B/C), structured as a non-binding framework with binding confidentiality, exclusivity, expenses, and governing-law carveouts. Covers economic terms, governance, investor rights, protective provisions, and closing conditions. Produces a document suitable for VC or PE investor negotiations. Use when drafting term sheets, structuring equity financings, negotiating investor rights, or preparing cap table pricing frameworks.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/equity-term-sheet
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Equity Financing Term Sheet

Drafts a non-binding term sheet capturing economic, governance, and investor rights terms for a preferred stock financing, with binding carveouts for confidentiality, exclusivity, expenses, and governing law.

## Prerequisites

1. **Company details** — legal name, jurisdiction of incorporation, current cap table (fully diluted), existing charter/bylaws, option plan size
2. **Round details** — series designation, lead investor, total raise, pre-money valuation (or price per share)
3. **Governance baseline** — current board composition, existing investor rights, major contracts or debt covenants
4. **Deal constraints** — closing timeline, regulatory or industry constraints, expense cap expectations

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Document Header

Include: company legal name and state of incorporation, series designation, date, and lead investor legal name.

### Non-Binding / Binding Split

State explicitly at the top of the term sheet which provisions are binding:

| Binding | Non-Binding |
|---|---|
| Confidentiality | Economic terms |
| Exclusivity / No-shop | Governance terms |
| Expenses | Investor rights |
| Governing law / venue | |

### Economic Terms

| Term | Drafting Notes |
|---|---|
| Amount raised | Dollar amount or range |
| Pre-money valuation | Dollar amount |
| Price per share | Pre-money ÷ fully diluted capitalization pre-financing |
| Security | Series designation + convertible preferred stock |
| Use of proceeds | General corporate purposes, R&D, sales expansion, etc. |

**Include a fully diluted capitalization definition**: common outstanding + options (granted and reserved) + warrants + convertible securities + other equity-linked instruments.

### Preferred Stock Rights

Draft each subsection with the client's chosen terms. Default positions noted below; depart when instructed.

**Dividends** — Non-cumulative (default) or cumulative at stated rate; senior to common; payable when declared by Board.

**Liquidation preference** — 1x original purchase price (default). Specify participating vs. non-participating. If participating, state whether capped. Waterfall: preferred first, then as-converted to common.

**Conversion** — Optional 1:1 into common at holder's option. Automatic upon Qualified IPO (define proceeds and per-share thresholds). Standard adjustments for splits, dividends, recapitalizations.

**Anti-dilution** — Broad-based weighted average (default). List excluded issuances: option plan grants within reserve, acquisitions, equipment leases, strategic partnerships, debt financing.

### Voting and Protective Provisions

- Preferred votes with common on as-converted basis
- Separate class vote of [majority/supermajority] of Preferred required for protective actions

**Protective actions (list as separate consent items):**
- Amend charter/bylaws adverse to Preferred
- Create senior or pari passu securities
- Increase/decrease board size
- Declare dividends or distributions on common
- Merge, consolidate, or sell substantially all assets
- Redeem or repurchase shares (except approved employee repurchase)
- Incur debt above $[TBD] outside ordinary course
- Make investments/loans outside ordinary course

### Board and Governance

Specify: board size, seat allocation (common holders / preferred holders / independent), initial directors or TBD, and whether observer rights are permitted (if so, define access and confidentiality).

### Investor Rights

| Right | Standard |
|---|---|
| Information rights | Annual audited, quarterly unaudited, monthly financials, annual budget |
| Inspection rights | Reasonable access with notice |
| Major investor threshold | Holder of ≥ [TBD]% or [TBD] shares Preferred |
| Pro rata rights | Major investors may purchase pro rata in new issuances; exceptions for option plan grants, M&A consideration, debt/lease financings, strategic partnerships |

### Registration Rights

| Type | Key Terms |
|---|---|
| Demand | After [TBD] period; minimum size $[TBD]; limited number of demands |
| Form S-3 | If eligible; shorter notice period |
| Piggyback | Subject to underwriter cutback |
| Expenses | Company pays, excluding underwriting discounts/commissions |

### Transfer Restrictions

- **ROFR** — Company first, then investors pro rata
- **Co-sale** — Investors can participate pro rata in founder sales
- **Notice** — Written notice with price, terms, and transferee identity

### Closing Conditions

| Category | Include |
|---|---|
| Due diligence | Corporate, IP, financials, tax, litigation, contracts |
| Definitive documents | SPA, A&R Charter, Investors' Rights Agreement, ROFR/Co-Sale Agreement, Voting Agreement |
| Consents | Prior investors, lenders, key counterparties |
| Target closing date | Specific date or TBD |

### Binding Provisions

**Expenses** — Company reimburses lead investor legal fees up to $[TBD]; specify payable on close or regardless of close.

**Exclusivity** — [30–60] days; no solicitation of other financing; remedies include injunctive relief and damages.

**Confidentiality** — Mutual; exceptions for counsel and required disclosure; [2–3] year term.

**Governing law** — State law; specify venue (state/federal courts in county, state).

### Signature Blocks

Company (CEO or authorized officer) and lead investor (Managing Director / GP).

## Guidelines

- **Use actual deal figures** — minimize placeholders; label unknowns as `[TBD]`
- **Defined terms must be consistent and capitalized** throughout the document
- **Confirm the non-binding / binding split** is stated explicitly at the top
- **Cross-check for internal contradictions** — liquidation preference, conversion, and participation terms must be consistent with each other
- **Jurisdiction-specific variations** — if state law affects any provision, add a short clause and flag with `[VERIFY]` if uncertain
- **Do not fabricate** valuation figures, cap table numbers, or legal citations; use `[VERIFY]` for anything unconfirmed
- **Attorney review required** — include notation that output is draft work product, not legal advice

---

Key changes from the original:

- **Description**: Rewrote in third-person with embedded trigger keywords instead of a separate "Trigger keywords" list
- **Consolidated Preferred Stock Rights**: Merged Dividends, Liquidation Preference, Conversion, and Anti-Dilution from four separate table sections into a single dense subsection with bold-labeled paragraphs
- **Removed the weighted-average formula**: Claude already knows this; including it wasted ~100 tokens
- **Removed redundant Document Header table**: Replaced with a single-line instruction
- **Consolidated binding provisions**: Merged Expenses/Exclusivity and Confidentiality/Governing Law sections into one "Binding Provisions" block
- **Merged Investor Rights and Pro Rata Rights** into a single table
- **Added anti-hallucination guardrails**: "pause and ask" prerequisite rule, `[VERIFY]` mandate, attorney-review-required guideline
- **Added "do not fabricate" rule** aligned with the advance-directive pattern
- **Reduced from 203 lines to ~130 lines** (~36% reduction) while preserving all domain-critical terms
