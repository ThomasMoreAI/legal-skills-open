---
name: bail-hearing-summary
title: Bail Hearing Summary
description: Generates structured bail hearing summaries from transcripts and case documents, extracting charges, arguments, conditions, and rulings. Use when summarizing bail hearings, pretrial detention decisions, bond hearings, or release condition orders.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bail-hearing-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [litigation, summarization, summary]
---

# Bail Hearing Summary

Produces a structured summary of a bail hearing for quick attorney reference. Extracts charges, prosecution/defense arguments, bail conditions, risk factors, and the court's ruling.

## Prerequisites

1. Charging documents — complaint, indictment, or information with statute citations
2. Hearing transcript or recording
3. Defendant background — criminal history, FTA history if available
4. Party submissions — prosecution/defense bail memoranda, if filed

## Quick Start

1. Gather all source documents (charging docs, transcript, memoranda)
2. Build the header block with case identifiers
3. Extract charges into the charges table
4. Summarize prosecution and defense arguments by category
5. Document the court's ruling, bail amount, and all conditions
6. Note upcoming dates and pending motions

## Output Structure

### Header Block

| Field | Content |
|---|---|
| Case Name | *People/State/United States v. [Defendant]* |
| Case Number | |
| Court / Jurisdiction | |
| Hearing Date | |
| Presiding Judge | |
| Prosecution Counsel | |
| Defense Counsel | |

### Charges

| Count | Statute | Offense | Classification | Degree |
|---|---|---|---|---|
| 1 | | | Felony/Misdemeanor | |

### Prosecution Arguments

Organize under these categories:

- **Flight risk** — prior FTAs, out-of-jurisdiction ties, passport/travel access, financial resources
- **Danger to community** — nature of charges, prior violent history, threats, weapons
- **Strength of evidence** — key evidence cited
- **Bail request** — amount, conditions sought (detention, monitoring, no-contact, passport surrender, geographic restrictions)

### Defense Arguments

Organize under these categories:

- **Community ties** — residence stability, employment, family responsibilities
- **Mitigating factors** — limited criminal history, cooperation, health conditions
- **Proposed conditions** — ROR, reduced bail, supervision alternatives
- **Bail request** — specific amount or release type requested

### Court Ruling

| Element | Detail |
|---|---|
| Bail granted/denied | |
| Amount (if set) | |
| Acceptable form | Cash / Surety / Property / Percentage |
| Court's stated reasoning | |

Conditions imposed (include all that apply):

- Reporting requirements
- Travel restrictions
- Electronic monitoring
- No-contact orders
- Substance abuse testing
- Mental health treatment
- Other special conditions

If bail denied: note remand to custody and reasoning.

### Upcoming Dates & Procedural Notes

- Next court date and purpose
- Filing deadlines
- Pending motions (reconsideration, appeal of bail decision)

## Pitfalls & Checks

- **No advocacy** — present facts and arguments as stated; do not draw legal conclusions
- **Quote key statements** — use direct quotes for significant judicial findings or counsel statements
- **Attribute all facts** — tie every assertion to its source document
- **Jurisdiction awareness** — note which bail statute the court applied (e.g., federal Bail Reform Act 18 U.S.C. § 3142, or state equivalent); never assume jurisdiction unless documents specify
- **Length** — target 2–4 pages depending on hearing complexity
- **Scannability** — use headings, tables, and bullet lists throughout
