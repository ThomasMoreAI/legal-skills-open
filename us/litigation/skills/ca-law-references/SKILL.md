---
name: ca-law-references
title: California Law References — General Civil Practice
description: This skill should be used when the user needs to cite, apply, or research law that bears on California civil court practice across any subject matter. Triggers include "CCP 437c", "Code Civ. Proc., § 437c", "summary judgment California", "CCP 2016", "Civil Discovery Act", "California discovery rules", "CEC 1271", "Cal. Evid. Code § 1271", "business records California", "authentication California evidence", "hearsay exception California", "California citation format", "California Style Manual", "CSM", "Cal.", "Cal.App.", "Cal.Rptr.", "California prevailing party fees", "CCP 1032", "CCP 1033.5", "cost memorandum California", "motion to tax costs", "CCP 998 offer", "Civ. Code § 1717", "attorney fees contract California", "CCP 1021.5 private attorney general", "LASC local rules", "SFSC local rules", "Cal. Rules of Court rule 3.1308", "CRC 3.1300", "CRC 3.700", "case management conference California", "California civil demurrer", "CCP 430.10", "CCP 431.30", "motion to strike California",
  "CCP 435", "California answer deadline", "30 days to answer California", "verify California citation", "Aguilar v. Atlantic Richfield", "Howell v. Hamilton Meats", "collateral source California", "Riverisland parol evidence", "canonical URL California courts", "fetch California court rule". Covers the California Code of Civil Procedure (CCP), the California Evidence Code (CEC, Cal. Evid. Code), California Rules of Court (CRC), fees and costs under CCP §§ 1032 and 1033.5, local rules for LASC, SFSC, OCSC, and other Superior Courts, general civil key cases, the California Style Manual citation conventions, and the canonical online-sources catalog for fetching current rule text, statutes, and case law. For subject-matter-specific law (debt collection under Rosenthal FDCPA or the UCL, landlord-tenant, family, personal injury), compose with the relevant subject-matter skill (e.g., ca-consumer-debt).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# California Law References — General Civil Practice

This skill is a matter-neutral reference index — a pointer to the
statutes, rules, and doctrines most often invoked in California
civil practice *across any subject matter*. The body below
summarizes each source. Detailed sections, elements, and citation
examples live in `references/`.

> **NOT LEGAL ADVICE.** These notes are drafting aids, not legal
> advice. Every citation should be verified against the current
> CCP, current court rule, or current case law before it goes
> into a filing. Use `ca-fact-check` before any packet is filed.

## How to use this skill

Ask: *what is the user trying to establish procedurally?*

- **A procedural motion** (demurrer, motion to strike, motion to
  compel, summary judgment, default, vacate) → start with
  `references/civil-rules.md`
- **An evidentiary objection** (hearsay, authentication, best
  evidence, foundation, privilege) → start with
  `references/evidence-rules.md`
- **A fee-and-cost request or objection** → start with
  `references/fees-and-costs.md`
- **A local-rule question** (LASC, SFSC, OCSC, or other
  Superior Court local rules) → start with
  `references/local-rules.md`
- **Citation format** → `references/citation-format.md`
- **Canonical URL or citation verification** → start with
  `references/online-sources.md` and hand off to `ca-fact-check`
  for per-filing verification
- **Programmatic / structured lookup** (California codes XML,
  USC XML, eCFR API, CourtListener for cite-checking, bulk
  extraction, change detection) → `references/legal-data-apis.md`.
  Prefer the APIs listed there over HTML scraping when the result
  will be parsed
- **A general civil case** (SJ standard, lodestar, default
  vacation, collateral source) → start with
  `references/key-cases.md`
- **Subject-matter law** (FDCPA, Rosenthal Act, UCL, CLRA, FDBPA,
  landlord-tenant, family, PI) → use the relevant subject-matter
  skill (e.g., `ca-consumer-debt` for debt collection)

## California civil rules

California civil practice draws on **three overlapping rule sets**:

1. **California Code of Civil Procedure (CCP)** — the primary
   procedural statute; covers pleadings, service, motions,
   discovery, trial, judgment, and post-judgment. Enacted by the
   Legislature; codified at Cal. Code Civ. Proc. §§ 307–1062.

2. **California Rules of Court (CRC)** — promulgated by the
   Judicial Council under Cal. Const. art. VI, § 6. CRC
   Title 2 covers trial court rules; CRC Title 3 covers civil
   rules in detail. CRC governs format (CRC 2.100-2.119), case
   management (CRC 3.700-3.770), and motion practice (CRC
   3.1100-3.1390).

