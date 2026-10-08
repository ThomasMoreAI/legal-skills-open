---
name: conversation-intake-nda-sboghossian
title: Intake — NDA
description: Use when a user wants to draft a non-disclosure agreement (NDA) or confidentiality agreement and Claude must gather the five minimum inputs before generating the document. Triggers on any request to prepare an NDA, mutual NDA, one-way confidentiality agreement, or CDA. Applies across all jurisdictions (LB, UAE, DIFC, KSA, UK, US-DE, FR). Designed for efficient single-turn intake with intelligent defaults. Routes to draft-nda-mutual or draft-nda-unilateral.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Intake — NDA

## When this applies

Activate when a user asks to draft, prepare, or review a non-disclosure agreement (NDA), confidentiality agreement (CDA), or any instrument whose primary purpose is to protect confidential information shared between two or more parties. This is the highest-volume commercial drafting request and should be handled with maximum efficiency: gather five fields, apply sensible defaults, and draft.

## Behavior

**Single-turn intake target**: gather all five required fields in one message exchange when possible.

- If the user has provided **all five**: skip intake entirely, proceed directly to [[draft-nda-mutual]] or [[draft-nda-unilateral]].
- If the user has provided **two to four**: ask only for the missing items in a single, compact message.
- If the user has provided **zero or one**: ask all five as a numbered list with sensible defaults pre-offered in brackets.

### Required fields

**Field 1: Mutual or one-way (unilateral)?**

- **Mutual**: both parties are disclosing confidential information to the other. Use when both sides are sharing sensitive information (joint venture evaluation, M&A due diligence, both parties pitching to each other, collaborative technology development).
- **One-way (unilateral)**: only one party discloses. Use when a service provider is sharing a proprietary system with a client, or when an employee is being given access to the employer's confidential information.
- If unsure: default to mutual — it is the standard in commercial transactions and is not disadvantageous to either side.

**Field 2: Parties**

Full legal names and entity types:
- Company name + jurisdiction of incorporation + entity type (Ltd, LLC, SPC, SAL, GmbH, Inc., etc.).
- Individual: full name + nationality if relevant (affects choice of law for enforcement).
- If one party is a government entity or quasi-government: flag — confidentiality obligations of government entities are often subject to freedom of information laws (UK FOIA, UAE open-government obligations) that may override contractual confidentiality.

**Field 3: Purpose**

The purpose clause defines the scope of permitted use. Examples:
- "Evaluating a possible acquisition of [Company B] by [Company A]"
- "Discussing a potential technology partnership between the parties"
- "Providing IT services to the Customer under a forthcoming MSA"
- "Employment of [Name] by [Company]"

A narrow, specific purpose clause is better for the discloser; a broad clause gives the recipient more flexibility. Confirm which side the user is representing (discloser or recipient) when drafting one-way NDAs.

**Field 4: Confidentiality term**

How long must the recipient hold information confidential?

Sensible defaults:
- Commercial transactions (evaluation, partnership): **2 years** from signing or from disclosure.
- M&A, strategic deals: **3–5 years** — longer because information revealed in due diligence remains sensitive through deal completion and for years after a deal falls through.
- Employment / HR: **perpetual** (or for as long as the information remains a trade secret) — most courts in LB, UAE, UK will give effect to perpetual confidentiality for genuine trade secrets even if the clause says "perpetual".
- Tech / IP sharing: **5 years** or perpetual for source code and genuinely proprietary algorithms.

Distinguish: the **NDA term** (how long the agreement is in force and new disclosures are covered) vs the **confidentiality obligation term** (how long after disclosure the recipient must keep information confidential). Best practice: the confidentiality obligation survives termination of the NDA for the stated period.

**Field 5: Governing law**

Offer common options with one-line guidance:

| Option | When to choose |
|---|---|
| **Lebanon (LB)** | Both parties are Lebanon-based; LB courts | Code of Obligations and Contracts governs; Arabic or French proceedings |
| **UAE (onshore)** | UAE-based parties; UAE federal courts | Federal Decree-Law on Commercial Transactions governs; Arabic proceedings |
| **DIFC** | International / cross-border; common-law regime preferred; parties want English-language courts | DIFC Contract Law (Law No. 6/2004); English proceedings; well-regarded international enforcement |
| **KSA** | Saudi parties; Saudi courts | Saudi law; Arabic proceedings; NDA enforced by Commercial Court |
| **English law** | International deals; LMA-standard transactions; parties with UK ties | Widely recognized; courts familiar to international counsel |
| **US — Delaware** | US-focused transactions; VC-backed company with US investors | Delaware courts; commercially sophisticated; US enforcement |
| **France** | French parties; EU-facing | French Civil Code (Code Civil); French courts or ICC arbitration |

