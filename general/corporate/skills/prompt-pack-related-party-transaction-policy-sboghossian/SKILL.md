---
name: prompt-pack-related-party-transaction-policy-sboghossian
title: Related Party Transaction Policy
description: Use when a company needs to draft a Related Party Transactions (RPT) policy covering identification of related parties, disclosure requirements, approval thresholds, board and audit committee review processes, arm's length standards, and regulatory compliance. Essential for MENA companies navigating UAE Commercial Companies Law, DIFC and ADGM company regulations, Saudi CG Code, and any entity preparing for listing or institutional investor scrutiny.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-related-party-transaction-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Related Party Transaction Policy

## When to use this

Use this skill when:
- A company is establishing or updating its corporate governance framework and needs a formal RPT policy.
- A listed or pre-IPO company requires an RPT policy that satisfies stock exchange listing rules (DFM, ADX, Tadawul, EGX).
- An institutional investor (PE fund, sovereign wealth fund, DFI) requires the portfolio company to adopt an RPT policy as a condition of investment.
- A board audit committee needs a policy to guide its review of management's related-party transaction disclosures.
- A company's auditors have flagged related-party transactions without adequate policy coverage.
- A company is undergoing M&A due diligence and needs to demonstrate governance controls.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Company name and entity type** | Policy must reference the specific company and its governing law | Ask before drafting |
| **Jurisdiction of incorporation** | Determines which legal definitions of "related party" apply and which mandatory disclosure rules govern | Ask; default to UAE onshore if unclear |
| **Ownership and group structure** | Determines who counts as a related party (shareholders above threshold, parent companies, sister entities) | Ask: "Who owns the company and is it part of a group?" |
| **Board and committee structure** | Determines which body approves which tier of transaction | Ask: does the company have an audit committee? |
| **Approval thresholds (if pre-determined)** | Allows customization; otherwise use market-standard thresholds | Default tiers: management approval below 1% of net assets; board approval 1–5%; shareholder approval above 5% |

## Optional inputs

- **Exchange listing rules applicable** — DFM, ADX, Tadawul, EGX each have specific RPT disclosure and approval obligations for listed companies.
- **Sector-specific rules** — banks (CBUAE requirements), insurance companies, investment funds each have sector-specific conflict-of-interest rules.
- **Existing conflict-of-interest policy** — the RPT policy may need to be consistent with or replace an existing CoI policy.

## Document structure

1. **Purpose and scope**
   - Why the policy exists: protecting minority shareholders, ensuring arm's length terms, meeting regulatory obligations.
   - Who it applies to: directors, senior management, controlling shareholders, and their affiliates.

2. **Definitions**
   - **Related party**: typically includes directors, key management personnel, controlling shareholders (usually defined as holding ≥10% or ≥20%), entities controlled by or controlling the above, immediate family members. The precise definition tracks the applicable accounting standard (IFRS IAS 24) and local company law.
   - **Related party transaction (RPT)**: transfer of resources, services, or obligations between the company and a related party, regardless of whether a price is charged.
   - **Material RPT**: any RPT above a defined threshold (see approval tiers below).

3. **Identification and disclosure of related parties**
   - Annual declaration process: all directors and senior management must submit an annual written declaration of their related-party interests.
   - Ongoing disclosure obligation: any new related-party relationship must be disclosed within [5/10/14] days of arising.
   - Register of related parties: maintained by company secretary; updated at each board meeting.

4. **Identification and disclosure of RPTs**
   - How to identify whether a proposed transaction involves a related party (screening against the register).
   - Advance disclosure to the board / audit committee before entering into any RPT.
   - Annual summary of RPTs to be included in the company's financial statements (IFRS IAS 24 requirement).

5. **Approval framework**

   | Transaction Value (as % of net assets) | Approval Required |
   |---|---|
   | Below 1% | CEO / Management approval; notification to board |
   | 1% – 5% | Audit Committee review and recommendation; Board approval |
   | Above 5% | Board approval; shareholder approval (ordinary or special resolution depending on jurisdiction) |
   | Any transaction where director has a direct financial interest | Board approval with interested director recusing; independent directors vote |

