---
name: compliance-check-nmoralescyber
title: Compliance Check (Pre-Launch)
description: 'Pre-launch regulatory go/no-go on a PROPOSED action, product feature, marketing campaign, partnership, sub-processor addition, AI capability, geographic expansion, or pricing/auto-renewal change — BEFORE it ships. Surfaces applicable regulations across jurisdictions (GDPR, CCPA/CPRA, state privacy laws, HIPAA, COPPA, PCI-DSS, CAN-SPAM, TCPA, FTC, EU AI Act, Puerto Rico Ley Núm. 111-2005 / DACO consumer rules, sector laws), required internal approvals (legal, DPO, security, exec), required external notifications (customer DPA notice, 30-day sub-processor notice, regulator filings, insurance), required pre-launch artifacts (DPIA, updated privacy policy, consent flow, SCCs), and risk areas. Outputs a clear GO / NO-GO / GO-WITH-CONDITIONS decision with specific verifiable conditions and a re-check trigger. Use whenever the user says "is this compliant", "can we launch X", "what regulations apply to [feature/campaign/partnership/sub-processor/AI capability]", "do we need approval
  before [action]", "pre-launch legal/regulatory check", "go/no-go on [proposed initiative]", "are we OK to ship [thing] in [jurisdiction]", or describes wanting a forward-looking compliance view on a not-yet-shipped initiative. Do NOT use for: auditing already-published customer-facing legal pages on a live site (use legal:legal-audit), reviewing a contract document like MSA/NDA/DPA (use legal:review-contract), tracking ongoing compliance program operations like SOC 2 evidence collection or audit calendar (use operations:compliance-tracking), SOX 404 internal financial-control testing (use finance:sox-testing or finance:audit-support), responding to an inbound legal inquiry like a DSAR or subpoena (use legal:legal-response), drafting an actual outbound breach notification AFTER an incident (escalate to counsel + use legal:legal-response template path; this skill is PRE-LAUNCH design check, not post-incident response). Defining characteristic: PRE-launch + proposed thing + forward-looking
  go/no-go'
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/compliance-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Compliance Check (Pre-Launch)

Pre-launch regulatory go/no-go check on a proposed initiative.

## When to use vs. adjacent compliance/legal skills

| Skill | Time orientation | Object | Use when |
|---|---|---|---|
| **legal:compliance-check (this one)** | Future (pre-launch) | A proposed initiative | "Can we ship X?" |
| `legal:legal-audit` | Past/present (live) | Customer-facing legal pages already on the site | "Audit our live privacy policy" |
| `legal:review-contract` | Present | A contract document (MSA, NDA, DPA, SOW) | "Review this vendor MSA" |
| `operations:compliance-tracking` | Ongoing | Multi-month program (SOC 2, ISO, GDPR) | "Where are we on SOC 2 evidence" |
| `finance:sox-testing` / `finance:audit-support` | Ongoing | SOX 404 internal financial controls | "Pull a sample for revenue control testing" |
| `legal:legal-response` | Reactive | An inbound inquiry (DSAR, subpoena, NDA request) | "Reply to this DSAR" |

**Defining characteristic of this skill: PRE-launch + proposed thing + forward-looking go/no-go.**

## Common invocations

- "Can we launch the new AI risk-scoring feature next month?"
- "Pre-launch check on a free-trial auto-convert flow for PR + 50 states"
- "Is it OK to add Anthropic as a sub-processor next week?"
- "We want to expand to EU customers in Q3 — go/no-go from a compliance angle?"
- "Marketing wants to run a 99% accuracy claim on the landing page — safe?"
- "Partnering with a health-data startup — what regulatory issues should we know?"

## What gets checked

