# Example Outputs

Use these examples to keep the skill behavior consistent.

## Example 1: Intake-Only Response

Use this pattern when the user asks for a review but has not yet provided enough facts or evidence.

```md
I need a few facts and documents before I can draft the review.

To get started, I need the core use-case details first:

- What is the AI use case, and what problem is it meant to solve?
- Who are the intended users?
- What is your organization's role here: customer of a vendor, deployer, integrator, or something else?
- What model or vendor is involved, if known?

Once you share that, I’ll ask the next short set of questions.
```

Do not convert these questions into a markdown table or a fill-in form. Ask them as direct questions the user can answer in plain text, one topic block at a time.

## Example 2: Preliminary Review

Use this pattern only after the intake-first process has happened and the user cannot or will not provide more information.

```md
# Draft AI Governance Review

## Requested AI Use Case Summary
- Use Case: Internal drafting assistant for contract summaries
- Scenario: Internal AI Use
- Organization Role: Internal business user
- Intended Users: Legal operations team
- Model / Vendor: Unknown
- Data Types Involved: Contract text; possible confidential information
- Deployment Model: Unknown
- Human Oversight: Human review before use
- Testing and Monitoring: Unknown
- Documents / Evidence Reviewed: User description only

## Review Status
Preliminary Review

Blocking unknowns:
- Model or vendor identity
- Deployment model
- Testing evidence
- Monitoring plan
- Privacy and retention documentation
```

Continue with the scorecard only after making clear that unknowns and missing evidence reduce confidence.

## Example 3: Final Review

Use this pattern only when minimum facts and core evidence are available.

```md
# Draft AI Governance Review

## Requested AI Use Case Summary
- Use Case: Customer-facing AI support assistant for billing questions
- Scenario: Product AI Integration
- Organization Role: Deployer and integrator
- Intended Users: Existing customers
- Model / Vendor: Vendor-provided LLM with internal retrieval layer
- Data Types Involved: Account data and support transcripts
- Deployment Model: Customer-facing, vendor-hosted model with internal controls
- Human Oversight: Escalation to human support and manual override
- Testing and Monitoring: Functional, abuse-resistance, and staged-release testing completed; monitoring plan documented
- Documents / Evidence Reviewed: Architecture overview, AI impact assessment, DPA, subprocessor list, testing summary, disclosure copy, monitoring plan

## Review Status
Final Review
```

Proceed with the scorecard, remediation list, confidence assessment, and next steps.
