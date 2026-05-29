# Metrics Catalog
Use only metrics supported by the supplied data. Do not fabricate missing denominators.

## 1. Spend Metrics
- Billed fees: sum of attorney and professional fee lines before credits.
- Billed expenses: sum of expense and disbursement lines before tax.
- Taxes or VAT: sum of tax lines; keep separate from fees and expenses.
- Total billed value: fees plus expenses plus taxes before credits.
- Net billed value: total billed value minus invoice-level credits or write-offs if shown.
- Reviewed population value: value represented by the invoices or lines actually reviewed.

## 2. Rate Metrics
- Standard rate: the law firm or timekeeper's undiscounted reference rate, if provided.
- Approved rate: the company-authorized rate under the OCG, engagement terms, or rate file.
- Billed rate: line-rate shown on the invoice or export.
- Net effective rate: net fees divided by hours after discounts or line-item write-offs.
- Approved-rate variance: billed rate minus approved rate.
- Approved-rate variance percent: `(billed rate - approved rate) / approved rate`.
- Year-over-year rate change: compare same timekeeper or same role and office where the comparator is valid.

## 3. Discount Metrics
- Contracted discount percent: discount promised in the engagement terms or rate schedule.
- Realized discount percent: `(standard rate - net effective rate) / standard rate` when standard rate is known.
- Discount shortfall: contracted discount percent minus realized discount percent.
- Invoice-level write-off value: reductions already reflected in the invoice or export.

## 4. Staffing Metrics
- Partner share of hours: partner hours divided by total fee hours.
- Partner share of fees: partner fees divided by total fee value.
- Timekeeper count: unique billed professionals on the matter or invoice.
- Staffing concentration: share of hours or fees attributable to the top 1, 3, or 5 timekeepers.
- Multi-attendee event count: count of meetings, calls, hearings, or depositions with multiple billers when identifiable.
- Review-layer count: number of billing roles touching the same workstream when identifiable.

## 5. Compliance and Hygiene Metrics
- OCG compliance rate: compliant lines divided by reviewable lines.
- Hard-rule breach count and value: lines tied to clear prohibitions or exceeded approvals.
- Clarification-needed count and value: lines that may be noncompliant but need more facts.
- Block-billing rate: block-billed lines divided by reviewable fee lines.
- Narrative adequacy rate: lines with sufficiently specific narratives divided by reviewable lines.
- Duplicate-attendance rate: events with arguably excessive attendance divided by reviewable multi-attendee events.

## 6. Budget and Forecast Metrics
- Spend-to-budget: actual spend divided by budget for the same scope.
- Budget variance: actual spend minus budget.
- Burn rate: spend per month, quarter, phase, or other approved period.
- Forecast-to-period-end: current spend plus projected remaining spend for the same scope.
- Forecast variance: forecast-to-period-end minus approved budget.

## 7. Benchmark Metrics
- Comparator median or mean fee value: use only with a stated comparator population.
- Comparator range: show a low to high band only when the sample is coherent enough to support it.
- Variance to comparator: current metric minus comparator metric.
- Variance percent to comparator: `(current metric - comparator metric) / comparator metric`.

Always identify the comparator basis, sample size if known, and the reason the comparator is relevant.

## 8. Value Framing
- Identified value at review: total billed value associated with flagged issues.
- Potential savings: the portion of identified value that might be reduced if the challenge is sustained.
- Realized savings: amounts actually written off, adjusted, credited, or paid lower.

Never present identified value or potential savings as realized savings.
