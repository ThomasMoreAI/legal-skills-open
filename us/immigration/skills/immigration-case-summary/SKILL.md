---
name: immigration-case-summary
title: Immigration Case Summary
description: 'Produces structured U.S. immigration case summaries covering applicant background, legal basis, procedural history, posture, and outcomes. Use when preparing case summaries, intake briefs, supervision reviews, handoffs, or client consultations. Trigger keywords: immigration summary, asylum, AOS, removal defense, I-589, I-485, I-130, I-140, NTA, RFE, NOID, EOIR, BIA, USCIS.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/immigration-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: immigration
language: en
---

# Immigration Case Summary

Summarizes an immigration matter into a scan-ready brief of facts, law, posture, and outcome.

## Prerequisites

Before starting, confirm availability of:

- Complete case file (filings, notices, decisions, transcripts, correspondence)
- Benefit/relief type (asylum, AOS, family-based, removal defense, appeal)
- Forum(s) (USCIS, EOIR/IJ, BIA, federal circuit, or mixed)
- Key dates (filing, RFE/NOID, interview/hearing, decisions, appeal deadlines)
- Confidentiality scope (redactions, sensitivity flags for trauma/medical/minors)

## Workflow

1. Identify benefit/relief and governing authority from the record
2. Extract applicant background and eligibility elements with cited evidence
3. Build chronological procedural timeline with agency/court actions
4. State current posture and deadlines; note risks and open items
5. Flag missing records or conflicts

## Output Template

```
## Matter Snapshot

| Field | Value |
|---|---|
| Client/Applicant | |
| Country of Origin | |
| A-Number / USCIS Receipt(s) | |
| Benefit/Relief Sought | |
| Forum(s) | |
| Counsel of Record | |
| Current Posture | |
| Last Updated | |

## Applicant Background

- Immigration history (entries, status changes, overstays):
- Family relationships (petitioner/beneficiary, derivatives):
- Employment/education:
- Relevant vulnerabilities or equities:
- Adverse factors (criminal, fraud, removability grounds):

## Legal Basis

- Statute/Regulation/Policy: exact INA/CFR/PM citations from record
- Eligibility elements: map each element to evidence
- Discretionary factors (if applicable):

## Evidence Inventory

| Element / Issue | Key Evidence | Gaps |
|---|---|---|

## Procedural History

| Date | Event | Forum | Outcome / Notes |
|---|---|---|---|

## Decisions & Outcomes

- Decision(s): approvals/denials/termination/remand with dates
- Grounds for decision (quote or summarize from decision)
- Appeal/motion status and deadlines

## Key Issues / Risks

- Inconsistencies or adverse evidence:
- Statutory bars or procedural defects:
- Credibility concerns or corroboration gaps:

## Next Steps

- Required filings and deadlines:
- Evidence to obtain:
- Strategy notes:
```

## Pitfalls

- **Never invent citations.** Mark uncertain legal citations as `[VERIFY]`.
- **Distinguish forum standards.** USCIS, EOIR, BIA, and circuit courts apply different standards — note which applies.
- **Capture RFE/NOID/NTA details verbatim** when critical to posture.
- **Flag record conflicts** — cite both sources; do not resolve silently.
- **Maintain confidentiality** — omit sensitive details unless required for analysis.
