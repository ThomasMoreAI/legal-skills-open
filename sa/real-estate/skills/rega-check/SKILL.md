---
name: rega-check
title: rega-check
description: Verify a listing form, deal, or property route satisfies Saudi REGA compliance — FAL license, ad license, GASTAT category, Saudi address, photos, commission cap. Use when adding listing-related features or before shipping property changes.
author: malhajri07
author_url: https://github.com/malhajri07/real-estate-CRM-project/tree/main/.claude/skills/rega-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: real-estate
language: en
---

# rega-check

REGA (Saudi Real Estate General Authority) rules are non-optional. Listings must carry valid licenses; deals must respect commission caps.

## Required for any listing

- [ ] **FAL license number** (`falLicenseNumber`) — agency-level brokerage license
- [ ] **Ad license number** (`adLicenseNumber`) — per-listing REGA-issued
- [ ] **REGA agent ID** linked to the agent profile
- [ ] **GASTAT category + type** — one of the 5 categories × 33 types (no free-text)
- [ ] **Valid Saudi address** — city + district from the official list
- [ ] **At least one photo**
- [ ] **Saudi mobile** for the agent (`+966 5X XXX XXXX`)

## Required for any deal

- [ ] **Commission ≤ 2.5%** of sale value (validated server-side, not just client)
- [ ] **RETT (5%)** calculated and stored on closed deals
- [ ] **Brokerage agreement** uploaded as `deal_documents`

## Steps

1. **Identify the target** — which form, route, or model is the user adding?
2. **For listing-related**:
   - Read `apps/api/routes/listings.ts` and the matching frontend form
   - Verify the zod schema requires every checkbox above
   - Verify the DB constraints match (NOT NULL on FAL/ad license)
3. **For deal-related**:
   - Read `apps/api/routes/deals.ts`
   - Verify commission validation (look for `2.5` or `commissionCap`)
   - Verify RETT is calculated on stage transition to `WON`
4. **For agent-related**:
   - Verify Saudi phone validation in `apps/api/lib/validation/saudi-phone.ts`
   - Verify the matching frontend zod schema
5. **Report** as a checklist: which boxes pass, which fail, and where the gap is (file:line).
6. **Do not auto-fix** REGA gaps — flag them for the user to confirm the fix approach (this is a regulated area, mistakes have legal weight).

## Verification

- [ ] All required fields verified at schema + form + API levels
- [ ] Gaps reported with file:line
- [ ] User asked before any fix

## Notes

- The 5 GASTAT categories: Residential, Commercial, Industrial, Agricultural, Land
- See [[Features/REGA Compliance]] in the vault for the canonical reference
- See [[02 - Glossary]] for term definitions
