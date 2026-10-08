---
name: prompt-pack-statement-of-defense-arbitration-sboghossian
title: Statement of Defense (Arbitration)
description: Use when a respondent in an international or domestic arbitration needs to draft a formal Statement of Defense (or Counter-Memorial) responding to the claimant's claims, asserting defenses, and filing any counterclaims. Tailored to international arbitration procedure under ICC, LCIA, DIAC, ADIAC, CRCICA, SCCA, and UNCITRAL rules with MENA-seat specific guidance on procedural timelines and substantive law defenses.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-statement-of-defense-arbitration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Statement of Defense (Arbitration)

## When to use this

Use this skill when:
- A respondent in an arbitration proceedings (whether ICC, LCIA, DIAC, ADIAC, CRCICA, SCCA, UNCITRAL, or other institution) must file a formal Statement of Defense or Counter-Memorial by the deadline set in Procedural Order No. 1 or the applicable rules.
- The Response to the Request for Arbitration has already been filed (which is the initial short document) and now the fuller merits-level pleading is needed.
- Counsel needs to organize the respondent's factual narrative, legal defenses, and counterclaim framework coherently.

**Distinguish from [[prompt-pack-statement-of-defense]]:** That skill covers general litigation (court proceedings) statements of defense. This skill is specifically tailored to international arbitration procedure — where the Statement of Defense is typically a full Counter-Memorial with exhibits, witness statements, and legal argument, rather than a shorter court pleading.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Arbitration case reference and institution** | Determines procedural requirements; filing must comply with applicable institutional rules | Ask |
| **Copy of the Statement of Claim / Memorial** | The defense must respond paragraph by paragraph | Must be provided |
| **Seat of arbitration** | Determines lex arbitri and some procedural rights | Ask |
| **Substantive governing law** | Determines which legal standards apply to the defenses | Ask; confirm from the underlying contract |
| **Key defense themes** | High-level summary of respondent's position | Ask; essential for coherent narrative |
| **Counterclaims (if any)** | Must be asserted at the correct procedural stage | Ask; deadline for counterclaims may be the same as the defense |

## Optional inputs

- **Jurisdictional challenges** — if the claimant has no valid arbitration agreement with the respondent, or if the arbitration clause is invalid, a jurisdictional objection is raised as a preliminary matter within (or alongside) the Statement of Defense.
- **Security for costs application** — if the claimant is a shell company or is domiciled in a jurisdiction where enforcement would be impossible, a security-for-costs application can be filed simultaneously.
- **Interim measures** — if the respondent needs urgent protective measures (e.g., to prevent disposal of assets), address in a separate emergency application.

## Document structure

### Statement of Defense / Counter-Memorial structure

1. **Introduction and executive summary**
   - Open with a clear statement of the respondent's case: "This is a dispute arising from [describe contract]; the Claimant's claims are legally and factually unfounded for the following reasons: [list 3–5 core defense themes]."
   - Signal any counterclaims at the outset.

2. **The respondent's perspective on the parties and factual background**
   - Provide the respondent's account of the relevant facts.
   - Do not simply repeat the claimant's narrative and add "however"; build the respondent's own coherent story.
   - Reference respondent's exhibits (R-1, R-2, ...) consistently.

