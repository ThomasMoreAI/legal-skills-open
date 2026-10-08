---
name: review-liability-cap-reasonableness-sboghossian
title: Liability Cap Reasonableness Review
description: Use when assessing whether a contract's liability cap is reasonable given the deal type, contract value, risk profile, and applicable jurisdiction. Covers cap structure analysis, common carve-outs, anti-patterns, and jurisdiction-specific enforceability rules. Produces a rated assessment with recommended position (ideal / acceptable / walk-away) calibrated against market norms for the contract type.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-liability-cap-reasonableness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Liability Cap Reasonableness Review

## When to use this

Use this skill when a contract contains a limitation of liability clause and you need to assess whether the cap:
- Is appropriately sized for the contract value and risk profile
- Contains the right carve-outs for high-risk categories
- Is consistent across the indemnification and general liability sections
- Is enforceable in the governing jurisdiction

This is a specialized sub-review. Run alongside [[review-indemnification-balance]] and [[review-msa-deep-review]] for a complete commercial contract review.

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Contract text | The limitation of liability clause plus indemnification and carve-out provisions | Required |
| Contract type | SaaS / professional services / outsourcing / construction / supply / M&A — caps differ by type | Infer from contract |
| Contract value | Fees paid / TCV — the cap is sized relative to this | Required for assessment |
| Party perspective | Which party are you acting for? Determines which direction to push | Ask if unclear |
| Jurisdiction | Enforceability rules vary; some jurisdictions void caps for certain conduct | From governing-law clause |

## Cap Structures — Ranked

The following structures are listed in order from most Provider-friendly (lowest exposure) to most Client-friendly (highest exposure):

| Rank | Structure | Typical context |
|---|---|---|
| 1 | Fees paid in preceding **3 months** | Very short SaaS contracts; aggressive Provider position |
| 2 | Fees paid in preceding **6 months** | Short-term or low-value SaaS; often unacceptable for multi-year |
| 3 | Fees paid in preceding **12 months** | Market standard for SaaS and commercial services |
| 4 | Fees paid in preceding **24 months** | Balanced for mid-term contracts; stronger Client position |
| 5 | **2× annual fees** | Acceptable for services where Provider's value significantly exceeds fees |
| 6 | **Total Contract Value (TCV)** | Full-term exposure; reasonable for high-risk engagements |
| 7 | **Specified absolute amount** (e.g., USD 5,000,000) | Common in M&A representations and warranties |
| 8 | **Uncapped** | Rare in commercial contracts; reserved for IP indemnity, fraud, death/personal injury |

## Reasonableness Factors

Apply these factors to calibrate whether the cap is appropriate:

### Factor 1 — Contract Value Scaling

A cap should scale with the value the Protected Party is getting from the deal:
- A cap of 12-month fees on a 5-year, USD 10M TCV contract means the Client can only ever recover USD 2M from a USD 10M deal — that's 20% of total value at risk.
- Rule of thumb: the cap should cover at least the value the Protected Party has a reasonable expectation of recovering if the agreement fails entirely.

### Factor 2 — Data Sensitivity

If the contract involves processing of personal data, sensitive personal data, or financially sensitive data:
- The risk of a data breach may dwarf the contract value (GDPR fines can reach 4% of global annual turnover; KSA PDPL fines up to SAR 5M; UAE PDPL fines up to AED 20M)
- Market trend: data breach indemnity and liability arising from privacy violations is increasingly carved out of the general cap entirely
- Flag if: data breach is included within a general 12-month fees cap — this is commercially inadequate for any meaningful data-processing engagement

### Factor 3 — IP at Stake

IP indemnification is almost universally carved out from the general liability cap:
- The rationale: a vendor who infringes a third-party patent has exposed the Client to an injunction and royalty claims that may massively exceed the contract value
- An IP cap aligned with the general liability cap effectively gives the vendor unlimited freedom to infringe
- Flag if: IP indemnity is subject to the same cap as general liability

### Factor 4 — Length of Contract vs. Cap Period

For multi-year contracts with a 12-month rolling cap:
- Year 1: client has exposure covered by fees paid in year 1
- Year 3: client has only the most recent 12 months of fees available — long tail is unprotected
- Better structure: TCV cap or 2× annual fees to avoid shrinking coverage relative to the full engagement

### Factor 5 — Insurance Limits

Where the contract requires the Provider to maintain professional indemnity, cyber liability, or E&O insurance, the insurance limits form a natural floor for what the cap should be:
- If Provider's cyber insurance is USD 5M but the liability cap is USD 500K, the insurance serves no purpose for the Client
- Align: cap should be at least as high as the required insurance limits

### Factor 6 — Jurisdiction-Specific Enforceability

