# Cross-cutting context: the Nigerian legal system

Orchestrator cold-start for any plugin under `ng/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Common law (English-derived), applied alongside customary law and, in northern states, Islamic (Sharia) law. Federal republic; the 1999 Constitution is supreme. The Supreme Court of Nigeria is the apex court.

## Sources of law (by priority)

1. The 1999 Constitution (as amended).
2. Federal Acts of the National Assembly and state laws.
3. Subsidiary legislation.
4. Received English law and case law of the Supreme Court and Court of Appeal.
5. Customary and Islamic law within their spheres.

## Language

Legislation and judgments are in English.

## Citation discipline (mandatory for every plugin under `ng/`)

- Statutes: "s 36 of the 1999 Constitution".
- Cases: law reports such as "(2002) 9 NWLR (Pt 772) 222".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
