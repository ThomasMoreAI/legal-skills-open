---
name: prompt-pack-demand-letter-sboghossian
title: Demand Letter
description: Use when a lawyer needs to draft a formal demand letter asserting a client's claim against a counterparty — stating the legal basis for the claim, damages suffered, supporting evidence, and a deadline for payment or response before legal proceedings are commenced. Applicable across MENA (UAE, KSA, LB, EG), DIFC/ADGM, and any specified jurisdiction; addresses the different formal requirements for pre-litigation demand in civil-law and common-law MENA contexts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-demand-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Demand Letter

A demand letter is the formal notice that precedes legal action. It serves three purposes: (1) it puts the opposing party on notice of the claim in documented form; (2) it gives them an opportunity to settle without litigation; and (3) in many MENA jurisdictions, it is a procedural prerequisite or strong convention before filing suit. A well-drafted demand letter creates a clear record and maximises settlement leverage.

## When to use this

- A client is owed money or has suffered a breach and has not received a satisfactory response to informal communications.
- The dispute is about to become a formal legal matter and the client wants one last documented opportunity for resolution.
- The applicable procedural rules or contract terms require a demand or notice before litigation can be commenced.
- A client wants to establish the date of formal notice (relevant for limitation periods and interest calculations).
- The opposing party's insurer has requested a formal demand as a condition of engaging with the claim.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Client name and role (claimant) | The letter is written on behalf of the client | Ask the user |
| Opposing party name and address | The letter must be correctly addressed | Ask the user |
| Description of the dispute | The factual and legal basis for the demand | Ask the user |
| Amount claimed (if monetary) | States the quantum of the demand | Ask the user |
| Evidence supporting the claim | Documents to be referenced or attached | Ask the user to list available documents |
| Deadline for response | Creates urgency; typically 7–21 days | Ask the user; default to 14 days for commercial claims |
| Governing law and jurisdiction | Affects legal basis cited and any procedural notes | Ask the user; identify from the underlying contract |

## Optional inputs

- Whether the letter should be sent by a lawyer's letterhead (often more effective) or the client directly.
- Whether the letter should propose settlement at a specific figure.
- Whether the client is open to mediation as an alternative.
- Whether the claim involves multiple parties.
- Whether interest on the debt/damages should be claimed.

## Letter structure

### Header
- Law firm letterhead (if sent by counsel) or client letterhead.
- Reference number.
- Date.
- Full name and address of the opposing party.
- "Without Prejudice Save as to Costs" — only add if the letter contains a settlement offer; a pure demand letter should not be marked without prejudice (it would exclude it from evidence in some jurisdictions).
- Subject line: "Formal Demand — [Brief description of claim] — [Reference, if any]"

---

### 1. Identification of the parties
"We act for [Client Name] ('our Client') in connection with the matter described below. We write to you in your capacity as [role — e.g., contracting party / director / guarantor]."

---

### 2. Background and facts
A concise, chronological narrative covering:
- The relationship between the parties (if any): contract, transaction, statutory obligation.
- What the opposing party was required to do.
- What they did (or failed to do).
- When the breach or failure occurred.
- The client's reliance and resulting damage.

Keep this factual and objective — avoid inflammatory language that will harden positions.

---

### 3. Legal basis for the claim
State the legal basis clearly:
- **Breach of contract:** Identify the specific contract, the provision breached, and how the breach has been established.
- **Statutory claim:** Identify the statute, article, and the specific obligation violated.
- **Tort / delict:** Identify the duty, breach, causation, and loss.
- **Unjust enrichment:** Where the opposing party has received a benefit at the client's expense without legal justification.

**MENA legal basis notes:**

| Jurisdiction | Key legal basis for commercial claims |
|---|---|
| UAE (onshore) | Civil Transactions Law (Federal Law No. 5 of 1985, as amended); Commercial Transactions Law; UAE Civil Code arts. governing breach and damages |
| UAE (DIFC) | DIFC Contract Law 2004 (based on UNIDROIT Principles and English law); DIFC courts have extensive commercial jurisdiction |
| KSA | Civil and commercial obligations under the Saudi Civil Procedure Law; Commercial Courts Law; general principles of Islamic law (Sharia) and Royal Decrees |
| Lebanon | Lebanese Code of Obligations and Contracts (Code des Obligations et des Contrats — COC); Code of Civil Procedure |
| Egypt | Egyptian Civil Code (Law No. 131 of 1948); Code of Civil and Commercial Procedure |
| ADGM | ADGM Contract Regulations; ADGM Courts |

---

