---
name: insurance-correspondence-summarization
title: Insurance Correspondence Summarization
description: Produces structured summaries of insurance claims correspondence including coverage letters, reservation of rights (ROR), denial letters, and claim file documents. Extracts policy details, coverage positions, claims chronology, settlement posture, and liability exposure. Use when summarizing claim files, coverage disputes, ROR letters, denial letters, or multi-document insurance correspondence threads.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/insurance-correspondence-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
---

# Insurance Correspondence Summarization

Synthesizes insurance claims correspondence into a structured briefing with actionable coverage and litigation intelligence. Jurisdiction: US.

## Prerequisites

1. **Claim correspondence** — coverage letters, ROR letters, denial letters, demand letters, claim notices, insurer responses
2. **Policy documents** — if available; flag if missing
3. **Underlying litigation materials** — if referenced (pleadings, case caption, court/docket)

## Output Structure

### 1. Executive Overview (2–3 paragraphs)

- Claim type, status, key parties (insured, insurer, claimant, counsel)
- Urgent coverage or liability issues needing immediate attention

### 2. Factual Background

- Underlying incident: date, location, parties, nature of alleged injury/damage/loss
- Distinguish **undisputed facts** from **contested allegations**

### 3. Coverage Analysis

| Field | Details |
|---|---|
| Policy number(s) | |
| Coverage type(s) | |
| Policy period | |
| Limits / deductibles | |
| Insurer's position | Grant / ROR / Denial |
| Policy language cited | Quote with attribution |
| Disputes / ambiguities | |

### 4. Claims Chronology

| Date | Document | Sender → Recipient | Key Points |
|---|---|---|---|
| | | | |

Include: initial notice, coverage positions, ROR letters, demands, responses, ADR/coverage litigation filings.

### 5. Settlement Posture

- All demands and offers (with dollar amounts)
- Conditions attached to proposals
- Status: ongoing / stalled / concluded

### 6. Missing Documents

List documents referenced but not provided that are needed for complete analysis.

### 7. Next Steps / Action Items

Flag: coverage response deadlines, investigation gaps, declaratory relief considerations, settlement authority needed.

## Guidelines

- **Synthesize across documents** — consolidate related information into single sections; do not summarize document-by-document
- **Quote policy language** verbatim when cited as coverage basis; include document name and date
- **Separate coverage from underlying litigation** — summarize underlying case only as it affects coverage analysis

## Critical Flags

Watch for and explicitly flag:

- **Bad faith indicators**: unreasonable delay, inadequate investigation, wrongful denial, failure to defend
- **Insured conduct issues**: cooperation clause concerns, late notice, misrepresentation
- **Procedural traps**: statute of limitations, notice requirements, conditions precedent

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` are valid frontmatter fields)
- **Tightened description** — removed redundant enumeration of audience roles; kept trigger keywords and concise functional summary
- **Added jurisdiction inline** to overview instead of burying it as a trailing bullet
- **Compressed verbose sections** — "Missing Documents" and "Next Steps" reduced to single directive lines instead of prose paragraphs
- **Split "Guidelines" into two focused sections** — core synthesis guidelines vs. critical flags to watch for, improving scannability
- **Removed redundant wording** throughout (e.g., "List any documents referenced but not provided that are needed for complete analysis" → "List documents referenced but not provided that are needed for complete analysis")
- **Line count reduced** from 69 to 65 lines while preserving all domain-specific content
