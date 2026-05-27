---
name: deposition-summary-exhibit-index
title: Deposition Summary with Exhibit Index
description: Produces a topic-based U.S. deposition summary with page/line citations and a keyed exhibit index linking testimony to documents. Use when creating deposition digests, exhibit-linked summaries, key document indexes, or discovery testimony maps in commercial litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-summary-exhibit-index
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, summarization, summary]
---

# Deposition Summary with Exhibit Index

Topic-based deposition summary with integrated exhibit index, precise page/line citations, and neutral testimony characterizations.

## Quick Start

Gather before starting:
- Full deposition transcript with page/line numbering
- Exhibit list with IDs/labels (filenames or Bates ranges)
- Witness name, role, date, parties, and caption block
- Any protective order or confidentiality designations

## Workflow

### 1. Cover Block

Include: caption (case name, court, case no.), witness name/role, deposition date, counsel for deponent, reporting service, preparer, and preparation date.

### 2. Topic Summary Table

| Page/Line Range | Topic Summary |
|---|---|
| p. 12:3–18:22 | **Topic: Formation of Master Services Agreement**. Neutral 2–3 sentence summary with key admissions/denials. Cite critical statements by page/line. Reference exhibits inline: "Ex. 12 (Invoice 1043)". |
| p. 19:1–24:6 | **Topic: Scope of Services and Deliverables**. Note uncertainty or evasive answers. Link discussed exhibits. |

Rules:
- 2–3 neutral sentences per topic; no legal conclusions
- Cite page/line for critical admissions or contradictions
- Use specific, descriptive topic titles
- Split rows when testimony shifts subtopic
- Exhibit format: `Ex. 12 (Invoice 1043)` or `PX-12 (Invoice 1043)`

### 3. Exhibit Index

| Exhibit | Description | Testimony Page/Line | Witness Characterization |
|---|---|---|---|
| Ex. 12 | Invoice 1043 dated 3/5/2023 | p. 45:2–46:20 | Identified as company invoice; reflects services rendered |

Rules:
- Include every transcript-mentioned exhibit with all page/line references
- One-sentence authentication/characterization summary
- Map informal exhibit references to correct IDs

### 4. Key Admissions / Contradictions (Optional)

Include only if requested. Use exact citations:
- **Admission**: "No written approval existed for change order." (p. 78:4–10)
- **Contradiction**: "Claimed no notice of default; later admitted receipt of 6/2/2023 email." (p. 102:11–16; p. 148:3–9)

### 5. Output

Deliver as DOCX and PDF with hyperlinks to exhibits and transcript anchors. If linking is infeasible, include file paths or document IDs in brackets.

## Pitfalls and Checks

- Never guess page/line ranges—use exact transcript references only
- Never add exhibits not discussed in the transcript
- No advocacy or legal conclusions in summaries
- Flag privilege or confidentiality issues; do not reproduce protected content
- Note gaps explicitly if transcript is incomplete or exhibits are missing
- Confirm compliance with any protective order or redaction protocol
- Mark uncertain citations or exhibit IDs with `[VERIFY]`

---

It looks like I don't have write permission to the file. Could you allow the write, or would you like me to try again?
