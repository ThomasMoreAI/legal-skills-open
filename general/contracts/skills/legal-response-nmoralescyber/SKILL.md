---
name: legal-response-nmoralescyber
title: legal:legal-response — Generate Reply from Templates
description: 'Generate a templated reply to a common INBOUND legal inquiry — data subject access/deletion requests (DSARs under GDPR / CCPA / CPRA), litigation / discovery hold notices to internal custodians, vendor legal questions (SLA, audit letter, certificate of insurance, compliance attestation), NDA send/decline responses to business teams, privacy inquiries from individuals, subpoena acknowledgments (always counsel-flagged), and insurance claim notifications. Customizes the chosen template with specific facts, dates, jurisdictions, and applicable regulation, and runs a built-in escalation check that BLOCKS templating for situations needing custom legal work (subpoenas, regulator letters, criminal exposure, sub-processor or internal breach notifications, threatened litigation, unprecedented matters, multi-jurisdiction conflicts). Use when the user says "respond to this DSAR", "draft a litigation hold", "vendor sent a legal question", "sales needs an NDA reply", "got a subpoena — start
  a draft", "privacy inquiry from a user", "insurance claim notification", or pastes inbound legal correspondence and asks for a reply. Do NOT use for: pre-launch regulatory go/no-go on a proposed initiative (use legal:compliance-check), reviewing or redlining a contract document like an MSA/DPA/SOW (use legal:review-contract), auditing live customer-facing legal pages (use legal:legal-audit), classifying an inbound NDA as green/yellow/red (use legal:triage-nda — then come back here to draft the reply), drafting outbound breach notifications to customers or regulators after a confirmed incident (escalate to counsel + incident-response runbook, NOT a template), tracking ongoing compliance program status (use operations:compliance-tracking). Defining characteristic: REACTIVE + inbound inquiry + templated reply with escalation gate.'
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/legal-response
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# legal:legal-response — Generate Reply from Templates

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate a templated response to a common inbound legal inquiry, customize with specific facts, and gate against situations that should not use a template.

**Important:** This skill assists with legal workflows. Generated responses are drafts and must be reviewed by qualified counsel before sending — especially for any regulated communication, anything to a regulator/court, anything touching breach or criminal exposure, and anything cross-border.

## When to use vs. adjacent legal skills

| Skill | When |
|---|---|
| **legal:legal-response (this one)** | Inbound inquiry → generate reply from template (DSAR, hold, vendor Q, NDA send/decline, subpoena ack, insurance) |
| `legal:compliance-check` | Forward-looking go/no-go on a proposed initiative (NOT an inbound reply) |
| `legal:review-contract` | Markup / redline of an actual contract document |
| `legal:legal-audit` | Audit existing live legal pages on the website |
| `legal:triage-nda` | Classify an inbound NDA as green/yellow/red — run BEFORE this skill if the inquiry is an NDA |
| `legal:legal-risk-assessment` | Assess severity/likelihood of an identified risk |
| `operations:runbook` | Operational IR procedure with regulator-clock triggers (this skill drafts the breach text; runbook owns the operational when/how/who) |
| `operations:compliance-tracking` | Ongoing compliance program tracking |

**Defining characteristic:** REACTIVE + inbound inquiry + templated reply + escalation gate.

## Common invocations

- "Respond to this DSAR from a German user requesting deletion"
- "Draft a litigation hold for engineering and product on matter Acme v. Us"
- "Vendor sent us a question about Section 5.2 of our MSA — draft a reply"
- "Sales needs me to send our standard NDA to a prospect"
- "Got a civil subpoena — start an acknowledgment draft (counsel will finalize)"
- "EU user asked how we handle international transfers — privacy inquiry reply"
- "Annual hold reaffirmation reminder for active matters"

## Workflow

### Step 1 — Identify inquiry type
Common types:
- `dsar` (or `data-subject-request`) — access / deletion / correction / portability / opt-out
- `hold` (or `discovery-hold`, `litigation-hold`) — initial notice, reminder, modification, release
- `vendor` — vendor legal question, audit letter, COI request, attestation
- `nda` — send standard NDA, decline NDA, accept counterparty NDA cover note (run `legal:triage-nda` first to classify)
- `privacy` — privacy/cookie/transfer inquiry from an individual
- `subpoena` — subpoena or legal-process acknowledgment (ALWAYS counsel-gated)
- `insurance` — claim notification or reservation-of-rights response
- `custom` — bespoke template

If type is ambiguous, list categories and ask.

### Step 2 — Run the escalation gate FIRST (before drafting)

**ALWAYS-ESCALATE situations — do NOT generate a final templated response:**
1. **Subpoena, warrant, court order, or any legal process** — draft labeled "DRAFT — FOR COUNSEL REVIEW ONLY"; route to outside / senior counsel
2. **Regulator or government-agency letter** (FTC, state AG, DPA, SEC, CFPB, DACO in PR, FBI, etc.)
3. **Sub-processor or internal data-breach notification** — this is incident response, not a templated reply. Route to incident-response + counsel; if a customer-facing notice is needed, draft is custom and counsel-led
4. **Threatened or pending litigation** (cease-and-desist, demand letter, tort claim)
5. **Criminal exposure** of any kind
6. **Media attention involved or likely**
7. **Multi-jurisdiction conflict** (e.g., GDPR right-to-erasure vs. US litigation hold)
8. **Unprecedented matter** with no prior team handling
9. **Executive / board-level subjects** of the matter

**Category-specific escalation triggers (continue templating only if NONE apply):**

