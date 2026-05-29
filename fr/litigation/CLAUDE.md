# Practice profile: Civil Litigation — France

Orchestrator cold-start for plugin `fr-litigation`. Loaded after `fr/CLAUDE.md`, before
invoking a specific skill.

## Scope

Civil proceedings before the courts of the judicial order: drafting submissions,
structuring legal reasoning (notably the judicial syllogism), and producing motivated
decisions.

## Forums & authorities

- First instance: `Tribunal judiciaire` (TJ) and specialized courts (`Tribunal de
  commerce`, `Conseil de prud'hommes`).
- Appeal: `Cours d'appel`.
- Final review: `Cour de cassation` (`chambres civiles`, `commerciale`, `sociale`,
  `criminelle`) — controls legality, does not re-examine facts.
- Administrative litigation (TA / CAA / Conseil d'État) is a separate jurisdiction and
  out of scope here.

## Key sources of law

- Code de procédure civile (CPC) — procedure.
- Code civil (C. civ.) — substantive civil law.
- Code de l'organisation judiciaire (COJ).
- ENM / Cour de cassation methodological guidance (e.g., the "Fiches méthodologiques de
  rédaction du jugement civil") for drafting judicial decisions.

## Citation discipline

Follow `fr/CLAUDE.md`. Distinguish chambers when citing Cass.; cite `n° de pourvoi`. For
procedural references, cite the CPC article. **Never invent** article numbers, case names,
or `n° de pourvoi`.

## When this plugin does NOT apply

- Criminal proceedings → out of scope (a `fr-criminal` plugin if created).
- Administrative disputes (TA / CAA / Conseil d'État) → out of scope.
- Labour disputes before `Conseil de prud'hommes` may need a `fr-employment` plugin when
  added.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
