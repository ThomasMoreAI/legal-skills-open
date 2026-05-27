---
name: ca-discovery-response
title: California Discovery Response Builder
description: Drafts code-compliant California responses to Requests for Production (CCP § 2031.010 et seq.) for Superior Court. Use when the user mentions California RFP responses, CCP 2031, discovery objections, compliance statements, inability to comply, privilege objections, Bates numbering, verification requirements, or responding to document requests in California state court. California Superior Court only — not for federal court without substantial modification.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ca-discovery-response
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# California Discovery Response Builder

Produces service-ready RFP responses under the CCP § 2031 three-option statutory framework (compliance, inability, objection). All output includes attorney-confirmation placeholders and is ready for verification and service.

**Scope**: California state court only. For federal court (FRCP 34), warn the user and stop.

## Quick Start

1. Gather case metadata and the full RFP set (see Intake below)
2. Reproduce each request verbatim, then classify and draft responses
3. Assemble into California service format with verification and proof of service
4. Run the quality checklist before delivering

## Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft":

1. **Full RFP set** — definitions, instructions, attachments
2. **Case metadata** — caption, case number, county, department, judge
3. **Attorney info** — name, bar number, firm, contact (both sides)
4. **Service details** — date served, method → determines deadline
   - 30 days (CCP § 2031.260); extensions for mail (§ 1013) / e-service (§ 1010.6)
   - `[ATTORNEY: CONFIRM RESPONSE DEADLINE — MISSED DEADLINE MAY WAIVE ALL OBJECTIONS]`
5. **Document universe** — categories, storage, custodians, sensitivity
6. **Privilege status** — withheld documents? Privilege log timing?
7. **Format** — pleading paper (28-line) vs. clean service format
8. **Case type** — PI, employment, contract, coverage/bad faith, etc.

