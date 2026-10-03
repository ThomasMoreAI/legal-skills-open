---
name: vendor-check-nmoralescyber
title: Vendor Check (Legal/Contractual Paperwork Status)
description: Checks the LEGAL/CONTRACTUAL paperwork status of agreements with a specific vendor across CLM, CRM, email, and document storage — what's signed, what's missing, what's expiring, what surviving obligations remain. Pulls together MSA, DPA, SOW, NDA, BAA, COI, SOC 2, pen-test attestation, sub-processor list, and addenda. Use when the user says what's our agreement status with [vendor], do we have an MSA/DPA with [vendor], what's signed with [vendor], when does [vendor]'s contract expire, what's missing in our [vendor] paperwork, audit our paperwork with [vendor], or onboarding/renewing a vendor and need a consolidated view. Tie-breaker vs operations:vendor-review — this skill answers "WHAT do we have signed?" (backward-looking, paperwork inventory). vendor-review answers "SHOULD we use them?" (forward-looking, buy/use decision). Both can be chained for renewal/onboarding. Do NOT use for cost analysis, TCO comparison, vendor-fit evaluation, or buy/replace decisions.
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/vendor-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Vendor Check (Legal/Contractual Paperwork Status)

Consolidated view of what's signed, missing, and expiring with a vendor across all systems.

## When to use vs. operations:vendor-review

This is the most-confused vendor cluster pair. Memorize the split:

