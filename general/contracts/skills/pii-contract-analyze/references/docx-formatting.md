# Formatting Reference — Legal Memo (.docx)

**Read the `docx` SKILL.md first** for setup, validation, and critical rules for docx-js.

**CRITICAL: Every TextRun MUST have explicit `font: "Arial"` and `size`.** Do NOT rely on defaults.

### Setup

```javascript
const { Document, Packer, Paragraph, TextRun, AlignmentType,
        Table, TableRow, TableCell, WidthType, ShadingType } = require('docx');
const fs = require('fs');

const BODY_RUN = { font: "Arial", size: 24 };             // 12pt
const BOLD_RUN = { font: "Arial", size: 24, bold: true };  // 12pt bold
const QUOTE_RUN = { font: "Arial", size: 22, italics: true }; // 11pt italic
const STD_SPACING = { before: 0, after: 120, line: 240, lineRule: "auto" };
```

### Paragraph types

| Type | Bold? | Italic? | Size | First-line indent | Left indent | Spacing |
|------|-------|---------|------|-------------------|-------------|---------|
| Title | YES | no | 24 | 0 | 0 | STD_SPACING |
| Body | no | no | 24 | 630 | 0 | STD_SPACING |
| Section heading | YES | no | 24 | 0 | 0 | STD_SPACING |
| Blockquote | no | YES | 22 | 0 | 900 | STD_SPACING |
| Risk line | no | no | 24 | 630 | 0 | STD_SPACING |

**Blockquote**: `indent: { left: 900, firstLine: 0 }` — shifts ENTIRE paragraph right, not just first line.

### Document structure (MEMO)

1. Title (bold)
2. Context paragraphs (1–2)
3. Definitions section
4. Analysis sections (heading → body → blockquote → risk assessment)
5. Conclusion (action items)
6. Risk summary table (optional)

### Validation

```bash
python scripts/office/validate.py output.docx
```
