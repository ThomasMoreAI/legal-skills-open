# Cross-cutting context: the South Korean legal system

Orchestrator cold-start for any plugin under `kr/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law (German-influenced) under the Constitution of the Republic of Korea. Unitary state; the Supreme Court is the apex court and a separate Constitutional Court handles constitutional review.

## Sources of law (by priority)

1. The Constitution and Constitutional Court decisions.
2. Treaties.
3. Statutes enacted by the National Assembly.
4. Presidential decrees and ministerial ordinances.
5. Case law of the Supreme Court — highly persuasive.

## Codes

Core codes: Civil Act, Commercial Act, Criminal Act, Civil Procedure Act.

## Language

Statutes, decisions, and official documents are in Korean.

## Citation discipline (mandatory for every plugin under `kr/`)

- Statutes/codes: "Article 750 of the Civil Act".
- Supreme Court: by case number (e.g. "2018Da12345").
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
