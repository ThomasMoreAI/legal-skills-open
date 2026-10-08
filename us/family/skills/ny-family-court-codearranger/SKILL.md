---
name: ny-family-court-codearranger
title: New York Family Court (Family Court Act / 22 NYCRR Part 205)
description: Use when drafting or filing in New York Family Court — the specialized trial court handling child custody, visitation, child support, paternity, juvenile delinquency, PINS, abuse/neglect (Article 10), family-offense / orders of protection. Triggers include 'NY Family Court', 'Family Court Act', 'FCA Article 4', 'FCA Article 8', 'CSSA child support', 'CSSA 17% basic', 'Family Court custody', 'family offense petition', 'PINS petition'. Covers **Child Support Standards Act (CSSA)** at FCA § 413 (17/25/29/31/35%, $183k cap); **best-interests** custody framework; **Article 10 abuse/neglect** with ACS (NYC) / DSS; **Article 8 family-offense** Orders of Protection; **paternity** under Article 5; **Article 3 juvenile delinquency** with Raise-the-Age; and the **Support Magistrate** + referee structure. NOT for divorce / matrimonial property (Supreme Court Matrimonial Part) or adoptions of adults.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# New York Family Court (Family Court Act / 22 NYCRR Part 205)

> **NOT LEGAL ADVICE.** Family Court matters have strict
> procedural rules, court-appointed-counsel rights, and
> interplay with parallel Supreme Court matrimonial
> proceedings. Verify every petition's statutory predicate
> and the specific county's filing protocol before filing.

## At a glance

- **Court**: New York Family Court — established by Art VI
  § 13 of the NY Constitution and the **Family Court Act**
  (NY Family Court Act, "FCA"), with procedural rules at
  **22 NYCRR Part 205**
- **Coverage**: one Family Court per county (62 total);
  larger counties have multiple courthouses + many Judges
  + Support Magistrates + Referees
- **Filing fee**: **no filing fee** for most petitions (FCA
  § 217 / § 251) — Family Court is **fee-waived by default**
  to ensure accessibility
- **E-filing**: **NYSCEF mandatory in many counties** for
  divorce-adjacent matters; rolling out for support, custody,
  family-offense, and PINS as well; some petitions still
  filed in person
- **Right to counsel**: assigned counsel under FCA § 262 for
  parents in Article 10 abuse/neglect, Article 6 termination
  of parental rights, Article 7 PINS, Article 3 juvenile
  delinquency, and **family-offense respondents in
  Article 8 proceedings facing the prospect of Order of
  Protection consequences**

## Court structure — Judges, Support Magistrates, Referees

Family Court has a unique three-tier adjudicative structure:

- **Family Court Judges** — full-time judicial officers
  elected/appointed under Art VI § 13; hear custody,
  visitation, family-offense, PINS, abuse and neglect,
  termination of parental rights, juvenile delinquency
- **Support Magistrates** — court attorneys appointed under
  FCA § 439 who hear **all child support and spousal
  support** matters. Their orders are subject to objection
  before a Family Court Judge under FCA § 439(e). All NY
  Child Support Standards Act ("CSSA") cases proceed through
  Support Magistrates first.
- **Referees** — Judicial Hearing Officers or
  court-appointed referees who hear specific matters under
  FCA § 161; usually handles paternity testing-result
  reviews, specific orderly-administration tasks

## Article overview

The Family Court Act organizes Family Court jurisdiction by
**Article** — each Article corresponds to a different
proceeding type with its own procedure:

### Article 3 — Juvenile Delinquency (FCA § 301 et seq.)

Persons under 18 (Raise the Age 2017 + 2018) charged with
acts that would be crimes if committed by adults. Heard
before a Family Court Judge. Pre-adjudicatory probation /
ATD (Alternatives to Detention) common. Adjudication
results in **adjustment**, **dismissal**, **conditional
discharge**, **probation**, or **placement** with the OCFS.

### Article 4 — Child Support (FCA § 411 et seq.)

The principal financial-support proceeding. **CSSA** at
FCA § 413 governs the basic child-support obligation:

- **17%** of combined parental adjusted gross income for
  1 child
- **25%** for 2 children
- **29%** for 3 children
- **31%** for 4 children
- **35%** for 5 or more children

The 2024 statutory **combined-income cap**: **$183,000**
(adjusts every two years). Above the cap, the court may
apply CSSA percentages or weigh **paragraph (f) factors**
(financial resources, child's standard of living, tax
consequences, etc.). Both parties' incomes are pooled and
imputed where appropriate. **Add-ons** include:

- Child care
- Health insurance
- Unreimbursed medical
- Educational expenses
- Other (often clothes / extracurriculars by case-by-case)

### Article 5 — Paternity (FCA § 511 et seq.)

