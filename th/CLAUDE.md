# Cross-cutting context: the Thai legal system

Orchestrator cold-start for any plugin under `th/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law; the Civil and Commercial Code is the backbone of private law. Constitutional monarchy; the Supreme Court (Dika), Constitutional Court, and Administrative Court head their respective jurisdictions.

## Sources of law (by priority)

1. The Constitution and Constitutional Court rulings.
2. Statutes (Acts) and emergency/royal decrees.
3. Ministerial regulations and notifications.
4. Case law of the Supreme Court (Dika) — persuasive.

## Codes

Core codes: the Civil and Commercial Code, the Penal Code, the Civil Procedure Code.

## Language

Statutes, decisions, and official documents are in Thai.

## Citation discipline (mandatory for every plugin under `th/`)

- Statutes/codes: "Section 420 of the Civil and Commercial Code".
- Supreme Court: by Dika judgment number and year.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
