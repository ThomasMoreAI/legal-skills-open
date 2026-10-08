# in-statutes-debt Corpus — Indiana

This directory holds verbatim text of the Indiana Code articles
most relevant to civil practice, consumer-debt defense, and the
co-family-law subject bundle. Source: the Indiana General Assembly
(`iga.in.gov`), Office of Code Revision.

The contents are refreshed by the quarterly
`scripts/pull_indiana_statutes.py` agent routine.

## Articles covered

| Article | Topic | File | Update cycle |
|---|---|---|---|
| IC 24-4.5 | Indiana Uniform Consumer Credit Code (IUCCC) | `IC-24-4-5.md` | Quarterly |
| IC 24-5-0.5 | Deceptive Consumer Sales Act (DCSA — UDAP analog) | `IC-24-5-0-5.md` | Quarterly |
| IC 26-1-2 | UCC Article 2 — Sales | `IC-26-1-2.md` | Quarterly |
| IC 26-1-3 | UCC Article 3 — Negotiable Instruments | `IC-26-1-3.md` | Quarterly |
| IC 26-1-9.1 | UCC Article 9 — Secured Transactions | `IC-26-1-9-1.md` | Quarterly |
| IC 31-15 | Dissolution / annulment / legal separation | `IC-31-15.md` | Quarterly |
| IC 31-17 | Child custody and visitation rights | `IC-31-17.md` | Quarterly |
| IC 32-21 | Conveyance of real property | `IC-32-21.md` | Quarterly |
| IC 32-29 | Mortgages | `IC-32-29.md` | Quarterly |
| IC 32-30 | Real-property liens / foreclosure | `IC-32-30.md` | Quarterly |
| IC 32-31 | Landlord-tenant relations | `IC-32-31.md` | Quarterly |
| IC 33-29 | Indiana Superior Courts (jurisdiction / organization) | `IC-33-29.md` | Quarterly |
| IC 34-11 | Limitation of actions (SOLs) | `IC-34-11.md` | Quarterly |
| IC 34-26 | Civil-procedure provisions; protective orders | `IC-34-26.md` | Quarterly |
| IC 34-50 | Indiana Mediation Act / settlement of disputes | `IC-34-50.md` | Quarterly |
| IC 34-55 | Property exempt from execution; homestead | `IC-34-55.md` | Quarterly |
| IC 34-57 | Garnishment proceedings; enforcement of judgments | `IC-34-57.md` | Quarterly |
| IC 35-43-5 | Forgery, fraud, identity theft (civil parallels) | `IC-35-43-5.md` | Quarterly |

## Key sections by article

### IC 34-11 — Limitation of actions

The most-cited Indiana SOL sections for consumer-debt defense:

- **IC 34-11-2-9** — 6-year SOL on promissory notes, bills of
  exchange, deposit accounts, and other **written contracts for
  the payment of money** executed after August 31, 1982. (10-year
  SOL for contracts executed September 19, 1881 – August 31, 1982.)
- **IC 34-11-2-11** — 10-year SOL on **other written contracts**
  (i.e. written contracts not for payment of money). Note: the
  prompt-cited "6 yr written contract for money" maps to
  **IC 34-11-2-9**, not -11.
- **IC 34-11-2-7** — 6-year SOL on **accounts and contracts not in
  writing** (open accounts, oral contracts).
- **IC 34-11-2-13** — 6-year SOL on actions for relief from a
  fraud, accruing on discovery.
- **IC 34-11-3** — Accrual rules.
- **IC 34-11-5** — Tolling for concealment.
- **IC 34-11-6** — Tolling for legal disability.

### IC 24-4.5 — IUCCC

- **IC 24-4.5-3-105** — Permitted additional charges.
- **IC 24-4.5-5** — Consumer-credit remedies; cure rights.
- **IC 24-4.5-6** — Administrator (Department of Financial
  Institutions) and licensing of consumer-credit / debt-collection
  activity.

### IC 24-5-0.5 — DCSA

