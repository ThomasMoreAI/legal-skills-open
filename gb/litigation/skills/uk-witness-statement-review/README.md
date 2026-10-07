# uk-witness-statement-review

Reviews England and Wales civil witness statements for support, consistency, CPR/PD risks, and drafting issues.

## Inputs

- Draft witness statement.
- Pleadings, chronology, exhibits, disclosure, correspondence, or prior statements.
- Any court order or directions.

## Outputs

- Paragraph-by-paragraph issue table.
- Unsupported assertion list.
- Document conflict list.
- Argument/hearsay/speculation flags.
- Exhibit and statement-of-truth checklist.
- Questions for the witness or solicitor.

## Example Prompt

```text
Review this witness statement for England and Wales proceedings. Check every factual paragraph against the exhibits and chronology, flag argument or speculation, and list CPR/PD issues that need verification.
```

## Testing

Test scenarios:

- Paragraph with no source support.
- Date contradicted by an email.
- Argument presented as evidence.
- Hearsay with unclear source.
- Missing exhibit reference or statement of truth issue.

Expected behavior: the skill flags issues for lawyer/witness review and does not certify the evidence as true.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Does not replace witness confirmation or solicitor/counsel sign-off.
- Current CPR/PD and court-order requirements must be verified where relied on.
- Does not make final admissibility rulings.