### 4. Damages and quantum
- State the amount claimed as clearly as possible.
- Break down the claim into components if multiple heads of damage: principal debt / unpaid fees / penalty / consequential loss / interest.
- State the currency.
- State the basis for the interest claim if applicable:
  - UAE Civil Code: the legal rate of interest for commercial claims is 5% (or 9% in commercial matters — UAE Commercial Code).
  - DIFC: courts award interest at a rate they consider appropriate; commercial rate is typically the central bank rate plus a margin.
  - KSA: Islamic finance principles mean "interest" (riba) is not awarded as such; damages for late payment may be framed differently before Saudi courts; DIFC/ADGM arbitration seats avoid this complexity.
  - Lebanon: interest rates are regulated; Lebanese courts apply the contractual rate, failing which the legal rate of 9% per year under the COC.
- State that the client reserves the right to claim additional damages that become ascertainable before or during proceedings.

---

### 5. Supporting evidence
- List the key documents supporting the claim.
- State which documents are attached to the letter and which are available.
- Do not attach all evidence — select the 3–5 documents that most clearly establish the claim; retain the rest for proceedings.

---

### 6. The demand
State clearly and specifically what is demanded:
- "We hereby demand that you pay our Client the sum of [amount] in [currency] by [date] ('the Deadline')."
- If a non-monetary obligation: "We hereby demand that you [comply with / perform / cease and desist from] [specific obligation] by [date]."
- Payment details: provide the bank account for payment (IBAN, SWIFT, bank name, beneficiary) to remove any excuse for non-payment.

---

### 7. Consequences of non-compliance
State, without exaggeration, what will happen if the demand is not met by the Deadline:
- "If we do not receive [payment / compliance] by [date], our Client is instructed to commence [arbitration / litigation / insolvency proceedings] against you without further notice."
- Do not threaten actions the client cannot or will not take — this undermines credibility.
- Include: "Our Client reserves the right to claim all legal costs and interest accruing from the date of this letter."

---

### 8. Without prejudice settlement offer (optional)
If the client wishes to propose settlement at a specific figure less than the full claim, include a separate "WITHOUT PREJUDICE" paragraph at the end. This makes the settlement offer inadmissible in evidence in most jurisdictions:
"Our Client, without admission of any limitation of its claim, is prepared to accept [settlement amount] in full and final settlement of this matter if paid by [earlier date]. This offer will lapse on [date]."

---

### 9. Closing
- Contact details for the responding party.
- Instruction that all communications should be directed to the lawyer, not the client directly.
- "Yours faithfully" / "Yours sincerely" (per local convention).

---

## MENA-specific procedural requirements

| Jurisdiction | Pre-suit demand requirement |
|---|---|
| UAE (onshore) | Strong convention to send a formal demand before filing; some claims require notification through a notary public (إنذار رسمي — Inzar Rasmi) for certain obligations (lease termination, payment demands) |
| UAE (DIFC Courts) | No mandatory pre-suit demand; but courts take into account ADR attempts when awarding costs |
| KSA (commercial courts) | Formal demand is standard practice; some claims require notification through the notary or the Saudi Post (Bariid al-Sa'udi) for proof of delivery |
| Lebanon | Formal demand (mise en demeure) is required under the COC before certain obligations become enforceable; ideally sent by bailiff (huissier) or registered post |
| Egypt | Formal demand (إعذار — e'zar) sent by notary public (توثيق) or registered post is standard before filing; some claims require it as a matter of law |

## Delivery method

The method of delivery determines when formal notice is given and whether it can be proved:
- **UAE:** Registered post, courier with proof of delivery, or notarized Notice (Inzar) through a UAE Notary Public.
- **KSA:** Registered post; certified post through Saudi Post; notarized demand through a Saudi Notary.
- **Lebanon:** Bailiff (huissier) service is the most formally sound method; registered post with acknowledgment is common.
- **Egypt:** Notarized Inzar through the Egyptian Notary Office is the gold standard; registered post is commonly used.
- **DIFC/ADGM:** Email with read receipt and PDF attachment to the registered email address; follow up with courier.
- **Cross-border:** Consider whether service of the demand must comply with the Hague Service Convention or bilateral treaty between the jurisdictions.

## Common mistakes

- Demand letter that is so aggressive it makes settlement impossible — a good demand letter should be firm but leave a door open.
- Threatening criminal proceedings to enforce a civil debt — in many MENA jurisdictions, improperly threatening criminal prosecution is itself tortious or an abuse of process.
- Sending the letter to the wrong address or the wrong entity — this invalidates formal notice.
- Setting an unrealistically short deadline (24–48 hours) — courts view this negatively and it prevents genuine settlement.
- Not keeping a copy of the letter and the delivery record — both are evidence.

## Related skills

- [[prompt-pack-case-assessment-memo]]
- [[prompt-pack-settlement-agreement]]
- [[prompt-pack-arbitration-statement-of-claim]]
- [[prompt-pack-litigation-strategy-memo]]
- [[prompt-pack-case-law-research-prompt]]
