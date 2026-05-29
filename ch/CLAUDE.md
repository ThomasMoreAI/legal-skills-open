# Cross-cutting context: the Swiss legal system

Orchestrator cold-start for any plugin under `ch/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law tradition, codified federally with substantial cantonal autonomy. Federal state
(Confédération suisse / Schweizerische Eidgenossenschaft) with 26 cantons. Most private-law
and criminal law is federal; procedure has been federalized since 2011 (CPC, CPP), while
cantons retain organization of courts and certain administrative areas.

## Sources of law (by priority)

1. Federal Constitution (`Cst.` / `BV`); ratified international treaties.
2. Federal laws — published in the Systematische Sammlung des Bundesrechts (SR / RS).
   Major codes: Code civil (CC / ZGB), Code des obligations (CO / OR), Code pénal
   (CP / StGB), Code de procédure civile (CPC / ZPO), Code de procédure pénale
   (CPP / StPO).
3. Federal ordinances (`ordonnances` / `Verordnungen`).
4. Cantonal constitutions, laws, and ordinances.
5. Communal regulations.
6. Federal Supreme Court (`Tribunal fédéral` / `Bundesgericht` / `Tribunale federale`)
   jurisprudence — published in the `ATF` / `BGE` collection; not formally binding but
   strongly authoritative.

## Languages

Switzerland has four national languages. Federal statutes and decisions are official in
German, French, and Italian (all three texts equally authentic). Use the language version
that matches the user's working language; flag when texts differ.

## Citation discipline (mandatory for every plugin under `ch/`)

- Statutes: "Art. X CC", "Art. X CO" (or the German/Italian equivalents: ZGB / OR / StGB).
- Federal Supreme Court decisions: "BGE 140 III 264" / "ATF 140 III 264"
  (volume, part, page); recent unpublished: "TF, [date], [case ref]".
- **Never invent** article numbers, case references, or BGE/ATF citations. If unknown,
  say so explicitly.

## Working with current law

Federal law is stable but cantonal law varies widely. A skill that depends on cantonal
rules must say which canton it assumes; federal-law skills must state the assumed
version/date.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