| Category | Don't template if... |
|---|---|
| DSAR | minor's data; from a regulator (not the individual); data under litigation hold; current-employee dispute; fishing-expedition scope; special-category data (health/biometric/genetic) |
| Hold | criminal liability; scope unclear/disputed; conflicts with regulatory deletion duty; custodian objects |
| Vendor | dispute / breach allegation; vendor threatening litigation/termination; regulatory (not contract) question; could create binding waiver |
| NDA | counterparty is a competitor; classified info; M&A-flavored; unusual subject matter (AI training data, biometrics) — typically `legal:triage-nda` will already have flagged YELLOW/RED |
| Subpoena | always counsel-gated — privilege issues, third-party data, cross-border, unreasonable timeline are all counsel concerns, not template concerns |

**When triggered:** STOP. Surface the trigger to the user, name it, recommend escalation path (in-house counsel → outside firm if needed), and offer a labeled `DRAFT — FOR COUNSEL REVIEW ONLY` rather than a final reply.

### Step 3 — Load template
Look in local settings (e.g., `legal.local.md`, templates directory). If none exists for this type, offer to create one (see Template Creation Guide) and provide a reasonable default structure in the meantime.

### Step 4 — Gather customization details
Prompt for the variables required by the chosen template. Minimum sets:

- **DSAR:** requester name + contact, request type, data scope, applicable reg (GDPR Art. 15/17/etc., CCPA §1798.105, etc.), receipt date, response deadline (GDPR: 1 month + 2-month extension; CCPA: 45 days + 45-day extension; **PR Ley 111-2005 breach timing is separate**)
- **Hold:** matter name + reference, custodians, scope (date range, data types, systems, channels), outside-counsel contact, effective date, acknowledgment deadline
- **Vendor:** vendor name, agreement reference, specific question, relevant clause(s)
- **NDA:** business-team contact, counterparty, purpose, mutual vs. unilateral, special asks
- **Privacy inquiry:** individual's question, reference to current privacy policy section, jurisdiction
- **Subpoena (draft only):** case ref, court, served-on date, response date, type of process
- **Insurance:** policy number, coverage period, matter description, timeline

### Step 5 — Generate draft
Customize the template. Verify:
- Correct names, dates, references
- Correct applicable regulation cited (e.g., don't cite CCPA for an EU resident)
- Correct response deadline calculated from receipt date
- Tone calibrated (see below)
- Required legal elements present (e.g., DSAR must inform of right to lodge complaint with supervisory authority under GDPR Art. 13(2)(d))
- Signature block + correct contact

### Step 6 — Tone calibration
- **Audience:** internal vs. external; business vs. legal; individual vs. regulator
- **Relationship:** new counterparty vs. existing partner vs. adversarial
- **Sensitivity:** routine vs. contentious vs. regulatory
- **Urgency:** standard vs. expedited
Default DSAR/privacy tone: plain-English, respectful, regulation-cited.
Default hold tone: imperative, formal, marked PRIVILEGED & CONFIDENTIAL.
Default vendor tone: professional, contract-anchored, non-binding caveat where needed.
Default NDA tone: brief, transactional.
Default subpoena draft tone: formal, terse, fact-only, all substance counsel-flagged.

### Step 7 — Present draft + post-send actions
Always present for user review. Offer to draft an email via connected MCP if available. Surface:
- Response deadline (and offer calendar reminder)
- Logging requirement (DSAR register, hold tracker, etc.)
- Follow-up checkpoints (acknowledgment, fulfillment, closure)

## Response categories (template scaffolds)

### 1. DSARs
Sub-types: receipt acknowledgment, identity-verification request, fulfillment (access/delete/correct), partial denial, full denial, extension. Required elements: applicable reg, deadline, verification, supervisory-authority complaint right, contact.

### 2. Litigation / discovery holds
Sub-types: initial notice, reminder, scope modification, release. Required: matter ref, scope (date / data / systems / channels), spoliation prohibition, acknowledgment requirement, contact. Mark PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION.

### 3. Privacy inquiries
Sub-types: cookie/tracking, policy questions, data sharing, children's data, cross-border transfer (SCCs / UK IDTA / adequacy).

### 4. Vendor legal questions
Sub-types: contract status, amendment request, compliance certification, audit response, COI request.

### 5. NDA send / decline / accept-cover
Sub-types: send standard, decline with reason, accept counterparty (cover note only — redline is a contract-review task). Run `legal:triage-nda` first if the NDA hasn't been classified.

### 6. Subpoena / legal process (counsel-gated)
Sub-types: receipt acknowledgment, objection letter, extension request, compliance cover. Templates are starting frameworks ONLY; final response is counsel-led every time.

### 7. Insurance notifications
Sub-types: initial claim notification, supplemental info, reservation-of-rights response.

## Output format

```
## Generated Response: [inquiry type]

ESCALATION CHECK: [PASS — no triggers] OR [BLOCKED — see below]

**To:** [recipient]
**Subject:** [subject]

---
[Body]
---

### Required next steps
1. [Calendar reminder for deadline]
2. [Log entry: DSAR register / hold tracker / etc.]
3. [Counsel review checkpoint, if applicable]
```

## Template management (brief)

Templates should live in local settings with: category, use case, escalation triggers (when NOT to use), required variables, body, follow-up actions, last-reviewed date. Lifecycle: create → counsel review → publish → use → feedback → update → retire.

## Notes

- Always present the draft for user review before send
- For regulated responses (DSAR, subpoena, insurance), surface the deadline and offer a calendar reminder
- If a template was modified during use, suggest updating the source template
- Cybersec / PR-context callouts:
  - DSARs from EU residents: GDPR timeline (1 month, +2 extension)
  - DSARs from CA residents: CCPA timeline (45 days, +45 extension)
  - PR Ley Núm. 111-2005 governs breach-notification timing — breach notices are NOT in scope of this skill (escalate)
  - Sub-processor changes go through `legal:compliance-check` (forward-looking) and the customer-notice template here (reactive notice once decided)
