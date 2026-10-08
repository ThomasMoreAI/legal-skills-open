---
name: prompt-pack-arbitration-agreement-clause-sboghossian
title: Arbitration Agreement Clause
description: Use when drafting an arbitration clause for insertion into a contract, selecting an arbitration institution (ICC, LCIA, SIAC, DIAC, CRCICA, or ad hoc UNCITRAL) and specifying seat, governing law, language, number of arbitrators, and procedural rules. Arbitration practice area; particularly important for MENA contracts where choice of seat and institution affects enforceability and interim relief availability.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-arbitration-agreement-clause
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Arbitration Agreement Clause

## When to use this

Use this skill when drafting a **dispute resolution clause** that selects arbitration as the mechanism, for insertion into:
- Commercial contracts (sale, service, construction, agency, distribution)
- Joint venture agreements
- Shareholder agreements
- Licensing agreements
- Investment agreements

This skill is particularly critical in the MENA context: the choice of seat, institution, and governing law determines not only procedural rules but also whether an award can be enforced in the relevant country, whether emergency arbitrators are available, and what courts will supervise the arbitration.

---

## Prompt template

> Draft an arbitration clause for [type of contract] selecting [arbitration institution: ICC/LCIA/SIAC/DIAC/other]. Specify seat of arbitration, governing law, language, number of arbitrators, and any specific procedural rules or expedited procedures.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Contract type | Construction/engineering disputes have different complexity from simple services |
| Arbitration institution | Determines the procedural rules that will govern |
| Seat of arbitration | Most important decision — sets the legal framework for the arbitration and enforcing courts |
| Number of arbitrators (1 or 3) | 1 arbitrator is faster and cheaper; 3 is standard for large disputes |
| Governing law of the contract | Separate from seat; the law governing the substance of the dispute |
| Language | Language of proceedings and award |
| Dispute value threshold for expedited procedure | When to trigger fast-track rules |

---

## Key decisions and their implications

### 1. Choice of institution

| Institution | Notes |
|-------------|-------|
| **ICC** (International Court of Arbitration) | Global gold standard; scrutiny of awards by the Court; high administrative fees; suitable for large, complex, multi-party disputes; Paris/Singapore/other seats available |
| **LCIA** (London Court of International Arbitration) | Efficient; lower fees than ICC; London seat historical default but any seat available; strong in energy and banking |
| **SIAC** (Singapore International Arbitration Centre) | Asia's leading institution; strong enforceability in Southeast Asia and increasingly MENA; Singapore seat default |
| **DIAC** (Dubai International Arbitration Centre) | Primary institutional arbitration in UAE; 2022 Rules; strong enforceability in UAE courts; DIFC-LCIA model now subsumed into DIAC |
| **CRCICA** (Cairo Regional Centre for International Commercial Arbitration) | Egypt and Africa focus; UNCITRAL Rules-based; awards enforceable in Egypt and New York Convention states |
| **BCDR-AAA** (Bahrain) | GCC and Islamic finance disputes; Bahrain seat |
| **SCCA** (Saudi Centre for Commercial Arbitration) | Saudi Arabia; Saudi Arbitration Law 2012; Riyadh seat; increasingly credible for Saudi-connected disputes |
| **DIFC Arbitration** | DIFC-seated arbitration under DIAC or ad hoc rules; DIFC Courts can directly enforce awards (bypassing onshore courts) |
| **UNCITRAL (ad hoc)** | No institution; flexible; PCA administrative services available; cost-efficient for straightforward disputes; requires parties to agree on all procedural steps |

### 2. Seat of arbitration

The seat (legal domicile of the arbitration) determines:
- Which national courts supervise the arbitration
- The grounds for setting aside the award
- Whether interim measures (injunctions, asset freezes) are available from local courts
- The form of the arbitration agreement required by local law

**MENA seat options**:

| Seat | Legal framework | Enforcement notes |
|------|----------------|-----------------|
| Dubai (DIFC) | DIFC Arbitration Law (Law No. 1 of 2008 as amended); UNCITRAL Model Law-based | Awards enforced via DIFC Courts; DIFC Courts can enforce directly in onshore UAE via a gateway mechanism |
| Dubai (onshore) | UAE Federal Arbitration Law (Federal Law 6/2018); UNCITRAL Model Law-based | Awards enforced via Dubai Courts; UAE is New York Convention signatory |
| Abu Dhabi (ADGM) | ADGM Arbitration Regulations 2015; UNCITRAL Model Law | Similar to DIFC; enforced via ADGM Courts |
| Riyadh | Saudi Arbitration Law (Royal Decree M/34/2012); UNCITRAL Model Law-based | Awards enforced by Saudi courts; Sharia-law compliance required |
| Cairo | Egyptian Arbitration Law No. 27/1994; UNCITRAL Model Law | Awards enforced by Egyptian courts; Egypt is New York Convention signatory |
| Beirut | Lebanese Arbitration Law (Code of Civil Procedure arts. 762–808); UNCITRAL Model Law-influenced | Awards enforceable; Lebanon is New York Convention signatory |
| London | English Arbitration Act 1996 | Highly developed case law; party-friendly; awards widely enforceable |
| Paris | French Code of Civil Procedure (arts. 1442–1527) | ICC home; strong pro-arbitration courts |
| Singapore | Singapore International Arbitration Act (Cap. 143A) | SIAC home; highly enforcement-friendly |

