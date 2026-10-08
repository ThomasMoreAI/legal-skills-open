---
name: prompt-pack-shareholder-agreement-key-terms-sboghossian
title: Shareholder Agreement Key Terms
description: Use when shareholders or their counsel need to draft or negotiate the key terms of a shareholders' agreement, covering governance, board composition, reserved matters, transfer restrictions (tag-along, drag-along, ROFR/ROFO), anti-dilution, dividend policy, deadlock resolution, and exit mechanisms. Focuses on identifying and negotiating the most commercially sensitive provisions before a full shareholders' agreement is drafted. MENA-specific guidance on enforceability of transfer restrictions and governance rights in UAE LLC, DIFC, and KSA entities.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-shareholder-agreement-key-terms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Shareholder Agreement Key Terms

## When to use this

Use this skill when:
- Shareholders are in early-stage negotiation and need to agree commercial terms before instructing lawyers to draft a full shareholders' agreement (SHA).
- A term sheet or heads of terms for a shareholders' agreement is needed.
- An existing shareholders' agreement is being renegotiated and the key terms need to be reset before a full redraft.
- A new investor is being onboarded and the investment terms need to be mapped before formal documentation.

**Relationship to full SHA:** This skill produces a key-terms document (commercial term sheet or heads of terms). For the full legal agreement, use [[prompt-pack-shareholders-agreement]]. The key-terms document is typically non-binding on substance but binding on exclusivity and confidentiality.

## Key terms to address

The following are the commercially critical provisions in any shareholders' agreement. The key-terms document should resolve each one before a full SHA is drafted.

### 1. Governance

**Board composition:**
- Total board size.
- Each shareholder's right to appoint director(s) based on percentage ownership (e.g., 10%+ → 1 board seat; 25%+ → 2 seats; majority shareholder → majority of seats).
- Independent directors: required by institutional investors and listing rules; number and appointment process.
- Chairman: rotating vs. fixed; casting vote.
- Board quorum: minimum attendance; typically requires at least one director from each major shareholder bloc.

**Board meeting mechanics:**
- Meeting frequency (quarterly minimum is standard).
- Notice period.
- Decision-making: simple majority vs. special majority for specific matters.
- Written resolutions: unanimous or majority?

### 2. Reserved matters (shareholder veto rights)

Reserved matters require approval above simple board majority — typically shareholder supermajority (75%) or specific shareholder consent. The negotiation is about whose consent is required and what the threshold is.

**Typical reserved matters:**

| Matter | Approval Required |
|---|---|
| Annual budget approval | Board + [Investor] approval |
| Capex above [threshold] | Board + [Investor] approval |
| Borrowing above [threshold] | Shareholder supermajority |
| Acquisition above [threshold] | Shareholder supermajority |
| Change of business scope | Unanimous shareholder approval |
| Issuance of new shares | Shareholder approval (anti-dilution trigger) |
| Related-party transactions above [threshold] | Non-interested shareholder approval |
| Dividend policy changes | Shareholder agreement |
| Appointment / removal of CEO | Board + [Investor] approval |
| Amendment of constitutional documents | Unanimous or supermajority |
| Liquidation / winding up | Unanimous or supermajority |
| IPO / exit | Supermajority or per exit provisions |

**MENA note:** UAE LLC law requires notarized amendments to the Memorandum of Association for certain reserved matters; the SHA's reserved matters list must be consistent with or supplement what the MOA already requires.

### 3. Transfer restrictions

**Right of First Refusal (ROFR):**
- Before any shareholder transfers shares to a third party, they must offer the shares to existing shareholders pro-rata at the same price and terms.
- ROFR exercise period: typically [30/60] days from offer notice.
- Failure to exercise: shareholder may sell to the third party on terms no more favorable than offered to existing shareholders.

**Right of First Offer (ROFO):**
- Transferring shareholder must first offer to existing shareholders (without stating a price); if no agreement within the notice period, the transferring shareholder may seek a third-party buyer.
- Less protective than ROFR but preferred by sellers because it allows price discovery.

**Tag-along rights:**
- If a majority shareholder (or shareholder above a threshold, e.g., 30%) proposes to sell, minority shareholders have the right to sell their shares to the same buyer on the same terms.
- Partial tag: proportional right to tag on a proportional basis.
- The buyer must be willing to acquire all tagged shares (or the majority seller cannot proceed).

**Drag-along rights:**
- If shareholders above a threshold (e.g., 70%/75%) agree to sell to a third party, they may require the remaining shareholders to sell on the same terms.
- Protects majority from being held hostage by a minority blocking a trade sale.
- Fair price protection: drag is typically conditioned on the price being at or above a minimum (sometimes the higher of FMV or a return multiple for the dragged party).

**Lock-up period:**
- Shareholders may not transfer shares for a defined period (e.g., 18–36 months from the shareholder agreement date), except to permitted transferees.

**Permitted transfers:**
- Transfers to affiliates, holding companies, or related trusts are typically permitted without triggering ROFR/ROFO; subject to a joinder agreement to the SHA.

### 4. Anti-dilution protections

