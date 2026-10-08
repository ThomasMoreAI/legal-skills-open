---
name: review-unusual-terms-detector-sboghossian
title: Unusual / Atypical Terms Detector
description: Use when scanning a contract for clauses that deviate materially from market norms for that document type and jurisdiction. Identifies atypical provisions — including below-market liability caps, IP ownership reversals, disproportionate termination fees, retroactive most-favored-customer clauses, currency-risk shifts, and non-standard arbitration seat selection — and contrasts them with market-standard alternatives. Severity-rated output with a caution against treating atypical as automatically wrong.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-unusual-terms-detector
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Unusual / Atypical Terms Detector

## When to use this

Use this skill when:
- A contract has been submitted by a counterparty and you want to identify provisions that are out of the ordinary before investing time in a full review
- A client asks "is there anything weird in this contract?"
- You are reviewing against a market standard for a specific contract type and jurisdiction
- Prior to price negotiation — to understand which unusual terms are commercially motivated and which may be errors or overreach

This skill identifies deviations from market norms; it does not assess whether those deviations are legally problematic (for that, use [[review-risk-flagging]]). An unusual term may have a legitimate commercial explanation — always investigate before redlining.

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Contract text | The full document | Required |
| Document type | Calibrates the market norm baseline | Infer from contract; ask if unclear |
| Jurisdiction | Geographic and legal-system market norms differ | From governing-law clause |
| Deal type and value | Size matters — what is unusual for a USD 100K contract may be standard for a USD 10M deal | Infer; ask if unclear |

## Patterns to Surface

### 1. Liability Caps Materially Below Market

**Market reference**:
- Commercial services / SaaS: 12-month fees is standard Provider position; 24-month or 2× annual fees is a common negotiated outcome
- Construction: linked to contract price
- M&A representations: 20–30% of transaction value for general reps

**Flag as atypical**:
- Cap less than 6-month fees for a meaningful-value services contract
- Cap expressed as a fixed amount (e.g., USD 10,000) on a USD 500,000 annual contract
- Cap applies to all categories of damages including IP infringement and data breach with no carve-outs
- No cap at all for the Client (asymmetric — Client has unlimited liability; Provider capped)

### 2. IP Ownership Terms Reversed from Norm

**Market norm for services for hire (custom development)**:
- Client pays → Client owns the deliverables
- Provider retains its background IP; grants license back
- Foreground IP is assigned to Client on creation

**Atypical**:
- Provider retains ownership of all deliverables including custom code written for Client's specifications — "Client receives a license only" when the contract is a pure bespoke-for-hire engagement
- Client assigned background IP (pre-existing tools, libraries, frameworks) that the Provider has been using for years
- No license-back at all — Client cannot use the deliverables outside the scope of the agreement

**Commercial reason investigation**: sometimes a vendor retains IP ownership as a deliberate business decision (e.g., the deliverable becomes a standard product feature). Ask before redlining.

### 3. Term Lengths Far Outside the Market Band

**What is typical**:
- SaaS subscriptions: 1–3 years initial term
- Commercial leases: 3–10 years for commercial; up to 99 years for some ground leases
- NDA confidentiality term: 2–5 years
- Employment non-compete: 12–24 months post-termination

**Atypical**:
- SaaS contract: 10-year initial term with auto-renewal and no T4C (locks client in for a decade)
- NDA: perpetual obligations for all categories of information (not just trade secrets)
- Post-employment non-compete: 5 years (likely void in most jurisdictions)
- Lease: 1-year term with monthly break rights — very short for a commercial tenant who has invested in fit-out

### 4. Non-Compete Beyond Market Band

| Context | Market range | Atypical threshold |
|---|---|---|
| Senior executive (employer-side) | 12–24 months | >3 years |
| Mid-level employee | 6–12 months | >18 months |
| M&A (seller non-compete) | 3–5 years | >5 years |
| VC / investor (founder non-compete) | 12–24 months | >3 years |
| Commercial agency / distribution | 1–3 years | >5 years |

Geographic and functional scope must also be proportionate. A global non-compete for a regional business is atypical. A non-compete covering "any business" is overbroad for most employment contexts.

**MENA note**: UAE Labour Law limits post-employment non-competes to 2 years maximum; anything longer is void. KSA courts apply proportionality but have upheld 3-year commercial non-competes in appropriate circumstances. DIFC/ADGM: English-law restraint of trade test — must be reasonable in scope, geography, and duration.

### 5. Termination Fees Disproportionate to Value

**Market norm**:
- Early termination fee: typically a portion of fees that would have been earned over the remaining term; rarely more than 6–12 months of remaining fees
- Liquidated damages clauses in commercial services: must represent a genuine pre-estimate of loss

**Atypical**:
- Termination fee equals 100% of the full remaining contract value (e.g., USD 5M payable on termination of a USD 5M contract in Year 1 of a 5-year term)
- Termination fee applies even if termination is for the Provider's material breach
- No termination fee at all for a long-term exclusive arrangement — creates no incentive for Provider to maintain service quality

