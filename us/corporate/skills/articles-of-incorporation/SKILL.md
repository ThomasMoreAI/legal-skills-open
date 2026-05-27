---
name: articles-of-incorporation
title: Articles of Incorporation
description: Drafts jurisdiction-compliant U.S. Articles of Incorporation for corporate entity formation. Analyzes formation documents, term sheets, and cap tables to produce a filing-ready charter with name, purpose, capital structure, registered agent, and governance provisions. Use when forming a new corporation, drafting a charter document, or structuring equity for venture-backed or closely held companies.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/articles-of-incorporation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Articles of Incorporation

Draft a filing-ready U.S. Articles of Incorporation tailored to the jurisdiction, capital structure, and stakeholder requirements.

## Required Inputs

1. **Jurisdiction** — state of incorporation (Delaware, Wyoming, home state, etc.)
2. **Corporate name** — with required designator (Corp., Inc., Co., Ltd.); note any name reservation number
3. **Business purpose** — general commercial or specialized (professional corp, regulated industry)
4. **Capital structure intent** — founder-only common, VC-backed (blank check preferred), dual-class, S-corp
5. **Registered agent** — name + physical street address in incorporation state (no P.O. boxes)
6. **Incorporator** — name + mailing address
7. **Supporting docs** — term sheets, cap tables, shareholder agreements, business plans (as available)

## Quick Start

1. Collect all required inputs above; flag any gaps before drafting.
2. Verify corporate name is distinguishable from existing registrations in the jurisdiction.
3. Draft articles following the structure below, selecting the applicable capital structure pattern.
4. Include standard optional provisions (exculpation, indemnification) and any negotiated provisions.
5. Add execution block and post-filing checklist as guidance appendix.

## Article-by-Article Drafting

### Article I — Corporate Name

State exact legal name with required designator. Confirm name availability; note reservation number if applicable.

### Article II — Purpose

- **Default (recommended):** "to engage in any lawful act or activity for which corporations may be organized under [State] law"
- **Narrow purpose when:** VC docs restrict capital deployment to specific sectors; regulated industries require mandatory statutory language
- Include catch-all powers: acquire/dispose property, issue securities, contract, sue and be sued

### Article III — Registered Agent and Office

Individual resident of the state OR commercial agent authorized in-state. Full physical street address required: street, suite/unit, city, county (if required), state, ZIP.

### Article IV — Capital Structure

Select the applicable pattern:

**Simple Common (founder/closely held)**
- Authorized shares: 10M–100M; leave headroom for ESOP (10–20% fully diluted) and future rounds
- Par value: $0.001 or $0.0001 (affects Delaware franchise tax — lower par = less tax under authorized shares method)
- Voting: 1 vote/share · Dividends: board discretion, pro rata · Liquidation: pro rata after creditors

**Blank Check Preferred (VC-backed)**
- Authorize board to create series without shareholder vote
- Per-series board powers: dividend rate (cumulative/non-cumulative), liquidation preference (participating/non-participating), conversion ratio + anti-dilution, redemption terms, voting rights, protective provisions
- Authorize preferred ≥ common (commonly 1:1 ratio)
- Do NOT enumerate specific series in Articles — use Certificates of Designation at each round

**Dual-Class Common (founder control)**
- Class A: 1 vote/share (public/investor) · Class B: 10 votes/share (founder; converts to A on transfer)
- Specify whether classes vote together or separately by matter

**S-Corp compliance:** Single class only; ≤100 shareholders; eligible types only (no non-resident aliens, no entity shareholders except qualifying trusts/estates)

### Article V — Incorporator

Name and mailing address. Ministerial role — signs, files, may conduct initial organizational meeting.

### Article VI — Optional Provisions

| Provision | When to Include |
|-----------|----------------|
| Director exculpation | Always — eliminates duty-of-care monetary liability (not loyalty, bad faith, intentional misconduct) |
| Indemnification | Always — directors/officers, fullest extent permitted |
| Supermajority voting | Enhanced protection needed for mergers, asset sales, dissolution, charter amendments |
| Board classification | Staggered board for takeover defense or investor negotiation |
| Preemptive rights | Shareholders want pro rata maintenance on new issuances |
| No preemptive rights | Default for VC-backed; state expressly if jurisdiction implies them |
| Close corporation | Shareholder-managed structure in recognizing jurisdictions |
| Professional corporation | Licensed services (law, medicine, accounting); include authorized services, licensure requirements, transfer restrictions |

### Execution Block

- Declaration citing applicable state corporation statute
- Incorporator signature line with printed name and date
- Notarization block only if required by jurisdiction (most states do not)

## Post-Filing Checklist

Include as guidance appendix in deliverable:

- [ ] Organizational meeting: adopt bylaws, elect directors/officers, authorize shares, open bank accounts
- [ ] Federal EIN (IRS online — immediate)
- [ ] Issue shares with documented consideration (board resolution + subscription agreement)
- [ ] Initial report if required by state
- [ ] Foreign qualification if operating outside incorporation state
- [ ] Industry-specific licenses/permits
- [ ] Annual report and franchise tax calendar reminders

## Pitfalls and Checks

- **Jurisdiction variance:** Delaware DGCL, California Corp Code, Wyoming statutes differ on par value tax, required provisions, and permissive provisions — verify current statute for each filing state
- **Delaware franchise tax:** Authorized shares method taxes on share count; assumed par value capital method may yield lower tax for high-asset companies — [VERIFY current rates]
- **Exculpation scope:** Confirm jurisdiction permits duty-of-care liability elimination; identify state-specific exceptions [VERIFY per state]
- **Professional corporations:** Confirm state-specific licensure and ownership restrictions; some states prohibit non-licensed shareholders entirely
- **S-election:** Structural compliance in Articles is necessary but not sufficient — IRS Form 2553 required post-filing
- **Scope boundary:** Do NOT include bylaw-level details (meeting procedures, officer titles, quorum) — those belong in bylaws
- **Conflicts:** If term sheet or shareholder agreement conflicts with proposed charter terms, flag for client resolution before filing
