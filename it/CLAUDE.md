# Cross-cutting context: the Italian legal system

Orchestrator cold-start for any plugin under `it/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law; the 1948 Constitution is rigid and supreme. Unitary state with constitutional review by the Corte costituzionale.

## Sources of law (by priority)

1. The Constitution and Constitutional Court (Corte costituzionale) jurisprudence.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Statutes (leggi) and acts having force of law (decreti legge, decreti legislativi).
4. Regulations (regolamenti).
5. Case law of the Corte di Cassazione (civil/criminal) and Consiglio di Stato (administrative).

## Codes

Core codes: Codice civile, Codice penale, Codice di procedura civile (c.p.c.), Codice di procedura penale (c.p.p.).

## Language

Statutes, decisions, and official documents are in Italian.

## Citation discipline (mandatory for every plugin under `it/`)

- Statutes/codes: "art. 2043 c.c.".
- Court of Cassation: "Cass. civ., sez. [..], [date], n. [number]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
