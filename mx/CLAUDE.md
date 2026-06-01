# Cross-cutting context: the Mexican legal system

Orchestrator cold-start for any plugin under `mx/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law, federal; the 1917 Constitution is supreme. Federal and state civil codes coexist. Settled case law (jurisprudencia) of the federal courts is binding.

## Sources of law (by priority)

1. The 1917 Constitution and human-rights treaties (bloque de constitucionalidad).
2. Federal statutes and state statutes (per the division of powers).
3. Regulations (reglamentos).
4. Jurisprudencia of the Suprema Corte de Justicia de la Nación (SCJN) and collegiate circuit courts (binding when established).

## Codes

Core codes: Código Civil Federal and state civil codes, Código Penal, codes of civil/criminal procedure.

## Language

Statutes, decisions, and official documents are in Spanish.

## Citation discipline (mandatory for every plugin under `mx/`)

- Statutes/codes: "artículo 1910 del Código Civil Federal".
- Case law: cite the tesis/jurisprudencia registry number (e.g. "Tesis: 1a./J. 1/2020").
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
