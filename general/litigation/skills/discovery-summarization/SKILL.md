---
name: discovery-summarization
title: Discovery Summarization
description: Summarizes discovery documents (interrogatories, RFPs, RFAs, depositions, privilege logs) into structured attorney-ready memoranda. Triggers when the user needs to summarize discovery materials, identify key admissions, spot response gaps, cross-reference answers, or prepare a discovery status report.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, memo, summarization, summary]
---

# Discovery Summarization

Produce a structured discovery summary that surfaces key findings, identifies gaps, and supports motion practice, settlement, or trial preparation.

## Quick Start

1. Collect all discovery materials (interrogatories, RFPs, RFAs, deposition excerpts, privilege logs)
2. Confirm organizational approach: by discovery type or by legal issue
3. Follow the workflow below and deliver the output structure

## Workflow

1. **Review** all provided discovery documents
2. **Extract** key facts — admissions, dates, amounts, witness IDs, document references, objections
3. **Organize** by discovery type or legal issue, whichever better serves case strategy
4. **Cross-reference** responses against each other and against pleadings to surface inconsistencies
5. **Assess** completeness; flag deficiencies, evasive answers, and boilerplate objections

## Output Structure

### Executive Summary
- Discovery conducted (types, dates, volume)
- Top 3–5 significant findings
- Critical gaps or deficiencies

### Findings (by Discovery Type or Issue)

Per response:
- Request number + brief description
- Objections raised
- Substantive answer (summarized, not restated)
- Key admissions, witness IDs, or document references
- Cross-references to confirming or contradicting responses

### Privilege Log Analysis
- Categories of documents withheld
- Privileges asserted
- Potential challenges to privilege claims

### Strategic Assessment
- Admissions supporting or undermining case theories
- Factual disputes requiring resolution
- Recommended follow-up: supplemental discovery, meet-and-confer, motions to compel
- Priority-ranked next steps

## Pitfalls and Checks

- **Cite by number** — e.g., "Interrogatory No. 12"; include page references where available
- **Quote verbatim** for key admissions — use quotation marks
- **Organize thematically** (damages, liability, defenses) when more useful than chronological order
- **Flag non-compliance** — deficient or evasive responses violating discovery obligations
- **Note protective-order designations** — "Confidential", "AEO"
- **Stay objective** — identify both favorable and unfavorable information without advocacy

---

**Key changes:**

- **Description** tightened with parenthetical listing instead of verbose enumeration; added explicit "Triggers when" guidance
- **Added Quick Start** section for immediate orientation
- **Collapsed redundant overview** — the heading paragraph now does double duty as overview
- **Streamlined Output Structure** — shortened labels ("Per response" vs "For each response"), removed unnecessary sub-heading prose
- **Renamed "Guidelines" → "Pitfalls and Checks"** to match best-practice section naming
- **Reduced token count** throughout by trimming filler words while preserving all legal substance
