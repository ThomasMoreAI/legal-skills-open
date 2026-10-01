# Changelog — colombia-conflict

## 0.2.0 — 2026-06-28

Full-text grounding substrate + on-demand PDF provenance (BRO-1580).

- **`references/fulltext/*.txt.gz`** — complete extracted text of all 24 volumes
  (~3.67M words, ~7.7 MB gzipped) bundled as verbatim grounding substrate.
- **`cc.py source <topic>`** — full-text search returning verbatim passages with
  match-centered snippets (the digests summarize; this quotes the report exactly).
- **`sources/MANIFEST.json`** (11 units, all sha256) + **`scripts/fetch_sources.sh`**
  — fetch + verify the 385 MB of source PDFs on demand (not committed).
- **`scripts/build_manifest.py`** — regenerate the manifest from a local corpus.
- Tests: 28 total (added full-text search, manifest-validity, corpus-presence).
- Also folded `_fold()` accent-folding into a shared helper.

## 0.1.0 — 2026-06-28

Initial release. Distilled (via `/skillify`, BRO-1578) from the Colombian Truth
Commission final report *Hay Futuro Si Hay Verdad* (2022), after downloading and
fan-out-digesting all 24 PDFs (~8,900 pp / ~3.67M words).

- **Substrate** — 12 per-volume sourced digests + master synthesis + lexicon in
  `references/`.
- **Data** — `statistics.json`, `actors.json`, `recommendations.json` (67 recs /
  8 blocks), `concepts.json`.
- **Engine** — `scripts/cc.py`: two-tier kg `load`, `rec`/`stat`/`actor`/`concept`
  queries, the `align` non-repetition scorer, and the `index` catalog generator.
- **Tests** — `tests/test_cc.py`: 17 unit + data-integrity tests (stdlib, no network).
- **Architecture** — kg / LLM-wiki (LLM-as-index): substrate + catalog projection
  + body-grep fallback + agent-as-query-engine.
