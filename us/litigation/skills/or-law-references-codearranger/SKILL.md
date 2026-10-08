---
name: or-law-references-codearranger
title: Oregon Law References — General Civil Practice
description: Use this skill to cite, apply, or research Oregon civil law. Triggers include "ORCP 21", "ORCP 43", "ORCP 46", "ORCP 47", "ORCP 71", "Oregon civil rules", "OEC 803", "OEC 901", "OEC 902", "business records", "authentication", "motion to compel", "attorney fees", "ORS 20", "lodestar", "UTCR", "Oregon citation format", "Or", "P3d", "SLR". Covers ORCP, OEC (ORS 40.010 et seq.), UTCR citation format, ORS 20 fees-and-costs, local SLRs, key civil cases, and canonical online-sources. For subject-matter- specific law (debt collection, landlord-tenant, etc.), compose with relevant subject-matter skill (e.g., or-consumer-debt). Composes with or-statewide-format, or-multcc / or-wccc, or-pro-se, and or-fact-check.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Citation Format
  path: references/citation-format.md
- title: Civil Rules
  path: references/civil-rules.md
- title: Multnomah Slr
  path: references/court-rules/Multnomah-SLR.md
- title: Oec
  path: references/court-rules/OEC.md
- title: Orap
  path: references/court-rules/ORAP.md
- title: Orcp
  path: references/court-rules/ORCP.md
- title: Orpc
  path: references/court-rules/ORPC.md
- title: Readme
  path: references/court-rules/README.md
- title: Utcr
  path: references/court-rules/UTCR.md
- title: Washington Slr
  path: references/court-rules/Washington-SLR.md
- title: Evidence Rules
  path: references/evidence-rules.md
- title: Fees And Costs
  path: references/fees-and-costs.md
- title: Key Cases
  path: references/key-cases.md
- title: Legal Data Apis
  path: references/legal-data-apis.md
- title: Local Rules
  path: references/local-rules.md
- title: Online Sources
  path: references/online-sources.md
- title: Ors 100
  path: references/or-ors-debt/ORS-100.md
- title: Ors 105
  path: references/or-ors-debt/ORS-105.md
- title: Ors 107
  path: references/or-ors-debt/ORS-107.md
- title: Ors 109
  path: references/or-ors-debt/ORS-109.md
- title: Ors 116
  path: references/or-ors-debt/ORS-116.md
- title: Ors 12
  path: references/or-ors-debt/ORS-12.md
- title: Ors 124
  path: references/or-ors-debt/ORS-124.md
- title: Ors 14
  path: references/or-ors-debt/ORS-14.md
- title: Ors 165
  path: references/or-ors-debt/ORS-165.md
- title: Ors 174
  path: references/or-ors-debt/ORS-174.md
- title: Ors 18
  path: references/or-ors-debt/ORS-18.md
- title: Ors 187
  path: references/or-ors-debt/ORS-187.md
- title: Ors 19
  path: references/or-ors-debt/ORS-19.md
- title: Ors 192
  path: references/or-ors-debt/ORS-192.md
- title: Ors 20
  path: references/or-ors-debt/ORS-20.md
- title: Ors 21
  path: references/or-ors-debt/ORS-21.md
- title: Ors 32
  path: references/or-ors-debt/ORS-32.md
- title: Ors 33
  path: references/or-ors-debt/ORS-33.md
- title: Ors 36
  path: references/or-ors-debt/ORS-36.md
- title: Ors 40
  path: references/or-ors-debt/ORS-40.md
- title: Ors 41
  path: references/or-ors-debt/ORS-41.md
- title: Ors 646
  path: references/or-ors-debt/ORS-646.md
- title: Ors 657
  path: references/or-ors-debt/ORS-657.md
- title: Ors 659A
  path: references/or-ors-debt/ORS-659A.md
- title: Ors 697
  path: references/or-ors-debt/ORS-697.md
- title: Ors 71
  path: references/or-ors-debt/ORS-71.md
