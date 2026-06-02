# Cross-cutting context: the Australian legal system

Orchestrator cold-start for any plugin under `au/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Common law federation under a written Constitution. Commonwealth and six states/territories; binding precedent. The High Court of Australia is the apex court.

## Sources of law (by priority)

1. The Commonwealth Constitution.
2. Commonwealth statutes (within enumerated powers) and state/territory statutes.
3. Delegated legislation (regulations).
4. Case law of the High Court of Australia and intermediate appellate courts (binding precedent).

## Language

Legislation and judgments are in English.

## Citation discipline (mandatory for every plugin under `au/`)

- Statutes: "s 51 of the Constitution"; "s 18 of the Australian Consumer Law".
- Cases: "Mabo v Queensland (No 2) (1992) 175 CLR 1"; medium-neutral "[2020] HCA 1". Follow AGLC.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
