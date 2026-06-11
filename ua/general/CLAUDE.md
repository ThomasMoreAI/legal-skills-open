# Practice profile: General / Legal Research — Ukraine

Orchestrator cold-start for plugin `ua-general`. Loaded after `ua/CLAUDE.md`, before invoking a specific skill.

## Scope

Cross-cutting research utilities that serve every substantive area rather than one of them:

- **`citing-ukrainian-law`** — formatting citations to legislation, court rulings, and Constitutional Court decisions in a consistent style (act type, article/part/point, redaction date, source URL), with the standard NPA abbreviations (КУ, ЦК, ЦПК, ГК, ГПК, КАС, КК, КПК, КЗпП, КУпАП, СК, ПК, ЗК, БК, ЖК).
- **`fetching-zakon-rada`** — retrieving statute text and historical redactions from the official portal, building URLs from `zakon.rada` identifiers, and checking the current validity of a norm.
- **`checking-martial-law-overrides`** — determining whether a default norm is modified, suspended, or adjusted under martial law (procedural deadlines, limitation periods, registration actions, labour/property relations, jurisdiction, mobilisation).

## Forums & authorities

Not court-bound — these skills support work across any practice. The authoritative source for statute text and redactions is the official portal **`zakon.rada.gov.ua`**; for case law, the **Unified State Register of Court Decisions (ЄДРСР, `reyestr.court.gov.ua`)**.

## Key sources of law

Used by the skills (verify the current redaction at runtime via the fetch skill — IDs are `zakon.rada` identifiers, not citations):

- **Codes:** Конституція (`254к/96-вр`), ЦК (`435-15`), ЦПК (`1618-15`), ГК (`436-15`), ГПК (`1798-12`), КАС (`2747-15`), КК (`2341-14`), КПК (`4651-17`), КЗпП (`322-08`), СК (`2947-14`), ПК (`2755-17`), ЗК (`2768-14`).
- **Martial-law base:** ЗУ «Про правовий режим воєнного стану» (`389-19`), «Про оборону України» (`1932-12`), «Про мобілізаційну підготовку та мобілізацію» (`3543-12`), «Про організацію трудових відносин в умовах воєнного стану» (`2136-20`). Martial law runs in periods set by presidential decrees approved by statute — **always verify the period currently in force.**

## Citation discipline

Follow the rules in `ua/CLAUDE.md`; the `citing-ukrainian-law` skill carries the detailed format and abbreviations. **Never invent** article numbers, case names, redaction dates, or `zakon.rada` IDs — confirm the current version before relying on a reference.

## When this plugin does NOT apply

- Substantive analysis of a specific dispute or transaction → the relevant practice plugin (`litigation`, `arbitration`, `contracts`, `administrative`, `military`).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
