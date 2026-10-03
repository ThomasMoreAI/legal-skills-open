# Exhibit Handling — California (CRC 3.1110(f))

## Where exhibits live in the filing

Exhibits go at the end of the supporting declaration (or motion,
if the motion is self-supporting), **after** the signature block
and the Proof of Service, in this order:

1. **Exhibit cover page / tab** for Exhibit A, then the exhibit
   content
2. **Exhibit cover page / tab** for Exhibit B, then the exhibit
   content
3. ...

Pagination continues sequentially through the exhibits — do not
restart the page counter. The CRC 2.110 footer (document title +
case number + page number) runs on every page including exhibit pages.

## Lettering convention

California practice uses **lettered exhibits** (Exhibit A,
Exhibit B, Exhibit C, etc.) — this contrasts with Oregon's
numbered convention (Exhibit 1, 2, 3) and is consistent with
Washington state practice.

For very large filings with more than 26 exhibits, use double
letters: AA, BB, CC, or A-1, A-2, A-3 for sub-exhibits to a
primary exhibit.

## CRC 3.1110(f) — Exhibit attachment rule

California Rules of Court, rule 3.1110(f) requires that each
exhibit attached to a declaration or motion:

1. Be **identified by an exhibit tab** — a physical tab
   protruding from the right edge of the exhibit pages, labeled
   with the exhibit letter
2. Follow the **declaration or other document** it supports
3. Be preceded by a **cover page** (optional but strongly
   recommended) that identifies the exhibit

For **e-filed PDF documents**, physical tabs are not possible.
The functional equivalent is:
- A **PDF bookmark** for each exhibit (labeled "Exhibit A —
  [description]")
- An **exhibit cover page** within the PDF before each exhibit

Most California courts accept PDF exhibits with bookmarks in
lieu of physical tabs for eFiled documents. For **courtesy
copies** delivered to chambers, physical tabs are required.

## Exhibit cover page

A single page introducing each exhibit:

```
                        EXHIBIT A
                   ─────────────────
             Cardholder Agreement
          Bank of America, August 2018
```

Format:
- "EXHIBIT A" centered and bold, 24 pt (or 16 pt), at vertical
  center of the cover page (or approximately 3 inches from top)
- A short descriptive caption in italic underneath the heading
- One centered horizontal rule between the heading and the
  caption (optional but common)
- The actual exhibit content begins on the **next page** after
  the cover page

## Referencing exhibits in the body

In the body of the declaration or motion, cite exhibits by letter
and page where applicable:

- "A true and correct copy of the Cardholder Agreement is
  attached hereto as **Exhibit A**."
- "See **Exhibits A through D** for the chain of title."
- "The validation notice (**Exhibit C**, at p. 2) reflects a
  balance of $7,432.18."

Bold the exhibit letter reference the first time it appears;
thereafter a plain reference is fine.

## Declaration sentence for authenticating exhibits

Standard California authenticating language:

> "Attached hereto as Exhibit [A] is a true and correct copy
> of [description of document], which I obtained / received /
> reviewed on [date], and which [brief basis for authentication —
> e.g., 'is a printout from the account portal to which I have
> access']."

For business records, add: "This document was made in the
regular course of business, at or near the time of the act or
event it records, by a person with knowledge."

Authentication of exhibits is required to make the exhibit
admissible; the declaration paragraph authenticating each
exhibit is the mechanism.

## Confidential exhibits

If an exhibit contains information subject to CRC 2.550-2.551
(sealing records) or protected personal information (SSNs,
minor's names), consider:

1. **Redact** the protected information in the filed version and
   note "SSN REDACTED" or "MINOR'S INITIALS" in place of the
   information
2. For full unredacted exhibit: file a **Motion to Seal** under
   CRC 2.550-2.551 and lodge the unredacted exhibit under seal

California law on sealing (CRC 2.550) requires a showing that:
(a) there is an overriding interest supporting sealing;
(b) a substantial probability that the interest will be
prejudiced absent sealing;
(c) the order is narrowly tailored; and
(d) no less restrictive means exist to protect the interest.

## Cumulative exhibit lettering across multiple declarations

When supplemental declarations are filed, **continue** the
exhibit lettering rather than restarting:

- First declaration: Exhibits A-F
- Supplemental declaration: Exhibits G-J
- Second supplemental: Exhibit K

This convention is not mandatory under the CRC but is the
dominant California practice and makes record citations
unambiguous at hearing.

## Physical tab preparation (for courtesy copies)

For paper courtesy copies delivered to a judge's chambers
or to opposing counsel:

1. Use Avery-style exhibit tabs (protruding from the right edge)
   labeled "A", "B", "C" etc. Available at office supply stores
2. Insert the tab at the first page of each exhibit (the cover
   page if using cover pages, or the first page of content if
   not)
3. The tab should protrude beyond the right edge of the paper
   by at least 0.5 inches for easy retrieval
4. Bind the courtesy copy with a binder clip or place in a
   manila folder with an index — do NOT staple

Some judges' standing orders specify how courtesy copies should
be bound and tabbed. Check the assigned department's standing
orders before preparing courtesy copies.

## PDF bookmarking for eFiled exhibits

For PDF filing, use a PDF editor to add bookmarks named:
- "Exhibit A — Cardholder Agreement"
- "Exhibit B — Bill of Sale"
- etc.

In Adobe Acrobat:
- View → Navigation Panels → Bookmarks
- Right-click → "Add Bookmark" at the first page of each exhibit

The bookmarks appear in the Acrobat navigation panel, allowing
the clerk and judge to jump directly to each exhibit. Many
California eFiling portals also allow you to flag the start of
each exhibit in the document metadata at the time of upload.

## docx-js exhibit page insertion

```javascript
import { AlignmentType, ImageRun, Paragraph, TextRun,
         PageBreak } from "docx";
import fs from "fs";

// Cover page for each exhibit
function exhibitCover(letter, description) {
  return new Paragraph({
    pageBreakBefore: true,
    alignment: AlignmentType.CENTER,
    spacing: { before: 4320 },  // ~3" of leading space
    children: [
      new TextRun({
        text: `EXHIBIT ${letter}`,
        bold: true,
        size: 48,              // 24 pt
        font: "Times New Roman",
      }),
      new TextRun({ break: 2 }),
      new TextRun({
        text: description,
        italics: true,
        size: 24,
        font: "Times New Roman",
      }),
    ],
  });
}

// Insert a page-break before each exhibit image
function exhibitImage(imagePath) {
  return new Paragraph({
    pageBreakBefore: true,
    alignment: AlignmentType.CENTER,
    children: [
      new ImageRun({
        data: fs.readFileSync(imagePath),
        transformation: { width: 600, height: 800 },
      }),
    ],
  });
}

// Usage:
const exhibits = [
  exhibitCover("A", "Cardholder Agreement, Bank of America, August 2018"),
  exhibitImage("./exhibits/exhibit-a.png"),
  exhibitCover("B", "Bill of Sale, Velocity Investments to LVNV, March 14, 2024"),
  exhibitImage("./exhibits/exhibit-b.png"),
];
```

For multi-page exhibits, embed each page as a separate image
or merge the PDFs after `.docx` → PDF conversion using
`pdf-lib` or similar. Most California practitioners file
separate PDF exhibits in the eFiling portal where the court
system allows individual exhibit uploads — this avoids the
PDF-size-limit problem and lets the clerk bookmark each exhibit
separately.
