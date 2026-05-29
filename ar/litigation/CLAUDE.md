# Practice profile: Civil & Commercial Litigation — Argentina

Orchestrator cold-start for plugin `ar-litigation`. Loaded after `ar/CLAUDE.md`, before
invoking a specific skill.

## Scope

Civil and commercial proceedings before Argentine courts (national and provincial),
including the path of cases to the Supreme Court (CSJN) and analysis of constitutional
review (recurso extraordinario federal, recurso de queja).

## Forums & authorities

- Federal judiciary: federal trial courts (`juzgados federales`), federal appellate courts
  (`cámaras federales`), and the Corte Suprema de Justicia de la Nación (CSJN).
- National civil and commercial courts in CABA.
- Provincial courts, each under the procedural code of its province.
- The Federal Prosecutor's Office (`Ministerio Público Fiscal`) for matters with public
  interest.

## Key sources of law

- Código Procesal Civil y Comercial de la Nación (CPCCN) — federal civil/commercial procedure.
- Provincial procedural codes (`Códigos Procesales Civiles y Comerciales provinciales`) — vary by province.
- Código Civil y Comercial de la Nación (CCyCN, in force since 2015) — substantive civil/commercial.
- Constitución Nacional and the precedents of the CSJN published in `Fallos`.

## Citation discipline

Follow the AR rules in `ar/CLAUDE.md`. Always identify which procedural code is being applied
(federal vs. the specific province). For CSJN decisions, prefer the `Fallos` collection
citation. **Never invent** docket numbers, case names, or article numbers.

## When this plugin does NOT apply

- Arbitral proceedings → use `general/arbitration` (or a dedicated `ar-arbitration` plugin if
  added).
- Administrative/regulatory disputes before agencies → out of scope for this plugin.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
