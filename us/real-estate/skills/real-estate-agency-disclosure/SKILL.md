---
name: real-estate-agency-disclosure
title: Real Estate Agency Disclosure
description: Drafts state-compliant real estate agency disclosure documents for residential transactions. Triggers at first substantive contact with buyers or sellers, when preparing pre-transaction disclosure forms, or when establishing representation relationships and fiduciary duties among transaction parties.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/real-estate-agency-disclosure
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Real Estate Agency Disclosure

Produces a jurisdiction-compliant disclosure establishing representation relationships and fiduciary duties before parties commit to a residential real estate transaction.

## Required Inputs

1. **Jurisdiction** — state where property is located (drives all statutory requirements)
2. **Parties** — legal names of buyer(s), seller(s), licensee(s); brokerage names; license numbers
3. **Transaction** — property address; purchase or listing
4. **Agency model** — buyer's agent, seller's agent, dual agency, designated agency, or transaction brokerage

## Workflow

### 1. Research Jurisdiction Rules

- Identify the state statute or regulation mandating the disclosure
- Confirm the delivery trigger (typically first substantive contact — verify state-specific timing)
- Determine permissible agency models and whether the state requires verbatim statutory language

### 2. Draft Document

**Header**: document title (use jurisdiction-mandated title if required), disclosure date, all party names with brokerage and license numbers.

**Statutory basis**: cite the specific statute, state the delivery trigger, note any timing variations.

**Agency relationship definitions** — include all models permitted in the jurisdiction:

| Role | Represents | Core Duties |
|---|---|---|
| Seller's Agent | Seller exclusively | Loyalty, confidentiality, best price/terms for seller |
| Buyer's Agent | Buyer exclusively | Loyalty, confidentiality, best price/terms for buyer |
| Dual Agent | Both parties | Neutrality; no advocacy or cross-disclosure of confidential info |
| Designated Agent | Respective client (separate agents, same brokerage) | Full fiduciary to each; supervising broker is dual agent |
| Transaction Broker | Neither party | Honesty, material fact disclosure, ministerial care |

Distinguish **client** (full fiduciary) from **customer** (honest dealing, no advocacy).

Core fiduciary duties where full agency applies: loyalty · confidentiality · disclosure · obedience · reasonable care · accounting.

### 3. Address Dual Agency / Alternatives

- [ ] State permits dual agency?
- [ ] Informed written consent required?
- [ ] Transaction broker/facilitator role available?
- [ ] Designated agency required in lieu of dual agency?

If **prohibited**: state explicitly and identify the required alternative.
If **permitted**: include conspicuous warning that the agent cannot fully advocate for either party; consent required beyond this disclosure.

### 4. Acknowledgment Language

The disclosure must state:
- Receipt does **not** create an agency relationship
- Agency requires a **separate written agreement**
- Parties may choose any available representation type or proceed unrepresented
- Parties may seek independent legal counsel

### 5. Agency Election

Include on-form selection if jurisdiction requires:
- [ ] Seller's Agency
- [ ] Buyer's Agency
- [ ] Dual Agency *(where permitted)*
- [ ] Designated Agency
- [ ] Transaction Brokerage

### 6. Signature Blocks

Separate block per buyer, seller, and licensee: printed name, signature, date, license number and brokerage (licensees only). Include caption confirming receipt and understanding.

- Check whether jurisdiction requires witness signatures or notarization
- If electronic: confirm UETA / E-SIGN compliance [VERIFY]

## Pitfalls

- **Verbatim language** — many states require exact statutory text; do not paraphrase without confirming flexibility
- **Timing errors** — cite the applicable delivery trigger explicitly; late disclosure can void the relationship
- **Dual agency inadequacy** — insufficient disclosure of limitations can void consent and create liability
- **No recommendation** — the disclosure informs of options; it must not advise which representation type to select
- **NAR vs. statute** — follow NAR guidelines but state statutory requirements control where they diverge
- **[VERIFY]** all statutory citations against the current state code and real estate commission regulations before use in an actual transaction
