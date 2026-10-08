---
name: prompt-pack-statement-of-defense-sboghossian
title: Statement of Defense
description: Use when a defendant or respondent needs to draft a statement of defense to a civil or commercial claim, addressing each allegation, asserting applicable defenses, and including any counterclaims. Covers factual admissions and denials, affirmative defenses, counterclaims, and the legal framework for each. MENA-specific guidance covers UAE civil court defense practice, DIFC/ADGM defense procedures, and the strategic differences in civil-law vs. common-law pleading.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-statement-of-defense
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Statement of Defense

## When to use this

Use this skill when:
- A defendant or respondent has been served with a statement of claim or claim brief and must file a formal defense within the applicable deadline.
- A party needs to respond to allegations systematically, challenge legal bases, and preserve all available defenses.
- A party has counterclaims against the claimant that should be asserted in the same proceedings.
- Legal counsel needs to draft a responsive pleading that sets up the defense narrative while preserving procedural options.

**Deadline sensitivity:** Failure to file a defense within the required time can result in default judgment (in court proceedings) or a deemed admission (in some arbitration contexts). Establish the filing deadline before starting to draft.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Defendant / respondent identity** | Who is filing the defense | Ask |
| **Court or tribunal and case reference** | Determines procedural requirements, format, and language | Ask |
| **Copy of the statement of claim** | The defense must respond to the claim paragraph by paragraph | Must be provided; cannot draft without it |
| **Key defenses** | The legal bases for denial or partial admission | Ask; identify with counsel |
| **Counterclaims (if any)** | Any claims the defendant has against the claimant | Ask |

## Optional inputs

- **Evidence in support of the defense** — documents, communications, contracts showing the defendant's version of events.
- **Witness statements** — if witness statements are filed simultaneously (common in international arbitration).
- **Affirmative defense basis in law** — statute of limitations, force majeure, novation, payment, accord and satisfaction, set-off, contributory fault.

## Document structure

### For international arbitration (full Counter-Memorial / Statement of Defense)

1. **Introduction and summary**
   - Deny the claimant's characterization of the dispute.
   - State the respondent's alternative narrative in one or two paragraphs.
   - Identify the key defenses and whether any counterclaims are asserted.

2. **Admissions and denials — paragraph-by-paragraph response**
   - For each paragraph of the Statement of Claim: admit, deny, or state "No admission is made" (the appropriate response where the defendant neither knows nor can verify the allegation).
   - Do not leave any paragraph unanswered — in most procedural systems, failure to respond is deemed an admission.
   - For complex allegations: deny the characterization while acknowledging underlying facts ("The Respondent admits that [event] occurred but denies that this constitutes a breach of the Agreement for the reasons set out below.").

3. **Respondent's version of the facts**
   - Chronological narrative of the facts from the respondent's perspective.
   - Reference documents by exhibit number (R-1, R-2, etc.).
   - Address specifically the facts relied on by the claimant; provide the respondent's explanation or context.
   - Include facts that support affirmative defenses even if not raised by the claimant.

4. **Legal defenses**

   **4.1 Defenses to each cause of action:**
   For each of the claimant's causes of action:
   - Identify the elements the claimant must prove.
   - Address each element: which are contested and why.
   - Set out the affirmative defense arguments.

   **Common defenses in MENA commercial disputes:**

   | Defense | Legal basis | Key considerations |
   |---|---|---|
   | No breach / full performance | Claimant's characterization of "breach" is incorrect; defendant performed | Most common defense; requires factual rebuttal |
   | Force majeure / Acts of God | Contract force majeure clause; UAE CTL Art. 273; DIFC Contract Law Art. 72 | Must show: (a) event was unforeseeable; (b) beyond reasonable control; (c) prevented performance (not just made it more difficult) |
   | Claimant caused or contributed to the loss | Contributory fault (UAE CTL Art. 290); the claimant's own breach broke the causal chain | Reduces damages even if breach by defendant is proven |
   | Payment / full satisfaction | All amounts due have been paid; release granted | Produce evidence of payment and any discharge documents |
   | Limitation / prescription | Claim is time-barred | UAE commercial limitation: 10 years; DIFC: 6 years (DIFC Limitation Law); KSA: varies |
   | Set-off | Respondent has a cross-debt owed by claimant; net balance is zero or less | Requires a connected cross-claim; formally assert as set-off |
   | Novation or variation | The original obligation was replaced or modified; claimant's claim is on the original, not the modified version | Requires written evidence in most MENA jurisdictions |
   | Waiver or estoppel | Claimant's conduct waived the right to enforce the obligation | Common-law estoppel is available in DIFC/ADGM; doctrine of venire contra factum proprium applies in some civil-law systems |
   | Penalty clause reduction | Contractual penalty is unconscionable or grossly disproportionate | UAE CTL Art. 390: court may reduce an agreed penalty if grossly disproportionate |

   **4.2 Quantum challenges:**
   Even if liability is established in part, challenge the claimant's damages:
   - Denial of causation: the alleged loss was not caused by the defendant's act.
   - Mitigation failure: the claimant failed to take reasonable steps to mitigate its loss (duty to mitigate under UAE, DIFC, and most MENA systems).
   - Overclaim: specific heads of loss are unsubstantiated, speculative, or calculated on an incorrect basis.
   - Deduction: set-off of amounts owed by claimant to defendant.
   - No consequential / indirect loss: most commercial contracts exclude consequential damages; assert this.
   - Interest overclaim: challenge the rate, start date, or compounding basis.

