# Cross-cutting context: the Turkish legal system

Orchestrator cold-start for any plugin under `tr/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law, received from the Swiss/German tradition (the Civil Code and Code of Obligations are adapted from Swiss law). The Constitution is supreme.

## Sources of law (by priority)

1. The Constitution and Constitutional Court (Anayasa Mahkemesi) jurisprudence.
2. International treaties (prevail over statutes on fundamental rights, Art. 90).
3. Statutes (kanun).
4. Presidential decrees and regulations (yönetmelik).
5. Case law of the Court of Cassation (Yargıtay) and Council of State (Danıştay).

## Codes

Core codes: Türk Medeni Kanunu (Civil Code), Türk Borçlar Kanunu (Obligations), Türk Ticaret Kanunu (Commercial), Türk Ceza Kanunu (Criminal).

## Language

Statutes, decisions, and official documents are in Turkish.

## Citation discipline (mandatory for every plugin under `tr/`)

- Statutes/codes: "Article 6 of the Turkish Civil Code (TMK)".
- Court of Cassation: "Yargıtay [chamber] [date], E. [.]/K. [.]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