Establishment of paternity for unmarried fathers. Father
or mother may petition; court may order **genetic-marker
test** (GMT) at no charge to the petitioner. The Article 5
Order of Filiation is a predicate for any subsequent Article
4 support proceeding.

### Article 6 — Custody and Visitation; Adoption (FCA § 611 et seq.)

The principal custody / visitation forum. Family Court has
**concurrent jurisdiction with Supreme Court** for custody;
Supreme Court has exclusive jurisdiction over **divorce
itself** but can refer custody to Family Court (or retain
it under the Matrimonial Part). The **best-interests**
standard from *Eschbach v. Eschbach*, 56 N.Y.2d 167 (1982),
governs. **Joint legal custody** is the modern default unless
parental conflict is so high that joint decision-making is
unworkable (*Friederwitzer v. Friederwitzer*).

Sub-areas under Article 6:

- **Custody petitions** between unmarried parents, or
  between a parent and a non-parent who has assumed
  parental role (in narrow circumstances — *Brooke S.B. v.
  Elizabeth A.C.C.*, 28 N.Y.3d 1 (2016), expanded
  "parent" definition for non-biological co-parents)
- **Visitation petitions** by grandparents under DRL § 72
- **Adoption** under FCA § 651 + DRL Article 7

### Article 7 — Persons In Need of Supervision (PINS)

Persons under 18 (some jurisdictions extend to 21) deemed
"in need of supervision" by behavior such as truancy,
incorrigibility, running away, or other status offenses.
NYC has substantially eliminated the PINS docket since
2018 in favor of diversion programs; outside NYC the PINS
docket remains active.

### Article 8 — Family Offenses + Orders of Protection

**Family-offense petitions** allow a victim to seek a civil
**Order of Protection** against a respondent who has
committed a qualifying offense. Two qualifying elements
must both be met:

1. **Qualifying relationship**: spouse, ex-spouse, parent
   in common with the victim's child, family member by
   blood/marriage, **or person with whom the victim has had
   an "intimate relationship"** (an expanding category;
   FCA § 812)
2. **Qualifying offense** from the FCA § 812 catalog —
   includes:
   - Assault (Penal Law § 120)
   - Aggravated harassment (PL § 240.30)
   - Stalking (PL § 120.45-120.60)
   - Menacing (PL § 120.13-120.15)
   - Reckless endangerment (PL § 120.20-120.25)
   - Strangulation (PL § 121.11-121.13)
   - Identity theft (PL § 190.78-190.80)
   - Forcible touching (PL § 130.52)
   - Coercive control (PL § 121.05-121.07, added 2022)
   - Many others — verify against the current § 812 list

**Order of Protection types**:

- **Temporary** — issued ex parte at the first appearance,
  pending the fact-finding
- **Final** — after fact-finding, can run up to 2 years
  (5 years on showing of aggravating circumstances)
- **Stay-away** clauses + no-contact clauses + firearm
  surrender are routine

### Article 10 — Child Abuse and Neglect

ACS (NYC) or DSS (rest of state) is the petitioner. The
fact-finding determines whether abuse / neglect occurred.
**Right to assigned counsel** for the respondent parent
(FCA § 262). Dispositional outcomes range from **adjustment
without finding** to **placement of the child with OCFS or
relatives**. Parallel **Article 6 termination of parental
rights (TPR)** proceedings may follow if the parent fails
to remediate.

### Article 11 — Habeas Corpus for Children

Used historically for custodial-interference disputes.
Less common today; supplanted by direct Article 6 custody
petitions.

## Distinctives

### No divorce — Supreme Court matrimonial only

Family Court **does not handle divorces**. Divorce, legal
separation, annulment, and equitable distribution of marital
property route to **Supreme Court Matrimonial Part** (see
`ny-nyco`, `ny-kings`, `ny-nassau` etc.). Family Court has
concurrent jurisdiction with Supreme Court for **custody,
visitation, and child support** when no matrimonial action
is pending; once a matrimonial action is filed in Supreme
Court, the Supreme Court can retain custody / support or
refer to Family Court under DRL § 252.

### Support Magistrate process + objection procedure

All Article 4 child support and Article 5 paternity matters
are heard initially by a **Support Magistrate** — not a
Family Court Judge. Within **35 days** of the Support
Magistrate's order, a party may file a **written objection**
under FCA § 439(e) to be heard by the Family Court Judge.
The objection process is the principal vehicle for
correcting CSSA calculation errors and reviewing
Magistrate findings.

### CSSA presumption + rebutting it

CSSA's percentage-of-income formula is **presumptively
correct** under FCA § 413(1)(g). A court can deviate only
on findings that the presumptive amount is "unjust or
inappropriate" considering the paragraph (f) factors.
Magistrates routinely rubber-stamp the CSSA calculation
absent specific deviation arguments.

### Family-offense forum strategy

Family Court family-offense petitions run **in parallel**
with any criminal prosecution. The respondent may face:

