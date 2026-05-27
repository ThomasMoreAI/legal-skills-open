---
name: shareholder-rights-plan
title: Shareholder Rights Plan
description: 'Drafts a U.S. shareholder rights plan (poison pill) package including rights agreement, certificate of designations, board memo, Form 8-K, and press release. Applies Unocal/Revlon fiduciary framing, Rule 13d-3 beneficial ownership, flip-in/flip-over economics, and redemption/exchange mechanics. Use when a board addresses a hostile bid, activist accumulation, or plan renewal. Trigger: "poison pill", "rights plan", "rights agreement", "flip-in", "flip-over", "DGCL 203", "Unocal", "Revlon".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/shareholder-rights-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Shareholder Rights Plan

Produces an execution-ready rights plan package with board rationale and post-adoption compliance steps.

## Prerequisites

Collect before drafting:

1. Charter and bylaws (blank-check preferred authority, vote thresholds)
2. Cap table and outstanding equity/derivative positions
3. Board resolution template
4. Proposed Rights Agent and fee terms
5. Trading price range and peer plan comparables
6. Incorporation jurisdiction and exchange listing rules
7. Known large holders, activism context, or inbound bid details

## Quick Start

1. Run fact intake checklist (Section 1)
2. Set key plan terms with the board (Section 2)
3. Draft rights agreement per outline (Section 3)
4. Prepare certificate of designations, board memo, and disclosure package (Sections 4-6)
5. Execute post-adoption checklist (Section 7)
6. Use `[PLACEHOLDERS]` for all client-specific inputs

## Workflow

### 1. Fact Intake

- [ ] Incorporation state standards (Unocal/Revlon for Delaware)
- [ ] Anti-takeover statute applicability (e.g., DGCL 203)
- [ ] Charter/bylaw constraints on rights or preferred issuance
- [ ] Exchange rules and proxy advisor policies [VERIFY]
- [ ] SEC reporting timeline (Form 8-K within 4 business days) [VERIFY]
- [ ] Existing defensive measures and thresholds
- [ ] Peer rights plan comparables

### 2. Key Plan Terms

| Term | Default Range | Notes |
|---|---|---|
| Trigger threshold | 10%-20% | Adjust for ownership concentration |
| Distribution Date | 10 biz days post-trigger or tender offer | Board may extend/shorten |
| Exercise Price | 2x-3x market price | Drives dilution severity |
| Duration | 1-10 years | Align with governance norms |
| Redemption price | $0.001/Right | Nominal; confirm economics |
| Exchange ratio | 1 share/Right | Subject to adjustments |

### 3. Rights Agreement Outline

**Preamble and definitions:**
- Parties: company name, state, principal office; Rights Agent
- Recitals: fiduciary rationale, shareholder value protection
- Key definitions: Acquiring Person (threshold + affiliate aggregation + exceptions), Beneficial Ownership (Rule 13d-3), Distribution Date, Flip-In Event, Flip-Over Event, Expiration Date

**Rights issuance and preferred stock:**
- One Right per outstanding share; attach to common until Distribution Date
- Series A Junior Participating Preferred: dividend, voting, and liquidation parity with common

**Triggering mechanics:**
- 10 biz days after public announcement of threshold ownership
- 10 biz days after tender/exchange offer commencement
- Exceptions: inadvertent acquirer cure, passive investor certification, repurchase-induced increases

**Flip-in provisions:**
- Non-Acquiring holders buy common at 50% discount; Acquiring Person Rights void
- Exercise procedures, payment methods, fractional share cash-in-lieu

**Flip-over provisions:**
- Post-Flip-In merger/asset sale triggers right to buy acquirer shares at 50% discount
- Acquirer assumption or supplemental agreement required
- Covenant to maintain sufficient authorized shares

**Redemption, exchange, and amendment:**
- Pre-Distribution redemption at nominal price
- Post-Flip-In exchange for common at set ratio
- Broad pre-trigger amendment authority; no post-trigger adverse changes to non-Acquiring holders

**Termination:**
- Fixed expiry, redemption, exchange, or board-approved merger
- Optional annual review covenant

**Rights Agent and governance:**
- Limited duties, reliance on company instructions, indemnification, successor mechanics
- Governing law: incorporation state; exclusive forum for internal corporate claims

### 4. Certificate of Designations

- Series name, authorized shares count
- Dividend, voting, and liquidation parity with common
- Conversion/exchange mechanics tied to Rights
- Anti-dilution adjustments

### 5. Board Memo

- Fiduciary framework: Unocal/Revlon threat analysis and proportionality
- Market comparables and governance considerations
- Recommended terms and alternatives considered

### 6. Disclosure Package

- Form 8-K summary and exhibit list [VERIFY]
- Press release with key terms and FAQ
- Exchange notice checklist [VERIFY]

### 7. Post-Adoption Checklist

- [ ] File Certificate of Designations with Secretary of State
- [ ] File Form 8-K with rights agreement and exhibits [VERIFY]
- [ ] Notify exchange and transfer agent [VERIFY]
- [ ] Issue press release and update investor materials
- [ ] Train internal contacts and Rights Agent on exercise/redemption workflows

## Pitfalls

- **Fiduciary record is mandatory.** Board rationale and proportionality analysis (Unocal/Revlon) must be documented — absence invites challenge.
- **Authorized shares shortfall.** Verify sufficient authorized shares for flip-in/exchange and flip-over before adoption.
- **Charter conflicts.** Confirm no bylaw or charter constraints block rights or preferred issuance.
- **Proxy advisor exposure.** Review ISS/Glass Lewis policies before setting thresholds or duration [VERIFY].
- **Disclosure timing.** Form 8-K is due within 4 business days of adoption [VERIFY].
