# Statutory Duplication — Reference

Loaded when the audit reaches Step 7. Detects passages that restate applicable statute without adding contractual content, and assesses whether the restatement is justified.

This pillar depends on the jurisdiction inferred in Step 2. If jurisdiction confidence is Low or Unknown, run the pillar with reduced weight (see SKILL.md scoring rubric) and phrase findings as `Unverified — jurisdiction-dependent`.

## Why statutory duplication is a legal-design problem

Restating the law has four costs:

1. **Length.** A clause that recites the statute is paid for in reader time even though it conveys no party-specific information.
2. **Confusion.** Readers cannot tell which clauses are the parties' bargain and which are statutory baseline they would have received anyway.
3. **Drift risk.** Statutes change; a clause that paraphrases the current text becomes incorrect when the statute is amended.
4. **Enforcement risk.** In some regimes, restating mandatory consumer-protection rules in a contractual clause can paradoxically narrow them if the wording diverges — and unfair-terms regimes scrutinise restatements that mislead the consumer about the source of the right.

That said, **not every restatement is wasteful**. The pillar must distinguish three cases.

## The three cases

### Case A — Wasteful duplication

A clause restates a **mandatory statutory rule** that applies regardless. The parties cannot opt out, and the reader gains nothing from the restatement. Flag as Red.

Examples:

- A UK consumer contract that recites the consumer's right to reject under sections 20–22 of the Consumer Rights Act 2015 in the contract body. The right exists by operation of law; the restatement adds nothing.
- A French B2C contract that recites the *garantie légale de conformité* (Code de la consommation, articles L. 217-3 et seq.). Mandatory regardless.
- A German contract that restates the consumer's *Widerrufsrecht* from § 312g and § 355 BGB. The right is statutory; the restatement is required only because of the **information** duty under Art. 246a EGBGB, not because the right needs to be contractually granted. (Note: the *information* about the right is mandatory; the *grant* is not — the line item being audited is whether the clause is doing information-disclosure work or pure restatement.)
- A B2B contract under any continental civil-code system that restates *pacta sunt servanda* in its general provisions.

### Case B — Justified restatement for clarity

A clause restates **non-mandatory** (dispositive) statutory rules **and** the parties want those rules to apply, **and** the restatement adds clarity for a non-specialist reader. This is acceptable, especially in consumer documents where the reader would not be expected to know the dispositive default. Score Green or Yellow depending on length and accuracy.

Example: A consumer T&C that explains, in plain language, the right to withdraw within 14 days, including the practical steps, even though the underlying right is statutory. This is **information disclosure**, which is itself a legal-design good.

### Case C — Modification of dispositive rules

A clause cites the statute and **modifies** the dispositive rule (within the limits of what can be modified). This is not duplication at all — it is the parties exercising their freedom of contract. Score Green and exclude from the duplication count.

Example: "The Customer shall give notice of defects within 30 days, in derogation from the longer period under [statute]." The clause uses the statute as a baseline and modifies it.

## Detection signals

Scan the document for the following surface patterns:

### English

- "in accordance with applicable law" / "as required by law" / "to the extent permitted by applicable law" — these are **ritual incorporations** that add no content. Count every instance; high frequency is a drafting tic.
- "The parties acknowledge and agree that…" followed by a general statement of law.
- "Without prejudice to the rights of the Customer under applicable consumer protection legislation" — common UK / Irish pattern; usually a Red flag for Case A duplication.
- "Notwithstanding the foregoing, nothing in this Agreement shall limit any non-excludable statutory right" — generic safety clause; flag as Yellow unless the document also makes substantive restatements.

### French

- "conformément à la loi applicable" / "dans la mesure permise par la loi" / "sans préjudice des droits du Consommateur".
- "Il est rappelé que… [texte de la loi]" / "Conformément aux dispositions de l'article…" followed by a paraphrase.
- "La présente clause s'applique sans préjudice des dispositions impératives…" — generic safety clause.
- Recitations of *garantie légale de conformité* and *garantie des vices cachés* with no modification of dispositive parameters.

### German

- "im Rahmen der gesetzlichen Bestimmungen" / "soweit gesetzlich zulässig" / "nach Maßgabe der gesetzlichen Vorschriften".
- "Es gelten die gesetzlichen Bestimmungen" — particularly common in AGB; a flat reference to statute that adds nothing.
- Recitations of *Mängelrechte* under § 437 BGB without modification.
- Recitations of *Widerrufsbelehrung* (which **is** required by law as an information duty, so flag as Green — but check that the wording matches the official template; deviations can void the disclosure).

## Per-jurisdiction watchlists

### England & Wales / Scotland / Northern Ireland

Mandatory consumer rights — restatement is Case A (wasteful or potentially misleading):

