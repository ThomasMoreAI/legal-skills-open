---
name: word-contract-formatting
title: Darwin Legal Word Contract Formatting
description: Apply Darwin Legal formatting conventions when drafting or generating any contract, agreement, amendment, or legal document as a Word (.docx) file. Use this skill whenever Ryan asks to draft, generate, or format any agreement — including RSPAs, consulting agreements, amendments, board consents, side letters, or any other legal document — even if the request doesn't explicitly mention formatting. Also use when asked to reformat or clean up an existing contract. Always read this skill before producing any .docx legal document.
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/word-contract-formatting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Darwin Legal Word Contract Formatting

## Overview

This skill governs how all Darwin Legal contracts and legal documents are formatted in Word. Apply these rules to every document generated as a .docx, regardless of agreement type.

Also read the docx SKILL.md at `/mnt/skills/public/docx/SKILL.md` for general Word document mechanics. This skill governs Darwin Legal-specific content and style choices.

The base template lives at: `assets/Darwin_Legal_Base_Template.dotx`

---

## Document Generation Workflow

**Always start from the template.** Do not create a blank document. The template contains the Darwin Legal Numbering style, Normal style with correct font/spacing, and all numbering definitions.

```bash
# Step 1: Copy template as working docx
cp assets/Darwin_Legal_Base_Template.dotx /tmp/output.docx

# Step 2: Unpack
python scripts/office/unpack.py /tmp/output.docx /tmp/unpacked/

# Step 3: Edit word/document.xml — replace body content, preserve structure
# Step 4: Pack
python scripts/office/pack.py /tmp/unpacked/ /tmp/output.docx --original /tmp/output.docx

# Step 5: ALWAYS run post-processing fix (see below) before saving to workspace
```

Clear the existing body content in `document.xml` (the template contains test paragraphs) and replace with the contract content. Preserve the `<w:body>` wrapper and `<w:sectPr>` (section properties) at the end.

### CRITICAL: Post-Processing Fix (Required After Every pack.py Run)

The `.dotx` base template causes two bugs that make Word refuse to open the output file. Both must be patched after pack.py runs, every time, without exception.

**Bug 1 — Wrong content type.** The template registers `word/document.xml` as `wordprocessingml.template.main+xml` in `[Content_Types].xml`. A `.docx` must use `wordprocessingml.document.main+xml`. pack.py preserves the template type and Word rejects the file.

**Bug 2 — Missing `standalone="yes"`.** pack.py strips the `standalone="yes"` attribute from the XML declaration in `word/document.xml`. Some versions of Word reject files missing this attribute.

A reusable fix function lives at `/sessions/funny-ecstatic-ride/mnt/.claude/fix_docx.py`. Call it immediately after pack.py, before saving anywhere:

```python
import sys
sys.path.insert(0, '/sessions/funny-ecstatic-ride/mnt/.claude')
from fix_docx import fix_docx
fix_docx('/tmp/output.docx', '/sessions/funny-ecstatic-ride/mnt/Drafts and Comments/FINAL_NAME.docx')
```

Do not save the raw pack.py output to the workspace — always run fix_docx first.

### CRITICAL: Preserve `<w:document>` Opening Tag Verbatim

Never reconstruct the `<w:document>` opening tag from scratch. The tag declares many optional namespace prefixes (`cx1`–`cx8`, `w16sdtdh`, `w16sdtfl`, `w16du`, `wp14`, etc.) that must match the `mc:Ignorable` attribute exactly. If any declared prefix is missing or mismatched, Word rejects the file.

Always extract the header from the template itself:

```python
import zipfile, re

with zipfile.ZipFile('/tmp/output.docx') as z:
    orig = z.read('word/document.xml').decode()
m = re.match(r'(.*?<w:body>)', orig, re.DOTALL)
header = m.group(1)  # use this verbatim as the opening of document.xml
```

Then build the new document.xml as `header + body_content + sectPr + '</w:body></w:document>'`.

