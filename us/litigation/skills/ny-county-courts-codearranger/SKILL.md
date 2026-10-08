---
name: ny-county-courts-codearranger
title: New York County Courts — Long-tail Roll-up
description: 'Use when filing in a New York **Supreme Court** Civil Term other than the five flagship counties (New York, Kings, Bronx, Nassau, Queens). Triggers include ''Suffolk County Supreme Court'', ''Westchester County Supreme Court'', ''Erie County Supreme Court'', ''Monroe County Supreme Court'', ''Onondaga Supreme'', ''Richmond County Supreme Court'' (Staten Island). Now narrowly scoped to **Supreme Court Civil Term** only — the long-tail roll-up of upstate Supreme Courts plus Richmond. For other civil-court layers use dedicated skills: `ny-nyc-civil-court` (NYC Civil Court $50k cap), `ny-nyc-housing-court` (RPAPL Art 7 summary proceedings), `ny-nassau-dc` / `ny-suffolk-dc` (Long Island UDCA District Courts $15k cap), `ny-city-courts` (upstate UCCA City Courts $15k cap), `ny-justice-courts` (Town & Village UJCA Justice Courts $3k cap).'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York County Courts — Long-tail Roll-up

> **NOT LEGAL ADVICE.** Verify the specific court's local
> rules before filing.

This skill is the **Supreme Court Civil Term roll-up** for
counties outside the five flagship venues (`ny-nyco`,
`ny-kings`, `ny-bronx`, `ny-nassau`, `ny-queens`). Other
NY civil-court layers each have their own dedicated skill —
see the [Other civil-court layers](#other-civil-court-layers)
section below to route to the right one.

## Supreme Court (other counties)

The Supreme Court is New York's court of general
jurisdiction in every county. Beyond the five flagship
counties, the next-largest civil-trial venues:

| County | JD | Courthouse | Comm Div threshold |
|--------|----|----|----------------|
| Suffolk | 10th | Riverhead | $100,000 |
| Westchester | 9th | White Plains | $200,000 |
| Richmond (Staten Island) | 2nd (admin); separate filing | St. George Courthouse | $150,000 |
| Erie | 8th | Buffalo | $100,000 |
| Monroe | 7th | Rochester | $50,000 |
| Onondaga | 5th | Syracuse | $50,000 |
| Rockland | 9th | New City | $100,000 |
| Albany | 3rd | Albany | $50,000 |
| Orange | 9th | Goshen | $100,000 |
| Dutchess | 9th | Poughkeepsie | (no Comm Div) |
| Saratoga | 3rd | Ballston Spa | $50,000 |
| Oneida | 5th | Utica | (no Comm Div) |

Filings use NYSCEF in nearly all counties. Confirm the
assigned Justice's Part Rules before motion practice.
**Individual Assignment System** under 22 NYCRR § 202.3
applies — case stays with one Justice from RJI through
judgment.

For Commercial Division-eligible matters (see the
threshold table above), use `ny-commercial-disputes` for
the substantive 22 NYCRR § 202.70 rule overlay.

## Other civil-court layers

NY has an unusually fragmented trial-court system — far
more layers than most states. **This skill no longer covers
the non-Supreme-Court layers**. Each layer has its own
dedicated skill:

| If your matter is in... | Use this skill |
|---|---|
| **NYC Civil Court** (Civil Court Act, $50k cap) | [`ny-nyc-civil-court`] |
| **NYC Housing Court** (RPAPL Article 7 summary proceedings) | [`ny-nyc-housing-court`] |
| **Nassau District Court** (UDCA, $15k cap) | [`ny-nassau-dc`] |
| **Suffolk District Court** (UDCA, $15k cap, western towns + Brookhaven only) | [`ny-suffolk-dc`] |
| **Upstate City Court** (UCCA, $15k cap, Buffalo/Rochester/Syracuse/Albany/Yonkers/etc.) | [`ny-city-courts`] |
| **Town or Village Justice Court** (UJCA, $3k cap, ~1,250 courts) | [`ny-justice-courts`] |
| **Family Court** (FCA: custody, support, family offense, PINS, JD, abuse/neglect) | [`ny-family-court`] |
| **Surrogate's Court** | wills/estates/guardianship — outside the ny-court-docs scope; consult `ny-law-references` for SCPA citations |
| **Court of Claims** (22 NYCRR Part 214; claims against the State of NY) | see `ny-law-references` for the 90-day notice-of-intention regime; specialized practice |

## Cross-references

- `ny-statewide-format` — format baseline (22 NYCRR Part 202
  applies to Supreme/County Court; the other civil-court
  layers use their parallel parts in 22 NYCRR with
  per-court adjustments)
- `ny-commercial-disputes` — Commercial Division substance
  for over-threshold cases routing to one of the Supreme
  Courts above
- `ny-personal-injury`, `ny-employment` — subject-matter
  overlays applicable in Supreme Court Civil Term
- `ny-consumer-debt`, `ny-landlord-tenant` — subject-matter
  bundles
- `ny-file-packet` — NYSCEF assembly for Supreme Court
  filings
