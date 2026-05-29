# Cross-cutting context: the Argentine legal system

Orchestrator cold-start for any plugin under `ar/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law tradition. Federal republic: nation (Estado Federal), 23 provinces, and the
Autonomous City of Buenos Aires (CABA). Substantive civil and commercial law is unified
nationally (since the Código Civil y Comercial of 2015) but applied through both federal
and provincial courts; procedure is mostly federal at the federal level and provincial in
the provinces.

## Sources of law (by priority)

1. National Constitution (Constitución Nacional); international human-rights treaties
   granted constitutional rank under Art. 75(22).
2. Other international treaties ratified by Argentina (supra-legal).
3. National laws (`leyes nacionales`) and codes — Código Civil y Comercial, Código Penal, etc.
4. Presidential decrees and regulations.
5. Provincial constitutions, laws, and regulations.
6. Municipal ordinances.
7. Jurisprudence — Corte Suprema de Justicia de la Nación (CSJN); persuasive elsewhere,
   stronger where the CSJN has issued `doctrina obligatoria`.

## Language

Statutes, court filings, and government documents are in Spanish. Foreign-language
documents typically require a sworn translation (`traducción pública`) by a
`traductor público matriculado` to be admitted.

## Citation discipline (mandatory for every plugin under `ar/`)

- Statutes: "Ley N° 27.401, art. X"; codes: "art. X CCyCN" (Código Civil y Comercial).
- Cases: court, parties, date, collection — e.g., "CSJN, 'Halabi, Ernesto c. PEN',
  24/02/2009, Fallos 332:111".
- **Never invent** statute numbers, case names, or article numbers. If the exact
  reference is unknown, say so and prompt the user to verify the current edition.

## Working with current law

Laws and jurisprudence change. A skill that relies on a specific rule must state the
version/date it assumes and warn the user to confirm it is still in force.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
