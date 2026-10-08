# docx-js Generation Patterns for WA Pleadings

Reference patterns for producing GR 14-compliant Washington court documents
with the `docx` npm package.

## Install

```bash
npm install docx
```

## Skeleton

```javascript
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, ImageRun,
  Header, Footer, AlignmentType, PageNumber,
  Table, TableRow, TableCell, WidthType, BorderStyle,
  TabStopType, VerticalAlign, LineNumberRestartFormat,
} = require('docx');

const TNR = "Times New Roman";
const SIZE_12 = 24;  // half-points
const SIZE_10 = 20;

const doc = new Document({
  creator: "[Filer name]",
  title: "Document Title",
  styles: {
    default: {
      document: {
        run: { font: TNR, size: SIZE_12 },
        paragraph: { spacing: { line: 360, lineRule: "auto" } },
      },
    },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },    // US Letter
        margin: {
          top: 1440, right: 1440, bottom: 1440, left: 1440,
          footer: 720, header: 720, gutter: 0,
        },
      },
      lineNumbers: {                               // pleading paper
        countBy: 1,
        restart: LineNumberRestartFormat.NEW_PAGE,
      },
    },
    footers: { default: buildFooter() },
    children: buildBody(),
  }],
});

Packer.toBuffer(doc).then(buf => fs.writeFileSync("out.docx", buf));
```

## Three-inch top margin on page 1

docx-js doesn't support a different first-page margin directly. The
clean workaround is to add ~2 inches of leading space on the first
paragraph:

```javascript
new Paragraph({
  spacing: { before: 2880, line: 240, lineRule: "auto", after: 0 },  // 2 inches
  children: [new TextRun("")],
});
```

With a 1-inch section top margin, this yields an effective 3-inch top
margin on page 1 and a 1-inch top margin on all subsequent pages — exactly
what GR 14 requires.

## Required footer: title left, "Page X of Y" right

**Every generated document must include this footer.** It is validated by
`scripts/format-check.py` and a missing or incomplete footer FAILs the check.

```javascript
function buildFooter() {
  return new Footer({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
      spacing: { line: 240, lineRule: "auto", after: 0 },
      children: [
        new TextRun({ text: FOOTER_TITLE, font: TNR, size: SIZE_10 }),
        new TextRun({ text: "\t", font: TNR, size: SIZE_10 }),
        new TextRun({ text: "Page ", font: TNR, size: SIZE_10 }),
        new TextRun({ children: [PageNumber.CURRENT], font: TNR, size: SIZE_10 }),
        new TextRun({ text: " of ", font: TNR, size: SIZE_10 }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: TNR, size: SIZE_10 }),
      ],
    })],
  });
}
```

Requirements:

- `FOOTER_TITLE` is a single-line identifier such as
  `"Motion to Compel — Case No. 25CIV######KCX"`. It must be non-empty and
  must not consist only of the word "Page" or "of".
- Both `PageNumber.CURRENT` (renders as a `PAGE` field) and
  `PageNumber.TOTAL_PAGES` (renders as `NUMPAGES`) must be present — use
  "Page X of Y", not "Page X" alone.
- Pass the footer via `section.footers.default` so it applies to every
  page including exhibit pages. Do not restart pagination after the
  signature block.

## Line numbering (pleading paper)

Apply line numbering through the section's `lineNumbers` property. Number
every line (`countBy: 1`) and restart the count on each page
(`restart: NEW_PAGE`) — the standard pleading-paper convention.

