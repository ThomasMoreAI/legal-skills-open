---
name: mi-circuit-courts-codearranger
title: Michigan Circuit Courts — Roll-Up
description: Use when filing in a Michigan circuit court other than Wayne (Third) or Oakland (Sixth), which have dedicated skills. Covers most-populous circuits (Macomb 16th, Kent 17th, Genesee 7th, Washtenaw 22nd, Ingham 30th, Kalamazoo 9th, Ottawa 20th, Saginaw 10th) with directory of counties and circuits. Triggers include "Michigan circuit court", "Macomb circuit", "Kent County circuit", "which circuit court Michigan", "Michigan Business Court", "find my county's local administrative order". Layer on top of `mi-statewide-format`. Confirm the circuit's local rules and MiFILE e-filing status before filing.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-circuit-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Circuit Courts — Roll-Up

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> the controlling circuit, its local administrative orders, and
> its e-filing (MiFILE) status with the clerk and the current
> court rules before filing.

Use this skill in addition to `mi-statewide-format` when the case
is in a Michigan **circuit court** other than the two flagship
counties, which have their own overlay skills:

| County | Principal city | Circuit | Skill |
|--------|----------------|---------|-------|
| Wayne | Detroit | **3rd** | `mi-wayne` |
| Oakland | Pontiac | **6th** | `mi-oakland` |

## What a circuit court is

The **circuit court** is Michigan's court of **general jurisdiction**
— one in each of the state's judicial circuits, established under MCL
600.501 et seq. It hears:

- **civil cases over $25,000** (claims at or below $25,000 go to the
  district court — see `mi-district-courts`);
- the **Family Division** (domestic relations, custody, support,
  juvenile, personal-protection orders — see `mi-family-court`);
- **felony** criminal matters; and
- **appeals** from district court, probate court, and many
  administrative agencies.

Each circuit has a presiding/chief judge and operates under both the
statewide Michigan Court Rules (MCR) and its own **local
administrative orders (LAOs)** approved by the State Court
Administrative Office (SCAO).

## Confirm the circuit — do not assume

Most Michigan circuits are a **single county**, but several are
**multi-county** (one circuit spanning two or more rural counties).
**Do not state a circuit number you have not verified.** Look up the
controlling circuit and its local administrative orders via the SCAO
court directory at **courts.michigan.gov**.

**Agent behavior:** before drafting anything circuit-specific (a
notice, a scheduling request, a page-limited brief, a proposed
order), confirm (1) which circuit the county sits in, (2) that
circuit's current local administrative orders, and (3) its e-filing
status. Local administrative orders govern motion-call days,
scheduling practice, chambers/judge copies, and case-flow management
on top of the statewide MCR.

## Most-populous circuits — directory

Name the county, its principal city, and the circuit generically;
**confirm the local administrative orders and MiFILE status** before
relying on any specific.

| County | Principal city | Circuit |
|--------|----------------|---------|
| Macomb | Mount Clemens | **16th** |
| Kent | Grand Rapids | **17th** |
| Genesee | Flint | **7th** |
| Washtenaw | Ann Arbor | **22nd** |
| Ingham | Lansing | **30th** |
| Kalamazoo | Kalamazoo | **9th** |
| Ottawa | Grand Haven | **20th** |
| Saginaw | Saginaw | **10th** |

This list is illustrative, not exhaustive. For any county not listed,
and to confirm the circuit number and judges for any county listed,
use the SCAO court directory at courts.michigan.gov.

## Michigan Business Court

Each circuit that meets the statutory case-volume threshold maintains
a **Business Court** docket under **MCL 600.8031 et seq.** — a
specialized docket for business and commercial disputes (shareholder
and LLC-member disputes, commercial contract claims above the
statutory amount, trade-secret and non-compete matters, business
torts). Assignment is by case-type code at filing. Whether a given
circuit has a Business Court, and the local assignment mechanics, vary
by circuit — **confirm with the controlling circuit's local
administrative orders.** See `mi-commercial-disputes` for the
substantive framework.

## Caption — generic circuit variant

```
        STATE OF MICHIGAN
        IN THE CIRCUIT COURT FOR THE COUNTY OF [COUNTY]

[PLAINTIFF],
       Plaintiff,
v.                                     Case No. ____________-___
                                       Hon. ____________________
[DEFENDANT],
       Defendant.
___________________________________/

                  [DOCUMENT TITLE]
```

The Michigan case number carries a **case-type code** (e.g., `-CZ`
general civil, `-NZ` other civil, `-CB`/`-CK` Business Court, `-NM`
auto negligence). Use the code that matches the claim; confirm the
circuit's accepted codes. See `mi-statewide-format` for the full MCR
1.109 / MCR 2.113 caption and signature-block conventions, including
the attorney **P-number**.

## Filing — MiFILE status varies by circuit

Michigan is mid-rollout of **MiFILE** (the MiCOURT / TrueFiling
e-filing system). E-filing is **mandatory in some circuits and case
types and not yet live in others**. Confirm the controlling circuit's
MiFILE status and whether e-filing is mandatory before assembling a
packet. See `mi-file-packet`.

## Composition

- For statewide format: `mi-statewide-format`
- For the two flagship circuits: `mi-wayne`, `mi-oakland`
- For claims at or below $25,000 (district court):
  `mi-district-courts`
- For domestic relations / custody / support / PPOs:
  `mi-family-court`, `mi-family-law`
- For business and commercial matters: `mi-commercial-disputes`
- For the first responsive pleading: `mi-first-30-days`
- For scheduling and filing: `mi-schedule-hearing`, `mi-file-packet`
- For pro se conventions: `mi-pro-se`

## References

- `mi-law-references` — MCR, MRE, MCL, and local-rules corpus
- SCAO court directory (courts.michigan.gov) — confirm the circuit,
  its local administrative orders, and MiFILE status per county
