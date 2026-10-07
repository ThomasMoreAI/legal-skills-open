# corporate-registry-investigation

Investigates UK companies using Companies House registry records.

## Inputs

- Company name or number.
- Optional purpose: diligence, litigation, onboarding, enforcement, or conflicts.

## Outputs

- Company snapshot.
- Officer and PSC tables.
- Charges summary.
- Filing timeline.
- Risk signals and follow-up searches.
- Clear separation between registry facts and inferences.

## Example Prompt

```text
Investigate ACME LIMITED on Companies House. Give me the company snapshot, officers, PSCs, charges, filing history, red flags, and what needs verification from filings or other sources.
```

## Testing

Test scenarios:

- Exact company-number lookup.
- Ambiguous company-name search.
- Company with outstanding charges.
- Company with officer churn.
- Company with missing or unusual PSC statements.

Expected behavior: registry facts are cited as registry evidence, while ownership or risk conclusions are marked as inferences or follow-up items.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Public registry data is not conclusive beneficial ownership evidence.
- Filing metadata can miss important text inside accounts or charges.
- Non-UK entities require different registry sources.
