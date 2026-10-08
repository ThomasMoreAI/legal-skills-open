# Caption Format

A Washington court caption has three parts: the court header, the parties
block, and the case number / document title block. The latter two sit
side-by-side separated by a vertical rule.

## Layout

```
             KING COUNTY DISTRICT COURT, SOUTH DIVISION
                 IN AND FOR THE STATE OF WASHINGTON

VELOCITY INVESTMENTS, LLC,          │   No. 25CIV######KCX
                                    │
         Plaintiff,                 │   SECOND SUPPLEMENTAL
                                    │   DECLARATION OF JOHN DOE
vs.                                 │   IN SUPPORT OF
                                    │   COUNTERCLAIM FOR
JOHN DOE,                           │   EMOTIONAL DISTRESS
                                    │   DAMAGES (HEARING-DAY
         Defendant/Counter-         │   BIOMETRIC DATA)
         Claimant.                  │
─────────────────────────────────────────────────────────────
```

A horizontal rule below the caption separates it from the body.

## Rules

- Court name is centered and bold across the top
- Parties (left cell) are in ALL CAPS, bold; role (Plaintiff, Defendant,
  etc.) is in normal case and indented under the party name
- Case number is bold on the right
- Document title is bold, ALL CAPS, wrapped so no line exceeds the right
  cell width (typically 4–6 lines)
- Vertical rule is one line on the right edge of the left cell OR the
  left edge of the right cell — never both (avoids doubling)

## docx-js implementation

Use a two-cell borderless table. Add a `right` border only on the left
cell to create the single vertical rule.

```javascript
const {
  Table, TableRow, TableCell, WidthType, BorderStyle,
  Paragraph, TextRun, AlignmentType, VerticalAlign,
} = require('docx');

const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const verticalBorder = {
  top: noBorder, bottom: noBorder, left: noBorder,
  right: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
};

new Table({
  width: { size: 9360, type: WidthType.DXA },   // 6.5" content width
  columnWidths: [4680, 4680],                   // equal split
  borders: {
    top: noBorder, bottom: noBorder, left: noBorder, right: noBorder,
    insideHorizontal: noBorder, insideVertical: noBorder,
  },
  rows: [
    new TableRow({
      children: [
        new TableCell({
          borders: verticalBorder,
          width: { size: 4680, type: WidthType.DXA },
          margins: { top: 60, bottom: 60, left: 60, right: 180 },
          verticalAlign: VerticalAlign.TOP,
          children: [/* party paragraphs */],
        }),
        new TableCell({
          borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
          width: { size: 4680, type: WidthType.DXA },
          margins: { top: 60, bottom: 60, left: 180, right: 60 },
          verticalAlign: VerticalAlign.TOP,
          children: [/* case number + title paragraphs */],
        }),
      ],
    }),
  ],
});
```

## Horizontal rule below caption

Apply a bottom border to a blank paragraph:

```javascript
new Paragraph({
  spacing: { before: 0, after: 200 },
  border: {
    bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 1 },
  },
  children: [new TextRun("")],
});
```

## Court header line — by court

| Court | Line 1 | Line 2 |
|-------|--------|--------|
| KCDC South Div. | KING COUNTY DISTRICT COURT, SOUTH DIVISION | IN AND FOR THE STATE OF WASHINGTON |
| KC Superior Court | SUPERIOR COURT OF WASHINGTON | FOR KING COUNTY |
| WA Supreme Court | THE SUPREME COURT OF THE STATE OF WASHINGTON | (no second line) |
| WA Court of Appeals | COURT OF APPEALS, DIVISION [N] | OF THE STATE OF WASHINGTON |
