# Visual Hierarchy — Reference

Loaded when the audit reaches Step 8 **and** the document is provided in a form that preserves layout — PDF, screenshots, Word document with applied styles, or a rendered web page. Skip this pillar entirely for plain-text inputs and redistribute its weight per the SKILL.md scoring rubric.

## What this pillar covers

How the document appears on the page or screen — independent of the words on it. A document with perfect prose, perfect structure, and perfect plain-language drafting can still defeat its reader through a wall-of-text layout.

## Checkpoints

### 1. Text density per page (or screen)

For PDFs, estimate:

- Words per page (excluding page numbers and headers / footers).
- Lines per page.
- Mean paragraph length in lines.

For web pages, estimate per screen viewport on a desktop default (1440 × 900) and on a mobile default (375 × 800), if both are available.

Rules of thumb (consumer documents):

- < 350 words per page → comfortable.
- 350–550 → standard.
- 550–750 → dense.
- 750+ → wall-of-text.

For B2B documents these thresholds shift up by ~150 words.

### 2. Font size

For consumer documents, the practical floor is 9–10 pt for body text on print and 14–16 px on the web. Documents using:

- 7–8 pt on print → Amber.
- < 7 pt on print → Red.
- < 12 px on the web → Amber.
- < 10 px on the web → Red.

Note that **fine print** (smaller font for less-important content) is a different question — what we are flagging is **material obligations** in fine print. If the document uses 7 pt only for a list of postal addresses, that is acceptable. If it uses 7 pt for the arbitration clause, that is Red.

### 3. Line spacing and paragraph spacing

- Line spacing 1.0 (single) with no paragraph spacing → cramped, score Amber to Red depending on density.
- Line spacing 1.15–1.5 with visible paragraph breaks → standard, score Green.
- Excessive spacing (line spacing 2.5+ for no reason) → not a legal-design problem but a sign of padding to inflate apparent length; note only if extreme.

### 4. Use of typographic emphasis

Bold, italics, underline, and ALL CAPS used to call attention should:

- Be reserved for genuinely emphatic content.
- Be used sparingly. A document with 40 instances of bold across 3,000 words has no working emphasis system.
- Follow a discipline (e.g., bold for defined terms only, italics for foreign terms only).

ALL CAPS deserves special attention in legal drafting:

- ALL CAPS clauses are common in US contracts (warranty disclaimers, limitation of liability) because of state-court doctrines requiring "conspicuous" presentation. Legitimate use.
- ALL CAPS that runs over a paragraph is **less** readable than mixed-case bold of the same content (a well-attested finding in typography research). Flag ALL CAPS clauses longer than two lines as Amber, and longer than five lines as Red.
- ALL CAPS used inconsistently (some emphatic clauses ALL CAPS, others not) signals undisciplined drafting; note as Yellow.

### 5. Use of bullets, numbered lists, and tables

These are powerful legal-design tools and their **absence** in a complex enumeration is a deficiency:

- A clause listing 12 permitted uses as a single paragraph separated by semicolons → Red.
- The same clause as a numbered list → Green.
- A pricing schedule as prose → Amber to Red.
- The same pricing schedule as a table → Green.

Flag prose enumerations of three or more items that would be clearer as a list. Flag conditions / consequences pairings that would be clearer in a two-column table.

### 6. Prominence of consent, signature, and acknowledgement elements

For consumer documents requiring action:

- Is the consent affirmative, with a clearly visible button or checkbox?
- Is the action separated from the rest of the page so the reader knows what they are agreeing to?
- Are pre-ticked boxes used? (See cookies / consent law — outside this pillar, but flag the typographic fact here.)
- Is the "Accept" treatment more prominent than the "Reject" treatment (size, colour, contrast, position)? If yes, note as Red — dark-pattern adjacent.

For documents requiring signature (contracts):

- Signature block clear and complete?
- Signature placement after material terms, not before?
- Counterpart provisions visible?

### 7. Tables, charts, and infographics

A well-placed table can replace pages of prose. A poorly-placed table can hide content. Assess:

- Tables that are split awkwardly across pages → Amber.
- Tables without visible headers → Amber.
- Tables where the data could be a single sentence → Yellow (the table adds nothing).
- Documents with substantive content rendered as graphics that cannot be selected or searched → Amber (accessibility failure).

### 8. Layered presentation (web or interactive PDF)

If the document is delivered as a web page or interactive PDF:

- Are sections collapsible? (Useful at large scale; problematic if a section that would mislead the reader is collapsed by default with no indication of content.)
- Is there a "key points" / "summary" panel?
- Are defined terms tooltipped or hyperlinked to definitions?

Layered presentation is a strong Green if well done.

## Pillar score

Combine the eight checkpoints:

| Checkpoint | Component |
| --- | --- |
| 1. Text density per page | … |
| 2. Font size | … |
| 3. Line / paragraph spacing | … |
| 4. Use of emphasis (and ALL CAPS) | … |
| 5. Use of bullets, lists, tables | … |
| 6. Prominence of consent / signature | … |
| 7. Tables and charts | … |
| 8. Layered presentation | … |

Each maps to a component:

- Green → 90.
- Yellow → 70.
- Amber → 45.
- Red → 20.
- Not applicable → exclude from average.

Pillar score = mean of applicable components, rounded.

## What to report in the pillar section

For each finding, include:

| # | Issue | Location (page / element) | Severity | Note |
| --- | --- | --- | --- | --- |
| 8.1 | Arbitration clause set in 7 pt font | p. 14 | Red | Material clause in fine print |
| 8.2 | "ACCEPT" button visually dominant over "REJECT" | consent page | Amber | Reject in low-contrast grey, accept in primary brand colour |
| 8.3 | Pricing schedule as prose with semicolons | clause 4.2 | Amber | Eight pricing tiers in a single 95-word sentence; would clarify as a table |
| 8.4 | 1.0 line spacing throughout, no paragraph breaks | document-wide | Amber | Contributes to wall-of-text appearance |

End with a synthesis: is the document visually accessible to its stated audience?

## When this pillar is skipped

If the user provided plain text only, do not attempt to infer layout. Report in Section 2 (Scope) of the assessment that this pillar was not assessed, and that the remaining five pillars carry redistributed weight.

If the user provided a PDF but the layout is uniform (e.g., a generated text-only PDF with no styling), assess what is available — density, font choice, headings — and skip the checkpoints that need richer visual information.
