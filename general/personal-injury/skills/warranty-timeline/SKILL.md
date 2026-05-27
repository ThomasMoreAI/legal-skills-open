---
name: warranty-timeline
title: Warranty Request Timeline
description: Generates a chronological timeline of warranty requests, claims, and complaints for product defect litigation, regulatory proceedings, or internal investigations. Analyzes complaint patterns, establishes manufacturer notice dates, and calculates defect statistics. Use when building warranty claim timelines, product defect chronologies, complaint pattern analysis, discovery summaries, expert report exhibits, or trial timeline exhibits.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/warranty-timeline
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: personal-injury
language: en
---

# Warranty Request Timeline

Builds a defensible chronological timeline of warranty requests and complaints for product defect litigation, regulatory proceedings, or internal investigations.

## Prerequisites

Collect before starting:
- **Product ID** — model number, SKU, or product name
- **Source documents** — warranty DBs, complaints, service records, RMA logs, internal emails, quality reports
- **Date range** — target period
- **Privacy constraints** — redaction/anonymization requirements per protective order

## Workflow

Copy and track progress:

```
- [ ] Step 1: Collect and extract data from source documents
- [ ] Step 2: Organize chronologically and analyze patterns
- [ ] Step 3: Calculate statistics
- [ ] Step 4: Assemble deliverables
- [ ] Step 5: Apply privacy redactions and verify source attribution
```

### Step 1: Data Collection

Search uploaded documents using broad terms:

| Primary | Secondary |
|---|---|
| warranty claim/request | return authorization, RMA |
| product defect, malfunction | service/repair request |
| customer complaint, product failure | engineering investigation, quality hold |
| [product name/model/SKU] | batch/lot number |

Extract per record:

| Field | Notes |
|---|---|
| Request date | Exact date; temporal proximity matters for notice |
| Customer ID | Redact per protective order |
| Product info | Model, serial, mfg date, batch/lot, purchase date |
| Defect description | Preserve verbatim customer language |
| Company response | Repair/replace/refund/deny + rationale |
| Resolution date | Calculate days-to-resolution |
| Handling personnel | Name + role (potential fact witnesses) |
| Source attribution | Document title, repository, custodian, creation date |

### Step 2: Chronological Organization & Pattern Analysis

Organize earliest to most recent. For high-volume products, group by week/month with drill-down.

Flag these patterns:

- [ ] **Earliest complaint** — establishes initial notice date (SOL, punitive damages, regulatory reporting)
- [ ] **Temporal clusters/spikes** — bad production batches or design-phase defects
- [ ] **Geographic concentrations** — distribution, storage, or environmental factors
- [ ] **Defect evolution** — progressive failure modes, emerging secondary defects
- [ ] **Internal acknowledgments** — engineering emails, quality holds, design change discussions
- [ ] **Response pattern shifts** — denial rate changes, escalation frequency, legalistic language
- [ ] **Inconsistencies** — gaps between internal knowledge and public statements (fraud/misrepresentation)

### Step 3: Statistics

Calculate:
- Total requests + unresolved count
- Requests per 1,000 units sold (if sales data available)
- Repair vs. replace vs. deny rates
- Average/median time to resolution
- Median time from purchase to first complaint (short = latent defect argument)

### Step 4: Deliverables

**A. Master Spreadsheet** — One row per claim with columns: Request Date (YYYY-MM-DD), Customer ID (redacted), Location, Product Model, Serial Number, Mfg/Batch Date, Defect Category (Electrical/Mechanical/Cosmetic/Safety/Performance), Severity (Minor/Moderate/Severe/Safety-Critical), Defect Description, Company Response, Resolution Date, Days to Resolution, Handling Personnel, Source Reference.

**B. Executive Summary** — At-a-glance metrics: total requests, date range, unresolved count, top defect categories with percentages, most affected regions, notable spikes, key statistics.

**C. Narrative Overview (2-5 paragraphs)** — Chronological progression: when defects first appeared, when patterns became statistically significant, when internal investigations began (or should have), when regulatory reporting triggered, when corrective action taken or not. Present facts neutrally — no legal conclusions.

**D. Supporting Materials** — Source document log with full attribution, methodology statement (search terms, repositories, date ranges, limitations), visualizations if data supports (complaint volume over time, geographic heat maps).

## Pitfalls and Checks

- **Preserve verbatim language** — customer descriptions carry evidentiary weight as contemporaneous non-expert statements
- **Disclose all gaps** — missing periods from retention policies, system migrations, or business unit changes must be noted, not papered over
- **Do not interpret ambiguous complaints** — present as-written; let counsel characterize
- **Maintain factual objectivity** — separate factual data from analytical observations to preserve work product protection
- **Dual format output** — manipulable (Excel) + fixed (PDF) for discovery production
- **Privacy compliance** — redact PII per protective orders and applicable consumer protection statutes
- **Authentication readiness** — source attribution must support independent verification by opposing counsel or court
- **Flag regulatory triggers** — note when complaint volume/severity may trigger reporting under CPSA or state consumer protection statutes
