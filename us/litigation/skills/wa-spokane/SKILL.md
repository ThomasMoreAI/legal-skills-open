---
name: wa-spokane
title: Spokane County Superior Court — Venue Skill
description: Use when handling a Spokane County, Washington Superior Court case — civil practice at the **Spokane County Courthouse** (1116 West Broadway Avenue, Spokane), the largest Eastern Washington county with ~547,000 residents and the regional hub for Eastern WA civil + family + criminal practice. Spokane County Superior Court has **Spokane County Local Rules (SLR)** overlaying the general CR + GR. Coverage includes Spokane's **e-filing system**, the case-management order issued under SLR 16, family-law calendar, Spokane Family Law Commissioners under RCW 2.24, Spokane's participation in **Mandatory Arbitration of Civil Actions (MAR) under RCW 7.06** (current cap per RCW 7.06.020 — read from references), Spokane's **drug- court / therapeutic-court divisions**, and the General Order on remote hearings. Spokane functions as the **Eastern Washington appellate hub** with Division III of the Court of Appeals also seated in Spokane. Triggers include "Spokane County Superior Court", "Spokane
  Superior Court", "SLR", "Spokane local rules", "Spokane e-filing", "Spokane family law", "Spokane MAR", "Division III Court of Appeals".
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-spokane
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Spokane County Superior Court — Venue Skill

> **NOT LEGAL ADVICE.** SLR motion-timing, MAR caps, and
> revision-motion windows are amended periodically.
> Current values live in the references corpus
> (`court-rules/`, `wa-rcw-debt/`) — this skill names
> the controlling sources without embedding the day
> counts.

## At a glance

- **Court**: Spokane County Superior Court
- **Address**: Spokane County Courthouse, 1116 West
  Broadway Avenue, Spokane, WA 99260
- **Population served**: ~547,000
- **Jurisdiction**: General-jurisdiction trial court
  (RCW 2.08) — civil, family, criminal, juvenile,
  probate
- **Regional role**: Eastern Washington's largest
  civil-trial court; **Division III of the Washington
  Court of Appeals** seated in Spokane (serves the
  Eastern Washington counties)

## Local rules

**Spokane County Local Rules (SLR)** overlay the
statewide CR + GR.

### SLR 4 — Initial filings

- Civil cover sheet
- Confidential information form per GR 22
- Specific Spokane case-assignment protocol

### SLR 7 — Motion practice

SLR 7 sets the motion-day timing. **Read the current
schedule from `wa-law-references/references/court-
rules/`** (or hand off to `wa-deadlines`) rather than
relying on memory. Working copies to assigned judge.

### SLR 16 — Case scheduling

Standing case-management order issued setting:

- Status conference
- Discovery cutoff
- Pretrial
- Trial date

### Spokane family-law local rules

Separate family-law local rules — temporary orders,
parenting evaluators, family-law-commissioner practice.

## E-filing

Spokane County uses an electronic filing system; e-filing
mandatory for represented parties. Pro se can use paper
or e-filing through the clerk's portal. Filing fees per
RCW 36.18.020.

## Mandatory Arbitration of Civil Actions — RCW 7.06 + MAR

Spokane County **participates** in mandatory arbitration.
Civil cases below the local jurisdictional cap are
referred. **The cap and the trial-de-novo window are set
by RCW 7.06 and the WA MAR; read current values from
`RCW-7_06.md` and `court-rules/MAR.md`** rather than
relying on memory.

## Commissioners

Spokane has Family Law Commissioners + civil
commissioners (under RCW 2.24) for ex parte, motions,
civil protection orders under RCW 7.105.

**Revision motion** under RCW 2.24.050. **Read the
current revision-motion window from `RCW-2_24.md`** or
hand off to `wa-deadlines`.

## Remote appearances

Spokane maintains a General Order on Remote Appearances.
WebEx dominant; check specific judge's standing order.

## Family law

Spokane has a dedicated family-law calendar. Family Law
Facilitator available under RCW 26.12.180.

## Therapeutic / specialty courts

Spokane operates therapeutic courts including drug court,
mental health court, and (in some divisions) family-
recovery court. These divert qualifying cases from the
traditional criminal calendar.

## Appellate context

**Division III of the Washington Court of Appeals** sits
in Spokane and hears appeals from the 20 Eastern
Washington counties. Spokane practitioners regularly
practice before both Superior Court and Division III.

## Composition with other wa- skills

- `wa-statewide-format` — CR + GR 14
- `wa-deadlines` — current SLR motion timing + RCW
  2.24.050 revision-motion window
- `wa-discovery` — CR 26-37
- `wa-first-30-days` — answer (current day count via
  `wa-deadlines`)
- `wa-family-court` + `wa-family-law`
- Subject-matter bundles
- `wa-fact-check`
