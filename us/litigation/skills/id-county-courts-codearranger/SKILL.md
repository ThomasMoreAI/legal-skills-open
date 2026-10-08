---
name: id-county-courts-codearranger
title: Idaho District Courts — Roll-Up (Other Counties and Districts)
description: Use when filing in an Idaho District Court other than Ada County (Fourth District) or Bonneville County (Seventh District), which have their own overlay skills. Idaho's trial court is one unified District Court organized into seven judicial districts, each with a Magistrate Division. Triggers include "Idaho District Court", "which judicial district", "what district is my Idaho case in", "Canyon County District Court", "Kootenai County District Court", "Twin Falls District Court", "Bannock County District Court", "Nez Perce County District Court", "Coeur d'Alene courthouse", "Pocatello courthouse", "Caldwell courthouse", "Lewiston courthouse", "Idaho county district court local rules", "First Judicial District", "Second Judicial District", "Third Judicial District", "Fifth Judicial District", "Sixth Judicial District", and "Idaho magistrate division". Tells the reader to confirm the county's judicial district, its local rules, and iCourt e-filing status. Layer on top of `id-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Idaho District Courts — Roll-Up (Other Counties and Districts)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> the controlling county's judicial district, its local rules, and
> its iCourt E-File status with the clerk and the current rules
> before filing.

Use this skill in addition to `id-statewide-format` when the case is
in an Idaho **District Court** other than the two highest-volume
counties, which have their own overlay skills:

| County | Principal city | District | Skill |
|--------|----------------|----------|-------|
| Ada | Boise | Fourth | `id-ada` |
| Bonneville | Idaho Falls | Seventh | `id-bonneville` |

## What the District Court is

Idaho's trial court is a single unified **District Court**,
organized into **seven judicial districts**. Each district contains
a **Magistrate Division**. A filing is captioned in the "District
Court of the [Nth] Judicial District of the State of Idaho, in and
for the County of [COUNTY]" — not in a separately constituted county
court. The court hears:

- **civil cases over $5,000** before a **district judge**; civil
  claims of **$5,000 or less** go to the **Magistrate Division**
  (**I.C. § 1-2208**), as does the **Small Claims Department** up to
  **$5,000** (**I.C. § 1-2301**);
- in the **Magistrate Division**, regardless of amount: forcible
  entry / unlawful detainer (eviction), probate, misdemeanors,
  traffic infractions, juvenile, and **all family-law actions**
  (see `id-family-court`, `id-family-law`);
- **felony** criminal matters in the District Court.

Appeals from the trial court run to the **Idaho Court of Appeals**
and the **Idaho Supreme Court** (five justices). Because the
District Court is unified, the **statewide Idaho Rules of Civil
Procedure (I.R.C.P.)** and **Idaho Rules of Evidence (I.R.E.)**
apply in every district. Each district layers its own **local
rules** on top.

## The seven judicial districts — directory

Confirm the controlling county's judicial district and its principal
courthouse, then confirm that district's current local rules and
iCourt status before relying on any specific.

| District | Seat / principal city | Counties |
|----------|-----------------------|----------|
| **First** | Coeur d'Alene (Kootenai) | Benewah, Bonner, Boundary, Kootenai, Shoshone |
| **Second** | Lewiston | Clearwater, Idaho, Latah, Lewis, Nez Perce |
| **Third** | Caldwell (Canyon) | Adams, Canyon, Gem, Owyhee, Payette, Washington |
| **Fourth** | Boise (Ada) — see `id-ada` | Ada, Boise, Elmore, Valley |
| **Fifth** | Twin Falls | Blaine, Camas, Cassia, Gooding, Jerome, Lincoln, Minidoka, Twin Falls |
| **Sixth** | Pocatello (Bannock) | Bannock, Bear Lake, Caribou, Franklin, Oneida, Power |
| **Seventh** | Idaho Falls (Bonneville) — see `id-bonneville` | Bingham, Bonneville, Butte, Clark, Custer, Fremont, Jefferson, Lemhi, Madison, Teton |

The most populous counties outside Ada and Bonneville — and the
districts that handle them — include **Canyon** (Third, Caldwell),
**Kootenai** (First, Coeur d'Alene), **Bannock** (Sixth,
Pocatello), **Twin Falls** (Fifth, Twin Falls), **Madison** (Seventh,
Rexburg), **Nez Perce** (Second, Lewiston), **Bingham** (Seventh,
Blackfoot), and **Bonner** (First, Sandpoint). Each is filed in its
own county's District Court within the listed judicial district.

## Confirm the district — and its local rules

**Do not assume one district's practice from another's.** Each
judicial district adopts **local rules** and standing administrative
orders governing motion practice, civil case management,
scheduling/trial-setting, chambers or judge copies, and assignment.
Look up the controlling county, its judicial district, and that
district's local rules through the Idaho Judicial Branch directory
at **isc.idaho.gov**.

**Agent behavior:** before drafting anything district-specific (a
Notice of Hearing, a trial-setting request, a page-limited
memorandum, a proposed form of order), confirm (1) which county and
judicial district the case is in, (2) that district's current local
rules and standing orders, and (3) its iCourt E-File status. Local
rules govern on top of the statewide I.R.C.P.

## Caption — generic District Court variant

```
       IN THE DISTRICT COURT OF THE [NTH] JUDICIAL DISTRICT
       OF THE STATE OF IDAHO, IN AND FOR THE COUNTY OF [COUNTY]

[PLAINTIFF],                       )
                                   )   Case No. ____________________
       Plaintiff,                  )
v.                                 )
                                   )
[DEFENDANT],                       )
       Defendant.                  )
___________________________________)
```

See `id-statewide-format` for the full I.R.C.P. 2 caption, the
attorney/party block with the **ISB number**, the title-of-court ≥
3"-from-top placement, and statewide drafting conventions. Confirm
the county's accepted civil case-type codes and the case-number
format with the clerk.

## Filing — iCourt E-File status

Idaho e-filing runs through **iCourt E-File** (Odyssey File & Serve),
governed by **I.R.E.F.S.** E-filing is **mandatory for attorneys**
(I.R.E.F.S. 4(a)) and **optional for self-represented individuals**
(I.R.E.F.S. 4(b)) — but a self-represented party who opts in is bound
to e-file for the life of the case. Confirm the controlling
district's iCourt acceptance details, the document-type selections,
and the fee / fee-waiver workflow before assembling a packet. See
`id-file-packet`.

## Composition

- For statewide format and the caption: `id-statewide-format`
- For the two flagship counties: `id-ada` (Boise / Fourth),
  `id-bonneville` (Idaho Falls / Seventh)
- For the first responsive pleading (21-day answer):
  `id-first-30-days`
- For drafting motions / declarations / notices / orders:
  `id-draft-motion`, `id-draft-declaration`, `id-draft-note`,
  `id-draft-order`
- For discovery and deadlines: `id-discovery`, `id-deadlines`
- For scheduling and filing: `id-schedule-hearing`, `id-hearings`,
  `id-file-packet`
- For family-law / Magistrate-Division family matters:
  `id-family-court`, `id-family-law`
- For pro se conventions: `id-pro-se`

## References

- `id-law-references` — I.R.C.P., I.R.E., I.R.E.F.S., Idaho Code
  (incl. I.C. § 1-2208 and § 1-2301), and the per-district
  local-rules corpus
- Idaho Judicial Branch directory (isc.idaho.gov) — confirm the
  county's judicial district, its local rules and standing orders,
  and its iCourt E-File status
