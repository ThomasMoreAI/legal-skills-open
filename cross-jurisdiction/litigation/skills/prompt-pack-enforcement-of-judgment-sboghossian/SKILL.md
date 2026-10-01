---
name: prompt-pack-enforcement-of-judgment-sboghossian
title: Enforcement of Judgment
description: Use when preparing a strategy memo for enforcing a domestic or foreign judgment or arbitral award against a judgment debtor. Covers available enforcement mechanisms (attachment of assets, garnishment, property seizure), asset location strategies, domestication requirements for cross-border enforcement, and priority among enforcement steps. Critical for MENA enforcement (UAE, KSA, LB, EG) where foreign judgment enforcement has specific statutory requirements and practical challenges. Trigger when a client has obtained a judgment or award and needs to convert it into recovery.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-enforcement-of-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: litigation
language: en
---

# Enforcement of Judgment

## When to use this

Use this skill when a client has obtained a judgment (from a court) or award (from an arbitral tribunal) and needs a practical strategy memo to recover against the judgment debtor. Winning a case is only the first step; enforcement — converting the paper judgment into actual recovery — is often where cases are won or lost commercially.

Typical triggers:
- Client has a final and binding UAE court judgment or arbitral award; debtor is refusing to pay
- Cross-border enforcement: judgment obtained in France needs to be enforced in UAE
- Judgment debtor is an entity in Lebanon or KSA; creditor needs to understand the practical path
- Enforcement of a foreign arbitral award under the New York Convention

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Judgment or award details (court, date, amount, parties) | Basis of enforcement | Must be provided |
| Jurisdiction where judgment was obtained | Domestic enforcement is different from cross-border | Ask |
| Jurisdiction(s) where enforcement is sought | Multiple jurisdictions may be needed | Ask |
| Known or suspected assets of the judgment debtor | Enforcement without assets is academic; asset intelligence is critical | Ask for all known information |
| Status of judgment (final? on appeal?) | Cannot enforce a non-final judgment in most jurisdictions | Ask |

## Optional inputs

- Judgment debtor's corporate structure (useful for piercing the corporate veil claims or tracing assets to related parties)
- Prior enforcement attempts and results
- Existence of any security (pledge, mortgage, personal guarantee) attached to the judgment
- Expiry dates of enforcement rights (statutes of limitation on enforcement)

## Enforcement strategy framework

### Step 1 — Confirm enforceability

Before proceeding, verify:
- Is the judgment/award final and not subject to appeal?
- Is the enforcement right still alive? (Limitation period: in UAE, 15 years for final judgments; check each jurisdiction)
- Are there any immunities? (State entities, diplomatic immunity)
- For arbitral awards: is the New York Convention (NYC) applicable in the enforcement jurisdiction?

### Step 2 — Asset tracing and intelligence

The quality of enforcement depends entirely on identifying assets. Methods include:
- **Corporate registry searches**: Identify assets owned by the debtor entity (registered shares, real estate)
- **Land registry searches**: UAE property owned by or associated with the debtor
- **Court record searches**: Prior judgments or charges against the debtor
- **UBO register checks**: In UAE, the Ultimate Beneficial Owner register is publicly accessible in some circumstances
- **Open source intelligence**: News, social media, LinkedIn — may reveal assets or business dealings
- **Formal court-ordered disclosure**: In DIFC and ADGM courts, a judgment creditor can apply for an order requiring the debtor to disclose assets; in common-law systems, a third-party debt order can be applied to debtors of the judgment debtor

### Step 3 — Identify available enforcement mechanisms

**UAE onshore enforcement (Federal Law of Civil Procedure, as amended)**:
- Attachment of movable assets (hajz tanfeezi — executive attachment)
- Attachment of bank accounts (attachment order served on UAE banks where debtor holds accounts)
- Seizure and auction of real property (requires Court of Execution order)
- Attachment of shares in UAE companies
- Travel ban application (prevents debtor from leaving UAE during enforcement proceedings)
- Imprisonment for debt: in UAE, failure to pay a final judgment can lead to enforcement against the person in some circumstances (not applicable to corporate debtors)

**DIFC Courts enforcement**:
- DIFC Courts are a separate enforcement jurisdiction with efficient common-law procedures
- DIFC Court can enforce its own judgments via court bailiffs, bank account garnishment, appointment of receivers
- DIFC judgment against a party with UAE mainland assets: must obtain a UAE Court of Cassation recognition order to enforce mainland; DIFC has a memorandum of understanding with Dubai courts for this purpose

**ADGM Courts enforcement**:
- Similar to DIFC; common-law procedure; efficient enforcement
- Cross-enforcement with Abu Dhabi courts via protocol

