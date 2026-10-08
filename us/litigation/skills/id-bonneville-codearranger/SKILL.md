---
name: id-bonneville-codearranger
title: Bonneville County District Court (Seventh Judicial District, Idaho Falls)
description: Use when drafting or filing civil documents in the Bonneville County District Court — the Seventh Judicial District, sitting in Idaho Falls. Triggers include "Bonneville County District Court", "file in Bonneville County", "sued in Bonneville County", "Idaho Falls courthouse", "Idaho Falls District Court", "Seventh Judicial District", "Seventh District Idaho", "Bonneville County Magistrate Division", "Bonneville County small claims", "Bonneville County case number", "eastern Idaho District Court", "iCourt Bonneville County", and "Bonneville County civil filing". Covers the District Court and its Magistrate Division, the general-vs-limited civil jurisdictional split, the $5,000 Magistrate Division / Small Claims cap, iCourt E-File / I.R.E.F.S. e-filing, the Seventh Judicial District local rules and scheduling-order practice, and Bonneville case-number conventions. Layer on top of `id-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-bonneville
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Bonneville County District Court (Seventh Judicial District, Idaho Falls)

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Local rules,
> administrative orders, and judge-specific practices change; verify
> with the clerk and the current Seventh Judicial District local
> rules before relying on anything here.

Use this skill in addition to `id-statewide-format` when the case is
in the **Bonneville County District Court**, seated in **Idaho
Falls** as the trial court of the **Seventh Judicial District**.
Bonneville is the largest county in eastern Idaho, and its District
Court is the principal high-volume general-civil trial court for the
region.

## The court and the district

Idaho's trial court is a single unified **District Court**,
organized into **seven judicial districts**, each with a
**Magistrate Division**. Bonneville County is the seat of the
**Seventh Judicial District**, which covers **Bingham, Bonneville,
Butte, Clark, Custer, Fremont, Jefferson, Lemhi, Madison, and
Teton** counties. A civil action filed in Bonneville County is
captioned in the **District Court of the Seventh Judicial District
of the State of Idaho, in and for the County of Bonneville** — see
`id-statewide-format` for the full caption form.

Several other Seventh-District counties carry meaningful civil
volume of their own — notably **Madison** (Rexburg) and **Bingham**
(Blackfoot). A matter properly venued in one of those counties is
filed in that county's District Court within the Seventh District,
not in Bonneville; see `id-county-courts` for the district roll-up.

## District Court vs. Magistrate Division — the jurisdictional split

The same District Court has two tiers, and routing the case to the
right tier matters:

- **District Court (district judge)** hears civil claims **over
  $5,000**, plus equity, larger civil disputes, and felonies.
- **Magistrate Division (magistrate judge)** hears civil claims of
  **$5,000 or less** (**I.C. § 1-2208**), and — **regardless of the
  amount in controversy** — forcible entry / unlawful detainer
  (eviction), probate, misdemeanors, traffic infractions, juvenile
  matters, and **all family-law actions**.
- The **Small Claims Department** handles claims up to **$5,000**
  (**I.C. § 1-2301**) with **no punitive damages and no
  pain-and-suffering**; venue lies where the defendant resides or
  the claim arose. Small claims is a simplified, attorney-optional
  track.

Confirm the amount in controversy and subject matter before
choosing the tier; a misfiled case can be transferred. For family
matters in the Magistrate Division, see `id-family-court` and
`id-family-law`.

## Facilities

Bonneville County District Court sits at the **Bonneville County
Courthouse complex in Idaho Falls**. Confirm the current street
address, the civil-filing counter, and the assigned
courtroom/division with the Clerk of the District Court before any
in-person filing or appearance; facility assignments and hours
change.

## Local rules

Practice in this court is governed by the **statewide Idaho Rules of
Civil Procedure (I.R.C.P.)** and **Idaho Rules of Evidence
(I.R.E.)**, as supplemented by the **Seventh Judicial District local
rules** and the court's standing **administrative orders**. The
local rules and standing orders address civil case assignment,
motion and calendar practice, scheduling, chambers-copy
requirements, and local filing conventions.

Do not hard-code rule numbers, page limits, or motion-call mechanics
from memory — read the current Seventh Judicial District local rules
and administrative orders in `id-law-references` (or, where the
corpus is a pointer stub rather than verbatim text, confirm with the
clerk and the court's website) before relying on them.

## E-filing — iCourt E-File (I.R.E.F.S.)

Idaho's statewide electronic-filing portal is **iCourt E-File** (the
Tyler Technologies **Odyssey File & Serve** platform), governed by
the **Idaho Rules for Electronic Filing and Service (I.R.E.F.S.)**.

- **E-filing is mandatory for attorneys** (I.R.E.F.S. 4(a)).
- **Self-represented individuals may e-file (optional)** under
  I.R.E.F.S. 4(b); **once a self-represented party opts in, they are
  bound to e-file for the life of the case.** The Odyssey **Guide &
  File** assisted self-help front end is available.
- **E-filing constitutes consent to electronic service** (I.R.E.F.S.
  17), and documents must meet the **PDF / size requirements** of
  I.R.E.F.S. 6.

Confirm whether e-filing is required for your case type and party,
the current document-type selections, and the filing-fee /
fee-waiver workflow with the clerk. See `id-file-packet` for packet
assembly and preflight.

## Case management and scheduling orders

After the case is at issue, the court manages civil cases through a
**scheduling order** setting discovery cutoffs, disclosure
deadlines, dispositive-motion dates, and the trial date. Note the
load-bearing rule deadlines that the schedule wraps around:

- A **summary-judgment motion (I.R.C.P. 56)** must be **filed at
  least 90 days before trial**; the motion and supporting memorandum
  must be **served at least 28 days before the hearing**, and an
  answering brief is due **at least 14 days before the hearing**.
- A **Notice of Hearing** for an ordinary motion (I.R.C.P. 7(b))
  must be served and filed **at least 14 days before the hearing**.

**Calendar your obligations from the scheduling order entered in
your specific case**, not from a generic template, and confirm the
assigned judge's individual practices, motion-call day, and any
chambers-copy or courtesy-copy requirement. See
`id-schedule-hearing`, `id-hearings`, and `id-deadlines`.

## Case-number conventions

A Bonneville County case number follows Idaho's pattern — a county /
district designator, a year, a case-type code, and a sequential
number (commonly seen as `CV__-__-_____` for civil). **Confirm the
exact case-type code and number format the Bonneville County clerk
assigns** for your cause of action; the case-type code drives docket
routing and tier assignment. Once assigned, the case number anchors
the caption per `id-statewide-format`. Do not guess the code —
verify it against the clerk's intake practice.

**Agent behavior:** before drafting a Notice of Hearing, setting a
page-limited memorandum, or calendaring a deadline, read the current
Seventh Judicial District local rules and standing orders in
`id-law-references`, the scheduling order entered in the case, and
the assigned judge's practices. Confirm the District-Court vs.
Magistrate-Division tier, the iCourt document-type selection, the
motion-call procedure, and any chambers-copy requirement with the
clerk.

## Composition

- For statewide format and the Idaho caption: `id-statewide-format`
- For the first responsive pleading (21-day answer): `id-first-30-days`
- For drafting motions / notices / orders / affidavits:
  `id-draft-motion`, `id-draft-note`, `id-draft-order`,
  `id-draft-declaration`
- For discovery (interrogatories capped at 40; 30-day responses):
  `id-discovery`
- For computing deadlines (I.R.C.P. 2.2): `id-deadlines`
- For scheduling and oral argument: `id-schedule-hearing`,
  `id-hearings`
- For filing mechanics: `id-file-packet`; pre-filing QC:
  `id-quality-check`; citation / quote checking: `id-fact-check`
- For other venues: `id-ada` (Boise / Fourth District),
  `id-county-courts` (other counties and districts)
- For family-law matters in the Magistrate Division:
  `id-family-court`, `id-family-law`
- For pro se conventions: `id-pro-se`

## References

- `id-law-references` — Idaho Rules of Civil Procedure, Idaho Rules
  of Evidence, I.R.E.F.S., Idaho Code (incl. I.C. § 1-2208 and
  § 1-2301), and the Seventh Judicial District local-rules corpus
- Seventh Judicial District local rules and administrative orders;
  the Idaho Supreme Court / Idaho Judicial Branch (isc.idaho.gov)
  for the statewide iCourt E-File system (confirm current versions
  with the clerk and the court's website)
