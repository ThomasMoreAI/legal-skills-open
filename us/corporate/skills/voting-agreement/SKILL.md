---
name: voting-agreement
title: Shareholder Voting Agreement
description: 'Drafts enforceable shareholder Voting Agreements coordinating director elections, fundamental transactions, charter amendments, and other corporate matters for closely-held companies and venture financings. Covers DGCL §218 compliance, irrevocable proxy mechanics, transfer-binding provisions, and integration with related governance documents. Trigger keywords: "voting agreement", "shareholder voting", "director election commitment", "irrevocable proxy", "board composition agreement", "DGCL 218".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/voting-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Shareholder Voting Agreement

Draft a binding voting agreement coordinating shareholder voting on specified corporate matters, integrated with related governance documents and jurisdiction requirements.

## Prerequisites

1. **Corporate details** — jurisdiction, cap table, share classes and voting rights.
2. **Parties and holdings** — legal names, entity type/formation state, share counts and percentages.
3. **Transaction context** — financing round, merger, founder arrangement, or standalone governance.
4. **Related agreements** — investors' rights, ROFR/co-sale, stockholders' agreement (for consistency).
5. **Voting scope** — board composition, fundamental transactions, charter/bylaw amendments, equity plan approvals.
6. **Term preference** — IPO/liquidity-tied, employment-tied, fixed period, or perpetual.

## Output Structure / Process

### 1) Document Skeleton
```text
VOTING AGREEMENT
- Parties; Effective Date; Recitals
1. Definitions
2. Voting Commitments
3. Irrevocable Proxy
4. Enforcement / Specific Performance
5. Representations and Warranties
6. Covenants
7. Transfer Provisions
8. Term and Termination
9. Governance Integration
10. Miscellaneous
Signatures
Schedule A — Shareholdings
Exhibit A — Form of Irrevocable Proxy
Exhibit B — Form of Transferee Joinder
```

### 2) Recitals
- Total shares outstanding; parties' aggregate voting percentage.
- Transaction or event precipitating the agreement.
- Cross-references to related agreements by name and date.

### 3) Party Identification

| Field | Individual | Entity |
|---|---|---|
| Name | Full legal name | Entity name + formation state |
| Address | Residential | Principal business address |
| Shares | Record + beneficial if nominee-held | Record holder + beneficial owner |
| Execution | Personal | Signatory name, title, authorization |

### 4) Voting Commitments

| Matter | Commitment Type | Key Mechanics |
|---|---|---|
| Director elections | Vote for named individuals/group designees | Nomination, qualifications, replacement |
| Fundamental transactions | Affirmative / negative / board-directed | Conditional criteria if applicable |
| Charter/bylaw amendments | As specified per type | Class vote applicability |
| Authorized share increases | As specified | Which class(es) subject |
| Equity incentive plans | As specified | Board-approval prerequisite |

Additional commitment mechanics:
- **After-acquired shares**: whether options, warrants, dividends, or market purchases are automatically subject or require amendment.
- **Quorum covenant**: attend or deliver proxies to ensure quorum.
- **Written consent**: execute when board-approved matters proceed by consent in lieu of meeting.

### 5) Irrevocable Proxy
- Explicitly irrevocable; coupled with an interest per DGCL §212(e) [VERIFY equivalent for non-Delaware].
- Triggered only on breach or failure to vote as required — self-executing enforcement, not routine mechanism.
- Survives bankruptcy, death, incapacity, and share transfer.
- Scope: vote shares, execute consents, take all actions to effectuate commitments.
- Appoints proxy holder as attorney-in-fact with full authority.

### 6) Enforcement
- Voting rights unique; breach causes irreparable harm not compensable by damages.
- Specific performance and injunctive relief **without bond**.
- Equitable remedies cumulative with all other remedies.

### 7) Transfer Provisions

| Approach | Mechanics |
|---|---|
| **Runs with shares** | Transferee joinder as condition precedent; corporation refuses to record without joinder |
| **Personal only** | Transfer releases obligation; specify adjustment/termination rights for remaining parties |

- Advance notice to other parties required.
- Include Form of Transferee Joinder as exhibit.

### 8) Term and Termination

**Term**: DGCL §218 imposes no duration cap on voting agreements (voting trusts are the capped instrument) [VERIFY for non-Delaware].

**Auto-termination triggers**:
- Qualified IPO meeting size/exchange criteria
- Change of control or acquisition
- Dissolution or winding-up
- Collective ownership falls below [___]% threshold

**Voluntary termination**: unanimous written consent or [supermajority] of subject shares — distinguish core provisions (unanimous) from administrative (supermajority).

**Partial termination**: specify full termination vs. departing-party-only.

### 9) Reps, Warranties, and Covenants

**Each party represents**:
- Sole legal/beneficial owner (or disclose nominee arrangement).
- Shares free of liens, encumbrances, and conflicting voting arrangements.
- Full authority; no required third-party consents; no conflicting obligations.
- **Entities add**: due organization, good standing, authorized signatory.

**Covenants**:
- Vote all subject shares per agreement at meetings and by consent.
- No conflicting proxies, trusts, or arrangements.
- Execute documents reasonably necessary to effectuate obligations.
- Timely notice of proposed transfers.

### 10) Governance Integration
- Designate controlling document in conflicts with related agreements.
- **Multi-class stock**: identify subject classes; address class-specific vote interaction.
- **Voting instruction procedure**: notice method, timing, default if instructions not timely received.

### 11) Schedule/Exhibit Map

| Label | Content |
|---|---|
| Schedule A — Shareholdings | Party, share count, class, certificate numbers, % outstanding |
| Exhibit A — Irrevocable Proxy | Self-executing proxy for use upon breach |
| Exhibit B — Transferee Joinder | Transferee bound to voting commitments |

## Guidelines

- **DGCL §218** governs Delaware voting agreements; confirm analogous statute for non-Delaware [VERIFY].
- Irrevocable proxy must be "coupled with an interest" — the voting agreement itself supplies the interest; include explicit recitation in the proxy.
- Enumerate specific covered matters; vague commitments create enforcement ambiguity.
- Reconcile with preferred stock protective provisions — preferred holders may hold class vote rights outside this agreement.
- If parties hold less than majority voting power, flag that the agreement may not achieve control objectives.
- Ensure no conflicts with concurrent investors' rights, ROFR/co-sale, or stockholders' agreements.
- Governing law should match state of incorporation; amendments should distinguish core vs. administrative thresholds.
