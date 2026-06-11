# Practice profile: Administrative & Public Services — Ukraine

Orchestrator cold-start for plugin `ua-administrative`. Loaded after `ua/CLAUDE.md`, before invoking a specific skill.

## Scope

Citizen-facing administrative procedures and public services, plus choosing the correct legal regime for communicating with authorities:

- **`applying-cnap-passport`** — ID-картка, закордонний паспорт, residence registration/de-registration at ЦНАП or ДП «Документ»: documents, fees, deadlines, appeal.
- **`applying-consular-procedures`** — consular procedures abroad (passport, свідоцтво на повернення, civil-status acts, apostille/legalisation, notarial acts, consular registration, military registration abroad).
- **`applying-servisnyi-centr-mvs`** — driver licences and vehicle registration at сервісні центри МВС (`hsc.gov.ua` / «Дія»).
- **`determining-ua-request-regime`** — routing a written document to the correct single regime (one document = one regime), preventing the mixing of access-to-information, citizens' appeals, administrative-procedure applications, advocate requests, personal-data requests, and complaints.

## Forums & authorities

Administrative-service providers: **ЦНАП, ДП «Документ», ДМС, СЦ МВС (`hsc.gov.ua`), consular institutions of the МЗС (`mfa.gov.ua`)**, and the «Дія» e-services portal. Refusals, silence, or unlawful inaction are challenged first by hierarchical/administrative complaint and then before the **administrative courts (КАС)** — see the `litigation` plugin for the court route.

## Key sources of law

Used by the skills (verify the current redaction at runtime — IDs are `zakon.rada` identifiers):

- **Request regimes:** ЗУ «Про доступ до публічної інформації» (`2939-17`), «Про звернення громадян» (`393/96-вр`), «Про адміністративну процедуру», «Про адміністративні послуги», «Про захист персональних даних», «Про адвокатуру та адвокатську діяльність» (`5076-17`, адвокатський запит).
- **Passports / ID:** ЗУ `5492-VI` (документи, що посвідчують особу) and the relevant Cabinet of Ministers resolutions per document type.
- **Consular:** ЗУ «Про дипломатичну службу» (`4059-12`), Консульський статут (Указ Президента `127/94`), Віденська конвенція про консульські зносини 1963, Гаазька конвенція про апостиль 1961, наказ МЗС про консульські збори.

## Citation discipline

Follow the rules in `ua/CLAUDE.md`. **Never invent** statute/resolution numbers, fees, or deadlines — each skill verifies the current values against official sources (with a dated fallback) before relying on them.

## When this plugin does NOT apply

- Court challenge of a refusal (адмінпозов у КАС) → `litigation`.
- Drafting the substantive document itself (claim, complaint, contract) → the relevant practice plugin.
- Military registration disputes with the ТЦК → `military`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
