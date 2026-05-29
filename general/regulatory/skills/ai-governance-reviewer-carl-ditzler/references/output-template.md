# Output Template

Read this file before drafting the governance review output.

Also review [example-outputs.md](example-outputs.md) when you need a concrete response pattern.

## Review Status Rule

- Use `Final Review` only when role, use case, data type, deployment model, oversight, and testing state are known.
- Do not label the output `Preliminary Review` merely because facts are missing.
- Missing facts trigger questions first, not a review.
- Only after the model has asked the missing intake questions and requested missing evidence may it label the output `Preliminary Review`.
- In a preliminary review, use `Unknown` entries instead of guessing and state that the review is incomplete.
- If material evidence is missing, ask the user for that evidence before generating a review. Only draft the review without it when the user cannot provide it, refuses to provide it, or explicitly asks you to proceed anyway, in which case keep the review preliminary.

## First-Response Rule

When the user has not yet provided enough facts or evidence to support a review:
- The response must be an intake and evidence-request message first.
- Do not generate the `Draft AI Governance Review` section yet.
- Do not generate scorecards, findings, remediation, or recommendations yet.
- Ask only the first topic block as direct questions.
- Do not mention `Preliminary Review` as the default next step in that first response.
- Never ask the user to complete a form, markdown table, or governance evidence table inside the assistant response.
- Ask each missing document or status item as a separate direct question.
- Do not preface the questions with a summary of web search results, vendor materials, or your current understanding.
- Do not include later topic blocks in the first response unless the user already supplied the earlier answers.
- Do not front-load governance document-status questions in the first response unless the user explicitly asked about document readiness.

Preferred intake format:
- short heading
- direct questions
- one topic block at a time by default
- plain-text questions instead of tables or fill-in forms

Recommended sequence:
1. `Core Use Case`
2. `Data and Deployment`
3. `Oversight and Testing`
4. `Governance Documents and Status`
5. `Vendor and Contracting`

## Intake-First Rule

Before generating any report, findings, governance review, or scorecard:
- Ask clarifying questions when the AI use case, role, data, deployment, oversight, or testing facts are unclear.
- Ask for missing evidence when the analysis depends on documents, technical details, approvals, test results, or vendor materials that have not been provided.
- Do not jump directly to the report if the missing facts or evidence can still be collected from the user.
- Use the `Preliminary Review` route only after this intake-first process has been attempted.
- Prefer sequential topic blocks over one long catch-all questionnaire.
- Do not suppress necessary follow-up questions because of an internal question-count preference.
- In each intake turn, usually ask only 2 to 4 direct questions.

Use intake questions covering, where relevant:
- AI use case and intended users
- Organization role
- Model or vendor
- Data types and data sources
- Deployment model
- AI impact assessment
- Technical documentation
- DPA and subprocessor list
- Audit rights or audit materials
- User disclosures and whether users will know AI is being used
- Testing, red-team, and validation evidence
- Incident response process
- Post-launch monitoring plan
- AI acceptable use policy
- Approvals, owners, and escalation paths

## Evidence Sufficiency Rules

Use these as minimum evidence thresholds before treating a review as robustly supported.

### Internal AI Use

Prefer to have:
- use-case description,
- data description,
- deployment description,
- owner and oversight details,
- acceptable-use or training expectations,
- testing and monitoring summary.

### Product AI Integration

Prefer to have:
- product or feature description,
- intended users and user reliance context,
- user disclosure or UX materials,
- architecture or technical overview,
- testing and red-team summary,
- incident response and monitoring plan,
- accountable owner and approvals.

### Third-Party AI Vendor

Prefer to have:
- vendor documentation or model documentation,
- DPA or equivalent contractual language,
- subprocessor list,
- retention and training-right terms,
- audit rights or control materials,
- incident and change-notification terms,
- accountable internal owners.

If several of these are missing, confidence should stay low or medium and the review should remain preliminary unless the user explicitly asks to proceed despite the gaps.

## Confidence Discipline

- `High` confidence requires strong evidence, mature testing, and clear ownership.
- `Medium` confidence is appropriate when some evidence exists but gaps remain.
- `Low` confidence is required when critical facts, documents, or test evidence are missing.

Do not overstate confidence because the narrative sounds plausible. Confidence follows evidence.

## Response Structure

### 1. Draft AI Governance Review

