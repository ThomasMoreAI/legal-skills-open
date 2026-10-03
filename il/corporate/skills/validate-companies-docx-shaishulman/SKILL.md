---
name: validate-companies-docx-shaishulman
title: 'Validate companies DOCX'
description: 'ALWAYS use this skill instead of validate-companies when a .docx file is involved. Validates Israeli company references in Word (.docx) files and annotates with correct registration details from the Israeli Companies Registrar (רשם החברות הישראלי). Triggers on: any request referencing a .docx file with company validation, annotation, or completion — e.g. ''check companies in this contract'', ''annotate the Word file with company numbers'', ''fill in company details in the document'', ''validate companies in the agreement'', ''complete the company details in the docx''. Also triggers when user provides a .docx path and asks to complete, verify, or fix company information. For Hebrew documents, assume Israeli company unless stated otherwise.'
author: ShaiShulman
author_url: https://github.com/ShaiShulman/isracorp-mcp/tree/main/.claude/skills/validate-companies-docx
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: il
practice: corporate
language: en
---

# validate-companies-docx

Validates Israeli company references in a Word `.docx` file and annotates the document. Missing details are inserted as tracked changes; discrepancies or not-found companies receive comment balloons.

## Required

- `isracorp` MCP server (provides `search_company` and `get_company` tools)
- Python with the scripts in `scripts/` (unpacking, packing, comments)
- `pandoc` (for text extraction)

## Scripts Location

All scripts are at `.claude/skills/validate-companies-docx/scripts/`. When running commands, use paths relative to the skill's scripts directory, or provide full paths.

## Full Workflow

### Step 1: Confirm the Document Path

If not provided, ask the user:

```
Please provide the full path to the .docx file you want to annotate.
```

Verify the file exists before proceeding.

### Step 2: Extract Text for Analysis

```bash
pandoc --track-changes=all "<input.docx>" -o "/tmp/doc_text.md"
```

Read `/tmp/doc_text.md` to identify company mentions. This gives clean text that's easier to search than raw XML.

### Step 3: Unpack the Document

```bash
python scripts/office/unpack.py "<input.docx>" unpacked/
```

The default `--merge-runs` collapses adjacent same-format runs, which helps locate company names that Word has split across `<w:r>` elements.

### Step 4: Extract Company Mentions

Apply the same extraction logic as the `validate-companies` skill:

1. **Hebrew names**: `[\u0590-\u05FF\s"'״]+ ?(בע"מ|בעמ|בע״מ)`
2. **English names**: `[A-Z][A-Za-z\s]+ (Ltd|Limited|Inc|LP)\.?`
3. **Numbers already present**: `ח\.?[פצ]\.?\s*(\d{2}-\d{6}-\d|\d{9})` or `No\.\s*(\d{2}-\d{6}-\d|\d{9})`
4. **Placeholders**: `ח\.?[פצ]\.?\s*_{2,}` or `No\.\s*_{2,}`

For each mention, note the surrounding sentence for context when locating it in the XML.

### Step 5: Validate Each Mention via MCP

Same logic as `validate-companies` skill (Steps 2–3):

- Number present → `get_company({ number })`
- Name only → `search_company({ name })`; if no results and name contains parentheses, strip the parenthetical and retry (e.g. `גד משקאות (2000)` → retry as `גד משקאות`)
- Record: confirmed match / discrepancy / not found / warnings

### Step 6: Locate Each Mention in the XML

Read `unpacked/word/document.xml`.

For each mention to annotate:

1. Concatenate all `<w:t>` text within each `<w:p>` paragraph (ignoring tags) to reconstruct visible text
2. Find the paragraph(s) whose concatenated text contains the company mention
3. Within that paragraph, identify which `<w:r>` run(s) end with the company name

**RTL detection**: Check if the paragraph's `<w:pPr>` contains `<w:bidi/>`. If so, it's a Hebrew RTL paragraph and RTL insertion rules apply.

### Step 7: Annotate the XML

Use sequential comment IDs starting from 0 (or the next available ID if comments already exist).

---

#### Case A: Missing detail — company confirmed in registry