If the parties are in different jurisdictions and cannot agree, suggest DIFC law for MENA cross-border deals or English law for international deals — both are common-law, widely respected, and enforceable globally.

## Optional inputs

Collect these only if the user raises them or if they are obviously relevant:

- **Standard exceptions**: the four universal carve-outs (information in public domain, independently developed by recipient, received lawfully from a third party, required to be disclosed by law or court order). These are always included; no need to ask unless the user wants to modify them.
- **Return or destruction of materials**: does the discloser want materials returned or certified destroyed on termination? Confirm if requested.
- **Injunctive relief clause**: agreement that breach will cause irreparable harm for which monetary damages are inadequate, and that injunctive relief is an available remedy without the need to post a bond. Standard in DIFC/UK/US NDAs; less standard in civil-law jurisdictions but not harmful to include.
- **Residuals clause**: recipient may retain and use general knowledge retained in the unaided memories of its personnel that was not deliberately memorized. Common in tech company NDAs; disclosers usually resist.
- **Non-solicitation / non-hire**: prohibition on recruiting the discloser's employees for a defined period. Relevant when tech teams interact during M&A due diligence or partnership discussions.
- **No license**: express statement that the NDA does not grant any IP rights to the recipient. Standard; should always be included.

## Jurisdictional notes

| Jurisdiction | Key NDA enforceability points |
|---|---|
| Lebanon | NDA enforceable under general contract law (Code of Obligations and Contracts). No specific trade-secrets statute; rely on contract and professional confidentiality (Art. 579+ COC). Injunctive relief available (référé d'urgence). Courts will reduce unconscionable damages clauses. |
| UAE (onshore) | Federal Law No. 18/1993 (Commercial Transactions); confidentiality provisions enforceable as contractual obligations. Labor law requires additional confidentiality clause in employment NDAs. Courts may void penalty clauses that are grossly disproportionate (Federal Civil Transactions Law Art. 390). |
| DIFC | DIFC Contract Law and general common-law principles; no specific trade-secrets act but equity doctrine of breach of confidence applies. Standard enforcement; injunctive relief readily available in DIFC Courts. |
| KSA | Saudi Commercial Court; contract-based enforcement; penalty clauses enforceable if proportionate. Sharia-based principles apply to contract interpretation. |
| UK | Common law breach of confidence; EU Trade Secrets Directive implemented by UK via Trade Secrets (Enforcement, etc.) Regulations 2018. Injunctive relief standard. |
| France | French Civil Code + Loi Macron trade secrets provisions (Law 2018-670). GDPR applies to personal data within the NDA's scope. |

## Examples

**Complete intake given upfront:**
> "I need a mutual NDA for our company, Acme Ltd (DIFC-registered), and XYZ Tech (UAE onshore LLC). We're exploring a potential software licensing deal. 3-year confidentiality. DIFC governing law."

Action: Extract all five fields silently. Proceed to [[draft-nda-mutual]] immediately with: mutual / Acme Ltd (DIFC) + XYZ Tech (UAE LLC) / software licensing evaluation / 3 years / DIFC law.

**Thin intake:**
> "I need an NDA."

Ask: "To draft the NDA, I need five things: (1) Mutual (both sides sharing) or one-way? [default: mutual] (2) Full legal names of both parties? (3) What's the purpose of the disclosure? (4) How long should confidentiality last? [default: 2 years] (5) Which governing law? [options: LB / UAE / DIFC / KSA / English / US-DE / FR]"

## Do not

- Draft the NDA before confirming whether it is mutual or one-way — the entire structure differs.
- Assume the purpose is an M&A transaction without being told; purpose scoping is consequential.
- Apply US-style "at-will employment" carve-outs to MENA employment NDAs.
- Include a liquidated damages clause without noting that UAE courts may reduce disproportionate penalties under the Federal Civil Transactions Law.
- Offer perpetual NDA terms as a default for general commercial deals — most courts will honor a perpetual confidentiality obligation, but many commercial parties prefer certainty.

## Related skills

- [[draft-nda-mutual]]
- [[draft-nda-unilateral]]
- [[conversation-intake-msa]]
- [[conversation-intake-shareholders-agreement]]
- [[kb-commercial-contracts-mena]]
- [[conversation-uncertainty-language]]
