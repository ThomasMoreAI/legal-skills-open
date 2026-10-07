# building-chronologies

Builds sourced legal chronologies from documents, correspondence, pleadings, disclosure, and witness materials.

## Inputs

- Folder or bundle of legal documents.
- Optional issue list, witness name, or date range.
- Optional existing chronology to update.

## Outputs

- Working chronology.
- Disputed-events list.
- Source-gap list.
- Optional witness-specific, issue-specific, or statement-of-facts variant.

## Example Prompt

```text
Build a chronology from these documents. Include date, actor, event, source, quote, confidence, issue tags, and gaps. Do not infer events that are not sourced.
```

## Testing

Test scenarios:

- Email thread with several dated events.
- Later witness statement contradicting an earlier email.
- Event referenced in a pleading but missing from documents.
- Partial date, such as "March 2024".
- Duplicate event described in multiple documents.

Expected behavior: duplicate events are merged with source trail preserved, conflicts are flagged, and source gaps are listed.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- OCR quality affects extraction.
- The chronology is not a substitute for reviewing key documents.
- Procedural deadline calculation needs a separate rules analysis.
