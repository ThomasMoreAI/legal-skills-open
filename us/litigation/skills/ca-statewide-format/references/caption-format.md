# Caption Format (CRC 2.111)

A California superior-court caption has two parts:
(1) the attorney/party information block (upper-left) and
(2) the case body (court name, party block, and case
information). The format differs substantially from Oregon and
Washington, which use a two-column side-by-side split.

## Layout — full example

```
JANE DOE                                          (line 1 — name or firm)
123 Main Street                                   (line 2)
Los Angeles, CA 90012                             (line 3)
Tel: (213) 555-0100                               (line 4)
Fax: (213) 555-0101                               (line 5)
Email: jane.doe@email.com                         (line 6)
                                                  (line 7 — blank)
Defendant, self-represented                       (line 8)


                IN THE SUPERIOR COURT OF CALIFORNIA
                       COUNTY OF LOS ANGELES

VELOCITY INVESTMENTS, LLC,               )
                                         )  Case No. 24STCV12345
          Plaintiff,                     )
                                         )  DEFENDANT'S NOTICE OF
    vs.                                  )  MOTION AND MOTION TO
                                         )  COMPEL FURTHER
JANE DOE,                                )  RESPONSES TO SPECIAL
                                         )  INTERROGATORIES, SET
          Defendant.                     )  ONE; MEMORANDUM OF
                                         )  POINTS AND AUTHORITIES
                                         )
                                         )  Date:  March 15, 2025
                                         )  Time:  10:00 a.m.
                                         )  Dept.: 36
                                         )  Judge: Hon. John Smith
                                         )
                                         )  [Reservation No.: 12345678]
```

## Attorney/party information block (CRC 2.111(a))

The block occupies the upper-left of page 1, within the top
2.5 inches. Standard elements:

| Line | Content |
|------|---------|
| 1 | Attorney's name and State Bar number: "JOHN SMITH, State Bar No. 123456" — OR — pro se: "JANE DOE" |
| 2 | Firm name (if attorney) or blank (if pro se) |
| 3 | Street address |
| 4 | City, CA ZIP |
| 5 | Tel: (NNN) NNN-NNNN |
| 6 | Fax: (NNN) NNN-NNNN (may be omitted if no fax) |
| 7 | Email: address |
| 8 | (blank) |
| 9 | "Attorney for Plaintiff: [CLIENT NAME]" or "Attorney for Defendant: [CLIENT NAME]" |
|   | Pro se: "Plaintiff, self-represented" or "Defendant, self-represented" |

**State Bar number**: all licensed California attorneys must
include their California State Bar number in the information
block (Cal. Rules of Court, rule 2.111(a)(1)). Pro se litigants
omit the State Bar line.

**For pro se litigants**: use "Defendant, self-represented" (or
"Plaintiff, self-represented") on the last line of the block.
Some courts also accept "Defendant, in pro per" — both are
understood. Do NOT use "pro se" in formal California court
filings (it is a Latin term more common in federal courts;
California courts prefer "self-represented" or "in pro per").

## Court name line (CRC 2.111(b))

```
         IN THE SUPERIOR COURT OF CALIFORNIA
              COUNTY OF [COUNTY NAME]
```

Both lines are centered. In practice, both lines are often in
all caps or title case; either is accepted. The county name
is in all caps in most California court filings.

Do NOT write "Superior Court of the State of California" —
the official form is "Superior Court of California" (per the
Trial Court Funding and Unification Act and the current Judicial
Council forms).

## Party block and case information

**Left side**: party names, roles, and "vs." separator.

