---
name: mi-law-references-codearranger
title: Michigan Law References
description: Matter-neutral reference catalog for Michigan civil practice. Contains MCR civil-practice map (Chapters 1-4), Michigan Rules of Evidence (MRE) including business-records exception (MRE 803(6)), self-authentication (MRE 902(11)), fees-and-costs framework, citation format per Michigan Appellate Opinion Manual, landmark Michigan civil and family precedents, and canonical online-sources and data-API catalog. Triggers include "Michigan civil rule", "MCR 2.116", "summary disposition", "Michigan evidence rule", "MRE 803(6)", "MCL 600...", "Michigan citation format", "courts.michigan.gov", "legislature.mi.gov". Other skills cite this one for rule numbers, statute citations, and case authorities. Heavy reference corpora (court-rules, mi-statutes-debt, federal-debt-laws, federal-bankruptcy, ucc-model) live in this skill's `references/` subdirectory.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-law-references
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
- title: Mcr Chapter 1 General
  path: references/court-rules/MCR-chapter-1-general.md
- title: Mcr Chapter 2 Civil
  path: references/court-rules/MCR-chapter-2-civil.md
- title: Mcr Chapter 3 Special Proceedings
  path: references/court-rules/MCR-chapter-3-special-proceedings.md
- title: Mcr Chapter 4 District Court
  path: references/court-rules/MCR-chapter-4-district-court.md
- title: Mre Evidence
  path: references/court-rules/MRE-evidence.md
- title: Readme
  path: references/court-rules/README.md
- title: Evidence Rules
  path: references/evidence-rules.md
- title: Fees And Costs
  path: references/fees-and-costs.md
- title: Key Cases
  path: references/key-cases.md
- title: Legal Data Apis
  path: references/legal-data-apis.md
- title: Elcra
  path: references/mi-statutes-debt/ELCRA.md
- title: Mcpa
  path: references/mi-statutes-debt/MCPA.md
- title: Rcpa Collection Practices
  path: references/mi-statutes-debt/RCPA-collection-practices.md
- title: Readme
  path: references/mi-statutes-debt/README.md
- title: Rja District Court Jurisdiction
  path: references/mi-statutes-debt/RJA-district-court-jurisdiction.md
- title: Rja Limitations
  path: references/mi-statutes-debt/RJA-limitations.md
- title: Rja Summary Proceedings
  path: references/mi-statutes-debt/RJA-summary-proceedings.md
- title: Ucc Article 9
  path: references/mi-statutes-debt/UCC-article-9.md
- title: Child Custody Support
  path: references/mi-statutes-debt/child-custody-support.md
- title: Comparative Fault
  path: references/mi-statutes-debt/comparative-fault.md
- title: Family Divorce
  path: references/mi-statutes-debt/family-divorce.md
- title: Garnishment Exemptions
  path: references/mi-statutes-debt/garnishment-exemptions.md
- title: Holidays
  path: references/mi-statutes-debt/holidays.md
- title: Landlord Tenant
  path: references/mi-statutes-debt/landlord-tenant.md
- title: Online Sources
  path: references/online-sources.md
---

# Michigan Law References

> **NOT LEGAL ADVICE.** Reference catalog only. Read the cited rule,
> statute, or case in full — and confirm it is current — before
> relying on it.

This is the **matter-neutral** reference index for Michigan civil
practice. Other skills in the `mi-court-docs` plugin point here for
rule numbers, statute citations, and case authorities. This skill is
also the physical **host** of the plugin's reference corpora.

## What's here

```
references/
├── civil-rules.md          # MCR civil-practice map (Ch. 1-4)
├── evidence-rules.md       # MRE map (relevance, hearsay, authentication, experts)
├── fees-and-costs.md       # Filing fees + cost / fee-shifting framework
├── citation-format.md      # Michigan Appellate Opinion Manual conventions
├── key-cases.md            # Landmark Michigan civil + family precedents
├── online-sources.md       # Canonical human-facing URLs
├── legal-data-apis.md      # Programmatic access (legislature.mi.gov, CourtListener)
├── court-rules/            # Verbatim MCR / MRE / local-rule text — corpus
├── mi-statutes-debt/       # Michigan Compiled Laws chapters for civil practice — corpus
├── federal-debt-laws/      # FDCPA, FCRA, TILA, etc. (symlink into the
│                           #   shared claude-legal-federal-laws plugin)
├── federal-bankruptcy/     # Title 11 U.S.C. (symlink into shared plugin)
└── ucc-model/              # Model UCC Articles 1/2/3/9 (symlink into shared plugin)
```

