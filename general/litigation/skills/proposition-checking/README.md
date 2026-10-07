# proposition-checking

Checks whether a legal or factual proposition is actually supported by the source cited for it.

This complements citation verification. A case can exist and still be cited for the wrong point.

## Inputs

- Legal draft with citations or record references.
- Source materials, such as judgments, statutes, exhibits, transcripts, pleadings, or correspondence.

## Outputs

- Proposition-by-proposition support table.
- Inaccurate quotation flags.
- Unsupported or overstated propositions.
- Argument dependency summary.

## Example Prompt

```text
For each paragraph of this draft, extract the proposition being asserted, identify the cited support, and classify whether the source supports, partially supports, contradicts, or does not verify it.
```

## Testing

Test scenarios:

- Real case cited for wrong doctrine.
- Correct authority with overstated holding.
- Direct quote with changed wording.
- Factual assertion contradicted by supplied exhibit.
- Source unavailable, requiring `unverified` rather than invented analysis.

Expected behavior: the skill separates "not found", "not checked", "exists but misused", and "actually unsupported".

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Needs the underlying source text for reliable checking.
- Does not replace jurisdiction-specific legal research.
- Does not predict outcome or decide admissibility unless the user supplies the governing standard.
