---
name: in-family-law-codearranger
title: Indiana Family Law — Subject-Matter Bundle
description: 'Use for Indiana family-law substantive matters — paternity (**IC 31-14**), dissolution/annulment/legal separation (**IC 31-15** — **equitable distribution, NOT community property**), child support (**IC 31-16** + **Indiana Child Support Guidelines**), custody/parenting time (**IC 31-17** + **Indiana Parenting Time Guidelines**), adoption (**IC 31-19**), UCCJEA (**IC 31-21**), CHINS (**IC 31-34**), TPR (**IC 31-35**), and protection orders (**IC 34-26-5**). Reference corpus holds current statutory text, thresholds, and subsection detail. Triggers: "Indiana divorce", "IN paternity", "IC 31-14", "Indiana child support", "IC 31-16", "IN custody", "IN equitable distribution".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Indiana Family Law — Subject-Matter Bundle

> **NOT LEGAL ADVICE.** Indiana family-law statutes are
> amended regularly; the Indiana Child Support Guidelines
> and Indiana Parenting Time Guidelines (both published
> as Indiana Supreme Court rules) are revised on a
> rolling basis. This skill names the controlling
> chapters and describes doctrinal frameworks; **current
> statutory text, dollar thresholds, day counts, combined-
> income caps, and section-level rules live in the
> references corpus** at `in-law-references/references/
> in-statutes-debt/` and `in-law-references/references/
> court-rules/`. Verify before relying on any specific
> figure.

## At a glance — Indiana's family-law architecture

- **Substantive code**: **IC Title 31** (Family and
  Juvenile Law) — Indiana's consolidated family / juvenile
  code, with civil-procedure overlay from the Indiana
  Trial Rules and special-action statutes at IC 34-26
  (protection orders).
- **Court rules**: the **Indiana Child Support Guidelines**
  (a court rule with detailed worksheets and a combined-
  income schedule) and the **Indiana Parenting Time
  Guidelines** (a court rule with default residential-
  time schedules by age cohort) supply the day-to-day
  practitioner framework for support + parenting cases.
- **Marital property regime**: **equitable distribution**
  under IC 31-15-7. Indiana is NOT a community-property
  state. The statute creates a rebuttable presumption of
  equal division.
- **Child-support model**: **income-shares** under the
  Indiana Child Support Guidelines (court rule), keyed to
  combined weekly adjusted gross income; with a statutory
  cap above which the court has discretion.
- **Forum**: Circuit Court or Superior Court (general-
  jurisdiction trial court) — see `in-family-court` for
  per-county venue topology.

## Chapter pointers (substantive)

| Topic | Article | Reference file |
|---|---|---|
| Paternity (JP cases) | IC 31-14 | `IC-31-14.md` |
| Dissolution / annulment / legal separation | IC 31-15 | `IC-31-15.md` |
| Child support | IC 31-16 | `IC-31-16.md` |
| Custody and parenting time | IC 31-17 | `IC-31-17.md` |
| Adoption | IC 31-19 | `IC-31-19.md` |
| UCCJEA | IC 31-21 | `IC-31-21.md` |
| Department of Child Services | IC 31-25 | `IC-31-25.md` |
| Juvenile court jurisdiction | IC 31-30 | `IC-31-30.md` |
| Juvenile court procedure | IC 31-32 | `IC-31-32.md` |
| Children In Need of Services | IC 31-34 | `IC-31-34.md` |
| Juvenile delinquency / status | IC 31-37 | `IC-31-37.md` |
| Protection orders | IC 34-26-5 | `IC-34-26.md` |

For residency requirements, waiting periods, combined-
income caps, modification-threshold percentages, specific
factor enumerations, and day counts, **read the relevant
chapter file**. Don't rely on memory.

## Paternity — doctrinal framework

IC 31-14 governs the establishment of paternity for
children born out of wedlock and the orders that follow
(custody, parenting time, support). Paternity matters
file as **JP case-type** in the county's Juvenile Court
or Circuit Court.

### Methods of establishment

- **Paternity affidavit** — executed in the hospital at
  birth or later through the State Department of Health;
  carries statutory effect as an acknowledgment of
  paternity. Rescission window is short (see chapter
  file).
- **Judicial action** — a verified petition under IC
  31-14, available to the mother, the alleged father, the
  child (through a next friend), the prosecutor, or DCS
  where public assistance is involved.
- **Genetic testing** — IC 31-14-6 sets the framework. A
  test result above the statutory threshold creates a
  rebuttable presumption of paternity.

