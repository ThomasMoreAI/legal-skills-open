# uk-citation-verification

Checks UK legal citations against public authority sources such as Find Case Law and BAILII.

## Inputs

- Legal draft containing UK case citations.
- Optional expected court or jurisdiction scope.

## Outputs

- Citation status table.
- Source used for each check.
- Case-name, paragraph, and quotation mismatch flags.
- Unresolved authority list.

## Example Prompt

```text
Verify every UK citation in this draft. Use Find Case Law first, then BAILII. Flag hallucinated cases, mismatched party names, missing paragraphs, and inaccurate quotations.
```

## Testing

Test scenarios:

- Real neutral citation with matching case name.
- Real neutral citation with wrong party name.
- Fabricated neutral citation.
- Valid case with non-existent paragraph reference.
- Quote with a material wording change.

Expected behavior: unresolved or unavailable sources stay marked unresolved; the skill does not invent case summaries.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Subscription-only law reports may need manual review.
- Citation checking is separate from proposition checking.
- Public databases may be incomplete or temporarily unavailable.
