# Georgia statutes corpus (`ga-statutes-debt`)

Verbatim snapshot of the Official Code of Georgia Annotated (O.C.G.A.)
chapters most used in Georgia civil, consumer, and family practice.

> **Slug note:** the directory keeps the legacy `-debt` suffix for path
> stability (other skills cite into `references/ga-statutes-debt/`), but
> the **scope is full civil + family practice**, not just debt
> collection.

## Scope (O.C.G.A. chapters carried)

- **Title 9, Ch. 11** — Civil Practice Act (pleadings, motions,
  service § 9-11-4, discovery §§ 9-11-33/34/36, default § 9-11-55,
  summary judgment § 9-11-56).
- **Title 9, Ch. 3** — limitation of actions (§§ 9-3-24/25/26/33).
- **Title 24** — Georgia Evidence Code (2013 FRE-modeled; business
  records § 24-8-803(6), self-authentication § 24-9-902(11)).
- **Title 10, Ch. 1** — Fair Business Practices Act (FBPA, Art. 15
  Pt. 2; § 10-1-390 et seq., remedy § 10-1-399).
- **Title 7, Ch. 3** — Georgia Industrial / Installment Loan Act.
- **Title 18, Ch. 4** — garnishment (post-2016 renumbered chapter;
  §§ 18-4-4/5/6/15).
- **Title 44, Ch. 7** — landlord and tenant (dispossessory § 44-7-50
  et seq.; security deposits).
- **Title 44, Ch. 13** — debtor's exemptions (§ 44-13-100; Georgia is
  opted out of the federal bankruptcy exemptions).
- **Title 19** — domestic relations (divorce § 19-5-3, child support
  § 19-6-15, custody § 19-9-3, Family Violence Act § 19-13-1 et seq.).
- **Title 15** — courts (jurisdiction and organization;
  §§ 15-6-8, 15-7-4, 15-10-2).
- **Title 11** — Uniform Commercial Code (Georgia enactment).

## Sources

The **official O.C.G.A. text is paywalled and copyrighted**
(LexisNexis publishes the official annotated code for the State), so
it is **not** scraped. The corpus is built from open mirrors:

- **FindLaw** — `codes.findlaw.com/ga/` (current, scrapeable; the
  puller's primary open source).
- **Justia** — `law.justia.com/codes/georgia/` (corroborating mirror;
  Justia **403s automated fetch**, so it is a manual/fallback source,
  not the automated target).
- **`ga.elaws.us`** — `ga.elaws.us/ocga/{title-chapter-section}`
  (usable but can lag current text; confirm currency against FindLaw).

## Refresh

Pulled by `scripts/pull_georgia_statutes.py` (to be added), primarily
from FindLaw with Justia / `ga.elaws.us` as mirrors. After a refresh,
bump the `ga-law-references` `SKILL.md` `version:` (PATCH for a routine
refresh, MINOR if a new chapter is added). Note that § 19-6-15 (child
support) was revised effective 1/1/2026 — pull the post-1/1/2026 text.

> **NOT LEGAL ADVICE.** Snapshot from open mirrors for drafting
> reference only. The official annotated O.C.G.A. controls; verify
> current section text before relying on anything here.
