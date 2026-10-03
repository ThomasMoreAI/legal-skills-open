# docx-js Generation Patterns — California CRC 2.100-2.119

Working recipes for producing CRC-compliant `.docx` files using
the `docx` npm package (https://docx.js.org/) for conversion to
PDF and upload to a California eCourt filing portal.

## Why .docx, not direct PDF?

California courts accept (and for represented parties in most
courts, require) PDF for eFiling. The clean workflow is:

1. Generate the `.docx` from a template using `docx-js`
2. Save it locally so the litigant can review/edit in Word
3. Print or "Save As PDF" to produce the upload file
4. Upload the PDF to the eFiling portal (Odyssey eFileCA or
   File & ServeXpress) with the correct document code

Producing `.docx` gives the litigant a review surface —
essential for pro se filers who need to read and verify before
filing.

## California-specific formatting challenges

California CRC formatting has three elements that require
careful handling in docx-js:

1. **2.5-inch top margin on page 1** — requires a section break
   between page 1 and subsequent pages in `docx-js`
2. **Line numbering — MANDATORY under CRC 2.108(b)** —
   consecutively numbered lines on the left margin of every
   page. Applied via the section's `lineNumbers` property
   (see "Line numbering (CRC 2.108(b))" below for the recipe)
3. **CRC 2.110 footer on every page** including page 1

## Document setup

```javascript
import {
  Document, Packer, Paragraph, PageOrientation,
  SectionType, SectionProperties, Footer, AlignmentType,
  TextRun, PageNumber, TabStopType, TabStopPosition,
  Table, TableRow, TableCell, WidthType, BorderStyle,
  LineNumberRestartFormat, convertInchesToTwip
} from "docx";

const LETTER_WIDTH  = 12240;  // 8.5" in twips
const LETTER_HEIGHT = 15840;  // 11" in twips
const MARGIN_1IN    = 1440;   // 1" in twips
const MARGIN_2_5IN  = 3600;   // 2.5" in twips (page-1 top margin)
const CONTENT_WIDTH = 9360;   // 6.5" content area (8.5 - 1 - 1)

const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: "Times New Roman",
          size: 24,           // 12 pt (docx uses half-points)
        },
        paragraph: {
          spacing: {
            line: 480,        // double-spaced: 480 twips (240 × 2)
            lineRule: "auto",
          },
        },
      },
    },
  },
  sections: [
    // ─── Section 1: Page 1 (2.5" top margin) ────────────────────
    {
      properties: {
        type: SectionType.CONTINUOUS,
        page: {
          size: { width: LETTER_WIDTH, height: LETTER_HEIGHT },
          margin: {
            top:    MARGIN_2_5IN,  // 2.5" on page 1 for attorney block
            right:  MARGIN_1IN,
            bottom: MARGIN_1IN,
            left:   MARGIN_1IN,
            header: 720,           // 0.5"
            footer: 720,
          },
        },
        lineNumbers: {                                // CRC 2.108(b)
          countBy: 1,
          restart: LineNumberRestartFormat.NEW_PAGE,
        },
      },
      footers: {
        default: makeFooter("DEFENDANT'S MOTION TO COMPEL", "24STCV12345"),
      },
      children: [
        ...attyBlock,      // attorney / party info block
        courtNamePara,     // centered court name
        captionTable,      // party block + case info table
        dividerParagraph,  // horizontal rule below caption
        ...bodyContent,    // body paragraphs (auto-line-numbered by section property)
        // End of page 1 — section break after last line of page 1
        // docx-js auto-paginates; the section break fires at the
        // end of this section's content
      ],
    },
    // ─── Section 2: Pages 2+ (1" top margin) ────────────────────
    {
      properties: {
        type: SectionType.NEXT_PAGE,
        page: {
          size: { width: LETTER_WIDTH, height: LETTER_HEIGHT },
          margin: {
            top:    MARGIN_1IN,    // 1" on subsequent pages
            right:  MARGIN_1IN,
            bottom: MARGIN_1IN,
            left:   MARGIN_1IN,
            header: 720,
            footer: 720,
          },
        },
        lineNumbers: {                                // CRC 2.108(b)
          countBy: 1,
          restart: LineNumberRestartFormat.NEW_PAGE,
        },
      },
      footers: {
        default: makeFooter("DEFENDANT'S MOTION TO COMPEL", "24STCV12345"),
      },
      children: [
        ...remainingBodyContent,
        ...exhibits,
      ],
    },
  ],
});
```

**Note on section breaks**: `docx-js` v7+ supports the two-section
pattern. Place page-1 content (attorney block, caption, first page
of body) in section 1, and the rest of the document in section 2.
The `NEXT_PAGE` section type forces the margin change at the exact
page boundary.

## Footer with "Page X of Y" (CRC 2.110)

```javascript
function makeFooter(docTitle, caseNo) {
  return new Footer({
    children: [
      new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
        children: [
          new TextRun({
            text: `${docTitle} — Case No. ${caseNo}`,
            font: "Times New Roman",
            size: 20,   // 10 pt
          }),
          // Right-aligned page counter
          new TextRun({ children: ["\t"] }),
          new TextRun({
            text: "Page ",
            font: "Times New Roman",
            size: 20,
          }),
          new TextRun({
            children: [PageNumber.CURRENT],
            font: "Times New Roman",
            size: 20,
          }),
          new TextRun({
            text: " of ",
            font: "Times New Roman",
            size: 20,
          }),
          new TextRun({
            children: [PageNumber.TOTAL_PAGES],
            font: "Times New Roman",
            size: 20,
          }),
        ],
      }),
    ],
  });
}
```

## Line numbering (CRC 2.108(b))

**MANDATORY under CRC 2.108(b).** Apply line numbering through
the section's `lineNumbers` property. Number every line
(`countBy: 1`) and restart the count on each page
(`restart: NEW_PAGE`) — the California pleading-paper
convention. Both sections (page 1 and pages 2+) must set the
same property so numbering is continuous across the section
break.

```javascript
import { LineNumberRestartFormat } from "docx";

properties: {
  // `type` is set per the Document setup above:
  //   section 1 (page 1)   -> SectionType.CONTINUOUS
  //   section 2 (pages 2+) -> SectionType.NEXT_PAGE
  page: { /* size + margins, as in Document setup above */ },
  lineNumbers: {
    countBy: 1,                                // number every line
    restart: LineNumberRestartFormat.NEW_PAGE, // restart 1.. each page
  },
}
```

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>`
into the section's `<w:sectPr>`. The numbers render in the
left margin and do NOT shift the 1-inch text margin.

CRC 2.108(b) lays out the substantive requirements that the
recipe satisfies:

- **Each line on each page numbered consecutively** (countBy: 1)
- **Beginning with the number 1 on each page** (restart: NEW_PAGE)
- **Lines spaced 1/4-inch (1.5-spaced) or 1/3-inch (double-
  spaced) apart**, matching the body text's line spacing

The `docx` default body line spacing of 480 twips
(double-spaced) keeps the line-numbers and body lines aligned.
At 1.5-line spacing, set body `spacing: { line: 360, lineRule:
"auto" }` and the numbers will follow.

### `start` attribute caveat

**Do NOT set `start` explicitly.** When `start` is omitted, the
OOXML default is 1 and the first line renders as "1". But
passing `start: 1` emits `w:start="1"`, which LibreOffice
(commonly used for headless PDF rendering) renders off by one —
the first body line shows "2". Omitting `start` renders
correctly as 1..N on every page in both Microsoft Word and
LibreOffice.

`distance` (the gap between the numbers and the text) is
optional; the default is fine.

Verified against the `docx` npm package: the `lineNumbers`
section property, the `countBy` / `restart` keys, and
`LineNumberRestartFormat.NEW_PAGE`.

### Two-section pattern

When using the two-section pattern shown in the Document setup
(section 1 for page 1's 2.5-inch top margin; section 2 for
pages 2+ at 1-inch top margin), apply the same `lineNumbers`
property to BOTH sections. Without it on section 2, the
numbers stop appearing at the section break.

## Margin rule (double vertical line)

Line-numbered pleading paper conventionally carries a *double*
vertical rule — two thin parallel lines down the left margin,
between the line numbers and the body text — matching the
pre-printed Judicial Council pleading paper. Apply it by default
to every line-numbered pleading; exhibits are exempt.

### Do NOT use an OOXML `double` page border

A `<w:pgBorders>` left border with `w:val="double"` does draw two
lines, but the OOXML `double` style **couples the inter-line gap
to the line weight** — widening the gap (via `w:sz`) also thickens
both lines into heavy bars. You cannot get thin lines *and* a wide
gap this way. Use two independent line shapes instead.

### Two header-anchored line shapes

Draw the two lines as two separate thin filled rectangles (VML
`v:rect`), anchored in the **page header** so they repeat on every
page, positioned absolutely relative to the page.

**One shape per `<w:pict>`.** Multiple `<v:rect>` elements inside
a single `<w:pict>` will **not** all render — each rectangle needs
its own `<w:pict>` inside its own `<w:r>` run:

```xml
<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
     xmlns:v="urn:schemas-microsoft-com:vml">
  <w:pict>
    <v:rect id="VRuleOuter"
      style="position:absolute;margin-left:60pt;margin-top:21.6pt;width:0.75pt;height:748.8pt;mso-position-horizontal-relative:page;mso-position-vertical-relative:page;z-index:-251658240"
      fillcolor="black" stroked="f"/>
  </w:pict>
</w:r>
```

The second run is identical with `margin-left:67pt` and
`id="VRuleInner"`.

`docx-js` has no first-class API for header-anchored,
absolutely-positioned VML shapes. Add them with the docx skill's
**unpack → edit → pack** workflow: generate the file with docx-js (give
each section an empty `Header` so a `word/header1.xml` part exists, and
keep the `lineNumbers` section property from above), then rewrite the
header XML and repack:

```bash
python scripts/office/unpack.py out.docx unpacked/
#   ... inject the rule into unpacked/word/header*.xml (helper below) ...
python scripts/office/pack.py unpacked/ out.docx --original out.docx
```

Inside each `unpacked/word/header*.xml`, declare the VML namespace on the
root `<w:hdr>` and add the two runs — one `v:rect` per `<w:pict>` per
`<w:r>` — inside the header paragraph. A document can have several header
parts (first-page / even / default, or one per section); add the runs to
**each** distinct `word/header*.xml`, giving every `v:rect` a unique `id`.
This stdlib helper (no `python-docx`) does it and is idempotent:

```python
import pathlib, re

def _runs(i):
    outer = ('<w:r><w:pict><v:rect id="VRuleOuter%d" '
             'style="position:absolute;margin-left:60pt;margin-top:21.6pt;'
             'width:0.75pt;height:748.8pt;'
             'mso-position-horizontal-relative:page;'
             'mso-position-vertical-relative:page;z-index:-251658240" '
             'fillcolor="black" stroked="f"/></w:pict></w:r>') % i
    return outer + (outer.replace('VRuleOuter%d' % i, 'VRuleInner%d' % i)
                         .replace('margin-left:60pt', 'margin-left:67pt'))

word = pathlib.Path('unpacked/word')

# 1. Double rule: one set of shapes per distinct header part (unique ids).
for i, hdr in enumerate(sorted(word.glob('header*.xml'))):
    xml = hdr.read_text(encoding='utf-8')
    if 'VRuleOuter' in xml:                                   # idempotent
        continue
    if 'xmlns:v=' not in xml:
        xml = re.sub(r'(<w:hdr\b)',
                     r'\1 xmlns:v="urn:schemas-microsoft-com:vml"', xml, count=1)
    xml = xml.replace('</w:p>', _runs(i) + '</w:p>', 1)       # first header para
    hdr.write_text(xml, encoding='utf-8')

# 2. Keep line numbers off header/footer text.
for f in list(word.glob('header*.xml')) + list(word.glob('footer*.xml')):
    xml = f.read_text(encoding='utf-8')
    xml = re.sub(r'(<w:pPr(?:\s[^>]*)?>)(?!<w:suppressLineNumbers/>)',
                 r'\1<w:suppressLineNumbers/>', xml)
    xml = re.sub(r'(<w:p(?:\s[^>]*)?>)(?!<w:pPr)',
                 r'\1<w:pPr><w:suppressLineNumbers/></w:pPr>', xml)
    f.write_text(xml, encoding='utf-8')
```

The `<w:lnNumType>` line-numbering element is already emitted by docx-js's
`lineNumbers` section property (above), so the patch only touches the
header / footer parts.

**Geometry** (US Letter, 1-inch margins, line-number `distance` of 360
twips = ¼″):

- Body text left edge sits at 72 pt from the page edge; the line-number
  gutter at ~54 pt.
- The two rules at `margin-left` **60 pt** and **67 pt** sit ~7 pt apart,
  both clear of the numbers (~54 pt) and the text (72 pt). The gap is the
  difference of the two values; tune them, keeping both between the gutter
  and the text margin.
- `margin-top:21.6pt` + `height:748.8pt` spans ~0.3″–10.7″ on an 11″ page
  (effectively full height); `width:0.75pt` is the line weight;
  `fillcolor="black" stroked="f"`.

### Verify

```bash
python scripts/office/validate.py out.docx
python scripts/office/soffice.py --headless --convert-to pdf out.docx
```

Confirm two thin parallel lines with a clear gap appear between the numbers
and the text on **every** page (including page 2 and later), and that the
header / footer text is not line-numbered. Then **open the `.docx` in
Microsoft Word** — VML renders slightly differently in Word vs LibreOffice,
and the output must be correct in Word; this check cannot be skipped.
## Caption table (CRC 2.111)

The caption table and other borderless tables in this file
share a small helper for the borders config:

```javascript
function allNoBorders() {
  const none = { style: BorderStyle.NONE };
  return { top: none, bottom: none, left: none, right: none,
           insideH: none, insideV: none };
}
```

```javascript
// ) column separating party block from case info
// Left cell: ~3.5" wide; right cell: ~3" wide
const captionTable = new Table({
  width: { size: CONTENT_WIDTH, type: WidthType.DXA },
  borders: allNoBorders(),
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 5040, type: WidthType.DXA },
          borders: allNoBorders(),
          children: [
            cPara("VELOCITY INVESTMENTS, LLC,             )"),
            cPara("                                       )"),
            cPara("          Plaintiff,                   )"),
            cPara("                                       )"),
            cPara("    vs.                                )"),
            cPara("                                       )"),
            cPara("JANE DOE,                              )"),
            cPara("                                       )"),
            cPara("          Defendant.                   )"),
          ],
        }),
        new TableCell({
          width: { size: 4320, type: WidthType.DXA },
          borders: allNoBorders(),
          children: [
            cPara("Case No. 24STCV12345"),
            cPara(""),
            cPara("DEFENDANT'S NOTICE OF MOTION"),
            cPara("AND MOTION TO COMPEL;"),
            cPara("MEMORANDUM OF POINTS AND"),
            cPara("AUTHORITIES"),
            cPara(""),
            cPara("Date:  March 15, 2025"),
            cPara("Time:  10:00 a.m."),
            cPara("Dept.: 36"),
            cPara("Judge: Hon. John Smith"),
          ],
        }),
      ],
    }),
  ],
});

