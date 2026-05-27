---
name: ferc-market-based-rate-tariff
title: FERC Market-Based Rate Tariff
description: Drafts eTariff-ready FERC Market-Based Rate Tariffs for wholesale electric energy, capacity, and ancillary services sales. Use when preparing MBR tariff filings, structuring market-based rate authority documentation, or drafting wholesale power tariffs for FERC proceedings. Covers Order Nos. 697/697-A/860, Category 1/2 analysis, 18 CFR Part 35 formatting, and EQR/change-in-status reporting.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ferc-market-based-rate-tariff
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [agreement, drafting]
---

# FERC Market-Based Rate Tariff

Produces a filing-ready tariff authorizing wholesale sales of electric energy, capacity, and ancillary services at market-based rates under FERC jurisdiction.

## Prerequisites

Collect before drafting:

1. **Seller identity** — legal name, state of incorporation, principal place of business
2. **FERC identifiers** — docket number, MBR authorization order date, assigned codes
3. **Category status** — Category 1 or 2 per FERC region (Northeast, Southeast, Southwest, Central, Northwest, California)
4. **Authorization conditions** — MW caps, affiliate restrictions, behavioral/structural remedies, geographic limits
5. **Asset inventory** — generation (capacity, fuel, location), transmission, affiliate holdings
6. **Organized market participation** — ISO/RTO memberships if applicable

## Quick Start

1. Gather all prerequisites and the FERC authorization order
2. Draft sections in order below; populate the regional category matrix early — it drives mitigation and reporting sections
3. Flag all client-specific gaps with `[INSERT]` tags
4. Run the checks in Pitfalls before delivering

## Output Structure

### 1. Preamble
- Seller legal name, organizational details, FERC identifiers
- Docket number, authorization order date; cite Order No. 697 as foundational authority
- Effective date: `[DATE CERTAIN]` or date of FERC acceptance, whichever is later
- Statement of wholesale sales authority acknowledging FERC oversight jurisdiction

### 2. Regulatory Compliance Commitments (18 CFR Part 35)

| Obligation | Trigger | Timeframe |
|---|---|---|
| Maintain category status | Ongoing | Continuous |
| Change-in-status notification | Ownership/asset/affiliate changes | 30 days |
| Horizontal market power screens | Delivered price test + pivotal supplier | Ongoing |
| Vertical market power compliance | Transmission/fuel control concerns | Ongoing |
| Affiliate codes of conduct | Per authorization order | Per Commission order |
| Organized market participation | If required by authorization | Per RTO/ISO tariff |

### 3. Market Power Mitigation & Constraints
- Generation capacity caps by market (MW limits per FERC order)
- Affiliate transaction restrictions (Standards of Conduct)
- Behavioral remedies (price caps) or structural remedies (divestitures) if imposed
- Geographic scope: each authorized balancing authority area, ISO, or RTO by full legal name
- Cross-reference authorization order factual findings supporting each limitation

### 4. Regional Category Status Matrix

| FERC Region | Category | Basis | Special Conditions |
|---|---|---|---|
| Northeast | [1/2] | [Screen results / case-specific] | [If any] |
| Southeast | [1/2] | | |
| Southwest | [1/2] | | |
| Central | [1/2] | | |
| Northwest | [1/2] | | |
| California | [1/2] | | |

- **Category 1** — passed indicative screens; rebuttable presumption of no horizontal market power
- **Category 2** — failed ≥1 screen; requires case-specific showing with enhanced reporting

### 5. Ongoing Reporting Obligations

| Filing | System | Frequency |
|---|---|---|
| Market power analysis update | FERC eFiling | Triennial or within 30 days of material change |
| Electric Quarterly Report | FERC EQR | Within 30 days of quarter end |
| Change-in-status report | FERC eFiling | Within 30 days of triggering event |
| Asset appendix update | FERC eFiling | Upon asset acquisition/disposition |

Triggering events: mergers, acquisitions, reorganizations, affiliate changes, asset transactions affecting market power analysis. Format per 18 CFR § 35.42.

### 6. General Terms and Conditions
- **Rate-setting** — bilateral contracts or FERC-approved organized market; subject to filed rate doctrine
- **Non-discrimination** — consistent with MBR authority
- **Dispute resolution** — FERC complaint procedures (18 CFR Part 206); contractual arbitration where consistent with Commission jurisdiction
- **Force majeure** — notice and mitigation obligations
- **Creditworthiness** — collateral requirements on purchasers
- **Termination/amendment** — tariff amendments via FERC eFiling

### 7. Certification and Filing Authorization

Include authorized officer certification block:
- Officer name, title, seller legal name
- Certifications: (1) authority to file, (2) truth/completeness, (3) acceptance of FERC jurisdiction, (4) compliance commitment
- Signature block with date, phone, email
- Attorney/authorized representative eFiling certification with bar number

## Formatting Requirements

- Hierarchical section numbering (1.0, 1.1, 1.1.1)
- Seller name and tariff designation in headers/footers on every page
- Complete citations using Bluebook or FERC conventions
- Target length: 12–25 pages

## Pitfalls

- **Category 2 sellers**: must include case-specific market power showing; flag enhanced reporting prominently throughout
- **Jurisdictional limits**: no provision may restrict FERC regulatory authority or create barriers to competitive market entry
- **Placeholder audit**: deliver with cover memo identifying every `[INSERT]` tag and unusual conditions
- **Verify before filing**: Order No. 697 (2007), Order No. 697-A (2008), Order No. 860 (2019) — confirm current amendment status; verify 18 CFR § 35.42 text and check for intervening Commission orders
