---
name: tn-juvenile-court-codearranger
title: Tennessee Juvenile Court — Title 37
description: This skill should be used for a Tennessee matter before Juvenile Court under Title 37 — parentage / paternity and legitimation, custody and support of children of UNMARRIED parents, dependency and neglect, termination of parental rights, and delinquency. Triggers include "Tennessee Juvenile Court", "paternity Tennessee", "parentage Tennessee", "legitimation Tennessee", "establish paternity Tennessee", "unmarried parents custody Tennessee", "child support unmarried parents Tennessee", "dependency and neglect Tennessee", "termination of parental rights Tennessee", "TPR Tennessee", "Tenn. Code Ann. Title 37", "Tenn. Code Ann. 37-1-103", "juvenile court magistrate Tennessee", "juvenile court appeal Tennessee", "de novo appeal Circuit Court Tennessee". A venue skill for Title 37 Juvenile Court jurisdiction and routing; it defers the substantive parentage / custody / support law to tn-family-law and document form to tn-statewide-format.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-juvenile-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Juvenile Court — Title 37

> **NOT LEGAL ADVICE.** Juvenile-court matters — parentage,
> custody, dependency and neglect, and especially termination of
> parental rights — carry profound and often irreversible
> consequences for parents and children. Strongly consider
> consulting a licensed Tennessee family-law / juvenile attorney;
> in many of these proceedings a parent may be entitled to
> appointed counsel. This skill is a drafting/venue aid; verify the
> controlling Title 37 provisions and the court's local rules before
> filing.

Tennessee's **Juvenile Courts** are creatures of **Title 37** of the
Tennessee Code. They are the venue for matters concerning **minors**
that fall outside a married-couple divorce. This skill covers what
Juvenile Court handles, how matters are routed there (versus to
Circuit / Chancery), and the magistrate / appeal structure. For the
substantive parentage, custody, and support law, see `tn-family-law`.
For document form, see `tn-statewide-format`.

## What Juvenile Court handles (for minors)

| Matter | Authority |
|---|---|
| **Parentage / paternity and legitimation** | Title 37 (with the Title 36 ch. 2 parentage statutes) |
| **Custody and support of children of UNMARRIED parents** | Title 37 |
| **Dependency and neglect** | Title 37 (Tenn. Code Ann. § 37-1-101 et seq.) |
| **Termination of parental rights (TPR)** | Title 37 / Title 36 ch. 1 |
| **Delinquency and unruly children** | Title 37 |

Once parentage and custody are before the Juvenile Court, the
**substantive standards are the same Title 36 framework** covered in
`tn-family-law`: child support follows the **income-shares model**
(§ 36-5-101; Guidelines at Tenn. Comp. R. & Regs. ch. 1240-02-04), and
custody / parenting decisions apply the **best-interest factors at
§ 36-6-106(a)**. The forum differs; the substantive law does not.

## Routing — Juvenile vs. Circuit / Chancery

The dividing line is whether the parents were **married to each
other**:

- **Unmarried parents** → establishing parentage and the resulting
  custody / support order is a **Juvenile Court (Title 37)** matter.
  Use this skill.
- **Married or formerly married parents** → custody and support
  **incident to a divorce** (or post-divorce modification) is a
  **Circuit or Chancery Court** matter. Use `tn-family-court`, not
  this skill.

> State the routing plainly: divorce and married-parent custody do
> **not** go to Juvenile Court — they go to Circuit / Chancery
> (`tn-family-court`). Juvenile Court is for parentage,
> unmarried-parent custody/support, dependency/neglect, TPR, and
> delinquency.

There can be overlap — for example, parentage may be raised in more
than one proceeding, and a dependency/neglect or TPR case can run
alongside a custody case. Confirm the proper forum for the specific
facts before filing.

## Establishing parentage / paternity and legitimation

- A parentage or legitimation action establishes the **legal
  parent-child relationship** for a child whose parents were not
  married to each other. Tools include a **voluntary acknowledgment
  of paternity**, **genetic (DNA) testing**, and an adjudication of
  parentage.
- Once parentage is established, the court can enter **custody /
  parenting** and **child-support** orders applying the Title 36
  standards (see `tn-family-law`).
