# court-rules Corpus — Indiana

- Last refreshed: 2026-05-14
- Rule sets (verbatim PDF conversions): 7
- Total corpus size: ~2.0 MB

Verbatim text of the Indiana court-rule sets most relevant to civil practice. Sources: the Indiana Supreme Court rule-publication site `rules.incourts.gov` (state-wide rule sets) and the Indiana Judicial Branch's main asset host `in.gov/courts/files/` (county local-rule PDFs).

Refresh with `python3 scripts/pull_indiana_rules.py` (auto-runs quarterly via `.github/workflows/refresh-references.yml` under target `in`).

## Inventory

| File | Citation form | Source |
|---|---|---|
| `Trial-Rules.md` | `Ind. Trial R.` / `T.R.` | https://rules.incourts.gov/pdf/PDF%20-%20Trial/trial.pdf |
| `Evidence-Rules.md` | `Ind. Evid. R.` / `IRE` | https://rules.incourts.gov/pdf/PDF%20-%20Evidence/evidence.pdf |
| `Appellate-Rules.md` | `Ind. App. R.` | https://rules.incourts.gov/pdf/PDF%20-%20Appellate/appellate.pdf |
| `Professional-Conduct.md` | `Ind. R. Prof. Cond.` | https://rules.incourts.gov/pdf/PDF%20-%20Professional%20Conduct/professional-conduct.pdf |
| `Admin-Rules.md` | `Ind. Admin. R.` | https://rules.incourts.gov/pdf/PDF%20-%20Admin/admin.pdf |
| `Marion-Local-Rules.md` | `LR49-...` | https://www.in.gov/courts/files/marion-local-rules.pdf |
| `Lake-Local-Rules.md` | `LR45-...` | https://www.in.gov/courts/files/lake-local-rules.pdf |

## Conversion approach

Each PDF is fetched with retry+backoff and converted via `pdftotext -layout`. Layout mode preserves the document's column structure, which matters for rule numbering and indentation. The raw `pdftotext` output is written under a standard Markdown header block (title + source URL + fetch date + format note + "NOT LEGAL ADVICE" disclaimer).

No paraphrasing or human re-typing — the body is exactly what `pdftotext` emits. If a downstream skill needs cleaner formatting (e.g., bolded rule headings), the cleanup happens in the consuming skill, not in this corpus.

## Refresh

```bash
# All seven sets:
python3 scripts/pull_indiana_rules.py

# One set:
python3 scripts/pull_indiana_rules.py --only Evidence-Rules

# Different output directory (e.g., a sanity-check scratch dir):
python3 scripts/pull_indiana_rules.py --only Trial-Rules --out /tmp/in-rules-test
```

Refresh is also wired into `.github/workflows/refresh-references.yml` as the `in` target (manual dispatch + quarterly cron). The workflow pulls all seven rule sets and opens a PR if anything changed.

## Why these seven sets

- **Trial Rules** — Indiana's civil-procedure rule set; the foundation for every civil filing.
- **Evidence Rules** — admissibility, privileges, judicial notice, hearsay framework.
- **Appellate Rules** — for any procedural skill that touches appellate timing or briefing.
- **Professional Conduct** — duties owed by counsel; relevant to ethics-adjacent procedural questions.
- **Administrative Rules** — court administration, including recordkeeping (Admin Rule 9), electronic filing standards, and case-management rules that civil litigants must comply with.
- **Marion County LR49** — Indianapolis. Indiana's highest-volume civil court complex; many consumer-debt cases land here.
- **Lake County LR45** — Hammond / Crown Point. Indiana's second-largest county by population; significant civil docket.

Long tail of other counties (Allen / LR02, St. Joseph / LR71, etc.) is referenced inline in `in-county-courts` SKILL.md when relevant; the puller can be extended with additional LR codes by adding entries to the `SPECS` list in `scripts/pull_indiana_rules.py`.

## NOT LEGAL ADVICE

Each generated file repeats the standard claude-legal "not legal advice" disclaimer in its header block.
