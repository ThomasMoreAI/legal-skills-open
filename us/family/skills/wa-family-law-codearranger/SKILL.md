---
name: wa-family-law-codearranger
title: Washington Family Law — Subject-Matter Bundle
description: Use when handling a Washington family-law matter — dissolution / legal separation / annulment, child support and modification, parenting plans, allocation of decision-making, spousal maintenance, property distribution (Washington is community-property), parentage, UCCJEA / UIFSA, civil protection orders (RCW 7.105), and post-decree modification. Triggers include "Washington divorce", "parenting plan", "child support", "RCW 26.09", "community property", "RCW 26.16", "spousal maintenance", "RCW 7.105 civil protection order", "UCCJEA", "UIFSA", "parentage", "dissolution".
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Washington Family Law — Subject-Matter Bundle

> **NOT LEGAL ADVICE.** Family-law statutes are amended
> frequently. This skill names the controlling chapters and
> describes the procedural framework; **current statutory
> text, dollar thresholds, day counts, and section numbers
> live in the references corpus** at `wa-law-references/
> references/wa-rcw-debt/`. Verify against the current
> chapter file before relying on any specific figure.

## At a glance — Washington's family-law architecture

- **Forum**: Superior Court Family Law Department in each
  county. Washington has no separate Family Court trial
  court; family matters sit inside the general-jurisdiction
  Superior Court.
- **Substantive code**: **RCW Title 26** (Domestic
  Relations) covers marriage, dissolution, child support,
  custody / parenting, parentage, community property,
  UCCJEA, and UIFSA. RCW Title 13 covers juvenile-court
  dependency and termination of parental rights when CPS /
  DCYF involvement crosses over.
- **Procedural overlay**: General CR + GR + each county's
  Local Rules; mandatory AOC forms published under GR 31.
- **Marital property regime**: **community property** —
  one of only 9 U.S. community-property states. NOT
  equitable distribution.

## Chapter pointers

| Topic | Chapter | Reference file |
|---|---|---|
| Marriage (formation, capacity) | RCW 26.04 | `RCW-26_04.md` |
| Dissolution / legal separation | RCW 26.09 | `RCW-26_09.md` |
| Community property | RCW 26.16 | `RCW-26_16.md` |
| Child support enforcement | RCW 26.18 | `RCW-26_18.md` |
| Child support schedule | RCW 26.19 | `RCW-26_19.md` |
| UIFSA | RCW 26.21A | `RCW-26_21A.md` |
| Parentage (UPA, 2019) | RCW 26.26A | `RCW-26_26A.md` |
| UCCJEA | RCW 26.27 | `RCW-26_27.md` |
| Child-abuse reporting / CPS | RCW 26.44 | `RCW-26_44.md` |
| Civil protection orders (2022 consolidated) | RCW 7.105 | `RCW-7_105.md` |
| Juvenile dependency / TPR | RCW 13.34 | `RCW-13_34.md` |

When applying a specific subsection, residency requirement,
deadline, or dollar threshold, **read the relevant chapter
file**. Don't rely on memory.

## Dissolution — procedural framework

The Washington dissolution process is no-fault. The
controlling fact is whether the marriage is irretrievably
broken. The mechanical steps:

1. Verify petitioner's Washington residency
2. File Petition for Dissolution (AOC mandatory FL Divorce
   forms)
3. Serve respondent; respondent answers
4. Mandatory financial disclosures
5. Temporary orders (parenting / support / restraints)
6. Mediation / dispute resolution where ordered
7. Final hearing (after the mandatory waiting period)
8. Decree + Findings + parenting plan + support order

For the residency requirement, the response window, and
the waiting-period day count, consult `RCW-26_09.md`.

## Property distribution — community-property framework

The court must make a "just and equitable" division
considering both community AND separate property and the
factors at RCW 26.09.080. The key distinctions:

- **Community property**: acquired during marriage with
  community labor / income
- **Separate property**: pre-marital + gift / inheritance +
  rents/profits of separate property
- **Quasi-community property**: out-of-state property that
  would have been community if acquired in WA
- **Commingling**: separate property loses character when
  it can no longer be traced

Unlike common-law / equitable-distribution states, a
Washington court can award separate property to the
non-owning spouse to achieve a just-and-equitable result.
For factor enumeration and commingling doctrine, see
`RCW-26_09.md` and the case law summarized in
`wa-law-references/references/key-cases.md`.

## Child support — income-shares framework

Washington uses an income-shares model implemented via the
**Washington State Child Support Schedule and Economic
Table**. Mechanical steps:

1. Determine each parent's net monthly income (gross minus
   the specifically-allowable subtractions in RCW 26.19)