- **Criminal Court** order of protection (issued at
  arraignment under Criminal Procedure Law)
- **Family Court** order of protection (Article 8)
- **Supreme Court** order of protection (if matrimonial
  action pending)

The three forums issue overlapping but distinct orders.
Family Court orders are civil; violations are punishable
as contempt under Judiciary Law § 750 or criminal
contempt under Penal Law § 215.50.

### NYC vs. outside NYC differences

**NYC Family Court** is housed in **5 borough courthouses**:

- New York County: **60 Lafayette Street, NY NY**
- Kings County: **330 Jay Street, Brooklyn**
- Bronx County: **900 Sheridan Avenue, Bronx**
- Queens County: **151-20 Jamaica Avenue, Jamaica**
- Richmond County: **100 Richmond Terrace, Staten Island**

NYC operates a high-volume PINS / Article 10 / Article 3
docket with **ACS** (Administration for Children's Services)
as the petitioner. Outside NYC, **DSS** (Department of
Social Services, by county) is the equivalent petitioner.

### Confidentiality + sealed records

Article 3 juvenile delinquency records are **sealed** by
default under FCA § 375.1-375.3. Article 7 PINS records are
also sealed. Article 10 abuse and neglect records are
confidential by statute (FCA § 1043) but accessible to the
parties + counsel. Family Court orders + petitions are
generally **not public** in the way Supreme Court papers
are — viewers must establish standing.

## Filing checklist

1. **Identify the correct petition type** — each Article
   has its own petition form (most accessible via NYCourts
   "Form Search" at `nycourts.gov/forms/`)
2. **Determine the proper county** — generally where the
   child resides (FCA § 421); special venue rules for
   Article 8 (where parties reside or where offense
   occurred) and Article 10 (where the child resides)
3. **No filing fee** (FCA § 217) for most petitions
4. **First appearance** — typically within **2-4 weeks** of
   filing
5. **Court-appointed counsel** for the respondent on
   Article 10, Article 7, Article 3, Article 8 if Order
   of Protection sought
6. **Counsel for the child** (formerly "law guardian") in
   custody, visitation, abuse / neglect, TPR (FCA § 241,
   § 1042)

## Composition with other ny- skills

- `ny-statewide-format` — caption + format baseline; Family
  Court uses **22 NYCRR Part 205** with simplified
  procedural rules
- `ny-pro-se` — pro se framework (Family Court is
  predominantly pro se for petitioners on family-offense,
  custody, support — Article 10 / juvenile delinquency
  respondents have assigned counsel right)
- `ny-deadlines` — Support Magistrate 35-day objection
  clock + Order of Protection 2/5-year duration
- `ny-first-30-days` — Answer + counter-petitions in Family
  Court are less formal than in Supreme Court; the petition
  is usually answered orally at first appearance
- `ny-nyco`, `ny-kings` etc. — Supreme Court Matrimonial
  Part for divorce + equitable distribution (Family Court
  handles parenting + support concurrently)
- `ny-county-courts` — appellate destination for some
  Family Court orders is the Appellate Division (the same
  Department as the Supreme Court for that county)

## Pro-se resources

- **NYS OCA Family Court forms** — `nycourts.gov/forms/familycourt/`
- **Court Help** — `nycourts.gov/courthelp/` — extensive
  Family Court material with petition walkthroughs
- **NYC Family Justice Centers** (Bronx, Brooklyn, Manhattan,
  Queens, Staten Island) — combined-services centers
  offering free legal assistance for family-offense matters
- **Sanctuary for Families** — NYC; family-offense focus
- **Day One** — NYC; family-offense / teen dating violence
- **Pace Women's Justice Center** — Lower Hudson; family-offense
- **NYS OCFS Office of Children and Family Services** —
  state-level oversight for foster care, adoption,
  juvenile justice; intake hotlines

## High-yield Family Court checks

1. **Article identification**: is this Article 3 (JD), 4
   (support), 5 (paternity), 6 (custody), 7 (PINS), 8
   (family offense), 10 (abuse and neglect)?
2. **Forum vs. matrimonial overlap**: is there a parallel
   Supreme Court matrimonial action? Concurrent jurisdiction
   issue?
3. **CSSA application**: cap of $183,000 (2024) reached?
   Deviation grounds under paragraph (f)?
4. **Support Magistrate 35-day objection** clock for
   correcting calculation errors?
5. **Order of Protection scope**: qualifying-relationship
   established? Qualifying offense pled with PL section
   cite? Duration (2 years default, 5 with aggravating
   circumstances)?
6. **Counsel rights**: assigned counsel on Article 10 / TPR
   / Article 8 OP / JD requested + appointed?
7. **NYC-specific**: ACS as petitioner in Article 10? Right-
   to-Counsel under NYS not applicable in NYC because of
   Family Justice Center coverage?
