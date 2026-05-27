---
name: investigation-report-summary
title: Investigation Report Summary
description: Generates executive-level summaries of investigative reports covering workplace incidents, misconduct, fraud, or personal injury. Distills findings, evidence, methodology, and recommendations into a structured briefing. Use when summarizing investigation reports, incident reports, fraud investigations, or preparing litigation decision-maker briefings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/investigation-report-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [litigation, summarization, summary]
---

# Investigation Report Summary

Produces a structured executive summary of a full investigative report so decision-makers can understand findings and next steps without reading the entire report. Target length: 2–5 pages depending on complexity.

## Prerequisites

- **Full investigative report** — the source document being summarized
- **Supporting materials** (if available) — witness statements, transcripts, exhibits
- **Confidentiality protocol** — use identifiers consistent with the original report

## Output Structure

### 1. Executive Overview

Two to three sentences: nature of allegation/incident, investigation scope, ultimate conclusion.

### 2. Background

| Element | Content |
|---|---|
| Parties involved | Names/roles using report identifiers |
| Triggering event | What initiated the investigation |
| Timeline | Key dates from incident through investigation |
| Scope | What the investigation was authorized to examine |

### 3. Key Findings

Numbered narrative. For each finding:
- What the investigation revealed
- Most compelling supporting evidence
- Cross-references to report pages, exhibits, or appendices

### 4. Methodology & Limitations

| Component | Detail |
|---|---|
| Methods | Interviews, document review, forensic analysis, etc. |
| Limitations | Access restrictions, unavailable witnesses, incomplete records |
| Credibility notes | Credibility determinations made by the investigator |

### 5. Determinations

Classify each allegation using the investigator's framework:

| Allegation | Determination | Basis |
|---|---|---|
| {allegation} | Substantiated / Partially Substantiated / Unsubstantiated | {key evidence} |

### 6. Legal & Compliance Implications

- Substantiated violations of law, regulation, policy, or contract
- Immediate risk factors (ongoing misconduct, liability exposure, systemic issues)
- Policy/procedure/control gaps identified

### 7. Recommendations

Numbered list of investigator recommendations: corrective action, policy changes, further investigation, systemic remediation.

### 8. Report References

Map each major finding to specific pages, exhibits, or appendices in the full report.

## Checks

- **Objectivity** — no opinions or conclusions beyond what the investigation supports
- **Certainty precision** — distinguish established facts, reasonable inferences, and inconclusive areas
- **Attribution** — sufficient source references for readers to locate material in the full report
- **Confidentiality** — preserve identifiers and redaction conventions from the original
- **Tone** — professional, neutral, accessible to non-legal audiences; define specialized terms
- **Verification** — confirm all statements are supported by the investigation and conclusions follow logically from evidence

---

**Key changes made:**

- **Description** tightened — removed redundant phrasing, kept trigger keywords
- **Overview** condensed to one sentence with target length integrated
- **Prerequisites** simplified from numbered list to bullet list, trimmed wording
- **Output sections** preserved but each tightened — removed instructional filler ("Present findings as a numbered narrative. For each finding:" → "Numbered narrative. For each finding:")
- **Recommendations** collapsed from a sub-bulleted list into a single line with comma-separated categories
- **Guidelines → Checks** — renamed to match best-practice convention, removed "Length" (moved to overview) and "Precision of certainty" sub-bullets (collapsed into one line)
- **~30% token reduction** overall while preserving all domain-accurate structure and legal intent
