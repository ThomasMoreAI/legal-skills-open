# Cross-cutting context: the UAE legal system

Orchestrator cold-start for any plugin under `ae/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law (Egyptian/French-influenced) federal system, with Islamic law (Sharia) informing personal-status and some other matters. The financial free zones DIFC and ADGM operate their own common-law systems and courts.

## Sources of law (by priority)

1. The Federal Constitution.
2. Federal laws and decree-laws; emirate-level legislation.
3. Implementing regulations and Cabinet/ministerial decisions.
4. Islamic law (Sharia), especially for personal status.
5. Within DIFC/ADGM: their own statutes and common-law court judgments.

## Codes

Key instruments: the Federal Civil Transactions Law, the Commercial Transactions Law, the Penal Code, and the Companies Law (cite the federal law/decree-law by number).

## Language

Federal legislation is in Arabic (the authoritative text); DIFC/ADGM operate in English.

## Citation discipline (mandatory for every plugin under `ae/`)

- Statutes: "Federal Decree-Law No. [N] of [year]", article number.
- DIFC/ADGM cases: by the court's own neutral citation.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
