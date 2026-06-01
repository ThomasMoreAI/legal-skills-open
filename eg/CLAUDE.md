# Cross-cutting context: the Egyptian legal system

Orchestrator cold-start for any plugin under `eg/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law (French-influenced); Islamic law (Sharia) is, under the Constitution, the principal source of legislation and governs personal status. The Court of Cassation and the Supreme Constitutional Court are apex courts.

## Sources of law (by priority)

1. The Constitution and Supreme Constitutional Court jurisprudence.
2. Statutes (qawanin) enacted by Parliament.
3. Presidential and ministerial regulations.
4. Islamic law (Sharia), especially for personal status.
5. Case law of the Court of Cassation — persuasive.

## Codes

Core codes: the Civil Code (Law No. 131 of 1948), the Penal Code, codes of civil/criminal procedure.

## Language

Statutes, decisions, and official documents are in Arabic.

## Citation discipline (mandatory for every plugin under `eg/`)

- Statutes/codes: "Article [N] of the Civil Code (Law No. 131 of 1948)".
- Statutes by number: "Law No. [N] of [year]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