The three symlinked corpora (`federal-debt-laws/`,
`federal-bankruptcy/`, `ucc-model/`) point into the shared
`claude-legal-federal-laws` plugin so the federal text is stored once,
not copied per state. The Michigan-specific corpora (`court-rules/`,
`mi-statutes-debt/`) and the seven curated `*.md` index files live
physically under this skill.

## Court structure — terminology

Michigan trial courts and the vocabulary used across this plugin:

| Court | Jurisdiction |
|---|---|
| **Circuit Court** | General-jurisdiction trial court; civil claims over the district-court ceiling, equity, domestic-relations (the Family Division handles divorce, custody, support), and appeals from district court. Michigan circuits are numbered (Wayne County is the **Third Circuit**; Oakland County is the **Sixth Circuit**). |
| **District Court** | Limited-jurisdiction trial court; civil money claims up to the statutory ceiling, landlord-tenant **summary proceedings**, small claims, and civil infractions. Governed by **MCR Chapter 4**. |
| **Probate Court** | Estates, guardianships, conservatorships, and (with the Family Division of Circuit Court) certain juvenile and mental-health matters. |
| **Court of Claims** | Hears certain civil actions against the State (assigned to the Court of Appeals). |

Michigan has **83 counties**. The appellate courts are the **Michigan
Court of Appeals** (intermediate; sits in panels) and the **Michigan
Supreme Court** (court of last resort).

> **Summary disposition, not summary judgment.** Michigan's dispositive
> pretrial motion is the **motion for summary disposition under MCR
> 2.116**, not a "motion for summary judgment." The grounds are
> lettered subrules — most often **(C)(8)** (failure to state a claim,
> tested on the pleadings alone), **(C)(10)** (no genuine issue of
> material fact, tested on documentary evidence), and **(C)(7)**
> (claim barred — e.g., release, prior judgment, statute of
> limitations, immunity). Use the correct subrule; see
> `references/civil-rules.md`.

## Michigan Court Rules (MCR) — civil practice

The MCR govern practice in all Michigan courts. The civil-practice map
lives in `references/civil-rules.md`. The load-bearing chapters:

- **Chapter 1** — general provisions, including **MCR 1.109** (document
  format, signatures, the **(E)** signature-and-sanctions provision,
  and the personal-identifying-information / protected-data rules) and
  **MCR 1.108** (time computation).
- **Chapter 2** — civil procedure for circuit and the like: pleadings
  (**MCR 2.110-2.113**), motions and the general motion practice rule
  (**MCR 2.119**), discovery (**MCR 2.301-2.316**), **summary
  disposition (MCR 2.116)**, default and default judgment (**MCR
  2.603**), and judgments.
- **Chapter 3** — special civil proceedings (including the cross-
  reference to district-court summary proceedings for eviction).
- **Chapter 4** — district court practice: **landlord-tenant /
  summary proceedings (MCR 4.201)** and **small claims (MCR 4.301+)**.

Confirm current subrule lettering, day counts, and dollar ceilings
against the verbatim text in `references/court-rules/` and the
statutes in `references/mi-statutes-debt/` before relying on them.

## Michigan Rules of Evidence (MRE)

The MRE map lives in `references/evidence-rules.md`. The MRE were
**comprehensively restyled effective January 1, 2024** (rule numbers
held stable; wording modernized) — confirm the current text. The two
most load-bearing rules for documentary civil practice (especially
debt-buyer and business-records matters):

- **MRE 803(6)** — the **business-records** hearsay exception. A record
  of a regularly conducted activity is admissible if a custodian or
  other qualified witness (or a self-authenticating certification under
  MRE 902(11)) lays the foundation that it was made at or near the time
  by someone with knowledge, kept in the regular course, and that
  keeping it was the regular practice — unless the source or
  circumstances indicate a lack of trustworthiness.
- **MRE 902(11)** — **self-authentication** of certified domestic
  records of a regularly conducted activity, so no live foundation
  witness is required where the certification and notice requirements
  are met.