6. **Arm's length standard**
   - All RPTs must be concluded on terms no less favorable to the company than would be available in a transaction with an unrelated third party on equivalent terms.
   - For material RPTs, the board (or audit committee) should obtain an independent valuation or fairness opinion.
   - The basis for concluding the terms are arm's length must be documented.

7. **Interested party recusal**
   - Any director or senior manager who is a party to or has an interest in an RPT must:
     - Disclose the interest in full to the board before deliberation.
     - Recuse from voting on the transaction.
     - Leave the meeting during deliberation if requested.
   - Minutes must record the recusal and the basis for the board's determination that terms are arm's length.

8. **Prohibited transactions**
   - Loans to directors (prohibited or restricted under most MENA company laws).
   - Self-dealing contracts not approved under this policy.
   - Transactions designed to circumvent this policy by artificial structuring.

9. **Record-keeping and reporting**
   - All approved RPTs: documented in board minutes and company register.
   - Annual report / financial statements: summarize material RPTs per IFRS IAS 24.
   - Regulator reporting: as required by applicable exchange listing rules or sector regulator.

10. **Sanctions for non-compliance**
    - Failure to disclose a related-party interest is a breach of fiduciary duty.
    - Unapproved RPTs may be voidable at the company's election.
    - Directors in breach may be liable for damages and disqualification.

11. **Policy administration and review**
    - Owner: company secretary / general counsel.
    - Review frequency: annual, or whenever a material change in ownership or governance occurs.
    - Approval: board of directors.

## Jurisdictional notes

### UAE — onshore (Federal Decree-Law No. 32 of 2021 on Commercial Companies)
- Art. 166+ governs conflicts of interest for LLC managers; Art. 166 requires disclosure and prohibition on voting.
- PSC/PJSC (public companies): SCA Governance Code requires detailed RPT disclosures in annual reports and advance board approval.
- Listed companies: DFM/ADX listing rules require immediate disclosure to the exchange of material RPTs.

### DIFC
- DIFC Companies Law (DIFC Law No. 5 of 2018): Companies Act-style duty of directors to avoid conflicts; related-party transactions require board approval with interested director recusal.
- Investment business: DFSA Rules impose additional conflict management requirements on regulated firms.

### KSA (Saudi Corporate Governance Regulations, CMA)
- CMA Corporate Governance Regulations require listed companies to have an RPT policy, audit committee oversight, and semi-annual disclosure of all RPTs.
- Any RPT with a controlling shareholder (holding ≥5%) of a listed company requires shareholder approval at general assembly.

### Egypt (EGX Listed Companies)
- FRA Corporate Governance Code requires listed companies to disclose RPTs in annual reports.
- Companies Law No. 159 of 1981 requires shareholder approval for transactions between the company and its directors.

### Lebanon
- Lebanese Commercial Code requires disclosure of director interests; prohibits self-dealing contracts without general assembly approval.
- Banking sector: BDL Circular 44 imposes strict related-party lending limits.

## Drafting standards

- Define "related party" with reference to IAS 24 (internationally recognized) and supplement with the specific local-law definition where they differ.
- Use a clear tiered approval table — this is the core operative provision that practitioners will apply.
- Include a worked example in an annex (e.g., "A director owns 20% of a supplier company; the company proposes to award the supplier a USD 500,000 contract; which approval level applies?").
- Avoid vague language like "significant transaction" — tie all thresholds to measurable financial metrics.

## Common mistakes

- **Using IFRS IAS 24 definition alone without checking local law.** Local company laws (UAE, KSA) may define related party more broadly or differently; the policy should capture both.
- **No recusal procedure for the CEO/MD.** Policies often cover directors but forget that the CEO is also an officer subject to conflict rules.
- **Threshold set too high.** A 10% of net-assets threshold for shareholder approval may miss many material transactions in a large company; calibrate thresholds to the company's actual transaction profile.
- **No standalone prohibition on director loans.** Failing to include this creates ambiguity — most MENA company laws prohibit or restrict loans to directors; state it explicitly.

## Related skills

- [[prompt-pack-shareholders-agreement]]
- [[prompt-pack-shareholders-resolution]]
- [[prompt-pack-regulatory-filing-checklist]]
- [[prompt-pack-share-purchase-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
