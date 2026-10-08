---
name: ga-gwinnett-codearranger
title: Gwinnett County Trial Courts (Gwinnett Judicial Circuit)
description: This skill should be used when drafting or filing documents in any Gwinnett County trial court — the Superior Court of Gwinnett County (Gwinnett Judicial Circuit), the State Court of Gwinnett County, the Magistrate Court of Gwinnett County, or Gwinnett's Metro Atlanta Business Case Division enrollment. Triggers include "file in Gwinnett County", "Gwinnett County Superior Court", "Lawrenceville court", "Gwinnett Judicial Circuit", "Gwinnett State Court", "Gwinnett magistrate", "Odyssey eFileGA Gwinnett", and "75 Langley Drive". Covers which Gwinnett court has jurisdiction, the Civil Action File No. caption, the Odyssey eFileGA e-filing posture (NOT PeachCourt), the mandatory ADR program, the Superior Court Transfer Rules, and the domestic standing order. Layers on top of `ga-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-gwinnett
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Gwinnett County Trial Courts (Gwinnett Judicial Circuit)

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice.
> Local rules and judge-specific practices change; verify
> with the clerk and the current local rules before relying
> on anything here.

Use this skill in addition to `ga-statewide-format` whenever the case
is in a Gwinnett County trial court. The **Gwinnett Judicial Circuit**
is a single-county circuit (Gwinnett County only), seated at **75
Langley Drive, Lawrenceville, Georgia** (*verify the current
address*). Pick the right court first — Georgia splits trial
jurisdiction by **subject matter**, not by dollar amount.

## Which Gwinnett court

- **Superior Court of Gwinnett County** — general-jurisdiction trial
  court for the Gwinnett Judicial Circuit; reported at roughly 11
  judges sitting in Divisions 1 through 11 (*verify judge count
  against the current bench*). **Exclusive** over divorce, equity,
  title to land, and felonies (O.C.G.A. §§ 15-6-1, 15-6-8). Court
  **terms** convene the first Monday in March, June, and December and
  the second Monday in September (O.C.G.A. § 15-6-3).
- **State Court of Gwinnett County** — reported at roughly 7 judges
  (*verify against the current bench*). Civil jurisdiction of **any
  amount** with no dollar ceiling (O.C.G.A. § 15-7-4), except the
  superior-exclusive subjects. Most debt-collection and tort suits are
  filed here.
- **Magistrate Court of Gwinnett County** — one of Georgia's busiest
  magistrate courts, reported at roughly 21 judges (*verify against
  the current bench*). Civil cap of **$15,000** (O.C.G.A. § 15-10-2),
  with **no cap on dispossessory** money judgments. Note the
  **enhanced post-judgment discovery** posture under O.C.G.A. § 9-11-69
  where a dispossessory or distress judgment exceeds **$5,000**.
- **Business docket** — Gwinnett **opted into the Metro Atlanta
  Business Case Division (MABCD)**, the first county outside Fulton to
  do so and the **only county to enroll both its State and Superior
  courts** in the division. MABCD has no fixed dollar threshold and
  takes cases by transfer; it is distinct from the statewide Georgia
  State-wide Business Court (O.C.G.A. § 15-5A).

## Caption

Name the specific court and "STATE OF GEORGIA" in the caption, with
the county in the court line (O.C.G.A. § 9-11-10(a)).

```
SUPERIOR COURT OF GWINNETT COUNTY
STATE OF GEORGIA

[PLAINTIFF NAME],
                              Plaintiff,
v.                                          Civil Action File No. __________

[DEFENDANT NAME],
                              Defendant.

                         [TITLE OF PLEADING]
```

For the State Court, substitute the court line with **"STATE COURT OF
GWINNETT COUNTY / STATE OF GEORGIA"**. The Georgia case-number
designation is **"Civil Action File No. ____"**; the number is
assigned by the clerk at filing — do not invent or guess it. Party
designations are Plaintiff/Defendant in civil actions and
Petitioner/Respondent in divorce and family matters.

## E-filing — Odyssey eFileGA (NOT PeachCourt)

Gwinnett civil filings run through **Odyssey eFileGA** (the Tyler
Odyssey portal) — **not PeachCourt**. Flag this clearly: a filer who
defaults to the PeachCourt portal will be at the wrong gateway for
Gwinnett. E-filing is **mandatory** for all State and Superior civil
cases and **optional** in the Magistrate Court. Confirm the current
portal entry point and document codes with the Clerk of Superior Court
before filing.

## Mandatory ADR + Superior Court Transfer Rules

- **Mandatory ADR program** — Gwinnett operates a court-annexed
  alternative-dispute-resolution program; civil cases are routinely
  ordered to ADR. Check the current ADR order and timing for the case.
- **Superior Court Transfer Rules** — Gwinnett publishes transfer
  rules governing movement of cases **between the State and Superior
  Courts** (e.g., when a State Court case implicates a
  superior-exclusive subject). Consult these before assuming the
  filing court can keep a matter.
- **Standing orders by document number** — Gwinnett publishes its
  standing orders by document number; cite the operative document
  number in filings that reference them.

## Domestic standing order + child-support computation

When a domestic case is filed, a **domestic standing order**
auto-attaches and binds both parties on filing/service, and Gwinnett
separately issues a **Child Support Computation Procedures** order
governing the worksheet and supporting documentation. Read the
operative orders in the case and route domestic mechanics through
`ga-family-court`. Judge counts, division assignments, and the
courthouse address change; treat any specific count or address here as
**verify-against-current**.

## Composition

- `ga-statewide-format` — format baseline (O.C.G.A. § 9-11-10 + USCR)
- `ga-state-court` — State Court of Gwinnett County practice
- `ga-magistrate` — Magistrate Court $15,000 / dispossessory mechanics
- `ga-family-court` — divorce, equity, and the domestic standing order
- `ga-consumer-debt` — debt-collection subject-matter bundle
- `ga-first-30-days` — answer, defenses, counterclaims
- `ga-file-packet` — assemble and preflight the filing packet
- `ga-schedule-hearing` — setting hearings and rule nisi
- `ga-deadlines` — time computation and Georgia holidays

## References

- `references/gwinnett-courts-jurisdiction.md` — court-by-court
  jurisdiction split, terms of court, and where to file
- `references/gwinnett-efiling.md` — Odyssey eFileGA workflows and
  document codes (NOT PeachCourt)
- `references/gwinnett-transfer-and-adr.md` — Superior Court Transfer
  Rules and the mandatory ADR program
- `references/gwinnett-standing-orders.md` — standing orders by
  document number, the domestic standing order, and the Child Support
  Computation Procedures order
