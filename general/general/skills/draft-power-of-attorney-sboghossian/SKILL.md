---
name: draft-power-of-attorney-sboghossian
title: Power of Attorney (PoA / وكالة / Procuration)
description: Use when drafting a Power of Attorney (PoA / وكالة) authorizing an agent to act on a principal's behalf. Covers all PoA types (general, special, durable, springing), required inputs, precise enumeration of powers, revocation mechanics, and the critical form requirements (notarization, apostille, consular legalization) for LB, KSA, UAE, EU/UK, and cross-border use. Arabic terminology included. Triggers on "power of attorney", "poa", "وكالة", "procuration", "proxy", or "authorization letter" requests for formal legal authority.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-power-of-attorney
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Power of Attorney (PoA / وكالة / Procuration)

## When to use this

A Power of Attorney is a legal instrument by which a principal (موكِّل / mandant / grantor) authorizes an agent (وكيل / mandataire / attorney-in-fact) to act on the principal's behalf in defined legal matters. Use this skill when:

- The principal cannot be physically present to sign documents, appear before authorities, or transact (e.g., abroad, incapacitated, or for convenience)
- A company needs to authorize an employee or external representative to act on its behalf for specific transactions
- Real estate is being bought, sold, or mortgaged through a representative
- A person grants authority to manage bank accounts, customs clearances, or corporate proceedings
- Cross-border transactions require representation in a foreign jurisdiction

**Critical**: a PoA is not the transaction itself — it is the authority to perform the transaction. Draft it before the underlying transaction is signed; expired or revoked PoAs invalidate acts performed thereunder.

## Types of PoA

### 1. General PoA (وكالة عامة)
Grants broad authority to act across many matters. Use with caution:
- Many jurisdictions narrowly construe general PoAs for high-stakes acts (real estate, marriage)
- Principals often overestimate what a "general" PoA authorizes
- Third parties (banks, land registries) frequently require specific authority enumerated in the PoA rather than relying on a general grant
- Recommend a special PoA for any transaction that can be identified in advance

### 2. Special / Limited PoA (وكالة خاصة)
Grants authority for a specific act or transaction. The safest and most commonly accepted form:
- "To sell Property X, being [description], for a price of not less than [amount], and to sign all documents necessary to complete the transfer and registration"
- Banks, land registries, and courts typically require specific authorization; general PoAs are often rejected

### 3. Durable PoA
Survives the principal's incapacity. Common-law concept (US, UK, DIFC/ADGM). Civil-law analogues exist but vary:
- **UK**: Lasting Power of Attorney (LPA) under the Mental Capacity Act 2005; must be registered with the Office of the Public Guardian before use
- **France**: "mandat de protection future" — activated on incapacity
- **KSA / UAE / LB**: no direct durable PoA equivalent; PoA typically terminates on incapacity of the principal under classical civil-law rules; requires court-appointed guardianship instead for capacity-related situations

### 4. Springing PoA
Activates only on the occurrence of a condition (typically incapacity). Common in US estate planning. Limited acceptance in MENA civil-law jurisdictions — the condition-precedent nature creates uncertainty that third parties may not accept.

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Principal | Full legal identification (full name, ID/passport number, date of birth, nationality, address) |
| Attorney-in-fact / Agent | Same level of identification |
| Scope | Precisely enumerated powers — "general" wording is risky |
| Duration | From-to dates, or "until revoked in writing" |
| Jurisdiction of use | Determines form requirements; determines what third parties will accept |
| Country of authentication / use | May need apostille and/or consular legalization |
| Language | Arabic required for use in MENA onshore jurisdictions; French / English for international use |

## Common powers enumerated (select applicable)

State each power separately and specifically. Grouped by category:

**Property and real estate:**
- Purchase / sell / lease / mortgage the following specific property: [describe with plot number, title deed number, address]
- Register title deeds and complete all formalities with [Dubai Land Department / Abu Dhabi ADDED / Lebanese Cadastre / etc.]
- Receive purchase proceeds and sign receipts

**Banking and finance:**
- Open, operate, and close bank accounts in the principal's name at [named bank / any bank]
- Deposit and withdraw funds; execute transfers; sign checks
- Apply for and accept credit facilities

**Corporate and commercial:**
- Vote shares in [Company Name] at general and extraordinary meetings
- Sign [specific types of] contracts on behalf of the principal
- Represent the principal in negotiations for [specified purposes]

**Litigation and legal proceedings:**
- Represent the principal before [named court / all courts] in [specified matter or all civil matters]
- Sign pleadings, receive service, enter into settlement agreements, collect judgments
- Note: many jurisdictions (UAE, KSA, LB) require the attorney to be a licensed lawyer to appear before courts — a general PoA to a non-lawyer for court representation is typically ineffective