3. **Local rules** — each Superior Court adopts local rules
   under CRC 3.20, limited to matters not covered by the CRC.
   Los Angeles Superior Court (LASC), San Francisco Superior
   Court (SFSC), and Orange County Superior Court (OCSC) have
   the most extensive local rule sets.

Key CCP provisions at a glance:

- **CCP § 412.20** — Service of summons; required contents
- **CCP § 413.10** — Manner of service; personal, substituted,
  mail (with notice and acknowledgment)
- **CCP § 415.20** — Substituted service (dwelling, office)
- **CCP § 417.10** — Proof of service; date service complete
- **CCP § 430.10** — Grounds for demurrer to complaint
- **CCP § 430.30** — Timing for demurrer
- **CCP § 431.30** — Contents of answer; general / specific
  denial; affirmative defenses
- **CCP § 435** — Motion to strike (improper matter or matter
  not drawn in conformity with law)
- **CCP § 437c** — Summary judgment/adjudication (the keystone
  provision for pre-trial dispositive motions)
- **CCP §§ 1010-1020** — Notices and motions (general)
- **CCP §§ 2016.010-2036.050** — Civil Discovery Act of 1986
  (interrogatories, depositions, document production, RFAs,
  physical/mental examinations, experts)
- **CCP §§ 583.110-583.430** — Time to bring an action to trial
  (mandatory/discretionary dismissal for delay)
- **CCP §§ 664-681** — Judgments; entry, renewal, enforcement
- **CCP §§ 683.010-708.320** — Enforcement of judgments

See `references/civil-rules.md` for provision-by-provision coverage.

## California Evidence Code (CEC)

The CEC is codified in **Cal. Evid. Code §§ 1-1605** and enacted
by the Legislature (unlike the Federal Rules of Evidence, which
are court rules). Key provisions for civil practice:

- **Cal. Evid. Code § 350** — Relevance
- **Cal. Evid. Code § 352** — Exclusion for prejudice / confusion
- **Cal. Evid. Code §§ 900-1070** — Privileges (attorney-client,
  physician-patient, psychotherapist, spousal, trade secret, etc.)
- **Cal. Evid. Code §§ 1200-1390** — Hearsay; key exceptions:
  - **§ 1220** — Party admission
  - **§ 1271** — Business records (records made in the regular
    course of business by persons with knowledge)
  - **§ 1280** — Official records / public records
  - **§ 1310** — Statement by decedent
  - **§ 1370** — Threat statement
- **Cal. Evid. Code §§ 1400-1454** — Authentication and
  identification; **§ 1421** — authentication by content
