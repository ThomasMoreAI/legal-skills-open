# OCG / Billing Rule Schema
Normalize OCGs and billing rules into this schema.

## Rule Schema
- Rule ID
- Source file and page or section
- Effective date or period
- Rule category
- Rule summary
- Applies to
- Trigger condition
- Hard prohibition / soft guideline / approval required
- Threshold amount, time, or count
- Relevant role / title
- Rate type involved
- Expense or surcharge class
- Exception logic
- Evidence required
- Severity default
- Suggested remediation

## Standard Rule Categories
- Rates
- Discounts
- AFAs / caps / collars / blended rates
- Staffing approvals
- Travel
- Meals / entertainment
- Research
- Internal conferencing
- Administrative / clerical work
- Training / onboarding
- Narrative specificity
- Block billing
- Duplicate attendance
- Billing increments
- Expenses / overhead
- AI / technology / database charges
- Invoice preparation time
- Budget compliance
- Matter coding / task coding completeness
- Invoice timing / submission cadence

## Interpretation Rules
- Preserve the original rule language where possible.
- Distinguish hard prohibitions from approval-required items.
- Track any negotiated exceptions separately.
- Do not over-generalize a firm-specific or matter-specific exception into a general rule.

## Billing Fact Schema
Normalize invoice or LEDES data into these fields when available:
- Invoice ID
- Invoice status
- Invoice date
- Billing period
- Currency
- Matter ID and matter type
- Matter phase or task
- Line ID
- Line type: fee / expense / tax / credit
- Timekeeper name
- Timekeeper title or role
- Timekeeper office
- Timekeeper approval status and effective date
- Hours or units
- Standard rate
- Approved rate
- Billed rate
- Net effective rate if derivable
- Billed amount
- Adjusted amount
- Paid amount if known
- Discount or write-off amount
- UTBMS or LEDES codes
- Narrative text
- Budget phase or workstream

## Comparison Rules
- Compare like to like by matter type, phase, jurisdiction, and fee arrangement whenever possible.
- Do not compare hourly-rate matters to fixed-fee matters without stating the limitation.
- Separate taxes, VAT, FX, and pass-through vendor costs from attorney-fee comparisons.
