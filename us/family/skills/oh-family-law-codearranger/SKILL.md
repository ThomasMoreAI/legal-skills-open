---
name: oh-family-law-codearranger
title: Ohio Family Law — Substantive Framework
description: 'Use for Ohio family-law matters — divorce, dissolution, legal separation, annulment, child support, spousal support, parenting, property division. Covers **R.C. Chapter 3105** (divorce/dissolution), **R.C. Chapter 3109** (allocation of parental rights), **R.C. Chapter 3119** (child support — income-shares, **$300k cap**, **10% mod threshold**), **R.C. 3105.171** (property division — **equitable, NOT community property**), spousal support (**R.C. 3105.18**), CPOs (**R.C. 3113.31**), UCCJEA/UIFSA, and juvenile court (**R.C. Chapter 2151**). Triggers: "Ohio divorce", "Ohio dissolution", "R.C. 3119", "Ohio child support", "equitable distribution".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Ohio Family Law — Substantive Framework

> **NOT LEGAL ADVICE.** Ohio domestic-relations practice
> varies materially between Domestic Relations Divisions of
> different Common Pleas courts. Verify the assigned
> court's local rules and standard orders. Family-law
> outcomes can be life-altering — strongly recommend
> consulting a licensed Ohio attorney.

## Divorce vs. dissolution vs. legal separation vs. annulment

Ohio offers **four** distinct case types in the Domestic
Relations Division:

### 1. Dissolution (R.C. 3105.61-65) — agreed-on uncontested

- **Joint petition** signed by both spouses.
- **Separation agreement** must be complete: property
  division, debt allocation, spousal support, parenting
  plan, child support — all worked out before filing.
- **30-90 day window** to final hearing (R.C. 3105.64).
- **No "fault"** required; mutual decision to end marriage.
- Cheapest, fastest path when spouses agree.

### 2. Divorce (R.C. 3105.01) — contested

- **Grounds** at R.C. 3105.01:
  - Incompatibility (no-fault, requires both spouses to
    admit; if one denies, falls back to fault grounds)
  - Living separate without cohabitation 1+ year (no-fault)
  - Adultery, willful absence 1+ year, extreme cruelty,
    fraudulent contract, gross neglect of duty, habitual
    drunkenness, imprisonment, bigamy, divorce from other
    spouse outside Ohio
- **Residency** — petitioner must be Ohio resident **6
  months** before filing (R.C. 3105.03); **90 days** in
  the county.
- **Service** per Civ. R. 4.

### 3. Legal separation (R.C. 3105.17) — alternative

- Court can grant separation without dissolving marriage.
- Same grounds as divorce.
- Used when religious / immigration / insurance reasons
  prevent dissolution.

### 4. Annulment (R.C. 3105.31) — marriage was void / voidable

- Grounds: party under age, prior marriage, mental
  incapacity, consent procured by fraud / force / duress,
  consent of underage party not given by parent, marriage
  never consummated due to physical incapacity.
- Effect: marriage treated as if never occurred (but
  legitimacy of children preserved by R.C. 3105.32).

## Property distribution — equitable, NOT community

**Ohio is an equitable-distribution state** (R.C. 3105.171),
NOT community property. The court divides marital property
equitably — usually equally, but unequal division allowed
when equal would be inequitable.

### Marital vs. separate

- **Marital property** (R.C. 3105.171(A)(3)): property
  acquired during marriage; income, appreciation, and
  participant rights / interests that accrued during
  marriage.
- **Separate property** (R.C. 3105.171(A)(6)): pre-marital
  property; inheritance; gifts from third parties; certain
  passive appreciation; property acquired after legal
  separation.

### The "starting point is equal" rule

R.C. 3105.171(C)(1) creates a **rebuttable presumption** of
equal division of marital property. Court may deviate based
on the factors at R.C. 3105.171(F).

### Pension / retirement division

- Defined-benefit plans typically divided by **QDRO**
  (Qualified Domestic Relations Order under ERISA).
- Ohio public pensions (OPERS, STRS, SERS, OP&F, HPRS)
  divided by **DOPO** (Division of Property Order) — NOT
  a QDRO; statutorily distinct under R.C. 3105.80-90.
- Military retirement governed by Uniformed Services
  Former Spouses' Protection Act (10 U.S.C. § 1408).

## Child support — income-shares model

Ohio uses an **income-shares** model under R.C. Chapter
3119, calculated on the **R.C. 3119.022 worksheet**.

### Calculation steps

1. Determine **gross income** of each parent (R.C.
   3119.01(C)(9) definitions; potential / imputed income
   under R.C. 3119.01(C)(11)-(17)).
2. Sum to **combined gross income**.
3. **$300,000 cap** at R.C. 3119.04 — combined-income
   schedule extends to $300,000; above that, court has
   discretion to extrapolate.
4. Apply **basic support obligation** from R.C. 3119.021
   schedule.
5. **Health-insurance + childcare adjustments** (R.C.
   3119.30, R.C. 3119.302).
6. **Parenting-time deviation** (R.C. 3119.231) — extended
   parenting time can justify deviation downward.
7. **Self-sufficiency reserve** at low end of schedule.

### Modification

**R.C. 3119.79** sets the modification threshold:

- Recalculate using current incomes. If the new
  calculation differs from the existing order by **10% or
  more**, modification mandatory (with the floor /
  exceptions in R.C. 3119.79(C)).
