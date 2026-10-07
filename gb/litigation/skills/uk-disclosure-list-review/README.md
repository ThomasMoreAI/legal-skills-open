# uk-disclosure-list-review

Reviews England and Wales civil disclosure lists and disclosure exercise outputs for coverage, privilege, inspection, and document gaps.

## Inputs

- Draft disclosure list or review export.
- Pleadings, chronology, witness statements, or issue list.
- Disclosure order or directions where available.
- Search/custodian record if available.

## Outputs

- Coverage summary.
- Missing custodian/source flags.
- Documents referenced elsewhere but absent.
- Privilege, redaction, and inspection issue list.
- Potentially adverse document triage.
- Questions for supervising solicitor.

## Example Prompt

```text
Review this disclosure list against the pleadings and chronology. Flag missing documents, weak privilege descriptions, inspection objections, and potentially adverse documents. Keep close privilege calls for lawyer review.
```

## Testing

Test scenarios:

- Pleading references a document absent from the list.
- Custodian appears in correspondence but not in disclosure sources.
- Privilege claimed only because a lawyer is copied.
- Attachment not separately reviewed.
- Potentially adverse email described in neutral terms.

Expected behavior: the skill produces a QC report and keeps privilege/adverse labels as review flags.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Does not certify disclosure compliance.
- Current rules and court orders must be checked.
- Requires the search record to assess actual search adequacy.
- Does not make final privilege determinations.