3. **Response to the claimant's factual narrative**
   - Take the claimant's Statement of Claim paragraph by paragraph.
   - For each paragraph: **Admit** / **Deny** / **No admission** (where the fact is beyond the respondent's knowledge).
   - For denials: give the respondent's version in the body or cross-reference to the Respondent's Facts section.

4. **Jurisdictional objections** (if any — should be raised first)
   - Nature of the objection: is the arbitration agreement invalid? Did the dispute arise outside its scope? Is this the wrong institution?
   - Legal basis: applicable arbitration law (UAE Federal Law No. 6 of 2018, DIFC Arbitration Law, ICC Rules Art. 6, etc.).
   - Request: "The Respondent requests that the Tribunal determine this jurisdictional issue as a preliminary question / bifurcate the proceedings."
   - Note: many institutional rules (ICC, LCIA, DIAC) allow the respondent to raise jurisdictional objections without prejudice to its substantive defenses.

5. **Substantive defenses to each claim**

   Structure each defense as:
   - **Defense title:** e.g., "Defense to the Breach of Contract Claim."
   - **The claimant's case (summarized):** one sentence stating what the claimant alleges.
   - **The respondent's position:** the core denial.
   - **Factual basis:** specific facts and documents that contradict the claimant's account.
   - **Legal analysis:** the elements of the claimant's cause of action; which are not proven; which the respondent disputes.
   - **Conclusion:** "For these reasons, the breach of contract claim must fail."

   **Key arbitration-specific defense issues:**

   | Issue | Guidance |
   |---|---|
   | Force majeure (contract clause) | Read the contract's force majeure clause precisely; its scope may be wider or narrower than the statutory doctrine; most institutional cases analyze the clause first, then the statutory backstop |
   | Limitation / time bar | Check: (a) contractual notice requirements (notice of claim within X days); (b) statutory limitation of action under the governing law; (c) any estoppel or waiver argument if the claimant delayed |
   | Liquidated damages vs. penalty (UAE Art. 390 CTL / DIFC Contract Law) | Civil-law systems allow courts/tribunals to reduce an agreed penalty clause that is grossly disproportionate to the actual harm; argue reduction if the LD clause is a penalty in disguise |
   | Set-off and cross-claims | State clearly whether the respondent is asserting a set-off (reduces the claimed amount) or a counterclaim (asserts an independent cross-demand) |
   | No loss / no causation | Even if there was a breach, the claimant suffered no loss (or the loss was not caused by the breach); address separately from the liability defense |
   | Mitigation | Claimant failed to take reasonable steps to mitigate its loss; quantify the mitigation discount |

6. **Challenge to the claimant's damages**
   - Go through each head of damage claimed by the claimant.
   - For each: dispute the quantum, the causation, or the legal basis.
   - Provide the respondent's alternative calculation with supporting exhibits.
   - Note: even if the tribunal finds some liability, a well-presented damages challenge can significantly reduce the award.

7. **Respondent's counterclaims** (if any)
   - Structure each counterclaim like a mini-Statement of Claim:
     - Facts giving rise to the counterclaim.
     - Legal causes of action (breach of contract, misrepresentation, unjust enrichment, etc.).
     - Quantum and damages calculation.
     - Relief sought.
   - The counterclaim must arise from the same transaction or dispute unless the tribunal allows related claims (check institutional rules).

8. **Relief requested**
   - "For all of the foregoing reasons, the Respondent respectfully requests that the Tribunal:
     (i) Dismiss the Claim in its entirety;
     (ii) [If counterclaim:] Award the Respondent [relief] on the Counterclaim;
     (iii) Award the Respondent its costs of the arbitration including legal fees and the Respondent's share of the arbitration fees;
     (iv) Grant such other relief as the Tribunal considers appropriate."

9. **Exhibits list** — all respondent's exhibits numbered R-1, R-2, etc.
10. **Witness statements** — factual witness statements filed simultaneously (per the procedural timetable).
11. **Expert reports** — damages or technical expert reports filed simultaneously (if within the first round).

## Jurisdictional / institutional notes

### ICC Arbitration (Rules 2021)
- The Defense to the Request for Arbitration is filed within 30 days of the Secretariat transmitting the Request.
- The fuller Counter-Memorial is filed per the Terms of Reference and Procedural Order No. 1 timetable.
- Counterclaims: must be raised no later than the Counter-Memorial unless permitted by the tribunal or by agreement.

### LCIA (Rules 2020)
- Response to Request for Arbitration: within 28 days (extendable).
- Statement of Defense: per agreed or directed timetable.
- Counterclaims: may be raised with the Response or in the Statement of Defense per tribunal's directions.

### DIAC (Rules 2022)
- Statement of Defense: within 30 days of receiving the Statement of Claim (or per procedural order).
- Counterclaims: same deadline as Statement of Defense unless extended.
- Seat default: Dubai.

### SCCA (Saudi Center for Commercial Arbitration — Rules 2023)
- Statement of Defense (Statement of Response): within 30 days of receiving claimant's statement.
- Arabic language option: if requested, or if the seat is in KSA, the defense may be in Arabic.
- Counterclaims: filed with the Statement of Defense.

### CRCICA (Cairo Regional Centre for International Commercial Arbitration)
- UNCITRAL-based rules; Statement of Defense per timetable.
- Arabic or English (or French) per party agreement and tribunal direction.

## Drafting standards

- Tell the respondent's story first; do not let the claimant's narrative frame the entire case. A strong Statement of Defense opens with the respondent's account, not a rebuttal.
- The paragraph-by-paragraph response section must be complete — no gaps. Use a table or section for this to ensure every paragraph is covered.
- For every legal argument: state the rule, apply it to the facts, reach a conclusion. Do not assume the tribunal knows the legal principles without stating them.
- Exhibits: label and describe each exhibit clearly; do not rely on bare numbers.
- Proportionality: the Statement of Defense in a USD 10 million DIAC arbitration does not need to be 200 pages; match the document length to the complexity of the dispute.

## Common mistakes

- **Late jurisdictional objection.** If an arbitration-clause challenge (e.g., the clause is pathological, or there is no clause between these parties) is not raised in the Response to the Request for Arbitration or in the Statement of Defense, it is typically waived.
- **Blanket denial without factual basis.** "The Respondent denies all claims" without factual support is ineffective and damages credibility.
- **Missing the counterclaim deadline.** Institutional rules often prohibit new counterclaims after the Statement of Defense stage; missing this window can be fatal.
- **Treating the Statement of Defense as a preliminary document.** In international arbitration, the Statement of Defense is often the respondent's best (sometimes only) opportunity to present its full case in a structured document; it deserves the same investment as the claimant's Memorial.

## Related skills

- [[prompt-pack-statement-of-defense]]
- [[prompt-pack-request-for-arbitration]]
- [[prompt-pack-statement-of-claim]]
- [[prompt-pack-procedural-order-draft]]
- [[prompt-pack-settlement-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
