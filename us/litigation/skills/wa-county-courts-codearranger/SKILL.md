---
name: wa-county-courts-codearranger
title: Washington county courts (non-KCDC)
description: 'This skill should be used when drafting or filing civil documents in a Washington county court other than King County District Court — i.e., the district courts (and, secondarily, the superior court clerks) of the state''s most populous counties: Pierce (Tacoma), Snohomish (Everett / Lynnwood / Monroe / Arlington), Spokane, Clark (Vancouver), Thurston (Olympia), Kitsap (Port Orchard), Yakima, Whatcom (Bellingham), and Benton (Kennewick). Triggers include the county name plus "district court" / "superior court" / "where do I file" / "e-filing portal" / "LINX" / "local rules" / "civil motion calendar", or a case venued in one of those counties. For King County District Court use the dedicated `wa-kcdc` skill instead. Layer this on top of `wa-statewide-format`, and consult `wa-law-references` for the per-court LCR / LCRLJ local-rule text.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: District Court Directory
  path: references/district-court-directory.md
- title: Filing And Service
  path: references/filing-and-service.md
---

# Washington county courts (non-KCDC)

Use this skill in addition to `wa-statewide-format` when a civil matter is
venued in a Washington county **other than** King County District Court
(which has its own skill, `wa-kcdc`). It covers the courts of limited
jurisdiction — and the superior court clerks — of Washington's most
populous counties.

Most consumer-debt collection actions are filed in **district court**
(courts of limited jurisdiction, up to a $100,000 amount in controversy
under RCW 3.66.020; small claims up to $10,000). Larger matters, and some
debt cases filed there by choice, go to **superior court**. This skill
leads with the district court for each county and notes the superior court
clerk where it differs.

> **NOT LEGAL ADVICE.** This is a drafting and procedure aid. Court
> addresses, division assignments, e-filing portals, civil-calendar days,
> and local rules change without notice — verify every one against the
> court's own page (and the Washington Courts directory) before relying
> on it. Do not cache court-specific values across sessions.

## Canonical sources — pull current details every time

For *any* county court, these are the authoritative starting points:

- **Washington Courts directory** —
  `https://www.courts.wa.gov/court_dir/` — official address, phone,
  judges, and links for every court in the state. Use this to confirm a
  courthouse address or division before you put it in a caption.
- **Local rules (LCR for superior courts, LCRLJ / LCR for district
  courts)** — the `https://www.courts.wa.gov/court_rules/` page links out
  to "Superior Court Rules" / "District Court Rules" / "Municipal Court
  Rules", and *those* pages list the local-rule sets court by court; many
  courts also post their own local rules on their own site, and the clerk
  of court keeps the authoritative copy. Read the county's local rules
  for filing format, working-copy requirements, motion-confirmation
  deadlines, and the civil motion calendar. (Note: the in-repo
  `wa-law-references/references/court-rules/` corpus carries the
  **statewide** rule sets — CR, CRLJ, ER, GR, RAP, etc. — not the
  per-county local rules; pull those live.)
- The **county court's own website** (linked from each entry below) for
  the live e-filing portal, current civil-calendar dates, and
  division-specific note/scheduling forms.

**Agent behavior**: when you draft a caption, a note for a hearing, or a
filing packet for one of these courts, fetch the current courthouse
address, division assignment, e-filing instructions, and civil-calendar
day from the sources above. Treat anything hardcoded in this skill as a
pointer, not as ground truth.

## Caption — county-court variants

District court (limited jurisdiction):

```
        [COUNTY] COUNTY DISTRICT COURT[, [DIVISION] DIVISION]
            IN AND FOR THE STATE OF WASHINGTON
```

Superior court (general jurisdiction):

```
   IN THE SUPERIOR COURT OF THE STATE OF WASHINGTON
            IN AND FOR [COUNTY] COUNTY
```

Confirm the exact division line (some districts have multiple physical
divisions — see Snohomish below) from the court's website before filing,
and put the cause number on the right side of the caption directly below
"No." Cause-number formats vary by county and by case-management system;
do not invent one — copy it from the summons/complaint you were served, or
from the clerk's confirmation.

