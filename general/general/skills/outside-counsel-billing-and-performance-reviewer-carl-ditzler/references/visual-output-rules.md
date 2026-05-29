# Visual Output Rules

Use these rules whenever generating a PDF, Word document, PowerPoint-ready deck, or any other visually formatted report artifact.

## General Layout Rules
- Do not let text overlap across table columns, labels, or cards.
- Wrap text in all body cells, table cells, labels, and callouts.
- Keep numeric columns narrow and right-aligned.
- Keep prose columns flexible and top-aligned.
- If a table would exceed the page width, reduce the number of visible columns or switch to a card layout.
- Do not place long paragraphs in narrow columns such as `Amount`, `Confidence`, or label fields.
- Use short display labels in visual tags. Keep raw taxonomy slugs for machine-readable outputs only.

## Table Rules
- Prefer no more than 5 visible columns for portrait PDF or Word layouts when prose is involved.
- Use summary tables only for short phrases, values, and short labels.
- Move long descriptions, assessments, or rationale into:
  - issue cards;
  - notes beneath the table; or
  - appendix tables in landscape orientation.
- Vertically top-align all table cells.
- Allow row height to expand with wrapped text.

## Label and Tag Rules
- Do not use a visible pill or tag if the text will not fit comfortably.
- Use title-case display labels such as `Block Billing` or `Vague Narrative` instead of long slug strings.
- If a label still exceeds the available width, widen the label area or render the category as plain text instead of a pill. When adjusting a label for this need, make same adjustments to other labels so there is consistency. 

## PDF and HTML Rules
- Prefer card layouts or fixed-layout tables with explicit wrapping.
- Apply these CSS rules or their equivalent:
  - `table-layout: fixed`
  - `white-space: normal`
  - `overflow-wrap: anywhere`
  - `word-break: break-word`
  - `vertical-align: top`
- Use consistent page margins and generous cell padding.
- If a section contains issue narratives, use stacked issue cards rather than a very wide table.

## Word Document Rules
- Use simple, professional tables with preferred widths and wrapping enabled.
- Avoid decorative pills that can break awkwardly in Word export.
- Use clear section headings, summary tables, and issue cards or subheadings for long rationale text.
- Keep issue labels short and readable.

## PowerPoint Rules
- Do not use dense spreadsheet-like tables on slides.
- Use summary slides for metrics and issue-highlight slides for narrative content.
- Limit each slide to a small number of wrapped bullets or cards.
- Keep labels short and readable at presentation size.

## Fallback Rule
If a visual artifact still risks overflow or awkward wrapping, simplify the layout. Clean readability is more important than preserving a dense table.
