# Cross-cutting context: the Singaporean legal system

Orchestrator cold-start for any plugin under `sg/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Common law received from England, with local statutory development; the Constitution is supreme. Binding precedent. The Court of Appeal is the apex court.

## Sources of law (by priority)

1. The Constitution of the Republic of Singapore.
2. Acts of Parliament.
3. Subsidiary legislation.
4. Case law of the Court of Appeal and High Court (binding precedent).

## Language

Legislation and judgments are in English.

## Citation discipline (mandatory for every plugin under `sg/`)

- Statutes: "s 73 of the Penal Code 1871".
- Cases: neutral citation "[2020] SGCA 1" / "[2020] SGHC 1".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