### `w:pPr` Element Ordering

OOXML schema requires this order inside `<w:pPr>` for numbered paragraphs:

```xml
<w:pPr>
  <w:pStyle w:val="ListParagraph"/>
  <w:numPr>
    <w:ilvl w:val="0"/>
    <w:numId w:val="3"/>
  </w:numPr>
  <w:spacing w:after="360" w:line="240" w:lineRule="auto"/>
  <w:contextualSpacing w:val="0"/>
  <w:jc w:val="both"/>
</w:pPr>
```

Order must be: `pStyle → numPr → spacing → contextualSpacing → jc`. Any other order causes a schema validation error and may prevent the file from opening.

---

## Font and Page Setup

These are already baked into the template's Normal style. Do not override them in paragraph-level XML unless correcting a specific paragraph.

- Font: Times New Roman, 12pt
- Margins: 1 inch all sides
- Spacing after: 360 twips (18pt) — `<w:spacing w:after="360" w:line="240" w:lineRule="auto"/>`
- Justification: full — `<w:jc w:val="both"/>`
- Page numbers: plain Arabic numerals, centered footer, no decoration

---

## Document Title and Date

- Title: centered, all caps — use a plain Normal paragraph with `<w:jc w:val="center"/>` and a bold run
- Effective date appears in the first sentence of the body, not in the signature block
- Opening pattern: `This [Agreement Name] (this "Agreement") is made as of [Date] by and between...`

---

## Numbering — Darwin Legal Numbering Style

The template defines a four-level multilevel list style. Reference it by setting `numId="3"` and the appropriate `ilvl` in each paragraph's `<w:pPr>`.

### Level Reference Table

| Level | Format | ilvl | Example |
|-------|--------|------|---------|
| First | `1.` `2.` `3.` | 0 | `1.   Services.` |
| Second | `a.` `b.` `c.` | 1 | `a.   Scope.` |
| Third | `i.` `ii.` `iii.` | 2 | `i.   Deliverables.` |
| Fourth | `A.` `B.` `C.` | 3 | `A.   Engineering.` |

### Paragraph XML Pattern

```xml
<w:p>
  <w:pPr>
    <w:numPr>
      <w:ilvl w:val="0"/>
      <w:numId w:val="3"/>
    </w:numPr>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:r>
    <w:t xml:space="preserve">Services.  The Consultant agrees to perform...</w:t>
  </w:r>
</w:p>
```

For level 1, set `<w:ilvl w:val="1"/>`. For level 2, `<w:ilvl w:val="2"/>`. For level 3, `<w:ilvl w:val="3"/>`. The numId stays `3` at all levels.

### Section Heading Style

The heading text runs inline with the body paragraph — there is no separate heading line. The section label (e.g., `Services.`) is plain text followed by two spaces and then the body text, all in the same paragraph.

Do not apply bold, underline, or italics to heading text.

---

## Cross-References (Bookmarks + REF Fields)

Use Word bookmarks and REF fields for all cross-references so they auto-update on F9 after structural edits in Word.

### Bookmark Naming Convention

Generate bookmark names from the section identifier, lowercased, with underscores:

| Section | Bookmark Name |
|---------|--------------|
| Section 1 | `sec_1` |
| Section 2(a) | `sec_2_a` |
| Section 2(a)(i) | `sec_2_a_i` |
| Section 3(b)(ii)(A) | `sec_3_b_ii_A` |

### Step 1: Place Bookmark on Target Paragraph

Add bookmark start/end wrapping the section label text in the target paragraph:

```xml
<w:p>
  <w:pPr>
    <w:numPr>
      <w:ilvl w:val="0"/>
      <w:numId w:val="3"/>
    </w:numPr>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:bookmarkStart w:id="1" w:name="sec_2_a"/>
  <w:r>
    <w:t xml:space="preserve">Scope.  The services to be performed...</w:t>
  </w:r>
  <w:bookmarkEnd w:id="1"/>
</w:p>
```

