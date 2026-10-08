# court-rules Corpus — Tennessee

Verbatim text of Tennessee's statewide rule sets, pulled by
`scripts/pull_tn_court_rules.py` from the Tennessee
Administrative Office of the Courts at `tncourts.gov`.

## What's here

| File | Source | Content |
|---|---|---|
| `Tenn-Rules-Civil-Procedure.md` | tncourts.gov | Tenn. R. Civ. P. — all rule sub-pages, verbatim |
| `Tenn-Rules-Evidence.md` | tncourts.gov | Tenn. R. Evid. — all rule sub-pages, verbatim |
| `Tenn-Rules-Appellate-Procedure.md` | tncourts.gov | Tenn. R. App. P. — all rule sub-pages, verbatim |
| `Tenn-Supreme-Court-Rules.md` | tncourts.gov | Tennessee Supreme Court Rules (incl. Tenn. Sup. Ct. R. 4 on citation) — all rule sub-pages, verbatim |
| `Tenn-Local-Rules-Practice.md` | tncourts.gov | Pointer stub — county-by-county local rules are not aggregated under a single HTML index; confirm the filing court's current local rules via the AOC index |
| `_manifest.json` | — | Last-pulled date and source notes |

The Tennessee AOC publishes each rule as its own HTML sub-page,
with the rule body inside `<div class="field--name-field-rules-rule-content">`.
The puller walks each rule set's landing page, discovers sub-
page URLs by path prefix, and aggregates one MD file per rule
set with the rule number/title as an H2 heading.

## How to refresh

```
python3 scripts/pull_tn_court_rules.py --workers 2
```

Wired into the quarterly `refresh-references` workflow under
`target=tn`. The puller writes atomically (`.md.tmp` + rename)
and updates `_manifest.json` on each successful full pull.

## How to populate the local-rules stub

County local rules are published by each county clerk and are
indexed at the AOC "Local Rules of Practice" page. Add a target
to `pull_tn_court_rules.py`'s `TARGETS` list (with `stub_only:
False` and a `rule_path_prefix` matching the county's clerk
site) when a particular county's local rules become reachable
in a parseable form.
