---
name: snda
title: SNDA
description: Drafts a Subordination, Non-Disturbance, and Attornment Agreement (SNDA) for commercial real estate. Extracts key terms from lease and loan documents, structures tri-party protections balancing landlord, tenant, and lender interests. Trigger when new financing or refinancing requires subordinating tenant leases to lender liens, drafting non-disturbance protections, or preparing tri-party SNDA agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/snda
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# SNDA

Drafts a tri-party SNDA subordinating a tenant's lease to a lender's mortgage lien while securing non-disturbance protections and attornment obligations.

## Prerequisites

Collect before drafting:

1. **Lease** — executed lease with all amendments (names, premises, term, rent, renewal options, existing subordination language)
2. **Loan documents** — note, mortgage/deed of trust, loan agreement (lender name, principal, rate, legal description, recording info)
3. **Chronology** — whether lease predates or postdates mortgage recording
4. **Authority** — signatory authority confirmation for all three parties

## Quick Start

1. Extract and cross-verify key terms from lease and loan documents
2. Flag discrepancies between documents before drafting
3. Draft SNDA sections in order below
4. Confirm subordination conditionality with user
5. Present security deposit and TI allowance options for negotiation
6. Verify state-specific notarial and recording requirements

## Workflow

### 1. Document Review & Extraction

Cross-verify across all documents:

| Element | Source | Verify |
|---|---|---|
| Party legal names & addresses | Lease + Loan docs | Exact match |
| Property legal description | Lease + Mortgage | Consistent |
| Leased premises (suite, SF, APN) | Lease | Within mortgaged property |
| Lease dates & renewal options | Lease | Current and complete |
| Rent amounts & schedule | Lease | Current period confirmed |
| Loan amount, rate, terms | Note/Loan agreement | Match mortgage |
| Mortgage recording info | Mortgage | Book/page, date, county correct |
| Security deposit; TI/free rent status | Lease | Actual amounts, performed or remaining |

Flag discrepancies before proceeding.

### 2. Recitals

Establish:
- Party legal names, entity types, addresses
- Property address + full legal description (APN, county, state)
- Lease ID: date, parties, premises, term, recorded memorandum if any
- Loan ID: date, principal, mortgage recording info
- Chronological priority statement
- Lender requires subordination as loan condition; tenant requests non-disturbance as consideration

### 3. Subordination

- Lease subordinate to mortgage lien and all advances (obligatory and optional)
- Extends to renewals, modifications, consolidations, replacements, extensions, increases
- Effective regardless of lease/mortgage chronology
- Tenant acknowledges subordination as material inducement for loan
- **Conditionality**: subordination effective simultaneously with non-disturbance (confirm parties' intent)
- Multi-parcel provisions if applicable (partial releases, cross-collateralization)

### 4. Non-Disturbance

| Topic | Treatment |
|---|---|
| Core covenant | No disturbance if tenant not in default beyond cure periods |
| Prior landlord liability | Successor NOT liable for prior landlord acts/omissions |
| Prepaid rent | Successor not bound by rent paid >1 month ahead |
| Offsets/defenses | Successor not subject to claims against prior landlord |
| Security deposit | Honored only to extent actually received by successor |
| TI allowance / free rent | Address whether successor assumes unperformed concessions |
| Runs with land | Binds successors, assigns, foreclosure purchasers, deed-in-lieu grantees |

### 5. Attornment

- Tenant unconditionally attorns to successor landlord (foreclosure, deed in lieu, other enforcement)
- Self-operative — no further instruments required
- Confirmation instrument within 10–30 days if requested (no increased obligations)
- Lease continues on original terms except as modified by SNDA
- All tenant rights and options preserved subject to non-disturbance limitations

### 6. Representations & Warranties

**Landlord**: lease in force, no modifications except scheduled, no defaults, rent current, no assignment except to lender, authority to execute.

**Tenant**: lease is entire agreement, no defenses/offsets against rent, possession accepted, no undisclosed assignments/sublets, TI/concession status confirmed, authority to execute.

**Lender**: authority to execute and grant non-disturbance, status as mortgage holder.

### 7. Lender Cure Rights

- Tenant must copy lender on landlord-default notices
- Tenant may not terminate or exercise offset without giving lender cure opportunity

| Default Type | Lender Cure Period |
|---|---|
| Monetary | 30 days after landlord's cure period expires |
| Non-monetary | 60–90 days (longer if cure requires possession, provided diligent pursuit) |

- Lender may enter premises to cure; cure does not constitute lease assumption

### 8. Lease Modification Restrictions

- No material modification, termination, surrender, or rent reduction without lender consent
- Exceptions: ministerial amendments; changes improving lender security
- Unauthorized modifications void as against lender
- Address whether existing lease options (renewal, expansion) require lender consent

### 9. Administrative Provisions

Notices (addresses, delivery methods, 3-business-day rule) · Governing law (property state) · Jurisdiction (property county) · Counterparts and e-signatures · Amendments (all three parties) · Severability · SNDA controls over lease on SNDA matters · Binding on successors · Recordation rights

### 10. Execution

- Tri-party signature blocks with name, title, date
- Entity-appropriate execution format
- Notarial acknowledgments per property-state law (required if recording)

## Pitfalls

- **Conditional subordination**: always confirm parties intend subordination conditioned on non-disturbance before making self-executing
- **Security deposit / TI allowance**: most-negotiated provisions — present options, do not assume
- **Document discrepancies**: never draft over mismatches between lease and loan documents
- **Recording requirements**: vary by jurisdiction — confirm county recorder format
- **Defined terms**: cross-check for consistent usage throughout
- **Notarial form**: verify state-specific acknowledgment requirements before finalizing
