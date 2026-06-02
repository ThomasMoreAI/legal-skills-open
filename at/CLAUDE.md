# Cross-cutting context: the Austrian legal system

Orchestrator cold-start for any plugin under `at/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law, codified; the ABGB dates to 1811. Federal republic with a strong constitutional-review tradition.

## Sources of law (by priority)

1. The Federal Constitution (B-VG) and Constitutional Court (VfGH) jurisprudence.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Federal and Land statutes.
4. Ordinances (Verordnungen).
5. Case law of the OGH (civil/criminal), VwGH (administrative), VfGH (constitutional).

## Codes

Core codes: ABGB (civil), UGB (commercial), ZPO, StGB, StPO.

## Language

Statutes, decisions, and official documents are in German.

## Citation discipline (mandatory for every plugin under `at/`)

- Statutes/codes: "§ 1295 ABGB".
- Supreme Court: "OGH [date], [Geschäftszahl, e.g. 1 Ob 1/20x]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
