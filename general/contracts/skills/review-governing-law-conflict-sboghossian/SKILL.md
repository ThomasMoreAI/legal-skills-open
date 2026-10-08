---
name: review-governing-law-conflict-sboghossian
title: Governing Law and Forum Conflict Check
description: 'Use when a contract''s choice-of-law clause and forum-selection clause need to be reviewed for validity, internal consistency, and practical enforceability — particularly in cross-border MENA transactions. Checks: whether the chosen law is validly selected in each jurisdiction (Rome I in EU, freedom of contract in DIFC/ADGM/English law, mandatory rules in KSA/UAE onshore), whether the governing law and forum are compatible, what mandatory overriding rules apply regardless of choice, and whether the award or judgment will actually be enforceable where the assets are. MENA-specific traps: Sharia overlay in KSA, employment/consumer mandatory rules, Islamic finance compliance carve-outs.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-governing-law-conflict
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Governing Law and Forum Conflict Check

Review of a contract's choice-of-law clause, jurisdiction clause, and arbitration clause for internal consistency, validity in each relevant jurisdiction, and practical enforceability. Identifies mismatches between the governing law and the forum, flags mandatory rules that override party autonomy, and assesses enforcement risk where assets are located.

## When to use this

- Reviewing any cross-border commercial contract before execution
- Negotiating a governing law clause when the counterparty insists on their home jurisdiction's law
- Assessing whether an existing contract's DR mechanism and governing law clause are compatible
- Pre-litigation: checking whether the chosen forum can validly hear the dispute under the governing law
- MENA-specific: checking whether a "neutral" governing law choice (e.g., English law) will be respected in KSA or UAE onshore courts

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Governing law clause (verbatim) | The text to be reviewed | Required |
| Forum / jurisdiction clause (verbatim) | The dispute resolution mechanism to be reviewed | Required |
| Parties' nationalities and domiciles | Determines conflict-of-laws rules that apply | Required |
| Subject matter of the contract | Some contracts (employment, consumer, insurance) have overriding mandatory rules | Required |
| Where are the parties' assets located? | Enforcement jurisdiction determines what matters | Provide if known |

## Review framework

### 1. Validity of the choice-of-law clause

**Does the selected law respect the rules of the forum?**

| Jurisdiction | Freedom to choose governing law | Key constraints |
|---|---|---|
| **DIFC / ADGM** | Very broad — common law freedom of contract; party autonomy is the primary rule | Choice must be genuine and not a sham to evade mandatory rules; DIFC Contract Law applies as fallback for gaps |
| **UK / English law** | Very broad under common law | Overriding mandatory provisions (employment, consumer, competition) apply regardless |
| **EU (Rome I Regulation)** | Broad for B2B contracts; restricted for B2C and employment | For consumer contracts: can choose governing law but cannot deprive consumer of protections of habitual residence law; for employment: same — cannot choose law to deprive employee of protections of state where they normally work |
| **UAE onshore** | More limited — UAE Civil Transactions Law gives courts discretion to apply UAE law on certain mandatory matters | For employment contracts: UAE Labor Law (FDL 33/2021) is mandatory regardless of chosen governing law (if employee works in UAE); for real estate: UAE property law is mandatory |
| **KSA** | Most restricted — Sharia principles apply as mandatory overriding rules regardless of contractual choice of law | Choice of English or French law will not be honored if it conflicts with Sharia principles; courts may apply Saudi law to fill gaps; no formal reception of conflict-of-laws principles as developed in common law |

### 2. The governing law vs forum mismatch problem

A governing law clause and a forum clause that are inconsistent create problems:

**Compatible combinations**:
| Governing law | Forum | Assessment |
|---|---|---|
| English law | English High Court | ✅ Natural and consistent |
| English law | LCIA arbitration (London seat) | ✅ Very common international pairing |
| English law | DIFC Courts | ✅ DIFC courts regularly apply English law; good combination |
| DIFC law | DIAC arbitration (DIFC seat) | ✅ Consistent |
| UAE Civil Code | Dubai Courts (onshore) | ✅ Natural domestic pairing |
| English law | DIAC arbitration (Dubai seat) | ✅ Arbitration applies whatever governing law is specified |

**Potentially problematic combinations**:
| Governing law | Forum | Issue |
|---|---|---|
| DIFC law | Onshore Dubai Courts | ⚠️ Dubai onshore courts do not apply DIFC law; DIFC law is applicable only in DIFC courts or by designation in arbitration |
| KSA law | DIAC arbitration (DIFC seat) | ⚠️ DIAC can apply KSA law; but enforcing the award in KSA may face Sharia-compliance scrutiny of DIFC procedural law |
| English law | UAE onshore courts | ⚠️ UAE onshore courts will apply UAE mandatory rules regardless of English law clause; English law may be applied to fill gaps but UAE mandatory rules prevail |
| French law | DIFC Courts | ⚠️ Not a natural pairing; DIFC courts will apply French law if instructed, but familiarity with French civil code may be limited among DIFC bench |

### 3. Mandatory overriding rules

No matter what law the parties choose, certain rules apply regardless:

**Employment (almost universal)**:
- **UAE**: FDL 33/2021 employment protections apply to any employee who works in UAE — choice of English law does not override EOSB, notice, non-compete compensation
- **EU**: Article 8 of Rome I Regulation — employees cannot be deprived of the protection of the mandatory rules of the state where they habitually work
- **KSA**: Saudi Labor Law is mandatory — no choice of law can deprive a KSA-based employee of its protections

