# OOXML Tracked Changes (REDLINE Mode — Step 6)

Tracked changes in .docx are XML elements `w:ins` (insertion) and `w:del` (deletion) inside paragraph runs. They require `w:rPr` (run properties) to preserve formatting and `w:author`/`w:date` attributes.

**Critical implementation details:**
- Work on the **anonymized .docx** (`docx_output_path` from Step 3) — it preserves original formatting with PII replaced by placeholders
- Use `python-docx` to open the document + `lxml` to manipulate XML directly
- For each change: find the target paragraph → locate the text run → split at the change point → wrap deleted text in `w:del > w:r > w:delText` → insert new text in `w:ins > w:r > w:t`
- Preserve all `w:rPr` (font, size, bold, etc.) from the original run
- Set `w:author="Claude"` and `w:date` to current ISO datetime
- Save with `doc.save()`

**Example XML structure for a tracked change:**
```xml
<w:p>
  <w:r><w:rPr>...</w:rPr><w:t>unchanged text before </w:t></w:r>
  <w:del w:author="Claude" w:date="2026-03-27T12:00:00Z">
    <w:r><w:rPr>...</w:rPr><w:delText>old text</w:delText></w:r>
  </w:del>
  <w:ins w:author="Claude" w:date="2026-03-27T12:00:00Z">
    <w:r><w:rPr>...</w:rPr><w:t>new text</w:t></w:r>
  </w:ins>
  <w:r><w:rPr>...</w:rPr><w:t> unchanged text after</w:t></w:r>
</w:p>
```

**Important**: All changes use placeholder text (`<ORG_1>`, `<PERSON_2>`). After `deanonymize_docx`, the tracked changes will contain real names/entities.
