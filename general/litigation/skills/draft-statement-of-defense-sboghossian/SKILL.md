---
name: draft-statement-of-defense-sboghossian
title: Statement of Defense
description: Use when drafting a statement of defense, answer to complaint, or defense filing responding to a civil claim or arbitration notice. Covers both common-law format (DIFC, ADGM, UK, US) with paragraph-by-paragraph admissions/denials and affirmative defenses, and civil-law format (UAE onshore, KSA, Lebanon, Egypt, France) with jurisdictional/procedural objections first and substantive defenses second. Includes response deadlines, tactical considerations for affirmative defenses and counterclaims, and the rule that procedural objections must be raised in the first pleading or they are waived.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-statement-of-defense
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Statement of Defense

The statement of defense (called an "Answer" in US practice, "Defence" in UK/DIFC, "Mémoire en défense" in civil-law systems) is the Defendant's first formal pleading. It sets the battleground: what is admitted, what is denied, what is a procedural bar, and what the Defendant affirmatively asserts. Errors in the first defense pleading — particularly failure to raise jurisdictional objections or affirmative defenses — can be irreversible.

## When to use this

- Defendant has received a claim form, complaint, statement of claim, or arbitration notice
- Defendant must file a formal written response within the procedural deadline
- Instructions have been taken and the client has decided to contest the claim (as opposed to settling)

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Plaintiff's complaint / statement of claim | The document being responded to; must be read paragraph by paragraph | Must provide |
| Defendant and counsel details | Parties to the defense; counsel must be registered in the relevant jurisdiction | Must provide |
| Court or arbitral tribunal | Determines the procedural rules and filing format | Must provide |
| Procedural deadline | Critical — missing the deadline may result in default judgment | See deadline table below |
| Instructions on each allegation | What is admitted, denied, or contested for lack of knowledge | Must take full instructions |
| List of affirmative defenses | Defenses that must be raised in this pleading or may be waived | Advise client; cannot assume |
| Decision on counterclaims | Whether to counterclaim and if so the basis | Strategic decision; advise carefully |

## Procedural Deadlines

| Jurisdiction | Standard defense deadline | Notes |
|---|---|---|
| DIFC | 28 days from service of claim form | DIFC Rules; Defendant may apply to extend |
| ADGM | 28 days from service | ADGM Civil Procedure Rules |
| UAE onshore | 15–30 days depending on court and matter type | Dubai Courts: typically 15 days at first hearing; written submissions thereafter |
| KSA (Najiz) | 15 days standard; may be extended by court | Submit via Najiz portal |
| LB civil | 30 days from formal service (assignation) | Lebanese Code of Civil Procedure |
| UK (CPR) | 14 days to acknowledge service; 28 days from service to file full defence | Civil Procedure Rules |
| US (FRCP) | 21 days from service (federal); state varies | Federal Rules of Civil Procedure; 30 days if served via waiver |
| ICC arbitration | 30 days from receiving request for arbitration | ICC Rules Article 5 |
| DIAC | 30 days from receipt of request | DIAC Arbitration Rules |

Missing a defense deadline without an extension may result in default judgment (common law) or the court proceeding to hear the matter without the Defendant's position (civil law). Always seek an extension before the deadline if instructions are incomplete.

## Common-Law Style Defense (DIFC / ADGM / UK / US)

### Structure

1. **Caption and case number** — court name, case number, parties, document title "DEFENSE" or "ANSWER"
2. **Introduction** — one paragraph identifying the Defendant and the fact that it contests the claim
3. **Admissions, denials, and statements of insufficient knowledge** — respond to each numbered paragraph of the complaint:
   - "Admitted" — facts that are accurate and not disputed
   - "Denied" — facts that are inaccurate or disputed; do not explain why in the denial (save for pleadings)
   - "Defendant lacks knowledge or information sufficient to form a belief as to the truth of the allegations in paragraph [X] and therefore denies same" — honest use of this formulation is appropriate; overuse is a pleading failure
4. **Affirmative defenses** — each raised as a separate numbered defense:
   - "First Defense: Lack of jurisdiction — [brief statement]"
   - "Second Defense: Statute of limitations — [basis]"
   - "Third Defense: Lack of standing — [basis]"
   - Common affirmative defenses: statute of limitations, release / accord and satisfaction, payment, force majeure, estoppel, waiver, failure of consideration, contributory / comparative negligence, failure to mitigate, illegality, laches
5. **Counterclaims** (if any) — separate section with its own factual basis and prayer for relief
6. **Prayer for relief** — dismiss the complaint; award costs to Defendant; any other relief

### Template (DIFC)

