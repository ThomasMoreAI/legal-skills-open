---
name: review-contract-nmoralescyber
title: legal:review-contract — Contract Review Against Playbook
description: Review an executed-or-draft B2B contract (MSA, SOW, SaaS agreement, DPA, license, partnership, contractor IP assignment, reseller agreement) against the organization's negotiation playbook — flag clause-by-clause deviations, generate redlines with fallback positions, and prioritize must-haves vs. concessions. Use when the user pastes or attaches a counterparty's contract and asks to "review", "redline", "negotiate", "flag issues in", "find risks in", or "give negotiation strategy for" that contract. Do NOT use for standalone NDAs (use legal:triage-nda), for auditing the user's own customer-facing legal docs like ToS, privacy policies, refund policies, or HIPAA notices (use legal:legal-audit), for listing what agreements are already on file with a vendor (use legal:vendor-check), for asking whether a planned action or feature is compliant with a regulation (use legal:compliance-check), for severity-by-likelihood risk scoring without a contract document (use legal:legal-risk-assessment),
  or for sending an already-finalized contract for signature (use legal:signature-request).
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/review-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

# legal:review-contract — Contract Review Against Playbook

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review a counterparty's B2B contract against the organization's negotiation playbook. Analyze clauses, flag deviations, generate redlines with fallback positions, and provide business-impact analysis.

**Important**: This assists with legal workflow but is not legal advice. A qualified attorney must review before reliance.

## When to use this skill vs. an adjacent one

| If the user wants to… | Use this skill | Use instead |
|---|---|---|
| Redline a counterparty's MSA / SOW / SaaS agreement | legal:review-contract | — |
| Triage an inbound standalone NDA | — | legal:triage-nda |
| Audit the user's own customer-facing ToS / privacy policy / disclaimer | — | legal:legal-audit |
| List what agreements exist with a vendor | — | legal:vendor-check |
| Decide if a planned action / feature is regulator-compliant | — | legal:compliance-check |
| Score a risk by severity × likelihood (no document) | — | legal:legal-risk-assessment |
| Send a finalized contract for signature | — | legal:signature-request |

If the user's request straddles two skills (e.g., "review and send for signature"), run legal:review-contract first, then hand off.

## Invocation

```
legal:review-contract <contract file or URL>
```

Review the contract: @$1

## Workflow

### Step 1: Accept the contract

Accept PDF, DOCX, URL (CLM, Box, Egnyte, SharePoint), or pasted text. If none provided, prompt for one.

### Step 2: Gather context (one short turn)

Ask for:
1. **Side**: vendor/supplier, customer/buyer, licensor, licensee, partner
2. **Deadline**
3. **Focus areas** (e.g., "data protection critical", "IP ownership is the key issue")
4. **Deal context**: size, strategic importance, existing relationship, regulated data involved (PII, PHI, PCI), counterparty location

If partial context, proceed and note assumptions.

### Step 3: Load the playbook

Look for `legal.local.md` or similar in local settings.

The playbook should define standard positions, acceptable ranges, and escalation triggers.

**Playbook coverage tiers:**
- **Full playbook**: all major clause categories defined → cite the playbook position for every clause and flag any deviation.
- **Partial playbook**: some clauses defined → use playbook positions for covered clauses (cite explicitly), and use commercial-standard defaults for the rest (label as "DEFAULT" in the output so the user can see where the playbook is silent).
- **No playbook**: tell the user, then offer to (a) bootstrap one by walking through positions for the top 8 clauses, or (b) proceed entirely on commercial-standard defaults — labeled clearly throughout.

For every clause, the output must show one of: `[Playbook §X.Y]` (cite section), `[DEFAULT — market standard]`, or `[Playbook silent — using DEFAULT]`. Never silently substitute a default for a playbook position. Every redline must end with the citation that justifies it (see worked example in `references/REFERENCE.md`).

### Step 4: Clause-by-clause analysis

1. Identify contract type (SaaS, services, license, partnership, procurement, contractor).
2. Determine which side the user is on — this changes which protections matter.
3. Read the entire contract before flagging — clauses interact (e.g., uncapped indemnity may be partially mitigated by a broad LoL cap).
4. Analyze each material clause against the playbook.
5. Assess overall risk allocation.

**Material clause checklist** (extend if the contract type warrants):

