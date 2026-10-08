---
name: research-statute-of-limitations-lookup-sboghossian
title: Statute of Limitations Lookup
description: 'Use when a lawyer or claimant needs to know the limitation period for a specific claim type in a specific jurisdiction — including the start-date rules (accrual, discovery), tolling and suspension events, and whether limitation is procedural (raised by defendant) or substantive (raised by court ex officio). Covers KSA, UAE, Lebanon, Egypt, France, England, and the US. Critical practice-area flag: limitation is one of the most common reasons claims fail; always check before advising on whether to file.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-statute-of-limitations-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Statute of Limitations Lookup

Determine the applicable limitation period for a specific claim in a specific jurisdiction, including the start-date rule, tolling and suspension mechanisms, and the critical procedural-vs-substantive distinction. A missed limitation period is one of the most common and least-excusable failures in legal practice; this skill exists to prevent it.

## When to use this

- Before advising a client whether to file a claim
- When assessing whether a potential defendant can raise a time-bar defense
- In due diligence: checking whether target-company liabilities are time-barred
- When drafting contractual limitation clauses (checking against statutory floors and ceilings)
- When evaluating whether a limitation period has been extended by negotiation, part-payment, or acknowledgment of liability

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Jurisdiction | Limitation periods vary enormously by jurisdiction | Required |
| Claim type | Different periods apply to contract, tort, employment, commercial, property, debt recovery, etc. | Required |
| Accrual date | The date the cause of action arose (when the right to sue first arose) | Provide if known |
| Knowledge date | For discovery-rule jurisdictions: when the claimant knew or should have known of the claim | Provide if different from accrual date |
| Any partial payment or acknowledgment? | These events typically restart or toll the limitation clock | Flag if known |
| Contractual limitation clause? | Parties may have agreed to a shorter or longer period (where permitted) | Flag if present |

## Limitation periods by jurisdiction

### KSA (Saudi Arabia)

KSA limitation law is influenced by Sharia principles and is not comprehensively codified in a single statute. Key periods under the Commercial Court practice and implementing regulations:

| Claim type | Period | Start date |
|---|---|---|
| Commercial claims (general) | 10 years | Date of claim accrual |
| Negotiable instruments (cheques, promissory notes) | 5 years | Date of maturity / presentment |
| Insurance claims | 3 years | Date of loss event |
| Labor claims | 12 months | Date of termination of employment |
| Statutory right to overdue salary | 12 months | Date salary was due |
| Tax / ZATCA assessments | 5 years | End of fiscal year |

**Sharia note**: For certain Hudud criminal offenses, the concept of a fixed statute of limitations does not apply under classical Sharia jurisprudence. In practice, the Saudi commercial courts apply the periods above for commercial matters.

**Practical caveat**: KSA courts have discretion in some areas due to the ijtihad-based system; precise periods may vary by court division. Verify with KSA-qualified counsel for high-stakes matters.

### UAE Federal

UAE limitation law is set primarily in the UAE Civil Transactions Law (Federal Law No. 5 of 1985, as amended):

| Claim type | Period | Statutory basis | Start date |
|---|---|---|---|
| Commercial claims (general) | 10 years | Civil Transactions Law | Date of accrual |
| Employment claims | 1 year | Federal Decree-Law No. 33 of 2021 | Date of termination |
| Civil tort (general) | 3 years | Civil Transactions Law | Date claimant knew of injury AND identity of tortfeasor |
| Civil tort (absolute bar) | 15 years | Civil Transactions Law | Date of harmful act (regardless of knowledge) |
| Insurance | 3 years | Insurance Law | Date of event giving rise to claim |
| Negotiable instruments | 3 years (drawer v holder) | Commercial Transactions Law | Date of maturity |
| Real estate actions | 15 years | Civil Transactions Law | Accrual |

**Note**: Employment limitation of 1 year under FDL 33/2021 is a significant trap — in practice many employees wait more than 12 months before asserting claims, discovering the bar too late.

### Lebanon

Lebanese limitation law is governed primarily by the Code of Obligations and Contracts and the Labor Law:

| Claim type | Period | Source |
|---|---|---|
| Commercial claims (general) | 10 years | Code of Commerce |
| Employment claims | 5 years | Lebanese Labor Law |
| Civil personal claims (general) | 30 years (ordinaire) | Code of Obligations and Contracts |
| Contractual claims (standard) | 10 years | Code des Obligations et des Contrats |
| Tort (extra-contractual) | 3 years from knowledge; 10-year absolute bar | Code des Obligations et des Contrats |
| Insurance | 3 years | Insurance Law |

**Lebanon note**: The 30-year general civil period is unusually long by international standards. In practice, evidentiary difficulties and the economic crisis make litigation on ancient claims rare, but the legal period remains.

### Egypt

| Claim type | Period | Source |
|---|---|---|
| Civil claims (general) | 15 years | Egyptian Civil Code |
| Commercial claims (general) | 10 years | Egyptian Commercial Code |
| Labor claims | 1 year | Egyptian Labor Law |
| Tort | 3 years from knowledge; 15-year absolute bar | Egyptian Civil Code |