| Jurisdiction | Cap enforceability rule |
|---|---|
| UK / DIFC / ADGM | Unfair Contract Terms Act 1977 (UK) and DIFC Contract Law equivalents: caps must satisfy a "reasonableness test" in B2C and some B2B contexts; caps against death or personal injury void |
| UAE (onshore) | Civil Code allows courts to adjust contractual penalty/damages provisions to reflect actual loss; a cap much lower than actual loss may be judicially increased |
| KSA | Shariah-derived principles: courts have broad discretion to adjust disproportionate limitations; caps for gross negligence or willful misconduct may not be enforceable |
| France | Code civil: limitation clauses may be set aside for gross negligence (faute lourde) or intentional misconduct (dol); courts will not enforce caps that are manifestly disproportionate |
| Lebanon | Code des obligations et des contrats: similar to French law; caps for gross negligence may be void |
| Egypt | Civil Code follows similar civil-law tradition; gross negligence and intentional tort exclude caps |
| Germany | BGB §§ 307–309: caps must survive AGB (standard terms) review for B2B contracts; exclusion of liability for negligently caused damage is limited |
| US | Generally enforceable between sophisticated commercial parties; some states void consequential-damages exclusions in certain consumer/construction contexts |

### Factor 7 — Carve-Out Consistency

The general liability cap should contain carve-outs for specific high-risk categories. Map carve-outs in the cap clause against what is actually covered in the indemnification and other sections:

**Standard carve-outs from the general cap** (should NOT count against it):

| Carve-out | Rationale |
|---|---|
| IP infringement indemnity | Unlimited third-party exposure; should have its own sublimit or be uncapped |
| Breach of confidentiality | Damages may be speculative but strategic exposure is large |
| Willful misconduct / fraud | Public policy in virtually every jurisdiction |
| Gross negligence | Civil-law jurisdictions; increasingly in common law |
| Death or personal injury | Statutory void of cap in UK, DIFC, ADGM, many EU jurisdictions |
| Data breach with regulatory penalties | GDPR/PDPL fines are third-party regulatory actions; cap should not include them |
| Indemnification obligations themselves | Avoid making the indemnification circular with the cap |

**Mismatch flag**: cap section uses "gross negligence" but indemnification section uses "willful misconduct only" — creates a gap where gross-negligence IP infringement is still capped.

## Anti-Patterns to Flag

| Anti-Pattern | Why It Matters | Severity |
|---|---|---|
| 12-month fees cap on a 5-year contract | Long tail of contract entirely uncapped; severe for high-value engagements | High |
| Same cap applies to all damages including IP indemnity | Vendor effectively has no IP infringement exposure beyond 12 months of fees | Critical |
| "Reasonable" fees cap not defined numerically | Cap is unenforceable as indefinite | Critical |
| Cap covers data-breach damages including regulatory fines | GDPR / PDPL fines are not contractually cappable — they arise by operation of law; the clause may be misleading | High |
| Cap survives termination but carve-outs do not | Indemnities survive but the sublimit is now zero because the cap has expired | High |
| Mutual caps framed so that only Provider's cap is meaningful | Asymmetric risk without commercial justification | Medium |
| No carve-out for death/personal injury | Void in UK, DIFC, ADGM; unenforceable | Critical in those jurisdictions |

## Output Format

```json
{
  "cap_structure": {
    "type": "12-month-fees | 24-month-fees | 2x-annual | TCV | fixed-amount | uncapped",
    "amount_described": "<as drafted>",
    "estimated_amount_USD": <number or null>
  },
  "reasonableness_rating": 1-5,
  "recommended_position": {
    "ideal": "<description>",
    "acceptable": "<description>",
    "walk_away": "<description>"
  },
  "carve_out_analysis": [
    {
      "category": "ip | data-breach | fraud | death | confidentiality | ...",
      "status": "carved-out | within-cap | silent",
      "issue": "<if any>"
    }
  ],
  "jurisdiction_enforceability": "<note on governing law>",
  "anti_patterns": [
    { "pattern": "...", "severity": "critical|high|medium|low" }
  ]
}
```

Reasonableness rating: 1 = severely inadequate (Protected Party barely protected); 3 = market-standard; 5 = very strong (Protected Party well-protected).

## Jurisdictional Notes on Market Standards

**SaaS / commercial services (global market)**:
- 12-month fees is the market standard for Provider-side drafting
- Clients routinely push for 2× annual fees or TCV for contracts involving significant data or IP reliance
- IP indemnity: market is converging on uncapped or separate sublimit of 2× annual fees

**Construction / FIDIC contracts (MENA)**:
- FIDIC Red Book / Silver Book: liability cap often linked to Contract Price; exclusions for fraud and wilful misconduct are standard
- UAE construction: courts have historically been willing to reduce disproportionate penalty clauses (Civil Code adjustability)

**M&A (Representations and Warranties)**:
- Seller's liability cap for general reps: typically 20–30% of transaction value
- Seller's cap for fundamental reps (title, authority, taxes): often 100% of transaction value
- Fraud: uncapped by market convention

## Related Skills

- [[review-indemnification-balance]]
- [[review-msa-deep-review]]
- [[review-risk-flagging]]
- [[review-unusual-terms-detector]]
- [[draft-msa]]
