---
name: ga-law-references-codearranger
title: Georgia Law References
description: Matter-neutral reference hub for Georgia civil practice. Indexes the Georgia reference corpus — Uniform Court Rules (USCR + Uniform State Court Rules + Uniform Magistrate Court Rules + Supreme Court & Court of Appeals rules) and the O.C.G.A. chapters most used in civil, consumer, and family matters (Title 9 Civil Practice Act + limitations, Title 24 Evidence, Title 10 FBPA, Title 18 garnishment, Title 44 landlord-tenant + exemptions, Title 19 domestic relations, Title 15 courts, Title 11 UCC) — plus the shared federal corpora it symlinks. Triggers include "Georgia statute reference", "O.C.G.A. text", "look up O.C.G.A. §", "Georgia court rules", "USCR", "Uniform Superior Court Rule", "Georgia Civil Practice Act", "Georgia evidence rule", "Georgia statute of limitations", "look up Georgia case law", "what's the Georgia rule on X". Every other ga- skill cites into this corpus for rule numbers, statute sections, and case authorities.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Readme
  path: references/court-rules/README.md
- title: Court Of Appeals Rules
  path: references/court-rules/court-of-appeals-rules.md
- title: Supreme Court Rules
  path: references/court-rules/supreme-court-rules.md
- title: Uniform Magistrate Court Rules
  path: references/court-rules/uniform-magistrate-court-rules.md
- title: Uniform State Court Rules
  path: references/court-rules/uniform-state-court-rules.md
- title: Uniform Superior Court Rules
  path: references/court-rules/uniform-superior-court-rules.md
- title: Readme
  path: references/ga-statutes-debt/README.md
- title: Title 10 Ch 1 Fair Business Practices Act
  path: references/ga-statutes-debt/title-10-ch-1-fair-business-practices-act.md
- title: Title 11 Ucc
  path: references/ga-statutes-debt/title-11-ucc.md
- title: Title 15 Courts
  path: references/ga-statutes-debt/title-15-courts.md
- title: Title 18 Ch 4 Garnishment
  path: references/ga-statutes-debt/title-18-ch-4-garnishment.md
- title: Title 19 Domestic Relations
  path: references/ga-statutes-debt/title-19-domestic-relations.md
- title: Title 24 Evidence
  path: references/ga-statutes-debt/title-24-evidence.md
- title: Title 44 Ch 13 Exemptions
  path: references/ga-statutes-debt/title-44-ch-13-exemptions.md
- title: Title 44 Ch 7 Landlord Tenant
  path: references/ga-statutes-debt/title-44-ch-7-landlord-tenant.md
- title: Title 7 Ch 3 Installment Loan Act
  path: references/ga-statutes-debt/title-7-ch-3-installment-loan-act.md
- title: Title 9 Ch 11 Civil Practice Act
  path: references/ga-statutes-debt/title-9-ch-11-civil-practice-act.md
- title: Title 9 Ch 3 Limitations
  path: references/ga-statutes-debt/title-9-ch-3-limitations.md
---

# Georgia Law References

> **NOT LEGAL ADVICE.** This skill is a procedural and reference aid,
> not legal advice. Verify current rules, deadlines, and citations
> against the authoritative source before relying on anything here.
> Pair with substantive review by counsel where stakes warrant.

This is the **matter-neutral reference hub** for Georgia civil
practice. It is a pointer index: it tells the other `ga-` skills
where the rule text, statute text, and case authorities live, and
gives a curated topic map of the key Georgia authorities. It does
**not** reproduce statutory text — read the cited section in the
corpus or at an open source before relying on it.

## Corpus layout

