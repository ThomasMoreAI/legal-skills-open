---
name: oh-family-court-codearranger
title: Ohio Family Court (Domestic Relations + Juvenile Divisions)
description: Use when filing in Ohio family court — Domestic Relations Division of Common Pleas (divorce + married-parent custody/support) OR Juvenile Division of Common Pleas (unmarried-parent custody + child-support enforcement + abuse/neglect under R.C. Chapter 2151). Triggers include 'Ohio family court', 'Ohio Domestic Relations', 'Ohio Juvenile Court', 'R.C. Chapter 3105', 'R.C. Chapter 3109', 'R.C. Chapter 3119', 'R.C. Chapter 2151', 'Ohio CSEA child support', 'Ohio parental rights', 'Ohio custody', 'Ohio CPS'. Covers both divisions, support magistrate practice, guardian ad litem appointments under Sup. R. 48, and the right to assigned counsel in abuse/neglect cases.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Ohio Family Court (Domestic Relations + Juvenile Divisions)

> **NOT LEGAL ADVICE.** Family law has significant long-
> term consequences for property, children, and finances.
> Consult a licensed Ohio family-law attorney whenever
> possible.

## At a glance — two divisions

Ohio has **no separate "Family Court."** Family matters
are heard in two divisions of the **Court of Common
Pleas**:

### Domestic Relations Division

- **Subject matter**: divorce, dissolution, annulment,
  legal separation, allocation of parental responsibilities
  + parenting time + child support **for married parents**
  + spousal support + property distribution
- **Statutory authority**: R.C. Chapter 3105 (divorce);
  R.C. Chapter 3109 (children); R.C. Chapter 3119 (child
  support guidelines); R.C. Chapter 2301.03 establishes
  the Division
- **Procedural rules**: Ohio Civ. R. + per-court Loc. R.
- **Larger counties** have a separately-organized Domestic
  Relations Division; smaller counties handle family
  matters in the General Division

### Juvenile Division

- **Subject matter**: unmarried-parent custody +
  parentage + child support enforcement + juvenile
  delinquency + abuse, neglect, dependency proceedings
  under R.C. Chapter 2151 + adoption (in some courts)
- **Statutory authority**: R.C. Chapter 2151 (Juvenile
  Court); R.C. Chapter 3109 + 3119 for unmarried-parent
  custody and support
- **Procedural rules**: Ohio Juv. R. (Juvenile Rules of
  Procedure)

## Right to counsel

Ohio provides assigned counsel under R.C. 2151.352 (abuse/
neglect/dependency proceedings — indigent parents have a
constitutional and statutory right to counsel) and R.C.
2151.281 (juvenile delinquency). Divorce and unmarried-
parent custody disputes do **not** carry a right to
assigned counsel.

## Child Support Enforcement Agency (CSEA)

Each Ohio county operates a **Child Support Enforcement
Agency** under R.C. Chapter 3125. The CSEA:

- Administratively establishes paternity (with consent)
- Calculates child support using R.C. Chapter 3119
  guidelines
- Enforces support orders via wage withholding, license
  suspension, tax intercept
- **Administrative orders** can be modified or vacated by
  the Juvenile Court on objection

## Support magistrate practice

Under R.C. 3105.011 and Civ. R. 53, **support
magistrates** typically hear the bulk of child-support
calculations + modifications in the Domestic Relations
Division. The magistrate's decision is reviewable by the
Common Pleas judge on **14-day written objection** under
Civ. R. 53(D)(3)(b)(i).

## Guardian ad litem (GAL) — Sup. R. 48

In contested custody, abuse/neglect, or termination-of-
parental-rights cases, the court typically appoints a
**Guardian ad litem (GAL)** under Sup. R. 48 (Ohio Rules
of Superintendence). The GAL:

- Investigates the child's best interests
- Files a report with recommendations
- May testify at trial
- GAL fees typically split between parents (or
  county-paid if both parents are indigent)

## Divorce / dissolution procedure (Domestic Relations)

See `oh-family-law` for substantive law. Procedural flow:

1. **Complaint for divorce** OR **petition for
   dissolution** filed
2. **Restraining order** (Civ. R. 75(I)) auto-issued in
   divorce — preserves status quo pending decree
3. **Mandatory financial disclosure** under Loc. R.
   (varies by court)
4. **CSEA referral** for child support calculation
5. **GAL appointment** if contested custody
6. **Magistrate or judge hearing** — final decree

## Abuse / neglect procedure (Juvenile)

Under R.C. Chapter 2151:

1. **Complaint** filed by county children-services
   agency (CSB) or other authorized party
2. **Emergency / shelter-care hearing** within 72 hours
3. **Adjudicatory hearing** — abuse, neglect, or
   dependency determination
4. **Dispositional hearing** — placement (temporary or
   permanent custody) + case plan
5. **Annual review** under R.C. 2151.417

Parents have right to assigned counsel under R.C.
2151.352 throughout.

## Composition with other oh- skills

- `oh-statewide-format` — Civ. R. 10 caption + signature
- `oh-family-law` — substantive divorce / custody / support
  bundle
- `oh-deadlines` — 14-day magistrate-objection clock;
  divorce residency (6 months state / 90 days county);
  dissolution waiting period (30 days minimum)
- `oh-pro-se` — pro-se framework (family court has high
  pro-se volume)
- `oh-cuya` / `oh-frank` / etc. — flagship Common Pleas
  Domestic Relations Divisions
