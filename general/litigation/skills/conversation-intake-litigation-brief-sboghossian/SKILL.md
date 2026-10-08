---
name: conversation-intake-litigation-brief-sboghossian
title: Intake — Litigation Brief
description: Use when a user wants to draft a litigation brief, complaint, statement of claim, statement of defense, or any first substantive court pleading, and Claude must gather the jurisdictional, procedural, and factual inputs before generating the document. Triggers on requests to draft, prepare, or review court filings, complaints, or defenses across MENA civil, commercial, Sharia, and free-zone courts, as well as UK, French, and US federal/state jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-litigation-brief
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Intake — Litigation Brief

## When this applies

Activate when a user requests drafting of a litigation brief, complaint, statement of claim, plaint, memorial, petition, or statement of defense in any court or tribunal. This skill collects the eight mandatory inputs before routing to the appropriate drafting skill. Drafting a complaint without confirming the court, parties, causes of action, and limitation period risks producing a document that is inadmissible, time-barred, or filed in the wrong forum.

## Behavior

Multi-turn intake (up to three turns for complex multi-party matters). Extract any information already given and ask only for what is missing. Surface limitation-period risks immediately if the user provides factual dates — a time-bar is a fatal defect that cannot be corrected post-filing.

## Required fields

### 1. Court or tribunal

Jurisdiction determines procedure, language, and pleading style entirely. Confirm:

| Court type | Jurisdiction examples | Language / procedure |
|---|---|---|
| Civil court (first instance) | UAE, LB, EG, KSA, FR | Arabic (or French for LB/FR); civil procedure codes |
| Commercial court / chamber | UAE Federal Courts, LB Commercial Court, FR Tribunal de Commerce | Arabic / French; specialized judges |
| Sharia / Personal Status court | KSA general courts, UAE Sharia courts for family / personal status | Arabic; Sharia-based pleading |
| DIFC Courts | DIFC | English; DIFC Court Rules (Practice Directions 2014, as amended) |
| ADGM Courts | ADGM | English; ADGM Court Regulations |
| Arbitration | DIAC, DIFC-LCIA, ICC, ICSID, CRCICA | Per institutional rules; language determined by agreement |
| Employment tribunal | DIFC Employment Tribunal, UAE Labour Court | English (DIFC); Arabic (UAE onshore) |
| UK civil courts | England & Wales | English; CPR 1998 (Civil Procedure Rules) |
| French courts | France | French; Code de Procédure Civile |

### 2. Parties

- **Claimant(s)**: full legal name, entity type (individual / company / government), nationality, domicile, and litigation representative (lawyer name and bar registration if known).
- **Respondent(s)**: same information. For corporate defendants, confirm current registered address for service of process — many MENA courts will reject a filing if the address for service is outdated.
- Capacity: is anyone a minor, under guardianship, a deceased estate, or a bankrupt? Flag — these affect procedural rules and may require appointment of a legal representative.

### 3. Facts

A clear, chronological narrative:
- Dates, places, and persons involved.
- What happened, in what order, and what each party did or failed to do.
- Key documents that exist (contracts, correspondence, invoices, payment records, certificates of delivery/rejection).
- Any prior proceedings, arbitrations, or dispute-resolution steps already taken.

This narrative is the foundation for the causes of action and the factual section of the brief. The better the facts, the better the document.

### 4. Causes of action

What legal claims are being made (or what are you defending against)?

