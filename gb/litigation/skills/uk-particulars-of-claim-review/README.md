# uk-particulars-of-claim-review

Reviews draft Particulars of Claim for England and Wales civil proceedings.

## Inputs

- Draft Particulars of Claim.
- Cause-of-action notes or counsel advice.
- Key documents and chronology.
- Limitation assumptions and remedies sought.

## Outputs

- Cause-of-action element maps.
- Missing material fact list.
- Limitation, party, remedy, and source-support flags.
- CPR/PD16 verification checklist.
- Questions for solicitor, counsel, or client.

## Example Prompt

```text
Review these draft Particulars of Claim. For each cause of action, map the pleaded facts to the elements, identify gaps, and flag limitation, party, remedy, and CPR/PD16 issues.
```

## Testing

Test scenarios:

- Contract claim missing a pleaded term or breach.
- Misrepresentation claim missing reliance or loss.
- Claim with limitation date unclear.
- Serious allegation without source support.
- Remedy requested but not tied to pleaded facts.

Expected behavior: the skill surfaces pleading gaps and verification needs without certifying merits.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Current CPR/PD16, court orders, and pre-action protocols must be checked.
- Cause-of-action elements need lawyer confirmation where law is not supplied.
- Does not replace counsel's pleading review.