Bookmark IDs must be unique integers across the document. Start at 1 and increment.

### Step 2: Insert REF Field at Cross-Reference Site

Replace plain cross-reference text (e.g., "Section 2(a)") with a REF field:

```xml
<w:r>
  <w:t xml:space="preserve">as set forth in </w:t>
</w:r>
<w:r>
  <w:fldChar w:fldCharType="begin"/>
</w:r>
<w:r>
  <w:instrText xml:space="preserve"> REF sec_2_a \n \h </w:instrText>
</w:r>
<w:r>
  <w:fldChar w:fldCharType="separate"/>
</w:r>
<w:r>
  <w:t>Section 2(a)</w:t>
</w:r>
<w:r>
  <w:fldChar w:fldCharType="end"/>
</w:r>
```

The text inside the `separate`/`end` block is the display value before Word recalculates. Set it to the correct current section reference — Word will update it on F9 or document open.

The `\n` flag tells Word to display the paragraph number (the section label). The `\h` flag makes it a hyperlink.

### Field Update Note

Fields render correctly on first open in Word, which triggers automatic field recalculation. If a field shows the old number, Ctrl+A → F9 forces a full update.

---

## Defined Terms

- Quotes only on first definition — no bold, underline, or italics
- Example: `...the shares purchased hereunder (the "Shares")...`
- Subsequent uses: capitalize, no quotes

### Definitions Section

- Include a standalone "Definitions" section only for documents approximately 5,000 words or longer
- In shorter documents, define terms inline on first use
- If used, Definitions is typically Section 1; terms listed alphabetically as `(a)`, `(b)`, `(c)` sub-items

---

## Lists

- Never use bullets
- List-like content uses the next numbering tier: `(i)`, `(ii)`, `(iii)` or `(A)`, `(B)`, `(C)`
- List item punctuation: semicolons on all items except second-to-last ("; and" or "; or") and last (period)

---

## All-Caps Provisions

Use all caps (no additional formatting) for:
- Limitation of liability clauses
- Disclaimer of warranties
- Indemnification caps
- Section 83(b) notices
- Securities legend text
- Any provision where all-caps treatment is standard for enforceability or notice

---

## Recitals

Case-by-case. Appropriate for commercial agreements; typically omitted from equity documents.

If used:
- Centered plain-text "RECITALS" heading
- WHEREAS clauses are unnumbered paragraphs beginning with "WHEREAS,"
- Close with a "NOW, THEREFORE" paragraph

---

## Signature Block

```
[PARTY NAME IN ALL CAPS]

[Entity name, if signing on behalf of entity]

By:  _______________________________

Name:

Title:
```

- No date line (effective date is in the body)
- Plain text throughout — no bold, no small caps
- Spouse consent block header (if applicable): "CONSENT OF SPOUSE (IF APPLICABLE)"
- Use "[Signature Page Follows]" centered at bottom of last substantive page when appropriate

---

## Exhibits and Schedules

- New page, labeled "EXHIBIT A" / "SCHEDULE A" — centered, all caps, plain text
- Title of exhibit centered below label, all caps
- Same formatting rules as body — same font, spacing, numbering scheme
- Do not restart page numbering

---

## Amendment and Restatement Titling

- `First Amendment to [Agreement Name]`
- `Second Amendment to [Agreement Name]`
- `Amended and Restated [Agreement Name]`
- `First Amendment to Amended and Restated [Agreement Name]`

---

## What Never Appears in Darwin Legal Documents

| Element | Status |
|---------|--------|
| Bold headings | Never |
| Underlined headings | Never |
| Italic headings | Never |
| Bold defined terms | Never |
| Bullet points | Never |
| Table of contents | Never |
| Headers/footers (except page numbers) | Never |
| Date in signature block | Never |
| Small caps in signature blocks | Never |
| Dashes around page numbers (`-2-`) | Never |
| Manual section numbers (when Darwin Legal Numbering applies) | Never |
