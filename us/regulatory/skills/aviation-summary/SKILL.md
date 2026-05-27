---
name: aviation-summary
title: Aviation Law Summary
description: 'Generates structured U.S. aviation-law summaries by synthesizing FAA, DOT, and TSA rules, treaties, and precedent into actionable legal analysis. Use when briefing on air traffic rights, aircraft operations, airworthiness, carrier liability, or incident/compliance exposure. Trigger: aviation law, FAA, DOT, TSA, 14 CFR, Part 121/125/135, Montreal Convention, Warsaw Convention, ICAO, route authority, code-sharing, slot allocation, accident liability.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/aviation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Aviation Law Summary

Produces a structured, defensible aviation-law summary for counsel, aviation operators, regulators, and legal teams.

## Prerequisites

Gather before starting:

1. **Issue statement** — legal question, party posture, desired depth, decision use (advisory, compliance memo, litigation prep).
2. **Jurisdiction** — U.S. federal at minimum; add foreign states when international carriage is involved.
3. **Sources** — uploaded documents + whether fresh legal research is permitted.
4. **Audience** — client-facing vs internal counsel tone.
5. **Constraints** — confidentiality limits, preferred citation standards.

## Quick Start

1. Triage sources (uploaded files → primary law → secondary → gap list).
2. Build authority table with citations, pinpoints, and confidence levels.
3. Draft summary sections (see below).
4. Run the analytical checklist.
5. Mark every unconfirmed authority with `[VERIFY]`.

## Core Workflow

### 1. Source Triage

| Priority | Source | Action |
|---|---|---|
| 1 | Uploaded matter files | Extract facts, governing instruments, cited authorities, dates, procedural posture |
| 2 | Primary law | Pull statutes/regulations/treaties/cases; capture exact text and effective dates |
| 3 | Secondary sources | Context/trend analysis only; never sole basis for a legal rule |
| 4 | Gap assessment | Flag missing facts/authority; list what is needed to complete |

### 2. Authority Capture

| Type | Citation | Pinpoint | Jurisdiction | Core Holding/Rule | Relevance | Confidence |
|---|---|---|---|---|---|---|
| Statute/Regulation | | | US/Federal/State/Foreign | | | |
| Treaty/Convention | | | | | | |
| Case Law | | | | | | |
| Agency Rule/Order | | | | | | |

Add `[VERIFY]` to any citation, version, or quote not independently confirmed.

### 3. Required Summary Sections

| Section | Minimum Content |
|---|---|
| Executive Overview | Core issue, controlling framework, top 5 takeaways, immediate risks |
| Regulatory Stack | FAA regime, DOT/TSA overlays, state law interactions, treaty intersections |
| Jurisdictional Map | Domestic vs international application; country-of-treatment analysis |
| Case Law Matrix | Case, citation, facts, holding, reasoning, practical effect, splits |
| Liability & Exposure | Accident/cargo/passenger exposure; limitation defenses; insurance/indemnity |
| Operations & Compliance | Certification, training, maintenance, reporting, record-retention, remedial controls |
| Enforcement & Proceedings | Civil/admin pathways, penalties, certificate actions, appeals, criminal thresholds |
| Emerging Issues | UAS, advanced air mobility, commercial space overlaps, open regulatory questions |
| Table of Authorities | Bluebook-formatted citations with pinpoints |
| Recommendations | Priority actions, documentation plan, escalation points, monitoring triggers |

### 4. Analytical Checklist

- Distinguish regime by claim type:
  - Passenger/cargo claims: international carriage framework vs domestic.
  - Operational compliance: routes, slots, code-sharing.
  - Incident/accident: regulatory reporting vs civil exposure.
- Determine if treaty regime preempts or coexists with U.S. law.
- Confirm whether liability caps/defenses apply and when lost.
- Separate regulatory violation from tort exposure (no automatic civil shield).
- Track retroactivity and effective-date impacts.

## Pitfalls

- **No fabricated citations** — never invent holdings, citations, or amendment dates.
- **Thin sources** — state "insufficient authority" and list exact missing items.
- **Jurisdictional uncertainty** — flag explicitly (state law overlay, treaty ratification timelines, forum clauses).
- **Scope caveat** — note when external search was used vs document-only analysis.
- **U.S. federal first** — escalate to foreign-source harmonization only when the fact pattern requires it.
- **Neutral tone** — evidence-first wording; avoid overbroad conclusions.
