---
name: nz-regulatory-analysis-thecolab-ai
title: NZ regulatory analysis
description: Use when finding or inspecting current official New Zealand Regulatory Analysis Summaries (RAS), Regulatory Impact Statements or Assessments (RIS/RIA), supplementary or cost-recovery analyses, quality assessments, Cabinet documents, and linked PDFs published by the Ministry for Regulation or Ministry for the Environment.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/nz-regulatory-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: administrative
language: en
sources:
- title: Source Notes
  path: references/source-notes.md
---

# NZ regulatory analysis

## Goal

Discover current official regulatory-analysis publication pages and inspect their linked PDFs. The skill reads the Ministry for Regulation's RAS index and the Ministry for the Environment's Cabinet-paper/RIS index. It classifies records without downloading or interpreting PDF contents.

## Use this when

- Finding current official RAS, RIS, RIA, supplementary analysis reports, or cost recovery impact statements.
- Locating independent, departmental, agency, or otherwise-labelled quality assessments.
- Finding the Cabinet papers and minutes linked from an environmental regulatory package.
- Producing source URLs and retrieval timestamps before a policy comparison.

## Do not use this for

- Recovering deleted, superseded, or archived publications.
- Claiming that a search result is the complete government-wide corpus.
- Treating a document's presence as proof that its analysis or quality assurance is adequate.
- Summarising PDF contents: this CLI returns links and labels but does not fetch PDFs.
- Circumventing CAPTCHA, access challenges, robots controls, or request blocks.

## Preferred workflow

1. Run `search` with a narrow policy phrase. Use `--source` when the publisher is known.
2. Select the official publication-page URL from the results.
3. Run `inspect URL --json` to list linked official PDFs and their distinct document types.
4. Open and read the relevant returned PDF separately before making content claims.
5. Cite the exact page/PDF URL and `source.retrieved_at`; explain that listings can change.

## CLI

Run from the repository root:

```bash
python3 skills/nz-regulatory-analysis/scripts/cli.py <command> [flags]
```

Commands:

- `search QUERY [--source all|regulation|environment] [--limit 1-25] [--json]` searches one or both current indexes. `QUERY` is positional.
- `inspect URL [--json]` fetches one supported official HTML publication page and lists same-site linked PDFs. `URL` is positional.

Examples:

```bash
python3 skills/nz-regulatory-analysis/scripts/cli.py search "climate disclosures" --json
python3 skills/nz-regulatory-analysis/scripts/cli.py search freshwater --source environment --limit 5
python3 skills/nz-regulatory-analysis/scripts/cli.py inspect "https://www.regulation.govt.nz/publications-and-resources/regulatory-analysis-summaries/EXAMPLE/" --json
```

## Result contract

`--json` emits the repository result envelope (`schema_version: "1"`). Successful live results include `source.url`, `source.retrieved_at`, `query`, `data`, `warnings`, and `blocked: false`.

- Search records retain `title`, official `url`, displayed publication date, publisher, and `document_type`; source-specific author/tags are retained when shown. Regulation searches follow all result pages within the safety bound so `source_totals.regulation` is not a page-one count. Multi-document environment packages use `publication_package` and expose every labelled type in `document_types` rather than collapsing Cabinet and regulatory documents into one type.
- Inspect results retain the page title/type/update value plus deduplicated `documents` with official PDF URLs and separate document types.
- A genuine no-match search is `ok: true` with `results: []`.
- HTTP/access challenges are exit 4 with `blocked: true`; upstream outages are exit 5; changed/malformed page structures are exit 6. They never become empty success.

Document types include `regulatory_analysis_summary`, `regulatory_impact_statement`, `regulatory_impact_assessment`, `supplementary_analysis_report`, `cost_recovery_impact_statement`, quality-assessment variants, Cabinet paper/minute, briefing, and conservative fallback types.

## Resources

- `scripts/cli.py` — bounded stdlib HTTP client and parser.
- `scripts/test_contract.py` — deterministic repository contract runner.
- `tests/test_parser.py` and `tests/fixtures/` — scrubbed minimal parser and adversarial cases.
- `scripts/smoke_test.py` — fixture checks plus bounded normal/empty/blocked-aware live contracts.
- `references/source-notes.md` — source surfaces, limits, and parser assumptions.

## Safety and limits

- Read-only GET requests, no authentication, browser automation, cache, proxy configuration, or PDF download.
- Regulation searches follow at most 10 index pages (up to 120 results with the current 12-result page size); a broader result set fails explicitly and asks for a narrower query rather than reporting a partial total. Environment search makes one index request. Inspect makes one request. Each request has a 10-second timeout and 2 MB HTML cap.
- Redirects remain inside the two declared official hosts and supported publication paths.
- Labels drive type classification; inspect the document itself before relying on that classification in consequential work.