### Who can file + where

Venue is broader than typical Trial Rule 75 venue: a
paternity action can be filed in the county of the
mother's residence, the alleged father's residence, OR
the child's birth / residence. See `IC-31-14.md` for the
full venue framework.

### Effect of establishment

A paternity adjudication establishes the legal father
and opens orders for:

- Custody (initial determination)
- Parenting time (per the Indiana Parenting Time
  Guidelines, with court-ordered deviations)
- Child support (per the Indiana Child Support
  Guidelines)
- The child's right to inherit + claim benefits through
  the father
- The father's right to seek custody / parenting time

### Statutory presumption favoring biological mother

Indiana law historically created a presumption in favor
of placing custody of a non-marital child with the
biological mother. The presumption is rebuttable on the
best-interests factors at IC 31-17-2-8 + the paternity-
specific factors at IC 31-14-13-2. **Read the chapter
file for the current presumption framework + factor
enumeration.**

## Dissolution — procedural framework

IC 31-15 governs divorce, annulment, and legal
separation. Mechanical steps:

1. Verify petitioner's Indiana residency (county
   residency requirement)
2. File Verified Petition for Dissolution (state form
   available, not mandatory)
3. Serve respondent under Trial Rule 4
4. Mandatory waiting period before final hearing (see
   chapter file for current period)
5. Mandatory financial disclosures
6. Provisional orders (custody / support / restraints)
   on motion
7. Mediation where ordered (no statewide mandatory
   mediation, but most counties order it by local rule)
8. Final hearing → Decree

### No-fault

Indiana is a no-fault state. The statutory ground is
**irretrievable breakdown of the marriage**. Fault
grounds (impotence, conviction of an infamous crime,
incurable insanity for 2 years) remain technically
available but are rarely used. See `IC-31-15.md`.

### Equitable distribution — IC 31-15-7

IC 31-15-7 establishes the equitable-distribution
framework with a **rebuttable presumption of equal
division**. The presumption is rebutted by application of
the factors at IC 31-15-7-5 (contributions, economic
circumstances, dissipation, etc.). Unlike community-
property states, Indiana includes both marital + non-
marital property in the divisible pool, subject to
characterization arguments.

For the factor enumeration and the contribution / 
dissipation / economic-circumstances analysis, see
`IC-31-15.md`.

## Child support — Indiana Child Support Guidelines

Indiana child support is calculated under the **Indiana
Child Support Guidelines**, an Indiana Supreme Court
rule with detailed worksheets (Worksheet A for sole-
custody cases; Worksheet B for shared-physical-custody
cases). The statutory backbone is IC 31-16.

### Calculation framework

1. Determine each parent's **weekly gross income** (broad
   definition; includes wages, salary, commissions,
   bonuses, self-employment income, investment income,
   government benefits)
2. Subtract guideline deductions (other court-ordered
   support, prior-born children, health insurance,
   etc.) to reach **weekly adjusted gross income**
3. Sum to **combined weekly adjusted gross income**
4. Look up the basic child support obligation on the
   guideline schedule
5. Apply each parent's pro rata share
6. Apply parenting-time credit (Worksheet B) for shared-
   physical-custody cases (using the parenting-time-
   credit table indexed to annual overnights)
7. Apply additional credits (uninsured medical, work-
   related childcare)

**Combined-income cap**: above the schedule's upper
bound, the court has discretion to extrapolate or apply
the percentage of the parents' combined income at the
top of the schedule. **Read the current cap from the
Indiana Child Support Guidelines** (in
`court-rules/Indiana-Child-Support-Guidelines.md` once
the corpus is populated; pointer-stub for now).

### Modification

Modification under IC 31-16-8 requires a **substantial
and continuing change of circumstances**. Indiana has a
statutory shortcut: a recalculation under the Guidelines
that differs from the existing order by a defined
percentage threshold creates a presumption of substantial
change. **Read the current threshold from `IC-31-16.md`.**

## Custody and parenting time — IC 31-17

### Best-interests factors

IC 31-17-2-8 enumerates the best-interests factors the
court considers when making the initial custody
determination + parenting-time order. For the full
enumeration, see `IC-31-17.md`. Common categories:

- Wishes of parents
- Wishes of child (with age-dependent weight)
- Child's interaction + relationships
- Adjustment to home / school / community
- Mental + physical health
- Evidence of domestic / family violence
- Evidence of de facto custodian status (post-2002
  amendment recognizing non-parent caregivers)

