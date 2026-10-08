---
name: review-missing-clauses-sboghossian
title: Missing-Clauses Detector
description: Use when a contract needs a completeness check against the standard skeleton for its document type. Identifies absent mandatory, strongly recommended, and optional clauses across NDAs, MSAs, leases, employment agreements, and other common commercial instruments. Flags jurisdiction-specific mandatory provisions and links to drafting skills for remediation. Suitable as a first-pass quality gate before any detailed clause-by-clause review.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-missing-clauses
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Missing-Clauses Detector

## When to use this

Use this skill as a first-pass quality gate on any contract:
- After receiving a first draft from a counterparty — to check what they have omitted
- Before signing — to confirm the agreement is complete
- When assessing a historic agreement — to understand its gaps
- After generating a first draft via a drafting skill — to confirm completeness before sending

This skill identifies structural gaps. It is a completeness check, not a risk-in-existing-clauses review — run [[review-risk-flagging]] alongside it for the full picture.

## Process

1. **Identify document type** from the subject line, title, recitals, or the user's description (NDA, MSA, lease, employment agreement, SHA, services agreement, etc.)
2. **Load the standard skeleton** for that document type — each document type has a minimum viable clause list (see below)
3. **Compare clause by clause**: scan for each expected provision; note if absent, partially present, or fully present
4. **Categorize each gap**:
   - **Mandatory**: absence may make the contract invalid, unenforceable, or expose to regulatory penalty
   - **Strongly recommended**: absence creates material legal risk or ambiguity
   - **Optional**: standard market practice but not legally required; include if in scope for this deal type

## Standard Clause Skeletons by Document Type

### NDA (Non-Disclosure Agreement)

| Clause | Category | Why it matters |
|---|---|---|
| Parties and recitals | Mandatory | Defines who the obligation runs between |
| Definition of Confidential Information | Mandatory | Without it, the NDA protects nothing |
| Standard 4 exclusions (public domain, independent dev, lawful third party, court order) | Mandatory | Without exclusions, NDA is overbroad and potentially unenforceable |
| Permitted disclosure (need-to-know employees/advisors) | Strongly recommended | Prevents technical breach by normal business use |
| Obligations of the receiving party | Mandatory | The core of the NDA |
| Term and duration of obligations | Strongly recommended | Perpetual NDAs raise enforceability concerns; 2–5 years typical |
| Return/destruction on termination | Strongly recommended | Operational obligation; needed for data protection compliance |
| No license / no IP transfer | Strongly recommended | Avoids argument that disclosure implies license |
| Governing law and jurisdiction | Mandatory | Without it, forum disputes arise |
| Injunctive relief / remedies | Strongly recommended | Monetary damages rarely adequate for breach |
| Signature block and authority | Mandatory | No contract without valid execution |
| Entire agreement / no waiver | Optional | Good practice; prevents prior discussions being cited |

### MSA (Master Services Agreement)

| Clause | Category | Why it matters |
|---|---|---|
| Parties, recitals, and definitions | Mandatory | — |
| Scope of services / SOW mechanism | Mandatory | Without it, what is the Provider obligated to do? |
| Fees, invoicing, payment terms | Mandatory | Core commercial terms |
| Term and termination (for convenience + cause) | Mandatory | Without termination rights, parties are locked in indefinitely |
| IP ownership and license | Strongly recommended | Work product ownership default varies by jurisdiction |
| Confidentiality | Strongly recommended | Overlap with standalone NDA if one exists |
| Liability cap | Strongly recommended | Without it, liability is unlimited |
| Indemnification (IP, data breach, breach of warranty) | Strongly recommended | Allocates risk for third-party claims |
| Warranties (authority, professional standard, no encumbrances) | Strongly recommended | Foundation for claims in breach |
| Data processing / DPA attachment | Mandatory where personal data is involved | GDPR/PDPL/UAE PDPL compliance |
| Governing law and dispute resolution | Mandatory | — |
| Force majeure | Strongly recommended | Especially for multi-year engagements |
| Assignment and change of control | Strongly recommended | Prevents counterparty selling the contract without consent |
| Entire agreement and amendment mechanism | Optional but good practice | — |
| Signature blocks | Mandatory | — |

### Commercial Lease

