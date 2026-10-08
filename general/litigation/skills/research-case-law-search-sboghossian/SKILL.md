---
name: research-case-law-search-sboghossian
title: Case Law Search
description: Use when a lawyer or researcher needs to find relevant court decisions or arbitral awards on a specific legal issue in a specific jurisdiction. Covers primary MENA courts (Lebanese Cassation, KSA General/Commercial/Labor courts, UAE onshore, DIFC Courts, ADGM Courts) as well as UK, EU, France, and US sources. Triggers on queries about precedent, case outcome, how courts have interpreted a rule, or whether a position is "good law." Never fabricates citations; says so if no verified case is found.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-case-law-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Case Law Search

Find and analyze court decisions and arbitral awards on a specific legal issue. This skill structures the search, selects the right source by jurisdiction, retrieves verified decisions, and formats them for practitioner use. It never fabricates citations.

## When to use this

- Researching how courts have interpreted a specific statutory provision or contractual clause
- Finding authority on whether a legal position is well-established or contested
- Locating precedent for a memo, brief, or legal opinion
- Checking whether a principle is "good law" (still followed, or overruled / distinguished)
- Building a table of authorities for a court submission
- Advising a client on litigation risk based on how courts have decided similar disputes

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Legal issue | Specificity drives result quality — "non-compete enforceability post-FDL 33/2021" is far more useful than "employment law" | Required |
| Jurisdiction | Each jurisdiction has distinct sources; mixing them produces unreliable results | Required — use [[router-jurisdiction-detector]] if unclear |
| Date range | Recent decisions are stronger; landmark older decisions may still be controlling | Last 10 years; broaden on request |
| Court level | Apex / cassation decisions bind lower courts; first-instance decisions are persuasive at best | Default: apex first, then appellate |
| Purpose | Memo, brief, client advice, deal support — shapes formatting depth | Infer from context |

## Research pipeline

### Step 1 — Identify jurisdiction and issue
Confirm jurisdiction via [[router-jurisdiction-detector]] if not explicit. Restate the legal issue with precision — the more specific the issue, the more targeted the search and the lower the hallucination risk.

### Step 2 — Select authoritative source by jurisdiction

| Jurisdiction | Primary sources | Notes |
|---|---|---|
| **LB (Lebanon)** | Lebanese Court of Cassation official reports; Al-Adliya bulletin; [[connector-legal-data-hunter]] | Arabic + French; English translations rare. Confirm whether Cour de Cassation or Conseil d'État (administrative matters). |
| **KSA (Saudi Arabia)** | Najiz portal (MOJ public rulings — limited); [[connector-legal-data-hunter]]; Ministry of Commerce commercial court decisions | Arabic. Sharia court system — courts of first instance, Courts of Appeal, Supreme Court. Commercial Courts (established 2017) separate track. |
| **UAE (onshore)** | Dubai Courts public rulings portal; Abu Dhabi courts portal; [[connector-legal-data-hunter]] | Arabic. Federal Supreme Court (Mahkama Itihadia Ulya) for federal-law questions. |
| **DIFC** | DIFC Courts official case database (difccourts.ae) | English. Common law. Precedent from the DIFC Court of First Instance and Court of Appeal; also draws on English law persuasive authority. |
| **ADGM** | ADGM Courts official database | English. Common law. Draws on English law. |
| **UK** | BAILII (bailii.org); National Archives (legislation.gov.uk for statutory instruments); [[tool-web-search-orchestrator]] for UKSC recent decisions | Free. For commercial matters, EWHC (Comm) decisions are the core. |
| **EU** | [[connector-eur-lex]]; CURIA (Court of Justice of the EU) | ECLI citation format. |
| **FR** | [[connector-legifrance]]; Légifrance jurisprudence | French; Cour de Cassation and Conseil d'État are the apex courts. |
| **US** | [[tool-courtlistener-US]] (free); Westlaw / LexisNexis (if access available); [[connector-sec-edgar]] for securities enforcement | US is state-by-state for most matters; federal circuit for federal questions. |

### Step 3 — Search and filter

Search using:
1. Key terms from the legal issue (exact statutory phrases, well-known principle names)
2. Party type identifiers (commercial entity, employer, consumer) to narrow to analogous fact patterns
3. Date filter (default: most recent 10 years; for foundational principles, extend further)
4. Court level filter (apex / cassation > appellate > first instance)

