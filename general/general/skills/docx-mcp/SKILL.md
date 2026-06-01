---
name: docx-mcp
title: Editing Word Documents with docx-mcp
description: 'Use when editing existing Word (.docx) documents with track changes, comments, footnotes, or structural validation. Triggers: reviewing contracts, marking up reports, adding revision comments, validating document structure, removing watermarks, auditing OOXML integrity, bulk text replacement with revisions, footnote management, paragraph-level edits. Requires the docx-mcp MCP server to be running.'
author: SecurityRonin
author_url: https://github.com/SecurityRonin/docx-mcp/tree/main/skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Editing Word Documents with docx-mcp

## Overview

The `docx-mcp` MCP server provides tools for reading and editing .docx files with proper OOXML markup. Edits appear as real revisions in Microsoft Word — red strikethrough for deletions, green underline for insertions, comments in the sidebar.

A .docx file is a ZIP archive of XML files. This server unpacks the archive, parses all XML parts with lxml, edits the cached DOM trees directly, and repacks modified XML back into a valid .docx archive. This gives full control over OOXML markup — essential for track changes, comments, and structural validation that higher-level libraries don't expose.

## When to Use

- Editing existing .docx files with tracked changes
- Adding comments or footnotes to documents
- Reviewing/auditing document structure
- Removing watermarks
- Bulk find-and-replace with revision marks
- Any task where changes must be visible as Word revisions

**Do NOT use for:** Creating new .docx from scratch (use docx-js instead), PDFs, spreadsheets, or `.doc` (legacy binary format — convert to .docx first).

## Workflow

```
1. open_document("/path/to/file.docx")
2. get_headings() or get_document_info()     → understand structure
3. search_text("clause text")                → find target paragraphs
4. get_paragraph(para_id)                    → verify exact text before editing
5. delete_text(para_id, "old text")          → tracked deletion
6. insert_text(para_id, "new text")          → tracked insertion
7. add_comment(para_id, "Reason for change") → explain the edit
8. audit_document()                          → verify integrity
9. save_document("/path/to/output.docx")     → save (or omit path to overwrite)
```

**Always `audit_document()` before saving** to catch structural issues (orphaned footnotes, duplicate paraIds, unpaired bookmarks, missing relationship targets).

## Tool Quick Reference

### Document Lifecycle

| Tool | Purpose | Key args |
|------|---------|----------|
| `open_document` | Open .docx for editing | `path` |
| `close_document` | Close and clean up | — |
| `get_document_info` | Stats overview | — |
| `save_document` | Save to .docx | `output_path` (optional) |

### Reading

| Tool | Purpose | Key args |
|------|---------|----------|
| `get_headings` | Heading tree with paraIds | — |
| `search_text` | Find text in body/footnotes/comments | `query`, `regex` |
| `get_paragraph` | Full text of one paragraph | `para_id` |

### Track Changes

| Tool | Purpose | Key args |
|------|---------|----------|
| `insert_text` | Tracked insertion (green underline) | `para_id`, `text`, `position` |
| `delete_text` | Tracked deletion (red strikethrough) | `para_id`, `text` |
| `accept_changes` | Accept tracked changes | `author` (optional) |
| `reject_changes` | Reject tracked changes | `author` (optional) |
| `set_formatting` | Bold/italic/underline/color with tracked markup | `para_id`, `text`, `bold`, `italic`, `underline`, `color` |

### Tables

| Tool | Purpose | Key args |
|------|---------|----------|
| `get_tables` | List all tables with cell content | — |
| `add_table` | Insert table after paragraph | `para_id`, `rows`, `cols` |
| `modify_cell` | Modify cell text with tracked changes | `table_index`, `row`, `col`, `text` |
| `add_table_row` | Add row to table | `table_index`, `cells` (optional), `row_idx` (optional) |
| `delete_table_row` | Delete row with tracked changes | `table_index`, `row_index` |