```
references/
├── court-rules/            # Verbatim Georgia court-rule corpus:
│                           #   Uniform Superior Court Rules (USCR)
│                           #   Uniform State Court Rules
│                           #   Uniform Magistrate Court Rules
│                           #   Supreme Court of Georgia rules
│                           #   Court of Appeals rules
├── ga-statutes-debt/       # O.C.G.A. chapters most used in civil,
│                           #   consumer, and family practice
│                           #   (slug retains the legacy "-debt"
│                           #   suffix for path stability; scope is
│                           #   full civil + family — see below)
├── federal-debt-laws/      # FDCPA, FCRA, TILA, ECOA, etc. (symlink
│                           #   into claude-legal-federal-laws)
├── federal-bankruptcy/     # Title 11 U.S.C. (symlink)
└── ucc-model/              # Model UCC Articles 1/2/3/9 (symlink)
```

The three symlinked directories point into the shared
`claude-legal-federal-laws` plugin; the federal text is not
duplicated per state. Georgia-specific text (`court-rules/`,
`ga-statutes-debt/`) stays in-plugin.

### O.C.G.A. chapters carried in `ga-statutes-debt/`

| O.C.G.A. | Subject |
|----------|---------|
| Title 9, Ch. 11 | **Civil Practice Act** (pleadings, motions, discovery, judgments) |
| Title 9, Ch. 3 | **Limitation of actions** (statutes of limitation) |
| Title 24 | **Georgia Evidence Code** (2013 FRE-modeled) |
| Title 10, Ch. 1 | **Fair Business Practices Act** (FBPA, Art. 15 Pt. 2) |
| Title 7, Ch. 3 | **Georgia Industrial / Installment Loan Act** |
| Title 18, Ch. 4 | **Garnishment** (post-2016 renumbered chapter) |
| Title 44, Ch. 7 | **Landlord and tenant** (dispossessory + security deposits) |
| Title 44, Ch. 13 | **Debtor's exemptions** (homestead / personalty) |
| Title 19 | **Domestic relations** (divorce, support, custody, family violence) |
| Title 15 | **Courts** (jurisdiction, terms, court organization) |
| Title 11 | **Uniform Commercial Code** (Georgia enactment) |

## Curated authority index by topic

Chapter-level pointers only — read the section in the corpus or at an
open source for the operative text.

### Courts and jurisdiction (Title 15)

- **O.C.G.A. § 15-6-8** — Superior Court (general jurisdiction;
  exclusive over divorce, equity, title to land, felonies).
- **O.C.G.A. § 15-7-4** — State Court (limited jurisdiction;
  civil actions of **any amount** except the superior-exclusive
  classes — most debt and tort suits sit here).
- **O.C.G.A. § 15-10-2** — Magistrate Court (civil jurisdiction
  capped at **$15,000**; dispossessory, garnishment within cap,
  distress warrants; appeal de novo).

### Civil Practice Act (O.C.G.A. Title 9, Ch. 11)

- **§ 9-11-4** — process; summons and service (incl. § 9-11-4(f)
  methods and § 9-11-4.1 service by mail / waiver).
- **§ 9-11-12** — defenses and objections; **answer due 30 days**
  (§ 9-11-12(a)); 12(b)(6) motion to dismiss.
- **§ 9-11-33 / 9-11-34 / 9-11-36** — interrogatories (50-cap
  incl. subparts), requests for production, requests for admission
  (deemed admitted if no timely response).
- **§ 9-11-55** — default judgment (open as of right within 15 days
  on payment of costs; thereafter only on the (b) showing).
- **§ 9-11-56** — summary judgment (motion served ≥ 30 days before
  hearing).

### Evidence (O.C.G.A. Title 24)

- **§ 24-8-803(6)** — business-records hearsay exception (the
  debt-buyer / records-foundation workhorse).
- **§ 24-9-902(11)** — self-authentication of certified domestic
  business records (custodian affidavit + notice to adverse parties).

### Statutes of limitation (O.C.G.A. Title 9, Ch. 3)

- **§ 9-3-24** — written / simple contract = **6 years**.
- **§ 9-3-25** — open account / oral / implied contract = **4 years**.
- **§ 9-3-26** — catch-all contract limitation = **4 years**.
- **§ 9-3-33** — injury to the person = **2 years** (defamation
  = 1 year; loss of consortium = 4 years).

### Consumer / debt (Title 10, Title 7)

