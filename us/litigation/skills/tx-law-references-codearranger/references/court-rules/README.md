# court-rules Corpus — Texas

> **NOT LEGAL ADVICE.** Confirm every rule against the canonical txcourts.gov
> PDF and check for amendments by order of the Supreme Court of Texas before
> relying on it.

This corpus holds **verbatim Texas court-rule text** for the rules most
relevant to civil practice, consumer-debt defense, family law, and
justice-court (small-claims / eviction) practice. Each set file carries the
verbatim rule text under `## Rule N. Title` headings. It is a **bounded,
representative** set — the rules a drafter actually cites — not an
enumeration of every rule in every set.

## Mode

- **Mode:** `verbatim` (text extracted from the official consolidated PDFs).
- **Source:** Supreme Court of Texas / Office of Court Administration —
  https://www.txcourts.gov/rules-forms/rules-standards/
- **Puller:** `scripts/pull_texas_rules.py`

## Set files

- `TRCP-civil-procedure.md` — Texas Rules of Civil Procedure (the main
  civil set: time computation, service, form of pleadings, the Rule 47(c)
  relief-range statement, special exceptions / Rule 91a dismissal, general
  denial / verified pleas, the **Rule 99 "Monday rule" answer deadline**,
  summary judgment 166a(c)/(i), expedited actions 169, discovery-control-
  plan levels 190, sworn account 185, discovery rules, new-trial /
  plenary-power 329b).
- `TRCP-justice-court.md` — TRCP **Part V** (Justice Court, Rules 500–510:
  representation, commencement, the 14-day answer, default, **de novo
  appeal to county court**, debt-claim cases, and eviction).
- `TRE-evidence.md` — Texas Rules of Evidence (relevance 401–403, hearsay
  801–804 incl. the **803(6) business-records** exception, authentication
  901–902 incl. **902(10) self-authentication of business records by
  affidavit**).
- `TRAP-appellate.md` — Texas Rules of Appellate Procedure (Rule 9 document
  form; **Rule 26.1 time to perfect appeal**; **Rule 30 restricted
  appeal**).

The TRCP main set and the Part V justice-court set are both extracted from
the single consolidated Texas Rules of Civil Procedure PDF.

## Refresh

`scripts/pull_texas_rules.py` downloads each set's consolidated PDF from
txcourts.gov (paths recorded in `_manifest.json`), extracts the text with
`pypdf`, locates each rule's heading, and slices the verbatim body to the
next heading (umbrella rules such as Rule 510 pull in their dotted
sub-rules). `pypdf` is an optional dependency:

```
pip3 install --break-system-packages pypdf
python3 scripts/pull_texas_rules.py --force
```

Without `pypdf`, or on a failed download / no-rule-found, the set file is
written as an honest **pointer stub** carrying the canonical PDF URL —
never fabricated text. A `_file_is_stub` guard preserves committed verbatim
content on a failed run; pass `--force` to overwrite. The OCA re-issues
amended editions at new `/media/` paths — update the `pdf` field in
`_manifest.json` when an amendment lands. Widen a set by adding rule
numbers to its `rules` list.

Note: TRCP Rule 78a (Case Information Sheet) was **repealed 12.11.2018** and
carries no verbatim body; it is listed in the manifest for traceability but
is correctly skipped by the puller.
