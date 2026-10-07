# Code des Sociétés Commerciales (CSC) — key articles for SUARL / SARL

## Legal framework

The **Code des Sociétés Commerciales** is governed by **Law no. 2000-93 of 3 November 2000**, amended several times. Full source: https://www.jurisitetunisie.com/tunisie/codes/csc/Menu.htm

[REQUIRES MANUAL LEGAL VERIFICATION: list every amendment after 2020, some are very recent — search JORT 2023–2026]

## CSC structure relevant to freelancers

| Book | Content | Indicative articles |
|---|---|---|
| Book I | General provisions | art. 1 – 19 |
| Book II | Limited liability companies (SARL, SUARL) | art. 90 – 159 |
| Book III | Joint-stock companies (SA) | art. 160 – 388 |
| Book IV | Limited partnerships | art. 389+ |
| Book V | Partnerships | art. 397+ |

> For a freelancer incorporating, Book II is the core. Articles **90–159** in particular.

## Key SUARL / SARL articles

[REQUIRES MANUAL LEGAL VERIFICATION: exact text of each article — confirm the wording in the official text]

### Art. 90–95: SARL general provisions

- Commercial form, number of shareholders (2–50 for SARL).
- Liability limited to contributions.
- Minimum capital [REQUIRES VERIFICATION: confirm 1 000 TND].

### Art. 96–100: incorporation

- Written articles of association mandatory.
- Mandatory mentions in the articles (name, registered office, object clause, capital, duration, etc.).
- JORT publication.

### Art. 101–115: contributions and capital

- Contributions in cash and in kind.
- Valuation of in-kind contributions.
- Share capital, shares, paid-in amount.

### Art. 116–127: management

- Appointment and removal of managers.
- Powers and limits.
- Civil and criminal liability of managers.

### Art. 128–138: shareholder decisions

- Ordinary (AGO) and extraordinary (AGE) general meetings.
- Required majorities.
- Minutes and registers.

### Art. 139–148: control, annual accounts

- Bookkeeping.
- Approval of accounts.
- Filing with the RNE.

### Art. 148–159: SUARL specifically

- Art. 148: SUARL definition (single shareholder).
- Art. 149–154: specific rules for the sole shareholder.
- Art. 155–159: SUARL ↔ SARL conversion.

## SUARL vs SARL — practical summary

| Criterion | SUARL | SARL |
|---|---|---|
| Number of shareholders | 1 | 2 – 50 |
| Minimum capital | 1 000 TND | 1 000 TND |
| Articles of association | Simpler | More complex (shareholder rules) |
| Decisions | By the sole shareholder (minute in the register) | AGO / AGE per CSC majorities |
| Share transfers | Not applicable (sole shareholder) | Transfer conditions in articles + approval |
| Conversion | SUARL → SARL automatic if a 2nd shareholder joins | Possible SA switch above thresholds |
| Manager liability | Articles 116–127 plus specific rules | Same |

## Which company form by profile

### Solo freelance dev, revenue < 100k TND/year
→ Usually **SUARL**, unless you stay on patente forfaitaire.

### Dev studio with 2–5 people, shared projects
→ **SARL** (allows share splits between partners).

### Fundraising planned / wide shareholder base
→ **SA** (but complexity ↑↑, mandatory account audit).

### Activity requiring unlimited liability (rare)
→ General partnership (not recommended for tech freelancers).

## Fully exporting companies — benefit regime

[src: tunisieindustrie.nat.tn — Investment Code, Law 2016-71]

A SUARL / SARL that makes **more than 70%** of its revenue from exports benefits from:
- **IS 0%** during the incentive period (duration to reconfirm against 2026 Finance Law).
- **VAT suspended** on local purchases and imports of equipment.
- **Specific CNSS benefits** (preferential rates possible).
- **Privileged customs regime** (temporary admission, etc.).

[REQUIRES MANUAL LEGAL VERIFICATION: 70% threshold + 2026 incentive-period duration — check 2026 Finance Law changes to the Investment Code]

## Articles to cite for standard SUARL clauses

For a minimal SUARL articles document, clauses should refer (among others) to:
- Art. 90–91 (form and liability)
- Art. 96 (mandatory mentions)
- Art. 148–149 (sole shareholder)
- Art. 116–118 (management)
- Art. 139 (annual accounts)

See the template in `statuts-suarl-clauses.md`.

## Sources

- `data/sources.json` → `code-societes-commerciales`, `code-incitations-investissement`
- `rne.md` (registration procedure)
- `statuts-suarl-clauses.md` (template)