| Clause | Key review points |
|---|---|
| Limitation of Liability | Cap amount, mutuality, carveouts, consequential-damages exclusion, **separate cyber-incident sub-cap** |
| Indemnification | Scope, mutuality, IP infringement, data breach, defense control |
| IP Ownership | Pre-existing IP, developed IP, work-for-hire, license grants, feedback clause, **contractor assignment language** |
| Data Protection | **DPA required when personal data processed** (GDPR Art. 28, PR Ley de Protección de Datos), sub-processor flow-down, breach notification (72hr GDPR), cross-border transfer (SCCs), **data residency commitments**, deletion/return |
| Security | **Right-to-audit / pen-test rights**, security standards (SOC 2, ISO 27001), incident-notification SLA |
| Healthcare | **BAA required if PHI involved** (HIPAA) |
| Payment-card | **PCI-DSS flow-down** if cardholder data involved |
| Confidentiality (embedded) | Scope, term, carveouts, return/destruction — note: a standalone NDA belongs to legal:triage-nda |
| Reps & Warranties | Scope, disclaimers, survival |
| Term & Termination | Initial term, renewal, termination for convenience/cause, wind-down |
| Governing Law & Dispute Res. | **PR vs. US state law toggle**, venue, arbitration vs. litigation, jury/class waivers |
| Insurance | Coverage minimums, **cyber-liability policy required**, evidence |
| Assignment | Consent, change of control |
| Force Majeure | Scope, notice, termination rights |
| Payment | Net terms, late fees, taxes, escalation |

For deeper per-clause guidance (acceptable ranges, common counterparty pushback, sample fallbacks) and a fully worked SaaS-MSA review showing playbook-citation format end-to-end, see `references/REFERENCE.md`. Mirror that worked example's structure (clause read → playbook citation → deviation → severity → redline with citation → two fallbacks) for every YELLOW/RED finding you produce.

### Step 5: Flag deviations (GREEN / YELLOW / RED)

- **GREEN — Acceptable**: Aligns with or beats the standard position. Note for awareness.
- **YELLOW — Negotiate**: Outside standard but within market range. Provide redline language, fallback position, and business impact of accepting as-is.
- **RED — Escalate**: Outside acceptable range, triggers an escalation criterion, or material risk. Provide why-it's-red, market-standard alternative, exposure estimate, and recommended escalation path (senior counsel / outside counsel / business decision-maker).

**Cybersec-specific RED triggers (always escalate when present):**
- Uncapped liability or general cap that swallows cyber incidents (no separate sub-cap)
- Personal data processed with no DPA offered
- PHI processed with no BAA offered
- Sub-processor blanket pre-authorization with no notification rights
- IP assignment that captures the user's pre-existing IP or open-source contributions
- Data residency that forces transfer out of contractually required region
- No right-to-audit / pen-test prohibition for a security-sensitive vendor

**Cyber-exposure quantification matrix (run for any contract touching personal data or production systems):**

Step A — Estimate floor incident cost:

| Data type | Per-record baseline (USD) | Source |
|---|---|---|
| General PII | $165 | IBM Cost of Data Breach 2024 |
| Healthcare / PHI | $408 | IBM 2024 (highest sector) |
| Financial | $295 | IBM 2024 |
| Customer-facing SaaS (avg) | $180 | IBM 2024 sector avg |

Floor incident cost = `records-at-risk × per-record baseline`. Add forensic ($150K–$500K typical), notification + credit-monitoring (~$5–15/record), legal defense ($250K–$2M), business interruption.

Step B — Layer regulatory penalty exposure by jurisdiction (parallel, not exclusive):

| Jurisdiction | Statutory cap / formula | Trigger |
|---|---|---|
| GDPR (EU) | Greater of €20M or 4% of global annual revenue | EU data subjects affected |
| CCPA/CPRA (CA) | $2,500/violation; $7,500/intentional; $750/consumer statutory damages | CA residents' data |
| HIPAA | $137 – $2.07M per violation/year (tiered, 2024 adjusted) | PHI involved |
| NY SHIELD | $5,000/violation, no cap | NY residents' data |
| PR Ley 111 | $500–$5,000 per violation + notification costs + AG action | PR residents' data |
| FTC Act §5 | No statutory cap; consent decree can reach $5B (Equifax precedent) | Unfair/deceptive practice |

