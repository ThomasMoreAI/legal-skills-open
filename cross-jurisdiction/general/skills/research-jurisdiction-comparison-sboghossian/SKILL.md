---
name: research-jurisdiction-comparison-sboghossian
title: Jurisdiction Comparison
description: Use when a user needs to compare how a specific legal issue is handled across multiple jurisdictions — to choose where to incorporate, where to arbitrate, which governing law to select, or to understand cross-border deal risk. Produces a structured comparison table with per-jurisdiction columns covering statute, rule, enforceability, duration limits, and risk; concludes with a recommendation. Covers MENA (LB, KSA, UAE onshore, DIFC, ADGM, EG) and secondary jurisdictions (UK, US-DE, FR, EU). Each cell must cite a real source.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-jurisdiction-comparison
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Jurisdiction Comparison

Structured multi-jurisdiction comparison of a specific legal issue. Produces a table showing how the issue is treated in each relevant jurisdiction, with per-cell source citations, followed by a practitioner-grade recommendation on which jurisdiction is most favorable for the user's position.

## When to use this

- **Seat selection**: choosing where to incorporate a company, structure a fund, or seat an arbitration
- **Governing-law selection**: negotiating which law governs a contract, especially in cross-border deals
- **Forum selection**: understanding where it is strategic to litigate or arbitrate
- **Cross-border due diligence**: a target company operates in multiple jurisdictions; the buyer needs to understand the patchwork of applicable rules
- **Client memo**: advisor or in-house counsel comparing options for a client making a structuring decision
- **Quick cross-check**: "Is this clause enforceable in all the jurisdictions we operate in?"

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Legal issue | Be specific — "non-compete enforceability" not just "employment" | Required |
| Jurisdictions to compare | Which jurisdictions are relevant to the deal or dispute? | If not stated, use: LB, KSA, UAE, DIFC, UK, US-DE |
| User's position | Employer vs employee; buyer vs seller; lender vs borrower — determines which jurisdiction is "favorable" | State if known |
| Transaction context | Cross-border M&A, employment, finance, IP licensing — affects which axes matter | Infer from issue |
| Output use | Quick comparison vs formal memo vs deal-room reference | Infer from context; assume memo quality unless told otherwise |

## Comparison axes

Select 5–8 axes that are genuinely material for the legal issue. Do not dump all axes — only include axes that could plausibly lead to a different answer across jurisdictions.

### Standard axis menu (pick relevant ones)

| Axis | Use when |
|------|----------|
| Applicable statute / instrument | Always |
| Legal system (civil law vs common law) | When it affects how gaps in the contract are filled |
| Rule / test applied | When the jurisdictions use different legal tests |
| Enforceability (yes / qualified / no) | For restrictive covenants, penalties, choice-of-law |
| Maximum duration / threshold | For limitation periods, non-compete durations, ownership thresholds |
| Consideration requirement | For post-employment restrictions, SAFE instruments |
| Formality / registration requirement | For real estate, charges, IP assignments |
| Governing-law choice respected? | For cross-border contracts |
| Mandatory overriding rules | For employment, consumer, competition law |
| Enforcement / remedy | Injunction availability, damages, specific performance |
| Risk level for user's position | Red / Yellow / Green rating |
| Recent changes | If there has been significant reform in any jurisdiction |

## Output format

### Comparison table

Produce one column per jurisdiction, rows for each selected axis. **Every cell must cite a source** — statute name, regulation number, or case name. If a cell cannot be verified, mark it as "Not verified — confirm with local counsel" rather than leaving it blank or speculating.

Example structure for "Non-compete enforceability in employment contracts":

