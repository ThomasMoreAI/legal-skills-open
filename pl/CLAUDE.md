# Cross-cutting context: the Polish legal system

Orchestrator cold-start for any plugin under `pl/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law; the 1997 Constitution is supreme. Unitary state.

## Sources of law (by priority)

1. The Constitution and Constitutional Tribunal (Trybunał Konstytucyjny) jurisprudence.
2. Ratified international treaties and EU law (primacy under CJEU jurisprudence).
3. Statutes (ustawy).
4. Regulations (rozporządzenia).
5. Case law of the Supreme Court (Sąd Najwyższy) and Supreme Administrative Court (NSA).

## Codes

Core codes: Kodeks cywilny (k.c.), Kodeks postępowania cywilnego (k.p.c.), Kodeks karny (k.k.), Kodeks spółek handlowych (k.s.h.).

## Language

Statutes, decisions, and official documents are in Polish. Court fees: opłata sądowa.

## Citation discipline (mandatory for every plugin under `pl/`)

- Statutes/codes: "art. 415 Kodeksu cywilnego" / "art. 415 k.c.".
- Supreme Court: "[chamber] [signature, e.g. III CZP 1/20]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