| Skill | Question it answers | Direction | Stakeholders |
|---|---|---|---|
| **legal:vendor-check (this one)** | "What's our LEGAL paperwork status?" | Backward-looking (what's signed) | Legal, procurement, compliance, security |
| `operations:vendor-review` | "SHOULD we use / continue / replace this vendor?" | Forward-looking (decision) | Ops, procurement, finance, exec |

Often used together; different outputs and stakeholders.

### Boundary tie-breaker

| Prompt signal | Skill |
|---|---|
| "What's signed," "do we have a DPA," "when does X expire" | THIS skill |
| "Should we keep using X," "compare X vs Y," "is X worth it" | `operations:vendor-review` |
| "Audit our paperwork with X" | THIS skill |
| "Audit our usage of X" (cost/usage) | `operations:vendor-review` |
| "Renew X" | BOTH — this skill first (what's signed/expiring), then operations:vendor-review (should we) |

## What this skill produces

### 1. Document inventory

Per vendor:

| Document | Status | Effective | Expiration | Notes |
|---|---|---|---|---|
| MSA | Signed / Missing / Draft | date | auto-renew or fixed | LoL terms |
| DPA | Signed / Missing | date | tied to MSA | SCCs / IDTA module |
| Sub-processor list | Current / Stale | last reviewed | refresh cadence | Notice clause? |
| SOW(s) | Per-engagement | date | end date | Active/closed |
| NDA | Signed | date | survival term | Pre/post MSA |
| BAA | Signed / N/A | date | tied to MSA | Required if PHI |
| W-9 | On file | date | annual reconfirm | — |
| COI (general liability) | Current / Stale / Expired | date | renewal date | Limits meet MSA req? |
| COI (cyber liability) | Current / Stale / Missing | date | renewal date | Min coverage flow-down |
| SOC 2 Type II report | Received | period | annual refresh | Bridge letter for gap |
| SOC 2 bridge letter | Received / Stale | date | covers audit gap | — |
| Pen-test attestation | Received / Missing | date | annual | Required for prod-access vendors |
| Vulnerability disclosure policy | On file | — | review annually | Required by some customer DPAs |
| SBOM | On file / Missing | date | per release | For software supply chain |
| Encryption attestation (TLS 1.2+, AES-256 at rest) | Received | date | annual | Cyber-insurance warranty |
| PCI-DSS AOC | Received / N/A | date | annual | If payment data |
| Security questionnaire | Completed | date | annual refresh | CAIQ / SIG / custom |
| Right-to-audit letter on file | Yes / No | — | — | Per MSA audit clause |

### 2. Gap analysis (tiered)

Each gap is classified by remediation urgency:

- **Tier 1 — Stop-the-bus:** Block further data flow until cured (e.g., DPA missing while PII flowing; BAA missing while PHI flowing; expired cyber COI on a high-risk vendor)
- **Tier 2 — Cure within 30 days:** Material gap but not actively leaking liability (stale SOC 2 with no bridge letter; missing pen-test attestation on prod-access vendor)
- **Tier 3 — Backlog:** Hygiene improvement (missing W-9 reconfirm; outdated security questionnaire by < 1 quarter)

What's missing given relationship type:

- **Vendor processes personal data (any jurisdiction)** → DPA required (GDPR Art. 28; CCPA service-provider terms)
- **Vendor processes PR-resident PII** → DPA + verify breach-notification flow-down (PR Ley 111-2005 — controller must notify DACO and affected residents; processor must notify controller without unreasonable delay)
- **Vendor processes PHI** → BAA (HIPAA 45 CFR 164.504(e))
- **Vendor handles payment cards** → PCI-DSS AOC + scope confirmation
- **Vendor has admin access to production systems** → Pen-test attestation + SOC 2 Type II + right-to-audit + breach-notification clause with ≤72hr SLA
- **Vendor is a sub-processor under a customer DPA** → 30-day customer notice obligation; sub-processor list must be public or notice list maintained
- **Vendor in restricted jurisdiction (outside adequacy)** → SCCs / IDTA / data transfer mechanism + transfer impact assessment
- **Vendor amount > materiality threshold** → Insurance COI on file (general + cyber); minimum limits per MSA
- **Vendor multi-year commitment** → Termination-for-convenience window confirmed
- **Cyber-insurance carrier requires vendor warranties** → Confirm vendor meets policy's "vendor warranty" schedule (encryption, MFA, backup, IR plan); missing = potential coverage denial
- **Vendor delivers software to us** → SBOM + vulnerability disclosure policy + license-compliance scan
- **Vendor has access to source code** → IP assignment + code-handling/destruction clause

### 3. Surviving obligations register

Even after termination, what survives. Track each with its specific clock:

| Obligation | Typical clock | Source |
|---|---|---|
| Confidentiality | 3–5 yr post-term (perpetual for trade secrets) | NDA / MSA confidentiality clause |
| IP licenses granted | Per license terms | MSA IP clause / SOW |
| Indemnification | Typically perpetual for IP, capped tail for breach | MSA indemnity clause |
| Limitation of liability | Survives termination | MSA LoL clause |
| Audit rights | 1–3 yr post-term tail | MSA audit clause |
| Data return | Customer choice within 30 days; destruction within 60–90 days | DPA |
| Sub-processor wind-down notification | Vendor must notify customer of sub-processor changes during wind-down | DPA |
| Breach notification | Continues for data still in possession during wind-down | DPA |
| Cyber-insurance tail | Verify vendor maintains tail coverage for claims-made policies | COI |
| Source code escrow release | If escrow agreement exists | Escrow agreement |

### 3a. Termination action template

For each terminated vendor, produce a dated checklist:

```
Day 0  (notice given): Confirm wind-down period in MSA/DPA, freeze new SOWs, notify InfoSec to revoke access on Day X.
Day 7:  Send data-return-format request (CSV/JSON/parquet, encryption in transit).
Day 30: Confirm receipt of data; request destruction certificate if applicable.
Day 60: Confirm sub-processor purge; confirm vendor's sub-processors also destroy.
Day 90: Destruction certificate received and filed; close vendor in CLM with surviving-obligation watch list (NDA, IP, indemnity, audit-tail).
Year 1+: Calendar reminders for any tail clocks (audit rights, indemnification, NDA expiry).
```

### 3b. Sub-processor change protocol

When vendor announces a new sub-processor:

1. Check our customer DPAs for sub-processor notice obligation (typical: 30-day prior notice with right to object).
2. Push notice to affected customers within their contractual window.
3. Update sub-processor list in own DPA / trust center.
4. If customer objects: coordinate with vendor on alternative routing or accept termination right.
5. Confirm new sub-processor meets our security baseline (encryption, location, certifications).

### 4. Upcoming deadlines

Forward view with owner:

- Auto-renewal notice deadlines (often 30–90 days before renewal — set calendar reminder)
- Termination-for-convenience windows
- Annual obligations: COI refresh, SOC 2 refresh, pen-test refresh, security questionnaire, sub-processor review
- Pricing review windows
- Customer DPA notice windows triggered by sub-processor changes

## When to chain to other skills

- **About to negotiate a new vendor agreement:** chain to `legal:review-contract`
- **Deciding renewal vs. switch:** chain to `operations:vendor-review`
- **DPA missing and vendor processes personal data:** chain to `legal:legal-risk-assessment` for the privacy exposure score
- **About to onboard new vendor:** chain to `operations:vendor-review` first (decision), then this skill (paperwork) once decided
- **Suspected vendor security incident:** chain to `legal:legal-risk-assessment` (notification clocks) and `operations:risk-assessment` (containment)

## Decline triggers (do NOT use this skill if)

- Question is "should we use vendor X" (decision) → `operations:vendor-review`
- Question is "negotiate this clause with vendor X" (redline) → `legal:review-contract`
- Question is "what's the legal exposure if X fails" (risk score) → `legal:legal-risk-assessment`
- Question is "did X have an outage last week" (operational telemetry) → ops/observability tools

## Tools that should be connected for best output

- CLM (Ironclad, Spotdraft, ContractWorks, Concord) — primary source
- CRM with vendor records
- Document storage (Box, Drive, SharePoint, Egnyte) — for older agreements not yet in CLM
- Email — for vendor correspondence and informal commitments
- Procurement system (Coupa, Airbase, Ramp) — spend signal
- Security GRC (Vanta, Drata, Secureframe) — for SOC 2, pen-test, vendor-risk records
- Cyber-insurance policy on file — to confirm vendor warranty schedule

## Output formats (pick based on prompt)

- **Vendor snapshot** — full inventory + gap analysis + upcoming deadlines
- **Gap deep-dive** — one missing document analyzed with remediation steps
- **Renewal package** — what's needed for the renewal decision
- **Termination package** — surviving obligations checklist if relationship ends
- **Cross-vendor summary** — across all vendors, where are the highest-risk gaps (prioritized by data sensitivity × access scope × paperwork gap)
- **Customer-DPA flow-down audit** — verify each sub-processor meets your customer DPAs' security/notice requirements
