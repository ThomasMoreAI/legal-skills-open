# Cross-cutting context: the legal system of Denmark

Orchestrator cold-start for any plugin under `dk/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Nordic (Scandinavian) civil law tradition; less codified than continental systems, with strong reliance on statute and preparatory works (forarbejder). EU member state.

## Courts

Supreme Court (Højesteret); High Courts (Østre and Vestre Landsret); district courts (byretter).

## Core sources

Statutes (love) and executive orders (bekendtgørelser); EU law applies directly or via implementation. Official publication: Lovtidende; consolidated law at retsinformation.dk.

## Language

Danish.

## Citation discipline (mandatory for every plugin under `dk/`)

- Cite statutes by their official title, number, and date, and the article; cite cases by
  court, date, and docket or reference number.
- **Never invent** article numbers, case names, or references. If unknown, say so and ask
  the user to verify against the official publication.

## Working with current law

Statutes and regulations are amended frequently. A skill that depends on a specific rule
must state the assumed version or date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