**Jurisdictional enforceability**:
- UAE (onshore): courts will reduce a penalty clause to reflect actual loss regardless of the agreed amount (Civil Code adjustability)
- KSA: similar — Shariah courts apply proportionality
- DIFC/ADGM/UK: liquidated damages must be a genuine pre-estimate of loss; penalty clauses are void as penalties

### 6. Most-Favored-Customer Clauses Applied Retroactively

**Market norm**: MFC is prospective — if Provider gives a better price to any future customer (or current similarly-situated customers), Provider must give Client the same deal going forward.

**Atypical (flag)**:
- Retroactive MFC: if Provider has ever given a better price to anyone, Client gets a retroactive refund of the difference. This creates open-ended historical liability and is practically unworkable for any Provider with multiple pricing arrangements.
- MFC applied to all terms (not just pricing): "Client shall have terms no less favorable than any other customer" — extremely burdensome.
- MFC benchmarked against all customers regardless of size, volume, or negotiated terms — a 1-unit customer claims parity with a 10,000-unit customer.

### 7. Currency Clauses That Shift Exchange-Rate Risk Asymmetrically

**Typical**: contract denominated in a single currency; both parties bear the natural exchange-rate risk of their own businesses.

**Atypical**:
- Contract requires payment in USD but Client is a local entity earning in local currency without any USD revenue — forces Client to bear full FX risk on market movements
- Escalation clause tied to USD exchange rate applied retroactively
- "Payment in USD or USD equivalent at the rate on the day of payment" — creates uncertainty about actual obligation size

**Lebanon note**: given chronic LBP/USD exchange instability, any USD-denominated contract with a Lebanese entity requires explicit acknowledgment of the Banque du Liban regulatory environment, the applicable exchange rate mechanism, and whether Lollars (Lebanese bank-held USD) are acceptable or only "fresh" USD.

### 8. Arbitration in Non-Standard Seats

**Standard seats** for MENA commercial contracts:
- UAE/GCC: DIAC (Dubai International Arbitration Centre), DIFC-LCIA, ICC (Paris or Singapore), ADGM Arbitration Centre
- Saudi Arabia: SCCA (Saudi Center for Commercial Arbitration)
- Lebanon: BAC (Beirut Arbitration Center) or ICC
- Egypt: Cairo Regional Centre for International Commercial Arbitration (CRCICA)

**Flag as unusual**:
- Cayman Islands seat for a UAE-UAE commercial contract — ask why; may indicate sophisticated offshore structuring or may be an error
- Switzerland seat for a GCC-GCC contract without a specific Swiss nexus
- Ad hoc arbitration (no institutional rules) — increases enforceability risk and eliminates administrative support; acceptable in sophisticated M&A contexts but unusual in commercial services
- Arbitration in a country that has not acceded to the New York Convention — limits enforcement internationally
- Home-court arbitration: arbitration seat in the home city of the stronger party — equivalent of choosing the other party's preferred forum; ask for a neutral seat

**Investigations approach**: before flagging as a problem, ask whether there is a commercial or structural reason (e.g., the contract is governed by Swiss law and the Swiss nexus explains the seat choice).

### 9. Other Patterns Worth Surfacing

| Pattern | Description | Typical standard |
|---|---|---|
| Unilateral amendment right | Provider can amend contract terms on 30 days' notice | Mutual amendment by written agreement |
| Exclusive territory without minimum purchase | Distributor has exclusive territory but no obligation to sell | Minimum purchase commitment required |
| Assignment to affiliates unrestricted | Any affiliate of either party can step in without notice | Assignment to affiliates with notice; change of control requires consent |
| Audit rights unlimited in frequency and scope | Counterparty can audit at any time without restriction | Once per year with 30 days' notice; reasonable scope |
| Auto-renewal notice window > 90 days | 90+ day notice required to prevent auto-renewal | 30–60 days is standard |
| Price adjustment on cost-plus without ceiling | Provider can pass through unlimited cost increases | Cost-plus with cap or budget approval required |

## Output Format

For each atypical provision identified:

```
## Atypical: <short title>

**Clause**: <section reference>
**What it says**: <brief description of the clause>
**Market standard**: <what would typically appear in this type of contract for this jurisdiction>
**Severity**: 🔴 Critical / 🟡 Medium / 🟢 Low
**Commercial reason inquiry**: <question to ask before redlining — "Does this reflect a deliberate commercial decision?">
**Suggested alternative**: <market-standard language or approach>
```

## Important Caution

**Atypical ≠ wrong.** A deviation from market standard may reflect:
- A deliberate commercial negotiation (Client paid less in exchange for giving up IP ownership)
- Specific regulatory requirements (a regulated industry may impose unusual data-handling terms)
- Bespoke deal structure (M&A, outsourcing, or partnership contexts have non-standard norms)

Always verify the commercial context before treating an unusual term as a problem. The skill flags deviations; counsel decides whether they are appropriate.

## Related Skills

- [[review-risk-flagging]]
- [[review-msa-deep-review]]
- [[review-liability-cap-reasonableness]]
- [[review-ip-ownership-clarity]]
- [[review-nda-quick-check]]
- [[review-missing-clauses]]
