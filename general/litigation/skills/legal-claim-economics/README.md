# legal-claim-economics

Models claim and portfolio economics across damages, costs, funding structures, fee arrangements, recourse, and recovery waterfalls.

## Inputs

- Claim count or portfolio size.
- Damages distribution.
- Liability / quantum probability.
- Cost budget.
- Fee arrangement.
- Funding structure.
- ATE and adverse-cost assumptions.
- Recovery waterfall.

## Outputs

- Base, downside, and upside cases.
- Waterfall distribution.
- Firm and funder economics.
- Client residual recovery.
- Sensitivity analysis.
- Assumption checklist.

## Example Prompt

```text
Build a claim economics model for 1,000 claims with a DBA, ATE, and funder MOIC return. Show expected firm margin, funder cash multiple, client residual, and downside exposure.
```

## Testing

Test scenarios:

- Zero-damages loss case.
- Funder MOIC exceeds proceeds.
- Pari passu waterfall.
- Firm recourse versus non-recourse funding.
- DBA or percentage return flagged under user-supplied cap assumptions.

Expected behavior: the skill exposes assumptions and shortfalls rather than forcing a single commercial answer.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Not legal, tax, accounting, or investment advice.
- Jurisdiction-specific funding rules must be verified.
- Sensitivity output is more useful than a single point estimate.
