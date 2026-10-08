# Exhibit Handling — Oregon

## Where exhibits live in the filing

Exhibits go at the end of the supporting declaration (or motion,
if the motion is self-supporting), **after** the signature block,
in this order:

1. **Exhibit List** (one page)
2. **Cover page for Exhibit 1**, then the exhibit content
3. **Cover page for Exhibit 2**, then the exhibit content
4. ...

Pagination continues sequentially through the exhibits — do not
restart the page counter. UTCR 2.010 requires "Page X of Y" to
reflect the **entire** document including exhibits.

## Numbering convention

Oregon practice uses **numbered** exhibits: Exhibit 1, Exhibit 2,
Exhibit 3, etc. (Washington uses lettered: Exhibit A, B, C.) This
is a stylistic convention rather than a UTCR requirement, but it
is universal in Oregon practice and judges are accustomed to it.

For very large filings — say more than 26 exhibits — many Oregon
practitioners use "Exhibit 1.1", "Exhibit 1.2" sub-numbering rather
than rolling into double-digits, but this is purely conventional.

## Exhibit List

A single page titled "EXHIBIT LIST" centered and bold at the top.
Each entry on a separate line:

```
                        EXHIBIT LIST

Exhibit 1:    [Document title — e.g., "Cardholder Agreement,
              Bank of America, August 2018"]

Exhibit 2:    [Document title — e.g., "Bill of Sale dated
              March 14, 2024, Velocity Investments to LVNV"]

Exhibit 3:    [Document title — e.g., "Validation Notice
              dated April 1, 2024"]
```

Format:

- Title "EXHIBIT LIST" centered, bold, 14 pt (slightly larger than
  body)
- Each entry indented; exhibit number bold; colon and tab; then
  description in normal weight
- Single-spaced, with one blank line between entries
- If the list runs more than one page, repeat "EXHIBIT LIST
  (cont'd)" at the top of the second page

## Cover page per exhibit

A separate page introducing each exhibit:

```
                          EXHIBIT 1
                     ─────────────────
                Cardholder Agreement,
              Bank of America, August 2018
```

Format:

- "EXHIBIT 1" centered, bold, 24 pt at vertical center of the
  page (or roughly 3 inches from top)
- A short caption in italic underneath describing the exhibit
- One horizontal rule between the heading and the caption (3 inch
  centered rule)
- The actual exhibit (PDF page image, transcript text, screenshot
  capture) starts on the **next** page

## Referencing exhibits in the body

In the body of the declaration or motion, cite exhibits by number
and page where applicable:

- "True and correct copy of the Bill of Sale is attached as
  **Exhibit 2** at page 1."
- "See **Exhibits 1 through 4** for the chain of title."
- "The validation notice (**Exhibit 3** at p. 2) recites a balance
  of $7,432.18."

Bold the exhibit reference the first time it appears; thereafter
plain reference is fine.

## Confidential exhibits

If an exhibit contains information that UTCR 2.120 requires to be
redacted (SSN, account number, minor's name), redact in the filed
version. If the unredacted exhibit is needed by the court, file
the unredacted version under seal via a Confidential Information
Form (UTCR 2.130) or a motion to file under seal under UTCR 2.140.

## Cumulative exhibit numbering

When supplemental declarations are filed, **continue** the exhibit
numbering rather than restarting:

- First declaration: Exhibits 1–6
- Second supplemental declaration: Exhibits 7–9
- Third supplemental declaration: Exhibit 10

This way the record citation "Exhibit 8" unambiguously refers to a
single document across the case.

The cumulative numbering convention is not in UTCR — it is a
practice convention — but it is universally accepted and makes the
record dramatically easier to navigate at hearing.

## docx-js exhibit insertion

```javascript
// One page per exhibit cover
const exhibitCover = (num, caption) => new Paragraph({
  pageBreakBefore: true,
  alignment: AlignmentType.CENTER,
  spacing: { before: 4320 },  // ~3" leading
  children: [
    new TextRun({ text: `EXHIBIT ${num}`, bold: true, size: 48 }),
    new TextRun({ break: 2 }),
    new TextRun({ text: caption, italics: true, size: 24 }),
  ],
});

// Embed the exhibit content image on the following page
const exhibitImage = (imagePath) => new Paragraph({
  pageBreakBefore: true,
  alignment: AlignmentType.CENTER,
  children: [
    new ImageRun({
      data: fs.readFileSync(imagePath),
      transformation: { width: 600, height: 800 },
    }),
  ],
});
```

For multi-page exhibits, embed each PDF page as a separate image
or merge the PDFs after `.docx` generation using `pdf-lib` or
similar. Most Oregon practitioners just file separate PDF
exhibits in File and Serve rather than wedging large exhibits into
the main `.docx` — the court system accepts up to 25 MB per
document.