2. Sum to combined net income
3. Look up basic support on the Economic Table
4. Allocate pro rata to each parent's share of combined net
5. Apply pro rata adjustments (health insurance, daycare,
   extraordinary medical)
6. Apply standard deviations where appropriate

For the income-definition rules, the current Economic
Table, the combined-income cap above which courts have
discretion, the worksheet form, and modification
thresholds, consult `RCW-26_19.md` and `RCW-26_18.md`.

## Parenting plans — best-interests + limitations factors

The Parenting Plan replaces the old "custody / visitation"
framework. The court allocates:

- **Residential schedule** (where the child lives)
- **Decision-making** (major decisions on education,
  non-emergency medical care, religion)
- **Dispute resolution** mechanism

Two factor sets govern the residential schedule:

- **Best-interests factors**: the affirmative factors the
  court considers when setting the schedule (strength of
  each parent-child relationship is given the most weight;
  past performance of parenting functions; child's needs +
  development + relationships + activities; parental wishes
  and child's wishes if age-appropriate)
- **Limitations factors**: a separate set of MANDATORY
  restrictions on residential time or decision-making
  authority when the court finds qualifying conduct (e.g.,
  willful abandonment, physical / sexual / emotional abuse,
  history of domestic violence, assault). Limitations
  factors are not discretionary — a finding triggers
  automatic restrictions.

For the controlling factor enumeration, see `RCW-26_09.md`.

## Relocation

A parent intending to relocate the child with court-
ordered residential time must give notice via the AOC
Notice of Intended Relocation form. The objecting parent
has a fixed window to file objection. There's a rebuttable
presumption in favor of the primary residential parent.
For the notice period, objection deadline, and the
presumption framework, see `RCW-26_09.md`.

## Spousal maintenance

Washington has no formula for spousal maintenance. The
court applies the statutory factors (financial resources;
time to acquire training; standard of living; duration of
marriage; age + condition; ability to meet own needs while
paying). Duration guideposts come from case law, not
statute. Modification requires substantial change of
circumstances; non-modifiable if the decree so states.

For the factor enumeration and modification rules, see
`RCW-26_09.md`.

## Parentage — Uniform Parentage Act (2019)

Washington enacted the 2017 Uniform Parentage Act in 2019.
RCW 26.26A covers:

- Presumed parentage of married parents
- Voluntary acknowledgment of paternity (VAP) —
  administrative
- Genetic-testing-based adjudication
- Assisted-reproduction parentage (donor gametes, intended
  parents)
- Surrogacy (gestational-surrogacy parental designation)
- **De facto parentage** — codified recognition for
  someone who has resided as a regular household member,
  engaged in consistent caretaking without expectation of
  compensation, held the child out as their own, and
  established a bonded relationship that the other parent
  fostered

See `RCW-26_26A.md` for the de-facto-parentage element
list and the assisted-reproduction / surrogacy frameworks.

## Civil protection orders — 2022 consolidation

RCW 7.105 (effective 2022) consolidated six previously
fragmented civil-protection-order chapters into one. The
six categories:

1. Domestic violence
2. Sexual assault
3. Stalking
4. Anti-harassment
5. Vulnerable adult
6. Extreme risk

Common procedural shape: ex parte temporary order on
showing of immediate danger; full hearing within a short
window; final order duration set by statute / category;
firearm-surrender requirement when triggered. For
qualifying-relationship rules, qualifying-conduct
elements, hearing deadlines, and duration limits per
category, see `RCW-7_105.md`.

## UCCJEA + UIFSA — interstate jurisdiction

- **UCCJEA** (RCW 26.27) governs initial custody
  jurisdiction and modification. Home-state rule applies.
- **UIFSA** (RCW 26.21A) governs interstate enforcement
  and modification of support orders. One-controlling-
  order rule.

For the home-state definition, emergency-jurisdiction
mechanics, and the one-order rule, see `RCW-26_27.md` and
`RCW-26_21A.md`.

## DCYF / dependency overlap

When CPS / Department of Children, Youth & Families gets
involved, the case can run parallel to private
dissolution. Mandatory reporting rules sit in RCW 26.44;
dependency procedure (petition / shelter-care / fact-
finding / disposition) sits in RCW 13.34. Termination of
parental rights is a separate proceeding with a higher
burden. For mandatory-reporter categories, dependency
timeline, and TPR grounds, see `RCW-26_44.md` and
`RCW-13_34.md`.

## Composition with other wa- skills

- `wa-family-court` — venue mechanics + AOC forms
- `wa-statewide-format` — caption + GR 14 + AOC forms
- `wa-discovery` — discovery in family-law matters
- `wa-post-judgment` — modification + enforcement
- `wa-pro-se` — pro-se framework
- `wa-fact-check` — citation verification