```
IN THE DIFC COURTS

Case No: [X]

[Plaintiff Name]
— Plaintiff

v.

[Defendant Name]
— Defendant

DEFENCE

The Defendant, [Defendant Name], by its counsel [Firm], for its Defence
states as follows:

RESPONSE TO SPECIFIC ALLEGATIONS

1. In response to paragraph 1 of the Claim: [Admitted / Denied / Defendant
   lacks knowledge sufficient to form a belief and therefore denies].

[Continue for each paragraph]

AFFIRMATIVE DEFENCES

First Defence — Limitation
The Plaintiff's claims are time-barred. [Cause of action] accrued no later
than [date], more than [X] years before the commencement of these
proceedings, in violation of [DIFC Limitation Law / applicable limitation
period].

Second Defence — [Next defence]
[Basis]

PRAYER FOR RELIEF

The Defendant respectfully requests that:
(a) The Claim be dismissed in its entirety;
(b) The Defendant be awarded its costs;
(c) Such further relief as the Court deems appropriate.

[Signature block, date, counsel details]
```

## Civil-Law Style Defense (UAE Onshore / KSA / LB / EG / FR)

### Key structural difference
In civil-law jurisdictions, procedural and jurisdictional objections must be raised as the FIRST argument — before any substantive defense — or they may be waived. This is the reverse of the common-law approach where jurisdiction can sometimes be challenged later.

### Structure

1. **Heading**: "To the Honorable [Court Name]" — formal salutation
2. **Identification of Defendant and counsel** — full legal names, registration numbers
3. **Preliminary (procedural and jurisdictional) objections** — these must come first:
   - Lack of territorial jurisdiction (محكمة غير مختصة ترابياً)
   - Lack of subject matter jurisdiction (محكمة غير مختصة نوعياً)
   - Improper service / failure to serve properly
   - Res judicata (سبق الفصل في الدعوى)
   - Limitation / prescription
   - Lack of legal standing
4. **Substantive defenses** — after procedural objections (if any) are dealt with:
   - Denial of factual allegations with specific responses
   - Legal basis for defense (with statute citations — UAE Civil Code, Lebanese Code of Obligations, KSA regulations)
   - Response to facts alleged, paragraph by paragraph
5. **Counterclaims / cross-claims** (if any)
6. **Documentary exhibits** — in civil-law systems, exhibits are filed with the pleading, not exchanged later; attach all relevant documents as numbered annexures
7. **Prayer for relief** — specific relief requested with legal basis

### Procedural objection precedence in key jurisdictions

| Jurisdiction | Rule on jurisdictional objections |
|---|---|
| UAE onshore | Must be raised at first opportunity (typically first hearing / first written submission); failure waives the objection |
| KSA | Must be raised in the first pleading; Najiz portal |
| LB | Déclinatoire de compétence must precede defense on the merits |
| FR | Exceptions d'incompétence raised before défenses au fond |

## Tactical Considerations

### Do not admit more than necessary
Every admission is a binding concession. If a fact is not within the Defendant's personal knowledge, use "insufficient knowledge" rather than admission. Silence in common-law pleading is typically treated as a denial; in civil-law systems, silence may be treated as tacit admission of undisputed facts.

### Affirmative defenses must be pleaded upfront
In common-law systems (particularly US federal practice and DIFC), affirmative defenses not raised in the defense may be waived. Compile a full list of potential affirmative defenses at the outset:
- Has the limitation period expired for any of the claims?
- Was there a prior settlement or release?
- Did the Plaintiff fail to mitigate its losses?
- Was there contributory fault by the Plaintiff?
- Does the court lack personal jurisdiction over the Defendant?

### Counterclaims: strategic value and risk
A counterclaim shifts the settlement dynamic (Plaintiff must now defend as well as prosecute) but:
- Adds complexity and cost to the proceedings
- May alert the Plaintiff to claims it did not know existed
- In some jurisdictions (LB, UAE), counterclaims may require separate filing fees and procedural steps
- Assess whether the value of the counterclaim justifies the additional litigation overhead

### Expert evidence
In civil-law jurisdictions, courts often appoint their own experts (خبير المحكمة) rather than relying on party-appointed experts. Plan the defense strategy accordingly — court-appointed experts produce reports that both parties comment on, rather than competing expert reports.

## Common Mistakes

- **Missing the deadline** — default judgment is the most preventable adverse outcome; always diarize the deadline on day one
- **Failing to raise jurisdiction in civil-law courts** — once the defense on the merits is filed, the jurisdictional objection is often waived
- **Admitting facts casually** — every admission simplifies the Plaintiff's case; careful instructions-taking before drafting
- **Counterclaiming reflexively** — a counterclaim that fails awards the Plaintiff costs and strengthens its position
- **Filing without all exhibits attached** — in civil-law systems, the pleading and its documents are filed together; incompleteness may prejudice the defense

## Related skills

- [[draft-witness-statement]]
- [[draft-settlement-agreement]]
- [[review-litigation-risk]]
- [[kb-litigation-procedure-mena]]
