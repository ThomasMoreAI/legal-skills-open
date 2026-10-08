---
name: prompt-pack-statement-of-claim-sboghossian
title: Statement of Claim
description: Use when counsel needs to draft a statement of claim (or memorial, or claim brief) for a client bringing a civil or commercial dispute before a court or arbitral tribunal. Covers factual background, legal causes of action, heads of damage, and relief sought. MENA-specific guidance addresses UAE civil court pleading practice, DIFC/ADGM claim form requirements, Lebanese and Egyptian court procedures, and the distinction between civil-law declaratory and Arabic-language court filings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-statement-of-claim
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Statement of Claim

## When to use this

Use this skill when:
- A claimant (plaintiff) has decided to bring a claim and needs to draft the initiating pleading.
- In litigation: a Claim Form (DIFC/ADGM/UK) or Statement of Claim (various MENA courts) is required to commence proceedings.
- In arbitration: a Statement of Claim or Memorial is the first substantive pleading, filed after the Request for Arbitration (use [[prompt-pack-request-for-arbitration]] for the initiation document; this skill covers the fuller Memorial/Statement of Claim).
- The factual matrix and legal causes of action need to be organized coherently before counsel can advise on strategy.

**Important distinction:** In international arbitration, the Statement of Claim is typically the full merits pleading — a detailed document running 30–200 pages with factual narrative, legal argument, document references, and exhibit list. In MENA court proceedings, the initial claim brief may be shorter, with evidence submitted over subsequent procedural sessions. Calibrate the output accordingly.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Client / claimant identity** | Who is bringing the claim | Ask |
| **Defendant / respondent identity** | Who is being sued | Ask |
| **Court or tribunal** | Determines format, language, and substantive law | Ask; this is the single most important input |
| **Cause of action** | What legal wrong is alleged? (Breach of contract, tort, unjust enrichment, fiduciary breach, IP infringement, etc.) | Ask |
| **Key facts** | Chronological narrative of events giving rise to the claim | Ask; ideally provide a fact chronology |
| **Damages / relief sought** | What the claimant wants the tribunal to award | Ask; must include a quantified amount or a basis for quantification |

## Optional inputs

- **Governing law of the underlying contract** — may differ from the law of the forum; explain the conflict if one exists.
- **Evidence summary** — list of key documents that will be relied on; embedded as exhibit references.
- **Expert evidence** — if expert evidence (damages expert, technical expert) is anticipated, indicate this in the statement of claim.
- **Interim / emergency relief** — if urgency requires an interim injunction or emergency measure alongside the statement of claim, flag this separately.

## Document structure

### For international arbitration (full Memorial / Statement of Claim)

1. **Introduction and summary**
   - One-page introduction identifying the parties, the dispute, the claims, and the relief sought.
   - The tribunal should be able to read this introduction and understand the entire case.

2. **Parties**
   - Claimant: full legal name, jurisdiction, relevant background.
   - Respondent: full legal name, jurisdiction.
   - Key individuals (witnesses who will be relevant).

3. **Procedural background**
   - Arbitration agreement: cite the clause; state that all preconditions (notice, cooling-off) have been met.
   - Institutional background (if applicable): Request for Arbitration filed [date]; Respondent served [date]; tribunal constituted [date].
   - Governing law: substantive law of [jurisdiction]; lex arbitri: [seat law].

4. **Factual background**
   - Chronological narrative of all material facts.
   - Reference documents by exhibit number (C-1, C-2, etc.).
   - Structure: (a) the relationship / contract; (b) what was agreed; (c) what happened; (d) the breach or wrongful act; (e) its consequences.
   - Be specific: dates, parties, amounts, communications.
   - Do not omit facts that are unfavorable — the tribunal will eventually see them; present them in context.

5. **Legal analysis — causes of action**

   For each cause of action:
   - **Heading:** e.g., "Breach of Contract," "Unjust Enrichment," "Tort."
   - **Elements:** state each element of the cause of action under the applicable law.
   - **Application:** for each element, explain how the facts satisfy it, with document references.
   - **Legal framework:** cite the applicable statute, code article, or principle (without inventing article numbers). Common MENA sources:
     - UAE: UAE Civil Transactions Law (Federal Law No. 5 of 1985), DIFC Contract Law (DIFC Law No. 6 of 2004).
     - Lebanon: Code of Obligations and Contracts 1932.
     - Egypt: Egyptian Civil Code (Law No. 131 of 1948).
     - KSA: Saudi Commercial Court Law, general Sharia principles.

6. **Damages and quantum**
   - **Principle:** under UAE law (Art. 292 CTL) and most civil-law systems, damages compensate for actual loss and loss of profit that are a direct consequence of the breach.
   - **Types of loss:**
     - Direct financial loss: actual sums paid or lost.
     - Loss of profit (lucrum cessans): what the claimant would have earned but for the breach.
     - Consequential loss: additional losses flowing from the breach (subject to foreseeability/remoteness rules; more restricted in civil-law systems than common law).
   - **Quantification:** explain how each head of damage is calculated; attach a damages schedule as an exhibit if complex.
   - **Interest:** state the basis for claiming interest (contractual rate / statutory rate / LIBOR + margin); start date; compound or simple.
   - **Currency:** state the currency of all claims; address FX conversion if amounts arose in multiple currencies.

