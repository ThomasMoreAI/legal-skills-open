---
name: in-family-court-codearranger
title: Indiana Family Court — Venue Mechanics
description: 'Use for Indiana family-court matters — paternity (**JP case**), dissolution (**DC/DN**), child support (**DR**), custody / parenting time, adoption (**AD**), CHINS (**JC**), delinquency (**JD**). Indiana has **no separate Family Court**; family matters are heard by Circuit or Superior Court, with juvenile routed to a **Juvenile Division** in large counties (Marion, Lake, Allen, Hamilton) or **Circuit Court directly** in smaller counties (Bartholomew). Covers Odyssey case-type codes, paternity under **IC 31-14**, juvenile jurisdiction at **IC 31-30**, and county-by-county routing. Triggers: "Indiana family court", "IN paternity", "JP case", "IC 31-14", "IN juvenile court", "IN CHINS", "IN dissolution".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Indiana Family Court — Venue Mechanics

> **NOT LEGAL ADVICE.** Family-law procedure varies
> materially by county in Indiana — which division of the
> Circuit / Superior Court hears each case type, what
> local family-law rules apply, and what the standing
> orders require. This skill names the controlling
> sources for venue mechanics; **current statutory text,
> day counts, and per-county routing live in the
> references corpus** (county-rule references in
> `in-law-references/references/court-rules/`, IC 31
> chapters in `in-law-references/references/in-statutes-
> debt/`). Verify the assigned court's local rules +
> standing orders before filing.

## At a glance

Indiana has **no separate Family Court trial court**.
Family-law matters are heard by the **general-
jurisdiction Circuit Court or Superior Court** in each
county. Indiana's family-law topology depends on county
size:

- **Large urban counties** (Marion, Lake, Allen,
  Vanderburgh, Hamilton, St. Joseph) have a dedicated
  **Juvenile Division** or specialized **Juvenile Court**
  that hears JP / JC / JD / JS / JM / JT cases. Domestic
  Relations cases (DC / DN / DR) route to a Domestic
  Relations Division. Adoption may sit in the Probate
  Court (St. Joseph) or in a designated Superior Court.
- **Mid-sized + small counties** (most of Indiana's 92
  counties) consolidate family-law jurisdiction in the
  **Circuit Court** or one of the Superior Courts. The
  same judge may hear DC / JP / JC cases on the same
  calendar. **Bartholomew County** is in this category —
  Bartholomew Circuit Court hears JP cases directly.
- **Monroe County** is structurally unusual: 10 Circuit
  Court Divisions (no Superior Court at all); family-law
  cases distribute across divisions.

## Indiana case-type codes — the family / juvenile slice

Indiana's Odyssey case-management system identifies every
case by a **county-letter-number** identifier (e.g.,
`03C01-2501-JP-000123`). The middle two-letter code
identifies the case type. For family / juvenile cases:

| Code | Case type |
|---|---|
| **DC** | Dissolution **with** Children |
| **DN** | Dissolution **with No** Children (or no minor children) |
| **DR** | Domestic Relations Miscellaneous (modifications, child-support enforcement, post-decree) |
| **AD** | Adoption |
| **GU** | Guardianship (including guardianship of a minor) |
| **JC** | Juvenile CHINS (Children In Need of Services) |
| **JD** | Juvenile Delinquency |
| **JM** | Juvenile Miscellaneous |
| **JP** | **Juvenile Paternity** — establishes paternity + opens custody / support / parenting orders for a non-marital child |
| **JS** | Juvenile Status (truancy, runaway, incorrigible) |
| **JT** | Juvenile Termination of Parental Rights |
| **PO** | Protection Order (Order of Protection under IC 34-26-5) |

The case-type code prefixes everything that follows in the
case caption + Odyssey docket. A JP case filed in
Bartholomew Circuit Court would carry a caption like
`Cause No. 03C01-YYYYY-JP-NNNNNN`.

## Chapter pointers (family + juvenile)

| Topic | Article | Reference file |
|---|---|---|
| Paternity (JP case-type backbone) | IC 31-14 | `IC-31-14.md` |
| Dissolution / annulment / legal separation | IC 31-15 | `IC-31-15.md` |
| Child support | IC 31-16 | `IC-31-16.md` |
| Custody and parenting time | IC 31-17 | `IC-31-17.md` |
| Adoption | IC 31-19 | `IC-31-19.md` |
| UCCJEA | IC 31-21 | `IC-31-21.md` |
| Department of Child Services (DCS) | IC 31-25 | `IC-31-25.md` |
| Juvenile Court jurisdiction | IC 31-30 | `IC-31-30.md` |
| Juvenile Court procedure | IC 31-32 | `IC-31-32.md` |
| Children In Need of Services (CHINS) | IC 31-34 | `IC-31-34.md` |
| Juvenile delinquency / status | IC 31-37 | `IC-31-37.md` |
| Protection Orders | IC 34-26-5 | `IC-34-26.md` |
| Indiana Superior Courts (statutory framework) | IC 33-29 | `IC-33-29.md` |

For specific subsection numbers, current dollar thresholds
(combined-income cap for child-support guidelines,
adoption-fee figures, etc.), and day counts (filing
deadlines, summons / response periods, hearing windows,
modification thresholds), **read the relevant chapter
file**.

## Paternity (JP cases) — procedural framework

A JP filing under IC 31-14 establishes the legal father of
a child born out of wedlock and opens orders for custody,
parenting time, and support. Mechanical steps:

