# docx-js Generation Patterns — Oregon UTCR 2.010

Working recipes for producing UTCR 2.010-compliant `.docx` files
using the `docx` npm package
(https://docx.js.org/) for upload to OJD File and Serve.

## Why .docx, not direct PDF?

OJD File and Serve accepts only PDF. The clean workflow is:

1. Generate the `.docx` from a template using `docx-js`
2. Save it locally so the litigant can review/edit in Word
3. Print or "Save As PDF" to produce the upload file
4. Upload the PDF to File and Serve, picking the matching UTCR
   2.110 document code

Producing `.docx` (rather than direct PDF) gives the litigant a
review surface — most pro se filers want to read and tweak before
filing.

## Document setup

```javascript
import { Document, Packer, Paragraph, PageOrientation,
         SectionType, Footer, AlignmentType, TextRun,
         PageNumber, TabStopType, TabStopPosition, HeaderFooter,
         LineNumberRestartFormat,
         convertInchesToTwip } from "docx";

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Times New Roman", size: 24 },  // 12 pt
        paragraph: {
          spacing: { line: 360, lineRule: "auto" },  // 1.5x
        },
      },
    },
  },
  sections: [{
    properties: {
      page: {
        size: {
          width: 12240,   // 8.5"
          height: 15840,  // 11"
        },
        margin: {
          top: 1440,      // 1"
          right: 1440,
          bottom: 1440,
          left: 1440,
          header: 720,    // 0.5"
          footer: 720,
        },
      },
      lineNumbers: {                                  // pleading paper
        countBy: 1,
        restart: LineNumberRestartFormat.NEW_PAGE,
      },
    },
    footers: { default: makeFooter("Motion to Compel — Case No. 25CV12345") },
    children: [
      // 2-inch leading spacer to push first content down to ~3" from top of page 1
      new Paragraph({ spacing: { before: 2880 } }),
      ...captionAndBody,
    ],
  }],
});
```

## Footer with "Page X of Y" (UTCR 2.010(4))

```javascript
function makeFooter(documentTitle) {
  return new Footer({
    children: [
      new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
        children: [
          new TextRun({
            text: documentTitle,
            font: "Times New Roman",
            size: 20,  // 10 pt
          }),
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

The `PageNumber.CURRENT` and `PageNumber.TOTAL_PAGES` constants
emit `PAGE` and `NUMPAGES` Word fields — these are what
`scripts/format-check.py` looks for. A static "Page 5" string in
the footer will FAIL the format check.

## Caption table

See `caption-format.md` for the full caption-table recipe. Key
details:

- Two cells, 4,680 DXA each
- Vertical rule on the right of left cell OR left of right cell
  (not both)
- No top, bottom, left-of-left, right-of-right borders
- Horizontal rule below the table, full width

## Numbered paragraphs

Oregon uses bold Arabic numerals followed by a period and tab:

```javascript
const para = (num, text) => new Paragraph({
  children: [
    new TextRun({ text: `${num}.`, bold: true }),
    new TextRun({ text: "\t" }),
    new TextRun({ text }),
  ],
  indent: { left: 720, hanging: 720 },  // hanging indent for wrapping
});
```

For paragraphs with a bold lead-in label:

```javascript
const labeledPara = (num, label, text) => new Paragraph({
  children: [
    new TextRun({ text: `${num}.`, bold: true }),
    new TextRun({ text: "\t" }),
    new TextRun({ text: `${label}. `, bold: true }),
    new TextRun({ text }),
  ],
  indent: { left: 720, hanging: 720 },
});
```

## Signature block

```javascript
const signatureBlock = (name, role, address, phone, email) =>
  new Paragraph({
    spacing: { before: 480 },
    children: [
      new TextRun({ text: "DATED this ____ day of __________, 20__." }),
      new TextRun({ break: 1 }),
      new TextRun({ text: "Executed at " }),
      new TextRun({ text: "[city], Oregon." }),
      new TextRun({ break: 3 }),
      new TextRun({ text: "______________________________________" }),
      new TextRun({ break: 1 }),
      new TextRun({ text: name, bold: true }),
      new TextRun({ break: 1 }),
      new TextRun({ text: role }),
      new TextRun({ break: 1 }),
      new TextRun({ text: address }),
      new TextRun({ break: 1 }),
      new TextRun({ text: phone }),
      new TextRun({ break: 1 }),
      new TextRun({ text: email }),
    ],
  });
```

## Verification clause (declarations only)

```javascript
const verificationClause = new Paragraph({
  spacing: { before: 360 },
  children: [
    new TextRun({
      text: "I declare under penalty of perjury under the laws " +
            "of the State of Oregon that the foregoing is true " +
            "and correct.",
    }),
  ],
});
```

(Per ORCP 1 E; the longer "I hereby declare..." form is also
acceptable but ORCP 1 E is the cleanest.)

## Line numbering (pleading paper)

Apply line numbering through the section's `lineNumbers`
property. Number every line (`countBy: 1`) and restart the
count on each page (`restart: NEW_PAGE`) — the standard
pleading-paper convention.

```javascript
import { LineNumberRestartFormat } from "docx";

sections: [{
  properties: {
    page: { /* size + margins, as in Document setup above */ },
    lineNumbers: {
      countBy: 1,                                // number every line
      restart: LineNumberRestartFormat.NEW_PAGE, // restart 1.. each page
    },
  },
  footers: { default: makeFooter(...) },
  children: buildBody(),
}]
```

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>`
into the section's `<w:sectPr>`. The numbers render in the
left margin and do not shift the 1-inch text margin.

UTCR 2.010 does not itself require line numbering, but it's
the near-universal convention in Oregon civil practice. Apply
by default to every motion, memorandum, declaration, notice of
hearing, and proposed order. Exhibits / attachments are
exempt.

**Do NOT set `start` explicitly.** When `start` is omitted, the
OOXML default is 1 and the first line renders as "1". But
passing `start: 1` emits `w:start="1"`, which LibreOffice
(commonly used for headless PDF rendering) renders off by one —
the first body line shows "2". Omitting `start` renders
correctly as 1..N on every page in both Microsoft Word and
LibreOffice. `distance` (the gap between the numbers and the
text) is optional; the default is fine.

Verified against the `docx` npm package: the `lineNumbers`
section property, the `countBy` / `restart` keys, and
`LineNumberRestartFormat.NEW_PAGE`.

## Margin rule (double vertical line)

Line-numbered pleading paper conventionally carries a *double*
vertical rule — two thin parallel lines down the left margin,
between the line numbers and the body text. Apply it by default
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
## Common pitfalls

1. **A4 default**. `docx-js` defaults to A4. Set page size
   explicitly to 12,240 × 15,840 DXA.
2. **Static page numbers**. Never type "Page 3 of 7" as literal
   text — Word can't update it. Use `PageNumber.CURRENT` and
   `PageNumber.TOTAL_PAGES`.
3. **Missing leading space**. The 3-inch top margin on page 1 is
   achieved by leaving the section's top margin at 1 inch and
   adding 2 inches of leading paragraph space at the start of the
   body. Without it, page 1 will look identical to page 2 and
   bleed into the clerk's stamp zone.
4. **Color**. Don't use `color: "0000FF"` for hyperlinks or
   `highlight: "yellow"` for emphasis — UTCR 2.010 forbids both
   in the body. Use bold and italic instead.
5. **Unicode bullets**. Use the docx numbering config
   (`LevelFormat.BULLET`) rather than typing `•` or `*` — Word
   handles them differently across systems.
6. **Tab stops not set**. The right-aligned page counter requires
   an explicit tab stop at 9,360 DXA. Without it, "Page X of Y"
   falls in the middle of the footer.
7. **`lineNumbers.start: 1`**. Don't pass an explicit `start: 1`
   to `lineNumbers` — it renders off by one in LibreOffice
   (the first body line shows "2"). Omit `start`; it defaults
   to 1.

## Verification

After generation, run:

```bash
python3 plugins/or-court-docs/scripts/format-check.py path/to/draft.docx
```

It will validate paper size, margins, fonts, color, line spacing,
and the footer fields. Address every FAIL before saving as PDF and
uploading.
