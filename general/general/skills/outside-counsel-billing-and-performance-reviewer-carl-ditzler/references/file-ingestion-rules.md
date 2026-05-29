# File Ingestion Rules

Use this reference when the user uploads mixed file types or asks the skill to work from CSV, Excel, LEDES, PDF, DOCX, or JSON.

## Accepted Inputs
- `csv`, `tsv`
- `xlsx`
- `json`
- LEDES-like text exports
- PDF invoices and OCGs
- DOCX or text policy files
- zipped invoice or export bundles if the environment can unpack them

## Source Priority
1. user-supplied OCGs, approved-rate files, budgets, AFAs, and negotiated exceptions
2. structured billing exports such as CSV, XLSX, JSON, or LEDES
3. invoice PDFs and narrative-only materials
4. public directional material only if authorized

## Normalization Rules
- Prefer structured exports over manual extraction from PDFs when both exist.
- Normalize fee, expense, tax, and credit lines separately.
- Preserve source-file name, row number, invoice ID, and line ID where possible.
- Keep original headers available if a mapping decision is uncertain.
- If multiple source files overlap, preserve a `source_file` or equivalent reference for reconciliation.

## Canonical Data Expectations
Try to normalize into the billing-fact fields in [PLAYBOOK-SCHEMA.md](../PLAYBOOK-SCHEMA.md).

## Practical Use
- If the user provides CSV, TSV, XLSX, JSON, or LEDES-like text, prefer `scripts/normalize_billing_data.py`.
- If the user provides only PDFs or scans, say that extraction quality may materially limit confidence.
- If a workbook contains multiple sheets, ask which sheet is authoritative unless it is obvious.

## Cautions
- Do not assume workbook tabs are comparable unless headers and scope align.
- Do not merge different currencies without explicit treatment.
- Do not overwrite approved-rate files with invoice-rate data.