Use this exact title for the report:
`Draft AI Governance Review`

### 2. Requested AI Use Case Summary

Lay out the summary cleanly using labeled fields rather than one dense paragraph.

Recommended format:
- `Use Case`
- `Scenario`
- `Organization Role`
- `Intended Users`
- `Model / Vendor`
- `Data Types Involved`
- `Deployment Model`
- `Human Oversight`
- `Testing and Monitoring`
- `Documents / Evidence Reviewed`

If a field is not yet known, mark it `Unknown`.

### 3. Review Status

State either:
- `Preliminary Review`
- `Final Review`

If preliminary, list the blocking unknowns.

### 4. Governance Scorecard

Use these two tables.

**Table A**

| Category | Key Question | Status | Inherent Risk | Residual Risk | Evidence Provided |
|---|---|---|---|---|---|
| Feature Classification | What type of AI is this? | [status] | [inherent risk] | [residual risk] | [evidence] |
| EU AI Act Risk Tier | What risk tier applies? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Prohibited Use Screening | Are any prohibited uses implicated? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Transparency Obligations | What disclosures are required? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Training Data and IP | Are data rights and IP risks addressed? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Human Oversight | Is meaningful oversight in place? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Testing Evidence | Has adequate testing been conducted? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Incident Monitoring | Is incident response and monitoring in place? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Governance Approvals | Have required approvals been obtained? | [status] | [inherent risk] | [residual risk] | [evidence] |
| Beyond AI-Specific Law | What non-AI legal domains apply? | [status] | [inherent risk] | [residual risk] | [evidence] |

**Table B**

| Category | Key Question | Missing Evidence | Findings | Confidence | Required Owner |
|---|---|---|---|---|---|
| Feature Classification | What type of AI is this? | [missing evidence] | [findings] | [confidence] | [owner] |
| EU AI Act Risk Tier | What risk tier applies? | [missing evidence] | [findings] | [confidence] | [owner] |
| Prohibited Use Screening | Are any prohibited uses implicated? | [missing evidence] | [findings] | [confidence] | [owner] |
| Transparency Obligations | What disclosures are required? | [missing evidence] | [findings] | [confidence] | [owner] |
| Training Data and IP | Are data rights and IP risks addressed? | [missing evidence] | [findings] | [confidence] | [owner] |
| Human Oversight | Is meaningful oversight in place? | [missing evidence] | [findings] | [confidence] | [owner] |
| Testing Evidence | Has adequate testing been conducted? | [missing evidence] | [findings] | [confidence] | [owner] |
| Incident Monitoring | Is incident response and monitoring in place? | [missing evidence] | [findings] | [confidence] | [owner] |
| Governance Approvals | Have required approvals been obtained? | [missing evidence] | [findings] | [confidence] | [owner] |
| Beyond AI-Specific Law | What non-AI legal domains apply? | [missing evidence] | [findings] | [confidence] | [owner] |

Use:
- `Status`: `Pass`, `Partial`, `Fail`, or `Unknown`
- `Confidence`: `High`, `Medium`, or `Low`

### 5. Remediation Checklist

Provide a flat checklist of concrete remediation actions.

Example items:
- [ ] Complete the AI impact assessment.
- [ ] Confirm whether personal or sensitive data is processed.
- [ ] Define required human review before outputs are relied on.
- [ ] Complete testing for quality, abuse resistance, and monitoring.
- [ ] Confirm legal, privacy, security, and business ownership.

### 6. Risk Confidence Assessment

Summarize overall confidence and explain what facts or evidence raise or lower confidence.

### 7. Recommended Next Steps

Confirm whether the following exist where applicable:
- AI impact assessment
- Model card or equivalent documentation
- Technical documentation
- Instructions for use
- Transparency disclosures
- Incident response plan
- Post-launch monitoring plan
- Owner, approver, and escalation path

### 8. Governance as a Living Record

Document:
- Re-review triggers
- Drift or degradation signals to monitor
- Review cadence
- Complaint and feedback handling
- Continuous-improvement expectations

### 9. Mandatory Disclaimer

Include:
> This review supports AI governance processes but does not replace formal legal review. This is not legal advice. This output is a draft and may contain errors or omissions. Verify all conclusions against company policies, primary regulatory sources, and the appropriate internal legal, privacy, security, and compliance teams.