**UAE arbitral award enforcement**:
- UAE Federal Arbitration Law (Law No. 6 of 2018, Art. 55) provides for enforcement of domestic awards by UAE courts
- NYC awards: Art. 57 provides for enforcement of foreign NYC Convention awards; grounds for refusal are limited (Art. 55 mirrors NYC Art. V)

**KSA enforcement**:
- Enforcement via Saudi courts (Saudi Enforcement Law and Execution Court system)
- Saudi Execution Courts (Mahakim al-Tanfeed) established in 2012; relatively efficient
- Bank account attachment; real property attachment
- Exit ban (mana' safari) for individual debtors
- Foreign judgment enforcement: requires Saudi court recognition; bilateral treaty or reciprocity basis

**Lebanon enforcement** (highly challenging):
- Beirut Courts of First Instance; formal system but enforcement is challenging in practice
- Banking secrecy: Lebanon's banking secrecy law has historically made bank account attachment very difficult (though some reforms post-2019)
- Travel ban possible for individual debtors
- Foreign judgment recognition: Lebanese courts apply reciprocity principle; French judgments are routinely recognized; UK and US judgments on a case-by-case basis

**Egypt enforcement**:
- Execution Law (Law No. 308 of 1955, as amended); Egyptian Enforcement Courts
- Attachment of bank accounts; movable assets; real estate
- Foreign judgment enforcement: Egyptian courts recognize foreign judgments meeting specific criteria under Egyptian Code of Civil Procedure; bilateral treaties apply

### Step 4 — Cross-border enforcement under the New York Convention

For arbitral awards, the New York Convention on the Recognition and Enforcement of Foreign Arbitral Awards (1958) provides the primary framework. All GCC states (UAE, KSA, Kuwait, Bahrain, Qatar, Oman) are NYC signatories; Lebanon and Egypt are also signatories.

**Enforcement process**:
1. File application in the enforcement court of the jurisdiction where assets are located
2. Submit: certified copy of the award; certified copy of the arbitration agreement; certified translations into the local language
3. Respondent may oppose on limited NYC Art. V grounds only: incapacity, invalid arbitration agreement, procedural irregularities, award set aside at seat, non-arbitrability, public policy
4. If application successful: court issues an enforcement order (exequatur or equivalent)
5. Proceed to execution against specific assets

**NYC Art. V public policy defense in MENA**:
- Courts in some MENA jurisdictions have used the "public policy" exception broadly in the past; more recent jurisprudence (especially in UAE and KSA) has narrowed this
- Awards against state entities may be subject to sovereign immunity defenses
- Awards that offend Islamic commercial principles (riba in KSA) have been challenged

### Step 5 — Prioritize enforcement actions

Recommend enforcement sequence:
1. Bank account attachment first (fastest recovery; most liquid asset)
2. Real property attachment second (requires more process but creates security)
3. Share attachment in UAE companies (useful for value or leverage)
4. Travel ban / exit ban (powerful leverage against individual debtors; forces negotiation)
5. Settlement negotiation: a judgment in hand gives strong leverage; sometimes enforcement is used to force a settlement on better terms than the judgment

## Jurisdictional notes

| Enforcement step | UAE | KSA | Lebanon | DIFC |
|---|---|---|---|---|
| Bank account freeze | Yes — via Execution Court order | Yes — via Saudi Execution Court | Very difficult (banking secrecy) | Yes — via court order |
| Real property seizure | Yes | Yes | Yes in principle; practically slow | N/A (no DIFC real estate) |
| Travel ban | Yes — powerful tool | Yes (mana' safari) | Available | N/A |
| Foreign judgment recognition | Yes for NYC countries; bilateral treaties | Yes for GCC countries + bilateral | Reciprocity basis | Common-law mutual recognition |
| NYC award enforcement | Yes (Federal Arbitration Law 2018) | Yes | Yes | Yes — DIFC Arbitration Law |

## Common mistakes

- **Enforcing a non-final judgment**: In all jurisdictions, only final, binding, and executory judgments can be enforced. Check the appeal status and the judgment's finality certificate.
- **Ignoring the limitation period**: Enforcement rights expire. UAE: 15 years for court judgments but periodic renewal required to keep attachment orders alive. Check jurisdiction-specific rules.
- **No asset intelligence**: Pursuing enforcement without identifying specific assets leads to wasted court fees and time. Front-load asset tracing.
- **Underestimating Lebanon's banking secrecy barrier**: Lebanon's banking secrecy law (Law 3/1956) has historically blocked bank account attachment orders; take specialist Lebanese counsel advice.
- **Missing the Arabic requirement**: In UAE and KSA enforcement filings, all documents must be in Arabic or accompanied by certified Arabic translations; missing this causes rejection of the application.

## Related skills

- [[prompt-pack-injunction-application]]
- [[prompt-pack-draft-legal-notice]]
- [[prompt-pack-discovery-request]]
- [[prompt-pack-emergency-arbitrator-application]]
