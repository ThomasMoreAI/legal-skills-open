# uk-court-of-appeal-judicial-preference-check

Checks a draft appellate document against source-backed judicial preference signals from public England and Wales Court of Appeal decisions.

The skill is designed for Court of Appeal skeletons, grounds, respondent's notices, written submissions, and judgment-style memos. It helps identify whether a draft is too factual, too doctrinal, too long, too authority-heavy, too aggressive, too commercial, too black-letter, or otherwise misaligned with public Court of Appeal writing patterns.

## Inputs

- Draft skeleton, grounds, respondent's notice, memo, or submission.
- Appeal context and issues.
- Known or possible panel, if available.
- Public Court of Appeal decisions retrieved from Find Case Law, BAILII, court pages, or supplied by the user.

## Outputs

- Public-source decision corpus.
- Preference findings with excerpts and paragraph references.
- Draft strengths and risks.
- Suggested revision directions.
- Research limits and uncertainty.

## Example Prompt

```text
Review this draft Court of Appeal skeleton against public CoA decisions in comparable commercial cases. If the panel is known, look for multiple public decisions by those judges before making any judge-specific preference observations. Cite every finding.
```

## Testing

Test scenarios:

- Known panel with several public decisions available.
- Unknown panel requiring court-wide or case-type analysis only.
- Single relevant decision by a named judge, requiring `single-source-lead`.
- Draft with long factual narrative before identifying appealable error.
- Draft relying on broad authority survey where comparator judgments are statute-first or issue-first.

Expected behavior: the skill produces source-backed preference signals and preserves uncertainty. It does not predict the appeal outcome or claim to know private judicial preferences.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Judgments are not skeleton arguments; the comparison is indirect.
- Public decisions may not reveal stable judge-specific patterns.
- Current authorities and propositions should be checked separately.
