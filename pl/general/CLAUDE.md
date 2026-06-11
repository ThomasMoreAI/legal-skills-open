# Practice profile: General / Legal Research — Poland

Orchestrator cold-start for plugin `pl-general`. Loaded after `pl/CLAUDE.md`, before invoking a specific skill.

## Scope

Cross-cutting research utilities that serve every substantive area rather than one of them:

- **`citing-polish-law`** — formatting citations to legislation, court rulings, Constitutional Tribunal decisions, EU law, and international human-rights judgments in a consistent style (article/paragraph/point, act name, redaction date, source URL).
- **`fetching-isap-sejm`** — retrieving statute text and historical redactions from the official portal, working with consolidated texts (tekst jednolity), and building URLs from document identifiers.

## Forums & authorities

Not court-bound — these skills support work across any practice. Authoritative sources: **ISAP (`isap.sejm.gov.pl`)** and the **Dziennik Ustaw (`dziennikustaw.gov.pl`)** for statute text and official publication; **Monitor Polski** for official notices; **EUR-Lex** for EU acts (which take primacy over national law under CJEU jurisprudence).

## Key sources of law

Spans the whole legal system. The codes index used by the fetch skill (verify the current tekst jednolity at runtime) includes Konstytucja RP (Dz.U. 1997 nr 78 poz. 483), k.c. (Dz.U. 1964 nr 16 poz. 93), k.p.c. (Dz.U. 1964 nr 43 poz. 296), k.k., k.p.k., Kodeks pracy, KPA, PPSA, k.s.h., and Ordynacja podatkowa. For the sources-of-law hierarchy and working language, see `pl/CLAUDE.md`.

## Citation discipline

Follow the rules in `pl/CLAUDE.md`; the `citing-polish-law` skill carries the detailed format. **Never invent** article numbers, case signatures, Dz.U. references, or redaction dates — confirm the current version before relying on a reference.

## When this plugin does NOT apply

- Substantive analysis of a specific dispute or transaction → the relevant practice plugin (`litigation`, `arbitration`, `tax`, `data-protection`, …).

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
