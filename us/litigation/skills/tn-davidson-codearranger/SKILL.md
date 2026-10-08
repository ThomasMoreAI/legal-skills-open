---
name: tn-davidson-codearranger
title: Davidson County Trial Courts (Nashville — 20th Judicial District)
description: This skill should be used when drafting or filing documents in the Davidson County (Nashville) trial courts — the 20th Judicial District. Triggers include "Davidson County Circuit Court", "Davidson County Chancery Court", "Nashville Circuit Court", "Nashville Chancery", "Clerk and Master Nashville", "Davidson County General Sessions", "20th Judicial District", "Metro Nashville court", "Metropolitan Government court", "eFileTN", "Odyssey Davidson Chancery", "sued in Nashville", and "Davidson County Juvenile Court". Covers the Davidson County Circuit Court, Chancery Court (Clerk & Master), General Sessions Court (Civil), and Juvenile Court; the Metropolitan ("Metro") consolidated city-county government structure; Chancery e-filing via eFileTN/Odyssey (Tyler); and the local rules of practice published by the Davidson County clerks. Layer on top of `tn-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-davidson
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Davidson County Trial Courts (Nashville — 20th Judicial District)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current Davidson County local rules and the
> assigned judge's or chancellor's practice preferences before filing.

Use this skill in addition to `tn-statewide-format` when the case is
in a **Davidson County** trial court. Davidson County is the
**20th Judicial District** and is coextensive with the
**Metropolitan Government of Nashville and Davidson County**
("Metro") — a consolidated city-county government, so the county and
the city of Nashville share one government and one set of courts.

## The Davidson County trial courts

| Court | Jurisdiction | Clerk |
|-------|--------------|-------|
| **Circuit Court** | Actions at law; civil damages, tort, contract; divorce; jury trials | Circuit Court Clerk |
| **Chancery Court** | Equity; injunctions, declaratory judgments, many business/real-property matters; divorce | **Clerk & Master** |
| **General Sessions Court (Civil)** | Limited jurisdiction; civil warrants; detainer (eviction) warrants — see `tn-general-sessions` | General Sessions Clerk |
| **Juvenile Court** | Title 37 matters — parentage/custody/support of children of unmarried parents, dependency & neglect, delinquency — see `tn-juvenile-court` | Juvenile Court Clerk |

Both **Circuit and Chancery** have subject-matter jurisdiction over
divorce. Choose the forum based on the relief sought and local
practice; see `tn-family-law`.

## Caption — Davidson County variants

```
        IN THE CIRCUIT COURT FOR DAVIDSON COUNTY, TENNESSEE

[PLAINTIFF],                           )
       Plaintiff,                      )
v.                                     )   Docket No. ____________
[DEFENDANT],                           )
       Defendant.                      )

                  [DOCUMENT TITLE IN ALL CAPS]
```

For **Chancery Court**, the court identifier line reads
`IN THE CHANCERY COURT FOR DAVIDSON COUNTY, TENNESSEE, AT NASHVILLE`
and the matter is heard by a **Chancellor** with the **Clerk & Master**
as clerk. For **General Sessions**, see `tn-general-sessions` — civil
matters there are commenced by a **civil warrant**, not a captioned
complaint.

## Local rules — pull the current set every time

There is **no statewide page/margin/font rule** in Tennessee (see
`tn-statewide-format`). Davidson County's Circuit, Chancery, and
General Sessions courts each publish **local rules of practice** that
control page limits, chambers copies, motion-docket scheduling, and
e-filing requirements. They are indexed on the Administrative Office
of the Courts "Local Rules of Practice" page at **tncourts.gov** and
on the Davidson County clerks' sites.

**Agent behavior:** before drafting a notice, scheduling a hearing, or
setting a page-limited brief, fetch the current Davidson County local
rules for the controlling court and the assigned division. Confirm the
motion-docket day, any chambers-copy requirement, and the
proposed-order format.

## Filing — e-filing platform varies by court

- **Davidson County Chancery Court** uses **eFileTN / Odyssey
  (Tyler Technologies)** for electronic filing. Confirm whether
  e-filing is mandatory for the document type and party.
- **Circuit Court** and **General Sessions** filing mechanics are
  published by their respective clerks; confirm the current platform
  and whether paper filing is still accepted.
- The **appellate** courts use the statewide AOC e-filing portal.

Confirm the controlling platform and account requirements before
assembling a packet; see `tn-file-packet`.

## Motion practice and summary judgment

Davidson County motion practice runs on the Tennessee Rules of Civil
Procedure plus the court's local motion-docket rules:

- **Answer**: 30 days after service of the summons and complaint
  (Tenn. R. Civ. P. 12.01).
- **Summary judgment**: the motion must be served at least **30 days
  before the hearing** (Tenn. R. Civ. P. 56.04); the adverse party's
  response is due no later than 5 days before the hearing. The
  governing standard is the *Celotex*-style standard restored by
  *Rye v. Women's Care Center of Memphis, MPLLC*, 477 S.W.3d 235
  (Tenn. 2015). See `tn-first-30-days`.
- Confirm the local motion-docket scheduling rule and whether the
  division decides motions on the briefs or sets oral argument.

## Composition

- For statewide format: `tn-statewide-format`
- For limited-jurisdiction civil warrants / eviction:
  `tn-general-sessions`
- For Title 37 matters: `tn-juvenile-court`
- For divorce / custody / support: `tn-family-law`, `tn-family-court`
- For the first responsive pleading: `tn-first-30-days`
- For drafting motions / declarations / orders: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`
- For scheduling: `tn-schedule-hearing`
- For filing mechanics: `tn-file-packet`
- For other counties: `tn-county-courts`

## References

- `tn-law-references` — Tenn. R. Civ. P., Tenn. R. Evid., T.C.A.,
  and local-rules corpus
- Davidson County clerks' local rules of practice (via tncourts.gov)
