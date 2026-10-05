# DPO Engagement Playbook

Reference for engaging the Data Protection Officer during GDPR audit prep. Covers DPO role boundaries, audit-response coordination, supervisory authority dialogue, internal escalations, and DPO independence concerns.

---

## DPO role in GDPR audit context

The DPO (when appointed) is independent and reports to highest management level (Article 38.3). During audit, the DPO:

- **Coordinates** response to supervisory authority inquiries
- **Leads** walkthroughs with auditors (or customer reviewers)
- **Advises** on policy gaps and remediations
- **Communicates** with the supervisory authority
- **Monitors** compliance throughout the audit period
- **Documents** the audit response (Article 39 documentation requirement)

The DPO is NOT:
- Personally liable for compliance failures (Article 39 contains no personal liability)
- A signatory on data processing agreements
- The data controller's decision-maker on processing (advisory role)

---

## DPO availability and capacity

### When DPO is required (Article 37)

- Public authority / body
- Core activities consist of regular and systematic monitoring of data subjects at large scale
- Core activities consist of large-scale processing of special-category data (Article 9) or criminal data

### DPO models

| Model | Pros | Cons |
|-------|------|------|
| Internal DPO (employee) | Knows business; immediately available | Independence concerns; risk of conflict of interest |
| External DPO (consultant / law firm) | Independent; specialized; multiple-client expertise | Less embedded; slower response; cost |
| Group DPO (across subsidiaries) | Centralized expertise; consistency | Geographic / language gaps |
| Shared DPO (across small entities) | Cost-effective for small orgs | Limited time per entity |

### DPO independence (Article 38.6)

DPO must not perform tasks that conflict with DPO role. Common conflicts:
- DPO is also Chief Information Officer (CIO) — DPO advises on processing they're responsible for
- DPO is also Head of HR — processes employee data
- DPO is also Head of Marketing — processes customer data

Avoid by appointing DPO who doesn't own a major processing function.

---

## Audit response coordination

### Step 1: Initial assessment (within 24-48 hours of inquiry/notification)

DPO leads:
- Read the inquiry / notification carefully
- Identify scope (processing activities, time period, specific concerns)
- Identify relevant teams (engineering, security, legal, HR if employee data)
- Determine response timeline (statutory deadlines)
- Brief leadership

Output:
- Scope summary
- Stakeholder team identified
- Initial response timeline
- Decision: external counsel needed? (yes for formal supervisory authority investigations)

### Step 2: Information gathering (week 1-2)

DPO coordinates:
- Pull relevant ROPA entries
- Pull policies + procedures referenced
- Pull past-period evidence (incidents, DSRs, DPIAs)
- Pull vendor / sub-processor information if relevant
- Brief stakeholders + assign data-pulls

