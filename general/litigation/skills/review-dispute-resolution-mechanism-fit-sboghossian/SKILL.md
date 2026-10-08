---
name: review-dispute-resolution-mechanism-fit-sboghossian
title: Dispute Resolution Mechanism — Fit-for-Purpose Review
description: 'Use when a lawyer needs to evaluate whether a dispute resolution clause — arbitration or litigation, institutional or ad hoc — is appropriate for the specific deal and parties. Reviews seat selection, institution, number of arbitrators, language, confidentiality, carve-outs for interim relief, and multi-tier escalation. MENA-focused: covers DIAC (post-2021 DIFC-LCIA absorption), LCIA, SCCA, ICC, and the critical distinction between DIFC/ADGM courts (common law) and UAE onshore courts (civil law) for enforceability of awards and judgments.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-dispute-resolution-mechanism-fit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Dispute Resolution Mechanism — Fit-for-Purpose Review

Assessment of whether the dispute resolution clause in a contract is appropriately structured for the nature of the deal, the parties, the likely disputes, and the enforcement landscape. A poorly drafted DR clause is discovered only at the worst possible time — when a dispute has already arisen and the mechanism fails.

## When to use this

- Reviewing any commercial contract with a DR clause before execution
- Structuring a cross-border MENA transaction and selecting the appropriate forum
- Identifying whether a DR clause from a standard template is appropriate for a specific deal
- Post-dispute: checking whether an existing clause is valid and workable before commencing proceedings

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| The DR clause (verbatim) | The specific text to be reviewed | Required |
| Deal type and size | Complexity, value, and nature of likely disputes shapes the right mechanism | Required |
| Parties' nationalities and domiciles | Determines enforcement routes and seat options | Required |
| Governing law | The governing law and the arbitration seat are separate but interrelated choices | Required |
| Enforcement priorities | Where assets are located determines which enforcement routes matter | Provide if known |

## Review framework

### 1. Arbitration vs litigation: which is appropriate?

| Factor | Favors arbitration | Favors litigation |
|--------|------------------|------------------|
| Cross-border parties | ✅ NY Convention enforcement | ✅ Only if there is a mutual enforcement treaty |
| Confidentiality | ✅ Default in most arbitration rules | ❌ Generally public |
| Speed (first instance) | ❌ Often slower than competent court | ✅ Courts can be faster for simple disputes |
| Interim relief urgency | ⚠️ Court carve-out needed | ✅ Courts grant injunctions quickly |
| Technical complexity | ✅ Party-appointed expert arbitrators | ❌ Judges may lack technical expertise |
| Domestic enforcement (UAE onshore) | ⚠️ UAE arbitration enforcement has improved but requires court ratification | ✅ Onshore court judgment directly enforced |
| Appellate review | ⚠️ Very limited appeal rights | ✅ Full appellate review |

**Recommendation rule**: For any deal where the parties are in different jurisdictions and the other party's assets are primarily outside the UAE/KSA, arbitration with a recognized international institution is almost always preferable because of NY Convention enforcement.

### 2. Seat of arbitration

The seat is the legal domicile of the arbitration — it determines:
- Which national courts supervise the arbitration (set-aside applications go to seat courts)
- The procedural law supplement (where the arbitration rules are silent)
- The enforceability of the award in the seat jurisdiction

| Seat | Key features | Suited to |
|------|-------------|-----------|
| **DIFC (Dubai)** | English common law; DIFC Courts supervise; NY Convention via UAE; strong pro-arbitration courts; English language | MENA cross-border deals; parties wanting UAE enforceability with international recognition |
| **Abu Dhabi (ADGM)** | English common law; ADGM Courts supervise; NY Convention via UAE | Abu Dhabi nexus deals; same advantages as DIFC |
| **London** | English law; EWHC supervises; pro-arbitration; NY Convention | International deals; parties familiar with English law |
| **Paris** | French law; Court of Appeal (Paris) supervises; NY Convention | Francophone MENA (Lebanon); civil-law parties |
| **Geneva / Zurich** | Swiss law; very neutral; NY Convention | High-value, neutral-seat preference |
| **Singapore** | English common law; SIAC home seat; NY Convention | Asia-MENA corridor |
| **Riyadh (SCCA)** | Saudi law; SCCA supervises; not New York Convention | KSA-only deals; parties willing to rely on reciprocal treaty enforcement |

**KSA enforcement alert**: Saudi Arabia has not ratified the New York Convention. A DIAC/LCIA/ICC arbitration award against a KSA party must be enforced via the Riyadh Arab Convention (limited scope) or a bilateral treaty, or by obtaining a KSA court judgment recognizing the award. This is a critical consideration for any deal where the primary enforcement jurisdiction is KSA.

### 3. Arbitral institution

