---
name: restated-certificate
title: Amended and Restated Certificate of Incorporation
description: Drafts an Amended and Restated Certificate of Incorporation for Delaware corporations in preferred stock financing rounds. Covers authorized capital, preferred stock rights (dividends, liquidation, conversion, anti-dilution), protective provisions, and DGCL compliance. Use when drafting charter documents, restated certificates, venture financing corporate documents, or Delaware certificate amendments from term sheets and cap tables.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/restated-certificate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Amended and Restated Certificate of Incorporation

Drafts a filing-ready Amended and Restated Certificate of Incorporation for a Delaware corporation in connection with a preferred stock financing round. Delaware-specific — do not apply to other states without modification.

## Prerequisites

Collect before drafting:

1. **Term sheet** — pricing, liquidation preference multiple, anti-dilution method, protective provisions, board composition
2. **Prior Certificate** — current authorized capital, existing preferred series, unusual provisions
3. **Cap table** — shares outstanding, option pool, warrants, convertible notes
4. **Transaction documents** — SPA, IRA, voting agreement, ROFR/co-sale (for cross-reference)
5. **Registered agent** — name, physical Delaware street address (no P.O. boxes), county

## Quick Start

1. Gather all prerequisites above
2. Run pre-draft verification (cross-check term sheet against cap table and SPA)
3. Draft articles I–VII using the document skeleton
4. Verify anti-dilution formula and liquidation waterfall with sample numbers
5. Cross-check all defined terms against transaction documents
6. Confirm filing readiness with Delaware Secretary of State requirements

## Pre-Draft Verification

Extract and cross-check — flag discrepancies before drafting:

| Data Point | Source | Verify Against |
|---|---|---|
| Pre/post-money valuation | Term sheet | Cap table |
| Price per share | Term sheet | SPA, cap table math |
| Shares issued this round | Term sheet | SPA |
| Total authorized Common | Cap table | Outstanding + pool + all conversions + cushion |
| Total authorized Preferred (per series) | Term sheet | Shares issued + warrant/note conversions + anti-dilution cushion |
| Option pool size | Term sheet | Board resolutions, cap table |
| Liquidation preference multiple | Term sheet | SPA |
| Dividend rate and type | Term sheet | — |
| Anti-dilution method | Term sheet | — |
| Board composition | Term sheet | Voting agreement |

## Document Skeleton

```
AMENDED AND RESTATED CERTIFICATE OF INCORPORATION
OF [EXACT LEGAL NAME]

[Corporation] hereby certifies:

1. Original Certificate filed with the Delaware Secretary of State on [DATE].
2. This Amended and Restated Certificate has been duly adopted pursuant to
   Sections 242 and 245 of the DGCL [by board consent under §245 / by board
   and stockholder approval under §242].
3. The text of the Certificate is hereby amended and restated in its entirety
   as follows:

ARTICLE I — NAME
ARTICLE II — REGISTERED OFFICE AND AGENT
ARTICLE III — PURPOSE
ARTICLE IV — AUTHORIZED CAPITAL
ARTICLE V — PREFERRED STOCK RIGHTS
ARTICLE VI — DIRECTOR EXCULPATION
ARTICLE VII — [Additional governance as needed]

IN WITNESS WHEREOF...
[Signature block: name, title, date]
```

## Core Articles

**Article I — Name.** Must include corporate designator (Corp., Inc., etc.) per DGCL §102(a)(1). Must match across all transaction documents exactly.

**Article II — Registered Office.** Physical street address in Delaware with county. Named registered agent who has consented to serve.

**Article III — Purpose.** Standard broad clause: "any lawful act or activity for which corporations may be organized under the DGCL." Narrow only if regulatory/tax reasons require.

**Article IV — Authorized Capital.**

```
Total authorized: [X] shares
  Common Stock: [X] shares, $[0.0001] par value
  Preferred Stock: [X] shares, $[0.0001] par value
    Series Seed: [X] shares
    Series A: [X] shares
    Undesignated: [X] shares (blank check authority)
```

Common must cover: outstanding + option pool + all preferred as-converted + warrants/notes + cushion.

**Article V — Preferred Stock Rights.** Draft in this order:

| Section | Key Decisions |
|---|---|
| Dividends | Cumulative vs. non-cumulative; rate; when-as-if-declared vs. auto-accruing; series priority |
| Liquidation Preference | Preference amount (OIP × multiple + accrued dividends); pari passu vs. senior; participating vs. non-participating; cap |
| Optional Conversion | Ratio = OIP ÷ Conversion Price; initial CP = OIP; no fractional shares |
| Mandatory Conversion | Qualified IPO trigger (min proceeds + min price); majority/supermajority Preferred vote |
| Anti-Dilution | Broad-based weighted average; enumerate carve-outs |
| Voting Rights | As-converted with Common; separate class vote for protective provisions |
| Protective Provisions | Majority/supermajority Preferred consent for enumerated actions |
| Board Designation | Seats for Common, each Preferred series, independent/mutual |

See `references/DETAILS.md` for anti-dilution formula, carve-out checklist, protective provisions checklist, and liquidation waterfalls.

**Article VI — Director Exculpation.** DGCL §102(b)(7) maximum exculpation with statutory carve-outs (loyalty breach, bad faith, §174, improper personal benefit). Include future-amendment auto-update clause.

**Article VII+ — Optional Provisions.** Indemnification + mandatory advancement; D&O insurance authority; corporate opportunity waiver; forum selection (Court of Chancery); written consent/special meeting provisions.

## Pitfalls and Checks

1. **Defined terms** — define once, use consistently; cross-check against SPA/IRA/voting agreement definitions
2. **Mathematical verification** — test liquidation waterfall at multiple exit values; verify anti-dilution formula with sample down-round
3. **Cross-references** — verify all internal section references and subsection numbering
4. **DGCL compliance** — cite §§242, 245 in recitals; §102(a)(1) for name; §102(b)(7) for exculpation; §151 for stock rights
5. **Blank check preferred** — if authorized, ensure protective provisions cover future series designation
6. **Par value consistency** — match across Common and Preferred unless justified
7. **Filing readiness** — document must be executable and fileable as-is
8. **Never guess** share numbers, valuations, or pricing — flag gaps and request clarification
