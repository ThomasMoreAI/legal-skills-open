---
name: review-msa-deep-review-sboghossian
title: MSA Deep Review
description: Use when conducting a comprehensive review of a Master Services Agreement (MSA) or equivalent commercial services framework agreement. Covers all high-leverage clauses — liability cap, indemnification, IP ownership of deliverables, termination, SLA, data, audit rights, most-favored-customer, and term/renewal — with severity ratings and recommended positions. Takes approximately 30–60 minutes of focused review time. Links to specialist sub-review skills for deep-dives.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-msa-deep-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# MSA Deep Review

## When to use this

Use when you need a full commercial review of a Master Services Agreement or substantially similar services framework (Managed Services Agreement, Professional Services Agreement, Enterprise License Agreement with services components, IT Outsourcing Agreement). This is a comprehensive, high-effort review — plan for 30–60 minutes of focused work.

Typical triggers:
- High-value or strategic vendor engagement (multi-year, AED/USD 500K+)
- Enterprise SaaS with significant data processing obligations
- Outsourcing arrangement where the provider will have access to Client's systems or data
- Acquisition due diligence on a target company's material contracts
- Pre-signing review of counterparty's paper

For a quick NDA review, use [[review-nda-quick-check]]. For clause-level risk flagging as a first pass, use [[review-risk-flagging]].

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| MSA draft + all schedules | Full document including SOW template, DPA, SLA, pricing schedule | Required |
| Party perspective | Client vs Provider framing changes the priority of findings | Ask |
| Deal context | Contract value, term, data sensitivity, IP at stake | Helpful; infer from document |
| Jurisdiction | Governs enforceability of caps, non-competes, IP assignment | From governing-law clause |
| Prior negotiations | Any agreed positions — avoids re-opening closed items | Ask |

## Review Methodology

Run in two passes:

**Pass 1 — Structural completeness**: verify all standard MSA components are present (use [[review-missing-clauses]] checklist for MSA type).

**Pass 2 — High-leverage clause analysis**: deep-dive the ten clauses that determine who bears the real risk. For each, rate severity and recommend a position.

---

## High-Leverage Clause Analysis

### Clause 1 — Liability Cap

Rate: Is the cap reasonable for this deal?

Key questions:
- What is the cap structure? (12-month fees / 24-month / 2× annual / TCV / fixed amount)
- Does the cap apply to all damages including IP infringement? (red flag — IP should be carved out)
- Does the cap apply to data breach + regulatory fines? (red flag — regulatory fines are statutory)
- Are carve-outs consistent between this clause and the indemnification section?
- Is the cap enforceable in the governing jurisdiction? (civil-law courts can adjust; UK requires reasonableness test)

Escalate to [[review-liability-cap-reasonableness]] for full analysis.

Common patterns by contract type:

| Contract type | Typical Provider cap | Typical Client cap |
|---|---|---|
| SaaS (general) | 12-month fees | 12-month fees |
| SaaS (high data sensitivity) | 12-month fees + data breach uncapped | 12-month fees |
| IT Outsourcing | 12–24 months | TCV |
| Professional Services | 12-month fees | Fees paid for relevant services |
| Construction / FIDIC | Contract Price | Contract Price |

---

### Clause 2 — Indemnification

Key questions:
- Scope: third-party claims only? Or does it extend to direct losses between the parties?
- IP indemnification: does Provider indemnify Client for third-party IP infringement claims arising from use of the Provider's deliverables? (market standard: yes)
- Data breach: who bears indemnification for a breach of the DPA?
- Procedure: notice, defense control, settlement consent — all present?
- Cap alignment: are IP and data-breach indemnities carved out of the general cap?

Escalate to [[review-indemnification-balance]] for full analysis.

---

### Clause 3 — IP Ownership of Deliverables

Key questions:
- Are bespoke deliverables (custom software, reports, content) assigned to Client? Or retained by Provider?
- Is the assignment language present-tense ("hereby assigns") or executory ("agrees to assign")?
- Are background IP and pre-existing tools carved out?
- Is a license-back of background IP granted with an adequate scope and survival period?
- Are open-source components disclosed? Any copyleft contamination?
- What happens to IP on termination — does Client retain what it has paid for?

Escalate to [[review-ip-ownership-clarity]] for full analysis.

---

### Clause 4 — Termination

Key questions:
- Termination for convenience: available to which parties? Notice period? (market: 30–90 days for either party)
- Termination for material breach: is "material breach" defined? Cure period (typically 30 days)? Is right of cure limited to remediable breaches only?
- Acceleration of fees: on termination for convenience, does the terminating party owe remaining fees? (Provider-favorable; Client should resist for T4C by Client)
- Transition services: is Provider obligated to assist Client in transitioning to a new provider for some period post-termination? (critical for IT outsourcing and SaaS with Client data)
- Data return: on termination, within what timeframe does Provider return or delete Client data?

Red flags:
- No termination for convenience — parties locked in until term expires with no exit
- Material breach not defined — anything could be "material" or nothing could be
- No transition assistance obligation — Client left stranded on exit
- Fees continue to accrue during cure period after Client gives notice — double payment trap

---

### Clause 5 — Service Level Agreement (SLA)

