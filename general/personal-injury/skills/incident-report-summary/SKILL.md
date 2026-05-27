---
name: incident-report-summary
title: Incident Report Summary
description: 'Generates structured, litigation-ready summaries from police reports, crash reports, workplace incident reports, or investigative documents. Extracts parties, narratives, citations, witnesses, contributing factors, and visual documentation into a standardized format. Use when summarizing an incident report for case assessment, discovery planning, or liability evaluation; trigger keywords: police report, accident report, crash report, incident summary, report summary, investigative report.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/incident-report-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: personal-injury
language: en
tags: [litigation, summarization]
---

# Incident Report Summary

Extracts a structured, self-sufficient summary from a police or incident report so an attorney can assess facts, parties, and issues without the original document.

## Prerequisites

1. Source report (police, crash, workplace, or investigative document).
2. All attachments — supplements, witness forms, diagrams, photos.
3. Matter identifier — case name or number.

## Quick Start

1. Identify report type and adapt extraction fields accordingly (e.g., skip vehicle info for workplace incidents).
2. Extract each section below in order.
3. Flag every gap, contradiction, or ambiguity.
4. Verify every fact traces to specific source language — no inference.

## Output Sections

Produce sections in the order listed.

### 1. Header

| Field | Extract |
|---|---|
| Report/Case Number | Official identifier |
| Incident Date/Time | Include time zone if available |
| Report Filed Date | If different from incident date |
| Location | Full address, intersection, or mile marker |
| Agency | Name, officer/investigator, badge number |
| Report Type | Collision, criminal, workplace, etc. |

### 2. Parties Involved

Per party, extract:

- **Role** — Driver / Passenger / Pedestrian / Victim / Suspect / Reporting Party / Employee
- **Name** — full legal name
- **DOB / Age**
- **Address**, **Contact** (phone, email)
- **ID** — license number + state, or employee ID
- **Vehicle** (if applicable) — year, make, model, color, VIN, plate
- **Insurance** (if applicable) — carrier, policy number
- **Injuries noted** — as described in report

### 3. Narrative Summary

Provide two versions:

- **Complete narrative** — preserve the officer/investigator's full account.
- **Key facts extract** — legally significant facts only:
  - Fault admissions
  - Impairment / recklessness / distraction observations
  - Physical evidence (skid marks, distances, measurements)
  - Injury descriptions
  - Safety equipment use or non-use
  - Environmental conditions

Flag ambiguities, contradictions, and temporal gaps.

### 4. Citations / Charges

| Person Cited | Statute/Code | Description | Issued At Scene? | Court Date | Penalty |
|---|---|---|---|---|---|

### 5. Witnesses

Per witness:

| Field | Detail |
|---|---|
| Name | Full name |
| Contact | Phone, address, email |
| Relationship | Independent or party-related |
| Location at incident | Position and facing direction |
| Statement summary | Key observations in their words |

- Preserve direct quotes verbatim (excited utterances / hearsay exceptions).
- Flag witnesses identified but not interviewed.
- Flag references to unidentified potential witnesses.

### 6. Contributing Factors

| Category | Examples | Evidence Source |
|---|---|---|
| Environmental | Weather, lighting, road surface, visibility | Physical evidence / narrative |
| Human | Speed, inattention, impairment, fatigue | Witness / admission / observation |
| Equipment | Mechanical failure, defects | Inspection / narrative |
| Systemic | Training gaps, hazardous conditions | Report findings |

Flag factors suggesting:
- **Third-party liability** — road design defects, product defects, employer violations
- **Affirmative defenses** — comparative negligence, assumption of risk, intervening cause

### 7. Visual Documentation

Describe each diagram, sketch, or photo:

- **Collision diagrams** — road layout, lanes, traffic controls, vehicle positions (pre/during/post), point of impact, final rest, measurements.
- **Photos** — subject, perspective, visible damage/injuries, evidence markers.
- Note information in visuals absent from the narrative.

### 8. Gaps and Follow-Up

- [ ] Missing party contact information
- [ ] Uninterviewed or unidentified witnesses
- [ ] Narrative contradictions needing deposition clarification
- [ ] Missing supplemental reports referenced but not attached
- [ ] Unclear measurements or diagram elements
- [ ] Pending lab results, toxicology, or reconstruction reports

## Checks

- Every fact must trace to specific source language — no inference or speculation.
- Distinguish officer's direct observations from relayed information.
- Use consistent date (MM/DD/YYYY) and time format throughout.
- Adapt fields to report type — omit inapplicable sections.
- Protect PII not relevant to liability or damages.
- Use [VERIFY] on any uncertain extraction.