Insert the missing detail (company number and/or city) immediately after the company name as a tracked change.

**Choosing the number label:**

- **If the paragraph already contains a label** (`ח.פ.`, `ח.צ.`, or `Company Number`) immediately before the blank (`___`), preserve that exact label — do not change it.
- **If there is no existing label**, determine the correct one:
  - Hebrew document: use `ח.צ.` if the company number starts with `52` or the company name contains `ציבורית`; otherwise use `ח.פ.`
  - English document: use `Company Number`

```xml
<!-- Example: inserting ", ח.פ. 51-234567-9" after "טכנוגל בע"מ" in a Hebrew paragraph (private company) -->
<w:ins w:id="[next-id]" w:author="Claude" w:date="[ISO-8601-date]">
  <w:r>
    <w:rPr>
      <!-- CRITICAL: Copy <w:rPr> from the preceding Hebrew run exactly.
           This preserves: <w:cs/>, <w:rFonts w:cs="...">, <w:lang w:bidi="he-IL"/> -->
      [copied rPr here]
    </w:rPr>
    <w:t xml:space="preserve">, ח.פ. 51-234567-9</w:t>
  </w:r>
</w:ins>
```

**RTL rules** (when inserting into a Hebrew paragraph — `<w:bidi/>` present):

- Copy `<w:rPr>` from the immediately preceding `<w:r>` run in the same paragraph
- The copied `<w:rPr>` will already contain `<w:cs/>` and the bidi font — do NOT omit these
- Add `xml:space="preserve"` to `<w:t>` when the inserted text begins with a space
- If the preceding run has no `<w:rPr>`, add one with `<w:cs/>` and `<w:lang w:bidi="he-IL"/>`

**LTR rules** (English paragraphs — no `<w:bidi/>`):

- Copy `<w:rPr>` from preceding run (preserves font, size)
- No special bidi properties needed

---

#### Case B: Company not found in registry

Add a comment balloon on the company name span:

If the document is in Hebrew:

```bash
python scripts/comment.py unpacked/ [id] "החברה לא נמצאה ברשם החברה. אנא וודאו את השם או מספר החברה שלה."
```

If the document is in any other language:

```bash
python scripts/comment.py unpacked/ [id] "Company &quot;[name]&quot; was not found in the Israeli Companies Registrar. Please verify the name before signing."
```

Then add markers in `document.xml` around the company name text:

```xml
<w:commentRangeStart w:id="[id]"/>
[... existing runs with company name ...]
<w:commentRangeEnd w:id="[id]"/>
<w:r>
  <w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>
  <w:commentReference w:id="[id]"/>
</w:r>
```

**CRITICAL**: `<w:commentRangeStart>` and `<w:commentRangeEnd>` are direct children of `<w:p>`, never inside `<w:r>`.

---

#### Case C: Document details differ from registry

Add a comment balloon.

If the document is in Hebrew:

```bash
python scripts/comment.py unpacked/ [id] "פרטי החברה ברשם: &quot;[registryName]&quot;, ח.פ. [number]. הפרטים במסמך שונים &mdash; אנא וודאו לפני החתימה."
```

If the document is in any other language:

```bash
python scripts/comment.py unpacked/ [id] "Registry shows: &quot;[registryName]&quot;, Company Number [number]. Document has different details &mdash; please reconcile before signing."
```

Add markers as in Case B.

---

#### Case D: Dissolved or violating company

Add a comment warning regardless of whether other details were inserted.

If the document is in Hebrew:

```bash
python scripts/comment.py unpacked/ [id] "אזהרה: [name] (ח.פ. [number]) &mdash; סטטוס: &quot;[status]&quot;. אנא בדקו את מעמד החברה לפני החתימה."
```

If the document is in any other language:

```bash
python scripts/comment.py unpacked/ [id] "WARNING: [name] (Company Number [number]) has status &quot;[status]&quot;. Verify current standing before signing."
```

---

### Step 8: Pack the Document

```bash
python scripts/office/pack.py unpacked/ "<output_validated.docx>" --original "<input.docx>"
```

The output filename should be `<original-name>_validated.docx` in the same directory.

### Step 9: Report to User