Step C — Sub-cap erosion check:

Compute `single-incident exposure ÷ proposed cyber sub-cap`. If ratio > 0.5, the sub-cap is eroded by one incident with no headroom for a second. Flag RED and require: (a) sub-cap reset on annual basis OR (b) per-incident cap rather than aggregate OR (c) cyber-liability policy gap-filler.

Step D — Decision rule:

| Cap vs. exposure | Action |
|---|---|
| Cap ≥ exposure | GREEN — note for awareness |
| Cap = 0.5–1.0× exposure | YELLOW — request sub-cap raise OR insurance gap-filler |
| Cap < 0.5× exposure | RED — escalate; require (a) separate cyber sub-cap at exposure level, (b) cyber/data-breach carveout from general cap, OR (c) cyber-liability insurance with user named as additional insured covering the gap |
| No cap data possible (uncapped breach indemnity vendor-side) | GREEN for user; verify vendor solvency / insurance backing |

### Step 6: Generate redlines

For every YELLOW and RED:

```
**Clause**: [Section reference and name]
**Current language**: "[exact quote]"
**Proposed redline**: "[specific replacement language — show inserts in **bold** and deletions in ~~strikethrough~~]"
**Rationale**: [1–2 sentences, suitable for sharing with counterparty's counsel]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback 1**: [first compromise position]
**Fallback 2**: [walk-away or escalation trigger]
```

Be specific (ready to insert), balanced (firm on critical, reasonable elsewhere), prioritized, and include at least one fallback for every RED so the negotiator never has to improvise live.

**Reusable redline snippets (use as starting points, customize to the contract):**
- *Mutual liability cap*: "Each party's aggregate liability under this Agreement shall not exceed the greater of (a) the fees paid or payable in the twelve (12) months preceding the event giving rise to the claim or (b) US$[X]."
- *Cyber sub-cap carveout*: "Notwithstanding the foregoing, each party's liability for breach of its data-protection or information-security obligations shall be capped at the greater of US$[Y] or [N]× the General Cap."
- *DPA flow-down*: "The parties shall execute the Data Processing Addendum attached as Exhibit [X] prior to any Processing of Personal Data. Sub-processors require [30] days prior written notice and the right to object."
- *Right-to-audit*: "Customer (or its independent auditor under NDA) may, no more than once per twelve (12) months on [30] days notice, audit Vendor's compliance with security and data-protection obligations."
- *IP carveout*: "Each party retains all right, title, and interest in its Pre-Existing IP and any Independently Developed IP. No license is granted except as expressly set forth herein."

### Step 7: Business-impact summary

- Overall risk profile
- Top 3 issues
- Negotiation strategy: lead with Tier 1 must-haves, trade Tier 3 to win Tier 2, never concede Tier 1 without escalation
- Timeline considerations

**Tier 1 (deal-breakers)**: uncapped/insufficient liability, missing DPA/BAA for regulated data, IP provisions that jeopardize core assets, terms that conflict with regulatory obligations.
**Tier 2 (strong preferences)**: cap adjustments within range, indemnification scope/mutuality, termination flexibility, audit rights.
**Tier 3 (concession candidates)**: preferred governing law (if alternative acceptable), notice periods, minor definitional improvements, insurance certificates.

### Step 8: CLM routing (if connected)

If a CLM MCP is connected, recommend the approval workflow and routing path based on contract type and risk level. Otherwise skip.

## Output format

```
## Contract Review Summary
Document | Parties | Your Side | Deadline | Review Basis (Playbook / Generic)

## Key Findings
[Top 3–5 issues with severity flags]

## Clause-by-Clause Analysis
### [Clause] — [GREEN/YELLOW/RED]
Contract says | Playbook position | Deviation | Business impact | Redline (if YELLOW/RED)

## Negotiation Strategy
[Approach, priorities, concessions]

## Next Steps
[Specific actions]
```

## Notes

- Non-English contracts: ask whether the user wants translation or review in original.
- 50+ pages: offer to focus on the most material sections first, then complete review.
- Always remind the user to have qualified legal counsel review before relying on the analysis.
- If the document is actually a standalone NDA, stop and recommend legal:triage-nda. If it is the user's own customer-facing legal copy, recommend legal:legal-audit.