- The substantive parentage statutes sit in **Title 36, Chapter 2**;
  the Juvenile Court's authority to hear them sits in **Title 37**.
  Verify the current chapter, the standing rules, the acknowledgment
  and rescission timelines, and the genetic-testing provisions before
  drafting a petition.

## Dependency and neglect; termination of parental rights

- **Dependency and neglect** proceedings (Tenn. Code Ann.
  § 37-1-101 et seq.) address children alleged to be dependent,
  neglected, or abused, often involving the **Department of
  Children's Services (DCS)**. These cases follow their own statutory
  timeline (preliminary / adjudicatory / dispositional hearings) and
  a clear-and-convincing-evidence standard for adjudication — verify
  the current standards and timelines.
- **Termination of parental rights (TPR)** permanently severs the
  legal parent-child relationship and is the gateway to adoption. TPR
  requires proof of a **statutory ground** plus a **best-interest**
  finding, each by **clear and convincing evidence**. Grounds and the
  best-interest factors are statutory — research and cite the
  current provisions; do not rely on memory, as the grounds and the
  TPR best-interest factors have been amended.

> These are among the highest-stakes proceedings in Tennessee law.
> A parent may have a **right to appointed counsel** in dependency /
> neglect and TPR cases — confirm the current entitlement and advise
> the party to seek counsel.

## Magistrates and the appeal / rehearing path

Many Juvenile Court matters are heard in the first instance by a
**magistrate** (sometimes called a referee), whose findings and
recommendations are subject to **confirmation by the judge** and to a
party's right to request a **rehearing before the juvenile court
judge** within a short statutory window. Keep the two layers
distinct:

1. **Magistrate → juvenile court judge.** A party who disagrees with a
   magistrate's order may seek a **rehearing** before the juvenile
   court judge within the time set by Title 37 and the court's rules.
2. **Juvenile court → appeal.** From a final juvenile-court order,
   the appeal route depends on the **type of case**. Certain
   juvenile matters appeal **de novo to Circuit Court**, while others
   (notably termination of parental rights and dependency/neglect
   appeals in some configurations) follow a different appellate
   route. **The specific appeal route, the time to appeal, and any
   bond requirement vary by case type — verify the controlling Title
   37 provision for the specific order before relying on a particular
   route.**

> Do not assume a single appeal path. The rehearing-then-appeal
> structure and the destination of the appeal (Circuit Court de novo
> vs. the appellate courts) turn on the kind of juvenile order at
> issue. Confirm against current Title 37.

## Filing mechanics (overview)

- File in the **Juvenile Court** of the proper county (Tennessee has
  both dedicated juvenile courts and, in many counties, general
  sessions courts exercising juvenile jurisdiction — confirm the
  local court).
- Use `tn-statewide-format` for the Tenn. R. Civ. P. 10 caption,
  signature, and **redaction of minors' identifiers** (juvenile
  records carry heightened confidentiality — verify the current
  sealing / confidentiality rules).
- E-filing and forms are **county-by-county**; confirm the venue's
  platform and any AOC-approved juvenile forms with the relevant
  county skill.

## Composition

- For the substantive parentage / custody / support / TPR law:
  `tn-family-law`
- For divorce and married-parent custody (the other side of the
  routing line): `tn-family-court`
- For format, caption, and redaction of minors' identifiers:
  `tn-statewide-format`
- For the specific county / juvenile court: `tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, `tn-county-courts`
- For pro se conventions: `tn-pro-se`
- For drafting petitions / motions / declarations: `tn-draft-motion`,
  `tn-draft-declaration`
- For proposed orders: `tn-draft-order`, `tn-submit-order`
- For deadlines (rehearing / appeal windows): `tn-deadlines`
- For hearings: `tn-hearings`
- For citation verification: `tn-fact-check`

## References

- `references/jurisdiction-routing.md` — Title 37 jurisdiction and
  the unmarried-vs-married routing line
- `references/parentage-legitimation.md` — paternity, voluntary
  acknowledgment, genetic testing, legitimation
- `references/dependency-neglect.md` — § 37-1-101 et seq. timeline and
  DCS involvement
- `references/termination-of-parental-rights.md` — statutory grounds +
  best-interest standard (clear and convincing evidence)
- `references/magistrate-and-appeals.md` — rehearing before the judge
  and the case-type-dependent appeal route
