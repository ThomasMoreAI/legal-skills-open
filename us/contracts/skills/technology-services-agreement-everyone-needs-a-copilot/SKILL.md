---
name: technology-services-agreement-everyone-needs-a-copilot
title: Technology Services Agreement Skill
description: Technology professional services agreement review and negotiation. Use for SOW integration, acceptance testing, change orders, IP ownership, SLAs, data handling, security, warranties, and support obligations.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/technology-services-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Technology Services Agreement Skill

Technology professional services agreements have all the risks of a standard services agreement plus technology-specific risks: software deliverables that may not perform as expected, SLA obligations that create ongoing financial exposure, and data handling requirements that create privacy and security liability.

---

## Technology-Specific Risk Dimensions

In addition to standard services agreement review, technology engagements add:

1. **Performance standards**: Does the software/system work? Who decides?
2. **SLAs**: Ongoing availability and response time obligations with financial consequences
3. **Data handling**: What client data does ENAC's work touch, and who is liable for breaches?
4. **Technology IP**: Software code, algorithms, AI models, and configurations have specific ownership considerations
5. **Support and maintenance**: What ongoing obligations does ENAC have after delivery?

---

## Statement of Work Integration

The SOW is the operative document for a technology services engagement. The agreement sets the legal framework; the SOW defines what is actually being built or configured.

**SOW must include:**
- Specific system or software being developed, configured, or integrated
- Technology stack and third-party dependencies
- Functional requirements (what it must do)
- Non-functional requirements (performance, security, accessibility standards)
- Acceptance criteria and testing protocol
- Milestones and payment triggers
- Assumptions and dependencies (what the client must provide)
- Out-of-scope items explicitly listed

**Flag any SOW that says:** "and such other technical services as may be needed": this is unlimited scope in a technology context, where "needed" can be defined by the client's evolving expectations.

---

## Acceptance Testing

Technology deliverables require a defined acceptance process tied to objective criteria.

**Standard acceptance process:**
1. ENAC delivers the system/module to a test environment
2. Client has [15-30] business days to conduct acceptance testing
3. Client documents specific deficiencies with steps to reproduce
4. ENAC has [15] business days to correct confirmed deficiencies
5. Re-testing on corrected items
6. Deemed acceptance if no written notice within the testing period

**Acceptance criteria must be:**
- Objective (not "client is satisfied")
- Specific (reference the functional requirements)
- Measurable (pass/fail tests, not subjective quality assessments)

**Key risk:** Acceptance criteria that require the system to "meet all requirements" without defining requirements creates unlimited revision obligations.

---

## Change Order Process

Technology projects are especially vulnerable to scope creep because requirements always evolve. The change order process is not bureaucracy: it is the mechanism by which ENAC gets paid for additional work.

**Required change order clause:**
> "Any modification to the scope, requirements, schedule, or technology specified in the Statement of Work requires a written Change Order executed by both parties before work begins. ENAC will provide a Change Order proposal within [5] business days of receiving a written change request. Work on changes shall not commence until the Change Order is executed. Changes shall be billed at ENAC's then-current rates, or as negotiated in the Change Order."

**Verbal change order risk:** "The client told me to add this feature" is not a change order. Document everything in writing.

---

## Intellectual Property: Technology Context

Technology engagements create additional IP categories beyond the standard Background/Foreground/Derivative framework:

