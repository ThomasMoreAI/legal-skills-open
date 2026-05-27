---
name: safe-agreement
title: Simple Agreement for Future Equity (SAFE)
description: Drafts Simple Agreements for Future Equity (SAFE) for early-stage venture capital financing with valuation cap/discount mechanics, investor qualifications, and securities compliance. Use when drafting SAFEs, pre-seed investment documents, convertible equity instruments, or YC-style SAFE notes.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/safe-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [agreement, corporate, drafting]
---

# Simple Agreement for Future Equity (SAFE)

Drafts a SAFE granting investors future equity rights upon triggering events — no immediate ownership, no debt.

## Quick Start

Gather before drafting:

1. **Company** — legal name per certificate of incorporation, jurisdiction, state of formation
2. **Investor** — legal name, entity type, accredited investor basis
3. **Economics** — purchase amount, valuation cap, discount rate (if any)
4. **Cap table** — existing SAFEs, convertible notes, fully-diluted share count
5. **Special terms** — MFN clause, pro rata rights, side letters

## Document Structure

### Header & Recitals

| Element | Requirement |
|---|---|
| Company ID | Full legal name matching certificate of incorporation, entity type, jurisdiction |
| Investor ID | Legal name, entity type, capacity to contract |
| Purchase amount | Exact dollar figure |
| Core exchange | Capital → contractual right to future equity; state explicitly: no debt, no interest, no current stockholder status |

### Conversion Mechanics

Three triggering events:

**1. Equity Financing (automatic)**

- Converts into preferred stock of same series issued to new investors
- Conversion price = lesser of:
  - **Cap price**: Valuation Cap ÷ Pre-money fully-diluted capitalization
  - **Discount price**: Price per share × (1 − Discount Rate)
- Shares = Purchase Amount ÷ Conversion Price
- Include worked numerical example

**2. Liquidity Event (acquisition/merger/IPO)**

- Investor elects: cash = Purchase Amount OR common stock = Purchase Amount ÷ Liquidity Price
- Specify election timeline and default

**3. Dissolution**

- Cash = Purchase Amount, pre-dissolution
- Priority: senior to common, subordinate to creditors/debt

### Valuation Terms

| Term | Function |
|---|---|
| Valuation Cap | Ceiling on conversion valuation; larger stake if valuation exceeds cap |
| Discount Rate | Reduction from new investor price; rewards early risk |
| Interaction | Cap and discount are **alternative** (not additive); investor gets better result |

### Representations

**Investor:**

- [ ] Investment purpose (not for resale — supports private placement exemption)
- [ ] Accredited status — individual (income/net worth) or entity (assets/equity owner/institutional)
- [ ] Risk acknowledgments: speculative, total loss, illiquid, indefinite hold
- [ ] Sophistication or qualified advisors

**Company:**

- [ ] Valid incorporation and good standing
- [ ] Corporate power and authority
- [ ] Board/stockholder approvals obtained
- [ ] Binding obligation (standard bankruptcy/equitable exceptions)
- [ ] No conflict with charter, material contracts, or law

### Rights & Restrictions

**Pre-conversion** — no stockholder rights (no voting, dividends, distributions, preemptive rights).

**Transfer** — no transfer without written consent; unauthorized = void. Optional exceptions for affiliates, estate planning, retirement accounts.

**Securities** — unregistered; restrictive legends required; investor acknowledges illiquidity.

### Administrative Provisions

| Provision | Standard |
|---|---|
| Governing law | State of incorporation or principal place of business |
| Disputes | Litigation venue OR arbitration (rules, count, seat, costs) |
| Amendments | Written, signed by both parties |
| Waivers | Explicit, written; no implied waiver |
| Integration | Entire agreement; supersedes prior negotiations |
| Notices | Email, certified mail, or courier; specify addresses; deemed-received rules |
| Severability | Reform invalid provisions; remainder survives |

### Signature Blocks

Both Company and Investor: signature, printed name, title (entities), date.

## Checks

1. **Defined terms** — capitalize consistently; define before first use
2. **Math precision** — conversion formulas unambiguous to any financial professional
3. **Cross-references** — verify all internal section references
4. **No placeholders** — replace all `[brackets]` before finalizing
5. **YC compatibility** — if referencing YC SAFEs, align with applicable template version (post-money vs. pre-money) and flag deviations
6. **Securities exemptions** — confirm federal exemption (Reg D 506(b)/506(c)) and state blue sky requirements
7. **MFN conflicts** — check prior SAFEs for MFN clauses that could trigger
8. **Missing info** — identify gaps and request from user before finalizing
