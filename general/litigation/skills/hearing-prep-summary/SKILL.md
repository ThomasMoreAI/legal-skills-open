---
name: hearing-prep-summary
title: Hearing Preparation Summary
description: Produces a quick-reference hearing preparation summary synthesizing pleadings, evidence, witnesses, and governing law into issue matrices, exhibit cross-references, and procedural checklists. Use when preparing for motion hearings, evidentiary hearings, trials, administrative or arbitration hearings, or when asked for "hearing prep," "trial prep summary," "hearing brief," or "prep memo."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hearing-prep-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Hearing Preparation Summary

Single document that orients counsel, frames issues, and serves as a fast in-hearing reference. Covers every hearing type—motion, evidentiary, trial, administrative, arbitration.

## Prerequisites

Gather before starting:

1. Hearing notice/order (date, time, forum, scope)
2. Operative pleadings and amendments
3. Key motions, briefs, and oppositions
4. Docket sheet and relevant prior orders
5. Evidence: exhibits, declarations, discovery excerpts, transcripts
6. Witness list with contact info and prior statements
7. Applicable rules and authorities (or a request to research them)

## Output Sections

Fill every section that applies. Omit sections that are irrelevant to the hearing scope.

### 1. Hearing Snapshot

| Field | Value |
|---|---|
| Hearing type | |
| Date / time | |
| Location / courtroom / link | |
| Judge / officer / panel | |
| Matter(s) set | |
| Time limits | |
| Burdens of proof | |
| Applicable rules | |

### 2. Case Background

5–10 chronological, fact-only bullets with source citations.

### 3. Procedural Posture

| Item | Date | Source | Impact |
|---|---|---|---|
| Complaint / petition | | | |
| Answer / response | | | |
| Key motions / rulings | | | |
| Pending issues | | | |

### 4. Issues Matrix

Core section. One row per disputed issue.

| Issue | Standard | Moving party position | Opposing position | Key facts | Key authorities | Evidence tie-ins |
|---|---|---|---|---|---|---|

### 5. Legal Standards & Authorities

Include pin cites when available. Flag uncertain citations with `[VERIFY]`.

| Issue | Statute / Rule | Leading cases | Notes |
|---|---|---|---|

### 6. Evidence & Exhibits

| Exhibit ID | Description | Authenticity status | Relevance to issue | Sponsor witness |
|---|---|---|---|---|

### 7. Witnesses

| Witness | Role | Expected testimony | Prior statements | Cross targets | Impeachment |
|---|---|---|---|---|---|

### 8. Evidentiary / Procedural Flags

Include only what is relevant:

- Foundation / authentication gaps to cure
- Hearsay risks and available exceptions
- Motions in limine status and rulings
- Likely objections from each side
- Expert admissibility issues (methodology, qualifications, relevance)

### 9. Strategy & Risk

| Strengths | Weaknesses | Opponent likely themes | Recommended responses | Settlement / stipulation leverage |
|---|---|---|---|---|

### 10. Hearing Logistics & Deadlines

- Briefing or exhibit exchange deadlines
- Required filings (trial brief, witness list, exhibit list, proposed order)
- Tech needs (presentation, video, remote witness)
- Courtroom procedures (local rules, standing orders)
- Interpreter or accessibility needs

### 11. Examination Outlines

Include only if testimony is expected.

```
Witness: [Name]
Purpose: [Theme + issue]
Direct:
  - Topic 1: [Q objectives]
  - Topic 2: [Q objectives]
Cross:
  - Topic 1: [Impeachment / concession]
  - Topic 2: [Contradiction / bias]
```

### 12. Open Items

Actionable items with owner and due date if known.

## Guardrails

- Cite sources for every factual assertion and quote.
- Separate facts from arguments; label advocacy explicitly.
- Never assume law or local rules—verify and mark uncertainties with `[VERIFY]`.
- Prefer tables and checklists over narrative.
- Stay within hearing scope; omit unrelated case history.
- Note jurisdiction and forum in the Hearing Snapshot; adjust standards accordingly.
