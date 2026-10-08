---
name: basel31-openafterhours
title: Basel 3.1 — PRA PS1/26 Regulatory Reference
description: Look up Basel 3.1 / PRA PS1/26 credit risk rules. Use when you need new SA risk weights (including RE loan-splitting, ECRA/SCRA, corporate sub-categories), IRB parameter floors, output floor mechanics, CCF changes, CRM method changes, slotting updates, or any difference between CRR and Basel 3.1. Effective 1 Jan 2027.
author: OpenAfterHours
author_url: https://github.com/OpenAfterHours/rwa_calculator/tree/master/.agents/skills/basel31
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: corporate
language: en
sources:
- title: Credit Conversion Factors
  path: references/credit-conversion-factors.md
- title: Crm Changes
  path: references/crm-changes.md
- title: Irb Changes
  path: references/irb-changes.md
- title: Output Floor
  path: references/output-floor.md
- title: Reporting Changes
  path: references/reporting-changes.md
- title: Reporting Validation Rules
  path: references/reporting-validation-rules.md
- title: Sa Risk Weights
  path: references/sa-risk-weights.md
- title: Slotting Changes
  path: references/slotting-changes.md
- title: What Changed
  path: references/what-changed.md
---

# Basel 3.1 — PRA PS1/26 Regulatory Reference

Basel 3.1 as implemented by PRA PS1/26 for UK firms, effective 1 January 2027. The
framework shifts emphasis from risk sensitivity to comparability and floors.

## Where the numbers live

**This skill does not state regulatory values.** Every value tables in the reference
files below is generated from the rulepack
(`src/rwa_calc/rulebook/packs/{common,crr,b31}.py`) by
`uv run python scripts/generate_regulatory_tables.py`, and
`scripts/check_skill_values.py` fails the build if a value is reintroduced as prose.

This is a graduated lesson, not a style preference: hand-maintained copies of pack
values drifted three times in this repo — the corporate CQS5 Basel 3.1 risk weight was
stated here as 100% in three separate files while the pack, the engine and PS1/26
Art. 122(2) Table 6 all said 150%.

So, when you need a number:

1. **Read the generated table** in the relevant reference file below — each
   `### entry_name` heading is the literal pack key, with its citation.
2. **Or grep the pack directly**: `rg 'b31_corporate_risk_weights' src/rwa_calc/rulebook/packs/`.
3. **Or read the whole rendered pack**: `docs/data-model/regulatory-tables.md`.

Do **not** try to extract values from the source PDFs for routine lookups. Most agents
cannot read `docs/assets/*.pdf` at all, and PS1/26 renumbers articles — the
`[Note: corresponds to Article NNN]` line, not the printed number, tells you which CRR
article a PS1/26 article maps to. Use the PDFs to *audit* a pack value you have reason to
doubt, and when you do, fix the **pack**.

## What changed from CRR — qualitatively

The magnitude of each change lives in the generated tables; the shape of it is here.

1. **Output floor** — IRB RWA floored against an SA recalculation of the whole portfolio
2. **Supporting factors removed** — no SME or infrastructure relief
3. **IRB scaling factor removed** — a uniform reduction in IRB RWA before the floor
4. **PD floors differentiated** — class-specific, where CRR used one uniform floor
5. **A-IRB LGD floors introduced** — by collateral type; CRR had none
6. **F-IRB supervisory LGD reduced** — for senior non-FI corporates and secured positions
7. **A-IRB restricted** — large corporates, FIs and institutions become F-IRB only
8. **Equity IRB removed** — SA only, with a transitional phase-in
9. **Real estate becomes a standalone class** — PRA loan-splitting, *not* the BCBS
   whole-loan table
10. **New retail sub-categories** — transactor and payroll/pension

## Quick Navigation

| Question | Reference File |
|----------|---------------|
| What changed overall? (generated divergence table) | [references/what-changed.md](references/what-changed.md) |
| What are the Basel 3.1 SA risk weights? | [references/sa-risk-weights.md](references/sa-risk-weights.md) |
| What are the new IRB floors and restrictions? | [references/irb-changes.md](references/irb-changes.md) |
| How does the output floor work? | [references/output-floor.md](references/output-floor.md) |
| What are the new CCF values? | [references/credit-conversion-factors.md](references/credit-conversion-factors.md) |
| What changed in CRM (haircuts, methods)? | [references/crm-changes.md](references/crm-changes.md) |
| What changed in slotting risk weights? | [references/slotting-changes.md](references/slotting-changes.md) |
| What changed in reporting templates? | [references/reporting-changes.md](references/reporting-changes.md) |
| What must my OF template tie out to? (BoE validation rules) | [references/reporting-validation-rules.md](references/reporting-validation-rules.md) |

## External Regulatory Sources

