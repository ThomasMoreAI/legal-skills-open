# Dispute Log Template

Use this when the user wants a paste-ready review sheet for Legal Tracker, CounselLink, Brightflag, email, or an internal legal-ops tracker.

## CSV Header Template
```csv
invoice_id,line_id,matter_id,matter_name,timekeeper_name,timekeeper_title,issue_label,issue_summary,rule_or_term_reference,evidence_reference,billed_value,challenged_value,confidence,recommended_action,status,notes
```

## Markdown Table Template
| Invoice ID | Line ID | Matter | Timekeeper | Issue Label | Issue Summary | Rule or Term Reference | Evidence Reference | Billed Value | Challenged Value | Confidence | Recommended Action | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
| INV-001 | 1005 | Employment Matter A | J. Doe | `vague-narrative` | Narrative does not state task, issue, or work product. | OCG narrative specificity section | Invoice page 3, line 1005 | 1240.00 | 620.00 | Moderate | Request clarification or partial write-off. | Open |

## Recommended Status Values
- `open`
- `needs-clarification`
- `challenged`
- `resolved`
- `approved-with-note`

## Use Rules
- Prefer stable issue labels from [issue-taxonomy.md](issue-taxonomy.md).
- Keep `issue_summary` short enough to paste into billing-system notes.
- Use `challenged_value` for the amount actually in dispute, not the full invoice unless justified.
