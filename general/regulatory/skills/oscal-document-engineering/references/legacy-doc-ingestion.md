# Legacy Document Ingestion

## Goal

Extract content from old SSP, PDF, DOCX, or Markdown documents into a normalized form.
Map that content to OSCAL without loss of source traceability.

## Process

1. Keep the original input file unchanged.
2. Record file name, hash, date received, and user-provided context.
3. Extract text to Markdown.
4. Keep page numbers for PDFs and heading hierarchy for DOCX when possible.
5. Make source IDs for each section or paragraph that can map to OSCAL.
6. Fill `source-traceability-map.csv` as you make mappings.

## Dependency preferences

- DOCX: `pandoc`, then Python libraries such as `python-docx`.
- PDF: `pdftotext`, then PyMuPDF.
- Markdown and text: copy and normalize line endings.

## Quality checks

- Compare extracted heading count to the original document outline when available.
- Spot-check tables, control IDs, diagrams, and footnotes.
- Treat OCR or PDF extraction errors as `needs_review`.
- Never discard source sections only because they do not map cleanly.
