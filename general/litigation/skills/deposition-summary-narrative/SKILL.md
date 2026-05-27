---
name: deposition-summary-narrative
title: Deposition Summary — Narrative
description: Transforms deposition transcripts into topic-organized narrative memoranda with page-line citations, flagged admissions, contradictions, and credibility issues. Use when summarizing depositions, condensing transcripts for trial prep, or building case strategy during discovery or pre-trial phases.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-summary-narrative
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [summarization, summary]
---

# Deposition Summary — Narrative

Synthesizes a deposition transcript into a strategic narrative memorandum with embedded citations, flagged admissions, and credibility analysis.

## Prerequisites

1. **Deposition transcript** — full text with page and line numbers
2. **Case caption and docket number**
3. **Witness role** — plaintiff, defendant, fact witness, expert, or 30(b)(6) representative
4. **Attendee list** — attorneys and represented parties (preferred)

## Quick Start

1. Collect transcript and case identifiers
2. Identify witness role and key topics from transcript
3. Generate output sections in order: Header → Executive Overview → Narrative Body → Exhibit Log → Privilege & Objection Notes
4. Embed `(page:line–line)` citations after every material assertion
5. Flag admissions, contradictions, and memory gaps throughout

## Output Sections

### 1. Header Block

- Case caption (style of cause, court, docket number)
- Deponent name and litigation role
- Date, location, attorneys present with affiliations
- Privilege notice: "Prepared at the direction of counsel. Attorney Work Product — Privileged and Confidential."

### 2. Executive Overview (1–2 paragraphs)

Cover key topics, most significant admissions, credibility concerns, and impact on case theory.

### 3. Narrative Body

Organize by **topic, not Q&A order**. Typical sections: Background & Qualifications, Events Leading to Incident, The Incident, Damages & Injuries, Medical Treatment, Employment & Financial Impact. Adjust to fit case type.

Per section:
- Write flowing prose — never reproduce Q&A format
- Cite immediately after each assertion: `(78:3–15)`
- Flag admissions: *"Significantly, the witness acknowledged..."*
- Flag contradictions: *"This conflicts with the affidavit stating..."*
- Flag memory gaps: *"Witness claimed no recollection of X despite prior specificity about Y (167:12–168:3)."*
- Note demeanor shifts or evasiveness inline

### 4. Exhibit Log

| Exhibit No. | Description | Witness Response |
|---|---|---|
| Ex. 1 | Document type / date | Authenticated / Denied / No recognition / Contradicted |

### 5. Privilege & Objection Notes

- Instructions not to answer (question, objecting counsel, basis)
- Privilege assertions (attorney-client, work product, FRE 408)
- Material objections on form, foundation, or scope

## Pitfalls and Checks

- **Always cite**: never paraphrase a critical admission without `(page:line–line)`
- **Length target**: ~25–33% of transcript length; completeness over brevity
- **Accuracy**: do not characterize beyond what the transcript supports; summary must be defensible to opposing counsel
- **Work product header**: repeat on every page with case name and deponent
- **Follow-up queries**: cite both summary location and underlying transcript page/line
- **Jurisdiction**: follows US federal and state civil litigation conventions
