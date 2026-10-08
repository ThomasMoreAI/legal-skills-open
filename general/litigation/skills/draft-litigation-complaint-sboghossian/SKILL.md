---
name: draft-litigation-complaint-sboghossian
title: Litigation Complaint / Statement of Claim
description: Use when drafting a litigation complaint or statement of claim initiating court proceedings in a civil or commercial dispute. Covers both common-law style (DIFC, ADGM, UK, US) and civil-law style (UAE onshore, KSA, LB, EG, FR) complaint structures, jurisdictional and venue analysis, Arabic-translation requirements for MENA courts, service rules, court fees, and the critical tactical decisions around cause of action pleading and damages quantification. Triggers on "complaint", "statement of claim", "litigation filing", "court claim", or "initiating proceedings" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-litigation-complaint
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Litigation Complaint / Statement of Claim

## When to use this

Use this skill when a party is initiating court proceedings to assert a civil or commercial claim. The complaint / statement of claim is the pleading that starts the lawsuit: it identifies the parties, the court, the cause(s) of action, the material facts, and the relief sought.

This skill covers both:
- **Common-law style** complaints (DIFC Courts, ADGM Courts, English Courts, US Federal/State Courts)
- **Civil-law style** statements of claim (UAE federal courts, KSA courts, Lebanese courts, Egyptian courts, French courts)

Before drafting, confirm:
- The applicable statute of limitations has not expired
- The chosen court has subject-matter and personal jurisdiction
- The correct venue (local court) has been identified
- Court fees have been calculated and payment arranged

For arbitration commencement instead of court proceedings, use [[draft-notice-of-arbitration]].

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Plaintiff(s) | Full legal name, entity type, address, counsel |
| Defendant(s) | Full legal name, address (for service) |
| Court | Jurisdiction + venue; state whether filing in civil, commercial, or specialized chamber |
| Cause(s) of action | Each legal theory that supports the claim |
| Material facts | Chronological narrative with dates, documents, and parties |
| Damages claimed | Quantified where possible; prayer for damages in the alternative |
| Relief sought | Full enumeration of remedies requested |

## Common-law style complaint (DIFC / ADGM / UK / US)

### Structure

1. **Caption**
   - Court name and division
   - Case number (assigned on filing)
   - Plaintiff(s) vs Defendant(s)
   - Document title ("Claim Form and Particulars of Claim" / "Complaint")

2. **Introduction / overview** (1-2 paragraphs)
   - One-paragraph summary of the dispute
   - Stakes: amount in controversy and nature of relief
   - Strong opening framing (factual, not argument-forward)

3. **Parties**
   - For each party: full name, entity type, jurisdiction of formation, principal place of business / address
   - Basis for personal jurisdiction over each Defendant

4. **Jurisdiction and venue**
   - Subject-matter jurisdiction basis (commercial claim ≥ AED X; DIFC nexus; etc.)
   - Personal jurisdiction basis (contract performed in jurisdiction; defendant incorporated here; etc.)
   - Proper venue

5. **Factual allegations** (numbered paragraphs)
   - Chronological narrative
   - Each material fact in a separate numbered paragraph
   - Cross-reference exhibits by exhibit letter
   - Avoid argument; plead facts, not characterizations
   - Identify the relevant contract, clause, date, and breach precisely

6. **Causes of action** (separately pleaded counts)
   - Each cause of action is a separate count with its own heading
   - Each count: re-alleges prior factual allegations, identifies the legal basis, applies facts to elements, pleads that Defendant breached / is liable
   - In DIFC/ADGM: DIFC Contract Law, DIFC Law of Obligations — cite to specific provisions
   - In UK: cause of action at common law / equity; specific statute if applicable
   - Common commercial causes of action: breach of contract, fraudulent misrepresentation, negligence, unjust enrichment, conversion, breach of fiduciary duty

7. **Damages**
   - Quantify all ascertainable losses with supporting calculation
   - For unliquidated damages: plead "in an amount to be determined at trial, but not less than USD X"
   - Special damages (direct, specific losses): itemize
   - General damages (consequential losses): describe
   - Interest: claim pre-judgment interest (statutory or contractual rate)
   - Costs: include a claim for costs

8. **Prayer for relief**
   - Enumerate every remedy sought:
     - Judgment for damages in the principal amount of USD X
     - Pre-judgment interest
     - Post-judgment interest
     - Specific performance / injunction (where applicable)
     - Costs and legal fees
     - Such further relief as the Court deems just

9. **Verification** (where required by local rules)
   - Plaintiff's officer certifies accuracy of the pleading

## Civil-law style statement of claim (LB / KSA / UAE onshore / FR / EG)

### Structure

1. **Court heading**
   - "To the Honorable Presiding Judge of [Court Name]"
   - Chamber / division (commercial, civil)
   - Date of filing

2. **Identification of Plaintiff (and counsel)**
   - Full name, father's name, nationality, civil status, address
   - Law firm + counsel details
   - Registered agent (where required by court rules)

3. **Identification of Defendant(s)**
   - Full name(s) and address(es) for service

4. **Statement of facts** (narrative form)
   - Continuous chronological narrative (not numbered paragraphs — though some courts accept numbering)
   - Detail the relationship, the events, and the breach or harm
   - Cite relevant documentary evidence (attached as exhibits) throughout