For a **Hebrew document**, report in Hebrew:

```
עובד על: <input_filename>
פלט:     <output_filename>

תוצאות:
✓ אומת (שינוי עם מעקב הוכנס): [שם עברי] / [שם אנגלי] — ח.פ. [מספר]
⚠ אזהרה (תגובה הוספה): [שם עברי] / [שם אנגלי] — [סיבת האזהרה]
✗ לא נמצא ברשם (תגובה הוספה): [שם חברה]
✗ אי-התאמה (תגובה הוספה): [שם עברי] / [שם אנגלי] — [מה שונה]
```

For any **other language document**, report in English:

```
Processed: <input_filename>
Output:    <output_filename>

Results:
✓ Validated (tracked change inserted): [Hebrew name] / [English name] — No. [number]
⚠ Warning (comment added): [Hebrew name] / [English name] — [warning reason]
✗ Not found (comment added): [company name as mentioned]
✗ Discrepancy (comment added): [Hebrew name] / [English name] — [what differs]
```

Always show both Hebrew and English names when the registry has both. Omit the ` / [English name]` part if the English name is absent.

## Important Docx XML Rules

### Comment ID Management

Before adding new comments, check if `unpacked/word/comments.xml` already exists. If it does, find the highest existing `w:id` value and start new comment IDs from that value + 1.

### Tracked Change IDs

Every `<w:ins>` and `<w:del>` element needs a unique `w:id`. Use sequential integers not used elsewhere in the document. Scan `document.xml` for all existing `w:id` attributes on `<w:ins>` and `<w:del>` before assigning new ones.

### XML Escaping in Hebrew Text

When inserting Hebrew text in `<w:t>` elements:

- Apostrophes/double quotes in company names like `בע"מ`: use `&quot;` for `"` and `&#x2019;` for `'`
- The `unpack.py` script converts smart quotes to XML entities — new insertions should do the same

### Do Not Use `\n` in XML

Separate text runs use separate `<w:r>` elements. Never use `\n` or newlines inside `<w:t>`.

## Example: Complete Hebrew Annotation

**Input paragraph in document.xml (simplified):**

```xml
<w:p>
  <w:pPr>
    <w:bidi/>
    <w:jc w:val="right"/>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:rFonts w:cs="David"/>
      <w:cs/>
      <w:lang w:bidi="he-IL"/>
    </w:rPr>
    <w:t xml:space="preserve">ההסכם נחתם בין </w:t>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:cs="David"/>
      <w:cs/>
      <w:lang w:bidi="he-IL"/>
    </w:rPr>
    <w:t>טכנוגל בע"מ</w:t>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:cs="David"/>
      <w:cs/>
      <w:lang w:bidi="he-IL"/>
    </w:rPr>
    <w:t xml:space="preserve"> לבין צד ב.</w:t>
  </w:r>
</w:p>
```

**After annotation (inserting company number as tracked change):**

```xml
<w:p>
  <w:pPr>
    <w:bidi/>
    <w:jc w:val="right"/>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:rFonts w:cs="David"/>
      <w:cs/>
      <w:lang w:bidi="he-IL"/>
    </w:rPr>
    <w:t xml:space="preserve">ההסכם נחתם בין </w:t>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:cs="David"/>
      <w:cs/>
      <w:lang w:bidi="he-IL"/>
    </w:rPr>
    <w:t>טכנוגל בע"מ</w:t>
  </w:r>
  <w:ins w:id="1" w:author="Claude" w:date="2026-04-08T00:00:00Z">
    <w:r>
      <w:rPr>
        <w:rFonts w:cs="David"/>
        <w:cs/>
        <w:lang w:bidi="he-IL"/>
      </w:rPr>
      <w:t xml:space="preserve">, ח.פ. 51-234567-9</w:t>
    </w:r>
  </w:ins>
  <w:r>
    <w:rPr>
      <w:rFonts w:cs="David"/>
      <w:cs/>
      <w:lang w:bidi="he-IL"/>
    </w:rPr>
    <w:t xml:space="preserve"> לבין צד ב.</w:t>
  </w:r>
</w:p>
```