### Indiana Parenting Time Guidelines

The **Indiana Parenting Time Guidelines** (a court rule)
publish default residential-time schedules by age cohort
(infant 0-3 / toddler 3-5 / school-age 5-13 /
adolescent 13+). Courts presumptively apply the
Guidelines unless deviation is in the child's best
interests. Both the standard schedule and the shared-
custody worksheet feed into the child-support Worksheet B
calculation.

### Relocation

IC 31-17-2.2 governs relocation by a custodial parent.
Notice to the non-relocating parent is required; the
non-relocating parent may object; the court applies the
best-interests factors + relocation-specific factors.
For the notice-period day count and the relocation-
specific factors, see `IC-31-17.md`.

## Adoption — IC 31-19

Indiana adoption proceedings file as **AD case-type**.
Available paths:

- **Direct placement adoption** — birth parents place
  with adoptive parents directly
- **Agency adoption** — through a licensed child-placing
  agency
- **Stepparent adoption** — IC 31-19-15 (streamlined)
- **Adult adoption** — IC 31-19-1
- **Foster-parent adoption** — IC 31-19-2 + DCS
  coordination

Common procedural anchors:

- Consent of biological parents (or termination of
  parental rights via JT case)
- Indian Child Welfare Act (ICWA) applicability check
- Home study by licensed agency
- Background checks
- Adoption hearing → Decree

See `IC-31-19.md` for procedural specifics.

## UCCJEA — IC 31-21

Indiana's enactment of the Uniform Child Custody
Jurisdiction and Enforcement Act. **Home-state
jurisdiction** governs initial custody determinations:

- "Home state" = state where child lived with parent for
  6 consecutive months before commencement (or since
  birth if less than 6 months old)
- Emergency jurisdiction for child present in IN + needs
  protection
- Continuing exclusive jurisdiction once initial order
  entered

For the home-state definition, emergency-jurisdiction
mechanics, and the continuing-exclusive-jurisdiction
framework, see `IC-31-21.md`.

## CHINS + TPR — IC 31-34 + IC 31-35

When DCS (IC 31-25) becomes involved, the case file in
the Juvenile Division (or Circuit Court directly in
counties without a separate Juvenile Court) as a **JC
case-type** under IC 31-34.

### CHINS procedural framework

1. **Preliminary inquiry / fact-finding** by DCS
2. **Petition** filed by DCS or prosecutor; case docketed
3. **Initial hearing** — informal-adjustment vs. formal-
   adjudication paths
4. **Fact-finding hearing** → adjudication
5. **Dispositional hearing** → disposition (home with
   services, removal, foster care, etc.)
6. **Periodic review** (every 6 months)
7. **Permanency planning** (within 12 months of removal)
8. **Termination of parental rights (TPR)** at IC 31-35
   if reunification fails — separate JT case

### Right to counsel

Indigent parents have a right to assigned counsel in
CHINS and TPR proceedings. The court appoints CASA
(Court Appointed Special Advocate) or GAL for the child.
See `IC-31-32.md` and `IC-31-34.md` for the procedural
framework.

## Juvenile delinquency / status offenses — IC 31-37

Distinct from CHINS — **JD cases** address acts that
would be a crime if committed by an adult; **JS cases**
address status offenses (truancy, runaway, incorrigible).
The procedural framework lives in IC 31-37 + IC 31-32.

## Protection orders — IC 34-26-5

Indiana's civil protection orders file as **PO case-type**
under IC 34-26-5 (NOT IC 31). Available:

- DV protection order (qualifying intimate-partner /
  household relationship)
- Stalking / repeat-violation protection order
- Workplace violence protection order (for employers
  seeking on behalf of employees)

Ex parte temporary order on showing of immediate /
present danger; full hearing within the statutory window;
final order duration set by statute (renewable). For
qualifying relationships, hearing-window day count, and
order duration, see `IC-34-26.md`.

## Common-law marriage

Indiana **does not recognize common-law marriage**
(abolished by statute decades ago). Indiana will honor a
common-law marriage validly created in another
jurisdiction that recognizes it (under conflict-of-laws
principles).

## Composition with other in- skills

- `in-family-court` — venue mechanics + per-county
  routing (including Bartholomew Circuit Court for JP
  cases)
- `in-statewide-format` — Trial Rule 5(E) format
- `in-discovery` — Trial Rule 26-37 discovery
- `in-post-judgment` — modification + enforcement
- `in-pro-se` — pro-se framework
- `in-fact-check` — citation verification
