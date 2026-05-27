# Cross-cutting context: the United States legal system

Orchestrator cold-start for any plugin under `us/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Common law (federal plus the 50 states, D.C., and territories). Binding precedent (stare decisis);
statutes and regulations are interpreted against the case law. Federal and state systems are parallel —
always identify which one governs.

## Sources of law (by priority)

1. U.S. Constitution; treaties.
2. Federal statutes (U.S. Code) and the Code of Federal Regulations (CFR).
3. Federal case law (Supreme Court → Courts of Appeals → District Courts).
4. State constitutions, statutes, regulations, and case law.
5. Local ordinances.

## Language

Court filings and legal references are in English. Foreign-language documents generally require a
certified translation for use in a U.S. court or agency.

## Citation discipline (mandatory for every plugin under `us/`)

- Statutes: title, code, section — e.g. "42 U.S.C. § 12112"; regulations — "29 C.F.R. § 1630.2".
- Cases: name, reporter, court, year — e.g. "Hertz Corp. v. Friend, 559 U.S. 77 (2010)".
- Follow Bluebook form. **Never invent** citations, case numbers, or section numbers. If the exact
  reference is unknown, say so and prompt the user to verify the current edition.

## Working with current law

Statutes, regulations, and controlling precedent change. A skill that relies on a specific rule must
state the version/date it assumes and warn the user to confirm it is still current — federal vs. state
and circuit splits can change the answer.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