5. **Legal arguments** (article-by-article)
   - In civil-law courts, the legal argument is part of the pleading, not reserved for trial
   - Cite: applicable statute, article number, court interpretation if established
   - Apply the article to the facts
   - Address each cause of action / legal basis separately
   - In Lebanese courts: cite Lebanese Code of Obligations and Contracts; Lebanese Code of Civil Procedure
   - In KSA courts: cite Saudi Royal Decrees, Saudi Labor Law, Commercial Court Law; note Sharia basis where applicable
   - In UAE federal courts: cite UAE Civil Code (Federal Law 5/1985), Commercial Transactions Law (Federal Law 18/1993), relevant specific laws; note Arabic citation conventions
   - In Egyptian courts: cite Egyptian Civil Code, Commercial Code

6. **Claims** (numbered relief sought)
   - Numbered list of precise reliefs sought
   - Include request for costs, attorney fees (if permitted by court rules), and interest

7. **Annexed exhibits list**
   - Each exhibit identified by number, description, and relevance

8. **Signature block**
   - Plaintiff / counsel signature, date, place

## Critical procedural considerations

### Statute of limitations
Verify before filing — missing the limitation period is fatal:
- **UAE federal (commercial)**: generally 10 years (Civil Code Art. 473); some specific claims shorter (insurance: 3 years; checks: 6 months from dishonor)
- **KSA**: 5-year limitation for commercial claims under the Commercial Court Law; 1-year for some labor claims
- **LB**: 10 years for personal obligations (Code of Obligations Art. 340); shorter for specific categories (insurance, labor)
- **DIFC**: DIFC Law of Limitation — 6 years for contract; 6 years for tort (generally)
- **UK**: Limitation Act 1980 — 6 years for contract and tort; 12 years for deed
- **FR**: Code Civil Art. 2224 — 5 years from date knowledge of facts

### Jurisdiction (MENA specifics)
- **UAE federal courts**: commercial courts in Abu Dhabi and Dubai for commercial disputes; civil courts for non-commercial; ADGM and DIFC have exclusive jurisdiction over matters with a DIFC/ADGM nexus
- **KSA**: Commercial Court Law 2021 — dedicated commercial courts for commercial disputes; Labor Courts for employment; Administrative Courts for disputes with government entities
- **Lebanon**: Court of First Instance (civil/commercial); specialized courts (rent, labor); Court of Appeal for enforcement of foreign judgments
- **DIFC Courts**: opt-in for non-DIFC-nexus parties possible under a 2011 protocol (UAE parties may voluntarily submit)

### Service of process
- **MENA civil-law courts**: service by court bailiff (muhdar) is standard; personal service to defendant required in most cases; substituted service only if Defendant cannot be found after diligence
- **International service**: Hague Service Convention governs where both countries are members; diplomatic channels otherwise; UAE has bilateral service treaties with certain countries
- **DIFC/ADGM**: service in accordance with DIFC Courts Rules; may serve by email if contractually agreed

### Arabic language requirements
- **UAE federal courts**: all pleadings must be in Arabic; certified Arabic translations of any foreign-language documents are required
- **KSA courts**: Arabic required; foreign-language documents require licensed translator
- **LB**: Arabic or French accepted in most cases; Arabic required before certain courts
- **DIFC/ADGM**: English proceedings; Arabic translation not required for court filings

### Court fees
- **UAE federal courts**: typically 6% of the claim amount, capped at AED 40,000 per level; fees for interim relief additional
- **DIFC Courts**: graduated fee schedule based on claim value; DIFC Courts online fee calculator
- **KSA Commercial Courts**: court filing fee per schedule of fees under Commercial Court Law
- **LB**: modest court fees (legacy); additional lawyer registration fees
- Always verify current fee schedules — these change

## Drafting tactics

- **Lead with your strongest cause of action** — courts (and their clerks) read the first count first
- **Plead facts with specificity**: date, who did what, what document was involved — vague pleadings invite motions to dismiss / exceptions de procédure
- **Quantify damages early** even if the final number is "to be assessed at trial, but no less than USD X" — it alerts the court to the scale of the dispute and affects court allocation
- **Reserve the right to amend** — "Plaintiff reserves the right to add parties, claims, or causes of action pending further investigation and discovery / disclosure"
- **Attach key documents as exhibits** and refer to them in the body of the complaint
- **Do not volunteer weaknesses** in the complaint; but do not misrepresent — bad faith pleading carries sanctions in most jurisdictions

## Common mistakes

- Filing in the wrong court (wrong jurisdiction, wrong chamber) — requires refiling and potentially resets statute of limitations if the original was invalid
- Missing the limitation period
- Failing to serve Defendants properly — jurisdiction not established
- Omitting a cause of action that could have been pleaded — claim preclusion (res judicata) bars it later
- Pleading facts that are inconsistent with documentary evidence already in hand — credibility destroyed at an early stage
- Forgetting to request interim relief (injunctions, attachments) at the same time as the main claim, when urgency exists

## Related skills

- [[draft-statement-of-defense]]
- [[draft-notice-of-arbitration]]
- [[draft-legal-opinion]]
- [[review-litigation-strategy]]