### 3. Governing law of the contract vs. seat

These are **separate choices**:
- **Seat** governs the procedure and the courts that supervise
- **Governing law of the contract** governs the substance (what the parties' obligations are)

Example: a UAE company and a French company contracting for services in Lebanon may choose Paris as the seat (French courts supervise), DIAC rules (familiar to the UAE party), and UAE law as governing law (where performance occurs). This is a valid combination.

**Important**: the governing law of the arbitration agreement itself is also separate and may differ from both. In MENA practice, it is common to state the governing law of the arbitration agreement explicitly.

### 4. Number of arbitrators

| Matter size | Recommendation |
|------------|---------------|
| < USD 500K | Single arbitrator (faster, cheaper) |
| USD 500K–5M | Single or three depending on complexity |
| > USD 5M or complex | Three arbitrators (one per party, one presiding) |

Most institutional rules default to one arbitrator unless the parties agree otherwise or the institution determines three is appropriate given the complexity.

---

## Standard clause drafts

### Institutional clause (example: DIAC, Dubai seat)

> Any dispute, controversy or claim arising out of or in connection with this Agreement, or the breach, termination or validity thereof, shall be finally settled by arbitration under the Dubai International Arbitration Centre (DIAC) Rules, as currently in force. The seat of arbitration shall be Dubai, United Arab Emirates. The number of arbitrators shall be [one/three]. The language of the arbitration shall be [English/Arabic/English and Arabic]. The governing law of the arbitration agreement shall be UAE law.

### Ad hoc clause (UNCITRAL, any seat)

> Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, shall be referred to and finally resolved by arbitration in accordance with the UNCITRAL Arbitration Rules. The seat of arbitration shall be [city, country]. The number of arbitrators shall be [one/three]. The language of the arbitration proceedings shall be [language].

### Multi-tier clause (negotiation → mediation → arbitration)

> (a) The parties shall attempt in good faith to resolve any dispute arising out of or in connection with this Agreement through direct negotiations between their senior representatives for a period of [30] days from the date one party notifies the other of the dispute.
> (b) If the dispute is not resolved under (a), the parties shall attempt to resolve it through mediation under [DIAC/DIFC-LCIA/ICC] mediation rules for a period of [30] days.
> (c) If the dispute is not resolved under (b), it shall be finally settled by arbitration under [institution] Rules. [seat, language, arbitrator number as above]

Multi-tier clauses are common in construction and long-term commercial contracts. **MENA trap**: ensure the escalation steps are drafted as conditions precedent, not merely directory — courts have dismissed arbitral proceedings for failure to follow mandatory pre-arbitration steps.

---

## Jurisdictional notes

### UAE
Since UAE Federal Arbitration Law 6/2018, UAE-seated arbitration is fully UNCITRAL Model Law-based and pro-arbitration. DIFC seat is advantageous for enforcement because the DIFC Courts can directly execute awards without going through onshore courts. Note: arbitration cannot be used for disputes that must be decided by UAE government entities (some real estate, employment, administrative matters).

### KSA
Saudi Arbitration Law 2012 allows arbitration with a Saudi seat. Awards are enforced by Saudi courts but may be challenged on Sharia-law grounds. Consider Sharia-compliance of the governing law and award content when selecting a Saudi seat. International awards are enforceable in Saudi Arabia under the New York Convention (KSA acceded in 1994) and Arab League Convention on Commercial Arbitration (1987).

### Lebanon
Lebanon has a developed arbitration tradition (particularly at the Beirut Chamber of Commerce). Enforcement of foreign awards is generally effective. Lebanese courts have set aside awards for public policy violations — define public policy scope in the governing law clause.

### Egypt
Egypt is one of the most pro-arbitration MENA jurisdictions. Egyptian Arbitration Law 1994 is UNCITRAL Model Law-based. Cairo is a major arbitral seat (CRCICA); ICC Africa/Middle East cases also frequently seated in Cairo.

---

## Common mistakes

- Omitting the seat (pathological clause — arbitration cannot proceed without a seat)
- Confusing governing law of the contract with the seat (different choices; make both explicit)
- Ad hoc arbitration without any institutional support in a jurisdiction where party cooperation is uncertain
- Escalation clause drafted as advisory rather than mandatory (courts can dismiss for non-compliance)
- Not addressing emergency arbitrator provisions when interim relief may be needed

---

## Related skills

- [[prompt-pack-arbitration-clause-comparison]] — compare arbitration clauses from different institutions
- [[prompt-pack-arbitration-cost-submission]] — costs submission at the end of an arbitration
- [[prompt-pack-award-enforcement-application]] — enforcing the resulting award
- [[kb-arbitration-mena]] — MENA arbitration law and institution reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction-first drafting