7. **Other relief**
   - Declaratory relief: specific declaration sought.
   - Injunctive relief (if applicable): describe the interim measure and the basis.
   - Specific performance: if the claimant wants the respondent to perform a contractual obligation rather than just pay damages.
   - Costs: claim for legal costs and arbitration costs (standard in international arbitration).

8. **Conclusion and prayer for relief**
   - Summary of all relief sought.
   - Formal prayer: "WHEREFORE, Claimant respectfully requests that the Tribunal award: (i) [specific relief]..."

9. **Exhibits list** — numbered list of all documents referenced.
10. **Witness statement index** — if factual witness statements are filed simultaneously, list them.
11. **Expert report index** — if damages or technical expert reports are filed, list them.

### For MENA court proceedings (shorter initial claim brief)

UAE/Lebanon/Egypt civil courts typically accept a shorter initial claim brief, with evidence and arguments developed over subsequent sessions:

1. **Court identification and case heading** — court name, case number (to be assigned), parties.
2. **Statement of claim facts** — brief factual summary (2–5 pages); detailed exhibits attached.
3. **Legal basis** — cite the specific articles of the applicable civil code or statute.
4. **Relief claimed** — the specific order(s) sought.
5. **Signature** — advocate's signature and bar registration number (required in most MENA courts).
6. **Arabic language** — UAE onshore and KSA courts require Arabic-language claims; Lebanon accepts French or Arabic; Egypt requires Arabic.

## Jurisdictional notes

### UAE — onshore courts (Dubai, Abu Dhabi, Sharjah)
- Claims filed in Arabic; translated documents must have certified translations.
- UAE courts operate on an inquisitorial model; the judge investigates the evidence as well as hearing argument.
- Expert witnesses (khabeer) appointed by the court, not just the parties; the court-appointed expert's report carries significant weight.
- Counterclaims: respondent/defendant may file a counterclaim in the same proceedings; address this risk in the claim strategy.
- Prescription/limitation: UAE Civil Law — contractual claims: 15 years; commercial claims: 10 years; bills of exchange/cheque claims: 3 years; tort claims: 3 years.

### DIFC / ADGM courts
- Common-law pleading rules; DIFC Court Rules (DCR) / ADGM Court Procedure Rules.
- DIFC: Claim Form (Part 7 or Part 8 procedure depending on claim type); Particulars of Claim filed simultaneously or within 14 days.
- English language; documents in other languages must be translated.
- Expert evidence: party-appointed, subject to court directions; concurrent evidence ("hot-tubbing") available.
- DIFC courts have jurisdiction over disputes where parties agree to DIFC jurisdiction (jurisdiction agreement) or where the defendant is DIFC-incorporated.

### KSA
- Saudi Commercial Courts (established 2016) handle commercial disputes.
- Claims filed in Arabic.
- Sharia-based contract law: proof standards, witness requirements, and documentary evidence rules may differ from civil or common law.
- Interest claims: not available as of right in Saudi courts (conventional interest is not Sharia-compliant); rephrase as "delay compensation" or "agreed penalty" where contractually stipulated.

### Lebanon
- Lebanese Code of Civil Procedure governs; civil courts (tribunaux de grande instance) for commercial matters.
- Claims in Arabic or French.
- Judge-led investigation process (examining judge system in some matters).

## Drafting standards

- Lead with your strongest facts and most certain legal arguments; do not bury the case in procedural history.
- Number every paragraph; arbitral tribunals and courts rely on paragraph references for efficiency.
- Reference every document by exhibit number in the text; do not describe documents without referencing them.
- State damages with precision; "substantial damages" without quantification is insufficient in most jurisdictions — you need at minimum a framework for quantum even if the exact figure is disputed.
- Use the words "it is submitted" or "the Claimant submits" for legal argument; distinguish clearly from factual narrative.

## Common mistakes

- **Mixing facts and argument.** Factual narrative should come first; legal argument applied to the facts comes later. Mixing them makes the claim hard to follow.
- **Omitting unfavorable facts.** Tribunals expect claimants to address the hardest facts; omitting them looks evasive and damages credibility when they emerge in cross-examination.
- **Inadequate damages quantification.** Filing a claim without a damages schedule leaves the quantum to be determined later; this weakens settlement leverage and may result in the tribunal awarding less than the actual loss.
- **Wrong court / tribunal.** Check the dispute resolution clause and applicable jurisdiction rules before filing; filing in the wrong forum can be fatal to the claim and costly to correct.

## Related skills

- [[prompt-pack-statement-of-defense]]
- [[prompt-pack-request-for-arbitration]]
- [[prompt-pack-settlement-agreement]]
- [[prompt-pack-procedural-order-draft]]
- [[heuristic-always-state-jurisdiction-first]]
