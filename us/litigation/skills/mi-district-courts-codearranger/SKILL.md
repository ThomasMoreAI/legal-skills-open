---
name: mi-district-courts-codearranger
title: Michigan District Courts — Roll-Up
description: Use when filing in a Michigan district court other than 36th District (Detroit), which has its own skill. Michigan's limited-jurisdiction trial courts dominant in consumer-debt and eviction. Triggers include "Michigan district court", "district court debt", "Michigan eviction", "small claims Michigan", "which district court Michigan", "summary proceedings Michigan", "MCR 4.201", "civil infraction Michigan". Covers $25k civil jurisdiction cap (MCL 600.8301), landlord-tenant summary proceedings (MCL 600.5701, MCR 4.201), small claims division (MCR 4.301), civil infractions, district numbering and organization, and how to find controlling district court, its local orders, and MiFILE e-filing status. Layer on top of `mi-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-district-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan District Courts — Roll-Up

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> the controlling district court, its local administrative
> orders, the current jurisdictional and small-claims dollar
> caps, and every local requirement against the official sources
> before filing.

Use this skill in addition to `mi-statewide-format` when the case
is in a Michigan **district court other than the 36th District
Court** (Detroit), which has its own overlay skill:

| Court | Coverage | Skill |
|-------|----------|-------|
| 36th District Court | City of Detroit | `mi-36th-district` |

Michigan's district courts are limited-jurisdiction trial courts
organized into numbered **judicial districts** under MCL 600.8101
et seq. They are the busiest civil forum in the state and where
**most consumer-debt collection suits and residential evictions
are filed**. Above the district court sits the general-jurisdiction
**circuit court** (see `mi-circuit-courts`).

## Civil money jurisdiction — up to $25,000

A district court has jurisdiction over civil actions where the
amount in controversy does **not exceed $25,000** (MCL 600.8301).
Claims above that ceiling belong in circuit court. Confirm the
current statutory amount in the corpus before relying on it — the
cap is set by statute and has been raised over time.

District courts also handle:

- **Landlord-tenant summary proceedings** (eviction / recovery of
  possession) — see below.
- **Small claims** through the small claims division — see below.
- **Civil infractions** (traffic and ordinance), garnishments
  ancillary to district-court judgments, and certain
  misdemeanors (criminal scope is outside this skill).

## Landlord-tenant summary proceedings (MCL 600.5701+ / MCR 4.201)

Residential and commercial **summary proceedings to recover
possession** are filed in the district court for the district
where the property sits. The substantive and procedural framework
is the **Summary Proceedings Act, MCL 600.5701 et seq.**, with
practice governed by **MCR 4.201** (and MCR 4.202 for land-contract
forfeitures). Key features:

- Commenced by a statutory **notice to quit / demand for
  possession** followed by a **summons and complaint** on the
  SCAO-approved form.
- An accelerated timeline with a short return date — confirm the
  current day counts and notice periods in the corpus.
- A possession judgment, money judgment, and (after the redemption
  / stay period) a **writ of restitution / order of eviction**.

For the substantive landlord-tenant law (notice periods, the
Truth in Renting Act, security deposits, retaliation, the
warranty of habitability), use **`mi-landlord-tenant`** — these
cases live almost entirely in district court.

## Small claims division (MCR 4.301+)

Each district court has a **small claims division** governed by
**MCR 4.301 et seq.** It is an informal forum: no attorneys for
parties (with narrow exceptions), no jury, **no appeal of right**,
and a streamlined hearing. The **dollar ceiling for small claims
is lower than the general $25,000 district-court cap** and is set
by statute — **point to the corpus for the current small-claims
cap rather than stating a figure that may be stale.** A party
(or the opposing party) may **remove** a small-claims case to the
general civil docket of the district court, where the regular
rules and the right to counsel apply.

## How district courts are numbered and organized

District courts are identified by **judicial-district number**
(e.g., "52-1 District Court", "41-B District Court"). A district
may be:

- a **single municipality** (a district of the "first class" or
  "third class"), or
- a **county-wide or multi-jurisdiction district** ("second
  class"), sometimes with multiple **divisions** sitting in
  different cities.

Because districting and division geography are set by statute and
local administrative order, **do not assert which numbered
district court controls a given address without confirming it.**

## Find the right district court — do not assume

Before drafting anything court-specific (a complaint caption, a
notice, a scheduling request, a proposed order):

1. **Identify the controlling district court** for the
   defendant's residence or the property's location. The Michigan
   Courts directory at **courts.michigan.gov** maps municipalities
   to district courts.
2. **Pull that court's local administrative orders (LAOs)** and
   any posted local practices — they control motion-day
   scheduling, chambers copies, and form preferences.
3. **Confirm the court's e-filing status.** Michigan is rolling
   out mandatory statewide e-filing through **MiFILE (MiCOURT
   TrueFiling)** county-by-county; some district courts are live
   and mandatory, others still take paper. Verify before
   assembling a packet — see `mi-file-packet`.

## Caption — generic district-court variant

```
                       STATE OF MICHIGAN
   IN THE [NN-N] DISTRICT COURT FOR THE COUNTY OF [COUNTY]

[PLAINTIFF],
       Plaintiff,
                                        Case No. ____________-__
v.                                      Hon. ____________________

[DEFENDANT],
       Defendant.
___________________________________/

                  [DOCUMENT TITLE IN ALL CAPS]
```

Confirm the exact district number, the county / municipality tag,
and the case-type code against the controlling court's caption
forms. Apply the `mi-statewide-format` conventions for paragraph
numbering, the signature block with the attorney's **P-number**,
and proof of service.

## Composition

- For statewide format and the caption / signature mechanics:
  `mi-statewide-format`
- For the Detroit district court: `mi-36th-district`
- For general-jurisdiction matters over $25,000: `mi-circuit-courts`
- For consumer-debt defense (these suits mostly live here):
  `mi-consumer-debt`
- For eviction / summary-proceedings substance:
  `mi-landlord-tenant`
- For the first responsive pleading: `mi-first-30-days`
- For scheduling and filing: `mi-schedule-hearing`, `mi-file-packet`
- For pro se conventions: `mi-pro-se`

## References

- `mi-law-references` — MCR (MCR 4.201, 4.202, 4.301 et seq.),
  MCL Chapter 600 (§ 600.8301 jurisdiction; § 600.5701 et seq.
  summary proceedings; small-claims cap), and local-rules corpus.
  Confirm current dollar caps and day counts here.
- Michigan Courts directory (courts.michigan.gov) — map an
  address to its district court; confirm MiFILE status and LAOs.
