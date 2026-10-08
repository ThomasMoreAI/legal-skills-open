---
name: wa-pierce-codearranger
title: Pierce County Superior Court — Venue Skill
description: Use when handling a Pierce County, Washington Superior Court case — civil practice at the County-City Building in Tacoma (930 Tacoma Avenue South), second-most-populous county (~922,000 residents). Covers general civil + family + criminal + juvenile + probate with Pierce County Local Rules of Superior Court (PCLR) overlaying CR + GR. Pierce participates in Mandatory Arbitration (RCW 7.06) for civil cases below local jurisdictional cap. Coverage includes LINX e-filing system, case-management order (PCLR 16), family-law commissioner system (RCW 2.24), and remote-appearance orders. Appeals route to Court of Appeals Division II (Tacoma). Triggers include "Pierce County Superior Court", "Tacoma Superior Court", "PCLR".
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-pierce
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pierce County Superior Court — Venue Skill

> **NOT LEGAL ADVICE.** Pierce County's local rules
> (PCLR), MAR jurisdictional cap, motion-timing day
> counts, and revision-motion windows are amended by
> court / by the Legislature. This skill names the
> controlling sources; **current day counts and caps
> live in the references corpus** (county-rule text in
> `wa-law-references/references/court-rules/` and
> `wa-law-references/references/wa-rcw-debt/`) rather
> than embedded here.

## At a glance

- **Court**: Pierce County Superior Court
- **Address**: County-City Building, 930 Tacoma Avenue
  South, Tacoma, WA 98402
- **Population served**: ~922,000 (second-largest
  Washington county after King)
- **Jurisdiction**: General-jurisdiction trial court
  (RCW 2.08) — civil, family, criminal, juvenile,
  probate
- **Appellate context**: appeals route to **Washington
  Court of Appeals, Division II** (seated in Tacoma);
  Division II also hears appeals from Thurston, Kitsap,
  Clark, Lewis, Mason, Cowlitz, Pacific, Wahkiakum,
  Skamania, Jefferson, Clallam, and Grays Harbor.

## Local rules

**Pierce County Local Rules of Superior Court (PCLR)**
overlay the statewide CR + GR. Key PCLR provisions:

### PCLR 4 — Initial filings

- Civil cover sheet required
- Confidential information form for cases with sealed
  attachments under GR 22

### PCLR 7 — Motion practice

PCLR 7 sets the motion-day timing (motion / response /
reply schedule). Specific day counts are amended by
order of court — **read PCLR 7 from
`wa-law-references/references/court-rules/`** (or hand
off to `wa-deadlines`) for the current schedule. Working
copies to judge or commissioner.

### PCLR 16 — Case schedule

Standing case-management order issued by court setting:

- Joint Status Conference deadline
- Discovery cutoff
- Pretrial conference
- Trial date

## E-filing — LINX

Pierce County uses **LINX** as its electronic filing
system. Access: https://linxonline.co.pierce.wa.us/

- Mandatory e-filing for represented parties
- Pro se parties may file paper or e-file
- Filing fees per RCW 36.18.020 schedule

## Mandatory Arbitration of Civil Actions — RCW 7.06 + MAR

Pierce County **participates** in mandatory arbitration.
Civil cases below the local jurisdictional cap are
referred to arbitration after answer + initial
discovery. **The cap and the trial-de-novo window are
set by RCW 7.06 and the WA MAR; read current values from
`wa-law-references/references/wa-rcw-debt/RCW-7_06.md`
and from `court-rules/MAR.md`** rather than relying on
memory — RCW 7.06.020 lets counties set local caps and
the procedural rules can be amended. Sanctions apply if
the trial de novo result is no better than the
arbitration award (per MAR 7.3).

## Commissioners

Pierce County uses commissioners (under RCW 2.24) for:

- Ex parte
- Family law motions
- Probate
- Civil protection orders under RCW 7.105
- Some general-civil motions

**Revision motion** — any party may move to revise a
commissioner's ruling under RCW 2.24.050. **The
revision-motion window is statutory; read the current
day count from `RCW-2_24.md`** or hand off to
`wa-deadlines`.

## Remote appearances

Pierce County maintains a **General Order on Remote
Appearances** post-COVID. Cisco WebEx is the dominant
platform; some judges still use Zoom. Check the
specific department's standing order.

## Family law department

Pierce County has a dedicated **Family Law Department**
within Superior Court — separate calendar, dedicated
commissioners. Family Law Facilitator available under
RCW 26.12.180.

## Probate department

Pierce County has a dedicated probate calendar.
Probate ex parte processed by commissioner.

## Composition with other wa- skills

- `wa-statewide-format` — CR + GR 14 baseline
- `wa-deadlines` — current PCLR motion timing + RCW
  2.24.050 revision-motion window
- `wa-discovery` — CR 26-37 discovery + Pierce M&C
  conventions
- `wa-first-30-days` — answer (current day count via
  `wa-deadlines`)
- `wa-family-court` + `wa-family-law` — family-law
  practice in Pierce
- `wa-consumer-debt` / `wa-landlord-tenant` /
  `wa-personal-injury` / `wa-employment` /
  `wa-commercial-disputes` — subject-matter overlays
- `wa-fact-check` — citation verification
