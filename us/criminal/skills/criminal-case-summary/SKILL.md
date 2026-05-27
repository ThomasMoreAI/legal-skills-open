---
name: criminal-case-summary
title: Criminal Case Summary
description: Produces structured U.S. criminal case summaries covering charges, statutes, evidence, procedural history, disposition, and sentencing. Trigger when the user requests a criminal case summary, charge overview, procedural history, trial or plea summary, verdict recap, or sentencing breakdown.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/criminal-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [litigation, summarization, summary]
---

# Criminal Case Summary

Neutral, verifiable summary of a criminal case from initiation through disposition.

## Required Inputs

1. **Charging documents** — complaint, information, indictment, superseding filings
2. **Docket / timeline** — key dates, hearings, rulings
3. **Motions and orders** — suppression, discovery, evidentiary rulings
4. **Transcripts** — hearings, trial, plea, sentencing
5. **Evidence inventory** — exhibits, reports, forensic results, witness lists
6. **Disposition records** — verdict forms, plea agreement, judgment, sentencing order

## Quick Start

1. Collect all available case materials from the list above.
2. Walk through each section below in order; mark inapplicable sections "Not applicable" with a brief reason.
3. Flag any unverified statute or procedural point with `[VERIFY]`.
4. Review against the pitfalls checklist before delivering.

## Output Sections

### 1. Case Header

| Field | Value |
|---|---|
| Court / Jurisdiction | |
| Case No. | |
| Parties | |
| Judge | |
| Prosecutor | |
| Defense Counsel | |
| Defendant Status | in custody / out / pretrial supervision |

### 2. Charges

List all charges including amended or dismissed counts.

| Count | Statute | Charge | Level | Enhancements | Disposition |
|---|---|---|---|---|---|
| | | | felony / misdemeanor | | pending / dismissed / convicted / acquitted |

- Include statute citations; mark unverified ones `[VERIFY]`.
- Note charging changes with dates and authority (e.g., superseding indictment).

### 3. Core Facts (Neutral)

Concise, non-argumentative narrative covering:
- Key incident date(s) and alleged conduct tied to each count
- Victim/witness identifiers (initials if privacy-sensitive)
- Arrest or charging basis
- Context needed to understand the charges

### 4. Evidence Summary

Cover both prosecution and defense evidence.

| Item | Source | Relevant Count(s) | Admitted / Excluded | Ruling / Notes |
|---|---|---|---|---|

Categories to address: physical, documentary, digital, witness testimony, expert testimony, forensic analysis, demonstrative exhibits, suppression issues.

### 5. Procedural History

Chronological timeline of material events.

| Date | Event | Outcome / Ruling | Citation |
|---|---|---|---|

Include: arraignment, pretrial motions, discovery disputes, continuances, mistrials, trial or plea hearing dates.

### 6. Trial Summary (if tried)

| Phase | Key Points |
|---|---|
| Jury selection | |
| Openings | |
| Prosecution case | |
| Defense case | |
| Rebuttal | |
| Closings | |
| Jury instructions | |
| Deliberations | |

Include objections/rulings only if outcome-relevant.

### 7. Plea Summary (if plea)

Cover: plea type, counts pled, dismissed counts, factual basis, sentencing terms, waivers.

### 8. Verdict / Findings

| Count | Verdict | Special Findings | Notes |
|---|---|---|---|

### 9. Sentencing

| Count | Sentence | Concurrent / Consecutive | Credits | Fines / Restitution | Supervision |
|---|---|---|---|---|---|

Include total custodial term, probation/supervised release, and all conditions.

### 10. Post-Trial / Post-Conviction

Note any: motions for new trial, appeals filed and status, post-conviction relief petitions, sentence modifications.

### 11. Open Issues / Unknowns

List missing documents or unresolved factual/procedural gaps.

## Pitfalls

- **Neutrality** — no advocacy or opinion; do not infer facts beyond the record.
- **Cite sources** — tie evidence and facts to specific counts; reference docket entries, transcripts, or exhibits.
- **Jurisdiction terminology** — respect variations (information vs. indictment, etc.).
- **`[VERIFY]` tag** — use on any uncertain statute citation or procedural point.
- **Privacy** — use initials for victims/witnesses when appropriate.
