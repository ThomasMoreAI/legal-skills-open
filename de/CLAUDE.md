# Cross-cutting context: the German legal system

Orchestrator cold-start for any plugin under `de/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law, comprehensively codified. Federal republic; the Basic Law (Grundgesetz) is supreme. No binding precedent doctrine, but decisions of the Federal Constitutional Court bind all organs, and apex-court case law is followed in practice.

## Sources of law (by priority)

1. The Basic Law (Grundgesetz, GG) and Federal Constitutional Court (BVerfG) jurisprudence.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Federal statutes (Bundesgesetze) and the codes.
4. Statutory instruments (Rechtsverordnungen) and by-laws (Satzungen).
5. Land (state) constitutions and statutes.
6. Case law of the federal apex courts (BGH, BVerwG, BFH, BAG, BSG) — persuasive, highly followed.

## Codes

Core codes: BGB (civil), HGB (commercial), ZPO (civil procedure), StGB and StPO (criminal), plus GmbHG, AktG, InsO, and many sectoral statutes. Cite the code where a provision is codified.

## Language

Statutes, decisions, and official documents are in German.

## Citation discipline (mandatory for every plugin under `de/`)

- Statutes/codes: "§ 433 BGB", "§ 823 Abs. 1 BGB".
- Federal Court of Justice: "BGH, Urteil v. [date] – [Az., e.g. VIII ZR 1/20]".
- Constitutional Court: "BVerfGE [vol], [page]".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
