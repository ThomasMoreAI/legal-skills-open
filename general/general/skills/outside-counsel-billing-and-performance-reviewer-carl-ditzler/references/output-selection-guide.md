# Output Selection Guide

Use this guide when the user asks for the best format or specifically requests CSV, Excel, PDF, or PowerPoint-ready output.

## Best-Format Rules
- Use `csv` for dispute logs, issue logs, and uploads into internal trackers or e-billing systems.
- Use `xlsx` for finance-friendly review workbooks, sortable issue logs, or tables users will edit.
- Use markdown `.md` for narrative reports, audit memoranda, and executive summaries.
- Use PDF-friendly HTML or carefully constrained PDF-ready markdown when the user wants a fixed narrative document that will be rendered to PDF `.pdf`.
- Use PowerPoint-ready outline content when the user wants slides but the environment does not support native `.pptx` generation.

## Practical Selection by Deliverable
- Detailed issue log: CSV or XLSX
- Detailed audit report: markdown plus PDF-friendly HTML
- Executive summary: markdown plus PDF-friendly HTML
- QBR or MBR pack: markdown plus PDF and PowerPoint-ready outline
- Cross-firm comparison tables: XLSX
- Negotiation points: markdown or CSV depending whether they want prose or a tracker

## Scripts
- `scripts/export_issue_log.py`: CSV, markdown, or XLSX issue-log outputs
- `scripts/build_exec_pack.py`: markdown report, PDF-friendly HTML report, or PowerPoint-ready outline

## Cautions
- Do not promise a true PDF or `.pptx` file unless the environment supports that conversion.
- If the user only needs something usable in Excel, CSV works.
- For PDF, Word, and PowerPoint, must apply [visual-output-rules.md](visual-output-rules.md) to avoid text overlap, unwrapped labels, and unusable wide tables.
