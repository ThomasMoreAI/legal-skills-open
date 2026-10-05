# company-registers, Roadmap / TODOs

State of each country path. Goal: real financial figures **and** structured register data,
not just listing/metadata.

_Last updated: 2026-07-10 (FR + PL rebuilt, DE Handelsregister added; all live-tested)._

## Status at a glance

| Country | Search / metadata | Financials | Structured register data | State |
|---|---|---|---|---|
| **DE** Jahresabschluss | ✅ Unternehmensregister + Bundesanzeiger, parallel, CAPTCHA-free | ✅ figures ≤2021 (BA) and GJ 2022+ (UR, free-captcha) via Claude | n/a | ✅ **DONE** |
| **DE** Handelsregister | ✅ handelsregister.de search (browser) | n/a | ✅ Geschäftsführer, Stammkapital, Sitz, Gegenstand, Prokura, Rechtsform (AD → parsed) | ✅ **DONE** (this session) |
| **FR** France | ✅ name/SIREN via recherche-entreprises (free) | ✅ **revenue + earnings free**; total assets needs INPI token | ✅ officers (dirigeants) | ✅ **DONE** (this session) |
| **PL** Poland | ✅ name (browser) · KRS number · NIP→KRS | ⚠️ filing list (periods/dates); figures gated (JPK XML) | ✅ share capital, purpose, board, seat | ✅ **core DONE** (this session) |
| **GB** UK | ⚠️ needs a free API key (none configured) | ❌ `financial_data: null`, needs iXBRL parse | metadata only | ⛔ **TODO** |

**Not free anywhere (paid only):** Austria (Firmenbuch), Spain (Registro Mercantil),
Netherlands (KVK). Documented as "not supported".

---

## ✅ DE, Jahresabschluss (reference implementation)

`de-combined.js` runs the Unternehmensregister + Bundesanzeiger **concurrently**, merges per
company × fiscal year, tags each report's source, isolates the CAPTCHA to on-demand extraction.
`report` extracts every free year's figures in one pass. Benchmarks: latest ~0.34 s, parallel
`--all` ~1.1 s (total ≈ max(UR, BA) → true parallelism).

## ✅ DE, Handelsregister (new)

`de-handelsregister.js` + `hr-browser.py`. `search` → register rows (name, HRB, court, seat,
status, former names). `details --hrb N` → downloads the AD (free, post-DiRUG) and parses the
numbered sections into JSON: `share_capital`, `managing_directors[]` (with birth dates + titles),
`prokura[]`, `legal_form`, `purpose`, `seat`, `business_address`, `last_entry_date`. Verified on
Holz-Richter GmbH (HRB 37497). Known constraint: handelsregister.de **rate-limits document
retrieval**, the helper detects the throttle page, retries, then returns `reason:"throttled"`;
retry after a short cooldown. Search itself isn't throttled.
- [ ] Optional: parse the **SI (structured XML)** instead of the AD PDF once the SI flow is stable
  (it currently errors); would drop the pdftotext dependency.

## ✅ FR, France (INPI / RNE)

`fr-inpi.js` rebuilt on `recherche-entreprises.api.gouv.fr` (free, no key). Fixed the broken name
search (dead `data.inpi.fr` primary → `recherche-entreprises` is now primary). Returns real
**revenue** (`ca`) + **earnings** (`resultat_net`) per year + **officers** for companies in the open
ratios dataset, plus metadata. `analyze` picks the best entity for a name, or takes a SIREN.
- [ ] Optional: wire the free `INPI_API_TOKEN` (RNE API) for balance-sheet depth (total assets/equity).
  Revenue already works without it.

## ✅ PL, Poland (KRS), core done

`pl-krs.js` rebuilt on the official Ministry-of-Justice API (`api-krs.ms.gov.pl`), reliable by
**KRS number**: name, legal form, NIP/REGON, seat, **share capital**, purpose (PKD), board
(GDPR-masked names), filed-statement list. `nip <nip>` resolves via the MF whitelist. `search
"name"` uses the stealth browser (`pl-browser.py`; the portal is Incapsula-protected) → tagged
`{krs, name, city, register}` candidates. Verified: Orlen, IKEA Retail, CD PROJEKT.
- [ ] **Financial figures** still gated: the e-sprawozdania (JPK XML) in the RDF repository need a
  session flow on `ekrs.ms.gov.pl`. Currently we return the filing list + repository link.
  Implement XML download + parse (`Przychody netto ze sprzedaży` → revenue, `Suma aktywów` →
  total_assets, `Wynik netto` → earnings).

## ⛔ GB, UK (Companies House), TODO (deferred by user)

`gb-companies-house.js` returns metadata but leaves `financial_data` all `null`.
- [ ] **Provision a free API key** (hard blocker, nothing runs without it):
  https://developer.company-information.service.gov.uk/ → `COMPANIES_HOUSE_API_KEY` as an
  env var or in `config/keys.json`.
- [ ] **Extract figures from the accounts iXBRL.** `getFilingHistory(number,'accounts')` → newest
  filing → `links.document_metadata` → `document-api.company-information.service.gov.uk` →
  `Accept: application/xhtml+xml` → parse `<ix:nonFraction>` by taxonomy local-name (`Turnover`,
  `TotalAssetsLessCurrentLiabilities`, `NetAssetsLiabilities`, `ProfitLoss`,
  `AverageNumberEmployeesDuringPeriod`), honouring `sign`/`scale`/`decimals` and the latest context.
  - Deterministic tag parse preferred (free, no LLM); Claude extraction as fallback across
    FRS 105 / FRS 102 / IFRS layouts.
- [ ] Expect legitimate `null` turnover for micro/abridged accounts, fill balance-sheet items,
  leave revenue `null` with a reason.

---

## Cross-cutting

- [ ] **Unify the output contract** across all `analyze` commands (`revenue, total_assets, earnings,
  equity, employees, fiscal_year, currency` + `source`) for country-agnostic B2B-lead enrichment.
- [ ] **Config bootstrap**, add a `config/keys.json` template + "which key unlocks what"
  (GB → figures; FR → balance-sheet depth; DE/PL → none for the core).
- [ ] **Multi-country parallel lookup** in `search.js` (same `Promise.all` pattern as `de-combined.js`)
  to check a lead across DE/FR/PL/GB at once.
- [ ] **Browser dependency note**, DE-Handelsregister and PL-name-search need a stealth-browser
  module (`COMPANY_REGISTERS_BROWSER`). DE-Handelsregister also needs `pdftotext` (poppler).