- **IC 24-5-0.5-3** — Deceptive consumer-sales acts catalog
  (Indiana's UDAP-equivalent).
- **IC 24-5-0.5-4** — Remedies, including treble damages on
  incurable / intentional deceptive acts.

### IC 26-1-2, IC 26-1-3, IC 26-1-9.1 — Indiana UCC

Indiana's enactments of Model UCC Articles 2, 3, and 9. The text
parallels the model UCC (already mirrored in
`../ucc-model/`), with Indiana variants.

### IC 31-15, IC 31-17 — Family law

- **IC 31-15-2** — Dissolution-of-marriage grounds and procedure.
- **IC 31-15-7** — Property disposition under Indiana's "one-pot"
  equitable-division regime.
- **IC 31-17-2** — Custody factors and joint-legal-custody
  presumptions.
- **IC 31-17-2-15** — Parenting-time guidelines (referencing the
  Indiana Parenting Time Guidelines as a separate publication).

### IC 32-21, IC 32-29, IC 32-30, IC 32-31 — Real property

- **IC 32-21-1** — Statute of Frauds for real-property
  conveyances.
- **IC 32-29-7** — Mortgage-foreclosure procedure and the
  three-month settlement-conference period under
  IC 32-30-10.5.
- **IC 32-31-3** — Security deposits.
- **IC 32-31-5, IC 32-31-7** — Landlord and tenant obligations;
  residential eviction.

### IC 34-26 — Special civil actions

- **IC 34-26-5** — Indiana Civil Protection Order Act.
- **IC 34-26-6** — Workplace Violence Restraining Orders Act.

### IC 34-50 — Mediation / ADR

- **IC 34-50-2** — Court-annexed mediation.

### IC 34-55 — Exemptions from execution

- **IC 34-55-10-2** — Indiana's exempt-property schedule
  (homestead, intangibles, retirement accounts, etc.). Amounts
  are CPI-adjusted; see the Department of Financial Institutions
  publication for current figures.

### IC 34-57 — Garnishment / enforcement

- **IC 34-57-3** — Wage garnishment.
- **IC 34-57-1** — Final-process enforcement of judgments.

### IC 33-29 — Superior Courts

- **IC 33-29-1** — Standard superior courts.
- **IC 33-29-1.5** — Reorganization to multi-judge superior
  courts.

### IC 35-43-5 — Forgery, fraud, identity theft

- **IC 35-43-5-1, -2, -3, -3.5, -4** — Forgery, counterfeiting,
  fraud, identity deception, identity theft. Most relevant to
  civil practice when consumer fraud or identity-theft defenses
  arise.

## How to re-pull

```bash
python3 scripts/pull_indiana_statutes.py \
  --out plugins/in-court-docs/skills/in-law-references/references/in-statutes-debt \
  --workers 4

# Refresh one article only:
python3 scripts/pull_indiana_statutes.py --only IC-34-11

# Override the Indiana Code edition year (default 2024):
python3 scripts/pull_indiana_statutes.py --year 2024
```

## Upstream-access status (May 2026)

As of the initial PR, **every article file in this directory is a
`STATUS: fetch failed` stub.** The reason: `iga.in.gov` is a
single-page React application served via CloudFront. Every path —
including the URL pattern the prompt verified
(`https://iga.in.gov/laws/2024/ic/titles/34/articles/11`) — returns
the 691-byte SPA shell HTML rather than server-rendered statute
text. The substantive content is loaded by the JS runtime from the
authenticated `api.iga.in.gov` backend, which requires a registered
API key (`x-api-key`).

The puller is built to handle two recovery paths:

1. **API key (preferred).** Register at
   <https://docs.api.iga.in.gov> for an `IGA_API_KEY` and add it
   as a GitHub Actions secret. The puller picks it up
   automatically and walks
   `article → chapters → sections` via JSON. No code change
   required — set the secret on the `refresh-references`
   workflow and the next quarterly run will replace every stub
   with verbatim text.

2. **Server-rendered HTML.** If IGA fixes the CloudFront
   configuration to server-render `/laws/<year>/ic/...` paths,
   the puller's HTML scrape path will start producing populated
   sections automatically; the SPA-shell detector in the script
   will see substantive paragraphs and route content into the
   verbatim output.

Until one of those is in place, the corpus mirrors the article
shape but downstream skills should rely on:
- `../court-rules/` for Indiana Trial / Evidence / Appellate /
  Professional-Conduct / Administrative rules (pulled separately
  by `scripts/pull_indiana_rules.py`).
- `../federal-debt-laws/` for FDCPA / FCRA / TILA / ECOA / Reg
  F/V/Z/B (shared content, identical across state plugins).
- `../ucc-model/` for the Model UCC Articles 2, 3, and 9 (shared
  content). The Indiana enactments at IC 26-1-2 / -1-3 / -1-9.1
  parallel the model text with the Indiana-specific variants
  flagged in `co-consumer-debt` and the WA/OR equivalents.

## Cross-references

- `../online-sources.md` — canonical URLs for IC and other Indiana
  legal sources.
- `../legal-data-apis.md` — programmatic access notes (MyIGA
  Hypermedia API, etc.).
- `../../in-consumer-debt/` — Indiana consumer-debt subject bundle
  that relies on this corpus once populated.
- `../court-rules/` — Indiana court-rule corpus (state-wide +
  Marion / Lake local rules).
