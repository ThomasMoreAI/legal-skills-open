---
name: field-selector-quality-audit
title: 'Field selector quality audit'
description: 'Audit NVCA field-selector quality: check file inventory, metadata schema, field-to-replacement coverage, ambiguous keys, smart quotes, test fixtures, and fill quality. Produces a structured scorecard per field-selector with maturity tier classification. Use when user says "audit field-selector quality," "check field-selector coverage," "field-selector scorecard," or "NVCA field-selector quality."'
author: open-agreements
author_url: https://github.com/open-agreements/open-agreements/tree/main/skills/internal/field-selector-quality-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# field-selector-quality-audit

Audit a single NVCA field-selector's quality and produce a structured scorecard.

## Security model

- This skill operates on **local repository files only** — no network access required.
- Source document downloads (Tier 2 checks) use `ensureSourceDocx()` which fetches from known template source URLs only.
- No credentials or API keys are needed.

## Usage

Run the audit for a specific field-selector:
```
Audit the field-selector: nvca-certificate-of-incorporation
```

Or audit all field-selectors:
```
Audit all NVCA field-selectors and update the quality tracker
```

## Checks

### Tier 1: Structural (no source download needed)

| # | Check | How |
|---|-------|-----|
| S1 | File inventory | Does field-selector have metadata.yaml, replacements.json, clean.json? Optional: computed.json, normalize.json, selections.json |
| S2 | Metadata schema valid | Run existing `validateFieldSelectorMetadata()` from `src/core/metadata.ts` |
| S3 | Field-to-replacement coverage | For each field in metadata, is there a replacement key referencing `{field_name}`? |
| S4 | Ambiguous keys | Flag replacement keys < 8 chars without context qualifier (e.g., `[name]`, `[its]`) |
| S5 | Smart quote coverage | Keys with apostrophes should have smart-quote variants (or patcher normalizes — check patcher has normalizeQuotes) |
| S6 | Source SHA present | `source_sha256` in metadata.yaml |
| S7 | Test fixture exists | `integration-tests/fixtures/{field-selector-id}-*.json` exists |

### Tier 2: Behavioral (requires source download)

| # | Check | How |
|---|-------|-----|
| B1 | Source download + scan | Count placeholder-shaped matches using the exact regex `\[[_A-Z][_A-Z\s]*\]` (underscore-fill or all-capital placeholders) |
| B2 | Replacement coverage ratio | For the re-audited NVCA selectors, covered unique matches / total unique matches from the exact B1 regex, target >80%. The legacy all-brackets population and >=70% threshold remains only for selectors outside that audited set. |
| B3 | Unmatched underscore patterns | `[___+]` patterns in source not in replacements.json |
| B4 | Clean effectiveness | After clean, no footnotes, no "Note to Drafter", no preamble |

### Tier 3: Fill quality (requires fill run)

| # | Check | How |
|---|-------|-----|
| F1 | Default-only fill | Fill with defaults, run verifyOutput, count blank placeholders |
| F2 | Full-values fill | Fill with all fields from test fixture, assert all verify checks pass |
| F3 | Formatting anomaly count | Check 8 from verifier (single-char underlined runs) |
| F4 | Zero-match replacement keys | Keys that existed in replacements.json but matched nothing in the source |

## Output: Quality Scorecard

```json
{
  "field_selector_id": "nvca-voting-agreement",
  "maturity": "beta",
  "scores": { "structural": "6/7", "behavioral": "3/4", "fill": "0/4", "total": "9/15" },
  "checks": [
    { "id": "S1", "name": "File inventory", "passed": true, "details": "metadata.yaml, replacements.json, clean.json present" },
    { "id": "S7", "name": "Test fixture exists", "passed": false, "details": "No fixture matching integration-tests/fixtures/nvca-voting-agreement-*.json" }
  ],
  "field_coverage": { "metadata_fields": 14, "replacement_refs": 10, "uncovered": 4 },
  "recommendations": [
    "Add test fixture for fill testing (S7)",
    "Add replacement keys for 4 uncovered fields (S3)"
  ]
}
```

## Maturity Tiers

- **scaffold**: metadata-only, can't fill
- **beta**: has replacements + clean, score < 11/15 OR no test fixture
- **production**: score >= 11/15 AND has test fixture AND has computed.json (if conditional sections exist in source)

## Workflow

When running the audit:

1. Read `templates/nvca-free-non-redistributable/QUALITY_TRACKER.md` for current state
2. Run Tier 1 checks (always possible)
3. Run Tier 2 checks if source document is available (use `ensureSourceDocx()`)
4. Run Tier 3 checks if a test fixture exists
5. Compute scorecard and maturity tier
6. Output the scorecard as JSON
7. Update the quality tracker if requested

## Implementation Notes

- Use `validateFieldSelectorMetadata()` from `src/core/metadata.ts` for S2
- Use `ensureSourceDocx()` from `src/core/field-selector/downloader.ts` for B1-B4
- Use `runFieldSelector()` from `src/core/field-selector/index.ts` for F1-F4
- Bracket pattern detection uses a two-or-more-character `\[[_A-Z][_A-Z\s]+\]` shape for re-audited NVCA selectors to avoid counting citations, legal references, and single-letter exhibit references
- Zero-match keys come from `PatchResult.zeroMatchKeys` returned by the patcher
- Cross-reference zero-match keys with `cleanConfig.removeRanges` and `cleanConfig.removeParagraphPatterns` to suppress expected zero-matches

> **Corrected 2026-09-02.** The first placeholder-only pattern admitted one-letter
> exhibit references such as `[E]`, depressing coverage even though they are not
> fill sites. Re-audited NVCA selectors now require at least two characters inside
> the bracket; underscore blanks such as `[__]` remain in scope.