- **§ 10-1-390 et seq.** — Fair Business Practices Act (FBPA);
  prohibition on unfair / deceptive consumer-marketplace acts.
- **§ 10-1-399** — FBPA private remedy: actual damages, treble
  damages for intentional violation, attorney fees, and the
  **30-day pre-suit written demand** (§ 10-1-399(b)).
- Title 7, Ch. 3 — Installment Loan Act (loans ≤ $3,000; the only
  Georgia debt-side licensing regime).

### Garnishment (Title 18, Ch. 4)

- **§ 18-4-4** — process and garnishment period; garnishee answer
  window.
- **§ 18-4-5** — wage-garnishment limit (lesser of 25% of disposable
  earnings or the amount over 30× the federal minimum wage).
- **§ 18-4-6** — exempt funds (retirement, Social Security, SSI, VA,
  unemployment, workers' comp, disability).
- **§ 18-4-15** — defendant's claim / challenge mechanism for
  asserting an exemption.

### Exemptions (Title 44, Ch. 13)

- **§ 44-13-100** — debtor's exemptions (homestead, vehicle,
  wildcard, household goods, tools); Georgia has **opted out** of the
  federal bankruptcy exemptions (§ 44-13-100(b)).

### Family law (Title 19)

- **§ 19-5-3** — grounds for divorce (12 fault + no-fault
  "irretrievably broken").
- **§ 19-6-15** — child support (income-shares model; BCSO table).
- **§ 19-9-3** — custody (best-interests standard; child election at
  14+).
- **§ 19-13-1 et seq.** — Family Violence Act (definition,
  protective orders).

### Landlord-tenant (Title 44, Ch. 7)

- **§ 44-7-50** — demand for possession + sworn dispossessory
  affidavit (precondition to a dispossessory).
- **§ 44-7-51** — summons and service; **answer due 7 days** from
  actual service (§ 44-7-51(b)).
- **§ 44-7-55** — judgment and writ of possession.

### Key cases (general civil + family)

Cite with the official reporter and the S.E.2d parallel (Georgia
still uses the official `Ga.` / `Ga. App.` reporters — there is no
public-domain neutral citation).

- **Lau's Corp., Inc. v. Haskins, 261 Ga. 491, 405 S.E.2d 474
  (1991)** — Celotex-style summary judgment; movant may point to the
  absence of evidence (governs § 9-11-56).
- **Stokes v. Stokes, 246 Ga. 765, 273 S.E.2d 169 (1980)** —
  Georgia is an equitable-distribution (not community-property)
  state for marital property.
- **Hill v. American Express, 289 Ga. App. 576, 657 S.E.2d 547
  (2008)** — credit-card debt is a written contract (6-year
  limitation under § 9-3-24).
- **Nyankojo v. North Star Capital Acquisition, 298 Ga. App. 6, 679
  S.E.2d 57 (2009)** — debt-buyer must prove an unbroken chain of
  assignment (the go-to for attacking debt-buyer standing).
- **Bowen v. Savoy, 308 Ga. 204, 839 S.E.2d 546 (2020)** — the
  "proper case" prong of § 9-11-55(b) needs no reasonable
  explanation.

## Citation conventions

- **Cases**: `Lau's Corp. v. Haskins, 261 Ga. 491, 405 S.E.2d 474
  (1991)` (Supreme Court); `Nyankojo v. North Star Capital
  Acquisition, 298 Ga. App. 6, 679 S.E.2d 57 (2009)` (Court of
  Appeals). Official `Ga.` / `Ga. App.` reporters plus the `S.E.2d`
  regional parallel — Georgia has not adopted a public-domain neutral
  citation, so always supply the reporter cite.
- **Statutes**: `O.C.G.A. § 9-11-56` (always with `§`; subsections
  `O.C.G.A. § 10-1-399(b)`).