function cPara(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Times New Roman", size: 24 })],
    spacing: { before: 0, after: 0, line: 320, lineRule: "auto" },
  });
}
```

## Attorney/party info block (page 1, upper-left)

The attorney block appears in the top-left of page 1, within the
2.5-inch top margin space. Because the page margin is 2.5 inches,
the content area begins 2.5 inches from the top. The attorney
block is the first content in section 1.

```javascript
const attyBlock = [
  aPara("JANE DOE"),
  aPara("123 Main Street"),
  aPara("Los Angeles, CA 90012"),
  aPara("Tel: (213) 555-0100"),
  aPara("Email: jane.doe@email.com"),
  aPara(""),
  aPara("Defendant, self-represented"),
  aPara(""),
];

function aPara(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Times New Roman", size: 22 })],
    spacing: { before: 0, after: 0, line: 240, lineRule: "auto" },
  });
}
```

## Packaging and saving

```javascript
const buffer = await Packer.toBuffer(doc);
fs.writeFileSync("motion-to-compel.docx", buffer);
```

To convert to PDF for filing, use the `.docx` as the working
copy and either:
- Open in Microsoft Word → File → Save as PDF (best fidelity)
- Use `python scripts/office/soffice.py --headless --convert-to pdf motion-to-compel.docx`
  (for server-side conversion; minor formatting differences from Word)
- Use the `docx-pdf` npm package (wraps LibreOffice)

## Validation

Run `plugins/ca-court-docs/scripts/format-check.py` on the
generated `.docx` to validate:
- 2.5-inch top margin on page 1
- CRC 2.110 footer present on all pages
- Font: Times New Roman 12 pt
- Line spacing: double or 1.5
- Line numbers present on left margin

The script will FAIL on a document missing the footer, having
the wrong top margin, or missing line numbers.

## California docx layout — quick reference

| Element | California requirement |
|---------|------------------------|
| Top margin, page 1 | 2.5" (CRC 2.110 attorney/party info block) |
| Top margin, pages 2+ | 1" |
| Section break needed? | Yes — 2-section pattern for the page-1 → pages-2+ top-margin shift |
| Line numbers | **Required** under CRC 2.108(b) — both sections carry the `lineNumbers` property |
| Footer | CRC 2.110: short document title + case number + Page X of Y |
| Caption style | Two-column with right-side `)` separator between party block and case info |
| Two-hole punch | Top center, 2¾" apart (paper filings only; CRC 2.119) |
