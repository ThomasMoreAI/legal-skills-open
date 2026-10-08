---
name: wa-family-court-codearranger
title: Washington Family Court — Venue Mechanics
description: Use when handling a Washington family-law matter at the trial-court level — the Superior Court Family Law Department. Washington has no separate Family Court trial court; family matters sit inside the general-jurisdiction Superior Court but are administered by a dedicated Family Law Department in most counties. Triggers include "Washington family court", "family law facilitator", "AOC family forms", "dissolution petition", "parenting plan filing", "family court commissioner", "King County Family Law", "Pierce County Family Law", "family-law local rules". Coverage includes mandatory AOC forms under GR 31, county-specific intake procedures, case-scheduling deadlines, the family-court commissioner system (RCW 2.24), mandatory parenting seminars, GAL appointment, and civil protection orders (RCW 7.105).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Washington Family Court — Venue Mechanics

> **NOT LEGAL ADVICE.** Family-law procedure varies
> materially by county. This skill names the controlling
> sources for venue mechanics; **current case-scheduling
> deadlines, revision-motion windows, and county-rule
> day counts live in the references corpus** (county
> local rules under `court-rules/`, RCW 2.24 under
> `wa-rcw-debt/`). Verify the assigned Superior Court
> Family Law Department's local rules + standing orders
> before filing.

## At a glance

Washington has **no separate Family Court trial court**.
Family-law matters are heard by the **general-
jurisdiction Superior Court** in each county,
administered by a dedicated **Family Law Department** in
larger counties.

- **Forum**: Superior Court (RCW 2.08 jurisdiction)
- **Trial-rules**: General **CR** + **GR** + each
  county's **Local Rules** (LR)
- **Forms**: Mandatory **AOC forms** under **GR 31** —
  the Administrative Office of the Courts publishes
  unified family-law forms for statewide use
- **Decisionmakers**: Family Court Commissioners (under
  RCW 2.24 — for ex parte, motions, contempt, protection
  orders) + Superior Court Judges (for trials)

## County-by-county architecture

| County | Family Law Dept | Family Law Facilitator | Mandatory Parenting Seminar |
|---|---|---|---|
| King | Maleng Regional Justice Center (Kent) + Seattle | Yes — King County Pro Se | Yes — local rule |
| Pierce | County-City Building (Tacoma) | Yes | Yes |
| Snohomish | Mission Building (Everett) | Yes | Yes |
| Spokane | Spokane County Courthouse | Yes | Yes |
| Clark | Vancouver | Yes | Yes |
| Thurston | Olympia | Yes | Yes |
| Kitsap | Port Orchard | Yes | Yes |
| Whatcom | Bellingham | Yes | Yes |
| Yakima | Yakima | Yes | Yes |
| Other 30 counties | Roll-up via `wa-county-courts` | Varies | Varies |

## AOC family-law forms — GR 31

Washington courts require the use of **AOC mandatory
forms** for family-law filings. The forms are published
at https://www.courts.wa.gov/forms/ and updated
periodically (most recent comprehensive update: 2020
plain-language overhaul).

### Form series

| Series | Coverage |
|---|---|
| **FL Divorce** | Dissolution / legal separation / annulment |
| **FL All Family** | Forms used across multiple case types — parenting plan, child support, financial declaration |
| **FL Parentage** | Parentage / paternity cases under RCW 26.26A |
| **FL Domestic Violence** | DV / family-violence civil protection orders under RCW 7.105 (formerly RCW 26.50) |
| **FL Modify** | Modification of decree / order |
| **FL Non-Parental Custody** | Non-parental custody actions (now generally under RCW 26.09 third-party framework) |

### Mandatory use

Under GR 31, parties **must** use the AOC mandatory form
where one exists — non-conforming filings can be
rejected by the clerk. Customization is limited to
adding facts and signatures.

## Case scheduling — county-by-county

Each county's family-law local rules set the case-
scheduling timeline (status conference, discovery
cutoff, pretrial, trial). **Specific deadlines vary by
county and are amended periodically** — read the
assigned county's local rules from
`wa-law-references/references/court-rules/` rather than
relying on memory.

### King County

- King County Local Rule 5 + King County Family Law
  Local Rules
- Standing Order on Temporary Family Law Orders prevents
  property transfers / changing insurance / moving with
  children pending hearing
- Joint Case Status Conference scheduled by local-rule
  default (current deadline per KCFLR — read from court-
  rules corpus)

### Pierce County

- Pierce County Local Rules of Superior Court, Family
  Law division
- Status conference set on filing (timing per PCLR)
- Mandatory mediation in most contested cases under PCLR

### Snohomish County

- Snohomish County Local Rules + standing orders
- Family law commissioners handle motions (timing per
  SCLR)

### Spokane County

- Spokane Local Rules + Family Court track
- Status conference + mediation orientation (timing per
  SLR)

## Family-Law Facilitator — RCW 26.12.180

Each county's Superior Court is **required** by RCW
26.12.180 to provide a **Family Law Facilitator** who:

- Helps pro-se parties understand forms + procedure
- Cannot give legal advice (procedural information only)
- Available at courthouse during set hours

For King County: **King County Family Law Facilitator**
at MRJC + Seattle courthouses.

## Commissioners — RCW 2.24

Family Court Commissioners (under RCW 2.24.040) handle:

- Ex parte applications + temporary restraining orders
- Motions (temporary support, temporary parenting,
  contempt)
- Civil protection orders under RCW 7.105
- Default decrees on uncontested dissolutions
- Contempt hearings

**Revision motion** — any party may move to revise a
commissioner's ruling under RCW 2.24.050. **Read the
current revision-motion window from
`wa-law-references/references/wa-rcw-debt/RCW-2_24.md`**
or hand off to `wa-deadlines`. The motion is heard by a
Superior Court Judge.

## Guardian ad Litem — RCW 26.12.175 + CR 17(c)

When parenting issues are contested + children's
interests need separate representation:

- Court appoints **GAL** under RCW 26.12.175 (for
  family-law cases) or **CR 17(c) GAL** (general civil
  rules — incapacitated parties)
- WA also has the **WA State GAL Program** training and
  certification system
- GAL fees split between parties (or assessed against
  one based on conduct)
- GAL reports + recommendations admissible at trial
  with cross-examination

## Mandatory parenting seminars — county-rule

Most counties require parties to a contested parenting
case to complete a **parenting seminar** before final
orders. Class length and curriculum vary by county
(typically 4 hours; "What About the Children" or
equivalent). Check the county's family-law local rules
for the current requirement.

## Civil protection orders — RCW 7.105

As of 2022, **RCW 7.105 consolidates** six former
chapters' civil-protection-order regimes (DV / sexual
assault / stalking / harassment / vulnerable-adult /
extreme-risk). Jurisdiction:

- **Superior Court**: DV, sexual assault, vulnerable
  adult (and most other categories)
- **District Court**: anti-harassment, stalking (can be
  Superior Court if requested)

The Family Court Commissioner usually hears initial
protection-order applications at Superior Court. **Read
current ex-parte / full-hearing / duration day counts
from `RCW-7_105.md`** rather than relying on memory.

## Composition with other wa- skills

- `wa-family-law` — substantive family-law framework
- `wa-statewide-format` — GR 14 + AOC forms compliance
- `wa-pro-se` — pro-se framework + Facilitator referral
- `wa-deadlines` — county-rule case-scheduling deadlines
  + RCW 2.24.050 revision-motion window + RCW 7.105
  hearing windows
- `wa-kcsc` / `wa-pierce` / `wa-snohomish` / `wa-spokane`
  — county-specific overlays
