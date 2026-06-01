# Cross-cutting context: the Spanish legal system

Orchestrator cold-start for any plugin under `es/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law; the 1978 Constitution is supreme. Decentralised State of Autonomous Communities; several have their own foral/special civil law.

## Sources of law (by priority)

1. The Constitution and Constitutional Court (Tribunal Constitucional) jurisprudence.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Statutes (leyes orgánicas and leyes ordinarias); autonomous-community statutes within competence.
4. Regulations (reglamentos, reales decretos).
5. Case law (jurisprudencia) of the Tribunal Supremo — doctrine settled by repeated rulings.

## Codes

Core codes: Código Civil, Código Penal, Ley de Enjuiciamiento Civil (LEC), Ley de Enjuiciamiento Criminal (LECrim), Código de Comercio.

## Language

Statutes, decisions, and official documents are in Spanish (Castilian); co-official languages apply in some communities.

## Citation discipline (mandatory for every plugin under `es/`)

- Statutes/codes: "art. 1902 del Código Civil".
- Supreme Court: "STS [number]/[year]"; Constitutional Court: "STC [number]/[year]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
