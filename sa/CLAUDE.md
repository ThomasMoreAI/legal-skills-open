# Cross-cutting context: the Saudi Arabian legal system

Orchestrator cold-start for any plugin under `sa/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Islamic law (Sharia) is the primary source of law; the State enacts regulations (anẓima) by royal decree that must not conflict with Sharia. Recent reforms have codified key areas (e.g. the Civil Transactions Law of 2023).

## Sources of law (by priority)

1. Sharia (the Qur'an and Sunna) as the supreme source.
2. The Basic Law of Governance.
3. Regulations (niẓam) enacted by royal decree; implementing regulations.
4. Decisions of the courts and the Board of Grievances (administrative).

## Codes

Codified instruments include the Civil Transactions Law (2023) and the Companies Law; much substantive law remains Sharia-based.

## Language

Legislation, decisions, and official documents are in Arabic.

## Citation discipline (mandatory for every plugin under `sa/`)

- Regulations: "Royal Decree No. [M/N] dated [Hijri date]", article number.
- Anchor each claim to a specific niẓam article or recognised Sharia source.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