- **Cal. Evid. Code §§ 1500-1567** — Secondary evidence rule
  (California's analog to the best-evidence rule)

**Important CEC/FRE distinctions**: California enumerates
hearsay exceptions in detail; there is no FRE 807-style residual
exception. The CEC § 1271 business-records foundation mirrors
FRE 803(6) closely but differs in exact language. California
privileges (§§ 900-1070) are broader and more numerous than
federal common-law privilege doctrine.

See `references/evidence-rules.md` for rule-by-rule coverage and
the business-records / authentication patterns most common in
civil practice.

## Fees and costs

California follows the **American Rule** as its baseline: each
party bears its own attorney fees absent statute, contract, or
other legal authority. *Trope v. Katz* (1995) 11 Cal.4th 274, 278.

Key cost-recovery provisions:

- **CCP § 1032** — Prevailing party is entitled to costs as a
  matter of right in most civil actions; "prevailing party"
  defined broadly to include judgment creditors and parties whose
  claims or defenses are dismissed with prejudice
- **CCP § 1033.5** — Allowable items: filing fees, service
  costs, deposition costs, jury fees, witness fees (incl.
  expert witness fees where court-ordered), interpreter fees,
  models, blowups. Not allowable: ordinary photocopying,
  postage, attorney travel, consultant fees
- **Civ. Code § 1717** — Reciprocal fee-shifting in contract
  actions: when a contract provides attorney fees to one side,
  the prevailing party on either side recovers under the clause
- **CCP § 1021.5** — Private attorney general fees: available
  when the action enforces an important right affecting the
  public interest, a significant benefit accrues to the public
  or class, and the necessity and financial burden of private
  enforcement make a fee award appropriate
- **CCP § 998** — Offer to compromise: if a plaintiff rejects a
  defendant's § 998 offer and fails to obtain a more favorable
  judgment, the plaintiff must pay post-offer costs including
  expert witness fees; reciprocal if defendant rejects
  plaintiff's offer

See `references/fees-and-costs.md` for full coverage, the
lodestar method, CCP § 1033.5 allowable-costs detail, and sample
memorandum of costs language.

## Local rules

Each California Superior Court adopts its own local rules within
the limits set by CRC 3.20. Rules address case assignment, trial
management, ex parte applications, discovery motions, and ADR.

- **LASC** (Los Angeles Superior Court) — the largest trial
  court in the nation; LASC Local Rules govern via lacourt.org
- **SFSC** (San Francisco Superior Court) — sfsuperiorcourt.org;
  Presiding Department for civil case management
- **OCSC** (Orange County Superior Court) — occourts.org;
  complex litigation department
- **Other populous counties** — San Diego, Riverside, San
  Bernardino, Sacramento, Santa Clara, Alameda, Contra Costa,
  Fresno, etc.

See `references/local-rules.md` for the high-volume courts, local
rule structure, and motions calendaring mechanics.

## Citation format

California uses the **California Style Manual** (CSM), published
by the Judicial Council. California citations diverge from Bluebook
in notation, comma placement, and statute format:

**Case**: *Aguilar v. Atlantic Richfield Co.* (2001) 25 Cal.4th 826

**Statute**: Code Civ. Proc., § 437c (note the comma and the §)

**Rule**: Cal. Rules of Court, rule 3.1308

**Unpublished opinions** are generally not citable under CRC 8.1115.

See `references/citation-format.md` for complete patterns,
parallel cites, short forms, and comparison to Bluebook.

## Canonical online sources

`references/online-sources.md` is the AI-agent-friendly catalog
of canonical URLs for:

- California court rules (CRC, local rules) — courts.ca.gov
- California Codes (CCP, CEC, Civ. Code, etc.) —
  leginfo.legislature.ca.gov
- Case opinions — courts.ca.gov/opinions
- Judicial Council forms — courts.ca.gov/forms
- eCFR (for federal regulations)
- Cornell LII (for U.S.C. sections)
- CourtListener and Google Scholar (for case law)
- LASC, SFSC, OCSC county court websites

The catalog is the **only approved fetch source** for
verification work. Per the plugin's safety policy, **WebFetch is
the only mechanism used** — no curl, wget, Python requests, or
other bypasses are permitted. See `ca-fact-check` for the
per-filing verification workflow.

## Key general-civil cases

`references/key-cases.md` catalogs the general-civil cases this
plugin relies on most:

- **SJ standard**: *Aguilar v. Atlantic Richfield Co.* (2001)
  25 Cal.4th 826 (burden-shifting framework for summary
  judgment under CCP § 437c)
- **Collateral source rule**: *Howell v. Hamilton Meats &
  Provisions* (2011) 52 Cal.4th 541 (injured plaintiff
  recovers only amounts actually billed and paid, not full
  reasonable value)
- **FEHA**: *Reid v. Google, Inc.* (2010) 50 Cal.4th 512
  (stray-remarks doctrine in employment discrimination)
- **Parol evidence**: *Riverisland Cold Storage, Inc. v.
  Fresno-Madera Production Credit Assn.* (2013) 55 Cal.4th 1169
  (fraud exception to parol evidence rule)
- **Premises liability**: *Wiener v. Southcoast Childcare
  Centers, Inc.* (2004) 32 Cal.4th 1138 (duty of care;
  foreseeability)

**Subject-matter cases** — FDCPA, Rosenthal Act, UCL, CLRA,
business-records foundation in debt cases, chain-of-title —
live alongside their subject-matter bundle (e.g.,
`ca-consumer-debt/references/key-cases.md`).

## Notes

- These references are neutral summaries. They do not tell the
  user whether they win or lose.
- Always **verify** a case before citing — California case law
  has evolved on several doctrines (SJ burden, collateral
  source, business-records foundation, § 998 offers).
- For federal law, check the most recent Ninth Circuit opinion
  where controlling in federal court; California state courts
  treat Ninth Circuit federal-statute interpretations as
  persuasive.
- **Before filing**, run `ca-fact-check` against the packet to
  catch fabricated, misquoted, or superseded citations.

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
