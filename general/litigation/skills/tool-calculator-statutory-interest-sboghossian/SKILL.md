---
name: tool-calculator-statutory-interest-sboghossian
title: Tool — Statutory Interest Calculator
description: Use when computing statutory or contractual interest on overdue payments, debt claims, or court-awarded sums across MENA and European jurisdictions. Covers Lebanon (Art 766 OCC), UAE (Federal Law 18/1993, 9%/12%), KSA (Sharia-compliant profit-margin approach), France (arrêté bi-annual rate), UK (Late Payment Act 1998, base+8%), and EU (Directive 2011/7/EU). Returns principal, period, rate, computation method, total interest, and jurisdiction-specific warnings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-calculator-statutory-interest
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Tool — Statutory Interest Calculator

## What it does

Computes statutory or contractual interest on overdue amounts — from debt claims and commercial invoices to court-awarded damages — across six major jurisdictions. Returns full computation with the applicable rate, day-count convention, and jurisdiction-specific warnings about enforceability.

## Inputs

| Field | Type | Required | Notes |
|---|---|---|---|
| `principal` | number | Yes | Amount in dispute or overdue |
| `currency` | string | Yes | ISO 4217 currency code |
| `fromDate` | ISO date | Yes | Start of interest accrual (service of notice, due date, or judgment date) |
| `toDate` | ISO date | Yes | End of accrual period (today, payment date, or anticipated judgment) |
| `jurisdiction` | enum | Yes | `LB`, `UAE`, `KSA`, `FR`, `UK`, `EU` |
| `rateOverride` | number | No | Contractually agreed rate (% p.a.) — overrides statutory default |
| `compounding` | enum | No | `simple` (default), `annual`, `monthly` |
| `dayCountConvention` | enum | No | `365` (default for most), `360`, `actual_actual` |
| `claimType` | enum | No | `civil` or `commercial` — affects UAE rate selection |

## Statutory defaults by jurisdiction

**Rates change. Always verify current rate before use in a court filing.**

### Lebanon

- **Governing law:** Article 766 of the Lebanese Code of Obligations and Contracts (OCC), as amended.
- **Statutory rate:** Published periodically; the civil rate and commercial rate may differ. Usury limits apply (interest cannot exceed a legally capped ceiling).
- **Compounding:** Simple interest is the default; compound interest requires express contractual agreement.
- **Currency:** Pre-2019 LBP claims require expert determination on conversion rate — see [[tool-currency-converter]].

---

### UAE Federal

- **Governing law:** Federal Law No. 18/1993 (Commercial Code) and Cabinet Decisions.
- **Civil matters:** 9% per annum (commonly applied default).
- **Commercial matters:** 12% per annum (commercial transactions between traders).
- **Cap:** Courts may reduce if the agreed rate is deemed excessively onerous.
- **Day count:** 365 days.
- **DIFC/ADGM:** These courts apply their own interest rules under DIFC Contract Law and ADGM Contract Regulations; statutory rate above does not apply. Check applicable DIFC/ADGM legislation.

---

### KSA (Sharia constraint — critical)

- **Sharia position:** Classical Islamic finance prohibits riba (interest). Saudi courts historically declined to award interest as a standalone remedy.
- **Current practice:** Saudi courts may award compensation for late payment structured as a "profit margin" or damages for delay, but not as classical interest accrual.
- **Contractual practice:** International contracts involving KSA parties frequently include a governing-law clause choosing English or DIFC law precisely to allow interest awards; Saudi courts may not enforce such clauses.
- **Warning:** **Do NOT** present an interest computation as enforceable in KSA courts without specialist local-law advice. Flag this constraint explicitly in every KSA output.
- **SAMA-regulated entities:** Saudi Central Bank (SAMA) regulated contracts (banking, lending) operate under different rules; interest is effectively recharacterised as financing fees.

---

### France

- **Governing law:** French Civil Code (Code civil) — legal interest rate set by arrêté published twice a year (January and July).
- **Commercial late payment:** Law No. 92-1442 and EU Directive 2011/7/EU transposed — minimum 3× ECB rate or ECB + 10 percentage points for commercial debts.
- **Compounding:** Anatocisme (compound interest) permitted only by court order or for periods of at least one year with express agreement.
- **Day count:** 365 days.

---

### UK

- **Governing law:** Late Payment of Commercial Debts (Interest) Act 1998 (as amended by Late Payment of Commercial Debts Regulations 2002 implementing EU Directive 2000/35/EC).
- **Rate:** Bank of England base rate + **8 percentage points** per annum (for qualifying commercial debts between businesses).
- **Day count:** 365 days.
- **Court award:** Section 69 Senior Courts Act 1981 gives courts discretion to award interest; commonly awarded at the statutory rate or at the rate applicable to the underlying obligation.
- **Personal injury:** Special rules under Part 36 and court practice directions.

---

### EU (Directive 2011/7/EU on Late Payments)

- **Rate:** ECB main refinancing rate + **8 percentage points** minimum (for commercial transactions — business to business or business to public authority).
- **ECB rate:** Published bi-annually; verify current rate.
- **Due date:** Interest accrues automatically after 30 days (60 days for public authorities) without the need for a reminder.
- **Member state implementation:** Each EU state may apply rates higher than the directive minimum; verify for France (see above), Germany, Netherlands, etc.

## Output schema

```json
{
  "jurisdiction": "UAE",
  "claimType": "commercial",
  "principal": 500000,
  "currency": "AED",
  "fromDate": "2024-01-01",
  "toDate": "2026-05-14",
  "rateApplied": 12.0,
  "rateType": "statutory_commercial",
  "dayCountConvention": "365",
  "compounding": "simple",
  "computation": {
    "days": 864,
    "years": 2.367,
    "interest": 142,027.40
  },
  "totalDue": 642027.40,
  "warnings": [
    "Rate verified as of May 2026 — confirm current Cabinet Decision before court use",
    "DIFC/ADGM matters: apply DIFC Contract Law rate, not UAE Federal rate"
  ]
}
```

## Critical warnings by jurisdiction

| Jurisdiction | Warning |
|---|---|
| KSA | Do not present as enforceable interest award; flag Sharia constraint; recommend English/DIFC governing law for cross-border recovery |
| LB (pre-2019 LBP) | Pin FX rate; currency ambiguity may need expert evidence |
| UAE (DIFC/ADGM) | Apply DIFC/ADGM-specific rules, not UAE Federal 18/1993 |
| All | Rates change — always verify against current primary source before court filing |

## Related skills

- [[tool-calculator-end-of-service-gratuity]]
- [[tool-currency-converter]]
- [[pa-workflow-litigation]]
- [[draft-demand-letter]]
