# court-rules Corpus — Idaho

> **NOT LEGAL ADVICE.** Confirm every rule against the canonical
> isc.idaho.gov page and check for pending amendments before relying on it.

This corpus holds **verbatim Idaho court-rule text** for the rules most
relevant to civil and family practice, fetched from the Idaho Supreme
Court (`isc.idaho.gov`) per-rule print views. Each set file carries the
verbatim rule text under `## Rule N. Title` headings. It is a **bounded,
representative** set — the rules a drafter actually cites — not an
enumeration of every rule in every set.

## Mode

- **Mode:** `verbatim` (fetched rule text).
- **Source:** Idaho Supreme Court — https://isc.idaho.gov/rules-procedure/
- **Puller:** `scripts/pull_idaho_rules.py`

## Set files

- `IRCP-civil-procedure.md` — Idaho Rules of Civil Procedure (I.R.C.P.)
- `IRE-evidence.md` — Idaho Rules of Evidence (I.R.E.)
- `IRFLP-family-law-procedure.md` — Idaho Rules of Family Law Procedure (I.R.F.L.P.)
- `IAR-appellate.md` — Idaho Appellate Rules (I.A.R.)

The **I.R.E.F.S.** (Idaho Rules for Electronic Filing and Service) is
referenced for filing mechanics in the host skill's `SKILL.md` and
`online-sources.md` rather than snapshotted as a dedicated file.

## Refresh

`scripts/pull_idaho_rules.py` fetches the per-rule print pages
(`https://isc.idaho.gov/rules-procedure/print/<slug>/<rule>`), strips the
site chrome, and writes verbatim Markdown per set (the set→rule map lives
in `_manifest.json`). A `_file_is_stub` guard preserves committed verbatim
content on a failed run; pass `--force` to overwrite. Widen a set by adding
rule numbers to its `rules` list in `_manifest.json`.
