---
name: stamp-duty-calculator-appgambitstudio
title: Stamp Duty Calculator Skill
description: Multi-state stamp duty calculator for Indian contracts — Gujarat, Maharashtra, Delhi, Karnataka. Auto-invoked when discussing contract costs, stamping, or registration requirements.
author: AppGambitStudio
author_url: https://github.com/AppGambitStudio/experimental-agents/tree/main/implementation/legal-contract-agent/.claude/skills/stamp-duty-calculator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: contracts
language: en
---

# Stamp Duty Calculator Skill

## Supported States
- Gujarat
- Maharashtra
- Delhi
- Karnataka

## Supported Document Types
- Service Agreement
- NDA
- Employment Agreement
- MSA (Master Services Agreement)
- Lease Agreement

## Duty Types

### Fixed Duty
- A flat amount regardless of contract value
- Example: Gujarat NDA = Rs 100, Maharashtra NDA = Rs 500

### Percentage-Based Duty
- Percentage of contract value, often with a maximum cap
- Example: Gujarat Service Agreement = 0.5% of contract value, capped at Rs 25,000

## Key Rules

### Section 35, Indian Stamp Act 1899
- Unstamped or under-stamped documents are INADMISSIBLE as evidence in court
- This is a critical compliance requirement, not optional

### e-Stamping
- Available in most states
- Preferred over physical stamp paper
- Verify via SHCIL portal (shcilestamp.com)

### Penalty for Deficiency
- 2% per month of the deficiency amount
- Maximum penalty: 4x the original duty amount
- Can be cured by paying the deficit + penalty

### Registration
- Some documents require registration with the Sub-Registrar
- Lease agreements exceeding 12 months must be registered
- Registration fees are separate from stamp duty

## Calculation Process

1. Identify the state where the contract is executed
2. Identify the document type
3. If percentage-based: multiply contract value by rate percentage
4. If percentage-based with cap: apply the cap if raw amount exceeds it
5. If fixed: use the fixed amount

## Tools to Use

- `get_stamp_duty` — calculate stamp duty for a specific state, document type, and contract value
- Always mention e-stamping availability and registration requirements in the output
