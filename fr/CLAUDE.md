# Cross-cutting context: the French legal system

Orchestrator cold-start for any plugin under `fr/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law tradition with comprehensive codification (Napoleonic origin). Unitary republic.
The judiciary is split into two parallel orders — judicial (`ordre judiciaire`) for civil
and criminal matters, and administrative (`ordre administratif`) — each with its own apex
court.

## Sources of law (by priority)

1. The `bloc de constitutionnalité` — Constitution of 1958, its Preamble, the 1789
   Declaration of the Rights of Man and of the Citizen, the Preamble to the 1946
   Constitution, and the fundamental principles to which the Preamble refers; Constitutional
   Council jurisprudence.
2. International treaties (primacy over domestic statutes per Art. 55 Cst.); EU law
   (primacy under CJEU jurisprudence).
3. Lois (statutes of Parliament); ordonnances (delegated legislation).
4. Décrets and arrêtés (executive regulations).
5. Jurisprudence — particularly the Cour de cassation (judicial order), the Conseil d'État
   (administrative order), and the Conseil constitutionnel.
6. Doctrine — persuasive only, but heavily relied upon.

## Codes

France relies on consolidated codes (Code civil, Code de commerce, Code de procédure civile,
Code pénal, Code de procédure pénale, Code monétaire et financier, Code de la consommation,
and many sectoral codes). When a provision is codified, cite the relevant code rather than
the underlying statute.

## Language

Statutes, court decisions, and official documents are in French. Foreign-language documents
typically require a sworn translation (`traduction assermentée`) to be admitted before
courts.

## Citation discipline (mandatory for every plugin under `fr/`)

- Statutes/codes: "Article 1240 du Code civil"; abbreviation: "art. 1240 C. civ.".
- Cour de cassation: "Cass. civ. 1re, [date], n° N° de pourvoi" — always specify the
  chamber (civ. 1re/2e/3e, com., soc., crim.).
- Conseil d'État: "CE, [date], [case ref], n° N°".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

French codes are amended frequently. Skills depending on a specific rule must state the
assumed version/date and warn the user to confirm currency.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
