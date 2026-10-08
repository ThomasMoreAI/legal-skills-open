---
name: draft-arbitration-request-sboghossian
title: Draft — Request for Arbitration
description: Use when asked to draft a Request for Arbitration (or Notice of Arbitration) to initiate institutional arbitration proceedings. Covers the required content under DIAC, ICC, DIFC-LCIA/LCIA, SIAC, and ICSID rules, the structure of the document, filing mechanics, service on the respondent, and critical deadlines. P0 priority — incomplete or untimely filing can waive claims or breach statute of limitations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-arbitration-request
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Draft — Request for Arbitration

## When to use this

Use this skill when a client wishes to initiate institutional arbitration under an arbitration clause or standalone arbitration agreement. The Request for Arbitration (RfA) — also called Notice of Arbitration under some rules — is the document that formally commences proceedings, sets the clock running on procedural timelines, and defines the scope of the dispute.

**Filing deadline is paramount**: verify whether a contractual limitation period or statutory time-bar applies before drafting. In many MENA jurisdictions, limitation periods under the applicable substantive law (civil code) run in parallel with any contractual period.

## Required inputs

| Input | Notes |
|---|---|
| Claimant(s) full legal name and address | Corporate entities: include registration number |
| Respondent(s) full legal name and address | |
| Arbitration agreement reference | Identify: contract name, date, clause number or standalone agreement date |
| Institutional rules | DIAC / ICC / DIFC-LCIA / LCIA / SIAC / ICSID / other |
| Seat of arbitration | The legal seat (lex arbitri); distinct from the physical hearing venue |
| Language of arbitration | English / Arabic / bilingual |
| Number of arbitrators | 1 or 3; check if prescribed by the arbitration clause |
| Summary of the dispute | Chronological narrative of the facts |
| Legal basis of claims | Contract breach / tort / statutory claim / treaty violation (ICSID) |
| Relief sought | Specific monetary amounts; declaratory relief; injunctions; specific performance; interest; costs |
| Nominated arbitrator (if required) | If the rules require nomination at filing stage |
| Filing fee | Verify current fee schedule; payment evidence must accompany the filing |

## Document structure

### 1. Identification of parties
```
CLAIMANT:
  [Full legal name]
  [Registered address]
  [Registration No. / ID]
  Represented by: [Counsel name and firm, if applicable]
  Contact for notices: [Email and address]

RESPONDENT:
  [Full legal name]
  [Registered address]
```

### 2. Reference to the arbitration agreement
Attach and quote the arbitration clause verbatim. State:
- Name of the contract containing the clause (or standalone agreement).
- Date of execution.
- Clause or article number.
- Why the dispute falls within the scope of the clause.

> "The Claimant invokes the arbitration clause contained in Article [X] of the [Contract Name] dated [Date] between the Claimant and Respondent, which provides: '[verbatim text of clause]'."

### 3. Summary of the dispute
Provide a concise but sufficiently detailed chronological narrative:
- The commercial relationship and its background.
- The key events giving rise to the dispute (with dates).
- The Respondent's acts or omissions that constitute the breach (or other wrong).
- How those acts/omissions caused the Claimant's loss.

**At filing stage**: you need enough detail to define the dispute for jurisdictional purposes and any limitation period analysis, but the full Statement of Claim (merits brief) comes later. Do not over-commit at this stage.

### 4. Legal basis of claims
State the legal framework:
- Breach of contract under [governing law]: specify the articles/provisions breached.
- Tort or unjust enrichment if applicable.
- For ICSID: investment treaty and BIT provision invoked.

### 5. Relief sought
Be specific and exhaustive here — claims not pleaded in the RfA may be barred under some rules:
- **Principal sum**: state currency and amount.
- **Interest**: pre-award interest from [date of breach]; post-award interest at [rate]. For KSA seat or KSA-governing-law clauses: interest framing is sensitive — use "financial compensation for delay" language tied to actual loss.
- **Costs**: legal fees, expert fees, arbitration costs.
- **Declaratory relief**: what declaration is sought.
- **Any other relief** the tribunal deems fit (catch-all).

### 6. Arbitrator nomination (if required by the rules)
For three-arbitrator tribunals, the Claimant typically nominates one co-arbitrator in the RfA. State:
- Nominated arbitrator's full name.
- Confirmation that the nominated arbitrator has been contacted and is available.
- Brief statement of qualifications relevant to the dispute.

### 7. Procedural matters
- Proposed seat (if the clause does not fix it).
- Proposed language.
- Proposed number of arbitrators (if not fixed).