Do not retrieve more than 10 cases unless the user has requested a comprehensive survey.

### Step 4 — Verify each case

**Anti-hallucination rule**: never include a case that has not been verified as existing in an authoritative source. If the database returns a partial match or the case cannot be confirmed, exclude it and note the gap.

For each candidate case:
- Verify the caption (parties' names), court, year, and docket match the source record
- Confirm the holding stated matches the decision text
- Check citator status if available (still good law? overruled? distinguished?)

## Output structure

For each case retrieved, produce:

```
**[Party A] v [Party B]**
Court: [full court name]  |  Year: [YYYY]  |  Docket: [number if available]
Citation: [official citation]

Facts (2–3 sentences): [what happened, who is suing whom, over what]

Holding (1 sentence): [what the court decided on the specific issue]

Key principle (1–2 sentences): [the legal rule extracted from the decision, stated abstractly so it can be applied to other facts]

Pin-cite: [paragraph / page number where the principle is stated, if available]

Citator status: [still good law / distinguished in X / overruled by Y / no subsequent treatment found]

Relevance to user's issue: [1 sentence explaining why this case matters to the specific query]
```

If comparing to the user's situation, add:
```
Distinguishing facts: [factual differences that may limit the case's application here]
```

## Anti-hallucination rules

1. **Never invent case citations.** If no real case is found, say so explicitly: "No verified precedent found in [jurisdiction] on [issue] within the search scope."
2. **Never paraphrase a holding** in a way that extends beyond what the text of the decision actually says.
3. **Never treat a lower-court decision as binding** — clearly label persuasive vs binding authority.
4. **Never treat a case decided before a statutory amendment as authority on the amended provision** without checking whether the amendment changed the applicable rule.
5. If confidence in a citation is below "verified," do not include it. See [[router-confidence-scorer]] cite-or-bust rule.

## MENA-specific notes

### Arabic-language court systems
KSA and UAE onshore courts publish in Arabic. English summaries, where they exist, are unofficial and may omit nuance. For high-stakes matters, obtain the Arabic original and have it reviewed by a native-language-qualified lawyer.

### Sharia-law courts (KSA)
Saudi courts are Sharia-based. Precedent functions differently: the principle of binding stare decisis does not apply in the same way as in common law; the court exercises independent ijtihad. However, Sharia legal opinions (fatwa) from the Council of Senior Scholars carry significant persuasive weight. The Commercial Courts (2017) operate under more codified rules.

### DIFC and ADGM: common law islands
DIFC and ADGM are common-law jurisdictions within UAE. Their courts expressly cite and apply English cases as persuasive authority, making English High Court and UK Supreme Court decisions highly relevant. A case decided by the DIFC Court of Appeal is binding on the DIFC Court of First Instance.

### The DIFC–Dubai onshore relationship
The DIFC Courts and the Dubai onshore courts operate under a judicial-transfer protocol. A DIFC Court judgment can be enforced onshore and vice versa. However, the applicable substantive law differs, so a DIFC case applying DIFC Contract Law is not directly binding on Dubai onshore courts applying UAE Civil Code.

### New UAE federal legislation (post-2021)
UAE has undergone significant legislative reform since 2021 (new Companies Law, Labor Law FDL 33/2021, new Personal Status Law). Cases decided before these reforms may be on different statutory text — always check whether the statutory basis for the decision has changed.

## Limits and escalation

- MENA public case-law databases are incomplete. Unreported decisions (which may represent the majority of first-instance decisions) are not accessible without direct court filing.
- In KSA, many commercial arbitration awards are not published. The Saudi Center for Commercial Arbitration (SCCA) does not maintain a public awards database.
- If the user needs exhaustive research for a high-stakes matter (client opinion, court filing), escalate to [[research-deep-research-orchestrator]] and pair with [[research-recent-amendments-tracker]] to check whether cited statutes have been amended.

## Related skills

- [[research-statute-lookup]]
- [[research-recent-amendments-tracker]]
- [[research-precedent-finder]]
- [[research-deep-research-orchestrator]]
- [[router-jurisdiction-detector]]
- [[router-confidence-scorer]]
