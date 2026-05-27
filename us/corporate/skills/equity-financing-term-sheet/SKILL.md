---
name: equity-financing-term-sheet
title: Equity Financing Term Sheet
description: 'Drafts a U.S. venture equity term sheet from deal facts into a negotiation-ready, investor-grade document. Use when counsel or founders need a structured term sheet covering pricing, capitalization, liquidation preferences, anti-dilution, governance, investor protections, transfer/registration rights, and closing mechanics. Trigger: term sheet, equity financing, venture capital, series preferred, pre-money valuation, liquidation preference, pro rata, ROFR, co-sale, registration rights.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/equity-financing-term-sheet
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Equity Financing Term Sheet

Produces a complete US venture equity term sheet with minimal placeholders and consistency controls for follow-on definitive agreements. Assumes US corporate law (typically Delaware) unless stated otherwise.

## Quick Start

Gather before drafting:

1. Company legal name and incorporation jurisdiction
2. Round metadata — series name, lead investor, raise amount, valuation inputs
3. Pre-financing cap table — common, preferred, options, warrants, convertibles, reserved pool
4. Governance baseline — board size, nominee rights, voting structure
5. Commercial boundaries — liquidation preference cap, anti-dilution type, board control limits
6. Existing charter, bylaws, and prior financing agreements

Mark anything unavailable as `{{PLACEHOLDER: field name}}`.

## Core Workflow

### 1. Intake Validation

Map each input to its output section and flag gaps:

| Input | Drives | If Missing |
|---|---|---|
| Company / jurisdiction | Header, governing law | `{{PLACEHOLDER}}` |
| Valuation / share price | Economics, ownership math | Flag — draft incomplete |
| Cap table | Dilution impact, conversion basis | Generate skeleton with placeholders |
| Rights matrix | Governance, protections | Insert defaults, mark for review |
| Closing preconditions | Conditions precedent, definitive docs list | List required docs by name |

### 2. Draft (Hard Section Order)

1. Header — non-binding notice, date, parties, round summary
2. Definitions — Binding Provisions, Major Investor, Fully Diluted Capitalization, Registrable Securities, Qualified IPO
3. Economics — security type, OIP, pre/post FD basis, price per share formula
4. Preferred stock rights — dividends, liquidation preference, conversion, anti-dilution
5. Governance — board allocation, observer rights, protective provisions
6. Investor rights — information, inspection, registration (demand/piggyback)
7. Transfer and liquidity — ROFR, co-sale, pro-rata, exceptions
8. Closing mechanics — diligence, required agreements, conditions, timeline
9. Binding provisions — confidentiality, exclusivity, expense reimbursement, governing law, forum
10. Signature block

### 3. Validation Pass

- [ ] Every defined term used consistently across clauses and tables
- [ ] All numeric variables resolve or carry explicit `{{PLACEHOLDER}}`
- [ ] Binding vs non-binding sections clearly separated under distinct headings
- [ ] Each economic right cross-referenced to its governance and transfer effects

## Key Formulas

```
Price Per Share = Pre-Money Valuation / Pre-Money Fully Diluted Shares

Ownership % (post-close) = Shares Held / Total Post-Financing FD Shares
```

**Liquidation preference:**
- Non-participating — greater of preference or as-converted value
- Participating — preference + pro-rata on residuals (state cap if any)

**Weighted-average anti-dilution:**
```
Adjusted CP = Old CP × (A + B) / (A + C)
  A = FD shares pre-issuance (broad or narrow basis)
  B = consideration received / Old CP
  C = new shares issued at lower price
```

## Mandatory Clauses Checklist

| Category | Minimum Content |
|---|---|
| Deal Identity | Date, parties, round, amount, currency, pre-money basis |
| Economics | Valuation inputs, conversion ratio, price-per-share formula |
| Preferences | Dividends, liquidation preference, conversion trigger, anti-dilution |
| Governance | Board allocation, observer terms, protective provisions |
| Investor Rights | Information, inspection, registration demand/piggyback |
| Liquidity Controls | ROFR, co-sale, pro-rata, exceptions |
| Closing | Diligence standards, required agreements, conditions, timeline |
| Enforceability | Binding carve-out, non-binding statement, survival, governing law |

## Assembly Rules

- Isolate binding clauses (confidentiality, exclusivity, expenses, law/forum) in their own section.
- Use exact thresholds — specific day-counts and percentage figures, not approximations.
- Reference each protection in both its definition and operative clause.
- Include closing conditions and list required definitive documents by name.
- Add termination-and-survival paragraph aligned to transaction stage.
- Attach exhibit placeholders for cap table and schedule of rights.

## Pitfalls

- **Mixed anti-dilution bases** — never combine broad-based and narrow-based results without explicit branch language.
- **Incomplete economics** — every unresolved economic field must carry a `{{PLACEHOLDER}}` marker; never present partial math as final.
- **Prose-only math** — always provide formulas alongside any valuation or ownership narrative.
- **Registration promises** — never state filing timelines or outcomes without `[VERIFY]` flag for counsel confirmation.
- **Non-US assumptions** — default to US law; do not imply foreign corporate law applies unless specified.
- **Securities compliance** — flag Rule 144 / resale language and federal securities implications with `[VERIFY]` before release.
- **Confidentiality carve-outs** — ensure survival terms are compatible with legal and advisor carve-out requirements.

**Key changes from original:** Removed `tags` (not in spec), trimmed 10-item prerequisites into 6-item Quick Start, collapsed the verbose intake table and templates into streamlined workflow steps, merged Do/Don't/Jurisdiction sections into a single Pitfalls list, eliminated redundant template blocks (the section order itself serves as the template), and preserved all domain-critical formulas and clause requirements. Reduced from 160 lines to ~100 while retaining full legal coverage.
