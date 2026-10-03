# Docx Output Template

Use this when producing a Word document deliverable. Logical content matches `output-template-markdown.md`; this file specifies the docx-specific rendering decisions. Generate by locating and using the document-generation capability available in the current runtime, preferring a `docx` or `documents` skill/tool when present. If no such capability is available, treat Word generation as blocked rather than silently downgrading.

## Reference table of contents

- [Document setup](#document-setup)
- [Privilege and distribution](#privilege-and-distribution)
- [Front matter](#front-matter)
- [Table of contents](#table-of-contents)
- [Section headings](#section-headings)
- [Encounter formatting](#encounter-formatting)
- [Tables](#tables)
- [Causation language callouts](#causation-language-callouts)
- [Inline UNVERIFIED flags](#inline-unverified-flags)
- [Page numbers and footer](#page-numbers-and-footer)
- [Final QC before delivery](#final-qc-before-delivery)

## Document setup

- **Page size:** US Letter, 1 inch margins
- **Body font:** Calibri 11pt or Times New Roman 11pt depending on firm preference. If the user attached a firm template, use the template's styling.
- **Heading style:** Built-in Word styles (Heading 1 for sections, Heading 2 for subsections, Heading 3 for individual encounter dates). Do not hand-format headings; built-in styles let the attorney regenerate the table of contents.
- **Tables:** Use Word tables, not tab-aligned text. The Provider Index, Diagnostic Studies, and Medication History are all tables.

## Privilege and distribution

Before applying attorney-work-product markings, confirm the intended audience and distribution when context suggests non-attorney use or external sharing. Use the work-product label for litigation-team work product; adjust or remove it if the user says the chronology is non-privileged, client-facing, or intended for external disclosure.

## Front matter

Page 1, top of document, before the table of contents:

```
MEDICAL RECORD CHRONOLOGY

Re: [Patient name]
DOB: [Date]
Date of incident: [Date]
Case type: [Type]
Records reviewed: [Bates range]
Citation scheme: Bates-stamped pages
Prepared: [Date]

CONFIDENTIAL - ATTORNEY WORK PRODUCT
```

The "ATTORNEY WORK PRODUCT" footer is required for litigation-team work product. It signals work product protection if the document is inadvertently disclosed, but it must be adjusted or removed when the intended audience or distribution makes that label inaccurate.

## Table of contents

Insert a Word automatic table of contents (TOC field) after the front matter. The TOC should be set to depth 2 (sections and subsections, not individual encounters).

## Section headings

Use these exact section headings in this order:

1. Case Information
2. Provider Index
3. Pre-Incident Medical History
4. Chronological Summary
5. Diagnostic Studies
6. Medication History
7. Damages Summary
8. Strategic Analysis
9. Methodology and Limitations

## Encounter formatting

In a docx, each encounter gets a Heading 3 line with the date and provider, followed by a labeled paragraph for each subsection. Example:

```
[Heading 3] 2024-03-14 - Dr. Sarah Chen - Portland Orthopedic Associates - Initial Consult

Chief complaint: Right knee pain following motor vehicle collision on 2024-03-08. [SMITH00145]

History: Patient reports she was rear-ended at a stoplight on 2024-03-08. Right knee struck the dashboard on impact. Pain has progressively worsened over the past six days. No prior right knee injuries reported. [SMITH00145-00146]

Examination: Right knee positive McMurray, mild effusion, range of motion 0-110 degrees (left knee 0-135). Tenderness over medial joint line. Neurovascularly intact. [SMITH00146]

Diagnostic studies: X-ray right knee three views: no acute fracture, mild patellofemoral degenerative changes. [SMITH00148]

Diagnoses:
S83.241A - Other tear of medial meniscus, current injury, right knee, initial encounter [SMITH00147]
M17.11 - Unilateral primary osteoarthritis, right knee [SMITH00147]

Treatment:
99204 - New patient evaluation, comprehensive [SMITH00147]
Naproxen 500mg BID prescribed [SMITH00147]
Referred for MRI right knee [SMITH00147]
Referred to physical therapy [SMITH00147]

Restrictions: No squatting, kneeling, or running. Light duty at work, no lifting over 20 pounds. [SMITH00147]

Follow-up: Two weeks pending MRI results. [SMITH00147]

Causation language: "Patient's right knee meniscal injury is causally related to the motor vehicle collision of 2024-03-08 based on mechanism of injury, temporal relationship, and absence of prior knee complaints." [SMITH00147]
```

## Tables

Use the runtime document-generation capability's table support. Set table styles consistently:

- Header row: bold, light gray fill
- Body rows: alternating shading optional
- Borders: simple single-line borders all around
- Column widths: auto-fit to content unless a column is content-heavy (e.g., "Findings" or "Significance" columns should be wider)

## Causation language callouts

When a provider makes a causation statement, render the quoted text in a slightly distinct way to draw the eye. Recommended: italic plus indent. Do not use bold quoted text (visually noisy in long documents) or color (will not survive printing).

## Inline UNVERIFIED flags

Render `[UNVERIFIED - claim appears in records but specific page not retrievable]` in italic, immediately after the affected sentence. Do not use a footnote. The attorney needs to see the flag in line; footnotes get skipped during fast review.

## Page numbers and footer

- Footer: page X of Y, plus "Confidential - Attorney Work Product"
- Header: optional, can include patient name and case caption if firm style requires

## Final QC before delivery

Before saving the docx:

1. Run the verification pass from `bates-citation-verification`.
2. Verify the table of contents reflects all sections.
3. Verify Bates citations are consistent in format throughout.
4. Verify no orphaned `[UNVERIFIED]` flags reference removed text.
5. Spot check three random encounters to confirm Bates citations point to the right source.
6. Verify Methodology and Limitations includes actual verification counts and the verification log pointer from `output-template-markdown.md`.

If any check fails, fix and rerun. A docx going to an attorney is a deliverable, not a draft.