**Consumer contracts (EU and increasingly MENA)**:
- Rome I Article 6: consumers retain protection of their habitual residence law regardless of a business-favoring governing law choice

**Competition law / antitrust**:
- Competition law applies where the market is affected, regardless of governing law

**Property law**:
- Immovable property is typically governed by the lex situs — the law of the jurisdiction where the property is located — regardless of contractual choice
- UAE real estate is governed by UAE/emirate property law regardless of an English-law clause

**Data protection**:
- GDPR applies wherever EU personal data is processed, regardless of governing law choice

### 4. Public policy carve-outs

Courts can refuse to apply a chosen foreign law (or enforce a foreign judgment / award) if it conflicts with public policy:

| Jurisdiction | Key public policy carve-outs |
|---|---|
| **KSA** | Sharia principles are overriding public policy; interest-bearing provisions, gambling, alcohol contracts, prohibited products will not be enforced |
| **UAE (onshore)** | Islamic public order; contracts that are immoral or contrary to UAE public policy will not be enforced (e.g., contracts for illegal activities, usurious interest rates, violation of UAE family law) |
| **Lebanon** | Ordre public / public order under Lebanese Civil Code; contracts violating fundamental Lebanese law will not be enforced |
| **EU / UK** | Foreign judgments / awards contrary to EU/UK public policy will be refused enforcement |

**Sharia compliance carve-out (Islamic finance)**:
For Sharia-compliant financial instruments (sukuk, murabaha, istisna'), the contract typically includes a Sharia compliance carve-out: in the event of conflict between the governing law and Sharia requirements, the Sharia fatwa prevails. This carve-out must be drafted precisely — an overbroad Sharia carve-out can render the entire contract uncertain.

### 5. Enforcement analysis

The best governing law clause and forum selection are worthless if the resulting judgment or award cannot be enforced where the assets are.

| Award/Judgment type | Enforcement route | Jurisdictions covered |
|---|---|---|
| **International arbitration award** | New York Convention (1958) | 170+ states including UAE, Lebanon, Egypt, UK, EU member states, France |
| **DIFC Courts judgment** | DIFC-Dubai judicial cooperation protocol (directly executable in Dubai onshore) | Dubai |
| **DIFC Courts judgment** | Common law reciprocal enforcement / comity | Other common-law jurisdictions with reciprocal recognition |
| **English High Court judgment** | Common law enforcement in UAE (must bring new court action recognizing the judgment); direct enforcement in EU under Brussels Regulation recast (for EU judgments only post-Brexit: no automatic enforcement in EU) | UAE: via new action; EU: Brussels recast pre-Brexit |
| **UAE onshore court judgment** | Riyadh Arab Convention (reciprocal between Arab states including Lebanon, KSA); GCC Enforcement Convention | Arab states; GCC |
| **KSA court judgment** | Limited reciprocity; Riyadh Convention; bilateral treaties | Restricted; foreign enforcement is not reliable |
| **Lebanon court judgment** | Limited international recognition; very restricted post-economic crisis | Restricted |

**Key MENA enforcement traps**:
- KSA has not ratified the New York Convention → international arbitration awards against KSA parties require enforcement via the Riyadh Arab Convention or a bilateral treaty → significantly more difficult than NY Convention enforcement
- Lebanon: even a valid Lebanese court judgment is difficult to enforce given the state of the judicial system post-2019
- UAE onshore: foreign court judgments are enforced under the UAE-GCC enforcement protocol and Riyadh Convention; UK and French judgments require a new action in UAE courts unless there is a specific bilateral treaty

### 6. Connection requirement

Some jurisdictions require a "genuine connection" between the contract and the chosen governing law:
- **UAE onshore**: in practice, UAE courts have accepted English or French governing law clauses in commercial contracts without requiring a nexus, but the risk remains for contracts with no international element
- **KSA**: Saudi courts are more likely to apply Saudi law if the chosen foreign law has no nexus to the contract
- **EU (Rome I)**: no connection requirement for B2B contracts — pure freedom of choice

## Output format

```json
{
  "conflicts": [
    {
      "issue": "description of the conflict or problem",
      "severity": "critical | material | minor",
      "recommendation": "specific drafting fix or strategic recommendation"
    }
  ],
  "mandatoryRuleOverrides": [
    {
      "jurisdiction": "UAE",
      "rule": "FDL 33/2021 employment protections",
      "effect": "Apply regardless of English law governing law clause; EOSB and notice rights cannot be contracted out"
    }
  ],
  "enforcementRisk": {
    "primaryEnforcementJurisdiction": "string",
    "mechanism": "NY Convention | DIFC-Dubai protocol | Riyadh Convention | bilateral treaty | new action required",
    "riskLevel": "low | medium | high",
    "riskBasis": "string"
  },
  "recommendedGovernLawClause": "optional — if a better combination is recommended",
  "overallAssessment": "2–3 sentence assessment of the governing law / forum package as a whole"
}
```

## Related skills

- [[review-dispute-resolution-mechanism-fit]]
- [[review-contract-redline]]
- [[research-jurisdiction-comparison]]
- [[research-court-procedure-lookup]]
- [[research-statute-lookup]]
