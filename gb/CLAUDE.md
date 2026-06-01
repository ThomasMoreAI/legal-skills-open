# Cross-cutting context: the United Kingdom legal system

Orchestrator cold-start for any plugin under `gb/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Common law. No single codified constitution; Parliament is sovereign. Three legal systems — England & Wales, Scotland (mixed civil/common), and Northern Ireland. Binding precedent (stare decisis).

## Sources of law (by priority)

1. Acts of Parliament (primary legislation); the principle of parliamentary sovereignty.
2. Retained/assimilated EU law (as amended post-Brexit).
3. Statutory instruments (secondary legislation).
4. Case law of the UK Supreme Court and senior courts (binding precedent).
5. Royal prerogative and constitutional conventions.

## Language

Legislation and judgments are in English (also Welsh for Welsh legislation).

## Citation discipline (mandatory for every plugin under `gb/`)

- Statutes: "s 2 of the Theft Act 1968".
- Cases: "Donoghue v Stevenson [1932] AC 562"; neutral citation "[2020] UKSC 1". Follow OSCOLA.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