Examples:
- Breach of contract (performance, payment, delivery failure)
- Unjust enrichment
- Tortious liability (negligence, fraud, misrepresentation)
- Unpaid wages / EOSB (employment)
- Breach of fiduciary duty (directors' liability)
- Intellectual property infringement
- Real estate recovery / eviction
- Bankruptcy / insolvency proceedings

Confirm the specific statutory basis if known (e.g., "Article 246 LB Code of Obligations and Contracts — breach of contract"; "DIFC Contract Law, DIFC Law No. 6/2004"; "KSA Commercial Court Law, Royal Decree M/93").

### 5. Damages claimed

- Specific amounts and supporting calculations, broken down by category:
  - Compensatory (direct loss: unpaid amounts, cost of cure)
  - Consequential (lost profit — note: consequential exclusions are common in commercial contracts)
  - Moral damages (LB, EG, FR: available; DIFC/ADGM/UK: limited to specific causes of action)
  - Interest (rate, accrual period — confirm statutory or contractual rate)
  - Legal costs and fees (recoverable in some jurisdictions: UK (CPR costs shifting), DIFC (costs follow the event), Lebanon (at court's discretion))
- If injunctive or interim relief is also sought, note it separately — this typically requires a parallel application.

### 6. Side

Plaintiff/Claimant or Defendant/Respondent? The structure of the document differs fundamentally:

| Side | Document | Key structural difference |
|---|---|---|
| Plaintiff | Complaint / Statement of Claim / Plaint | Narrates facts → states legal basis → requests relief |
| Defendant | Statement of Defense / Answer | Admits/denies each allegation → raises affirmative defenses → may counterclaim |

### 7. Procedural posture and deadlines

- **Statute of limitations**: see [[heuristic-statute-of-limitations-flag]] for jurisdiction-specific thresholds. Flag immediately if there is any risk of expiry. General reference (not a substitute for verification):
  - UAE (Federal): 10 years for civil claims; 5 years for commercial claims; 1 year for some labor claims.
  - DIFC: 6 years for contract claims (DIFC Law of Obligations); 3 years from discovery for tort.
  - LB: 10 years for civil; varies for criminal / personal status.
  - KSA: no codified limitation period in general civil law, but courts apply analogy to commercial norms; 5 years for commercial.
  - France (Code Civil Art. 2224): 5-year general limitation period.
  - UK: 6 years for contract; 6 years for tort; 12 years for specialty contracts under seal.
- **Response deadline**: has a filing deadline or court-ordered deadline been set? Confirm date.
- **Prior DRC / amicable demand**: some jurisdictions (KSA: mandatory mediation before commercial courts; UAE: mandatory reconciliation attempt for family matters) require a prior step before filing. Confirm whether it has been completed.

### 8. Key documents

List documents available and confirm they can be attached as exhibits:
- The contract at issue (including all amendments, side letters, annexes).
- Relevant correspondence (emails, WhatsApp if admitted in the relevant jurisdiction — UAE courts have accepted WhatsApp screenshots; DIFC courts: electronic evidence admissible per DIFC Evidence Law).
- Invoices, delivery notes, payment records.
- Witness contact information (and whether witnesses are willing to provide statements).
- Expert reports if obtained.

## Side-specific routing

After intake, route to:
- **Plaintiff/Claimant brief**: [[draft-litigation-complaint]]
- **Defendant/Respondent defense**: [[draft-statement-of-defense]]
- **Interim relief application**: separate workflow (note: interim injunctions require urgency threshold + balance of convenience analysis; available in DIFC Courts, UAE federal courts, Lebanon under emergency procedures)

## Critical flags at intake — always surface these

- **Statute of limitations**: run [[heuristic-statute-of-limitations-flag]] immediately if factual dates have been given. A time-bar check takes one minute and can save the client from a dead-on-arrival claim.
- **Document preservation / litigation hold**: instruct the user to immediately preserve all potentially relevant documents, emails, and electronic records. Deletion after litigation is reasonably foreseeable constitutes spoliation and can result in adverse inference orders in DIFC, UK, and US courts.
- **Conflicts check**: before drafting any client-specific pleading, confirm [[efirm-conflict-check]] has been run. If there is a conflict, do not proceed with the draft.
- **Settlement potential**: flag that settlement analysis should precede filing where the matter is commercially suitable. Filing costs, court fees, and enforceability of a judgment in the debtor's jurisdiction are all factors.
- **Enforceability of foreign judgment**: if the counterparty is in a different jurisdiction, flag enforcement risk. GCC countries have bilateral enforcement treaties (UAE-GCC Framework); DIFC has enforcement gateways to UAE courts. UK judgments enforceable in DIFC and many common-law jurisdictions. LB enforces foreign judgments by re-examination (exequatur) unless a treaty applies.

## Do not

- Draft a pleading before the statute of limitations has been assessed.
- Draft for the wrong side without clarifying which party the user represents.
- Assume Arabic-language proceedings for DIFC or ADGM courts — they operate exclusively in English.
- Apply US federal pleading standards (Twombly/Iqbal plausibility) to civil-law jurisdictions — MENA courts generally apply a "no surprise" rather than heightened pleading standard.
- Draft a complaint containing claims you know to be time-barred without flagging the problem prominently.

## Related skills

- [[draft-litigation-complaint]]
- [[draft-statement-of-defense]]
- [[heuristic-statute-of-limitations-flag]]
- [[efirm-conflict-check]]
- [[kb-civil-procedure-mena]]
- [[conversation-refusal-policy]]
- [[conversation-uncertainty-language]]