**Right side**: separated from the party block by a column of
closing parentheses `)`. The `)` column forms the visual
right boundary of the party block and is a distinctive feature
of California captions (contrasting with Oregon's explicit
vertical rule and Washington's use of a dividing line).

Each line of the party block ends with `)`, and the right
column (case number, document title, hearing info) is positioned
to the right of the `)` column.

**Party name format**:

- Party names in normal case (not ALL CAPS as in Oregon)
- Role (Plaintiff, Defendant) is indented and in regular case
- For an entity: "VELOCITY INVESTMENTS, LLC," — comma after
  the entity name, before the close-paren line
- For a person: "JANE DOE,"

**Separator**: Use **"vs."** (with period, not "v.") between
parties — California state-court convention. Federal courts
use "v." but California superior courts conventionally use
"vs."

**Case number formats** (selected courts):

| Court | Format | Example |
|-------|--------|---------|
| LA Superior (Stanley Mosk, unlimited) | `YYXXXXXX` | `24STCV12345` |
| LA Superior (limited civil) | `YYSMCVNNNNN` | `24SMCV12345` |
| San Francisco (unlimited) | `CGC-YY-NNNNNN` | `CGC-24-123456` |
| Orange County (unlimited) | `30-YYYY-NNNNNNN-CU-XX-CJC` | `30-2024-01234567-CU-OR-CJC` |
| San Diego (unlimited) | `37-YYYY-NNNNNNN-CU-XX-CTL` | `37-2024-00012345-CU-BC-CTL` |
| Alameda (unlimited) | `RGYYNNNNNNN` | `RG24123456` |
| Sacramento | `34-YYYY-NNNNNNN-CU` | `34-2024-00012345-CU-OR` |

## Document title and hearing info (right column)

For a **noticed motion**, the right column includes:

1. Document title (all caps, multi-line if needed)
2. Blank line
3. `Date:  [Month Day, Year]`
4. `Time:  [H:MM a.m./p.m.]`
5. `Dept.: [Department number]`
6. `Judge: Hon. [Judge's full name]`
7. (Optional) `Reservation No.: [CRS/reservation number]`

For a **declaration** or **memorandum**, the right column
includes only the document title and case number — no hearing info.

For a **proposed order**, include `[PROPOSED]` in brackets
at the start of the title:
`[PROPOSED] ORDER GRANTING DEFENDANT'S MOTION TO COMPEL`

## Multi-party / multi-claim captions

- On the complaint and all subsequent papers that add parties:
  list all parties
- Subsequent papers in a multi-party case may use the short form:
  "VELOCITY INVESTMENTS, LLC, et al."
- If the defendant has cross-claimed, note both roles:
  "JANE DOE, Defendant and Cross-Complainant,"
- For third-party complaints, add the role:
  "ACME CORP., Cross-Defendant,"

## docx-js implementation

```javascript
import { Document, Paragraph, Table, TableRow, TableCell,
         BorderStyle, AlignmentType, TextRun, WidthType,
         Footer, PageNumber, TabStopType, convertInchesToTwip } from "docx";

// Attorney/party info block (upper-left, within 2.5" from top)
const attyBlock = [
  new Paragraph({
    children: [new TextRun({ text: "JANE DOE", bold: false })],
    spacing: { before: 0, after: 0 },
  }),
  new Paragraph({ children: [new TextRun("123 Main Street")] }),
  new Paragraph({ children: [new TextRun("Los Angeles, CA 90012")] }),
  new Paragraph({ children: [new TextRun("Tel: (213) 555-0100")] }),
  new Paragraph({ children: [new TextRun("Email: jane.doe@email.com")] }),
  new Paragraph({ text: "" }),
  new Paragraph({ children: [new TextRun("Defendant, self-represented")] }),
  new Paragraph({ text: "" }),
];

// Court name (centered, below attorney block)
const courtName = new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "IN THE SUPERIOR COURT OF CALIFORNIA", bold: true }),
    new TextRun({ break: 1 }),
    new TextRun({ text: "COUNTY OF LOS ANGELES", bold: true }),
  ],
  spacing: { before: 240, after: 240 },
});

// Caption table — left cell: parties, right cell: case info
// Using the ) column approach: right-align the ) column
const captionTable = new Table({
  width: { size: 9360, type: WidthType.DXA },  // 6.5" content width
  borders: {
    top: { style: BorderStyle.NONE },
    bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.NONE },
    right: { style: BorderStyle.NONE },
    insideH: { style: BorderStyle.NONE },
    insideV: { style: BorderStyle.NONE },
  },
  rows: [
    new TableRow({
      children: [
        // Left cell: party names with ) at end of each line
        new TableCell({
          width: { size: 5040, type: WidthType.DXA },  // ~3.5"
          children: [
            makeParagraph("VELOCITY INVESTMENTS, LLC,           )"),
            makeParagraph("                                     )"),
            makeParagraph("          Plaintiff,                 )"),
            makeParagraph("                                     )"),
            makeParagraph("    vs.                              )"),
            makeParagraph("                                     )"),
            makeParagraph("JANE DOE,                            )"),
            makeParagraph("                                     )"),
            makeParagraph("          Defendant.                 )"),
          ],
        }),
        // Right cell: case number + document title + hearing info
        new TableCell({
          width: { size: 4320, type: WidthType.DXA },  // ~3"
          children: [
            makeParagraph("Case No. 24STCV12345"),
            makeParagraph(""),
            makeParagraph("DEFENDANT'S NOTICE OF MOTION"),
            makeParagraph("AND MOTION TO COMPEL;"),
            makeParagraph("MEMORANDUM OF POINTS AND"),
            makeParagraph("AUTHORITIES"),
            makeParagraph(""),
            makeParagraph("Date:  March 15, 2025"),
            makeParagraph("Time:  10:00 a.m."),
            makeParagraph("Dept.: 36"),
            makeParagraph("Judge: Hon. John Smith"),
          ],
        }),
      ],
    }),
  ],
});

function makeParagraph(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Times New Roman", size: 24 })],
    spacing: { before: 0, after: 0 },
  });
}
```

## Comparison to Oregon and Washington

| Element | California | Oregon | Washington |
|---------|------------|--------|------------|
| Court header | "IN THE SUPERIOR COURT OF CALIFORNIA / COUNTY OF [NAME]" | "IN THE CIRCUIT COURT OF THE STATE OF OREGON / FOR THE COUNTY OF [NAME]" | "[COURT NAME] / STATE OF WASHINGTON / COUNTY OF [NAME]" |
| Attorney info block | Upper-left, within 2.5" of top of page 1 | Not separately required (part of signature block) | Not separately required |
| Party name style | Normal case | ALL CAPS | ALL CAPS |
| Party separator | "vs." | "v." | "vs." |
| Case-number format | Varies by court / district | YYCVnnnnn | YY-[type]-nnnnn-n SEA |
| Exhibit labels | Lettered (A, B, C) | Numbered (1, 2, 3) | Lettered (A, B, C) |
| Caption visual device | Column of `)` on right of party block | Explicit vertical rule | Varies |
| Top margin, page 1 | 2.5 inches | 3 inches | 1 inch (no special top margin) |
| Line numbers | Required (CRC 2.108(b)) | Not required | Not required |

The most common authoring mistake when porting an Oregon or
Washington template to California is (1) forgetting the 2.5-inch
top margin, (2) omitting the attorney/party info block, and
(3) forgetting line numbers on the left margin.