Output:
- Comprehensive evidence packet
- Gap list (what we don't have)
- Plan to close gaps before response

### Step 3: Gap closure (week 2-4)

DPO oversees:
- Policy updates (drafts → legal review → approval)
- Technical fixes (e.g., access controls updated)
- Process changes (e.g., DSR process formalized)
- Subject communications (if affected)
- Internal accountability records

### Step 4: Response drafting (week 4-6, depending on complexity)

DPO + legal:
- Draft formal response to supervisory authority
- Internal review (DPO + legal + leadership)
- External counsel review (if engaged)
- Response submitted

### Step 5: Ongoing dialogue (week 6+)

- Supervisory authority may have follow-up questions
- DPO maintains dialogue
- Internal communication of any required remediations
- Closure (or escalation)

---

## Communicating with the supervisory authority

### Tone and content

- **Factual and concise** — not defensive
- **Acknowledge gaps where they exist** — credibility
- **Provide remediation plan with timeline** — show good faith
- **Don't argue legal interpretation** unless really needed; pick battles

### Communication record

Every communication with supervisory authority logged:
- Date
- Method (letter, email, call, meeting)
- Participants
- Summary
- Action items + follow-ups

### Common supervisory authority requests

| Request | Standard response |
|---------|-------------------|
| Full ROPA | Provide; pre-redact sensitive sub-processor info if appropriate |
| Policies and procedures | Provide; latest approved versions |
| DPIA for [activity] | Provide; if missing, acknowledge and provide commitment to remediate |
| Past 12-month breach register | Provide; with notification details where required |
| Past 12-month DSR records | Provide; anonymize subject identifiers |
| Sub-processor list with locations | Provide; with transfer mechanism documentation |
| TIA (Transfer Impact Assessment) | Provide; for US transfers, demonstrate Schrems II analysis |
| Past-period training records | Provide; per employee or aggregate |

### Common supervisory authority traps

- **Late response** — extensions are sometimes available; ask early if needed
- **Inconsistent information** — keep responses internally consistent; reconcile before sending
- **Over-disclosure** — provide what's asked, not more; legal review on scope
- **Acknowledging fault prematurely** — let legal + DPO assess before admissions

---

## Customer-side DPA audits

Customers (especially enterprise) sometimes audit processors per DPA Article 28 audit rights.

### Standard handling

- **Acknowledge audit request** within DPA-specified period
- **Confirm scope** (your processing of their data only, not your full operation)
- **Use neutral 3rd-party auditor** if customer agrees
- **Confidentiality**: auditor signs NDA; customer doesn't get other customers' data
- **In-place evidence**: SOC 2 / ISO 27001 reports often satisfy customer; provide first
- **On-site only if necessary**: most audits can be remote with documentation

### DPO role

- Coordinate with customer's audit team
- Provide evidence per request
- Lead walkthroughs
- Sign audit-completion documentation

---

## Internal escalations during audit prep

### When to escalate to leadership

- Supervisory authority indicates fine likely → CEO + Board + General Counsel
- Audit reveals systemic failure → CEO + relevant exec
- Audit response requires substantial budget → CFO
- Audit reveals criminal exposure → outside counsel + CEO immediately

### Escalation channel

DPO → CIO/CISO → CEO → Board (if material)
Parallel: GC + CFO informed throughout

### Documentation

Every escalation:
- Date
- Audience
- Issue summary
- Decision required
- Decision made + by whom

---

## DPO documentation requirements (Article 39)

DPO must document:
- Audit responses + findings
- Advice given to controller / processor
- Consultations with supervisory authority
- Training conducted
- Monitoring activities

Maintain in central location accessible to supervisory authority on request.

---

## DPO post-audit

### Immediate (within 1 week)

- Final response submitted to supervisory authority
- Internal post-audit review with executive sponsor
- Remediation plan documented + assigned

### 30-day follow-up

- All remediation items progressing
- Supervisory authority dialogue continued (if open)
- Internal communication on lessons learned

### 90-day follow-up

- All immediate remediations complete
- Process improvements implemented
- Update relevant policies + procedures
- Brief board if applicable

### Annual

- Audit response added to DPO documentation
- Lessons incorporated into training
- Annual GDPR readiness review

---

## When external counsel is essential

- Formal supervisory authority investigation (not just inquiry)
- Potential class-action or representative action
- Cross-border investigation (lead supervisory authority + concerned)
- Criminal investigation
- Customer dispute escalating to legal

---

## Common DPO failures during audit

| Failure | Mitigation |
|---------|------------|
| DPO not available (vacation, illness) | Have backup DPO or external DPO on call |
| DPO not independent (conflict of interest) | Restructure DPO role; consider external DPO |
| DPO advice ignored by leadership | Document the advice (Article 39); escalate non-compliance to supervisory authority if egregious |
| DPO not consulted on high-risk processing | Add DPO consultation to project gate criteria |
| DPO doesn't understand the technical reality | Pair with engineering / security; technical training |
| DPO over-promises supervisory authority | Stick to factual + realistic timelines |

---

## Cheat sheet

| Question | Answer |
|----------|--------|
| First call when audit notice arrives? | DPO. If no DPO, external privacy counsel. |
| When is external counsel needed? | Formal investigation, potential fine, criminal exposure, cross-border |
| DPO independence — how to maintain? | Don't combine with role that owns processing |
| Can DPO sign DPAs? | No; DPO is advisory, not signatory |
| Can supervisory authority audit on-site? | Yes (Article 58); usually announced; can be unannounced |
| How quickly to respond to a breach notification (subject side)? | Per Article 34: without undue delay if high risk to subjects |
| How quickly to notify supervisory authority? | Per Article 33: within 72 hours of awareness |
| What about US transfers post-Schrems II? | SCCs + TIA + supplementary measures (encryption / contractual / organizational) |