**Customs, import/export, and government:**
- Appear before customs authorities and sign customs declarations for [specified goods]
- Appear before [specific ministry or authority] for [specific purpose]
- Apply for and collect permits, licenses, and official documents

**Tax and accounting:**
- Sign tax returns and representations before tax authorities
- Receive tax assessments and file objections

**Personal status (very restricted):**
- Marriage and divorce: most jurisdictions prohibit PoA for marriage and divorce under Islamic law (these require personal appearance); Lebanon and some civil jurisdictions allow limited PoA for marriage under specific conditions
- Do not include these powers unless specifically verified with local counsel

## Form requirements by jurisdiction

These are the most common rejection causes for cross-border PoAs — verify current requirements with local counsel before relying on the instrument.

| Jurisdiction | Requirements |
|---|---|
| **UAE (Dubai)** | Notarized before Dubai Courts Notary Public (or Abu Dhabi Judicial Department for Abu Dhabi use). For use abroad: MOFA attestation, then consulate of destination country. For use before DLD: specific DLD-approved format; stamp and registration may be required. Arabic is required for local use; bilingual versions recommended. |
| **UAE (Abu Dhabi)** | Abu Dhabi Judicial Department notarization; MOFA attestation for international use. |
| **KSA** | Must be notarized before Saudi Notary Public (كاتب العدل) OR before a Saudi Embassy abroad. Specific format required by Saudi Sharia courts and government bodies — the PoA must comply with the format accepted by the receiving authority (DGA, SAIP, courts, real estate registry). Hijri date must be included. Language: Arabic required. |
| **Lebanon (LB)** | Notarized before a Lebanese Notary Public; for use abroad, Ministry of Foreign Affairs (Affaires Étrangères) apostille; for non-Hague countries, consular legalization. Bilingual Arabic/French versions common. |
| **France / EU** | Apostille under the Hague Convention of 5 October 1961 for use in Hague member states; for non-member states, consular legalization through the embassy. French notarial system: notarization by a French notaire creates an "acte authentique" with higher evidentiary weight. |
| **UK** | For UK PoA used abroad: notarial certification + apostille from FCDO (Foreign, Commonwealth & Development Office). For UK Lasting Power of Attorney: registration with Office of the Public Guardian mandatory. |
| **Cross-border chain** | The standard authentication chain for a UAE PoA for use in France: UAE Notary → UAE Ministry of Foreign Affairs (MOFA) attestation → French Consulate in UAE attestation. Verify the current MOFA/MFA procedure — digital attestation is increasingly available. |

## Revocation

**General rule**: a principal may revoke a PoA at any time, provided the PoA is not irrevocable (a PoA "coupled with interest" where the agent has a financial interest in the PoA cannot be unilaterally revoked).

**How to revoke effectively**:
1. Sign a formal revocation notice
2. Notarize the revocation (same standards as the original PoA)
3. **Critically**: serve the revocation notice on:
   - The agent (to stop them acting)
   - Every third party who has been informed of or relied on the PoA (banks, land registry, courts, etc.)
   
Without notice to the third party, acts performed by the agent in good faith reliance on the PoA before receiving notice of revocation are typically binding on the principal.

**Death of the principal**: most PoAs terminate automatically on the principal's death. Acts performed by the agent after the principal's death (even without knowledge) may be invalid. Inform third parties immediately upon death.

**Irrevocable PoA**: in limited circumstances, particularly M&A and financing transactions, an irrevocable PoA may be granted (e.g., a lender holding a PoA to execute security documents on the borrower's behalf). Must be expressly stated as irrevocable; consideration required; judicial scrutiny varies by jurisdiction.

## Bilingual requirements (MENA)

For LB, UAE, and KSA: **Arabic version governs** for use in local courts and with government authorities. The English or French version may be added for international use, but the Arabic text must be complete and accurate — do not rely on a summary translation.

For KSA in particular: the Saudi notary will typically prepare the PoA in Arabic; ensure the agent and principal verify the Arabic text before signing.

## Critical notice to user

> "PoAs to be used internationally typically require apostille or consular legalization. The chain is: notarization → Ministry of Foreign Affairs attestation → consulate of the country of use. Current procedures change — verify with the MOFA in the jurisdiction of notarization and the consulate of the target country before proceeding."

## Common mistakes

- Using a general PoA where the receiving authority requires specific powers enumerated (common rejection at DLD, SAIP, and banks)
- No Arabic version for MENA use — Western-language PoA rejected by local authorities
- Not revocating properly — agent continues to act on revoked PoA because third parties were not notified
- PoA covering personal-status acts (marriage, divorce) without verifying whether the jurisdiction allows them
- PoA signed without notarization for a transaction requiring notarized authorization — instrument invalid

## Related skills

- [[draft-prenup]]
- [[draft-property-sale-agreement]]
- [[draft-mortgage]]
- [[draft-corporate-resolution]]