| Institution | Rules version | Strengths | MENA use |
|---|---|---|---|
| **DIAC** (Dubai International Arbitration Centre) | 2022 Rules | Post-DIFC-LCIA absorption; increased caseload; Dubai government backing | Standard for UAE/MENA deals; large regional caseload |
| **LCIA** (London Court of International Arbitration) | 2020 Rules | International reputation; well-developed case law on rules interpretation; flexible procedures | Common for international MENA transactions; favored by English-law parties |
| **ICC** (International Chamber of Commerce) | 2021 Rules | Global gold standard; terms of reference; scrutiny function; good for complex multi-party disputes | Preferred for very large transactions; adds cost and time vs smaller institutions |
| **SCCA** (Saudi Center for Commercial Arbitration) | 2023 Rules | Growing; Saudi-government backed; Arabic/English | Best option when KSA-domestic enforcement is primary concern |
| **HKIAC** | 2018 Rules | Strong Asia-MENA connection; competitive costs | Asia-MENA corridor |
| **SIAC** | 2016 Rules | Efficient; competitive costs; good emergency arbitrator track record | Asia-Pacific deals with MENA nexus |

**DIFC-LCIA formal note**: The DIFC-LCIA arbitration centre was formally wound down and absorbed into DIAC in 2021. New contracts should reference DIAC, not DIFC-LCIA. Existing DIFC-LCIA clauses remain valid for disputes under those contracts.

### 4. Number of arbitrators

| Dispute value | Standard | Rationale |
|---|---|---|
| < USD 2M | 1 arbitrator | Cost and speed outweigh benefit of a three-member tribunal |
| USD 2M – USD 10M | 1 or 3 (by agreement) | Consider complexity; 3 for legally complex matters |
| > USD 10M | 3 arbitrators | Standard for large disputes; one arbitrator per party + presiding arbitrator |
| Any emergency arbitration | 1 emergency arbitrator (institution-appointed) | Established under DIAC 2022, LCIA 2020, ICC 2021 rules |

### 5. Language

- For DIFC/ADGM-seat arbitration: English is the default
- For UAE onshore court proceedings: Arabic is mandatory
- For DIAC: Arabic or English; specify in the clause
- For SCCA: Arabic or English; Arabic is common
- For Lebanese arbitration: French or Arabic

**Mixed-language contracts**: a contract in English with an Arabic translation — which governs? Specify explicitly. In a UAE court proceeding, an Arabic translation will be required; ensure the translation is certified and consistent.

### 6. Confidentiality

| Forum | Default |
|-------|---------|
| Most international arbitration (LCIA, DIAC, SCCA) | Confidential (default under rules) |
| ICC | Not confidential by default under ICC Rules (must be agreed) |
| DIFC Courts | Public (court proceedings are public by default) |
| UAE onshore courts | Public |
| UK courts | Public |

Specify confidentiality expressly in the clause if it matters: "The arbitration proceedings, all materials submitted in the arbitration, and the award shall be kept confidential, except as required by applicable law."

### 7. Interim relief carve-out

Arbitrators can grant interim relief, but:
- It takes time to constitute the tribunal (weeks to months)
- Interim awards may require court enforcement

For urgent injunctions (preventing asset dissipation, preserving evidence, stopping an ongoing breach), a carve-out to court is essential:

"Nothing in this clause prevents either party from seeking interim or provisional relief from a court of competent jurisdiction."

For DIFC-seat arbitration, the DIFC Courts are the natural court for interim relief and enforce well.

### 8. Multi-tier dispute resolution

A multi-tier clause requires parties to attempt negotiation, then mediation, before arbitration. These clauses are enforceable only if they are precise:
- The obligation to negotiate/mediate must be triggered by a specific notice and have a specific duration before the next tier can be invoked
- Vague provisions ("the parties shall endeavor to resolve disputes amicably") are generally not enforceable as conditions precedent to arbitration
- MENA courts (DIFC, ADGM) have upheld multi-tier clauses when the conditions precedent are clearly defined

**Recommended formulation**: specify a 30-day senior-management negotiation period, followed by an optional 30-day mediation with a named mediator (or DIAC/LCIA mediation), before arbitration may be commenced.

## Output format

```json
{
  "issues": [
    {
      "aspect": "Seat | Institution | Arbitrators | Language | Confidentiality | Interim Relief | Multi-tier | Enforceability",
      "current": "description of what the clause currently says",
      "recommended": "description of what should be changed",
      "reasoning": "why the current formulation is problematic",
      "severity": "critical | material | minor"
    }
  ],
  "overallFit": "good | marginal | poor",
  "overallFitRationale": "2–3 sentence summary of the overall assessment"
}
```

## Common issues found

1. **Seat not specified**: without a seat, the arbitration has no supervisory court and no procedural law supplement — the clause may be unenforceable
2. **DIFC-LCIA reference in a new contract**: institution no longer exists; replace with DIAC
3. **No carve-out for interim relief**: urgent injunctions will require commencing a separate court action with uncertain jurisdiction
4. **Multi-tier clause with vague timing**: "the parties shall try to resolve the dispute" — not a condition precedent; arbitration can commence immediately
5. **Arbitration clause in a KSA-law contract without KSA NY Convention analysis**: enforcement via reciprocal treaty only
6. **Arabic mandatory in arbitration for a UAE onshore entity party**: proceedings may need to be Arabic-language or use certified translation

## Related skills

- [[review-governing-law-conflict]]
- [[review-contract-redline]]
- [[research-court-procedure-lookup]]
- [[research-jurisdiction-comparison]]
