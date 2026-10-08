---
name: tn-county-courts-codearranger
title: Tennessee County Courts — Roll-Up
description: This skill should be used when filing in a Tennessee trial court outside the four flagship counties (Davidson/Nashville, Shelby/Memphis, Knox/Knoxville, Hamilton/Chattanooga). Covers the other populous counties' Circuit, Chancery, and General Sessions courts as a roll-up. Triggers include county and city names — "Rutherford County", "Murfreesboro Circuit Court", "Williamson County", "Franklin Chancery", "Montgomery County", "Clarksville court", "Sumner County", "Gallatin court", "Wilson County", "Sevier County", "Sevierville court", "Washington County", "Johnson City court", "Madison County", "Jackson court", "Bradley County", "Cleveland court" — plus generic phrasings like "what judicial district is my county in", "find my county's local rules", and "Tennessee circuit court near me". Tells the reader to confirm the judicial-district number and the controlling local rules via the AOC "Local Rules of Practice" index at tncourts.gov. Layer on top of `tn-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee County Courts — Roll-Up

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify the
> judicial-district number and every local-rule requirement for the
> filing county against the AOC "Local Rules of Practice" index at
> tncourts.gov before filing.

Use this skill in addition to `tn-statewide-format` when the case is
in a Tennessee trial court **other than** the four flagship counties,
which have their own overlay skills:

| County | Principal city | Judicial District | Skill |
|--------|----------------|-------------------|-------|
| Davidson | Nashville | **20th** | `tn-davidson` |
| Shelby | Memphis | **30th** | `tn-shelby` |
| Knox | Knoxville | **6th** | `tn-knox` |
| Hamilton | Chattanooga | **11th** | `tn-hamilton` |

Tennessee has **95 counties** organized into roughly **31 judicial
districts**. Each county has a **Circuit Court** (law), a **Chancery
Court** (equity), and a **General Sessions Court** (limited
jurisdiction). Many counties also have a separate or designated
**Juvenile Court** (see `tn-juvenile-court`).

## Confirm the Judicial District — do not assume

Outside the four flagship counties above, **do not state a
judicial-district number you have not verified.** Judicial-district
composition is set by statute and a single district often spans
several counties. Look up the controlling JD and its local rules on
the AOC index:

**Administrative Office of the Courts — "Local Rules of Practice":
tncourts.gov**

**Agent behavior:** before drafting anything county-specific (a
notice, a scheduling request, a page-limited brief, a proposed order),
fetch (1) the county's judicial-district assignment and (2) the
controlling court's current local rules. Local rules — not any
statewide rule — control page limits, chambers copies, motion-docket
days, e-filing platform, and proposed-order format. (Tennessee has
**no statewide page/margin/font rule** — see `tn-statewide-format`.)

## Other populous counties — generic reference

Name the county, its principal city, and the three trial-court types
generically; **confirm the JD and local rules** before relying on any
specific. Among the most populous non-flagship counties:

| County | Principal city | Courts (confirm JD + local rules) |
|--------|----------------|-----------------------------------|
| Rutherford | Murfreesboro | Circuit / Chancery / General Sessions |
| Williamson | Franklin | Circuit / Chancery / General Sessions |
| Montgomery | Clarksville | Circuit / Chancery / General Sessions |
| Sumner | Gallatin | Circuit / Chancery / General Sessions |
| Wilson | Lebanon | Circuit / Chancery / General Sessions |
| Sevier | Sevierville | Circuit / Chancery / General Sessions |
| Washington | Johnson City / Jonesborough | Circuit / Chancery / General Sessions |
| Madison | Jackson | Circuit / Chancery / General Sessions |
| Bradley | Cleveland | Circuit / Chancery / General Sessions |

This list is illustrative, not exhaustive, and the JD assignments are
**not stated here** precisely because they must be confirmed per
county. Use the AOC index for any county not listed and for the JD
number of any county listed.

## The three trial courts (every county)

- **Circuit Court** — general jurisdiction at law: civil damages,
  tort, contract, and divorce; jury trials. Clerk: Circuit Court
  Clerk.
- **Chancery Court** — equity: injunctions, declaratory judgments,
  many business and real-property matters, and divorce; presided over
  by a **Chancellor** with a **Clerk & Master** as the equity clerk.
- **General Sessions Court** — limited jurisdiction; **$25,000** civil
  cap (T.C.A. § 16-15-501) with **unlimited** detainer (eviction)
  jurisdiction; informal procedure; suit by **civil warrant**;
  **10-day de novo appeal to Circuit Court** (T.C.A. § 27-5-108). See
  `tn-general-sessions`.

Both Circuit and Chancery have subject-matter jurisdiction over
divorce; see `tn-family-law`.

## Caption — generic county variant

```
        IN THE CIRCUIT COURT FOR [COUNTY] COUNTY, TENNESSEE

[PLAINTIFF],                           )
       Plaintiff,                      )
v.                                     )   Docket No. ____________
[DEFENDANT],                           )
       Defendant.                      )

                  [DOCUMENT TITLE IN ALL CAPS]
```

For Chancery, use `IN THE CHANCERY COURT FOR [COUNTY] COUNTY,
TENNESSEE` (many add "AT [CITY]"); for General Sessions, use
`IN THE GENERAL SESSIONS COURT FOR [COUNTY] COUNTY, TENNESSEE`.
Confirm the exact "for/of" preposition and any city tag against the
county's local caption forms.

## Filing — platform varies by county

Tennessee has **no universal e-filing mandate**. Trial-court e-filing
is county-by-county: some courts use Tyler/Odyssey (eFileTN), some use
eFlex, some use Tybera (TnCIS), and some still accept paper. Confirm
the controlling county's platform and whether e-filing is mandatory
before assembling a packet. See `tn-file-packet`.

## Composition

- For statewide format: `tn-statewide-format`
- For the four flagship counties: `tn-davidson`, `tn-shelby`,
  `tn-knox`, `tn-hamilton`
- For limited-jurisdiction civil warrants / eviction:
  `tn-general-sessions`
- For Title 37 matters: `tn-juvenile-court`
- For divorce / custody / support: `tn-family-law`, `tn-family-court`
- For the first responsive pleading: `tn-first-30-days`
- For scheduling and filing: `tn-schedule-hearing`, `tn-file-packet`
- For pro se conventions: `tn-pro-se`

## References

- `tn-law-references` — Tenn. R. Civ. P., Tenn. R. Evid., T.C.A.,
  and local-rules corpus
- AOC "Local Rules of Practice" index (tncourts.gov) — confirm JD and
  local rules per county
