# Cross-cutting context: the South African legal system

Orchestrator cold-start for any plugin under `za/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Mixed legal system: Roman-Dutch civil law fused with English common law, under a supreme 1996 Constitution with a justiciable Bill of Rights. Binding precedent.

## Sources of law (by priority)

1. The 1996 Constitution (supreme law) and Constitutional Court jurisprudence.
2. Statutes of Parliament and provincial legislation.
3. Subordinate legislation.
4. Common law (Roman-Dutch) and case law of the Constitutional Court and Supreme Court of Appeal.
5. Customary law (recognised, subject to the Constitution).

## Language

Legislation and judgments are in English (one of 11 official languages). Data protection is governed by POPIA (Act No. 4 of 2013).

## Citation discipline (mandatory for every plugin under `za/`)

- Statutes: "s 9 of the Constitution"; "s 11 of POPIA".
- Cases: "[party] YYYY (vol) SA [page] ([court])".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
