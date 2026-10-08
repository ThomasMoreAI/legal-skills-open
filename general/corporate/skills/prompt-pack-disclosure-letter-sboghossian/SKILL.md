---
name: prompt-pack-disclosure-letter-sboghossian
title: Disclosure Letter
description: Use when drafting a disclosure letter from a seller to a buyer in connection with a share purchase agreement (SPA) or asset purchase agreement. Covers general and specific disclosures against representations and warranties, material contracts schedules, and exceptions to warranty coverage. Relevant for corporate M&A transactions across MENA (UAE, KSA, DIFC, ADGM, LB, EG), UK, EU, and other common-law or civil-law jurisdictions. Trigger when a user needs to prepare the disclosure bundle that accompanies a signed acquisition agreement.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-disclosure-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Disclosure Letter

## When to use this

Use this skill when the seller side of an M&A transaction needs to prepare the disclosure letter that qualifies the representations and warranties given in a share purchase agreement (SPA) or asset purchase agreement (APA). The disclosure letter is the seller's primary mechanism to carve out known facts from warranty liability; getting it right is as commercially critical as negotiating the warranties themselves.

Typical triggers:
- SPA or APA has been negotiated and the parties are moving to signing/closing
- Seller's counsel needs to prepare or review the disclosure bundle
- Buyer's counsel needs to evaluate adequacy of disclosures for indemnity purposes
- Virtual data room (VDR) contents need to be incorporated by reference

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Seller name and jurisdiction of incorporation | Determines governing-law baseline and disclosure formalities | Ask before proceeding |
| Buyer name | Addressee of the letter | Ask before proceeding |
| SPA/APA title and date | Identifies which agreement the disclosures qualify | Ask before proceeding |
| Governing law of SPA | Determines enforceability of "fair disclosure" vs. "specific disclosure" standard | Ask; note jurisdiction implications below |
| List of known issues to disclose | The commercial substance of the letter | Ask in detail; this is the whole point |
| VDR or document index | General disclosures often incorporate all VDR materials by reference | Optional; include if available |

## Optional inputs

- Escrow / indemnity cap amounts (relevant context for materiality thresholds)
- List of material contracts requiring specific disclosure
- Details of pending litigation, regulatory investigations, or tax exposures
- Real property irregularities or title issues
- Employee matters (key-person risk, disputes, benefit arrears)
- IP ownership gaps or third-party claims
- Environmental or regulatory non-compliances

## Document structure

A standard disclosure letter has the following sections:

1. **Parties and recitals** — Seller(s) as disclosing party, Buyer as addressee, reference to the SPA, date of the letter (typically same day as or just before signing).

2. **Definitions** — Import key terms from the SPA (Warranties, W&I, Disclosed, Data Room, etc.). Define "Fairly Disclosed" with precision — this standard (knowledge + sufficient detail for a buyer to assess impact) is heavily negotiated.

3. **General disclosures** — Blanket incorporations by reference:
   - All documents in the VDR (list the data room index as a schedule)
   - Public registries (commercial register, land registry, court filings)
   - Searches conducted prior to signing
   - Matters of public record in the jurisdiction

4. **Specific disclosures** — Organized warranty by warranty, corresponding to the warranty schedule in the SPA:
   - Corporate existence and authority
   - Capitalization and share title
   - Financial statements and accounts
   - Material contracts — list each, attach copies or VDR references
   - Litigation and disputes — identify each proceeding and status
   - Regulatory and licenses
   - Intellectual property
   - Real estate and leases
   - Tax (underpaid taxes, open assessments, transfer-pricing exposure)
   - Employment and benefits (pending claims, arrears, key-person departures)
   - IT / cybersecurity incidents
   - Environmental

5. **Schedules** — Attach or incorporate:
   - Disclosure index (if VDR-based)
   - Material contracts list
   - Litigation schedule
   - Properties schedule

6. **Signature block** — All sellers; authorized signatories; date.

## Jurisdictional notes

| Jurisdiction | Key disclosure standard | Specific traps |
|---|---|---|
| **DIFC / ADGM** (common law) | "Fairly disclosed" — English-style standard; buyer gets benefit of the doubt if detail insufficient | W&I insurance is common; insurers will scrutinize the letter closely |
| **UAE onshore / KSA** (civil law) | Warranty-driven disclosure less developed; Commercial Companies Law and SPA govern; standard is closer to "known facts" | Notarization (tawtheeq) may be required for transfer of shares in LLCs; regulatory approvals (FDI, sector-specific) can delay closing |
| **Lebanon** | Civil Code governs; disclosure letter less formalized; often replaced by reps + indemnities with specific schedules | Enforcement of indemnities against Lebanese sellers cross-border is challenging; advise client to negotiate escrow |
| **Egypt** | Companies Law and Capital Market Authority rules for listed targets; disclosure to EGX required | Foreign ownership caps in certain sectors; Central Bank approval for financial-sector targets |
| **UK** (common law) | "Fair disclosure with sufficient detail" — the gold standard; _Infiniteland v Artisan_ line of cases | Buyer's knowledge imputed from disclosed documents; VDR references widely accepted |
| **France / civil-law EU** | Déclarations et garanties (D&G) schedule attached to the SPA; disclosure less formalized; misrepresentation rules under Civil Code apply | Penalty clauses unenforceable unless specific statutory authority; liquidated damages capped |

## Drafting standards

- Write the specific disclosures in plain, declarative prose: "The Seller discloses that the lease for the Dubai Marina office (copy at Tab 12 of the Data Room) contains a change-of-control clause that requires landlord consent to the proposed transaction."
- Do not use vague language like "various issues with" or "potential concerns" — disclosure must be specific enough that the buyer can assess the risk.
- Each specific disclosure should: (a) identify the warranty being qualified, (b) describe the fact or circumstance, and (c) reference the document in the VDR or append it.
- General disclosures should never substitute for specific disclosures where the seller has actual knowledge of a warranty breach.
- Avoid over-disclosure (disclosing irrelevant matters) — it can waive privilege and weaken negotiating position on materiality thresholds.

## Common mistakes

- **VDR dump as general disclosure**: Blanket "everything in the VDR is disclosed" without an organized index is increasingly rejected by buyers and W&I insurers. The index must be organized and complete.
- **Circular disclosures**: "We disclose that the warranties may not be accurate" — not effective; courts disregard.
- **Missing material contracts**: Contracts with change-of-control clauses must be specifically disclosed or buyer can terminate.
- **Ignoring civil-law formalities**: In UAE onshore LLC deals, the SPA and its schedules may need notarization; the disclosure letter as a standalone document may need separate authentication.
- **Timing mismatch**: The letter must be dated as of signing; post-signing updates require a supplemental disclosure letter and buyer's written agreement to accept.
- **Conflating disclosure with indemnity**: Disclosure only limits warranty claims; it does not extinguish indemnity claims for specific known liabilities (tax, litigation) which need separate indemnity provisions in the SPA.

## Related skills

- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-due-diligence-request-list]]
- [[prompt-pack-escrow-agreement]]
- [[prompt-pack-investment-agreement-venture-capital]]
