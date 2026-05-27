---
name: lpa-agreement
title: Limited Partnership Agreement (LPA)
description: Drafts institutional-quality Limited Partnership Agreements for PE/VC fund formation. Covers GP/LP terms, capital commitments, distribution waterfall, carried interest, LPAC governance, clawback, and tax provisions. Use when drafting LPA, fund formation agreement, limited partnership terms, or PE/VC fund documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/lpa-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Limited Partnership Agreement (LPA)

Drafts a formal "Amended and Restated Agreement of Limited Partnership" governing the GP/LP relationship across a fund's full lifecycle.

## Prerequisites

Gather before drafting — prompt the user for any missing items:

- Fund name, jurisdiction, target size, investment strategy
- Management fee rate/basis, carry %, preferred return %, waterfall type (deal-by-deal vs. whole-fund)
- Key persons triggering key person provisions
- Term sheet or PPM (if available)
- Side letter commitments, co-investment arrangements
- Governing law (state RULPA)

## Quick Start

Draft with table of contents and consistent defined-term capitalization. Follow this article structure:

| Art. | Subject | Key Contents |
|------|---------|-------------|
| I | Formation & Purpose | Statutory authority, registered agent, purpose clause, investment thesis limitations |
| II | Definitions | Capitalized terms, alphabetical |
| III | Term | Initial term from final closing, investment period (~5 yrs), extension mechanism (2 x 1-yr, LPAC/LP approval) |
| IV | Capital Commitments | Subscription Agreements, pro rata capital calls, 10-30 day notice, default remedies |
| V | Allocations & Distributions | IRC 704(b) allocations, four-tier waterfall, tax distributions |
| VI | Management & Governance | GP authority, key person provisions, management fee, fee offsets, LPAC |
| VII | GP Obligations & LP Protections | Clawback, LP liability cap, fiduciary standards |
| VIII | Transfer Restrictions | Consent, permitted transfers (affiliates, estate vehicles), transferee conditions |
| IX | Tax Provisions | Pass-through status, K-1 delivery, 754 election, BBA audit regime, withholding |
| X | Dissolution & Liquidation | Triggering events, wind-up, final accounting, 90-day LP objection period |
| XI | General Provisions | Amendments, notices, confidentiality, governing law, severability |

## Core Economic Terms

### Distribution Waterfall

```
Tier 1 — Return of Capital: 100% to LPs until distributions = contributed capital
Tier 2 — Preferred Return: 100% to LPs until [8]% IRR (specify compounding)
Tier 3 — GP Catch-Up: 100% to GP until GP has [carry %] of Tiers 2+3
Tier 4 — Carried Interest Split: [80]% LPs / [20]% GP
```

- Specify deal-by-deal (add interim clawback + escrow) or whole-fund
- Address distribution timing (mandatory vs. discretionary) and reserve authority

### Management Fee

```
Investment Period: [2]% x commitments, quarterly in advance
Post-Investment: [2]% x [cost basis / FMV] of remaining investments
Adjustments: prorate for final closing; suspend during key person event
Fee Offset: [50-100]% of transaction/monitoring/directors' fees
```

### Default Remedies

Include: default interest, pro rata commitment reduction, capital forfeiture, forced sale at discount to FMV, cure period with notice requirements.

### Clawback

- GP returns excess carry so LPs receive capital + preferred return first
- Calculate on after-tax basis (gross-up for taxes on returned carry)
- Secure with escrow holdback (institutional) or personal guaranty with net worth covenant (emerging managers)

## LPAC Checklist

- [ ] Composition: [3-7] reps elected by majority of commitments
- [ ] Term, removal, replacement procedures
- [ ] Meeting frequency (minimum quarterly)
- [ ] Advisory-only except where consent required
- [ ] Consent matters: GP co-investments, affiliate/related-party transactions, material amendments, valuation changes, auditor removal, term extensions

## Tax and Regulatory

| Item | Detail |
|------|--------|
| Classification | Partnership pass-through |
| K-1 delivery | March 15 (calendar-year) |
| 754 election | GP discretion |
| BBA audit | Designate partnership rep; push-out election rights |
| Investor quals | Accredited (Reg D) and/or qualified purchaser (ICA 3(c)(7)) |
| AML/KYC | BSA/CIP compliance, beneficial ownership verification |
| Withholding | GP authorized; charge to partner's account |

## Pitfalls and Checks

1. **Cite specific RULPA** — e.g., Delaware RULPA, 6 Del. C. 17-101 et seq. [VERIFY for chosen jurisdiction]
2. **Cross-references** — verify all internal section references before finalizing
3. **ILPA compliance** — flag deviations from ILPA Principles v3.0 as non-standard
4. **Side letters** — note where MFN provisions override base LPA terms
5. **ERISA** — if benefit plan investors possible, include compliance provisions and 25% threshold analysis
6. **Securities law** — include unregistered securities legends referencing Securities Act 4(a)(2) and Reg D
7. **Ask, don't assume** — prompt user for unspecified investment period, preferred return, carry %, or waterfall structure
8. **No tax advice** — include disclaimer that LPs should consult their own tax advisors
