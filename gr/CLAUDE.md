# Cross-cutting context: the Greek legal system

Orchestrator cold-start for any plugin under `gr/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law; the Constitution is supreme. Unitary state with three apex jurisdictions.

## Sources of law (by priority)

1. The Constitution.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Statutes (nómoi).
4. Presidential decrees and regulatory acts.
5. Case law of the Areios Pagos (civil/criminal), Council of State (administrative), and Court of Audit.

## Codes

Core codes: the Civil Code (Astikós Kódikas), Penal Code, Code of Civil Procedure.

## Language

Statutes, decisions, and official documents are in Greek.

## Citation discipline (mandatory for every plugin under `gr/`)

- Statutes/codes: "Article 281 of the Civil Code".
- Areios Pagos: "AP [number]/[year]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
