---
name: tn-knox-codearranger
title: Knox County Trial Courts (Knoxville — 6th Judicial District)
description: This skill should be used when drafting or filing documents in the Knox County (Knoxville) trial courts — the 6th Judicial District. Triggers include "Knox County Circuit Court", "Knox County Chancery Court", "Knoxville Circuit Court", "Knoxville Chancery", "Clerk and Master Knoxville", "Knox County General Sessions", "6th Judicial District", "child support magistrate Knox Chancery", "sued in Knoxville", and "Knox County Juvenile Court". Covers the Knox County Circuit Court, Chancery Court (Clerk & Master, including child-support magistrate practice), General Sessions Court (Civil), and Juvenile Court; and the local rules of practice published by the Knox County courts. Layer on top of `tn-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-knox
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Knox County Trial Courts (Knoxville — 6th Judicial District)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current Knox County local rules and the
> assigned judge's or chancellor's practice preferences before filing.

Use this skill in addition to `tn-statewide-format` when the case is
in a **Knox County** trial court. Knox County (Knoxville) is the
**6th Judicial District**.

## The Knox County trial courts

| Court | Jurisdiction | Clerk |
|-------|--------------|-------|
| **Circuit Court** | Actions at law; civil damages, tort, contract; divorce; jury trials | Circuit Court Clerk |
| **Chancery Court** | Equity; injunctions, declaratory judgments, business/real-property matters; divorce; child-support magistrate matters | **Clerk & Master** |
| **General Sessions Court (Civil)** | Limited jurisdiction; civil warrants; detainer (eviction) warrants — see `tn-general-sessions` | General Sessions Court Clerk |
| **Juvenile Court** | Title 37 matters — parentage/custody/support of children of unmarried parents, dependency & neglect, delinquency — see `tn-juvenile-court` | Juvenile Court Clerk |

Both **Circuit and Chancery** have subject-matter jurisdiction over
divorce. See `tn-family-law`.

### Child-support magistrate practice in Chancery

Knox County Chancery Court hears certain **child-support** matters
before a **magistrate** (a referee/special master who hears and
recommends, with the chancellor confirming). When filing a
child-support matter in Knox Chancery, confirm whether the matter is
set before a magistrate, the magistrate's docket day, and the local
procedure for **filing exceptions / requesting rehearing** of the
magistrate's findings before the chancellor. Verify the current
magistrate-practice local rule before relying on any deadline.

## Caption — Knox County variants

```
        IN THE CIRCUIT COURT FOR KNOX COUNTY, TENNESSEE

[PLAINTIFF],                           )
       Plaintiff,                      )
v.                                     )   Docket No. ____________
[DEFENDANT],                           )
       Defendant.                      )

                  [DOCUMENT TITLE IN ALL CAPS]
```

For **Chancery Court**, the court identifier line reads
`IN THE CHANCERY COURT FOR KNOX COUNTY, TENNESSEE` (some clerks add
"AT KNOXVILLE") and the matter is heard by a **Chancellor** with the
**Clerk & Master** as clerk. For **General Sessions**, see
`tn-general-sessions`.

## Local rules — pull the current set every time

There is **no statewide page/margin/font rule** in Tennessee (see
`tn-statewide-format`). The Knox County courts publish **local rules
of practice** controlling page limits, chambers copies, motion-docket
scheduling, magistrate practice, and filing mechanics, indexed on the
Administrative Office of the Courts "Local Rules of Practice" page at
**tncourts.gov**.

**Agent behavior:** before drafting a notice, scheduling a hearing, or
setting a brief, fetch the current Knox County local rules for the
controlling court and division. Confirm the motion-docket day,
chambers-copy requirement, e-filing platform, and (for child-support)
the magistrate procedure.

## Motion practice and summary judgment

- **Answer**: 30 days after service of the summons and complaint
  (Tenn. R. Civ. P. 12.01).
- **Summary judgment**: served at least **30 days before the hearing**
  (Tenn. R. Civ. P. 56.04); response due no later than 5 days before
  the hearing; the *Celotex*-style standard of
  *Rye v. Women's Care Center of Memphis, MPLLC*, 477 S.W.3d 235
  (Tenn. 2015) governs. See `tn-first-30-days`.

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
- Knox County courts' local rules of practice (via tncourts.gov)
