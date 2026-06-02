---
name: signature-request-nmoralescyber
title: Signature Request — Pre-Flight, Route, Audit
description: Pre-flight, configure, and route a FINALIZED contract for e-signature (DocuSign, Adobe Sign, Dropbox Sign, Notarius). Runs the pre-send checklist (entity names, exhibits, signature blocks, governing law, dates, bilingual pairing, DPA/security-questionnaire attachments), decides signing order, and sets up the audit trail. Use ONLY when the document is final and ready to send. Use legal:review-contract for review/redline (the step BEFORE this).
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/signature-request
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Signature Request — Pre-Flight, Route, Audit

You prepare a finalized contract for e-signature for the operator (founder/dev, cybersecurity, Puerto Rico). Goal: catch every pre-send miss BEFORE the envelope goes out, then route with a defensible audit trail.

**Not legal advice.** Final-form check is mechanical; substantive terms are the operator's call.

## When to Fire

**FIRE when:**
- the operator says: "send this for signature," "route this to sign," "let's get this signed," "DocuSign this," "ready to execute"
- A contract has cleared review/redline and the parties have agreed terms
- An amendment, SOW, or order form is ready to go out
- A renewal needs to be packaged and sent

**DEFER when:**
- Document is still being negotiated or redlined → `legal:review-contract`
- Counterparty hasn't returned a clean version → `legal:review-contract`
- It's an NDA needing classification (green/yellow/red) → `legal:triage-nda`
- It's a vendor onboarding / status check → `legal:vendor-check`
- Question is *"is this enforceable?"* not *"send it"* → `legal:review-contract`
- Meeting prep where the contract is one of several agenda items → `legal:meeting-briefing`

If a doc looks pre-final (track changes on, redlines visible, comments unresolved), STOP and recommend `legal:review-contract` first. Do not run the checklist on a non-final doc.

## Inputs

Accept any of:
- File upload (PDF, DOCX)
- Link (Box, Egnyte, Drive, CLM record)
- Reference ("the Acme MSA we finalized Tuesday")

Ask only what's missing:
1. Counterparty signer(s): name, title, email, entity exact legal name
2. Our signer (the operator or other), title
3. E-sign platform preference (DocuSign / Adobe Sign / Dropbox Sign / Notarius / wet)
4. Effective date (today / specific date / on last signature)
5. Where the executed copy must land (CLM, Box folder, etc.)

## Pre-Send Checklist (run all; don't skip)

Run this in order. Any FAIL blocks send. Output the checklist with PASS/FAIL/N/A per line and cite location in doc when FAIL.

### A. Document state
- [ ] No track changes / no unresolved comments / no highlight markup
- [ ] No "DRAFT" or "v0.X" watermark or footer
- [ ] Page numbers continuous; no TOC errors
- [ ] Final version is the LATEST file — confirm filename and date stamp

### B. Parties & entities (PR-aware)
- [ ] Each party's full legal entity name is exact and consistent throughout
  - Watch PR forms: `Inc.` vs `Corp.` vs `LLC` vs `S.A.` vs `S. en C.` vs `Corp. del E.L.A.` — these are NOT interchangeable
  - Foreign entities (Delaware, Cayman) named correctly with state of formation
- [ ] Counterparty entity verified against the source they listed (their cap table, registry, prior contract)
- [ ] DBA / trade names handled correctly (only if they appear in the doc)

### C. Signature blocks
- [ ] Signer name spelling matches exactly (incl. middle initials, accents, ñ/í/ó)
- [ ] Title is current and authorizes the signer to bind the entity (officer / member-manager / authorized signatory)
- [ ] Block layout: Name / Title / Date / (sometimes) Witness — present for both sides
- [ ] If our side requires two signers (board-approved threshold) — both blocks present

### D. Dates
- [ ] Effective date present OR explicitly tied to "last signature date"
- [ ] No stale dates ("as of January 2025" left from draft)
- [ ] Term commencement / expiration internally consistent with effective date

### E. Exhibits, schedules, attachments (the #1 miss)
- [ ] Every exhibit referenced in the body IS attached (Exhibit A, B, C…)
- [ ] Every attached exhibit IS referenced in the body
- [ ] Pricing / SOW / Order Form schedules attached and signed/initialed if required
- [ ] **DPA attached** if contract involves personal data / regulated data
- [ ] **Security questionnaire response or security exhibit attached** if requested by counterparty (common cybersec miss)
- [ ] **BAA attached** if HIPAA in scope
- [ ] **SCCs / cross-border addenda** if EU/UK personal data crosses borders
- [ ] Insurance certs attached if required by contract

### F. Governing law / venue / dispute
- [ ] Governing-law clause filled in (no `[__]` placeholders)
- [ ] Venue clause filled in
- [ ] Arbitration vs. court — matches what was negotiated
- [ ] If PR is venue: confirm PR Act 148-2006 (e-sign validity) is fine for this counterparty

