---
name: claim-construction-chart
title: Joint Claim Construction Chart
description: Drafts Joint Claim Construction Charts for patent litigation Markman hearings in US federal courts. Organizes disputed claim terms with competing party constructions, intrinsic/extrinsic evidence citations, and agreement status. Use when preparing claim construction charts, Markman hearing exhibits, or joint prehearing statements in IP litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/claim-construction-chart
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Joint Claim Construction Chart

Drafts a joint claim construction chart presenting parties' competing interpretations of disputed patent claim terms for Markman proceedings.

## Prerequisites

- Asserted patent(s): number, title, issue date, inventors, full claim text
- Case caption: party names, court/division, civil action number
- Identified disputed terms from contentions or meet-and-confer
- Parties' proposed constructions with supporting intrinsic evidence
- Prosecution history: office action responses, amendments, examiner statements
- Applicable local patent rules (e.g., N.D. Cal., E.D. Tex., D. Del.)

## Quick Start

1. Gather patent documents, disputed terms, and both parties' proposed constructions
2. Identify the district's local patent rules for formatting requirements
3. Build the disputed terms table with per-term evidence citations
4. Classify each term as agreed, partially agreed, or disputed
5. Add certifications and signature blocks per local rules

## Output Structure

### Caption and Cover

Include: court (full designation with division), all parties, civil action number, patent(s) with number/title/issue date/inventors, and document title per local rules ("Joint Claim Construction Chart" or "Joint Claim Construction and Prehearing Statement").

### Disputed Terms Table

One row per disputed term with these columns:

| Column | Content |
|--------|---------|
| No. | Sequential or claim-order number |
| Claim Term | Exact language from patent |
| Claim No(s). | All claims where term appears |
| Context | Surrounding claim language for court reference |
| Plaintiff's Construction | Plain-language meaning + intrinsic evidence |
| Defendant's Construction | Plain-language meaning + intrinsic evidence |
| Agreement Status | Agreed / Partial / Disputed |

### Evidence Citations

For each proposed construction, cite intrinsic evidence:

- **Specification** — col:line (utility) or paragraph number (applications)
- **Claims** — related claim language providing definitional context
- **Prosecution history** — office action responses, amendments, applicant arguments
- **Figures/embodiments** — specific figures illustrating term meaning

All constructions follow *Phillips v. AWH Corp.*, 415 F.3d 1303 (Fed. Cir. 2005) (en banc): terms receive ordinary and customary meaning to a POSITA at time of invention, read in light of specification and prosecution history.

If extrinsic evidence is used, it is subordinate to intrinsic evidence per *Phillips*. Acceptable types: contemporaneous technical dictionaries/treatises, expert declarations (with qualifications and POSITA basis), prior art showing terminology usage, admissible inventor testimony.

### Agreement and Disagreement

For each term, classify as:

- **Full agreement** — present agreed construction; note no judicial construction needed
- **Partial agreement** — state agreed portions, isolate remaining disputes
- **Full disagreement** — summarize dispute nature (scope, embodiment limitation, prosecution history impact, indefiniteness)

### Indefiniteness Contentions

If a term is challenged under 35 U.S.C. § 112(b):

- State position in defendant's construction column
- Apply *Nautilus, Inc. v. Biosig Instruments, Inc.*, 572 U.S. 901 (2014): whether claim "inform[s] those skilled in the art about the scope of the invention with reasonable certainty"
- Provide factual and legal basis

### Certifications and Signatures

- Signature blocks for lead counsel (each party): name, bar number, firm, address, phone, email
- Meet-and-confer certification: dates, participants, good-faith compliance with local patent rules
- Any additional certifications required by local rules

## Checks and Pitfalls

- **Pin-cite everything** — specification col:line, prosecution history date/page, case reporter/page
- **Mirror structure** — defendant's section must parallel plaintiff's format exactly
- **Bluebook citations** — proper case names, reporters, pinpoints, parentheticals
- **USPTO conventions** — patent number, inventor names, issue date, col:line references
- **District-specific compliance** — check local rules for meet-and-confer requirements, page limits, font/margin rules, joint vs. separate filing
- **Jury-suitable constructions** — plain-language meanings understandable to a lay jury
- **Omit agreed terms** unless local rules require listing them
- **Flag same-term-different-context** — a term in multiple claims may warrant different constructions
- **Group related terms** by technology concept or claim element when logical