### 8. Filing fee
Attach proof of payment of the registration/filing fee. Verify the current fee schedule directly with the institution — fee schedules change.

### 9. Signature and service on Respondent
- Signed by Claimant or authorized counsel.
- Under most institutional rules, simultaneous service on Respondent is required — use the method specified in the arbitration clause's notice provision, or as specified in the rules.

---

## Institution-specific requirements

### DIAC (Dubai International Arbitration Centre) — Rules 2022
- File via DIAC online portal: `https://diac.ae`
- Article 4, DIAC Rules 2022: identification, dispute summary, relief, copy of arbitration clause, arbitrator nomination if applicable.
- Filing triggers DIAC's 30-day response window for the Respondent.
- DIAC registration fee: scale based on amount in dispute (see current DIAC fee schedule).
- Seat defaults to Dubai unless parties specify otherwise.

### ICC (International Chamber of Commerce) — Rules 2021
- File with ICC Secretariat (Paris or regional offices including Abu Dhabi, Singapore).
- Article 4, ICC Rules 2021: identification, arbitration agreement copy, dispute description, relief, nominated arbitrator.
- ICC advance on costs: paid by Claimant on filing; Respondent shares subsequently.
- The ICC Secretariat scrutinizes the award — higher institutional oversight than DIAC or LCIA.
- For MENA disputes: ICC has an Abu Dhabi regional office and strong regional caseload.

### DIFC-LCIA / LCIA — Rules 2020
- DIFC-LCIA merged operations into LCIA in 2021; DIFC seat is still available.
- Article 1, LCIA Rules 2020: file with LCIA Registrar (London) via online portal.
- Notice of Arbitration (LCIA terminology) must include: parties, dispute summary, arbitration agreement copy, relief sought.
- LCIA Registration fee + hourly-rate tribunal fee structure (different from ad valorem fees used by DIAC/ICC).

### SIAC (Singapore International Arbitration Centre) — Rules 2016 (6th Ed)
- Relevant for Singapore-seated MENA disputes (common in English/common-law contracts).
- Notice of Arbitration filed via SIAC case management system.
- Article 3, SIAC Rules: standard content plus filing fee.

### ICSID (International Centre for Settlement of Investment Disputes)
- Investor-State disputes only, where host state has consented (BIT, ICSID Convention, or contract).
- Request for Arbitration under Article 36, ICSID Convention: elaborate identification of the treaty and jurisdictional basis.
- ICSID has strict jurisdictional requirements; deficient requests risk preliminary objections.

---

## Critical practice points

### Limitation periods — check before filing
- Arbitration commences (and the limitation clock stops) on the date the RfA is received by the institution, or on service on the Respondent, depending on the rules.
- UAE law (Civil Transactions Law): general 15-year limitation; specific periods for certain claims.
- LB law: 10-year general commercial period; shorter for tort.
- KSA: period depends on claim type; labor claims have much shorter periods.
- **Verify the applicable limitation period under the governing law before finalizing the filing date.**

### Interim / emergency relief
- If Claimant needs urgent interim measures (asset freeze, injunction, preservation orders), file a separate Emergency Arbitrator application simultaneously or before the main RfA.
- Most modern institutional rules (DIAC 2022, ICC 2021, LCIA 2020, SIAC 2016) provide an Emergency Arbitrator mechanism.
- For urgency in DIFC or ADGM, consider parallel application to the DIFC Court or ADGM Court for interim support measures.

### Confidentiality
- Institutional arbitration is confidential by default under most rules; state this explicitly if confidentiality is important.
- ICSID arbitrations are partially public.

### Language
- For Arabic-language arbitrations (KSA, onshore UAE): Arabic RfA or bilingual; check whether the institution handles Arabic filings.
- DIAC handles Arabic; ICC can but prefers English; LCIA primarily English.

---

## Common mistakes

- **Vague relief statement**: failing to quantify the claim at the RfA stage can limit what the tribunal awards.
- **Wrong institution named**: the arbitration clause specifies the institution — do not substitute a different one without both parties' consent.
- **Failure to attach the arbitration agreement**: almost every institutional rule requires this exhibit; missing it causes the file to be returned.
- **Proof of payment not attached**: filings without fee payment are not accepted.
- **Service not contemporaneous**: under most rules, service on the Respondent must accompany filing; missing this step can affect the commencement date.
- **Interest framing for KSA-seat cases**: interest as such may be challenged; use delay compensation language.

## Related skills

- [[draft-cease-and-desist]]
- [[draft-boilerplate-clauses]]
- [[review-contract-general]]
- [[draft-bilingual-ar-en-side-by-side]]
