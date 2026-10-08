# oh-statutes-debt Corpus — Ohio Revised Code (curated)

Verbatim text of selected **Ohio Revised Code** chapters, pulled from
the Ohio Legislative Service Commission's official publisher at
`https://codes.ohio.gov/ohio-revised-code/` by
`scripts/pull_ohio_statutes.py`. One Markdown file per chapter
(`RC-Chapter-<n>.md`) with `## § <n>.<nn>. Title` section headings.

> **NOT LEGAL ADVICE.** The R.C. is amended frequently. Verify any
> section against the current published text before relying on it.

This is a **curated subset** scoped to the plugin's civil-practice +
subject-bundle coverage — NOT the full Revised Code. The directory
name retains the legacy `debt` slug for path stability; scope now
spans consumer-debt, family, landlord-tenant, personal-injury,
employment, and commercial practice.

## Chapters by domain (40 chapters)

| Domain | Chapters |
|---|---|
| Definitions / time | 1 (legal holidays R.C. 1.14 + time computation R.C. 1.45) |
| Courts / disqualification | 2701 (incl. § 2701.03 affidavit of disqualification) |
| Court-structure codes | 1901 (municipal), 1907 (county), 1925 (small claims) |
| UCC | 1302 (Art. 2 sales), 1303 (Art. 3 instruments), 1309 (Art. 9 secured) |
| Consumer / auto finance | 1345 (CSPA), 1317 (RISA), 4505 (motor-vehicle titles + lien perfection) |
| Civil practice / enforcement | 2305 (SOLs), 2323 (med-mal caps / frivolous conduct / cognovits), 2329 (execution + exemptions), 2333 (debtor exam) |
| Landlord-tenant | 1923 (forcible entry & detainer), 5321 (RLTA) |
| Personal injury / torts | 2125 (wrongful death), 2307 (OPLA product liability + contribution), 2315 (comparative negligence + damages caps), 2744 (political-subdivision immunity), 955 (dog-bite) |
| Employment | 4111 (minimum wage), 4112 (civil rights / discrimination), 4113 (whistleblower + prompt-pay), 4123 (workers' comp), 4141 (unemployment) |
| Commercial / business | 1333 (OUTSA trade secrets), 1336 (UFTA fraudulent transfer), 1701 (corporations), 1706 (Revised LLC Act), 2711 (arbitration), 4165 (Deceptive Trade Practices Act) |
| Family law | 3105, 3109, 3113, 3115, 3119, 3127 |
| Juvenile | 2151 |

## Re-pull

```bash
# All chapters:
python3 scripts/pull_ohio_statutes.py \
  --out plugins/oh-court-docs/skills/oh-law-references/references/oh-statutes-debt
# One chapter:
python3 scripts/pull_ohio_statutes.py --only RC-Chapter-2315
```

The puller's `TARGETS` list in `scripts/pull_ohio_statutes.py` is the
source of truth for which chapters are carried; add a `ChapterTarget`
there to extend the corpus.
