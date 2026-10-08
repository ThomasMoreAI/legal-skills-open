---
name: ga-fulton-codearranger
title: Fulton County Trial Courts (Atlanta Judicial Circuit)
description: This skill should be used when drafting or filing documents in any Fulton County trial court — the Superior Court of Fulton County (Atlanta Judicial Circuit), the State Court of Fulton County, the Magistrate Court of Fulton County, or the Metro Atlanta Business Case Division. Triggers include "file in Fulton County", "Fulton County Superior Court", "Atlanta Judicial Circuit", "Fulton State Court", "Fulton magistrate", "Fulton business case division", "Atlanta court e-file", "eFileGA", and "PeachCourt". Covers which Fulton court has jurisdiction, the Civil Action File No. caption, the mandatory eFileGA / PeachCourt e-filing posture, the Family Division Automatic Domestic Standing Order, and the per-judge Civil Standing Case Management Orders. Layers on top of `ga-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-fulton
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fulton County Trial Courts (Atlanta Judicial Circuit)

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice.
> Local rules and judge-specific practices change; verify
> with the clerk and the current local rules before relying
> on anything here.

Use this skill in addition to `ga-statewide-format` whenever the case
is in a Fulton County trial court. The **Atlanta Judicial Circuit** is
a single-county circuit (Fulton County only). Pick the right court
first — Georgia splits trial jurisdiction by **subject matter**, not
by dollar amount.

## Which Fulton court

- **Superior Court of Fulton County** — general-jurisdiction trial
  court for the Atlanta Judicial Circuit; the largest superior bench
  in Georgia (reported at roughly 20 judges — *verify judge count
  against the current bench*). Organized into General Civil, Family,
  Criminal, and Business Case divisions. **Exclusive** over divorce,
  equity, title to land, and felonies (O.C.G.A. §§ 15-6-1, 15-6-8;
  Ga. Const. art. VI). Hears all civil matters not committed
  exclusively elsewhere.
- **State Court of Fulton County** — created by Ga. L. 1976 p. 3023,
  consolidating the now-defunct Civil Court and Criminal Court of
  Fulton County (the old Civil Court of Fulton County is historical;
  cite only for legacy matters). Reported at roughly 10 judges
  (*verify against the current bench*). Civil jurisdiction of **any
  amount** with no dollar ceiling (O.C.G.A. § 15-7-4), except the
  superior-exclusive subjects. Most debt-collection and tort suits
  are filed here.
- **Magistrate Court of Fulton County** — civil cap of **$15,000**
  (O.C.G.A. § 15-10-2), plus dispossessory and garnishment matters
  (the cap does not limit dispossessory money judgments). Fulton
  Magistrate is **mandatory e-file with no paper accepted**, including
  for dispossessory and garnishment filings.
- **Metro Atlanta Business Case Division (MABCD)** — a local business
  docket; the Fulton **State Court** joined effective January 2020.
  **No fixed dollar threshold**; cases come in by transfer through a
  selection committee. This is **distinct** from the statewide Georgia
  State-wide Business Court (O.C.G.A. § 15-5A), whose thresholds are
  generally ≥ $1,000,000 in real-property disputes or ≥ $500,000
  otherwise. Do not conflate the two.

## Caption

Name the specific court and "STATE OF GEORGIA" in the caption, with
the county in the court line (O.C.G.A. § 9-11-10(a)).

```
SUPERIOR COURT OF FULTON COUNTY
STATE OF GEORGIA

[PLAINTIFF NAME],
                              Plaintiff,
v.                                          Civil Action File No. __________

[DEFENDANT NAME],
                              Defendant.

                         [TITLE OF PLEADING]
```

For the State Court, substitute the court line with **"STATE COURT OF
FULTON COUNTY / STATE OF GEORGIA"**. The Georgia case-number
designation is **"Civil Action File No. ____"**; the number is
assigned by the clerk at filing — do not invent or guess it. Party
designations are Plaintiff/Defendant in civil actions and
Petitioner/Respondent in divorce and family matters.

## E-filing — eFileGA / PeachCourt

Fulton civil filings run through **eFileGA / PeachCourt**, the
electronic-filing portal built on the Tyler Odyssey backbone.
E-filing is **mandatory** for Superior, State, and Magistrate civil
cases under SB 407 (statewide civil e-file mandate, effective on or
about January 1, 2019). Confirm the current portal entry point and
document codes with the Clerk of Superior and Magistrate Courts before
filing.

## Family Division — Automatic Domestic Standing Order

The Superior Court operates a dedicated **Family Division**. When a
domestic case is filed, an **Automatic Domestic Standing Order**
attaches and binds both parties on filing/service (typically
restraining dissipation of assets, changes to insurance, harassment,
and removal of children, among other terms). Read the operative
standing order in the case and route domestic mechanics through
`ga-family-court`.

## TRAP — per-judge Civil Standing Case Management Orders

Fulton Superior judges issue **individual Civil Standing Case
Management Orders** that govern motion practice, conferral, courtesy
copies, and scheduling for cases on that judge's calendar. These
control alongside — and sometimes tighten — the Uniform Superior Court
Rules. **Always read the assigned judge's standing order**, not just
the USCR, before drafting motions or setting anything. Judge counts,
division assignments, and addresses change; treat any specific count
or address here as **verify-against-current**.

## Composition

- `ga-statewide-format` — format baseline (O.C.G.A. § 9-11-10 + USCR)
- `ga-state-court` — State Court of Fulton County practice
- `ga-magistrate` — Magistrate Court $15,000 / dispossessory mechanics
- `ga-family-court` — divorce, equity, and the domestic standing order
- `ga-consumer-debt` — debt-collection subject-matter bundle
- `ga-first-30-days` — answer, defenses, counterclaims
- `ga-file-packet` — assemble and preflight the filing packet
- `ga-schedule-hearing` — setting hearings and rule nisi
- `ga-deadlines` — time computation and Georgia holidays

## References

- `references/fulton-courts-jurisdiction.md` — court-by-court
  jurisdiction split and where to file
- `references/fulton-efiling.md` — eFileGA / PeachCourt workflows and
  document codes
- `references/fulton-standing-orders.md` — per-judge Civil Standing
  Case Management Orders and the Family Division Automatic Domestic
  Standing Order
- `references/mabcd-business-case-division.md` — Metro Atlanta Business
  Case Division intake and transfer