**Defaults** (if user doesn't respond): hybrid objection + conditional compliance; clean service format; PI case type; standard privacy/overbreadth objections. Label defaults clearly.

## Core Workflow

### 1. Parse Requests

Reproduce every request **verbatim** — subparts, defined terms, time limits. Mirror propounding party's numbering. Include definitions section if extensive.

### 2. Classify Each Request

| Response Type | Statute | When |
|---|---|---|
| Compliance (full/partial) | § 2031.220 | Documents exist, no valid objection |
| Inability to comply | § 2031.230 | Documents don't exist or aren't in possession/custody/control |
| Objection | § 2031.240 | Improper, overbroad, or privileged |
| Objection + conditional compliance | Common practice | Object to scope, still produce non-privileged documents |

### 3. Draft Objections

Objections must be **specific, fact-tethered, and legally grounded** — no boilerplate.

Objection modules (adapt per request — never paste blindly):

- **Overbreadth/proportionality** — explain why scope is unreasonable; state the construction under which you will search
- **Vagueness** — identify unclear terms; state your construction
- **Attorney-client privilege** — Evid. Code § 954; note privilege log per CCP § 2031.240(c)(1)
- **Work product** — CCP § 2018.030; distinguish qualified from other work product
- **Privacy** — Cal. Const. Art. I, § 1; limit to injuries/damages at issue; propose protective order
- **Insurance** (case-type dependent) — irrelevant in routine PI; fully discoverable in coverage/bad faith
- **Lien-related** (case-type dependent) — collateral source rule, privacy; tailor to lien type
- **Expert materials** — consulting expert materials protected; testifying expert reports must be disclosed

Prefer statutory citations (CCP, Evid. Code) over case law. Mark any case citation `[VERIFY CITATION BEFORE SERVICE]`.

### 4. Draft Substantive Responses

**Compliance:**

> Subject to and without waiving the foregoing objections, Responding Party will comply with this Request. Responsive, non-privileged documents are being produced concurrently herewith as Bates Nos. [INSERT BATES RANGE: _____ to _____].

State production organization: "as kept in ordinary course of business" or "organized and labeled to correspond" (CCP § 2031.280(a)).

**Inability to comply** (CCP § 2031.230):

> After a diligent search and reasonable inquiry, Responding Party is unable to comply. [SPECIFY: documents have never existed / are not in possession, custody, or control / were in possession of [IDENTIFY]]. Search included [DESCRIBE REPOSITORIES — ATTORNEY/CLIENT TO CONFIRM].

**ESI**: Specify production format per CCP § 2031.280(c) — form ordinarily maintained or reasonably usable form.

### 5. Assemble Document

1. Attorney information block
2. Caption — "SUPERIOR COURT OF THE STATE OF CALIFORNIA, COUNTY OF [COUNTY]"
3. Case name and number (match operative pleading exactly)
4. Title: "RESPONSES TO REQUESTS FOR PRODUCTION OF DOCUMENTS (SET [NUMBER])"
5. Preliminary statement — reservation of rights, ongoing investigation, supplementation reserved
6. Numbered responses — verbatim request → objections + response
7. Footer: "[PARTY]'S RESPONSES TO REQUESTS FOR PRODUCTION PROPOUNDED BY [PARTY] (SET [NUMBER])"

### 6. Verification and Proof of Service

**Verification** (CCP § 2031.250) — required unless response contains only objections:

> I, [NAME], am a party to this action. I have read the foregoing Responses and know the contents thereof. The matters stated therein are true of my own knowledge, except as to those matters stated on information and belief, and as to those I believe them to be true.

`[CLIENT MUST SIGN — ATTORNEY SIGNATURE IS NOT SUFFICIENT FOR VERIFIED RESPONSES]`

**Proof of service** — California format matching service method. Include `[INSERT SERVICE LIST]` placeholder.

## Post-Draft Review

After delivering, ask:

1. Are response classifications correct for each request?
2. Do objections match your litigation strategy?
3. Any documents to produce that aren't accounted for?
4. Generate verification/proof of service now, or handle separately?

## Quality Checklist

Before finalizing, verify:

- [ ] Every response fits § 2031.210 (compliance, inability, or objection)
- [ ] Requests reproduced verbatim
- [ ] Factual assertions based on user-provided info only
- [ ] Bates placeholders marked `[INSERT BATES RANGE]`
- [ ] Party names, case number, set number consistent throughout
- [ ] Verification included (if any substantive responses)
- [ ] Proof of service included
- [ ] All citations verified or marked `[VERIFY]`
- [ ] No "none exist" claims without described search
- [ ] Case-type-appropriate objections
- [ ] Hybrid responses include both objection and conditional compliance
- [ ] ESI format specified where applicable

## Pitfalls

- **Over-objecting** invites motions to compel and sanctions (CCP § 2031.310, § 2023.010)
- **Under-responding** creates binding admissions
- **Boilerplate objections** without factual specificity are the most common failure
- **Case-type mismatch** — insurance, lien, and privacy objections vary dramatically by case type
- **Anti-hallucination** — all case citations must be verified or left as placeholders; rely on statutory citations over case law; never generate plausible-sounding unverified citations
- **Attorney review required** — all output is practice-support work product; must be reviewed by supervising counsel before service or filing

---

**Key changes from original:**

- **Removed `tags`** — not part of the Agent Skills spec
- **Trimmed description** from 14 lines to 7 while keeping all trigger keywords
- **Removed "Why This Skill Exists"** prose section — Claude already understands discovery law; the overview sentence covers it
- **Renamed checkpoints** — "Checkpoint A/B" became "Intake" and "Post-Draft Review" for clarity
- **Merged "Guidelines" into "Pitfalls"** — eliminated redundancy between the two sections
- **Converted Quality Audit to checklist format** with `- [ ]` for trackable progress
- **Removed ethics line with `[VERIFY]`** — replaced with the cleaner "attorney review required" pitfall
- **Cut ~40 lines** (170 → ~130) while preserving every statute, response template, objection module, and procedural requirement