- title: Ors 72
  path: references/or-ors-debt/ORS-72.md
- title: Ors 73
  path: references/or-ors-debt/ORS-73.md
- title: Ors 79
  path: references/or-ors-debt/ORS-79.md
- title: Ors 79A
  path: references/or-ors-debt/ORS-79A.md
- title: Ors 82
  path: references/or-ors-debt/ORS-82.md
- title: Ors 86
  path: references/or-ors-debt/ORS-86.md
- title: Ors 87
  path: references/or-ors-debt/ORS-87.md
- title: Ors 88
  path: references/or-ors-debt/ORS-88.md
- title: Ors 90
  path: references/or-ors-debt/ORS-90.md
- title: Readme
  path: references/or-ors-debt/README.md
---

# Oregon Law References — General Civil Practice

This skill is a matter-neutral reference index — a pointer to the
statutes, rules, and doctrines most often invoked in Oregon civil
practice *across any subject matter*. The body below summarizes
each source. Detailed sections, elements, and citation examples
live in `references/`.

> **NOT LEGAL ADVICE.** These notes are drafting aids, not legal
> advice. Every citation should be verified against the current
> ORS, current court rule, or current case law before it goes
> into a filing. Use `or-fact-check` before any packet is filed.

## How to use this skill

Ask: *what is the user trying to establish procedurally?*

- **A procedural motion** (compel, dismiss, strike, default, SJ,
  vacate) → start with `references/civil-rules.md`
- **An evidentiary objection** (hearsay, authentication, best
  evidence, foundation) → start with `references/evidence-rules.md`
- **A fee-and-cost request or objection** → start with
  `references/fees-and-costs.md`
- **A local-rule question** (Multnomah SLR; Washington Co SLR) →
  start with `references/local-rules.md`
- **Citation format** → `references/citation-format.md`
- **Canonical URL or citation verification** → start with
  `references/online-sources.md` and hand off to `or-fact-check`
  for per-filing verification
- **Programmatic / structured lookup** (ORS XML, USC XML, eCFR
  API, CourtListener for cite-checking, bulk extraction, change
  detection) → `references/legal-data-apis.md`. Prefer the APIs
  listed there over HTML scraping when the result will be parsed
- **A general civil case** (SJ standard, lodestar, default-
  vacation) → start with `references/key-cases.md`
- **Subject-matter law** (FDCPA, Reg F, consumer protection
  under UTPA, landlord-tenant, family, PI, criminal) → use the
  relevant subject-matter skill (e.g., `or-consumer-debt` for
  debt collection)

## Oregon civil rules

A **single** set of rules — there is no Oregon analog to
Washington's CR / CRLJ split, because Oregon consolidated its
trial courts in 1998.

- **ORCP** — Oregon Rules of Civil Procedure (adopted by the
  Council on Court Procedures under ORS 1.735, with legislative
  approval / non-disapproval)

Key rules:

- **ORCP 1** — applicability; ORCP 1 E permits declarations
  "under penalty of perjury" in lieu of notarized affidavits
- **ORCP 7** — service of summons and complaint; 63-day deadline
  for Return of Service (ORCP 7 D(3))
- **ORCP 9** — service of subsequent papers; ORCP 9 C: 3-day
  mail rule; ORCP 9 G: Certificate of Service
- **ORCP 10** — time computation; defines court days vs.
  calendar days
- **ORCP 15** — pleadings allowed; 30 days to answer (ORCP 7
  C(2))
- **ORCP 17** — signing of pleadings; sanctions for unfounded
  filings
- **ORCP 21** — motions to dismiss / defenses asserted as
  motions; ORCP 21 A(8) = failure to state ultimate facts (the
  Oregon analog to FRCP 12(b)(6))
- **ORCP 23** — amendment of pleadings; "leave shall be freely
  given"
- **ORCP 36** — general scope of discovery; ORCP 36 B(1) =
  relevance + proportionality