| Clause | Category | Why it matters |
|---|---|---|
| Parties (landlord + tenant) and registered entity details | Mandatory | — |
| Premises description with plan | Mandatory | Defines the demise |
| Term and commencement date | Mandatory | — |
| Rent and payment terms | Mandatory | — |
| Permitted use | Mandatory | Defines scope of occupation |
| Repair obligations allocation | Strongly recommended | Without it, default statutory allocation applies (varies) |
| Service charge | Strongly recommended for multi-tenanted buildings | — |
| Insurance obligations | Strongly recommended | — |
| Assignment and subletting provisions | Strongly recommended | Default varies by jurisdiction |
| Forfeiture / termination rights | Strongly recommended | Without it, landlord's remedies are unclear |
| Reinstatement / make-good obligation | Strongly recommended | Expensive disputes without it |
| Governing law and dispute resolution | Mandatory | — |
| Signature blocks | Mandatory | — |

### Employment Agreement

| Clause | Category | Why it matters |
|---|---|---|
| Job title and duties | Mandatory | Defines the engagement |
| Commencement date and probation period | Mandatory | Probation must be specified — defaults vary by jurisdiction |
| Compensation (salary, benefits, bonuses) | Mandatory | — |
| Working hours and location | Mandatory | Many jurisdictions regulate maximum hours |
| Leave entitlements (annual, sick, parental) | Mandatory | Statutory entitlements must be at least met |
| Termination notice periods | Mandatory | Statutory minimums apply; contract must be at least equal |
| End-of-service gratuity (MENA) | Mandatory in KSA, UAE, LB, EG | Statutory calculation; omission creates liability |
| Confidentiality | Strongly recommended | — |
| IP assignment | Strongly recommended | Default varies by jurisdiction |
| Non-compete / non-solicitation | Optional (enforceability depends on jurisdiction) | — |
| Governing law | Mandatory | — |
| Signature block | Mandatory | — |

## Jurisdictional Mandatory Clauses

Some provisions are not merely "best practice" — they are legally required or have specific local form requirements:

### UAE (onshore)

- **Governing law**: UAE Federal Law No. 33 of 2021 (Labour Law) requires employment contracts in Arabic or bilingual
- **Penalty clauses** in commercial contracts: UAE Civil Code allows courts to adjust disproportionate penalties regardless of contract terms (Article 390 equivalent); draft as indemnification rather than liquidated damages where possible
- **Real estate contracts**: must be registered with the relevant Land Department to be effective against third parties

### KSA

- **Arbitration clauses**: must specify (a) the arbitral institution (SCCA or ICC or other recognized body); (b) the seat; (c) the language; (d) the number of arbitrators. A clause saying only "disputes shall be referred to arbitration" is insufficient and courts will assume Saudi General Court jurisdiction
- **Employment contracts**: must be in Arabic; bilingual is acceptable; Arabic version prevails; must be registered with GOSI
- **Commercial Agency agreements**: must be registered with the Ministry of Commerce

### Lebanon

- **Bilateral commercial contracts of value ≥ LBP 1,000,000 (approx.)**: technically require written form under Article 254 of the Code of Obligations and Contracts (OCC) — though in practice this threshold is very low and most commercial practice is documented in writing regardless
- **Real estate transfers**: must be registered before the Land Registry; private sale agreements alone are not effective against third parties
- **Commercial leases**: Commercial Code and Law 160/1992 overlay private terms; some tenant rights cannot be waived

### DIFC / ADGM

- Contracts can be governed by DIFC / ADGM law respectively; no requirement for Arabic
- DIFC Data Protection Law and ADGM Data Protection Regulations impose DPA requirements for any processing within those free zones
- For employment: DIFC Employment Law No. 2 of 2019 (amended) and ADGM Employment Regulations require written employment contracts

## Output Format

| Missing clause | Document type | Category | Why it matters | Severity |
|---|---|---|---|---|
| Governing law | MSA | Mandatory | Courts will apply default forum rule; may be adverse | Critical |
| Data processing agreement | MSA with personal data | Mandatory | GDPR/PDPL compliance obligation | Critical |
| Liability cap | Commercial services | Strongly recommended | Unlimited liability exposure | High |
| Force majeure | Multi-year lease | Strongly recommended | No protection against closure events | Medium |
| Return/destruction | NDA | Strongly recommended | Data protection compliance gap | Medium |

Severity key: Critical = may make the contract unenforceable or expose to regulatory penalty; High = material legal risk; Medium = increased ambiguity or commercial risk; Low = best practice gap.

## Limits

- This skill identifies structural gaps; it does not assess quality of clauses that are present — use [[review-risk-flagging]] for that
- Jurisdiction-specific mandatory provisions require verification against current law — statute amendments can change what is required
- Document type classification must be accurate; if the document type is ambiguous, ask before running the checklist

## Related Skills

- [[review-risk-flagging]]
- [[review-msa-deep-review]]
- [[review-nda-quick-check]]
- [[review-unusual-terms-detector]]
- [[draft-contract-skeleton-builder]]
- [[review-indemnification-balance]]