1. **Verified petition** filed in the Juvenile Court (or
   Circuit Court directly in counties without a separate
   juvenile docket) — typically by the mother, the
   alleged father, the child, or a prosecutor / DCS where
   public assistance is involved. Filed in the county of
   the mother's residence, the alleged father's
   residence, or the child's birth/residence (IC 31-14-4-1
   et seq. — see chapter file for the venue framework).
2. **Service** on the respondent under Trial Rule 4 (with
   special service rules for paternity affidavits).
3. **Answer / response** within the Trial Rule 6 / 12
   response window — see `in-deadlines`.
4. **Genetic testing** under the IC 31-14-6 framework if
   paternity is contested; results raise a statutory
   presumption.
5. **Final order** — establishes legal father; sets
   custody, parenting time per the Indiana Parenting
   Time Guidelines (a court rule, not statute), and
   child support per the Indiana Child Support Guidelines
   (also a court rule).
6. **Modification** available on substantial change of
   circumstances under IC 31-16-8 (child support) or IC
   31-17-2-21 / IC 31-14-13-6 (custody / parenting).

### Bartholomew County (03) — Columbus

Bartholomew County does NOT have a separate Juvenile
Division — **Bartholomew Circuit Court (03C01)** hears JP
cases directly along with the rest of its family-law
docket. Court address: 234 Washington Street, Columbus,
IN 47201. Local rules: LR03 series. The two Bartholomew
Superior Courts (03D01-D02) handle other case types
(civil collections, misdemeanor criminal, small claims).

When the user's matter is a JP case in Bartholomew,
expect:

- Cause-number format: `03C01-YYYYY-JP-NNNNNN`
- Forum: Bartholomew Circuit Court (Circuit Judge, not a
  Juvenile Magistrate)
- E-filing: Odyssey statewide e-filing system (mandatory
  for represented parties; pro-se filers may use paper or
  e-file via the public portal at `mycase.in.gov`)

## Larger-county routing

For comparison, the larger-county family-law topology:

### Marion County (49) — Indianapolis

- **Marion Superior Court — Juvenile Division** (49D08 +
  Courtrooms 30-33 at the Juvenile Justice Center) hears
  JP / JC / JD / JS / JM / JT cases
- **Marion Superior Court — Domestic Relations Divisions**
  hear DC / DN / DR cases (Courtrooms 12-29; sub-numbering
  for custody / paternity / support)
- **Marion Superior Court — Probate Division** (49D08) for
  adoption + guardianship

### Lake County (45) — Crown Point

- **Lake Superior Court — Juvenile Division** (45D04)
  hears JP / JC / JD / JS / JM / JT
- **Lake Superior Court — County Division** for domestic
  relations

### Allen County (02) — Fort Wayne

- **Allen Superior Court 8** (02D08) — Family Relations
- **Allen Superior Court 9** (02D09) — Juvenile

### Hamilton County (29) — Noblesville

- Hamilton Superior Courts 4-7 split between criminal and
  family law (29D04-D07)

### St. Joseph County (71) — South Bend

- **St. Joseph Probate Court** (71J01) — distinct probate
  court that hears adoption + juvenile + guardianship

For the rest of Indiana's 92 counties, the rule is
generally: Circuit Court hears JP / JC / DC unless a
specific Superior Court has been designated for one of
those case types. Check the county's local rules at
LR<NN> in the `in-law-references/references/court-rules/`
corpus.

## Forms

Indiana publishes **state-approved family-law forms**
through the Indiana Supreme Court's Self-Service Center
at `courts.in.gov/help/self-service`. The form catalog
covers:

- Petition to Establish Paternity (JP cases)
- Verified Petition for Dissolution (DC / DN cases)
- Petition for Modification of Custody / Parenting Time /
  Child Support
- Child Support Obligation Worksheet (per the Indiana
  Child Support Guidelines)
- Indiana Parenting Time Guidelines acknowledgment

Forms are NOT mandatory in Indiana (unlike Washington's
AOC GR 31 regime) — a properly-pleaded substitute can be
filed in lieu of the state form. But the state forms are
the canonical safe-harbor structure.

## DCS / CHINS overlap

When the Indiana Department of Child Services (DCS,
statutory backbone at IC 31-25) becomes involved, the
family-law matter often runs in parallel with a CHINS
proceeding under IC 31-34. Critical points:

- A CHINS adjudication does NOT terminate parental rights;
  TPR is a separate JT proceeding under IC 31-35
- CHINS hearings, fact-finding, and disposition follow
  the IC 31-34 + IC 31-32 framework
- Indigent parents have a right to assigned counsel in
  CHINS / TPR proceedings (see chapter file)

## Composition with other in- skills

- `in-family-law` — substantive family-law framework
- `in-statewide-format` — caption + Trial Rule 5(E)
  formatting + Indiana cause-number conventions
- `in-discovery` — Trial Rule 26-37 discovery (applied to
  family-law matters)
- `in-deadlines` — Trial Rule 6 + Indiana legal-holiday
  list; family-court-specific deadlines (paternity-
  affidavit windows, modification thresholds) live in
  the IC 31 chapters
- `in-pro-se` — pro-se framework; Indiana lacks a
  family-law-facilitator equivalent, so pro-se family
  filers rely on the Self-Service Center + court clerks
  (clerks cannot give legal advice)
- `in-county-courts` — per-county routing detail (e.g.,
  the Bartholomew Circuit Court entry for JP cases)
- `in-marion` / `in-lake` — flagship-county overlays
- `in-fact-check` — citation verification
