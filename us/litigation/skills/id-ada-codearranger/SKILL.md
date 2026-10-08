---
name: id-ada-codearranger
title: Ada County District Court (Fourth Judicial District, Boise)
description: Use when drafting or filing civil documents in the Ada County District Court — the Fourth Judicial District, sitting in Boise, Idaho's largest and highest-volume trial court. Triggers include "Ada County District Court", "file in Ada County", "sued in Ada County", "Boise courthouse", "Fourth Judicial District", "Fourth District Idaho", "Ada County Magistrate Division", "Ada County small claims", "Ada County case number", "Boise District Court e-filing", "iCourt Ada County", and "Ada County civil filing". Covers the District Court and its Magistrate Division, the general-vs-limited civil jurisdictional split, the $5,000 Magistrate Division / Small Claims cap, mandatory iCourt e-filing, the Fourth Judicial District local rules, and Ada case-number conventions. Layer on top of `id-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-ada
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ada County District Court (Fourth Judicial District, Boise)

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Local rules,
> administrative orders, and judge-specific practices change; verify
> with the clerk and the current Fourth Judicial District local
> rules before relying on anything here.

Use this skill in addition to `id-statewide-format` when the matter
is a **civil** case in the **Ada County District Court**, which sits
in **Boise** as the trial court of the **Fourth Judicial District**.
Ada County is Idaho's most populous county and its District Court is
the state's largest by caseload.

## The court and the district

Idaho's trial court is a single unified **District Court**,
organized into **seven judicial districts**, each containing a
**Magistrate Division**. Ada County is the seat of the **Fourth
Judicial District**, which also covers **Boise, Elmore, and Valley**
counties. A civil action filed in Ada County is captioned in the
**District Court of the Fourth Judicial District of the State of
Idaho, in and for the County of Ada** — see `id-statewide-format`
for the full caption.

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

## Local rules

Practice in this court is governed by the **statewide Idaho Rules of
Civil Procedure (I.R.C.P.)** and **Idaho Rules of Evidence
(I.R.E.)**, as supplemented by the **Fourth Judicial District local
rules** and the court's standing **administrative orders**. The
local rules and standing orders address civil case management,
motion and calendar practice, scheduling, and chambers-copy
requirements.

Do not hard-code rule numbers, page limits, or motion-calendar
mechanics from memory — read the current Fourth Judicial District
local rules and administrative orders in `id-law-references` (or
confirm with the clerk and the court's website) before relying on
them.

## E-filing — iCourt E-File (mandatory posture)

Idaho's statewide electronic-filing portal is **iCourt E-File** (the
Tyler Technologies **Odyssey File & Serve** platform), governed by
the **Idaho Rules for Electronic Filing and Service (I.R.E.F.S.)**.

- **E-filing is mandatory for attorneys** (I.R.E.F.S. 4(a)). Ada
  County was an **early mandatory-adoption county** for iCourt, so
  represented civil filings here run through iCourt E-File.
- **Self-represented individuals may e-file (optional)** under
  I.R.E.F.S. 4(b), but **once a self-represented party opts in, they
  are bound to e-file for the life of the case.** The Odyssey **Guide
  & File** assisted self-help front end is available.
- **E-filing constitutes consent to electronic service** (I.R.E.F.S.
  17), and documents must meet the **PDF / size requirements** of
  I.R.E.F.S. 6.

Confirm the current document-type selections, the filing-fee /
fee-waiver workflow, and whether your document type permits any
alternative channel before assembling a packet. See
`id-file-packet`.

## Case management and scheduling

After the case is at issue, the court manages civil cases through a
**scheduling order** setting discovery cutoffs, disclosure
deadlines, dispositive-motion dates (note **I.R.C.P. 56** requires a
summary-judgment motion to be filed **at least 90 days before
trial**), and the trial date. **Calendar your obligations from the
scheduling order entered in your specific case**, and confirm the
assigned judge's individual practices, motion-call procedure, and
any chambers-copy requirement. See `id-schedule-hearing`,
`id-hearings`, and `id-deadlines`.

## Case-number conventions

An Ada County case number follows Idaho's pattern — a county /
district designator, a year, a case-type code, and a sequential
number (commonly seen as `CV__-__-_____` for civil). **Confirm the
exact case-type code and number format the Ada County clerk
assigns** for your cause of action; the case-type code drives docket
routing and tier assignment. Once assigned, the case number anchors
the caption per `id-statewide-format`. Do not guess the code —
verify it against the clerk's intake practice.

**Agent behavior:** before drafting a Notice of Hearing, setting a
page-limited memorandum, or calendaring a deadline, read the current
Fourth Judicial District local rules and standing orders in
`id-law-references`, the scheduling order entered in the case, and
the assigned judge's practices. Confirm the District-Court vs.
Magistrate-Division tier, the iCourt document-type selection, and
any chambers-copy requirement with the clerk.

## Composition

- For statewide format and the Idaho caption: `id-statewide-format`
- For the first responsive pleading (21-day answer): `id-first-30-days`
- For drafting motions / notices / orders / affidavits:
  `id-draft-motion`, `id-draft-note`, `id-draft-order`,
  `id-draft-declaration`
- For computing deadlines (I.R.C.P. 2.2): `id-deadlines`
- For scheduling a hearing and oral argument: `id-schedule-hearing`,
  `id-hearings`
- For assembling and e-filing a packet: `id-file-packet`
- For discovery: `id-discovery`
- For other venues: `id-bonneville` (Idaho Falls / Seventh
  District), `id-county-courts` (other counties and districts)
- For family-law matters in the Magistrate Division:
  `id-family-court`, `id-family-law`
- For pro se conventions: `id-pro-se`

## References

- `id-law-references` — Idaho Rules of Civil Procedure, Idaho Rules
  of Evidence, I.R.E.F.S., Idaho Code, and the Fourth Judicial
  District local-rules corpus
- Fourth Judicial District local rules and administrative orders;
  the Idaho Supreme Court / Idaho Judicial Branch (isc.idaho.gov)
  for the statewide iCourt E-File system (confirm current versions
  with the clerk and the court's website)