- **PRA PS1/26:** https://www.bankofengland.co.uk/prudential-regulation/publication/2026/january/implementation-of-the-basel-3-1-final-rules-policy-statement
- **PRA PS1/26 Appendix 1 (full rules):** https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/policy-statement/2026/january/ps126app1.pdf
- **BCBS CRE Standards:** https://www.bis.org/basel_framework/standard/CRE.htm
- **Source PDFs:** `docs/assets/ps126app1.pdf` (full rules), `docs/assets/comparison-of-the-final-rules.pdf` (delta summary) — for auditing a suspect pack value, not for routine lookup
- **BoE regulatory reporting (banking sector):** https://www.bankofengland.co.uk/prudential-regulation/regulatory-reporting/regulatory-reporting-banking-sector
- **BoE banking XBRL taxonomy validations v4.0.0:** https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/regulatory-reporting/banking/2026/february/boebankingtaxonomyvalidationsv400.zip — raw at `docs/assets/boe-banking-taxonomy-validations-v4.0.0.zip` (gitignored; `uv run python scripts/download_docs.py`), extract at `src/rwa_calc/reporting/validations/rules/basel31-boe-v4.0.0-credit-risk.json`

## Project Specification & Comparison Files

| File | Topic |
|------|-------|
| `docs/data-model/regulatory-tables.md` | **Every cited pack value, both regimes** (generated) |
| `docs/framework-comparison/key-differences.md` | Comprehensive CRR vs Basel 3.1 comparison |
| `docs/framework-comparison/technical-reference.md` | Developer-facing parameter tables, haircuts, config |
| `docs/framework-comparison/impact-analysis.md` | Capital impact by portfolio type |
| `docs/framework-comparison/reporting-differences.md` | COREP template changes (C -> OF) |
| `docs/framework-comparison/disclosure-differences.md` | Pillar 3 template changes (UK -> UKB) |
| `docs/specifications/crr/sa-risk-weights.md` | SA risk weights (covers both CRR + Basel 3.1) |
| `docs/specifications/crr/airb-calculation.md` | A-IRB with Basel 3.1 LGD floors and PMAs |

## Key Regulatory Sections

| PRA PS1/26 Article | BCBS Section | Topic |
|--------------------|--------------|-------|
| Art. 92(5) | — | Output floor formula |
| Art. 111, Table A1 | CRE20.92 | SA CCFs |
| Art. 112, Table A2 | CRE20.4 | Exposure class priority waterfall |
| Art. 114-121 | CRE20.7-21 | Sovereign, institution ECRA/SCRA |
| Art. 122, 122A-122B | CRE20.42-49 | Corporate + SA specialised lending |
| Art. 123B | — | Currency mismatch multiplier (no CRR equivalent) |
| Art. 124A-124L | CRE20.71-85 | Real estate loan-splitting, LTV tables |
| Art. 127 | CRE20.87-90 | Defaulted exposures |
| Art. 133 | CRE20.52-57 | Equity |
| Art. 146(3) | — | Post-model adjustments (PMAs) |
| Art. 147A | CRE30 | IRB approach restrictions |
| Art. 153, 154 | CRE31-32 | IRB K formula, correlation, LGD floors |
| Art. 161, 162 | CRE32.12-24 | F-IRB supervisory LGD, maturity |
| Art. 163(1) | CRE30.55 | Differentiated PD floors |
| Art. 166C-166D | CRE32.25-27 | F-IRB/A-IRB CCFs |
| Art. 191A | CRE22 | CRM method decision tree |

## Basel 3.1 Exposure Class Waterfall (Art. 112, Table A2)

Priority ordering — the highest-priority class applies where an exposure meets several
criteria:

1. Securitisation positions
2. CIU units/shares
3. Subordinated debt, equity and own funds instruments
4. Items associated with particularly high risk
5. Exposures in default
6. Eligible covered bonds
7. **Real estate exposures** (new standalone class)
8. International organisations
9. Multilateral development banks
10. Institutions
11. Central governments / central banks
12. Regional governments / local authorities
13. Public sector entities
14. Retail exposures
15. Specialised lending (new)
16. Corporates
17. Other items

## Transitional Schedules

Both phase-in schedules are pack `Schedule` entries, rendered in the reference files:

- **Output floor** (Art. 92(5)) — `output_floor_pct`, see
  [references/output-floor.md](references/output-floor.md)
- **Equity SA** (Art. 4.2/4.3) — `equity_transitional_std_rw` and
  `equity_transitional_hr_rw`, see the CRR skill's
  [slotting-and-equity.md](../crr/references/slotting-and-equity.md)

IRB transitional (Art. 4.4-4.6): firms with IRB permission use the **higher of** the old
IRB methodology and the transitional SA schedule. An irrevocable opt-out is available.
