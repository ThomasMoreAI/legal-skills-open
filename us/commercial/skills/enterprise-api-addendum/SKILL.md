---
name: enterprise-api-addendum
title: Enterprise API Addendum Negotiation
description: Negotiates bespoke enterprise API addenda that override standard click-wrap terms for high-value partners. Covers document precedence, indemnification and liability caps, SLA/service-credit design, exclusivity, API versioning governance, data rights, and internal alignment. Triggers when user mentions enterprise API addendum, click-wrap override, API SLA negotiation, API indemnity, service credits, breaking-change governance, MFN clauses, or enterprise partner terms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/enterprise-api-addendum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
tags: [agreement, drafting, transactional]
---

# Enterprise API Addendum Negotiation

Produces negotiation tables, clause language, decision trees, and internal readiness checklists for enterprise API addenda that layer over click-wrap terms. The addendum creates a document hierarchy (addendum → order form → DPA → SLA schedule → click-wrap) where precedence errors can elevate or gut standard terms, and misaligned indemnity or SLA clauses can create uncapped exposure.

## Pre-Draft Intake (Mandatory)

Ask every time unless user says "use defaults" or "just draft":

1. **Click-wrap API ToS** in production
2. **Governing contracts** — order form/SOW, existing MSA
3. **API spec** — endpoints, rate limits, versioning policy, criticality
4. **Data classification** — personal data, PCI/PHI, export-controlled, SSO, telemetry
5. **Commercial parameters** — fees, term, liability posture, exclusivity, MFN
6. **Partner requirements** — SLA targets, indemnity expectations, audit rights, insurance

