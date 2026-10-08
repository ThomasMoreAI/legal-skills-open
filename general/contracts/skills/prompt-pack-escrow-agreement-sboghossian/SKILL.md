---
name: prompt-pack-escrow-agreement-sboghossian
title: Escrow Agreement
description: Use when drafting an escrow agreement for an M&A transaction where a portion of the purchase price is held by an escrow agent to secure the seller's indemnification or other post-closing obligations. Covers escrow amount, term, release conditions, claim procedures, investment instructions, and escrow agent fees. Applicable across MENA (UAE, KSA, DIFC, ADGM, LB, EG) and internationally. Trigger when the SPA requires an escrow arrangement as part of the deal structure.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-escrow-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Escrow Agreement

## When to use this

Use this skill when drafting the three-party escrow agreement among a buyer, seller, and escrow agent that governs how a portion of M&A deal proceeds is held and released. Escrow arrangements are one of the most common deal protection mechanisms in M&A transactions: they provide the buyer with a funded source of recovery for post-closing warranty claims, without the difficulty of pursuing the seller for cash after the deal closes.

Typical triggers:
- SPA negotiated a warranty escrow (5–15% of deal price is typical)
- Specific known liability (tax claim, litigation, environmental) requires a dedicated escrow
- Sellers are individuals or offshore entities from whom post-closing recovery would be difficult
- W&I insurance has a retention/deductible that is backed by escrow

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Escrow amount | The principal amount to be held | Ask |
| Escrow term | How long funds are held (typically 12–24 months for warranty escrow) | Ask; default 18 months |
| Escrow agent identity | The bank or trust company holding the funds | Ask |
| Governing law | Determines the legal framework for the arrangement | Ask |
| Release conditions | When and how funds are released to seller | Ask |
| Claim procedure | How buyer makes a claim against the escrow | Must be precisely defined; ask |

## Optional inputs

- Investment instructions (how the funds are invested while in escrow: bank deposit, money market, government securities)
- Escrow agent fees (flat fee, percentage of fund, or transactional)
- Multiple release tranches (partial releases at 6 months, 12 months, 18 months)
- Tax treatment of interest earned on escrow funds
- Dispute resolution mechanism for contested releases

## Document structure

### 1. Parties

- Buyer (the party with the right to claim against the escrow)
- Seller(s) (the party whose funds are held)
- Escrow Agent (the neutral custodian — typically a regulated bank or escrow company)

### 2. Establishment of Escrow

- Escrow amount deposited at closing: state the amount and currency
- Funding mechanism: wire transfer to the escrow agent's designated account on the closing date
- The escrow agent acknowledges receipt and confirms the escrow account is established

### 3. Escrow Term and Release

The most heavily negotiated section:

**Standard warranty escrow release schedule**:
- **First release**: At the end of the general warranty survival period (typically 12–24 months after closing); amount released = escrow fund minus any pending claims
- **Final release**: At the later of: (a) the end of the warranty survival period; or (b) final resolution of all pending claims
- **Specific warranty / tax escrow**: May have a longer survival period (3–7 years for tax warranties); remainder released when the extended period expires

**Release mechanics**:
> "The Escrow Agent shall release the Remaining Escrow Amount to the Seller on receipt of a Joint Release Instruction from both Buyer and Seller, or an enforceable court order or arbitral award."

Define: What is a "Joint Release Instruction"? (A written instruction signed by authorized representatives of both parties)

**Contested releases**: If the Buyer has filed a claim notice before the release date, the portion equal to the claimed amount (plus a reasonable buffer) is retained until the claim is resolved; the balance is released to the Seller.

### 4. Buyer's Right to Make Claims

Define the claim procedure precisely:

1. **Claim Notice**: Buyer delivers a written Claim Notice to the Escrow Agent and Seller, specifying: the nature of the claim; the relevant warranty or indemnity provision in the SPA; the amount claimed (specifying best estimate if unliquidated).

2. **Response period**: Seller has [20–30] business days to deliver a Dispute Notice objecting to the claim. If no Dispute Notice is received, the claim is deemed accepted and the Escrow Agent releases the claimed amount to Buyer.