**Background IP (ENAC's pre-existing):**
- AI agent definitions and prompts
- Pipeline Copilot workflow and architecture
- Figma plugin code and bridge server
- Document generation logic and templates
- Methodology frameworks embedded in tools

**Foreground IP (created for the client):**
- Custom integrations, scripts, or workflows built specifically for the client
- Client-specific data models or schemas
- Reports and deliverables created under the engagement

**Third-party IP (licensed, not owned):**
- Open-source libraries
- Commercial APIs (Anthropic, Figma, etc.)
- Cloud service components

**AI system configurations:**
AI prompts and agent configurations are Background IP. The client does not own the prompts ENAC used to produce their deliverables. Ensure the IP clause explicitly excludes "AI systems, prompts, and agent configurations" from the definition of deliverables unless specifically agreed.

---

## Service Level Agreements (SLAs)

For engagements with ongoing support, hosting, or operational obligations:

**Key SLA dimensions:**
- Uptime / availability (e.g., 99.5% during business hours)
- Response time to support requests (by severity level)
- Resolution time for defects (by severity level)
- Maintenance windows (scheduled downtime excluded from SLA calculation)

**SLA financial consequences:**
- Service credits (typically % of monthly fees): acceptable if capped
- Termination rights for sustained SLA failure: acceptable with cure period
- Financial penalties beyond service credits: RED; reject

**ENAC's position:** Agree to SLAs with service credit remedies, capped at the monthly fee for that service component. No financial penalties beyond service credits. SLA failure for cause (client-side dependencies missing) does not count against ENAC.

---

## Data Handling

For technology engagements:

**Data at rest:** How is client data stored? Encryption standard? Access controls?

**Data in transit:** How is data transmitted between systems? TLS/HTTPS minimum.

**Data in AI systems:** If ENAC uses AI tools to process client data:
- Verify AI vendor terms permit government client data (see `@legal-ai-gov`)
- Ensure data is not used for model training
- Document which AI tools were used and for what purpose

**Data retention and deletion:**
- Define retention period in the contract
- Confirm ENAC's deletion obligations at engagement end
- Address backup copies: when are they deleted?

**Breach notification:**
- What are ENAC's notification obligations if a breach occurs?
- Timeline: Colorado C.R.S. 6-1-716 requires notification without unreasonable delay
- Who does ENAC notify first: the client or the affected individuals?

---

## Limitation of Liability: Technology Context

Technology agreements need clear liability provisions because system failures can have outsized downstream consequences.

**Standard position:**
- Cap at total fees paid in the preceding 12 months
- Mutual consequential damages waiver
- Carve-outs: indemnification, confidentiality, data breaches (consider whether breach liability should be separately capped)

**Technology-specific risk:** SLA failures that cause the client to lose revenue, suffer reputational harm, or face government penalties are consequential damages. Without a consequential damages waiver, ENAC's liability is not limited to the fees paid.

**Data breach liability:** Consider whether data breach liability should be separately addressed:
- Capped at a defined amount (e.g., fees paid)
- Subject to mitigation obligations
- Not subject to an uncapped indemnification for breach notification costs

---

## Indemnification: Technology Context

**ENAC indemnifies client for:**
- Third-party IP infringement claims arising from ENAC's deliverables (not from Background IP used with permission)
- ENAC's negligence in handling client data
- ENAC's breach of its data handling obligations

**ENAC does NOT indemnify client for:**
- Client's use of deliverables outside the scope of the license
- Third-party IP infringement arising from the client's modifications to deliverables
- Open-source license violations in components the client adds
- Breaches caused by the client's failure to maintain its own systems

---

## Termination and Wind-Down

**Technology-specific termination obligations:**
- Data return: what format, within how many days?
- Transition assistance: how long must ENAC cooperate with a successor vendor?
- System access: when does ENAC's access to client systems terminate?
- SLA obligations: do they continue during transition period?
- Source code delivery: if ENAC built custom software, is source code delivered at termination?

**Transition assistance clause:**
> "Upon termination, ENAC shall provide up to [30] days of reasonable transition assistance at its then-current hourly rates. Transition assistance includes knowledge transfer, documentation of system architecture, and cooperation with a successor service provider."

---

## Output Structure

1. **SOW integration assessment**: Is scope defined adequately? What is vague?
2. **Acceptance testing analysis**: Criteria objective and specific? Process defined?
3. **Change order mechanism**: Present and enforceable?
4. **IP ownership analysis**: Background IP carve-out, AI system configurations protected?
5. **SLA review**: Obligations achievable? Financial consequences capped?
6. **Data handling assessment**: Retention, deletion, breach notification, AI vendor terms
7. **Liability analysis**: Cap in place, consequential damages waived, breach liability addressed?
8. **Termination and transition**: Wind-down obligations clear?

---

## Anti-Generic Rules

- NEVER accept "all technical work product" as an IP assignment without carving out Background IP and AI configurations
- NEVER accept SLA financial penalties beyond service credits
- NEVER leave acceptance criteria as "client satisfaction": it must be objective
- NEVER omit the change order clause: scope creep in technology engagements is the primary profitability risk
- NEVER use AI tools with government client data without confirming vendor terms permit it