- Consumer Rights Act 2015: short-term right to reject (s. 20–22); right to repair / replacement / price reduction (s. 23–24); statutory implied terms re quality, fitness, description (s. 9–11, 49–52).
- Unfair Contract Terms Act 1977: liability for death / personal injury arising from negligence cannot be excluded.

### United States (federal level)

Mandatory restatement watchlist is sparse at federal level — most consumer rules are state-level (UCC variants, state consumer-protection statutes). Flag federal restatements only for:

- Magnuson–Moss Warranty Act restatements in consumer contracts.
- FTC Act § 5 restatements in marketing T&Cs.
- CAN-SPAM restatements in marketing-related clauses.

### Canada

- Federal: PIPEDA restatements in privacy notices (often Case B — information disclosure justified).
- Québec: Civil Code restatements in B2C contracts under the *Loi sur la protection du consommateur*.

### France

- Code de la consommation: garantie légale de conformité (art. L. 217-3 et seq.); garantie des vices cachés (Code civil art. 1641 et seq., applied via consumer code).
- Article L. 121-19-3 — information obligations on distance contracts.

### Belgium

- Livre VI du Code de droit économique (CDE) — consumer-protection book.
- Article 1641 Code civil belge (garantie des vices cachés).

### Switzerland (Romandie + Deutschschweiz)

- Code des obligations (CO) / Obligationenrecht (OR) — same substance in both languages.
- *Garantie* under art. 197 et seq. CO/OR.
- Loi fédérale contre la concurrence déloyale (LCD) / UWG.

### Germany

- BGB §§ 305–310 (AGB-Recht) — controls clause-by-clause unfairness.
- BGB §§ 312–312k (consumer contracts, distance contracts).
- BGB §§ 433–479 (purchase, with mandatory consumer rules in §§ 474 et seq.).
- BGB §§ 535–580a (lease, with mandatory consumer rules in §§ 569).

### Austria

- KSchG (Konsumentenschutzgesetz).
- ABGB (Allgemeines bürgerliches Gesetzbuch).
- FAGG (Fern- und Auswärtsgeschäfte-Gesetz).

### Luxembourg

- Code de la consommation luxembourgeois.
- Code civil luxembourgeois.

### Liechtenstein

- PGR (Personen- und Gesellschaftsrecht).
- KSchG (parallel to Austrian).

## What you do **not** flag as duplication

- Recitations that exist **for an information-disclosure reason mandated by statute**. For example, the German *Widerrufsbelehrung*, the French *bordereau de rétractation*, the EU *informations précontractuelles* under Directive 2011/83/EU and its transpositions. These look like duplication but are required disclosures.
- Choice-of-law and choice-of-jurisdiction clauses that recite statutory defaults. The recitation is doing real work because the parties are exercising party autonomy.
- Boilerplate that paraphrases the *Vienna Sales Convention* (CISG) in cross-border B2B sales contracts where the parties are confirming application or exclusion of the Convention — that is contractually meaningful.

## Pillar score

Combine findings:

- Count of Case A (wasteful) instances per 1,000 words.
- Count of "ritual incorporations" per 1,000 words.
- Presence of any Case A clauses that materially restate mandatory consumer rights in a way that could mislead (always Red).

| Profile | Pillar score |
| --- | --- |
| No Case A findings; ≤ 2 ritual incorporations per 1,000 words; some Case B justified disclosure present | 85–95 |
| ≤ 1 Case A per 1,000 words; ritual incorporations 3–5 per 1,000 words | 65–80 |
| 2–4 Case A per 1,000 words; or ritual incorporations 6–10 per 1,000 words | 40–60 |
| 5+ Case A per 1,000 words; or any Case A finding that misstates a mandatory consumer right | 20–40 |
| Document is largely a paraphrase of statute with negligible party-specific content | 0–20 |

If jurisdiction confidence is Low or Unknown, do not assign a pillar score; mark `Unverified — jurisdiction-dependent` and redistribute weight per the SKILL.md rubric.

## What to report in the pillar section

For each finding:

| # | Case | Quote (verbatim) | Location | Likely statute | Severity | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 7.1 | A — wasteful | "The Customer is entitled to reject the goods within 30 days if they do not conform to the contract" | Clause 8.4 | Likely Consumer Rights Act 2015 s. 20–22 — verify | Red | Right exists by operation of law; restatement adds no content. Risk: paraphrase differs slightly from statute, potentially narrowing the consumer's right. |
| 7.2 | "Ritual" | "in accordance with applicable law" | document-wide, 14 occurrences | — | Yellow | High frequency of unspecific statutory deference is a drafting tic, not a substantive problem on its own. |

Always tag findings with `Likely [statute] — verify` rather than asserting a precise pinpoint. The duty to verify is on counsel.