**Defaults** (apply and label if user doesn't respond):

| Parameter | Default |
|---|---|
| Governing law / venue | Delaware / Delaware courts |
| Data sensitivity | No PCI/PHI; limited personal data |
| SLA | 99.9% monthly uptime; 24×5 support; scheduled maintenance excluded |
| Liability cap | 12 months' fees; exclude indirect; super-cap 2× for confidentiality/privacy |
| Exclusivity | None; "preferred partner" marketing only |
| Breaking changes | 90 days' notice; security patches exempt |

## Step 1: Deal Architecture and Delta Analysis

Map gaps between click-wrap and enterprise requirements:

| Clause | Click-Wrap Default | Enterprise Ask | Strategy |
|---|---|---|---|
| SLA / Uptime | "As-Is" | 99.9–99.99% with credits | Credits; exclude beta + scheduled maintenance |
| Indemnity | None or limited | Broad IP + data breach | Cap at ACV multiple; standard exclusions; control of defense |
| Liability Cap | $100 or 1 month's fees | 12–24 months'; super-caps | Tiered: general cap + super-cap for data/IP |
| Breaking Changes | At will | 90–180 days' notice; sunset | Define narrowly; exempt security patches |
| Data Rights | Broad aggregate license | Service-delivery only; strict anonymization | Precise "Anonymized" definition |
| Termination | At will | For-cause only; wind-down | Cure period; transition assistance |
| Audit Rights | None | Annual security/compliance | Once/year at Customer's expense; more if breach |

### Architecture Checklist

- [ ] Click-wrap incorporated by reference or restated?
- [ ] Addendum covers entity only or also affiliates?
- [ ] Production only or also sandbox/beta?
- [ ] Multiple docs (Order Form, DPA, Security Exhibit, SLA Schedule)?
- [ ] MFN precedence clause accidentally elevates click-wrap?
- [ ] Amendment-by-posting locked for this partner?

### Precedence Matrix

| Document | Rank | Conflict Rule |
|---|---|---|
| Enterprise API Addendum | 1 (highest) | Controls over click-wrap |
| Order Form / SOW | 2 | Controls for commercial items |
| DPA | 2–3 | Higher for privacy conflicts |
| SLA Schedule | 3 | Controls for SLA topics |
| Security Exhibit | 3–4 | Must align with SLA and incident clause |
| Click-wrap API Terms | Lowest | Incorporated subject to addendum |

**Incorporation + Lock-In Clause:**

> "The Online API Terms are incorporated by reference solely as modified by this Addendum. In the event of conflict, this Addendum controls. For the Partner only, the Online API Terms will not be amended in a manner that materially diminishes Partner's rights or increases Partner's obligations without Partner's written consent."

## Step 2: Indemnification and Liability

| Topic | Customer Ask | Vendor Default | Fallback |
|---|---|---|---|
| IP indemnity | Broad | Unmodified API, U.S. IP only | Exclude foreign patents; cap to fees; modify/replace/refund |
| Data breach | All losses/fines | Vendor's failure per Security Exhibit | Super-cap 2× fees; direct damages only |
| Customer misuse | Silent | Customer indemnifies for unlawful use | Narrow to third-party claims from Customer's apps |
| Cap amount | 2–5× or uncapped | 12 months' fees paid/payable | 24 months'; fixed dollar amount |
| Indemnity vs. cap | Outside cap | Inside cap (IP possibly outside) | IP outside general cap with separate cap |
| Excluded damages | Some consequential | Exclude all indirect/consequential/punitive | Direct only; limited confidentiality carve-out |
| Confidentiality carve-out | Uncapped | Super-cap 2× | Separate fixed cap or insurance limits |

### Key Clauses

**IP Indemnity (balanced vendor form):**

> "Provider will defend Partner against any third-party claim alleging that the unmodified API, when used in accordance with this Agreement and Documentation, infringes such third party's U.S. copyright, U.S. trade secret, or U.S. patent, and will pay damages finally awarded or agreed in settlement, provided Partner (a) promptly notifies Provider, (b) allows Provider sole control of defense and settlement, and (c) reasonably cooperates."

**IP Exclusions:**

> "Provider has no obligation to the extent a claim arises from: (i) Partner Data or Partner Applications; (ii) modifications not made by Provider; (iii) combination with items not provided by Provider; (iv) use outside scope or contrary to Documentation; (v) failure to use updates made available to avoid infringement."

**Limitation of Liability:**

> "Except for Excluded Claims, each party's aggregate liability will not exceed the fees paid or payable under the applicable Order Form in the 12 months preceding the event giving rise to the claim ('General Cap'). In no event will either party be liable for indirect, incidental, special, consequential, exemplary, or punitive damages."

**Excluded Claims / Super-Cap:**

> "'Excluded Claims' means: (a) Customer's payment obligations; (b) Customer's indemnification obligations; (c) either party's breach of confidentiality (capped at 2× General Cap); (d) Provider's IP indemnification (capped at 2× General Cap); (e) gross negligence or willful misconduct."

## Step 3: SLA, Support, and Credits

### SLA Schedule

| Metric | Value |
|---|---|
| Monthly Uptime % | 99.9% |
| Downtime definition | API not responding HTTP 2xx for ≥5 consecutive minutes |
| Measurement | Provider monitoring + logs |

**Exclusions:** Scheduled maintenance (72h notice), emergency maintenance, force majeure, Partner's systems/network, rate-limit throttling, beta features.

### Service Credits (sole and exclusive remedy)

| Monthly Uptime % | Credit (% of Monthly Fees) |
|---|---|
| < 99.9% and ≥ 99.5% | 5% |
| < 99.5% and ≥ 99.0% | 10% |
| < 99.0% | 20% |

Request within 30 days. Max aggregate: 20% monthly fees. Apply to future invoices (cash refund if no future invoices).

### Support

| Item | Default | Premium |
|---|---|---|
| Hours | 24×5 | 24×7 (additional cost) |
| P1 response | 1 hour | 30 minutes |
| P2 response | 4 hours | Negotiable |
| Dedicated TAM | Not included | Top-tier deals |

**Critical:** Distinguish response from resolution times. Resolution = "commercially reasonable efforts" only — never attach SLA credits to resolution.

**Chronic Failure:** Termination right only if uptime < 99.0% for 2 consecutive months after documented cure plan.

## Step 4: Exclusivity and Competitive Restrictions

### Decision Checklist

- [ ] What consideration supports exclusivity? (minimum spend, volume, co-development)
- [ ] Scope: which endpoints, use cases, verticals, territories?
- [ ] Term: short duration, renewable on milestones?
- [ ] Exceptions: existing customers, strategic accounts, affiliates, acquisitions?
- [ ] Remedy for breach: termination of exclusivity only (not broad damages)?
- [ ] Antitrust review needed? (especially EU/UK)

### Graduated Options

| Option | Risk | Use When |
|---|---|---|
| No exclusivity (default) | None | Standard deals |
| Preferred partner marketing | Low | Recognition without restriction |
| Limited vertical exclusivity | High | Significant committed spend + milestones |
| MFN | Medium-High | Sparingly; pricing only, similarly situated, with sunset |

**MFN Guardrails:** Similarly situated customers + pricing only. Exclude promotional/pilot/strategic deals. Prospective credit only (not retroactive). Sunset after 12 months.

## Step 5: Technical Governance and Data Rights

**Breaking Change Definition:**

> "'Breaking Change' means any modification to the API that requires Partner to modify its code to maintain existing functionality, including removal of endpoints, changes to request/response schemas, or modification of authentication methods."

**Notice & Sunset:**

> "Provider will give Partner at least [90] days' prior written notice before implementing a Breaking Change. Provider will maintain the prior version for at least [180] days following notice. This Section does not apply to changes required to address security vulnerabilities, comply with law, or prevent imminent harm."

**Audit Rights:** Once/year at Partner's expense, 30 days' notice, scope limited to security + DPA compliance. Additional audits if breach. May satisfy via SOC 2 Type II or ISO 27001.

**Data Rights:**
- Partner retains all rights in Partner Data; Provider retains all rights in API and derivatives
- Provider uses Partner Data solely to provide API Services
- Aggregate/anonymized use requires precise "Anonymized Data" definition (irreversibly de-identified; cannot be re-identified)
- If personal data in scope, incorporate DPA

## Step 6: Consolidation and Internal Alignment

### Term Sheet

| Category | Agreed/Proposed | Fallback | Owner |
|---|---|---|---|
| API scope + endpoints | | | Product |
| Fees / usage limits | | | Sales / Finance |
| SLA / support / credits | | | SRE / Support |
| Indemnity (IP) | | | Legal |
| Indemnity (data breach) | | | Legal / Security |
| Liability cap & carve-outs | | | Legal / Finance |
| Exclusivity / MFN | | | BizDev |
| Breaking changes / versioning | | | Product / Engineering |
| Term / termination | | | Legal / Sales |

### Internal Readiness

- [ ] SRE: monitoring supports SLA measurement; maintenance windows defined
- [ ] Support: hours, P1 definitions, escalation path, staffing achievable
- [ ] Security: controls and incident response match Security Exhibit
- [ ] Privacy: DPA necessity and cross-border transfer mechanism confirmed
- [ ] Finance: credit mechanism, revenue recognition, insurance adequacy confirmed
- [ ] Product/Engineering: breaking-changes notice period feasible
- [ ] Legal: precedence clause prevents unilateral click-wrap changes
- [ ] Compliance: exclusivity reviewed for antitrust implications

## Post-Draft Alignment (Mandatory)

After delivering the initial package, ask:

1. Does the delta analysis correctly capture click-wrap vs. partner gaps?
2. Are indemnity and liability positions within approved risk tolerance?
3. Has SRE confirmed SLA metrics and credits are operationally achievable?
4. Should I produce specific clause language for any section?

## Quality Checks

- Delta analysis covers all material clause categories
- Precedence matrix prevents accidental click-wrap elevation
- Indemnity includes caps, exclusions, and super-cap structure
- SLA metrics, exclusions, and credit table are complete
- Service credits specified as sole and exclusive remedy
- Breaking Change excludes bug fixes and security patches
- Exclusivity (if any) has consideration, scope, term, exceptions, remedy
- "Fees paid" vs. "fees payable" clarified in liability cap
- MFN limited to pricing only (no legal terms)
- Amendment-by-posting locked for this partner
- All clause language marked as negotiation starting points

## Red Flags — Reject or Escalate

1. Uncapped liability for confidentiality or privacy breaches
2. IP indemnity covering Partner's own applications or data
3. SLA termination right for any single-month miss
4. MFN covering legal terms (not just pricing)
5. Unilateral click-wrap amendment overrides negotiated terms
6. Resolution-time SLA commitments with credits attached
7. Uncapped service credits (no aggregate monthly max)
8. Broad exclusivity without consideration or milestones
9. Audit rights with no frequency limit or scope boundary
10. "Breaking Change" so broad it covers bug fixes and security patches

## Guidelines

- Clarify "fees paid" vs. "fees payable" in every liability cap
- Always exempt security patches and legal compliance from breaking-change notice
- Service credits must be sole and exclusive remedy for SLA breach
- Regulatory fines as indemnifiable damages: enforceability varies — flag for local counsel
- Cross-reference DPA when personal data is in scope
- Verify entity names, signature authority, and affiliate definitions before execution
- Mark uncertain enforceability positions with [VERIFY]

**Required disclaimer on every output:**

> THIS NEGOTIATION GUIDANCE IS A DRAFTING AID AND REQUIRES REVIEW BY QUALIFIED LEGAL COUNSEL. IT DOES NOT CONSTITUTE LEGAL ADVICE.