### 1. Applicable regulations (by jurisdiction)
- **Privacy:** GDPR (EU/UK), CCPA/CPRA (CA), CO/VA/CT/UT/TX/OR state privacy laws, HIPAA, COPPA, PIPEDA, LGPD, DPDP (India), PDPA (Singapore), CSL (China)
- **Puerto Rico–specific:** Ley Núm. 111-2005 (citizen identity-data breach notification), DACO consumer protection rules, PR Department of State filing requirements (if entity-level), bilingual disclosure expectations
- **Marketing:** CAN-SPAM, TCPA (SMS/calls), FTC endorsement guides + substantiation, state-level deceptive practice laws, state auto-renewal disclosure laws (CA, NY, OR, etc.)
- **AI/algorithmic:** EU AI Act risk classification (prohibited/high-risk/limited-risk/minimal), CO AI Act (effective Feb 2026), NYC Local Law 144 (employment ADM), state-level deepfake/biometric laws
- **Industry-specific:** HIPAA (health), GLBA (finance), FERPA (education), FedRAMP (federal customers), PCI-DSS (card data), SEC marketing rule (financial advice), FDA SaMD (medical software)
- **Cybersec-specific:** SEC cyber disclosure rule (4-day material incident), state breach notification laws, NYDFS Part 500 (NY financial counterparties)

### 2. Internal approvals required
- Legal review
- Privacy / DPO sign-off
- Security review (threat-model + data-flow)
- Finance (if revenue or pricing impact)
- Brand / marketing (if external comms)
- Executive (if material risk, strategic shift, or PR-sensitive)

### 3. External approvals / notifications required
- Regulatory filings (DPA notification of high-risk processing where required, FTC/state AG)
- Customer notice (DPA-required terms updates, material privacy policy change)
- **Sub-processor notice — typically 30-day per DPA** (verify your DPA's exact term)
- Auditor notification (if mid-cycle and material)
- Cyber insurance disclosure (material new exposure)
- Cross-border transfer mechanism updated (SCCs, UK IDTA, adequacy)

### 4. Required pre-launch artifacts
- DPIA / TIA (Data Protection / Transfer Impact Assessment) if high-risk personal data
- Vendor DPAs in place if data shared with new processor
- Updated privacy policy / disclosures
- Updated cookie banner + consent flows
- Data retention schedule updated
- Incident response runbook updated for new data type/system
- AI Act conformity assessment (if high-risk AI)

## Output structure

1. **Initiative summary** — what is being proposed, in 2-3 sentences
2. **Jurisdictional scope** — where will this operate, where will users be (PR? US states? EU? UK?)
3. **Applicable regulations table** — regulation | requirement | applies (Y/N) | why
4. **Required approvals table** — approver | what they need to see | target date
5. **Required artifacts checklist** — done / in progress / missing
6. **Risk areas** — specific clauses, claims, or assumptions needing attention
7. **DECISION** — single-line `GO` / `NO-GO` / `GO-WITH-CONDITIONS` at the top of the report
8. **Conditions** (if conditional) — each condition must be verifiable and assigned: `[Owner] must [action] by [date], evidenced by [artifact]`
9. **Re-check trigger** — what change would invalidate the decision (e.g., "if we add EU users, re-run with GDPR scope")

## Common pre-launch gotchas (cybersec/PR-founder context)

- Launching a feature that processes personal data **without updating the privacy policy first**
- Marketing claims that exceed FTC substantiation ("99% of customers...", "military-grade encryption")
- AI/algorithmic features without **EU AI Act** risk classification
- New data collection without **consent capture** flow update
- Cross-border data transfer without **SCCs / UK IDTA / adequacy**
- New sub-processor without **30-day customer notification** per DPA
- Children-adjacent feature without **COPPA verifiable parental consent**
- Health-adjacent feature triggering **HIPAA covered-entity / business-associate** status
- Free trial auto-converting without **state-by-state auto-renewal disclosure** (CA Bus & Prof §17602, NY GBL §527-a, etc.)
- **PR consumer rollout** missing bilingual (Spanish) disclosures or DACO-required terms
- **PR-resident PII processing** without aligning to PR Ley 111-2005 breach-notification timing
- SaaS launching into NY-DFS-regulated counterparties without Part 500 attestation prep
- Cybersec product making detection-rate claims without **substantiation file**
- Partnership data-sharing without **joint-controller analysis** under GDPR Art. 26

## Output format

Markdown report with the structure above. Top line is **GO / NO-GO / GO-WITH-CONDITIONS**, followed by conditions list (each verifiable, owned, dated). Defer recommendation always cites the appropriate sister skill if the user's actual ask is misclassified.
