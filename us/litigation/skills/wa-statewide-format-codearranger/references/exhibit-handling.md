# Exhibit Handling

How to list, cover-page, and paginate exhibits inside a declaration or
motion packet.

## Order of elements at the end of a declaration

1. Verification clause (under penalty of perjury)
2. Date and place of execution
3. Signature block
4. **Exhibit List** (new page, centered title)
5. One cover page + image/content per exhibit

All of this is one continuous document with one running page number
sequence. Do not reset pagination for exhibits.

## Exhibit List format

```
                       EXHIBIT LIST

Exhibit A:  [One-line description of exhibit contents. Indent the
            description under a hanging indent so the exhibit label
            stays aligned.]

Exhibit B:  [Description]

Exhibit C:  [Description]

Exhibit D:  [Description]
```

In `docx-js`:

```javascript
new Paragraph({
  pageBreakBefore: true,
  alignment: AlignmentType.CENTER,
  spacing: { line: 276, lineRule: "auto", after: 240 },
  children: [new TextRun({ text: "EXHIBIT LIST", bold: true, font: "Times New Roman", size: 24 })],
});

// Each exhibit entry
new Paragraph({
  spacing: { line: 360, lineRule: "auto", after: 200 },
  indent: { left: 1080, hanging: 1080 },
  tabStops: [{ type: TabStopType.LEFT, position: 1080 }],
  children: [
    new TextRun({ text: `Exhibit ${letter}:\t`, bold: true }),
    new TextRun(description),
  ],
});
```

## Exhibit cover page

Each exhibit begins on a new page. Layout:

```
                        EXHIBIT A
      [italic one-line caption describing the exhibit]

                     [image or content]
```

In `docx-js`:

```javascript
new Paragraph({
  pageBreakBefore: true,
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 240, line: 360, lineRule: "auto" },
  children: [new TextRun({ text: "EXHIBIT A", bold: true, size: 36, font: "Times New Roman" })],
});

new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 300 },
  children: [new TextRun({ text: caption, italics: true, size: 22, font: "Times New Roman" })],
});

new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new ImageRun({
    type: "png",
    data: fs.readFileSync(imgPath),
    transformation: { width: 280, height: 607 },   // scale preserving aspect ratio
    altText: { title: `Exhibit ${letter}`, description: caption, name: `Exhibit_${letter}` },
  })],
});
```

## Referencing exhibits in the body

Always refer by exhibit letter and (where applicable) page:

- "True and correct screenshots are attached as **Exhibits A through D**."
- "See **Exhibit B at 2**" (for multi-page exhibits)
- "The April 10 email is attached as **Exhibit D**."

Bold the exhibit reference on first mention in each paragraph so the
judge can find it quickly.

## Color in exhibits

GR 14 prohibits colored markings but carves out attachments "unless the
nature of the attachment makes compliance impractical." Native phone
screenshots, color photos of physical evidence, and color medical charts
generally fit this exception. Convert to grayscale only when the color
is not evidentiarily meaningful.

If you do convert to grayscale, note in the declaration body:
"A grayscale reproduction of the screenshot is attached as Exhibit A;
the original is available in color for inspection."
