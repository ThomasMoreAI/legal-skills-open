---
name: tn-shelby-codearranger
title: Shelby County Trial Courts (Memphis — 30th Judicial District)
description: This skill should be used when drafting or filing documents in the Shelby County (Memphis) trial courts — the 30th Judicial District. Triggers include "Shelby County Circuit Court", "Shelby County Chancery Court", "Memphis Circuit Court", "Memphis Chancery", "Clerk and Master Memphis", "Shelby County General Sessions", "30th Judicial District", "eFlex Shelby", "sued in Memphis", and "Shelby County Juvenile Court". Covers the Shelby County Circuit Court, Chancery Court (Clerk & Master), General Sessions Court (Civil), and Juvenile Court; Circuit and Chancery e-filing via eFlex; and the local rules of practice published by the Shelby County courts. Layer on top of `tn-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-shelby
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Shelby County Trial Courts (Memphis — 30th Judicial District)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current Shelby County local rules and the
> assigned judge's or chancellor's practice preferences before filing.

Use this skill in addition to `tn-statewide-format` when the case is
in a **Shelby County** trial court. Shelby County (Memphis) is the
**30th Judicial District** and is Tennessee's most populous county.

## The Shelby County trial courts

| Court | Jurisdiction | Clerk |
|-------|--------------|-------|
| **Circuit Court** | Actions at law; civil damages, tort, contract; divorce; jury trials | Circuit Court Clerk |
| **Chancery Court** | Equity; injunctions, declaratory judgments, business/real-property matters; divorce | **Clerk & Master** |
| **General Sessions Court (Civil)** | Limited jurisdiction; civil warrants; detainer (eviction) warrants — see `tn-general-sessions` | General Sessions Court Clerk |
| **Juvenile Court** | Title 37 matters — parentage/custody/support of children of unmarried parents, dependency & neglect, delinquency — see `tn-juvenile-court` | Juvenile Court Clerk |

Both **Circuit and Chancery** have subject-matter jurisdiction over
divorce. See `tn-family-law` for forum selection.

## Caption — Shelby County variants

```
        IN THE CIRCUIT COURT OF SHELBY COUNTY, TENNESSEE

[PLAINTIFF],                           )
       Plaintiff,                      )
v.                                     )   Docket No. ____________
[DEFENDANT],                           )
       Defendant.                      )

                  [DOCUMENT TITLE IN ALL CAPS]
```

For **Chancery Court**, the court identifier line reads
`IN THE CHANCERY COURT OF SHELBY COUNTY, TENNESSEE, AT MEMPHIS` and
the matter is heard by a **Chancellor** with the **Clerk & Master** as
clerk. Confirm the exact "for/of" preposition and "AT MEMPHIS" tag
against current Shelby County local-rule caption forms. For
**General Sessions**, see `tn-general-sessions`.

## Local rules — pull the current set every time

There is **no statewide page/margin/font rule** in Tennessee (see
`tn-statewide-format`). The Shelby County Circuit, Chancery, and
General Sessions courts each publish **local rules of practice** that
control page limits, chambers copies, motion-docket scheduling, and
e-filing requirements, indexed on the Administrative Office of the
Courts "Local Rules of Practice" page at **tncourts.gov** and on the
Shelby County courts' sites.

**Agent behavior:** before drafting a notice, scheduling a hearing, or
setting a page-limited brief, fetch the current Shelby County local
rules for the controlling court and division. Confirm the
motion-docket day, chambers-copy requirements, and proposed-order
format.

## Filing — eFlex

- **Shelby County Circuit Court and Chancery Court** use **eFlex** for
  electronic filing. Confirm whether e-filing is mandatory for the
  document type and party, and confirm the current account / training
  requirements.
- **General Sessions** filing mechanics are published by the
  General Sessions Court Clerk; confirm the current platform.
- The **appellate** courts use the statewide AOC e-filing portal.

See `tn-file-packet` for the packet-assembly workflow.

## Motion practice and summary judgment

- **Answer**: 30 days after service of the summons and complaint
  (Tenn. R. Civ. P. 12.01).
- **Summary judgment**: served at least **30 days before the hearing**
  (Tenn. R. Civ. P. 56.04); response due no later than 5 days before
  the hearing; the *Celotex*-style standard restored by
  *Rye v. Women's Care Center of Memphis, MPLLC*, 477 S.W.3d 235
  (Tenn. 2015) governs. See `tn-first-30-days`.
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
- Shelby County courts' local rules of practice (via tncourts.gov)
