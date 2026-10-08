# tx-statutes-debt Corpus — Texas

> **NOT LEGAL ADVICE.** Confirm every section against the canonical
> statutes.capitol.texas.gov page and check for amendments from the most
> recent legislative session before relying on it.

This corpus holds **verbatim Texas statute text** for the sections most
relevant to civil practice, consumer-debt defense, and family law. Each
topic file carries the verbatim section text (catchline + body + history)
under `## Tex. <Code> § N.N` headings. It is a **bounded, representative**
set — the sections a drafter actually reaches for — not an enumeration of
the entire Texas statutes.

## Mode

- **Mode:** `verbatim` (fetched section text).
- **Source:** Texas Constitution and Statutes — https://statutes.capitol.texas.gov/
- **Puller:** `scripts/pull_texas_statutes.py`

The public viewer at `statutes.capitol.texas.gov` is a JavaScript
single-page app. The verbatim per-chapter HTML it resolves to is served
from the Legislature's file server at
`https://tcss.legis.texas.gov/resources/<CODE>/htm/<CODE>.<CHAPTER>.htm`;
the puller fetches each chapter page once, slices the HTML between section
catchline anchors, and writes the verbatim text. Cite the viewer URL.

## Code abbreviations

`CP` = Civil Practice & Remedies · `FI` = Finance · `BC` = Business &
Commerce · `PR` = Property · `FA` = Family · `GV` = Government.

## Topic files

- `CPRC-limitations.md` — Tex. Civ. Prac. & Rem. Code ch. 16 limitations
  (2-yr tort/PI § 16.003; **4-yr debt/contract § 16.004**; residual
  § 16.051; § 16.063 absence/nonresidence; § 16.065 written-acknowledgment
  to revive; § 16.069 counterclaim).
- `CPRC-fees-costs-judgments.md` — § 31.002 turnover, § 34.001 dormancy of
  judgment, § 34.021 liability for failure to levy/sell, § 37.009 UDJA
  fees, **Ch. 38 contract/sworn-account attorney fees**, § 132.001 unsworn
  declaration.
- `CPRC-proportionate-responsibility.md` — Ch. 33 modified comparative
  responsibility (**51% bar**), submission, and credit/contribution.
- `finance-code-debt-collection.md` — **Texas Debt Collection Act, Fin.
  Code ch. 392** (definitions; § 392.101 $10,000 surety-bond requirement;
  prohibited conduct §§ 392.301–.304; § 392.307 time-barred consumer debt;
  § 392.403 remedies; § 392.404 DTPA tie-in).
- `dtpa-bus-com.md` — **Deceptive Trade Practices–Consumer Protection Act,
  Bus. & Com. ch. 17** (consumer standing § 17.45; laundry list § 17.46;
  remedies + treble damages § 17.50; 60-day pre-suit notice § 17.505; SOL
  § 17.565).
- `property-exemptions-eviction.md` — Prop. Code Ch. 24 forcible
  entry/detainer (eviction), Ch. 41 homestead, Ch. 42 personal-property
  exemptions, § 92.331 tenant-retaliation.
- `family-code.md` — informal marriage § 2.401, community-property
  presumption § 3.003, divorce grounds/residency/waiting period (Ch. 6),
  just-and-right division § 7.001, conservatorship/possession (Ch. 153),
  child support (Ch. 154), spousal maintenance (Ch. 8).
- `holidays-courts-govt-code.md` — Gov't Code § 662.003 legal holidays,
  § 662.021 partial-staffing holidays, § 27.031 justice-court civil
  jurisdiction, § 22.004 Supreme Court rulemaking.
- `ucc-article9-bus-com.md` — Texas UCC Article 9 secured transactions
  (Bus. & Com. ch. 9: scope, attachment, priority, default/disposition).

## Refresh

`scripts/pull_texas_statutes.py` reads the topic→section map from
`_manifest.json`, fetches each unique `<CODE>.<CHAPTER>` page once, slices
each requested section, and writes verbatim Markdown. A `_file_is_stub`
guard preserves committed verbatim content on a failed run; pass `--force`
to overwrite. Widen a topic by adding section numbers to its `sections`
list in `_manifest.json`.