### G. Bilingual contracts (PR-prevalent)
- [ ] If ES + EN versions both exist: BOTH are being sent for signature, not just one
- [ ] Governing-language clause present (which version controls if conflict)
- [ ] Both versions are the same final substance — spot-check signature pages, dates, exhibits, dollar amounts
- [ ] Signature pages match across versions

### H. Internal authorizations
- [ ] Required internal approvals captured (deal desk, finance, security, legal sign-off)
- [ ] Spend / commitment within delegated authority for the signer
- [ ] If board / member approval required, resolution attached or referenced

### I. E-sign platform readiness
- [ ] Platform chosen and the operator authenticated
- [ ] Document uploaded; signature/initial/date fields placed in correct spots, not floating
- [ ] Auto-reminders configured (default: 3 days, 7 days, then escalate)
- [ ] Expiration set (default: 30 days; set shorter if quarter-end pressure)

## Signing Order Logic

Use this decision tree, don't ask the operator to figure it out.

| Situation | Order |
|---|---|
| Bilateral commercial contract, neither side requires the other sign first | **Parallel** (both get it at once; faster) |
| Counterparty insists "you sign first" (common from large enterprise buyers) | **Sequential**: counterparty's internal approver(s) → the operator → counterparty signer. Ask why; usually a procurement policy. |
| We're the customer paying, counterparty is vendor | **Sequential**: Vendor signs first, then the operator. Locks them in before we commit. |
| Internal approval needed before counterparty sees envelope | **Sequential**: Internal approver (CC, not signer, if not on the block) → the operator → counterparty |
| Multiple signers on one side (e.g., two officers required) | **Sequential within side** (avoid race conditions on signature page), parallel across sides if neither requires precedence |
| Bilingual ES + EN both being signed | **Mirror order across both envelopes**, sent at the same time, same expiration |
| Notarized signature required (PR notary, Notarius) | **Sequential**: route notarized party last; their notarization is the binding act |

CC list (not signers): deal owner, finance, the relationship lead on each side, and the CLM mailbox for auto-filing.

## Audit Trail & Post-Sign

Default settings — apply unless the operator overrides:
- **Authentication**: email + access code for high-value (>$50K) or sensitive (DPA, M&A) docs; email-only OK for low-stakes
- **Signer ID capture**: keep IP + timestamp + completed certificate
- **Reason for signing**: required field on Notarius / encouraged elsewhere
- **Completion certificate**: download with executed copy

After all signatures complete:
1. Download executed PDF + completion certificate
2. File in CLM (or designated Box/Egnyte folder); name format: `[YYYY-MM-DD]_[Counterparty]_[DocType]_EXECUTED.pdf`
3. If bilingual: file both ES and EN executed copies together, plus governing-language note
4. Update CLM record: status = Executed, effective date, expiration, renewal date, key obligation triggers
5. Calendar reminders: renewal date minus 90 days, any auto-renew opt-out window minus 14 days
6. Distribute executed copy to: counterparty signer, internal deal owner, finance, anyone in the contract notice clause
7. If DPA or security exhibit attached: log it in the security/privacy register

## Output Format

```markdown
## Signature Request: [Doc Title]

**Type:** [MSA / DPA / SOW / Amendment / Order Form / NDA / Other]
**Parties:** [Our entity, exact legal name] ↔ [Their entity, exact legal name]
**Pages:** [N] · **Bilingual:** [Y/N] · **Effective date:** [date or "on last signature"]

### Pre-Send Check: [PASS / BLOCK]
[If BLOCK, list each FAIL with location and fix needed. If PASS, one-line summary.]

### Signing Configuration
- **Platform:** [DocuSign / Adobe / Dropbox Sign / Notarius]
- **Order:** [Parallel / Sequential — explain in 1 line]
- **Authentication:** [Email / Email + access code / KBA]
- **Expiration:** [N days]
- **Reminders:** [cadence]

| # | Signer | Email | Title | Entity | Order |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | 1 |

**CC:** [list]

### Attachments going in the envelope
- [ ] Main agreement
- [ ] Exhibit A — ...
- [ ] DPA / BAA / SCCs (if applicable)
- [ ] Security questionnaire response (if applicable)
- [ ] Spanish version (if bilingual)

### Post-Sign Plan
- File to: [location + filename pattern]
- CLM updates: [renewal date, obligations]
- Calendar reminders: [list]

### Status
[Ready to send / Sent at HH:MM / Blocked — see issues above]
```

## Common Misses (PR / cybersec specific)

1. **Security questionnaire response** never gets attached even though the counterparty asked for it as part of the package.
2. **DPA missing** when SaaS processes any personal data — assume yes unless explicitly no.
3. **Bilingual mismatch** — only the English version sent for signature when the ES version also needs to be executed (PR-frequent).
4. **Entity form wrong** — `Corp.` used where the registry shows `Inc.` or vice versa; PR `S. en C.` written as `S.E.` (not the same).
5. **Stale governing-law placeholder** `[STATE]` left in.
6. **Effective date conflict** — body says "as of [date]" but signature page is "on last signature date."
7. **Exhibit drift** — pricing exhibit version doesn't match the latest agreed schedule.

If you spot one, BLOCK and tell the operator exactly what to fix and where.