```javascript
const { LineNumberRestartFormat } = require('docx');

sections: [{
  properties: {
    page: { /* size + margins, as in the skeleton above */ },
    lineNumbers: {
      countBy: 1,                                // number every line
      restart: LineNumberRestartFormat.NEW_PAGE, // restart 1.. on each page
    },
  },
  footers: { default: buildFooter() },
  children: buildBody(),
}]
```

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>` into the
section's `<w:sectPr>`. The numbers render in the left margin and do not
shift the 1-inch text margin.

**Do NOT set `start` explicitly.** When `start` is omitted, the OOXML
default is 1 and the first line renders as "1". But passing `start: 1`
emits `w:start="1"`, which LibreOffice (used here to render PDF previews)
renders off by one — the first body line shows "2". Omitting `start`
renders correctly as 1..N on every page in both Microsoft Word and
LibreOffice. `distance` (the gap between the numbers and the text) is
optional; the default is fine.

Verified against the `docx` npm package: the `lineNumbers` section
property, the `countBy` / `restart` keys, and `LineNumberRestartFormat.NEW_PAGE`.

## Margin rule (double vertical line)

Line-numbered pleading paper conventionally carries a *double* vertical rule —
two thin parallel lines down the left margin, between the line numbers and the
body text. Apply it by default to every line-numbered pleading; exhibits are
exempt.

### Do NOT use an OOXML `double` page border

A `<w:pgBorders>` left border with `w:val="double"` does draw two lines, but
the OOXML `double` style **couples the inter-line gap to the line weight** —
widening the gap (via `w:sz`) also thickens both lines into heavy bars. You
cannot get thin lines *and* a wide gap this way. Use two independent line
shapes instead.

### Two header-anchored line shapes

Draw the two lines as two separate thin filled rectangles (VML `v:rect`),
anchored in the **page header** so they repeat on every page, positioned
absolutely relative to the page.

**One shape per `<w:pict>`.** Multiple `<v:rect>` elements inside a single
`<w:pict>` will **not** all render — each rectangle needs its own `<w:pict>`
inside its own `<w:r>` run:

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

The second run is identical with `margin-left:67pt` and `id="VRuleInner"`.

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

def _runs(i, outer_pt=60, inner_pt=67):
    # Default outer_pt / inner_pt are tuned to a 1-inch left text margin;
    # see "Geometry" below for the formula at non-default margins.
    outer = ('<w:r><w:pict><v:rect id="VRuleOuter%d" '
             'style="position:absolute;margin-left:%dpt;margin-top:21.6pt;'
             'width:0.75pt;height:748.8pt;'
             'mso-position-horizontal-relative:page;'
             'mso-position-vertical-relative:page;z-index:-251658240" '
             'fillcolor="black" stroked="f"/></w:pict></w:r>') % (i, outer_pt)
    return outer + (outer.replace('VRuleOuter%d' % i, 'VRuleInner%d' % i)
                         .replace('margin-left:%dpt' % outer_pt,
                                  'margin-left:%dpt' % inner_pt))

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

The 60 pt / 67 pt rule positions are **tuned to the 1-inch left text
margin assumption**. If your section uses a different left margin, the
default positions will silently render the rules between the page edge
and the line numbers — i.e., on the wrong side. Choose rule positions for
a non-default left margin using:

```
outer_pt = left_margin_pt − 12
inner_pt = left_margin_pt − 5
```

Pass them as keyword arguments to `_runs(i, outer_pt=..., inner_pt=...)`
above. For example, a 1.5-inch left margin (108 pt) gives `outer_pt=96`
and `inner_pt=103`. The 7 pt inter-line gap is preserved; both values sit
between the line numbers and the text. The default `60 / 67` is the
result of this formula for `left_margin_pt = 72`.

### Verify

```bash
python scripts/office/validate.py out.docx
python scripts/office/soffice.py --headless --convert-to pdf out.docx
```

Open the generated PDF. On every page (including page 2 and later),
confirm the left-to-right order is:

```
page edge → line numbers (1, 2, 3…) → double rule → body text
```

Two thin parallel lines with a clear gap between them appear between the
numbers and the text, and the header / footer text is not line-numbered.
**If the rules appear to the left of the numbers**, the recipe's left-margin
assumption is being violated — re-derive `outer_pt` / `inner_pt` from the
formula above and regenerate. Finally, **open the `.docx` in Microsoft
Word** — VML renders slightly differently in Word vs LibreOffice, and the
output must be correct in Word; this check cannot be skipped.
## Numbered paragraphs with hanging indent

```javascript
function numPara(num, leadIn, rest) {
  const runs = [new TextRun({ text: `${num}.\t`, bold: true, font: TNR, size: SIZE_12 })];
  if (leadIn) runs.push(new TextRun({ text: leadIn, bold: true, font: TNR, size: SIZE_12 }));
  if (rest) runs.push(new TextRun({ text: rest, font: TNR, size: SIZE_12 }));
  return new Paragraph({
    spacing: { line: 360, lineRule: "auto", after: 240 },
    tabStops: [{ type: TabStopType.LEFT, position: 720 }],
    indent: { left: 720, hanging: 720 },
    children: runs,
  });
}
```

Use `numPara(3, "Court Hearing of March 9, 2026. ", "On March 9, 2026, I attended...")`
for bold-lead-in-style paragraphs.

## Bullet sub-lines under a paragraph

Use a numbering config rather than unicode bullet characters:

```javascript
new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 1440, hanging: 360 } } },
      }],
    }],
  },
  // ...
});

new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  children: [new TextRun("10:10 AM — 117 BPM")],
});
```

## Images

```javascript
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new ImageRun({
    type: "png",    // REQUIRED
    data: fs.readFileSync(imgPath),
    transformation: { width: 280, height: 607 },
    altText: { title, description, name },   // all three required
  })],
});
```

## Common pitfalls

- **Default page size is A4** — always set US Letter explicitly
- **`\n` does not create paragraphs** — use separate `Paragraph` objects
- **`PageBreak` must be inside a `Paragraph`** — not a standalone element
- **Tables require both `columnWidths` and cell `width`** with matching DXA
  values — otherwise tables render wrong in Google Docs
- **Use `WidthType.DXA`, not `PERCENTAGE`** — percentage breaks in Google Docs
- **Use `ShadingType.CLEAR`, not `SOLID`** — SOLID produces black backgrounds
- **Never insert unicode bullet characters directly** — always use
  `LevelFormat.BULLET` with a numbering config
- **Don't pass `start` to `lineNumbers`** — an explicit `start: 1` renders
  off by one in LibreOffice; omit it (it defaults to 1)

## Validation

After generating:

```bash
python scripts/office/validate.py out.docx
```

And run the bundled GR 14 check:

```bash
python scripts/format-check.py out.docx
```
