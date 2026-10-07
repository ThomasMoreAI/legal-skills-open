# collating-reviewer-feedback

Compiles Word comments, tracked changes, and external reviewer notes from multiple versions of the same draft into one lawyer-controlled resolution checklist.

This is not an auto-merger. It is designed for litigation and legal drafting workflows where a malformed merged document or silently accepted change is unacceptable.

## Inputs

- Master DOCX draft.
- One or more reviewer DOCX versions.
- Optional notes from email, chat, calls, or conferences.

## Outputs

- Grouped resolution checklist.
- Conflict list.
- Uncertain-location list.
- Optional CSV or JSON checklist for audit or re-import.

## Example Prompt

```text
Compile these reviewer versions against master.docx. Show every comment and track change in document order, group likely conflicts, and leave every item open for lawyer resolution.
```

## Testing

Tested against a reviewer-markup workflow design:

- Multiple reviewer versions of one draft.
- Comments with anchor text.
- Insertions, deletions, and whole-paragraph changes.
- Manual external comments.
- Deliberately conflicting reviewer suggestions.

Expected behavior: the skill produces a checklist and conflict report, not a merged document.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Matching is approximate when drafts diverge.
- Complex tables, text boxes, fields, and nested revisions may need manual checking.
- A lawyer must verify every proposed resolution before editing the master.
