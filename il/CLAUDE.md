# Cross-cutting context: the Israeli legal system

Orchestrator cold-start for any plugin under `il/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Mixed system: an English common-law heritage overlaid with civil-law-style codification and religious law for personal status. Binding precedent (Supreme Court decisions bind lower courts). Basic Laws serve a constitutional function.

## Sources of law (by priority)

1. The Basic Laws (constitutional) and Supreme Court jurisprudence.
2. Statutes of the Knesset.
3. Regulations (takkanot).
4. Case law of the Supreme Court (which also sits as the High Court of Justice) — binding.
5. Religious law for personal-status matters.

## Language

Legislation and judgments are in Hebrew (Arabic has special status).

## Citation discipline (mandatory for every plugin under `il/`)

- Statutes: by name and year (e.g. "Contracts (General Part) Law, 1973"), section.
- Cases: "CA [number]/[year]"; "HCJ [number]/[year]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
