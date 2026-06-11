# Practice profile: Immigration — Poland

Orchestrator cold-start for plugin `pl-immigration`. Loaded after `pl/CLAUDE.md`, before invoking a specific skill.

## Scope

Residence, work, and citizenship procedures for foreigners (cudzoziemcy):

- **`applying-cudzoziemcy-procedures`** — pobyt czasowy, pobyt stały, długoterminowy rezydent UE, zezwolenie na pracę (typy A–E), oświadczenie o powierzeniu pracy, and obywatelstwo (nadanie przez Prezydenta / uznanie przez wojewodę): documents, biometrics, deadlines, and the appeal path.

## Forums & authorities

The wojewoda (first instance for most residence/work permits), the **Szef Urzędu do Spraw Cudzoziemców (UdSC)** on administrative appeal, and on judicial review the administrative courts (**WSA → NSA**). Citizenship by nadanie is decided by the President; by uznanie, by the wojewoda.

## Key sources of law

Within Poland: ustawa o cudzoziemcach (residence/work — verify the current article numbering at runtime), ustawa o obywatelstwie polskim z 02.04.2009, and the implementing regulations. EU long-term-residence and free-movement rules apply where relevant. For the sources-of-law hierarchy and working language, see `pl/CLAUDE.md`.

## Citation discipline

Follow the rules in `pl/CLAUDE.md`. **Never invent** article numbers, fees, or deadlines — the skill verifies current values before relying on them.

## When this plugin does NOT apply

- Civil-status acts (birth, marriage, name change, transcription) → `family` (USC procedures).
- Choosing which request/appeal regime applies → `administrative`.
- Court challenge beyond the administrative-court route → `litigation`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