| Axis | LB | KSA | UAE onshore | DIFC | ADGM | UK | US-DE |
|------|----|----|-------------|------|------|----|-------|
| Statute | Lebanese Labor Law, Arts. 56–57 | Labor Law Royal Decree M/51 of 2005 | UAE Labor Law FDL 33/2021 | DIFC Employment Law | ADGM Employment Regulations | Common law + ERA 1996 | Delaware common law |
| Enforceability | Qualified — proportionality test | Qualified — 2-yr max + scope test | Qualified — 2-yr max + 100km + consideration | Qualified — DIFC courts apply reasonableness test | Qualified — similar to English approach | Qualified — protectable interest + reasonableness | Generally enforced — most US-employer-friendly state |
| Maximum duration | Not codified; courts vary | 2 years | 2 years (FDL 33/2021 Art. 10) | No fixed max; reasonable duration | No fixed max; reasonable duration | No fixed max; reasonable duration | No fixed max |
| Consideration required | None specified | None specified | Compensation payment for restrictive period (FDL 33/2021 Art. 10) | Implicit in employment contract | Implicit in employment contract | In contract; "garden leave" accepted | At time of signing or promotion |
| Risk (employee seeks injunction) | Medium | Medium | High (recent reform strengthens) | Medium-High | Medium-High | Medium | Low-Medium |

### Notes section (below table)

For each jurisdiction where the rule requires context to interpret correctly, add a note:

Example: "**UAE**: FDL 33/2021 represented a significant shift — pre-reform, courts rarely enforced non-competes; post-reform, the law provides a codified framework but requires compensation payment during the restricted period, which many employers overlook."

### Conclusion

End with a 3–5 sentence conclusion addressing:
1. Which jurisdiction is most favorable for the user's position, and why
2. Which jurisdiction presents the highest risk, and what the specific trap is
3. Any practical recommendation (e.g., "If the parties have freedom to choose governing law, DIFC or English law offers the most predictable non-compete enforcement framework for an employer; UAE onshore is increasingly enforceable but the compensation payment requirement is a trap")

## MENA-specific comparison notes

### Civil law vs common law split in MENA
- **Civil law** (LB, KSA, UAE onshore, EG, FR): gaps in contracts filled by statutory default rules; courts may not enforce clauses that violate mandatory law even if freely agreed.
- **Common law** (DIFC, ADGM, UK, US-DE): party autonomy is paramount; courts give effect to freely negotiated terms; implied terms are narrower.

### The DIFC/ADGM advantage for international transactions
DIFC and ADGM are common-law free zones within UAE. International parties often prefer them because:
- English is the language of proceedings
- Common law precedent (including English High Court decisions) is persuasive
- Judgments and arbitration awards are straightforwardly enforceable cross-border via the New York Convention

### UAE onshore: mandatory rules limit choice of law
UAE Federal Decree-Law No. 33 of 2021 on labor law is a mandatory statute — its protections cannot be contracted out of even if the employment contract specifies a foreign governing law, provided the employee works in UAE. This applies to: notice periods, EOSB (end-of-service gratuity), non-compete compensation, and anti-discrimination provisions.

### KSA: Sharia overlay and Saudization
Saudi law is Sharia-based and may strike down clauses that violate Islamic principles (e.g., interest-bearing provisions must be restructured as murabaha or other Sharia-compliant instruments). Additionally, Saudization (Nitaqat) requirements impose workforce nationalization quotas that affect employment contracts regardless of chosen governing law.

### Lebanon: functional legal system caveats
Lebanon has a sophisticated civil-law system on paper, but enforcement has been severely compromised by the economic and political crisis since 2019. Courts are backlogged; the banking system is dysfunctional; obtaining execution of a judgment is extremely difficult. Flag this in any comparison where Lebanon is a candidate forum.

## Per-cell source requirements

Each cell must cite one of:
- A named statute with its article number (where known and verified)
- A named regulation or decree with its number
- A named case (only if verified to exist — no fabricated citations)
- "Standard market practice confirmed by [regulator/bar]"
- "Not verified — confirm with local counsel"

Never leave a cell empty and never fabricate a source. If a cell cannot be populated with a verified source, mark it explicitly and note the gap.

## Related skills

- [[research-statute-lookup]]
- [[research-case-law-search]]
- [[research-deep-research-orchestrator]]
- [[review-governing-law-conflict]]
- [[review-dispute-resolution-mechanism-fit]]
- [[research-recent-amendments-tracker]]
