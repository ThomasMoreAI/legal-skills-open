---
name: class-action-notice
title: Class Action Notice
description: Drafts Rule 23-compliant class action notices to absent class members for certification or settlement. Agent uses this skill when drafting class action notices, class member notifications, settlement notices, opt-out notices, or fairness hearing notices.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/class-action-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Class Action Notice

Drafts a Rule 23-compliant notice informing absent class members of their rights, options, and deadlines in class certification or settlement proceedings.

## Prerequisites

Gather before drafting:

1. **Complaint** — factual allegations, legal claims, named parties
2. **Class certification order** — exact class definition, court-specified notice requirements
3. **Settlement agreement** (if applicable) — terms, amounts, allocation, release scope
4. **Court orders on notice** — format, length, reading level, mandatory language, distribution method
5. **Key deadlines** — claim submission, opt-out, objection, fairness hearing date/time/location
6. **Contacts** — class counsel, defense counsel, claims administrator, settlement website

## Quick Start

1. Collect all prerequisites and court-ordered specifications
2. Draft notice sections in order (heading → lawsuit → class definition → terms → options → procedures → hearing → resources → disclaimers)
3. Verify Rule 23(c)(2)(B) mandatory elements are covered
4. Apply due process test: would a non-lawyer understand their rights and options?
5. Cross-reference every factual statement against source documents

## Notice Sections

### 1. Heading & Introduction

| Element | Requirement |
|---|---|
| Court ID | Full district, division, department |
| Case caption | All named plaintiffs/defendants, exactly as filed |
| Civil action number | As assigned |
| Alert banner | **Bold** attention statement (e.g., "LEGAL NOTICE: A class action lawsuit may affect your rights.") |
| Subject matter | Concrete facts — specific conduct, dates, amounts |
| Why received | Court-authorized notice; not a solicitation or lawsuit against recipient |
| Neutrality disclaimer | Court has made no determination on the merits |

### 2. Description of the Lawsuit

Draft in this order:

1. **Factual background** — chronological, specific dates/conduct from complaint; concrete details only
2. **Legal claims translated** — convert statutory citations to plain English (e.g., "TCPA prohibits automated calls to cell phones without consent")
3. **Defendant's position** — from answer/defense filings, presented with equal clarity
4. **Procedural history** — key milestones in lay terms

### 3. Class Definition & Membership

- Quote exact class definition from certification order or settlement agreement
- Break each element into separately explained criteria
- Address: who qualifies as "person," qualifying conduct, geographic scope, temporal boundaries (inclusive dates, timezone)
- Label and explain subclasses separately if they exist
- List all exclusions (officers/directors, judicial officers, prior releasors, etc.)
- Provide practical membership guidance (e.g., "If your statement shows a $2.95 'processing fee' during the class period, you are likely a member")
- Include contact for membership questions

### 4. Settlement Terms (If Settlement Notice)

| Component | Include |
|---|---|
| Total value | Exact dollar amount |
| Allocation | Fund → class payments, admin costs, fees, service awards |
| Distribution method | Pro rata, tiered, or flat; concrete dollar examples per tier |
| Attorney fees | Exact amount/percentage; note requires separate court approval |
| Service awards | Amount per representative; note requires court approval |
| Injunctive relief | Specific conduct changes, not generalities |
| Release scope | Exactly which claims released vs. preserved |
| Risk assessment | Balanced: case strengths vs. litigation risks; why settlement is reasonable |

### 5. Legal Rights & Options

Present each as a discrete block:

**Option A — Submit a Claim (Participate)**
- What to do, where to get form, required info/docs
- Deadline with time and timezone
- Consequence: receive payment, release claims

**Option B — Exclude Yourself (Opt Out)**
- Written, personally signed (not by attorney without POA)
- Contents: full name, address, case name/number, exclusion statement, signature
- Mail to `[ADDRESS]`, postmarked by `[DATE]`
- No mass/group exclusions
- Consequence: no benefits, retain right to sue individually
- Caveat: statute of limitations may have run

**Option C — Object**
- Written objection filed with court + copies to class and defense counsel
- Contents: case name/number, name/address/phone, specific reasons, supporting docs, intent to appear, signature
- Deadline: `[DATE]`
- Consequence: still bound if approved; may still submit claim

**Option D — Do Nothing**
- **PROMINENT WARNING**: Bound by court's decision; forfeits right to sue separately; receives nothing unless claim submitted

### 6. Claims Process

1. **Obtain form** — website URL, phone with hours/timezone, mailing address
2. **Complete form** — required fields; sworn statement accepted if no documentation
3. **Submit** — online, mail, or email; deadline with time/timezone per method
4. **Retain copy** for records

### 7. Exclusion Procedure

- Exact mailing address
- Required elements (per Option B above)
- Postmark deadline
- Individual requests only

### 8. Fairness Hearing

- Date, time, courtroom, full court address
- Purpose: court decides if settlement is fair, reasonable, adequate; rules on fees/awards
- Attendance not required; right to attend if intent stated in written objection
- Hearing may be continued without further notice; how to confirm (website, phone, PACER)
- **Binding effect**: final judgment = res judicata on released claims for all non-excluded members

### 9. Resources & Contacts

- Class counsel: name, firm, address, phone, email, website
- Claims administrator: name, company, toll-free phone with hours, email, website
- Settlement website: complaint, agreement, orders, claim form, FAQs, deadline calendar
- **Scam warning**: Never pay to participate; legitimate contact only from administrator or class counsel
- Court records: PACER URL, Clerk's Office address/hours
- Primacy clause: settlement agreement and court orders control over this summary

### 10. Disclaimers

- Not legal advice
- Class counsel represents the class, not individual members
- Suggest consulting personal attorney for individual advice
- Include state bar lawyer referral service if appropriate

## Drafting Rules

- **Reading level**: 8th–10th grade for general consumer classes; adjust for class composition
- **Tone**: Scrupulously neutral — do not encourage or discourage any option
- **Style**: Average 15–20 words per sentence; active voice; one concept per paragraph
- **Jargon**: Avoid; if unavoidable, add parenthetical plain-language definition immediately
- **Placeholders**: Bracket format — `[DATE]`, `[ADDRESS]`, `[URL]`, `[PHONE NUMBER]`
- **Court orders override** any default format guidance in this skill

## Mandatory Compliance Checks

- [ ] **Rule 23(c)(2)(B) elements**: nature of action, class definition, class claims/issues/defenses, right to enter appearance through counsel, right to request exclusion, binding effect, time/manner for exclusion
- [ ] **Due process test**: reasonable non-lawyer understands all rights and options
- [ ] **FRE readiness**: notice may become an exhibit; maintain precision and verifiability throughout
- [ ] All factual statements cross-referenced against source documents
- [ ] Court-ordered specifications followed exactly
