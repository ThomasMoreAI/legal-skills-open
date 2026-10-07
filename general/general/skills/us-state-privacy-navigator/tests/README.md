# Tests

Stdlib-only test suite for the us-state-privacy-navigator skill. No external dependencies; runs anywhere Python 3.10+ runs.

## Run

```
python3 tests/run_all.py        # run everything
python3 tests/run_all.py -v     # verbose output
python3 -m unittest discover tests   # equivalent
python3 -m unittest tests.test_corpus_integrity   # single file
```

## What's covered

**`test_corpus_integrity.py`** — JSON well-formedness, ID uniqueness, taxonomy adherence, anchor-action presence, field-shape validation. Run this after any corpus edit. 12 tests.

**`test_precedent_match.py`** — Scoring and ranking against canonical privacy-counsel queries: GPC + processor contracts surfaces Healthline first; pixel-health surfaces Kaiser/Cerebral; CT notice surfaces TicketNetwork. 8 tests.

**`test_conflict_resolver.py`** — Multi-state synthesizer correctness: MD's flat sensitive-data ban controls when MD is in scope; dimension filtering narrows output; single-state synthesis still produces findings; unknown states don't crash. 7 tests.

**`test_citation_audit.py`** — Two layers: (a) fixture tests confirm the auditor flags planted issues in `memo_with_errors.md` and passes `memo_clean.md` cleanly; (b) reference-doc audits run the auditor against every shipped reference markdown file. The reference-doc tests caught 13 actual citation gaps during the v2.2 corpus expansion that have since been fixed — they are the safety net against future drift. 9 tests.

**`test_applicability_check.py`** — Threshold engine produces predictable verdicts for three canonical fixtures: a sub-threshold startup yields no applicable laws; a $30M / 50k-CA-consumer mid-market yields CA-only; a $500M national enterprise yields most states. Also verifies the "refuse to guess" principle: when state-specific inputs are missing, the engine returns Insufficient rather than guessing. 22 tests.

## What's not covered

- **The `references/states/*.md` per-state files** — these are descriptive content, not assertion-bearing claims, so they're excluded from the citation auditor sweep. If a contributor adds quantitative claims to a per-state file, they should run `python3 scripts/citation_audit.py --input references/states/X.md` manually.
- **The `assets/notice-clauses/*.md` files** — these are model clauses, not assertions, also excluded.
- **The `references/workflows/*.md` files** — operational checklists rather than legal claims.
- **`scripts/generate_docx_memo.js`** — the DOCX generator is templated content production; tested manually.

## Adding tests

Drop a `test_*.py` file with a `unittest.TestCase` subclass. The runner picks it up automatically. Use `subprocess.run` to invoke the scripts (don't import them directly) so tests exercise the actual CLI surface.

## Fixture conventions

`tests/fixtures/` holds:
- `intake_*.json` — applicability_check intake inputs (see `assets/applicability-questions.json` for schema).
- `gaps_sample.json` — precedent_match batch-mode gap definitions.
- `memo_clean.md` and `memo_with_errors.md` — citation auditor positive/negative cases.

Update fixtures when the underlying data model changes; tests deliberately couple to fixtures so they fail loudly when expected behavior shifts.
