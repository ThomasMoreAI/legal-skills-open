# Cross-cutting context: the Chinese legal system

Orchestrator cold-start for any plugin under `cn/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Socialist legal system with civil-law characteristics; the Constitution is supreme and the National People's Congress (NPC) is the highest legislative organ. Court decisions are not formally binding precedent, but the Supreme People's Court (SPC) issues binding judicial interpretations and publishes guiding cases (指导性案例) to be followed for reference.

## Sources of law (by priority)

1. The Constitution.
2. Basic laws of the NPC and laws of its Standing Committee.
3. Administrative regulations of the State Council; local regulations.
4. Judicial interpretations of the Supreme People's Court (binding on courts).
5. SPC guiding cases (referential).

## Codes

Core laws: the Civil Code of the PRC (2021), the Criminal Law, the Civil Procedure Law, the Company Law.

## Language

Statutes, decisions, and official documents are in (Simplified) Chinese.

## Citation discipline (mandatory for every plugin under `cn/`)

- Statutes/codes: "Article 1165 of the Civil Code of the PRC".
- SPC: cite the judicial interpretation or guiding-case number.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