- **Court rules**: `USCR 6.2` (Uniform Superior Court Rules); name
  the rule set for the others (e.g., "Uniform Magistrate Court Rule
  __", "Supreme Court of Georgia Rule __").
- **Federal**: `15 U.S.C. § 1692g(b)`; `12 C.F.R. § 1006.34`.

## Online sources

Open verification sources (Georgia has no free official statute-HTML
site; the official LexisNexis O.C.G.A. is paywalled and copyrighted,
so it is **not** scraped):

- **Statutes (O.C.G.A.)**:
  - FindLaw — `codes.findlaw.com/ga/` (current, scrapeable; primary
    open mirror for the puller).
  - Justia — `law.justia.com/codes/georgia/` (corroborating mirror;
    note Justia **403s automated fetch**, so it is a fallback/manual
    source, not the automated puller's target).
  - `ga.elaws.us/ocga/{title-chapter-section}` (usable but can lag;
    confirm currency against FindLaw).
- **Court rules**: `georgiacourts.gov` (and `assets.georgiacourts.gov`
  for dated USCR / Uniform Magistrate Court Rule PDFs); Council of
  Superior Court Judges at `cscj.georgiacourts.gov`; Supreme Court
  rules at `gasupreme.us/rules/`; Court of Appeals rules at
  `gaappeals.gov/court-rules/`.
- **Opinions**: `gasupreme.us/opinions/`, `gaappeals.gov/opinion-search/`,
  and CourtListener (court IDs **`ga`** = Supreme Court of Georgia,
  **`gactapp`** = Court of Appeals of Georgia).
- **County e-filing portals**: PeachCourt (`peachcourt.com`; Cobb,
  Gwinnett among others) and Odyssey eFileGA
  (`efilega.tylertech.cloud`; Fulton and many others); county-to-portal
  map at `georgiacourts.gov/efile-court-records/`.

## Legal data APIs

- **CourtListener / Legal Data Hunter MCP servers** — bundled by the
  shared `claude-legal-federal-laws` dependency (its `.mcp.json`) for
  live case-law lookup. Use court IDs `ga` and `gactapp` to scope to
  Georgia. These are the runtime path for "look up Georgia case law"
  — the snapshotted corpus carries statute and rule text, not the full
  opinion set.
- **Puller URL patterns** (used by the refresh scripts):
  - Statutes — `pull_georgia_statutes.py` (to be added): FindLaw
    (`codes.findlaw.com/ga/`), with Justia / `ga.elaws.us` as mirrors.
  - Court rules — `pull_georgia_rules.py` (to be added):
    `georgiacourts.gov` / `assets.georgiacourts.gov` PDFs plus the
    appellate-court rule pages.

## Composition

Every other `ga-` skill cites **into this corpus** for rule numbers,
statute sections, and case authorities rather than restating the law
itself. In particular:

- **`ga-fact-check`** — verifies the citations a draft relies on
  against this corpus (and the live MCP lookup for cases).
- **`ga-statewide-format`** — the pleading-form baseline
  (O.C.G.A. § 9-11-10 + the Uniform Court Rules indexed here).
- **`ga-deadlines`** — time computation (§ 1-3-1 / § 9-11-6) and the
  § 1-4-1 holiday set; this hub holds the limitation periods it pairs
  with.
- **`ga-consumer-debt`** — the FBPA, Installment Loan Act,
  garnishment, exemption, and SOL pointers above plus the federal
  symlinks.
- **`ga-family-law`** — the Title 19 domestic-relations pointers.

For the specific filing court, see the venue skills (`ga-fulton`,
`ga-cobb`, `ga-gwinnett`, `ga-county-courts`); for pro se conventions,
`ga-pro-se`.

## References

- `references/court-rules/` — verbatim Georgia court-rule corpus
  (USCR, Uniform State Court Rules, Uniform Magistrate Court Rules,
  Supreme Court & Court of Appeals rules); populated by
  `pull_georgia_rules.py`.
- `references/ga-statutes-debt/` — O.C.G.A. chapters most relevant to
  civil, consumer, and family practice; populated by
  `pull_georgia_statutes.py`.
- `references/federal-debt-laws/` — shared federal-law corpus
  (symlink).
- `references/federal-bankruptcy/` — shared Title 11 corpus (symlink).
- `references/ucc-model/` — shared Model UCC text (symlink).
