---
name: litigation-support-summary
title: Litigation Support Summary
description: Generates structured management summaries of active commercial litigation matters. Covers case overview, procedural posture, strategy, deadlines, discovery status, budget, and risk analysis. Use when preparing case status reports, onboarding stakeholders to active litigation, or conducting periodic case reviews.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/litigation-support-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Litigation Support Summary

Synthesizes case materials into a structured management document (5-10 pages) for legal teams and clients to track progress on active litigation.

## Quick Start

1. Gather inputs: pleadings, docket sheet, court orders, discovery materials, scheduling orders
2. Follow the six-section output structure below
3. Apply the quality checks before delivering

## Required Inputs

- **Case file**: pleadings, court orders, docket sheet, case caption/number, presiding judge
- **Discovery materials**: requests, responses, production logs, deposition transcripts
- **Scheduling orders**: court-imposed deadlines, trial date, expert disclosure dates
- **Correspondence** (if available): strategic memos, client communications
- **Budget/staffing** (if available): litigation budget, team assignments

## Output Structure

### 1. Case Overview & Procedural Posture

| Field | Content |
|-------|---------|
| Caption & Docket | Full case caption, docket number |
| Court & Judge | Court, jurisdiction, presiding judge |
| Parties | All parties with roles |
| Claims & Defenses | Each cause of action/counterclaim with status |
| Procedural Stage | Pleadings / discovery / pre-trial / trial |
| Significant Rulings | Key motions, hearings, orders |

### 2. Strategy & Theory of Case

- Primary legal theories and key factual arguments
- Desired outcome (damages, injunctive relief, dismissal, etc.)
- Strategy evolution based on discovery/rulings/new facts
- Candid strengths/weaknesses for both sides:

| Factor | Our Position | Opposing Position |
|--------|-------------|-------------------|
| Strongest argument | | |
| Key vulnerability | | |
| Critical unresolved issue | | |

- ADR/settlement posture: demand/offer history, mediation prospects

### 3. Timeline & Critical Deadlines

Chronological table covering discovery cutoffs, expert disclosures, dispositive motion deadlines, pretrial conferences, trial date, and internal targets.

| Date | Event/Deadline | Status | Action Required |
|------|---------------|--------|-----------------|
| _past_ | Event | Complete | -- |
| _upcoming_ | Deadline | Pending | Owner + prep needed |

Flag deadlines requiring immediate attention.

### 4. Discovery Status & Key Evidence

**Written discovery** (interrogatories, doc requests, RFAs): track served, received, outstanding, disputes.

**Depositions**: witness, date, status (completed/scheduled/needed), key testimony.

**Critical evidence**: most significant documents/testimony and relevance to case theory.

**Open issues**: privilege disputes, protective orders, Daubert challenges, outstanding productions.

### 5. Resource Allocation & Budget

Track by category (attorney fees, experts, e-discovery, court reporters, travel): budget, spent, projected remaining. Include team assignments and resource constraints.

Omit if no budget data available; note the gap and recommend gathering it.

### 6. Risks, Opportunities & Recommendations

- **Risks**: adverse outcome exposure (liability + damages range), cost escalation triggers, reputational concerns
- **Opportunities**: favorable developments, settlement leverage, dispositive motion prospects
- **Recommendations**: numbered, actionable next steps with priority (High/Medium/Low) and owner

## Quality Checks

- Cite specific documents by name and page/paragraph when asserting facts
- Distinguish established facts, disputed facts, and legal contentions
- Provide candid assessments, not advocacy; flag information gaps
- Use accessible language while maintaining legal precision; define terms of art on first use
- Note the summary date; frame as a living document
- Mark as attorney-client privileged / work product as appropriate
