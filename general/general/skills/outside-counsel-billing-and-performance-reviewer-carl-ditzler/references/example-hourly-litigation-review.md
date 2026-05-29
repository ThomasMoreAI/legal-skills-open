# Example: Hourly Litigation Invoice Review

Use this reference when the user wants a quick prompt pattern or output skeleton for a conventional hourly litigation matter.

## Example Prompt
Use $outside-counsel-billing-performance-reviewer to review these hourly litigation invoices for compliance with our OCGs, approved rates, and staffing rules for Q2 2026. Focus on partner overuse, vague narratives, duplicate attendance, research churn, and any charges that should go into a dispute log. Benchmark first against our internal employment-litigation history, then against same-firm prior matters if needed. Produce a concise audit report for Legal Ops and a paste-ready dispute log.

## Output Skeleton
### Disclaimer
- Draft only. Human review required before approval or dispute action.

### Scope
- Review period
- Firms and matters in scope
- Files reviewed

### Data Quality
- Missing fields
- Extraction limitations
- Comparator limitations

### Headline Findings
- Highest-priority issues with confidence labels

### Key Metrics
- billed fees
- billed expenses
- approved-rate variance
- partner share of hours
- block-billing rate
- identified value at review
- potential savings

### Compliance Findings
- rates
- staffing approvals
- narrative quality
- conferencing and attendance
- prohibited or questionable expenses

### Benchmarking Findings
- internal comparator used
- notable variance
- limitations

### Recommended Actions
- approve
- approve with clarification
- challenge specific entries
- request updated staffing plan

### Dispute Log
- include invoice ID, line ID, issue label, evidence summary, challenged value, and next step