**Pre-emption on new issuances:**
- Each shareholder has the right to subscribe for new shares pro-rata to their existing holding before any new shares are issued to third parties.
- Full ratchet vs. broad-based weighted average anti-dilution:
  - Full ratchet: if new shares issued at a lower price, investor's price is reset to the new lower price (very investor-favorable; uncommon in MENA early-stage).
  - Weighted average: investor's effective price is adjusted using a formula that averages the old and new price weighted by number of shares; more balanced.
- **MENA note:** Anti-dilution via price-adjustment mechanisms requires amendment of constitutional documents in UAE LLC and KSA LLC structures; simpler pre-emption rights are easier to implement.

### 5. Dividend policy

- Minimum distribution: if distributable profits exceed [threshold], [X%] must be distributed annually (or: discretionary).
- Preferred dividends: institutional investors may require a preferred dividend (cumulative or non-cumulative) before common shareholders receive any distribution.
- Reinvestment carve-out: no dividend obligation if profits are required for agreed capex or debt service.

### 6. Deadlock resolution

A deadlock occurs when board or shareholder votes are tied and no resolution can be passed.

**Escalation procedure:**
- Step 1: refer to CEOs of each shareholder party for negotiation ([30] days).
- Step 2: refer to Chairmen / senior representatives ([30] days).
- Step 3: if still unresolved: [see below].

**Resolution mechanisms:**
- *Independent expert:* an agreed expert determines the deadlocked issue (good for business/valuation questions; not suitable for governance deadlock).
- *Put/call (Texas Shootout):* either party may offer to buy the other's shares at a stated price; the offeree may elect to buy the offeror's shares at that same price instead. Creates a strong incentive to price fairly.
- *Russian Roulette:* similar to Texas Shootout; one party names a price; the other must either buy or sell at that price.
- *Windup:* if deadlock continues beyond [90/180] days, any shareholder may require the company to be wound up (last resort; avoid unless deadlock is truly irresolvable).

**MENA note:** UAE LLC law does not specifically regulate deadlock; courts have discretion in winding-up applications. The SHA mechanism is contractual; enforcement of Texas Shootout / Russian Roulette provisions depends on UAE courts' willingness to give specific performance.

### 7. Exit mechanisms

**IPO:**
- If shareholders holding [X%] request an IPO, the company and all shareholders must use best efforts to facilitate one.
- IPO conditions: minimum revenue/EBITDA; minimum valuation; approved exchange (DFM, ADX, Tadawul, NASDAQ Dubai).
- Lock-up: post-IPO lock-up period for founders/management.

**Trade sale:**
- Drag-along mechanics (above) govern compulsory sale situations.
- Sale process: auction / bilateral negotiation; who runs the process; fairness opinion.

**Put options (investor exit):**
- Investor may put its shares back to founders/company at a formula price (cost + IRR hurdle; or FMV) after a defined period if no IPO/trade sale has occurred.
- **MENA note:** Put options in UAE onshore companies may face enforceability issues if framed as guaranteed returns (which may be characterized as interest / riba in a Sharia context). Structure as a market-price put or seek advice on Sharia-compliant equivalents.

**Buyout at FMV:**
- On any shareholder's departure (death, incapacity, breach of SHA, change of control), remaining shareholders may buy out the departing shareholder at FMV (or at a discount to FMV for cause).
- Valuation mechanism: agreed valuer; bidding procedure; expert determination.

## Jurisdictional notes

### UAE LLC — onshore
- Transfer restrictions (ROFR, drag-along) are enforceable as contractual rights; they can also be embedded in the MOA (notarized) for stronger enforcement via the commercial register.
- Preferred returns / IRR provisions: review against UAE interest prohibition principles; structure as profit-sharing (mudarabah / musharakah) where Sharia compliance is required.
- Company law limits: LLC shares cannot be freely transferable without compliance with Art. 79+ of Commercial Companies Law.

### DIFC / ADGM
- Common-law principles; SHA provisions are freely enforceable as contracts.
- Share transfer provisions can also be embedded in the Articles of Association for additional protection.
- Anti-dilution mechanisms (weighted average, broad-based) are standard in DIFC/ADGM PE/VC structures.

### KSA
- Saudi LLC (Sharikat dhat mas'ooliyyah mahdoodah): transfer restrictions enforceable by contract; amendments to articles must be notarized and registered with MISA.
- Preferred dividend structures: check Sharia compliance if any party requires Sharia-compliant investment.
- Drag-along: enforceable by contract; courts may scrutinize fairness to minority shareholders.

## Key negotiation points (common battlegrounds)

| Issue | Founder position | Investor position |
|---|---|---|
| Board composition | Majority with founder | Investor seat + veto rights |
| Reserved matters | Narrow list | Broad list; low thresholds |
| Anti-dilution | Weighted average | Full ratchet |
| Drag-along threshold | 75%+ | 50.1% |
| Tag-along | Full tag | Pro-rata tag only |
| Deadlock | Windup as last resort | Put option / buyout rights |
| Exit timeline | No fixed date | Put option after 5 years |
| Dividend | Discretionary | Preferred dividend |

## Related skills

- [[prompt-pack-shareholders-agreement]]
- [[prompt-pack-share-purchase-agreement]]
- [[prompt-pack-shareholders-resolution]]
- [[prompt-pack-related-party-transaction-policy]]
- [[heuristic-always-state-jurisdiction-first]]
