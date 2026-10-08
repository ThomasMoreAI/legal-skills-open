# Oregon Court Rules Corpus

This directory holds verbatim text of the Oregon court rules
most relevant to civil practice, extracted from authoritative
sources.

## Rules covered

| Rules | File | Source | Update cycle |
|-------|------|--------|--------------|
| ORCP — Oregon Rules of Civil Procedure | `ORCP.md` | counciloncourtprocedures.org | Biennial (Jan 1, odd years) |
| UTCR — Uniform Trial Court Rules | `UTCR.md` | courts.oregon.gov | Annual (Aug 1) |
| ORAP — Oregon Rules of Appellate Procedure | `ORAP.md` | courts.oregon.gov | Periodic |
| OEC — Oregon Evidence Code (ORS 40) | `OEC.md` | oregonlegislature.gov | Per legislative session |
| ORPC — Oregon Rules of Professional Conduct | `ORPC.md` | osbar.org | Periodic |
| Multnomah SLR | `Multnomah-SLR.md` | courts.oregon.gov/courts/multnomah | Annual |
| Washington County SLR | `Washington-SLR.md` | courts.oregon.gov/courts/washington | Periodic |

## Citation tables

When citing in a filing, use these forms (per the Oregon Style
Manual):

| Rule | Cite form |
|------|-----------|
| ORCP | `ORCP 21 A(8)` |
| UTCR | `UTCR 2.010(1)` |
| ORAP | `ORAP 5.45` |
| OEC | `OEC 803(6)` (also citeable as `ORS 40.460(6)`) |
| Multnomah SLR | `Multnomah SLR 5.100` |

## How to re-pull

The Oregon plugin's `scripts/pull_oregon_rules.py` script (to
be created in parallel with the existing WA `pull_court_rules.
py`) handles the bulk extraction. To run:

```bash
python3 scripts/pull_oregon_rules.py \
  --workers 8 \
  --manifest plugins/or-court-docs/skills/or-law-references/references/court-rules/_manifest.json
```

(This script is on the to-do list for a future PR — the
infrastructure to support it is laid out here in the directory
structure.)

For ad hoc extraction without the script, use WebFetch against
the canonical URLs in `../online-sources.md`.

## Status

This corpus is **empty in the initial PR** — only this README
and a `_manifest.json` placeholder. The first re-pull will
populate the verbatim rule files. The quarterly agent routine
(once configured for Oregon) will keep it fresh.

## Cross-references

- `../online-sources.md` — canonical URLs
- `../legal-data-apis.md` — programmatic access
- `../civil-rules.md` — agent-facing summary of ORCP
- `../evidence-rules.md` — agent-facing summary of OEC