5. **Counterclaims** (if applicable)
   - State clearly: "In addition to defending the Claim, the Respondent asserts the following Counterclaims."
   - Structure each counterclaim in the same way as a Statement of Claim (factual basis, legal cause of action, quantum, relief sought).
   - Note: in some jurisdictions and under some institutional rules, counterclaims must be filed within a specified period and may require a separate filing fee.

6. **Relief sought**
   - "The Respondent respectfully requests that the tribunal: (i) dismiss the Claim in its entirety; (ii) award costs to the Respondent; (iii) [if counterclaim: award [relief] on the Counterclaim]."

7. **Exhibits list** — all documents relied on; numbered R-1, R-2, etc.

### For MENA court proceedings (shorter initial defense brief)

UAE, Lebanon, and Egypt civil courts:
- The defense is filed in writing; the defendant must appear at the scheduled hearing.
- Format: shorter brief responding to the claim; evidence attached.
- Arabic language required (UAE, KSA, EG); French acceptable in Lebanon.
- The defense brief identifies contested facts, disputes the legal basis of the claim, and sets out affirmative defenses.
- A plea on jurisdiction (e.g., arbitration clause exists; wrong court) is a preliminary defense that must be raised before addressing the merits.

## Jurisdictional notes

### UAE — onshore courts
- The defense is filed in Arabic; translated documents require certified translations.
- UAE courts give the defendant the right to respond to any new evidence or arguments filed by the claimant; multiple rounds of pleadings are common.
- Court-appointed expert (khabeer): if the court appoints an expert, both parties have the right to submit observations; engage proactively.
- Default judgment: if the defendant fails to appear or file a defense, the court may issue a default judgment; this can be challenged within defined periods.
- Set-off and counterclaim: both available in UAE court proceedings.

### DIFC courts
- DIFC Court Rules (DCR): Acknowledgment of Service + Defense within 28 days of service (or extended period by agreement / court order).
- Admissions and denials required per CPR Practice Direction.
- Preliminary issues: DIFC courts allow early determination of jurisdiction or legal issues; useful when an arbitration clause is overlooked by the claimant.

### KSA — commercial courts
- Defense in Arabic; filed within the time specified by the court.
- The judge plays an active investigative role; the defense frames the key disputed issues but the judge will question witnesses directly.
- Counterclaims must be connected to the main claim.

## Drafting standards

- Admit what is admitted — an overly blanket denial of all facts damages credibility with the tribunal. Admit uncontested facts (dates, party identities, contract existence) and contest the facts that actually matter.
- Use clear headings for each legal defense; do not mix factual narrative and legal argument in the same section.
- Number all paragraphs; cross-reference the claim's paragraph numbers in the admissions section for clarity.
- Do not overlook preliminary / jurisdictional defenses (arbitration clause, wrong court, limitation). These must be raised before the merits or they may be waived.
- Quantify counterclaims; a vague counterclaim "for losses to be determined" is weaker than a specific quantum claim.

## Common mistakes

- **Blanket denial of all allegations.** Overly broad denials ("The Respondent denies each and every allegation in the Statement of Claim") are disfavored by tribunals and fail to engage with the real issues.
- **Missing the limitation defense.** If the claim is potentially time-barred, the limitation defense must be raised in the defense or it may be waived.
- **Omitting contributory fault.** Even if the defendant did breach, if the claimant contributed to the loss, this reduces damages; failing to plead it waives the argument.
- **Counterclaim filed too late.** Check institutional rules and court rules for the deadline to assert counterclaims; they often differ from the defense deadline.
- **No preliminary jurisdiction challenge.** If there is an arbitration clause, a challenge to court jurisdiction must be raised in the defense; silence amounts to submission to the court's jurisdiction.

## Related skills

- [[prompt-pack-statement-of-claim]]
- [[prompt-pack-statement-of-defense-arbitration]]
- [[prompt-pack-settlement-agreement]]
- [[prompt-pack-procedural-order-draft]]
- [[heuristic-always-state-jurisdiction-first]]
