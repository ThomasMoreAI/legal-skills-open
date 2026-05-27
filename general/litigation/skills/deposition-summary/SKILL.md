---
name: deposition-summary
title: Deposition Summary with Key Document Index
description: Generates topic-based deposition summaries for commercial litigation with exhibit cross-referencing. Produces a two-column table (page:line | neutral summary) with embedded exhibit citations. Use when summarizing depositions, creating deposition digests, indexing exhibits, or preparing witness testimony summaries during discovery.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Deposition Summary with Key Document Index

Transforms a deposition transcript into a topic-based summary table with integrated exhibit cross-references for rapid navigation between testimony and documentary evidence.

## Prerequisites

- Complete deposition transcript with page and line numbering
- Exhibit list and files referenced or marked during deposition
- Case context: party names, key contract sections, claims at issue

## Workflow

### 1. Review Transcript

Read the full transcript and identify:
- Natural topic breaks (explicit subject changes and thematic shifts)
- Every exhibit reference — formal ("Exhibit 3") and informal ("the email we just reviewed")
- Key admissions, contradictions, evasive answers, and authentication testimony

### 2. Extract Topics

For each topic, capture:

| Element | Requirement |
|---|---|
| Topic heading | Specific — "Witness Knowledge of Payment Default Under §4.2" not "Payment Issues" |
| Page:line range | Start and end of testimony on that topic |
| Summary | 2-3 sentences, neutral, no legal conclusions |
| Exhibits referenced | Exhibit number + how witness characterized/authenticated it |
| Notable moments | Admissions, contradictions, refusals to answer |

### 3. Build Exhibit Index

Create a master exhibit cross-reference table:

| Exhibit | Description | Transcript Refs (pg:ln) | Witness Characterization |
|---|---|---|---|
| Ex. 1 | [doc type] | 45:3-47:12, 102:8-103:1 | [how witness described it] |

### 4. Assemble Summary Table

Primary deliverable — two-column table:

```
| Transcript Cite | Topic & Summary |
|-----------------|-----------------|
| pp. 12:4-18:22  | **Formation of the Supply Agreement**
|                 | [2-3 sentence neutral summary]. See Ex. 3
|                 | (Supply Agreement, discussed at 14:8-15:2).
|                 | Notable: Witness admitted not reading §4.2
|                 | before signing (15:18-22). |
```

Within each summary cell:
- Embed exhibit references discussed during that testimony
- Cite specific page:line for key admissions
- Use hierarchical headings for major topics vs. subtopics

### 5. Output

Produce both:
- **DOCX** — formatted table with hyperlinks to exhibits and transcript locations
- **PDF** — preserved hyperlinks, full-text searchable, locked for filing

## Key Rules

- **Neutral tone only** — summarize what the witness said, not what it means for the case
- **Specificity over brevity** — "Witness denied receiving the October 14 demand letter" not "Witness denied receiving correspondence"
- **Organize by substance, not questioner** — consolidate redirect and direct testimony on the same topic under one heading
- **Capture authentication testimony** — note when witness identifies, authenticates, or disputes a document
- **Flag evasive responses** — mark non-responsive answers, memory claims, and qualified answers

## Quality Checklist

- [ ] Every exhibit mentioned in testimony appears in summary and exhibit index
- [ ] No exhibits referenced that weren't actually discussed
- [ ] All page:line citations verified against transcript
- [ ] Summaries reflect actual testimony — no interpretation or legal conclusions
- [ ] Topic headings specific enough for at-a-glance navigation
- [ ] No privileged communications or work product included
- [ ] Hyperlinks resolve to correct targets
