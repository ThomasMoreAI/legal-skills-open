# Cross-cutting context: the Brazilian legal system

Orchestrator cold-start for any plugin under `br/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law, codified; the 1988 Federal Constitution is supreme and detailed. Federal republic; binding precedent exists in limited form (súmulas vinculantes of the STF).

## Sources of law (by priority)

1. The Federal Constitution of 1988 and Supremo Tribunal Federal (STF) jurisprudence.
2. International treaties (human-rights treaties may have constitutional/supra-legal status).
3. Federal statutes (leis); state and municipal laws within competence.
4. Decrees and regulatory acts.
5. Case law of the STF and Superior Tribunal de Justiça (STJ); binding súmulas.

## Codes

Core codes: Código Civil (Lei nº 10.406/2002), Código de Processo Civil, Código Penal, Consolidação das Leis do Trabalho (CLT).

## Language

Statutes, decisions, and official documents are in Portuguese.

## Citation discipline (mandatory for every plugin under `br/`)

- Statutes/codes: "art. 5º da Constituição Federal"; "art. 186 do Código Civil".
- Statutes by number: "Lei nº 10.406/2002".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