Key questions:
- Are service levels specified? (Uptime %, response time, resolution time)
- How is measurement done? (Provider-reported? Third-party monitoring? Client audit right?)
- What are the remedies for SLA failure? (Service credits — rate and cap)
- Is the service credit the **exclusive** remedy for SLA failure? (common; flag if yes — prevents Client from claiming actual damages for outage)
- Are there exclusions from SLA measurement? (Scheduled maintenance, Client-caused failures — should be limited and transparent)
- Is there a persistent SLA failure termination right? (e.g., right to terminate if SLA failure exceeds X% in Y months)

Red flags:
- No SLAs at all — Provider's obligation is just "reasonable efforts"
- Service credits as exclusive remedy with a very low cap (e.g., 10% of monthly fees) — inadequate for high-availability requirements
- No persistent-failure termination right

---

### Clause 6 — Data Processing and Privacy

Key questions:
- Is a Data Processing Agreement (DPA) attached? (mandatory where personal data of EU/UK/KSA/UAE residents is processed)
- Data residency: where are Client's data stored? Does this comply with applicable cross-border transfer restrictions?
- Subprocessors: is there a list of approved subprocessors? Can Provider add subprocessors without Client consent?
- Breach notification: within what timeframe must Provider notify Client of a personal data breach? (Must be short enough for Client to meet its own 72-hour regulatory obligation)
- Data deletion/return: specific obligation on timing and format of data return or deletion on termination?
- Security standards: what technical and organizational security measures does Provider commit to? (ISO 27001, SOC 2, etc.)

Jurisdiction note: if any party or data subject is in KSA, UAE (onshore), DIFC, ADGM, EU, or UK — the DPA is not optional. Its absence is a compliance breach.

---

### Clause 7 — Audit Rights

Key questions:
- Does Client have the right to audit Provider's compliance with the agreement? (financial audit, security audit, data audit)
- Frequency: typically once per year with 30 days' notice
- Cost: Client usually bears audit cost; Provider bears cost of remediation
- Scope: is it limited to the relevant Services / data? (avoid granting unlimited access to Provider's systems)
- Confidentiality of findings: audit results should be treated as confidential
- Inspector qualifications: independent third-party auditor (not Client's general staff)

Red flags:
- No audit right at all for a data-processing engagement
- Audit right is purely a right to "ask questions" with no right to access records
- Provider can refuse audit on confidentiality grounds with no arbitral override

---

### Clause 8 — Most-Favored-Customer (MFC)

Key questions:
- Does the MFC apply to pricing only? Or to all contractual terms?
- If pricing MFC: retroactive (Provider must refund the delta if it gives a better price to anyone)? Or prospective only?
- Scope: compared to all customers? Or a defined group (similarly-situated customers, same volume tier)?
- Duration: does it survive term expansion or renewal?

MFC is a significant obligation on the Provider — verify that the Client actually needs it given the deal dynamics. If included, mark retroactive MFC as a high-risk item for Provider side.

---

### Clause 9 — Term and Renewal

Key questions:
- Initial term and auto-renewal mechanics?
- Notice period for non-renewal: if notice for non-renewal must be given 90+ days before auto-renewal, the auto-renewal trap is a material risk (common in SaaS contracts)
- Term-end pricing protections: if the contract renews at a higher price without negotiation, Client may be locked into unfavorable pricing
- Most favored pricing at renewal: ensure renewal pricing is at least equivalent to current market

Red flags:
- Auto-renewal notice window greater than 60 days (creates trap for clients who don't track deadlines)
- Renewal at "then-current list prices" — may be materially higher than original pricing

---

### Clause 10 — Change Control

Key questions:
- Is there a change control process (Change Order / Statement of Work amendment)?
- Who has authority to approve changes?
- Does verbal approval bind either party to additional fees?
- Is there a mechanism to resolve disputes about whether work falls within existing scope?

Red flags:
- No change control process — Provider can claim any additional work was "in scope" or Client can refuse to pay for extra work
- Changes bind Client upon written acceptance — but acceptance is defined too broadly (e.g., commencing to use new feature)

## Output Format

Produce a top-10 findings list:

| Rank | Clause | Issue | Severity | Recommended Position | Fallback |
|---|---|---|---|---|---|
| 1 | Liability Cap | Cap applies to IP indemnity — no carve-out | Critical | IP indemnity uncapped | Separate sublimit at 2× annual fees |
| 2 | Data Processing | No DPA attached; GDPR/PDPL compliance gap | Critical | Attach standard DPA with SDAIA clauses | Require DPA execution before go-live |
| ... | ... | ... | ... | ... | ... |

Severity: Critical = potential regulatory violation or unlimited liability; High = material commercial exposure; Medium = suboptimal but manageable; Low = best-practice gap.

## Jurisdictional Notes

**DIFC / ADGM**: Common-law jurisdiction; English-style drafting conventions apply; DIFC and ADGM both have their own Data Protection Laws that require a DPA where personal data is processed.

**KSA**: Arbitration clauses must be explicit — specify SCCA/ICC, seat, language, number of arbitrators. IP assignments require specific present-tense language. PDPL DPA requirements apply where Saudi personal data is processed.

**UAE (onshore)**: Federal Data Protection Law (applicable alongside emirate-level rules); penalty clauses are adjustable by courts; IP assignment by future works requires care.

**Lebanon**: USD denomination for long-term contracts given currency instability; force majeure provisions should address banking and regulatory restrictions.

## Related Skills

- [[review-indemnification-balance]]
- [[review-liability-cap-reasonableness]]
- [[review-ip-ownership-clarity]]
- [[review-risk-flagging]]
- [[review-missing-clauses]]
- [[draft-msa]]
- [[review-nda-quick-check]]