Other commonly cited rules: 401-403 (relevance / probative-vs-
prejudicial), 701-703 (lay and expert opinion; **MRE 702** codifies the
*Daubert* reliability standard, adopted in Michigan in 2004), 801-807
(hearsay), 901 (authentication), and the privilege rules. See
`references/evidence-rules.md`.

## Fees and costs

The fees-and-costs framework lives in `references/fees-and-costs.md`.
Michigan follows the **American rule** — each party bears its own
attorney's fees unless a statute, rule, or contract shifts them. Key
hooks:

- Filing-fee amounts under the Revised Judicature Act (**MCL
  600.2401** and the Chapter 24/25 cost and fee provisions) — verify
  current amounts.
- **MCR 2.625** — taxation of costs to the prevailing party.
- **MCR 2.405** — offer-of-judgment **actual-cost** sanctions on a
  rejecting party (now the principal cost-shifting device).
- **MCR 2.403** — case evaluation; the **MCR 2.403(O) case-evaluation
  sanctions were eliminated effective January 1, 2022**, and case
  evaluation is no longer mandatory.
- **MCL 600.2591 / MCR 1.109(E)** — frivolous-filing sanctions (costs
  and reasonable attorney fees against a frivolous claim or defense).

Confirm current dollar amounts with the clerk of the filing court and
against `references/mi-statutes-debt/`.

## Citation format

Michigan uses the **Michigan Appellate Opinion Manual** (the appellate
courts' own style), which differs from the Bluebook. Details and
examples are in `references/citation-format.md`. Highlights:

- **Cases**: party names are **lowercased** and **not italicized** in
  Michigan-style citations (e.g., `people v smith`); reporters are
  `Mich` (Supreme Court official), `Mich App` (Court of Appeals
  official), and `NW2d` (North Western Reporter regional) — e.g.,
  `Maiden v Rozwood, 461 Mich 109; 597 NW2d 817 (1999)`. Note the
  **semicolon** between parallel cites.
- **Statutes**: `MCL 600.5807` (no section symbol; no periods in
  "MCL").
- **Rules**: `MCR 2.116(C)(10)`; `MRE 803(6)`.

## Local rules — where they live

Statewide format is set by **MCR 1.109**. Individual courts adopt
**Local Administrative Orders (LAOs)** approved by the State Court
Administrative Office (SCAO) for venue-specific mechanics (motion-day
scheduling, praecipe practice, chambers copies). E-filing is via
**MiFILE** (the statewide Tyler/Odyssey platform), mandatory in a
growing set of courts — confirm whether e-filing is mandatory in the
venue. See `references/online-sources.md` for the SCAO LAO index and
the MiFILE portal.

## Online sources and data APIs

- Human-facing canonical URLs (courts.michigan.gov for MCR/MRE/forms;
  legislature.mi.gov for MCL; MiFILE; SCAO forms): see
  `references/online-sources.md`.
- Programmatic access (legislature.mi.gov MCL objectName scheme,
  courts.michigan.gov PDFs, CourtListener Michigan Supreme Court +
  Court of Appeals, the connected CourtListener MCP): see
  `references/legal-data-apis.md`.

## Composition

- Every other Michigan skill cites this one for rule numbers, statute
  numbers, and case authorities.
- For statewide document format: `mi-statewide-format`.
- For the filing court's mechanics: `mi-wayne`, `mi-oakland`,
  `mi-circuit-courts`.
- For pro se conventions: `mi-pro-se`.
- For matter-specific bundles: `mi-consumer-debt`.

## References

- `references/civil-rules.md` — MCR civil-practice map
- `references/evidence-rules.md` — MRE map
- `references/fees-and-costs.md` — fees and cost / fee-shifting framework
- `references/citation-format.md` — Michigan Appellate Opinion Manual conventions
- `references/key-cases.md` — landmark Michigan civil + family precedents
- `references/online-sources.md` — canonical human-facing URLs
- `references/legal-data-apis.md` — programmatic access index
- `references/court-rules/` — verbatim MCR / MRE / local-rule corpus
- `references/mi-statutes-debt/` — Michigan Compiled Laws chapters for civil practice
- `references/federal-debt-laws/` — federal-law corpus (symlink)
- `references/federal-bankruptcy/` — Title 11 U.S.C. corpus (symlink)
- `references/ucc-model/` — Model UCC text (symlink)