**Table column sizing:** Column widths are in DXA (1440 DXA = 1 inch). Page content widths:
- A4 (11,906 DXA wide, 1" margins): **9,026 DXA** content width
- US Letter (12,240 DXA wide, 1" margins): **9,360 DXA** content width

**Header vs data cell widths must match exactly.** Even a 1 DXA difference between a header cell and its data cell causes persistent misalignment. Define column widths as constants and reuse them in every row.

**Usable cell width** = column width − 240 DXA (default margins: 120 DXA each side).

**Font character width reference** (avg DXA/char across a–z, A–Z, 0–9, measured from font files):

Formula: `DXA/char = (advance / upm) × pt × 20`. Word `size:` = pt × 2.  
Fitting: `chars × dxa_per_char ≤ column_width − 240` (240 = default cell margins, 120 each side).

*Monospaced — all variants identical width:*

| Font | 10pt | 11pt | 12pt | Notes |
|------|------|------|------|-------|
| PragmataPro (all variants) | 100 | 110 | 120 | Densest; exceptional Unicode coverage |
| Cascadia Code NF | 117 | 129 | 141 | VS Code / Windows Terminal default |
| Hack NF (all variants) | 120 | 132 | 144 | |
| Courier New (7pt / 6pt) | ~84 / ~72 | — | — | Legacy |

*Calibri (Office 2007–2023 body default):*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Light Italic | 99 | 109 | 119 |
| Light | 100 | 110 | 120 |
| Regular / Italic | 101 | 111 | 121 |
| Bold / Bold Italic | 103 | 114 | 124 |

*Aptos (Office 365/2024 default — replaced Calibri mid-2023):*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Light | 106 | 116 | 127 |
| Regular / Italic | 108 | 119 | 130 |
| Narrow Regular / Italic | 100 | 110 | 120 |
| Narrow Bold / Bold Italic | 102–103 | 112–113 | 122–123 |
| SemiBold | 111 | 122 | 133 |
| Bold / Bold Italic | 113 | 124 | 136 |

*Cambria (Office heading default):*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Italic | 105 | 116 | 126 |
| Regular | 109 | 120 | 131 |
| Bold Italic | 112 | 123 | 135 |
| Bold | 116 | 128 | 139 |

*Arial:*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Narrow Regular / Italic | 95 | 104 | 114 |
| Narrow Bold / Bold Italic | 99 | 109 | 119 |
| Regular / Italic | 116 | 127 | 139 |
| Bold / Bold Italic | 121 | 133 | 145 |
| Black | 137 | 151 | 165 |

*Times New Roman:*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Italic | 106 | 117 | 128 |
| Regular / Bold Italic | 111 | 122 | 133 |
| Bold | 116 | 128 | 140 |

*Verdana (widest — screen-optimised):*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Regular / Italic | 125 | 138 | 150 |
| Bold / Bold Italic | 141 | 155 | 169 |

*Georgia:*

| Variant | 10pt | 11pt | 12pt |
|---------|------|------|------|
| Regular | 117 | 128 | 140 |
| Italic | 118 | 129 | 141 |
| Bold | 134 | 147 | 160 |
| Bold Italic | 135 | 149 | 162 |

*Equity B (Matthew Butterick):*

| Variant | 10pt | 11pt | 12pt | Notes |
|---------|------|------|------|-------|
| Italic | 106 | 117 | 128 | |
| Regular | 110 | 121 | 132 | |
| Bold Italic | 113 | 124 | 135 | |
| Bold | 116 | 127 | 139 | |
| Caps Regular | 131 | 144 | 157 | lowercase = small caps |
| Caps Bold | 137 | 151 | 165 | lowercase = small caps |

*CJK — full-width Han/Hangul = exactly 1 em = pt × 20 DXA:*

| Font | Script | Full-width (10/11/12pt) | Half-width ASCII |
|------|--------|------------------------|-----------------|
| SimSun (宋体) | SC | 200 / 220 / 240 | 100 / 110 / 120 |
| Microsoft YaHei (微软雅黑) | SC | 200 / 220 / 240 | 117 / 129 / 141 |
| PMingLiU (新細明體) | TC | 200 / 220 / 240 | 100 / 110 / 120 |
| MS JhengHei (微軟正黑體) | TC | 200 / 220 / 240 | 116 / 128 / 139 |
| MS PGothic | JP | 185 / 204 / 222 | 100 / 110 / 120 |
| Yu Gothic | JP | 200 / 220 / 240 | 111 / 122 / 133 |
| Malgun Gothic (맑은 고딕) | KR | 200 / 220 / 240 | 110 / 121 / 132 |
| Batang (바탕) | KR | 200 / 220 / 240 | 119 / 131 / 143 |

*Other scripts:*

| Font | Script | 10pt | 11pt | 12pt |
|------|--------|------|------|------|
| Mangal | Devanagari (Hindi) | 172 | 190 | 207 |
| Cordia New | Thai | 68 | 74 | 81 |

### Lists

| Tool | Purpose | Key args |
|------|---------|----------|
| `add_list` | Apply bullet/numbered list formatting | `para_ids`, `style` |

### Comments

| Tool | Purpose | Key args |
|------|---------|----------|
| `get_comments` | List all comments | — |
| `add_comment` | Comment anchored to paragraph | `para_id`, `text` |
| `reply_to_comment` | Threaded reply | `parent_id`, `text` |

### Footnotes & Endnotes

| Tool | Purpose | Key args |
|------|---------|----------|
| `get_footnotes` | List all footnotes | — |
| `add_footnote` | Footnote with superscript ref | `para_id`, `text`, `url` (optional hotlink) |
| `add_footnote_ref` | Subsequent ref to existing footnote | `para_id`, `footnote_id` |
| `validate_footnotes` | Cross-ref footnote IDs | — |
| `get_endnotes` | List all endnotes | — |
| `add_endnote` | Endnote with superscript ref | `para_id`, `text` |
| `validate_endnotes` | Cross-ref endnote IDs | — |

### Headers, Footers & Styles

| Tool | Purpose | Key args |
|------|---------|----------|
| `get_headers_footers` | List all headers/footers with text | — |
| `edit_header_footer` | Edit header/footer text with tracked changes | `location`, `old_text`, `new_text` |
| `get_styles` | List all defined styles | — |

### Properties & Images

| Tool | Purpose | Key args |
|------|---------|----------|
| `get_properties` | Get core properties (title, creator, dates) | — |
| `set_properties` | Set core properties | `title`, `creator`, `subject`, `description` |
| `get_images` | List embedded images with dimensions | — |
| `insert_image` | Insert image after paragraph | `para_id`, `image_path` |

### Sections & Cross-References

| Tool | Purpose | Key args |
|------|---------|----------|
| `add_page_break` | Insert page break after paragraph | `para_id` |
| `add_section_break` | Add section break | `para_id`, `break_type` |
| `set_section_properties` | Set page size/orientation/margins | `width`, `height`, `orientation`, `para_id` (optional) |
| `add_cross_reference` | Internal hyperlink between paragraphs | `source_para_id`, `target_para_id`, `text` |

### Protection & Merge

| Tool | Purpose | Key args |
|------|---------|----------|
| `set_document_protection` | Set edit protection with optional password | `edit_type`, `password` (optional) |
| `merge_documents` | Merge content from another DOCX | `source_path` |

### Validation & Audit

| Tool | Purpose | Key args |
|------|---------|----------|
| `validate_paraids` | Check paraId uniqueness | — |
| `remove_watermark` | Remove DRAFT watermarks | — |
| `audit_document` | Full structural audit | — |

## Essential Patterns

### Replace Text (delete + insert on same paragraph)

```
1. search_text("30 days")              → find the paragraph
2. get_paragraph(para_id)              → verify exact text
3. delete_text(para_id, "30 days")     → tracked deletion
4. insert_text(para_id, "60 days")     → tracked insertion
```

Word shows both marks side by side: ~~30 days~~ **60 days**.

### Batch Edits Across Multiple Paragraphs

```
1. search_text("Net 30", regex=False)  → returns all matches with paraIds
2. For each match:
   a. get_paragraph(para_id)           → verify context
   b. delete_text(para_id, "Net 30")
   c. insert_text(para_id, "Net 60")
   d. add_comment(para_id, "Updated payment terms per Amendment 3")
3. audit_document()                    → verify no structural damage
```

### Add Explanatory Footnote

```
1. search_text("force majeure")        → find the clause
2. add_footnote(para_id, "Force majeure includes acts of God, war, pandemic, and other events beyond reasonable control.")
3. validate_footnotes()                → verify cross-references
```

### Full Document Review

```
1. open_document("/path/to/contract.docx")
2. get_document_info()                 → paragraph count, headings, footnotes
3. get_headings()                      → see structure at a glance
4. audit_document()                    → check for pre-existing issues
5. ... make edits ...
6. audit_document()                    → verify edits didn't break anything
7. save_document("/path/to/contract_reviewed.docx")
```

## Tips

- **paraId** is an 8-char hex string (e.g., `"1A2B3C4D"`). Get them from `get_headings()` or `search_text()`.
- **position** in `insert_text`: `"start"`, `"end"`, or a substring to insert after.
- **author** defaults to `"Claude"` for all tracked changes and comments.
- **Save to new file** to preserve the original: `save_document("/path/to/revised.docx")`.
- **Always verify before editing**: Use `get_paragraph()` to see the exact text before calling `delete_text()`. The text must match exactly within a single run.

## OOXML Pitfalls (Critical Knowledge)

These hard-won lessons prevent silent document corruption. Word may "repair" broken documents by silently rewriting your edits.

### Word for Mac: File-Refuses-to-Open Causes

These four issues all produce "Word experienced an error trying to open the file" with no further detail. Each one causes a hard open failure on Word for Mac (Windows Word is more forgiving).

#### 1. Field code elements in one `<w:r>` (fldChar + instrText)

Every `w:fldChar` and `w:instrText` element must live in its **own separate `<w:r>`**. Packing begin/instrText/end into a single run is schema-invalid.

```python
# WRONG — all three in one run (causes hard open failure)
r._r.append(fld_begin)
r._r.append(instr)
r._r.append(fld_end)

# CORRECT — one element per run
def _fld_run(para, fld_type=None, instr_text=None):
    r = para.add_run()
    if fld_type:
        fc = OxmlElement('w:fldChar')
        fc.set(qn('w:fldCharType'), fld_type)
        r._r.append(fc)
    if instr_text:
        it = OxmlElement('w:instrText')
        it.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        it.text = instr_text
        r._r.append(it)
    return r

_fld_run(para, fld_type='begin')
_fld_run(para, instr_text=' PAGE ')
_fld_run(para, fld_type='end')
```

Add `xml:space="preserve"` to every `w:instrText` so Word parses the instruction correctly.

#### 2. `w:titlePg` without a matching "first" header/footer

`w:titlePg` in `sectPr` tells Word to use a separate first-page header/footer. Word then **requires** a `<w:headerReference w:type="first">` entry. Declaring the flag without the part causes a load failure on Word for Mac.

**Fix:** either provide the "first" header/footer part, or don't set `titlePg` at all. In python-docx, never set `section.different_first_page_header_footer = True` unless you also populate `section.first_page_header`.

#### 3. PNG image relationships before header/footer relationships (Word for Mac bug)

Word for Mac has an undocumented constraint: if a PNG image relationship appears **before** header/footer relationships in `word/_rels/document.xml.rels`, the file refuses to open. JPEG images before header/footer are fine; only PNG triggers this.

Relationship ordering in the rels file follows the order parts are registered in python-docx. **Fix:** call `add_headers_footers()` (or any function that accesses `section.header`/`section.footer`) before any `add_picture()` calls in the generator. This ensures header/footer get lower rIds than all PNG images.

```python
def main():
    doc = setup_document()
    add_headers_footers(doc)   # ← must come BEFORE any add_picture() calls
    build_cover(doc)           # ← adds first image here
    build_section1(doc)
    # ...
```

#### 4. `w:abstractNum` elements after `w:num` elements in numbering.xml

`CT_Numbering` is a strict OOXML sequence: **all `w:abstractNum` elements must precede all `w:num` elements**. If your generator merges custom numbering into a template that already has `w:num` entries, a naive `.append()` puts the new `w:abstractNum` after existing `w:num` entries — schema violation, hard open failure.

**Fix:** insert new `abstractNum` elements before the first existing `w:num`, then append new `num` elements at the end.

```python
first_num = root.find(f'{{{W}}}num')
for child in abstract_nums:
    if first_num is not None:
        first_num.addprevious(child)   # insert before first w:num
    else:
        root.append(child)
for child in nums:
    root.append(child)                 # append after all w:num
```

#### 5. `wp:extent` cx/cy values in the billions (corrupted EMU dimensions)

Word for Mac refuses to open a file when any `<wp:extent>` element has `cx` or `cy` in the billions or trillions of EMUs. Normal document images range from 1–10 million EMUs (roughly 1–11 inches at 914,400 EMU/inch).

Two distinct causes, same symptom:

**Cause A — PIL BytesIO without DPI metadata:**
`PIL.Image.save(buf, format='JPEG', quality=92)` writes no DPI metadata to the BytesIO. python-docx's image parser defaults to DPI ≈ 0, computing an astronomical "natural" width. Even when `width=Inches(5.8)` is specified, the derived `cy` (height) is calculated from the corrupted natural dimensions.

```python
# WRONG — no DPI in BytesIO → python-docx gets DPI≈0 → cx/cy in trillions
img.save(buf, format='JPEG', quality=92)

# CORRECT — embed DPI so python-docx computes sane natural dimensions
img.save(buf, format='JPEG', quality=92, dpi=(96, 96))
```

**Cause B — double EMU conversion:**
A helper that calls `Inches(width)` internally receives a pre-converted EMU value instead of a float. Tell-tale signature: `4,849,538,688,000 = 5,303,520 × 914,400` — the display width (`Inches(5.8)`) multiplied by `Inches()` a second time.

```python
TEXT_WIDTH = Inches(5.8)          # = 5,303,520 EMU

# WRONG — add_image() calls Inches(width) internally, caller passes EMU
add_image(doc, path, width=TEXT_WIDTH)   # → Inches(5303520) = 4,849,538,688,000

# CORRECT — pass float inches so the internal Inches() call is the only conversion
add_image(doc, path, width=5.8)
```

**Detection script:**
```python
import zipfile
from lxml import etree

with zipfile.ZipFile("file.docx") as z:
    tree = etree.fromstring(z.read("word/document.xml"))
WPD = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
for i, ext in enumerate(tree.iter(f'{{{WPD}}}extent')):
    cx = int(ext.get('cx', 0))
    if cx > 100_000_000:  # > ~109 inches
        print(f"Drawing {i}: cx={cx:,}  *** OVERSIZED — will fail on Word for Mac")
```

### ParaId Rules

Every `<w:p>` and `<w:tr>` element has a `w14:paraId` attribute.

| Rule | Detail |
|------|--------|
| Must be unique | Across ALL XML parts: document.xml, footnotes.xml, headers, footers, endnotes |
| Must be < 0x80000000 | Word reserves the high bit internally — values >= 0x80000000 cause validation failure |
| 8 hex digits | Always uppercase, zero-padded (e.g., `1A2B3C4D`) |
| Duplicates from copy-paste | Duplicating content creates duplicate paraIds — fix the second occurrence |

The `validate_paraids()` tool checks all of these. Run it after any structural edits.

### Footnote Rules

| Rule | Detail |
|------|--------|
| 1:1 mapping | Each footnote ID must be referenced **exactly once** in document.xml. Multiple references to the same ID corrupt footnotes 1 and 2 |
| IDs must be sequential | No gaps — Word may silently renumber on recovery |
| Reserved IDs | id="-1" (separator) and id="0" (continuation) are reserved — real footnotes start at id="1" |
| Each paragraph needs paraId | Every `<w:p>` inside a footnote needs its own unique paraId |

The `validate_footnotes()` tool checks reference/definition matching. Always run after adding footnotes.

**Required styles:** The document template must contain `FootnoteReference` (character style, superscript) and `FootnoteText` (paragraph style). Missing styles cause silent rendering failures. Check with `get_styles()` before adding footnotes to an unfamiliar template.

**Citing the same source multiple times:** You cannot reference the same footnote ID from two places. Call `add_footnote()` once per citation point — N citations of the same source = N separate `add_footnote()` calls, each with its own ID. Never reuse a footnote ID across paragraphs.

**Multi-source citations at a single point:** When multiple sources support one statement, make successive `add_footnote()` calls at the same paragraph. They render as comma-delimited superscripts (e.g., ¹,²,³) — `add_footnote()` automatically inserts a superscript comma run when the last run of the target paragraph is already a footnote reference.

**Word Recovery Warning:** When Word recovers/repairs a file, it renumbers ALL footnotes sequentially by document position, not by original ID. After any Word recovery, re-examine footnotes before further edits.

### Non-Breaking Spaces

Word uses non-breaking spaces (`\xa0`, U+00A0) and narrow no-break spaces (`\u202f`, U+202F) throughout. **Direct string matching fails silently.** The `search_text()` tool handles this internally, but if you're checking text returned by `get_paragraph()`, be aware that what looks like a space may be `\xa0`.

### Text Inside Hyperlinks

Text inside `w:hyperlink` elements may not appear in `paragraph.text` from some parsers. The docx-mcp tools handle this correctly, but be aware when working with documents containing many hyperlinks — the visible text in Word may differ from what a naive text extraction shows.

### Tracked Changes: Key Rules

| Rule | Detail |
|------|--------|
| Use `w:delText` inside `w:del` | Never `w:t` — causes validation errors |
| Preserve `w:rPr` formatting | Copy the original run's formatting into tracked change runs |
| Minimal edits only | Mark only what changes — don't wrap entire paragraphs |
| Deleting entire paragraphs | Must also mark the paragraph mark as deleted via `<w:del/>` inside `<w:pPr><w:rPr>`, otherwise accepting changes leaves empty paragraphs |

### Smart Quotes

When adding text, use smart quotes for professional typography:

| Entity | Character |
|--------|-----------|
| `\u2018` | ' (left single) |
| `\u2019` | ' (right single / apostrophe) |
| `\u201C` | " (left double) |
| `\u201D` | " (right double) |
| `\u2013` | -- (en dash) |

The docx-mcp tools accept Unicode text directly — pass the actual characters, not XML entities.

### Element Order in `<w:pPr>`

The OOXML schema requires a specific element order: `<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`, `<w:rPr>` last. Out-of-order elements cause validation warnings and may trigger Word recovery.

### Element Order in `<w:rPr>`

Child elements inside `w:rPr` also have a required order. Wrong order = "unreadable content" in Word:

```
w:rStyle → w:rFonts → w:b/w:bCs → w:i/w:iCs → w:color → w:sz/w:szCs → w:u → w:vertAlign
```

Common mistake: placing `w:u` before `w:sz`, or `w:color` after `w:sz`.

### Heading Numbering

**NEVER embed literal section numbers in heading text** (e.g., "1.1 Background"). Heading numbers must come from Word's multilevel list numbering system. If you need to insert a heading via `insert_text()`, insert only the heading text — the numbering comes from the document's styles.

## Markdown-to-DOCX Conversion Pitfalls

When converting markdown content to DOCX edits via docx-mcp, watch for:

### Soft-Wrapped Lines

A long line in markdown may display across multiple lines in an editor. If you're extracting text from markdown to feed into `insert_text()` or `delete_text()`, ensure you're working with the logical line, not the display line. A `[bracketed construct]` that wraps across source lines must be treated as one unit.

### Fake Footnotes in Markdown

Markdown doesn't have real footnotes — `[^1]` syntax is a convention that some parsers support. When converting markdown with footnote-style references to DOCX:

1. Use `add_footnote()` to create real OOXML footnotes — don't insert `[1]` as plain text
2. Map each markdown `[^N]` reference to an `add_footnote()` call on the appropriate paragraph
3. Remove the footnote definition text from the body (it now lives in footnotes.xml)

### Superscript Numbers Concatenate

When extracting text from paragraphs that contain footnote references, the superscript reference numbers are invisible in the XML text but adjacent characters concatenate. Example: "File #8" followed by superscript footnote "73" extracts as "File #873". Account for this when using `search_text()` with regex patterns on footnoted text.

### Template List Indents May Override Your Content

A document template's numbering definition often specifies its own indents. When inserting list content via `add_list()`, verify the rendered indent matches expectations — the template's `w:abstractNum` definition takes precedence. If indents look wrong, the fix requires editing the numbering XML directly (outside docx-mcp's current tool set) or applying explicit paragraph indent overrides.

### Clickable Superscript Cross-References

Every footnote reference superscript created by `add_footnote()` is automatically wrapped in a `<w:hyperlink w:anchor="_FnN">` pointing to a `<w:bookmarkStart w:name="_FnN">` in the footnote definition. This means:

- Clicking the superscript navigates to the footnote in Word **and** in PDF exports.
- The back-arrow in Word's footnote pane navigates back to the reference in the body.

**Subsequent reference to the same footnote** — use `add_footnote_ref(para_id, footnote_id)` to add another superscript that links to the same footnote without duplicating the definition:

```
fn_id = add_footnote("00000004", "SWGDE Best Practices")["footnote_id"]
add_footnote_ref("00000009", fn_id)   # second citation → same footnote
```

Do NOT call `add_footnote()` twice with the same content — that creates two separate definitions. `add_footnote_ref` retroactively adds the anchor bookmark if the footnote predates this feature.

### Hotlinked URLs in Footnotes

Pass `url="https://..."` to `add_footnote()` to render the URL as a clickable hyperlink inside the footnote body:

```
add_footnote(para_id, "SWGDE Best Practices for Mobile Device Evidence Collection", url="https://www.swgde.org/documents")
```

- Label text is added as a plain run; the URL is appended as a `<w:hyperlink>` with `Hyperlink` character style and a relationship registered in `word/_rels/footnotes.xml.rels`.
- Multiple footnotes with different URLs each get a distinct `rId`.
- Omitting `url` produces plain-text footnotes (backward-compatible).

## Audit Checklist

Before delivering any edited document, run through this checklist:

```
1. audit_document()         → comprehensive structural check
2. validate_footnotes()     → if any footnotes were added/modified
3. validate_paraids()       → if any structural changes were made
4. save_document("new.docx") → save to new file (preserve original)
```

The `audit_document()` tool checks all of the following in one call:
- XML well-formedness of all parts
- Footnote cross-references (references vs definitions, duplicates, gaps)
- ParaId uniqueness and range validity (< 0x80000000)
- Heading level continuity (no skips like H2 -> H4)
- Bookmark pairing (start/end matching)
- Relationship targets (all referenced files exist)
- Image references (all embedded images exist in word/media/)
- Content type registration (all media extensions have entries)
- Residual artifacts (DRAFT, TODO, FIXME, PLACEHOLDER, TBD markers)
