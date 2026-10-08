# Caption Format (UTCR 2.100)

An Oregon circuit-court caption has three parts: the court header,
the parties block, and the case number / document title block. The
latter two sit side-by-side separated by a vertical rule.

## Layout

```
              IN THE CIRCUIT COURT OF THE STATE OF OREGON
                     FOR THE COUNTY OF MULTNOMAH

VELOCITY INVESTMENTS, LLC,          │   Case No. 25CV12345
                                    │
         Plaintiff,                 │   SECOND SUPPLEMENTAL
                                    │   DECLARATION OF JOHN DOE
         v.                         │   IN SUPPORT OF
                                    │   COUNTERCLAIM FOR
JOHN DOE,                           │   DAMAGES UNDER THE OREGON
                                    │   UNLAWFUL TRADE PRACTICES
         Defendant.                 │   ACT (ORS 646.605 et seq.)
─────────────────────────────────────────────────────────────
```

A horizontal rule below the caption separates it from the body.

## Rules

- Court name is centered and bold across the top, two lines:
  - Line 1: "IN THE CIRCUIT COURT OF THE STATE OF OREGON"
  - Line 2: "FOR THE COUNTY OF [COUNTY NAME]"
- Parties (left cell) are in ALL CAPS, bold; role (Plaintiff,
  Defendant, Petitioner, Respondent) is in normal case and
  indented under the party name
- **Use "v." (lowercase, with period), not "vs." or "VS."** —
  Oregon convention
- Case number is bold on the right; format `25CV12345` for civil
  cases (no spaces, no dashes); `25SC` for small claims; `25DR`
  for domestic relations; `25PR` for probate; `25LT` for landlord-
  tenant FED actions
- Document title is bold, ALL CAPS, wrapped so no line exceeds the
  right cell width (typically 4–6 lines)
- Vertical rule is one line on the right edge of the left cell OR
  the left edge of the right cell — never both (avoids doubling)

## Case number formats by case type

| Code | Case type | Authority |
|------|-----------|-----------|
| CV | General civil | UTCR 2.100, OJD case type policy |
| SC | Small claims (≤ $10,000) | ORS Ch. 46 |
| DR | Domestic relations (dissolution, custody) | ORS Ch. 107 |
| PR | Probate | ORS Ch. 111–117 |
| LT | Landlord-tenant FED | ORS Ch. 105 |
| CR | Criminal (felony or misdemeanor) | ORS Ch. 131–169 |
| TR | Traffic / violations | ORS Ch. 153 |
| JV | Juvenile | ORS Ch. 419A–419C |

The first two digits are the year of filing; the middle code is
the case type; the last 5 digits are the sequential filing number
for that case type in that county for that year.

## Multi-party / multi-claim captions

- On the first pleading, list every party; thereafter, the short
  form is acceptable: "VELOCITY INVESTMENTS, LLC et al."
- If a counterclaim or cross-claim is pleaded, the party block
  should reflect both roles: "JOHN DOE, Defendant/Counter-
  Claimant."
- For an interpleader or third-party complaint, add the role to
  the party name: "ACME CORP., Third-Party Defendant."

## docx-js implementation

```javascript
import { Document, Paragraph, Table, TableRow, TableCell,
         BorderStyle, AlignmentType, HeadingLevel,
         TextRun, WidthType } from "docx";

const COURT_HEADER = new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "IN THE CIRCUIT COURT OF THE STATE OF OREGON",
                  bold: true }),
    new TextRun({ break: 1 }),
    new TextRun({ text: "FOR THE COUNTY OF MULTNOMAH",
                  bold: true }),
  ],
});

const captionTable = new Table({
  width: { size: 9360, type: WidthType.DXA },
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 4680, type: WidthType.DXA },
          borders: {
            top:    { style: BorderStyle.NONE },
            bottom: { style: BorderStyle.NONE },
            left:   { style: BorderStyle.NONE },
            right:  { style: BorderStyle.SINGLE, size: 6 },  // vertical rule
          },
          children: [
            new Paragraph({
              children: [
                new TextRun({ text: "VELOCITY INVESTMENTS, LLC,",
                              bold: true }),
              ],
            }),
            new Paragraph({ text: "" }),
            new Paragraph({ text: "         Plaintiff," }),
            new Paragraph({ text: "" }),
            new Paragraph({ text: "         v." }),
            new Paragraph({ text: "" }),
            new Paragraph({
              children: [new TextRun({ text: "JOHN DOE,", bold: true })],
            }),
            new Paragraph({ text: "" }),
            new Paragraph({ text: "         Defendant." }),
          ],
        }),
        new TableCell({
          width: { size: 4680, type: WidthType.DXA },
          borders: {
            top:    { style: BorderStyle.NONE },
            bottom: { style: BorderStyle.NONE },
            left:   { style: BorderStyle.NONE },
            right:  { style: BorderStyle.NONE },
          },
          children: [
            new Paragraph({
              children: [
                new TextRun({ text: "Case No. 25CV12345", bold: true }),
              ],
            }),
            new Paragraph({ text: "" }),
            new Paragraph({
              children: [
                new TextRun({
                  text: "DEFENDANT'S MOTION TO COMPEL " +
                        "PRODUCTION OF DOCUMENTS UNDER " +
                        "ORCP 46",
                  bold: true,
                }),
              ],
            }),
          ],
        }),
      ],
    }),
  ],
});
```

## Comparison to Washington

| Element | Washington | Oregon |
|---------|------------|--------|
| Court header | "[Court Name]" + "IN AND FOR THE STATE OF WASHINGTON" | "IN THE CIRCUIT COURT OF THE STATE OF OREGON" + "FOR THE COUNTY OF [name]" |
| Party separator | "vs." | "v." |
| Case-number prefix (KCSC) | `25-2-NNNNN-N SEA` | `25CV12345` |
| Case-number prefix (KCDC) | `25CIV######KCX` | (no analog — Oregon has unified Circuit Court) |
| Small claims | (in District Court) | `25SC#####` (in Circuit Court, small-claims division) |
| Exhibit labels | `Exhibit A, B, C ...` | `Exhibit 1, 2, 3 ...` |

The most common authoring mistake when porting a Washington
template to Oregon is forgetting to change `vs.` to `v.` and
forgetting to renumber exhibits from letters to numbers.
