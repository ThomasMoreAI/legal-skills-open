# Oregon ORS — Debt-Relevant Chapters Corpus

This directory holds verbatim text of the Oregon Revised
Statutes (ORS) chapters most relevant to consumer-debt
defense, civil collection, and general civil practice in
Oregon. The contents are pulled from
**https://www.oregonlegislature.gov/bills_laws/ors/** via the
quarterly `scripts/pull_oregon_ors.py` agent routine.

## Chapters covered

| ORS | Subject | File | Update cycle |
|-----|---------|------|--------------|
| 12 | Limitations of actions | `ORS-12.md` | Quarterly |
| 14 | Jurisdiction; venue | `ORS-14.md` | Quarterly |
| 18 | Judgments; execution; garnishment | `ORS-18.md` | Quarterly |
| 19 | Appeals | `ORS-19.md` | Quarterly |
| 20 | Fees and costs | `ORS-20.md` | Quarterly |
| 21 | Court fees | `ORS-21.md` | Quarterly |
| 36 | Mandatory arbitration | `ORS-36.md` | Quarterly |
| 40 | Evidence Code (OEC) | `ORS-40.md` | Quarterly |
| 71 | UCC Article 1 (general) | `ORS-71.md` | Quarterly |
| 72 | UCC Article 2 (sales) | `ORS-72.md` | Quarterly |
| 73 | UCC Article 3 (negotiable instruments) | `ORS-73.md` | Quarterly |
| 79 | UCC Article 9 (secured transactions) | `ORS-79.md` | Quarterly |
| 82 | Interest; usury | `ORS-82.md` | Quarterly |
| 90 | Residential landlord and tenant | `ORS-90.md` | Quarterly |
| 105 | Property rights; FED | `ORS-105.md` | Quarterly |
| 174 | Construction of statutes | `ORS-174.md` | Quarterly |
| 187 | Holidays | `ORS-187.md` | Quarterly |
| 646 | Trade practices; UTPA | `ORS-646.md` | Quarterly |
| 697 | Collection agencies | `ORS-697.md` | Quarterly |

## Key sections by chapter

### ORS 12 — Limitations

- **ORS 12.080** — 6-year SOL: written contracts, open accounts,
  statutory liabilities
- **ORS 12.110** — 2-year SOL: torts; fraud (from discovery,
  max 10 years repose)
- **ORS 12.140** — 1-year SOL: assault, battery, false
  imprisonment, libel (selected)
- **ORS 12.040** — 10-year SOL: real property

### ORS 18 — Judgments / garnishment

- **ORS 18.182** — 10-year judgment, renewable
- **ORS 18.345–18.385** — Exemptions (homestead, wages, etc.)
- **ORS 18.600–18.850** — Garnishment procedure
- **ORS 18.700** — Writ of execution

### ORS 20 — Fees and costs

- **ORS 20.075** — Factors in fee awards
- **ORS 20.077** — Per-claim fees
- **ORS 20.082** — Small claims fees
- **ORS 20.096** — Reciprocal contract fees
- **ORS 20.105** — Fees against objectively unreasonable position
- **ORS 20.140** — In forma pauperis
- **ORS 20.180** — Costs as taxed
- **ORS 20.190** — Prevailing-party flat fees

### ORS 36 — Mandatory arbitration

- **ORS 36.400** — Authority for mandatory arbitration program
- **ORS 36.405** — Amount-in-controversy ceiling ($50,000)
- **ORS 36.425** — Trial de novo; fee-shifting

### ORS 40 — Evidence Code (OEC parallel)

- **ORS 40.150** = OEC 401 (relevance)
- **ORS 40.450** = OEC 801 (hearsay definition)
- **ORS 40.460** = OEC 803 (hearsay exceptions including
  business records 803(6))
- **ORS 40.505** = OEC 901 (authentication)
- **ORS 40.510** = OEC 902 (self-authentication, including
  902(11) certified business records)
- **ORS 40.555** = OEC 1002 (best evidence)

### ORS 82 — Interest

- **ORS 82.010** — Legal rate (9% per annum unless contract
  specifies)
- **ORS 82.045** — Interest on judgments

### ORS 90 — Landlord-tenant

- **ORS 90.100** — Definitions
- **ORS 90.155** — Service of notices
- **ORS 90.255** — Prevailing-party fees
- **ORS 90.394** — Notice of termination for cause
- **ORS 90.400** — Termination procedures

### ORS 105 — FED (forcible entry & detainer)

- **ORS 105.105–105.168** — FED procedure
- **ORS 105.135** — First Appearance (7 days from service)

### ORS 187 — Legal holidays

- **ORS 187.010** — State legal holidays:
  - New Year's Day
  - Martin Luther King, Jr. Day (3rd Monday of January)
  - Presidents' Day (3rd Monday of February)
  - Memorial Day (last Monday of May)
  - Juneteenth (June 19)
  - Independence Day (July 4)
  - Labor Day (1st Monday of September)
  - Veterans Day (November 11)
  - Thanksgiving Day (4th Thursday of November)
  - Christmas Day (December 25)
- Observed-day rule: Saturday holidays observed Friday; Sunday
  observed Monday (ORS 187.020)

### ORS 646 — UTPA

- **ORS 646.605–646.656** — Unlawful Trade Practices Act
- **ORS 646.607** — Unconscionable tactics list
- **ORS 646.608** — Unlawful trade practices catalog
- **ORS 646.638** — Private right of action
  - (2): Actual damages, $200 minimum, punitive damages
  - (3): Prevailing-party fees mandatory
  - (6): 1-year SOL from discovery; 6-year repose

### ORS 697 — Collection agencies

- **ORS 697.005** — Definitions
- **ORS 697.015** — Registration required to collect debts in
  Oregon
- **ORS 697.058** — Prohibited practices
- **ORS 697.085** — Civil cause of action for violation
- **ORS 697.105** — Records to be kept

## How to re-pull

```bash
python3 scripts/pull_oregon_ors.py \
  --workers 12 \
  --manifest plugins/or-court-docs/skills/or-law-references/references/or-ors-debt/_manifest.json
```

(Script to be created in parallel with the existing WA
`pull_wa_rcw.py`.)

## Status

Empty in the initial PR — only this README and a placeholder
`_manifest.json`. The first re-pull will populate the verbatim
chapter files.

## Cross-references

- `../online-sources.md` — canonical URLs for ORS
- `../legal-data-apis.md` — programmatic access
- `../../or-consumer-debt/` — Oregon consumer-debt subject-
  matter bundle, which relies on this corpus for substantive
  law