## County-by-county quick reference

The detailed entries — courthouse addresses, divisions, e-filing portals,
and known local-practice notes — live in
`references/district-court-directory.md`. Summary:

| County (≈2025 pop.) | District court seat | E-filing system | Notes |
|---|---|---|---|
| **King** (2.29M) | — | — | **Use the `wa-kcdc` skill.** |
| **Pierce** (930k) | Tacoma | **LINX** (reached from `piercecountywa.gov/374/E-Filing`) — e-filing is mandatory under PCLGR 30 / PCLR 30 for most filers | Check the current civil motion docket / confirmation rule |
| **Snohomish** (844k) | Everett (plus South/Lynnwood, Evergreen/Monroe, Cascade/Arlington divisions) | County e-filing portal | File in the **division** assigned to the case |
| **Spokane** (549k) | Spokane (Public Safety Bldg) | County e-filing portal | — |
| **Clark** (517k) | Vancouver | Clark County Odyssey/eFile portal | — |
| **Thurston** (~300k) | Olympia (Building 3, Lakeridge Dr SW) | County e-filing portal | — |
| **Kitsap** (~280k) | Port Orchard (614 Division St) | County e-filing portal | — |
| **Yakima** (~258k) | Yakima (courthouse, 2nd St) + Grandview branch | County e-filing portal | Two physical locations |
| **Whatcom** (~232k) | Bellingham (311 Grand Ave) | County e-filing portal | — |
| **Benton** (~213k) | Kennewick | County e-filing / NCourt for fees | Benton & Franklin share a superior court |

Population figures are from the Washington Office of Financial Management
April 2025 estimates and are included only to scope "most populous" — they
are not used for anything procedural.

## Filing workflow — what's the same everywhere

Regardless of county, a noted civil motion in a Washington court of limited
jurisdiction travels as a packet (this mirrors `wa-kcdc` and the
`wa-file-packet` skill):

1. **Motion** (primary relief)
2. **Supporting memorandum** (only if the motion isn't self-contained)
3. **Supporting declaration(s)** with exhibits
4. **Proposed order**
5. **Note for civil motion calendar / docket** (the county's scheduling
   form — pull the current version from that court's site)
6. **Certificate / declaration of service** (CRLJ 5 in district court,
   CR 5 in superior court)

E-file each as a separate PDF through that county's portal, serve opposing
counsel the same day by a CRLJ 5 / CR 5 method, and check the county's
local rules for whether **working copies** are required (superior courts
usually require them; most district courts do not, but some do for longer
motions).

## What's different — read the local rules

Things that genuinely vary county to county, and where to find them:

- **How you get a hearing date.** Some courts let you self-note onto a
  published civil calendar; others require an emailed date request to a
  calendar clerk first (KCDC-style). Check the county's local rules and
  civil-calendar page.
- **Motion confirmation.** Many superior courts require the moving party
  to *confirm* a contested hearing a set number of days out, or it's
  struck. District courts vary. The county's LCR/LCRLJ says.
- **E-filing mandate vs. option.** Pierce County mandates e-filing for
  most filers (PCLGR 30 / PCLR 30); others permit but don't require it.
- **Division/venue within the county.** Snohomish County District Court
  has four physical divisions; file in the one assigned to the case.
  Yakima County District Court has a Yakima courthouse and a Grandview
  branch.
- **Cause-number format and document codes.** Driven by the county's
  case-management system (LINX in Pierce, Odyssey/JIS elsewhere). Copy the
  format from the served pleadings or the clerk; don't construct one.

When in doubt, the controlling text is that county's local rules — pull
the current set from `https://www.courts.wa.gov/court_rules/` (District / Superior /
Municipal Court Rules link → court-by-court list) or the court's own site
— read alongside the statewide CRLJ / CR (which *are* mirrored in
`wa-law-references/references/court-rules/`).

## References

- `references/district-court-directory.md` — per-county courthouse
  addresses, divisions, e-filing portals, official-page links, and
  known local-practice notes
- `references/filing-and-service.md` — the cross-county packet, service,
  and working-copy checklist, with pointers into the statewide rules