- Modification can be sought through Ohio's **Child
  Support Enforcement Agency (CSEA)** administratively or
  via court motion.

### CSEA administrative review

R.C. 3119.60-79 authorize the **CSEA administrative
review** process — every 36 months either parent can
request administrative review without court filing.
Administrative recommendation becomes effective unless a
party objects + requests court hearing within 14 days.

## Allocation of parental rights and responsibilities

R.C. Chapter 3109 governs custody / parenting-time. Ohio
uses the terms "allocation of parental rights and
responsibilities" rather than "custody" since 1991.

### Sole vs. shared parenting

- **Sole legal custody (Sole Residential)** — one parent
  designated residential parent + legal custodian; other
  has parenting time.
- **Shared parenting plan** under R.C. 3109.04(D)(1) —
  requires plan covering: physical living arrangements,
  medical / dental decision authority, school placement,
  parental rights at school, parenting-time schedule,
  exchange logistics, dispute resolution mechanism.

### Best-interests factors

R.C. 3109.04(F)(1)(a)-(j) — the controlling factors:

(a) Wishes of parents
(b) Wishes of child (in chambers interview if requested)
(c) Child's interaction with parents / siblings /
    significant others
(d) Child's adjustment to home / school / community
(e) Mental + physical health of all involved
(f) Likely-to-honor-court-order parent
(g) Failure to pay child support
(h) History of family violence
(i) Whether parent established residence outside Ohio
(j) Recommendations of GAL / experts

### Guardian ad Litem

**Sup. R. 48** governs GAL appointment + duties in domestic
relations and juvenile cases. GAL fees typically split
between parties or assessed against one based on conduct.

## Spousal support — R.C. 3105.18

The court can order temporary (pendente lite) or permanent
spousal support. **Ohio has no formula** — courts apply
the **14 factors at R.C. 3105.18(C)(1)(a)-(n)**:

(a) Income of parties
(b) Earning abilities
(c) Ages + physical / mental / emotional condition
(d) Retirement benefits
(e) Duration of marriage
(f) Appropriateness of custodial parent staying home
(g) Standard of living during marriage
(h) Education
(i) Assets + liabilities
(j) Contribution to other's education / earning ability
(k) Time + expense for the recipient to acquire training
(l) Tax consequences
(m) Lost income from marital responsibilities
(n) Any other relevant factor

**Modification** — only if the decree expressly reserves
jurisdiction to modify (R.C. 3105.18(E)).

## Civil Protection Orders — R.C. 3113.31

The **DV CPO** is Ohio's family-violence remedy.

- **Qualifying relationships**: spouse / former spouse,
  blood-or-marriage relatives, person living as spouse,
  parent of common child, natural parent of any natural
  child of the respondent.
- **Qualifying acts**: attempting to cause / actually
  causing bodily injury; placing victim in fear of
  imminent serious physical harm; sexually oriented
  offenses; menacing-by-stalking under R.C. 2903.211;
  committing acts that would constitute child abuse.
- **Ex parte hearing** — same-day under R.C. 3113.31(D).
- **Full hearing** — within 7-10 days under R.C.
  3113.31(D)(2).
- **Duration** — up to 5 years; extendable.
- **Firearm-surrender** mandatory under federal 18 U.S.C.
  § 922(g)(8) and *United States v. Hayes*.

Companion **Stalking CPO** under R.C. 2903.214 (no
relationship requirement).

## UCCJEA — R.C. Chapter 3127

Ohio's enactment of the Uniform Child Custody Jurisdiction
and Enforcement Act. **Home-state jurisdiction** governs
initial custody determinations:

- "Home state" = state where child lived with parent for
  **6 consecutive months** before commencement of
  proceeding (R.C. 3127.01(B)(7)).
- Emergency jurisdiction under R.C. 3127.18 for child
  present in Ohio + needing protection.

## UIFSA — R.C. Chapter 3115

Ohio's enactment of the Uniform Interstate Family Support
Act governs interstate enforcement / modification of child
support and spousal support. **One-order rule**: only one
controlling support order at any time.

## Juvenile Court — R.C. Chapter 2151

The Juvenile Division of Common Pleas (or, in some
counties, the Juvenile Court as a separate court) handles:

- **Abuse / neglect / dependency** (R.C. 2151.03-04)
- **Permanent custody** to children services agency (R.C.
  2151.353-414)
- **Delinquency** (R.C. 2151.02)
- **Unruly** (R.C. 2151.022)
- **Paternity** (R.C. Chapter 3111 — though some counties
  vest paternity in DR Division)
- **Right to counsel** — indigent parent has right to
  appointed counsel in abuse/neglect/dependency
  proceedings (R.C. 2151.352; *In re Lassiter* federal
  parallel)

The `oh-family-court` venue skill covers procedural detail.

## Common-law marriage

Ohio **abolished common-law marriage effective October 10,
1991** (R.C. 3105.12). Ohio recognizes common-law
marriages validly created before that date OR validly
created in another jurisdiction that recognizes common-law
marriage (under conflict-of-laws principles).

## Composition with other oh- skills

- `oh-family-court` — venue mechanics (DR + Juvenile)
- `oh-statewide-format` — Civ. R. 10 caption (DR cases
  use `DR` case-number prefix; juvenile uses `JU` or
  county-specific)
- `oh-discovery` — discovery in DR matters
- `oh-post-judgment` — modification + enforcement
- `oh-pro-se` — pro-se framework
- `oh-fact-check` — citation verification