3. **Disputed claims**: If a Dispute Notice is received, the claimed amount is retained in escrow pending resolution by: (a) mutual agreement evidenced by a Joint Release Instruction; or (b) a final, binding decision of [the applicable arbitral tribunal / court].

4. **Minimum claim threshold**: Often the SPA specifies that buyer cannot claim until individual claims exceed a de minimis threshold (e.g., USD 50,000) and aggregate claims exceed a basket/deductible.

### 5. Escrow Agent's Role and Obligations

The escrow agent is a neutral custodian:
- Holds funds in trust; has no beneficial interest
- Acts only on Joint Release Instructions or enforceable court orders
- Must verify the identity and authorization of signatories before releasing funds
- Is not responsible for disputes between buyer and seller; its role is ministerial
- Entitled to resign on notice; replacement escrow agent must be agreed by buyer and seller

**Escrow agent protections**:
- No liability for following instructions that appear genuine and are in proper form
- No obligation to verify the underlying merits of a buyer's claim
- Right to apply to a court for directions if instructions are contradictory or unclear
- Indemnified by buyer and seller for costs incurred in its role (except for gross negligence or fraud)

### 6. Investment of Escrow Funds

Specify how the funds are invested while in escrow:
- Default: overnight bank deposit in a segregated account with [escrow bank]
- Optional: money market funds; short-term government securities (with buyer/seller joint instruction)
- Interest / income earned: allocated to [seller] (most common — seller retains the economic benefit while the escrow is held, unless a claim is made) subject to payment of taxes
- Tax reporting: escrow agent will report interest income to [seller] for tax purposes

### 7. Fees and Expenses

- Escrow agent's fees: [amount per year / percentage of fund]; payable by [buyer / seller / equally split]
- Out-of-pocket expenses (legal fees for disputed instructions, bank transfer fees): allocated between parties or paid from escrow fund

### 8. Governing Law and Dispute Resolution

- Governing law: typically the law of the jurisdiction where the escrow agent is located or where the main SPA is governed
- Disputes about the escrow agreement itself (other than the underlying SPA claims): arbitration or courts
- The escrow agreement should not conflict with the dispute resolution clause in the SPA

## Jurisdictional notes

| Jurisdiction | Escrow structure | Key considerations |
|---|---|---|
| **DIFC** | Common-law trust arrangement; escrow agents are licensed under DIFC law | DIFC Courts can issue freezing injunctions over escrow funds if disputed; robust enforcement |
| **UAE onshore** | UAE banks act as escrow agents; escrow concept recognized under UAE Civil Transactions Law | For UAE deals, the escrow account is typically held with a UAE bank (Emirates NBD, ADCB, FAB); certified Arabic escrow agreement recommended |
| **KSA** | Escrow through Saudi banks; regulated by SAMA | Saudi law escrow agreements; Saudi banks have internal escrow departments for commercial transactions |
| **Lebanon** | Historically difficult due to banking crisis; escrow outside Lebanon (Cyprus, France, UAE) is common for Lebanon deals | Post-2019 banking crisis, Lebanese bank escrows are not reliable; use offshore escrow |
| **ADGM / UK** | Common-law escrow; established law and practice | SRA-regulated law firms can act as escrow agents in the UK; ADGM entities use ADGM-regulated escrow services |

## Common mistakes

- **Vague release conditions**: An escrow agreement that says "funds released when the parties agree" without specifying the claim procedure creates a standoff that requires litigation to resolve.
- **No dispute resolution for contested releases**: Without a mechanism for resolving disputes when the buyer and seller cannot agree on a release, the escrow becomes a de facto permanent holdback.
- **Wrong escrow agent**: Using an unregulated entity or the law firm's client account as escrow is unprofessional and creates risk; use a regulated bank or licensed escrow agent.
- **Failure to address interest tax**: Interest earned on the escrow account during the holding period has tax implications; failure to address this leads to disputes about who bears the tax on interest income.
- **No provision for escrow agent resignation**: If the escrow agent withdraws from the market or the relationship breaks down, there must be a mechanism to appoint a successor.

## Related skills

- [[prompt-pack-disclosure-letter]]
- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-earnout-provisions-drafting]]
- [[prompt-pack-investment-agreement-venture-capital]]