- **ORCP 39** — depositions
- **ORCP 43** — requests for production
- **ORCP 44** — physical/mental examination
- **ORCP 45** — requests for admission
- **ORCP 46** — motion to compel; **ORCP 46 A(4)(a)** =
  mandatory fee-shifting on a successful motion to compel
- **ORCP 47** — summary judgment; ORCP 47 C governs filing /
  response / reply schedule
- **ORCP 54** — dismissal; ORCP 54 B = failure to prosecute
- **ORCP 67** — judgments
- **ORCP 68** — costs; **ORCP 68 C(2)–(4)** = statement of
  costs and fees procedure
- **ORCP 69** — default
- **ORCP 71** — relief from judgment or order; the Oregon
  analog to FRCP 60(b)
- **ORCP 81** — interpretation

**Note**: Oregon does **NOT have written interrogatories** under
ORCP as a matter of right. Discovery tools available are:
depositions (ORCP 39), requests for production (ORCP 43),
physical/mental exams (ORCP 44), and requests for admission
(ORCP 45). Some court-annexed arbitration programs allow
interrogatories under arbitrator's discretion. This is a major
distinction from Washington (which has CR 33 interrogatories)
and from the FRCP (which has FRCP 33).

See `references/civil-rules.md` for rule-by-rule coverage.

## Oregon Evidence Code (OEC)

The OEC is codified in **ORS 40.010–40.585**. Numbering parallels
the Federal Rules of Evidence (FRE) at the section level (OEC
401 = relevance; OEC 801 = hearsay definition; OEC 901 =
authentication), but the substantive rules sometimes diverge.

Key sections for civil practice:

- **OEC 401** — relevance
- **OEC 403** — exclusion for prejudice / confusion
- **OEC 602** — personal knowledge
- **OEC 801–803** — hearsay; **OEC 803(6)** = business records
- **OEC 901–902** — authentication; **OEC 902** =
  self-authentication
- **OEC 1001–1008** — best evidence; **OEC 1002** = original
  document rule

See `references/evidence-rules.md` for rule-by-rule coverage and
the business-records / authentication patterns most common in
civil practice.

## Fees and costs

**ORS Ch. 20** — the costs and fees chapter. Recovery mechanisms:

- **ORS 20.075** — factors considered in awarding fees (when fees
  are authorized by statute or contract)
- **ORS 20.077** — fees on a per-claim basis
- **ORS 20.082** — small claims fees
- **ORS 20.083** — fees as costs vs. as part of judgment
- **ORS 20.096** — reciprocal fee-shifting in contract cases
  (when contract has one-sided fee clause, prevailing party of
  either side recovers)
- **ORS 20.105** — fee award against party for objectively
  unreasonable position (rough analog to CR 11 in Washington /
  Rule 11 federal — but distinct standard)
- **ORS 20.140** — in forma pauperis status
- **ORS 20.180** — costs as taxed
- **ORS 20.190** — prevailing-party fees (mandatory $200–$590
  depending on case type)

**ORCP-based fee-shifting**:

- **ORCP 46 A(4)(a)** — mandatory fee-shifting to the prevailing
  party on a motion to compel, unless the opposing party's
  failure was "substantially justified"
- **ORCP 17** — sanctions for unsigned or unfounded pleadings
- **ORCP 32** — class action attorney fees
- **ORCP 54 E** — fees on dismissed claims

**Statutory fee-shifting** (subject-matter-specific):

- **ORS 646.638(3)** — UTPA: prevailing-party fees mandatory
- **15 USC § 1692k** — FDCPA: prevailing-consumer fees mandatory
- **ORS 90.255** — landlord-tenant: prevailing-party fees
  available

See `references/fees-and-costs.md` for full coverage, the
lodestar method, pro-se recovery limits, and pleading templates.

## Local rules

Each Oregon circuit court maintains **Supplemental Local Rules
(SLR)** layered on top of the statewide UTCR and ORCP:

- **Multnomah SLR** — Civil Department: motion practice through
  assigned JA (SLR 5.025), meet-and-confer certification (SLR
  5.045), working copies over 25 pages (SLR 5.100), order
  submission (SLR 5.101)
- **Washington County SLR (Oregon)** — Civil Division scheduling
  (SLR 5.025), simultaneous Notice of Hearing (SLR 5.045),
  meet-and-confer (SLR 5.046), working copies over 15 pages
  (SLR 5.100)
- **Other counties' SLR** — Lane, Marion, Jackson, Deschutes,
  Clackamas, etc.

See `references/local-rules.md` for the full coverage,
inter-county variation, and the interaction with UTCR statewide
formatting.

## Citation format

Oregon uses the **Oregon Appellate Courts Style Manual** (OACSM,
also called the "Oregon Style Manual") published by the OJD.
Form for an Oregon case citation:

> *Smith v. Jones*, 350 Or 1, 250 P3d 100 (2010)

Federal citations are non-Bluebook in Oregon style: `15 USC §
1692k(a)(1)` (no periods in "USC"). See
`references/citation-format.md` for patterns for Oregon and
federal citations, parallel cites, short-form references, and
UTCR / Style-Manual compliance.

## Canonical online sources

`references/online-sources.md` is the AI-agent-friendly catalog
of canonical URLs for:

- Oregon court rules (UTCR, ORCP, OEC, ORAP) — courts.oregon.gov
  and the Council on Court Procedures site
- ORS text — oregonlegislature.gov
- eCFR (for federal regulations)
- Cornell LII (for U.S.C. sections)
- CourtListener and Google Scholar (for case law)
- Multnomah and Washington County SLRs
- OJD eCourt File and Serve (for filing mechanics)

The catalog is the **only approved fetch source** for
verification work. Per the plugin's safety policy, **WebFetch is
the only mechanism used** — no curl, wget, Python requests, or
other bypasses are permitted. See `or-fact-check` for the
per-filing verification workflow.

## Key general-civil cases

`references/key-cases.md` catalogs the general-civil cases this
plugin relies on most:

- **SJ burden**: *Two Two v. Fujitec America, Inc.*, 355 Or 319,
  325 P3d 707 (2014) (no genuine issue of material fact; light
  shifts to non-movant after movant's prima facie showing)
- **SJ inferences favorable to non-movant**: *Jones v. General
  Motors Corp.*, 325 Or 404, 939 P2d 608 (1997)
- **Reciprocal fee-shifting**: *Lemargie v. Johnson*, 212 Or App
  451, 157 P3d 1284 (2007) (ORS 20.096 scope)
- **Lodestar method**: *Strawn v. Farmers Ins. Co. of Oregon*,
  353 Or 210, 297 P3d 439 (2013)
- **American rule baseline / no-fees-without-authority**:
  *Domingo v. Anderson*, 325 Or 385, 938 P2d 206 (1997)
- **ORCP 71 default-vacation**: *Wagar v. Prudential Ins. Co. of
  America*, 276 Or 827, 556 P2d 658 (1976) (excusable neglect
  standard; also discussed in Or App opinions on ORCP 71 B(1))

**Subject-matter cases** — FDCPA, UTPA, business-records
foundation in debt cases, chain-of-title — live alongside their
subject-matter bundle (e.g., `or-consumer-debt/references/
key-cases.md`).

## Notes

- These references are neutral summaries. They do not tell the
  user whether they win or lose.
- Always **verify** a case before citing — Oregon case law has
  evolved on several doctrines (business-records foundation,
  ORCP 71 grounds, fee-shifting scope, ORCP 47 inferences).
- For federal law, check the most recent Ninth Circuit opinion
  where controlling in federal court; Oregon state courts treat
  Ninth Circuit federal-statute interpretations as persuasive.
- **Before filing**, run `or-fact-check` against the packet to
  catch fabricated, misquoted, or superseded citations.
