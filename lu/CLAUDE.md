# Cross-cutting context: the Luxembourg legal system

Orchestrator cold-start for any plugin under `lu/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law of the Napoleonic tradition, close to Belgian and French law. Constitutional monarchy; the Cour de cassation heads the judicial order and the Cour administrative the administrative order.

## Sources of law (by priority)

1. The Constitution and Constitutional Court jurisprudence.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Statutes (lois) and grand-ducal regulations.
4. Case law of the Cour de cassation and Cour administrative.

## Codes

Core codes: Code civil, Code de commerce, and procedural codes (Napoleonic lineage).

## Language

Legislation is published mainly in French; French, German, and Luxembourgish are administrative languages.

## Citation discipline (mandatory for every plugin under `lu/`)

- Statutes/codes: "art. [N] du Code civil"; "loi du [date]".
- Cases: by the issuing court, date, and docket number.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