### France

France uses the concept of "prescription extinctive" (extinctive prescription). The 2008 reform rationalized French limitation periods:

| Claim type | Period | Source |
|---|---|---|
| Civil / commercial (general) | 5 years | Article 2224 Civil Code |
| Consumer claims | 2 years | Consumer Code |
| Personal injury (tort) | 10 years | Article 2226 Civil Code |
| Real property actions | 30 years | Article 2227 Civil Code |
| Salary claims | 3 years | Labor Code |

**Start date rule (France)**: the period runs from the day the holder "knew or should have known of the facts allowing the action to be brought" — a discovery-type rule codified since 2008.

### England and Wales

| Claim type | Period | Statute |
|---|---|---|
| Contract (simple) | 6 years | Limitation Act 1980, s.5 |
| Contract (under seal / deed) | 12 years | Limitation Act 1980, s.8 |
| Tort (general) | 6 years | Limitation Act 1980, s.2 |
| Personal injury | 3 years from knowledge (s.14) | Limitation Act 1980, s.11 |
| Negligence — latent damage | 3 years from knowledge; 15-year long-stop | Limitation Act 1980, ss.14A–14B |
| Recovery of land | 12 years | Limitation Act 1980, s.15 |

### US (general — state-by-state)

The US has no uniform federal limitation period for most civil claims; periods are set by each state:

| Claim type | Typical range | Notes |
|---|---|---|
| Contract | 3–6 years | Delaware: 3 years; New York: 6 years; California: 4 years |
| Tort | 2–3 years | Varies significantly by state |
| Fraud | 2–6 years (often from discovery) | Delaware: 3 years from accrual or discovery |
| Debt collection | 3–6 years | State-specific |

**Delaware note**: Delaware is the relevant jurisdiction for most US corporate matters. Delaware's general statute of limitations is 3 years (10 Del. C. § 8106 for most claims).

## Start-date rules: accrual vs discovery

The start date for a limitation period is often the most litigated aspect:

| Rule | Jurisdictions using it | Meaning |
|------|------------------------|---------|
| **Accrual rule** | UAE (civil), KSA (commercial) | Clock starts when the right to sue arose, regardless of whether the claimant knew |
| **Discovery rule** | England, France, Lebanon (tort), US (fraud/latent damage) | Clock starts when the claimant knew or should have known of the harm and its cause |
| **Combination** | Most jurisdictions: discovery-based primary period + absolute backstop long-stop | E.g., England: 3 years from knowledge but 15-year long-stop for latent damage |

## Tolling and suspension events

The limitation clock may be paused (tolled) or restarted by:

| Event | Effect | Jurisdictions |
|-------|--------|--------------|
| **Acknowledgment of debt / liability** | Restarts the clock | England, UAE, Lebanon, France |
| **Part payment** | Restarts the clock | England, UAE, Lebanon |
| **Filed proceedings** | Suspends or stops the clock | All jurisdictions (filing a claim stops the period) |
| **Mediation / arbitration initiated** | Suspends in some jurisdictions | Check jurisdiction-specific rules |
| **Minority or legal incapacity** | Suspends | All jurisdictions (clock pauses while claimant lacks legal capacity) |
| **Fraudulent concealment** | Restarts or defers start date | England (s.32 Limitation Act), France |
| **Force majeure / impossibility** | Suspends in some jurisdictions | Lebanon, France |
| **Contractual agreement to extend** | Extends the period | Permitted in most jurisdictions; not permitted below statutory minimum |

## Procedural vs substantive — critical distinction

| Type | Meaning | Jurisdictions | Practical consequence |
|------|---------|---------------|-----------------------|
| **Procedural** | The court does not raise limitation on its own; the defendant must plead it or it is waived | England, US | A defendant who fails to plead limitation in the defence loses the right to rely on it |
| **Substantive** | The right itself is extinguished by the passage of time; the court can raise it ex officio | France, Lebanon, UAE, KSA | Even if neither party raises it, the judge may dismiss a time-barred claim |

**Flag this distinction in every limitation output** — it determines whether a party who receives a time-barred claim must actively plead the defense or whether the court will reject the claim automatically.

## Output structure

```
## Limitation Period — [Claim type] in [Jurisdiction]

**Claim type**: [as specified]
**Jurisdiction**: [as specified]
**Applicable statute**: [name and article number]

**Limitation period**: [N years / months]
**Start date rule**: [accrual / discovery / combination]
**Accrual date (based on inputs)**: [date or "not specified"]
**Expiry date (calculated)**: [date or "cannot calculate without more information"]

**Tolling events applicable**: [list]
**Procedural vs substantive**: [procedural — must be pleaded / substantive — raised ex officio]

**Warnings**:
- [Any jurisdiction-specific trap or recent change]

**Confidence**: [high / medium — confirm with local counsel for high-stakes matters]
```

## Related skills

- [[research-statute-lookup]]
- [[research-court-procedure-lookup]]
- [[research-case-law-search]]
- [[research-recent-amendments-tracker]]
