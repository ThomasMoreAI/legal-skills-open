# Cross-cutting context: the Azerbaijani legal system

Orchestrator cold-start for any plugin under `az/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law tradition with post-Soviet codification, influenced by Germanic and French models.
Unitary republic. Constitutional supremacy, with primacy for ratified international treaties
in their domain.

## Sources of law (by priority)

1. Constitution of the Republic of Azerbaijan (1995, as amended); ratified international treaties.
2. Constitutional laws.
3. Ordinary laws (`qanunlar`) — Acts of the Milli Majlis.
4. Presidential decrees and orders.
5. Cabinet of Ministers regulations.
6. Sectoral agency rules (e.g., State Service for Personal Data Protection issuances).
7. Plenum interpretations of the Supreme Court (`Ali Məhkəmə`) — guidance on uniform application.

## Language

Statutes, court filings, and government documents are in Azerbaijani (Latin script).
Documents in other languages typically require a notarized translation for use before
courts and agencies.

## Citation discipline (mandatory for every plugin under `az/`)

- Statutes: "Law of the Republic of Azerbaijan No. 998-IIIQ on Personal Data, Art. X"
  (or the Azerbaijani-language form).
- Decrees: "Presidential Decree No. ... dated ..."; "Cabinet of Ministers Decision No. ...".
- **Never invent** statute numbers, decree numbers, or article references. If unknown,
  say so and prompt the user to verify.

## Working with current law

Azerbaijani statutes are amended frequently and several regulatory regimes are still
evolving. Skills relying on a specific rule must state the assumed version/date and warn
the user to confirm currency.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
