---
name: dsar-response-uk-agents
title: /dsar-response
description: Walk through a Data Subject Access Request (or erasure, portability, rectification, restriction, or objection request) and draft the response — verify identity, locate data system-by-system, assess DPA 2018 Schedule 2 exemptions, draft the acknowledgment and substantive response letters within the 1-month statutory deadline. Use when a DSAR comes in, the user pastes a data subject request, or says "DSAR came in", "access request", "right to erasure", "right to be forgotten", "someone wants their data", or a similar phrase.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/privacy-legal-uk/skills/dsar-response
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /dsar-response

1. Load `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → DSAR process (systems list, verification method, SLA).
2. Run the workflow below.
3. Classify request type. Check escalation triggers — if any fire, route before proceeding.
4. Walk through: verify identity → walk systems list → DPA 2018 Sch.2 exemption analysis → draft.
5. Output response draft. Do NOT send — human reviews and sends.
6. Log the DSAR per house process.

**Before pasting the request:** the request will contain the data subject's personal data. Confirm your session and output storage meet your data-handling requirements. Redact anything you don't need (ID attachments, unrelated email threads). Do not store the subject's name in filenames.

```
/privacy-legal-uk:dsar-response
[paste the request email]
```

---

# UK GDPR DSAR Response Drafting

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal-uk:matter-workspace switch <slug>` or say `practice-level`."

---

## Purpose

A DSAR has a statutory deadline (1 calendar month under UK GDPR Art.12(3), extendable by 2 further months for complex or numerous requests), a process (verify, locate, assess exemptions, respond), and a number of places it can go wrong. This skill walks through each step and drafts the response.

## Jurisdiction assumption

This analysis assumes UK GDPR and DPA 2018 as the primary regime. If the data subject is in the EU and EU GDPR also applies, note the potential parallel obligation — deadlines are the same (1 month) but the exemption regime differs slightly.

## Load the process

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## DSAR process`. That section has:
- The systems list (every place personal data lives)
- Identity verification method
- Response SLA
- Who handles routine vs. who gets escalated
- DPA 2018 Sch.2 exemptions regularly relied on
- Manifestly unfounded / excessive policy

If the systems list is empty or stale, flag it — can't do a complete DSAR without knowing where to look.

## Workflow

### Step 1: Classify the request

Identify which right under UK GDPR the data subject is invoking. Common categories:

- **Access (Art.15)** — copy of their personal data + supplementary information about processing
- **Erasure / right to be forgotten (Art.17)** — remove their data (subject to exemptions and DPA 2018 Sch.2)
- **Portability (Art.20)** — their data in machine-readable, structured, commonly used format (applies to data provided by the data subject and processed by consent or contract, by automated means)
- **Rectification (Art.16)** — fix inaccurate personal data or complete incomplete data
- **Objection to processing (Art.21)** — stop a particular processing (overriding legitimate interests or direct marketing)
- **Restriction (Art.18)** — pause processing pending a dispute
- **Rights related to automated decision-making (Art.22)** — not to be subject to a solely automated decision with legal or similarly significant effects; explanation; human review

**Research the applicable UK GDPR right before proceeding.** Use the uk-legal MCP where available. For each invoked right, identify the scope of the right, any conditions or exemptions, and the DPA 2018 modifications. Cite the controlling provision with OSCOLA-style references (UK GDPR, art 15; *Data Protection Act 2018*, sch 2). Note effective dates; UK GDPR rights may be affected by enacted UK legislative reform. Flag uncertainty and escalate for professional verification rather than stating a rule you haven't confirmed.

> **No silent supplement.** If the uk-legal MCP returns few or no results for a right, exemption, or deadline, report what was found and stop. Say: "The uk-legal MCP returned [N] results for [topic]. Options: (1) broaden the query, (2) check govuk MCP, (3) proceed on model knowledge tagged `[model knowledge — verify]`, or (4) flag as unverified and stop." A solicitor or DPO decides.
>
> **Source attribution tiering:**
> - `[settled — last confirmed YYYY-MM-DD]` — stable, well-known statutory provisions (e.g., UK GDPR Art.12(3) 1-month deadline, Art.15 access right, DPA 2018 Sch.2 exemptions as a concept)
> - `[uk-legal MCP]` — retrieved from the uk-legal MCP this session
> - `[verify]` — model-knowledge citations to verify
> - `[verify-pinpoint]` — specific subparagraph letters, Schedule paragraph numbers — always verify

Some requests are combinations — "delete my account and send me my data first" is erasure + access. Handle as two linked requests with a single acknowledgment.

**Special rules for direct marketing objections (Art.21(3)):** an objection to processing for direct marketing purposes must be complied with immediately — there is no balancing test. Cite `[UK-GDPR-ART.21(3)]`.

### Step 2: Verify identity

Per the method in `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. Common approaches:

- **Logged-in verification:** Request came from within an authenticated session → identity confirmed for the account data
- **Email match:** Request came from an email on file → usually sufficient for standard access requests
- **Additional verification:** For high-value accounts, deletion requests, or high-volume data → additional step; calibrate to the risk of providing data to the wrong person or deleting the wrong data

**Calibrate to risk.** Over-verifying creates a barrier that regulators have criticised — the ICO's guidance is that verification should be proportionate and not be used as a gatekeeping mechanism. Under-verifying risks handing someone else's personal data to a third party (a separate breach). `[ICO-GUIDANCE]`

If identity can't be verified:

```markdown
We were unable to verify that this request came from the individual whose personal
data is at issue. To proceed, please [verification step]. We cannot provide personal
data in response to a request we cannot verify.
```

This pauses the practical response but the clock still runs — respond within a few days, not on day 28.

### Step 3: Locate the data

Walk the systems list from `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. For each system:

| System | Queried? | Personal data found? | What |
|---|---|---|---|
| Production database | | | |
| Analytics (e.g., Mixpanel, Amplitude) | | | |
| Support tickets (e.g., Zendesk, Freshdesk) | | | |
| CRM (e.g., Salesforce, HubSpot) | | | |
| Email marketing (e.g., Mailchimp, Klaviyo) | | | |
| Logs | | | |
| Backups | | | (note: see Sch.2 para.16 exception for data held in unstructured manual files; retention exemption for backups under Art.17(3)(e)) |
| Third-party processors | | | (may need to be notified for erasure — Art.17(2) controller must take reasonable steps) |

**For a B2B processor:** the data subject may actually be your customer's end user. Check whether this is your DSAR to respond to, or whether your Art.28 DPA says to forward DSARs to the controller. Most processor DPAs route DSARs through the controller. If so, forward promptly and tell the data subject you've forwarded the request.

### Step 4: DPA 2018 Schedule 2 exemption analysis

Not everything gets produced or deleted. **The DPA 2018 Schedule 2 contains UK-specific exemptions that modify the UK GDPR rights for access and erasure.** These are more numerous than the EU GDPR exemptions and differ in several important respects. Always research the specific Schedule 2 paragraph before asserting an exemption. `[DPA2018-S.15, SCH.2]`

Use the uk-legal MCP to retrieve the current DPA 2018 Schedule 2 text before asserting any exemption.

**Key DPA 2018 Sch.2 exemptions for access requests (common ones — verify current text):**

| Exemption | DPA 2018 Sch.2 para | When it applies |
|---|---|---|
| Legal professional privilege | Para.19 | Communications between client and legal adviser for the purpose of giving or receiving legal advice |
| Confidential references | Para.24 | References given or received in confidence for employment, education, training, or appointment |
| Negotiations with the data subject | Para.15 | Information relating to negotiations with the data subject that the controller is not required to disclose |
| Management information | Para.16 | Forecasts, management planning, negotiations info where disclosure would prejudice the business |
| Examination scripts and marks | Para.20-21 | Exam scripts; examination marks before intended release date |
| Research, statistics, archiving | Para.26 | Subject to safeguards |
| Legal proceedings | Para.23 | Where data is processed for the purpose of, or in connection with, legal proceedings |

**Additional Art.17(3) grounds to refuse erasure (under UK GDPR):** `[UK-GDPR-ART.17(3)]`
- Freedom of expression and information
- Legal obligation
- Public health
- Archiving, research, statistical purposes
- Establishment, exercise, or defence of legal claims

**Don't narrow the exemption list on a subjective call.** Propose exemptions where a good-faith basis exists and flag uncertain ones; the solicitor or DPO narrows the list before the response goes out. Dropping an exemption that later turns out to apply is costly — once material is disclosed, the exemption is functionally gone. Every proposed exemption carries an explicit note: **"proposed — requires DPO / solicitor review before asserting."**

**Document every exemption claimed.** If the ICO asks why data wasn't produced or wasn't deleted, the exemption needs a citation to the specific DPA 2018 Sch.2 paragraph or UK GDPR article.

**Third-party data in scope:** Does the record contain personal data about *other* individuals? Redact or withhold if producing it would disclose another person's data without their consent, unless it's reasonable to produce it without the third party's consent (e.g., it is reasonable in all the circumstances to disclose). UK GDPR Art.15(4) `[UK-GDPR-ART.15(4)]`.

### Step 5: Draft the response — TWO LETTERS

> **Research-connector pre-flight.** Before emitting either letter or the internal exemption analysis, check whether the uk-legal MCP or govuk MCP is reachable for this session. Collect this into the reviewer note per CLAUDE.md `## Outputs` — the reviewer note sits on the INTERNAL exemption analysis and cover memo, NOT on the outward-facing DSAR letters. If no connector is reachable, record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; exemption references, deadline calculations, and DPA 2018 Sch.2 paragraph numbers are especially fabrication-prone, verify before asserting any exemption to a data subject or the ICO`.

**Two-letter rule:** produce an acknowledgment letter (sent promptly) AND a substantive response letter (sent by the statutory deadline). Do not collapse them into one letter sent on day 28.

- **Step 5a — Acknowledgment letter.** Sent within days of receipt (target: same-day to 3–5 days, always well inside the 1-month window). Confirms receipt, states the controller's understanding of the request, states the response clock and target date, asks for any outstanding identity-verification material.
- **Step 5b — Substantive response letter.** The actual disclosure, erasure confirmation, or portability export. Sent by the statutory deadline (or internal SLA if tighter). Only after identity verification is complete and Step 3 / Step 4 data location + exemption analysis is done.

**Clock-start rule:** The 1-month clock starts on receipt of the request, not on completion of identity verification — unless the data subject fails to provide information necessary to identify them (Art.12(6)) `[UK-GDPR-ART.12(6)]`. Do not tacitly toll the clock on verification; if verification is needed, send the acknowledgment and request verification simultaneously.

**Extension (Art.12(3)):** `[UK-GDPR-ART.12(3)]` The deadline may be extended by a further 2 months where the request is complex or numerous, taking into account the complexity and number of requests. If an extension is needed:
- Send notice of the extension to the data subject within the first 1-month period
- State the reason for the extension
- Note: "complex or numerous" is a narrow ground — the ICO does not consider high volume alone sufficient without genuine complexity. Document the reason.

**Manifestly unfounded or excessive requests (Art.12(5)):** `[UK-GDPR-ART.12(5)]` The controller may charge a reasonable fee or refuse to act on a request that is manifestly unfounded or excessive (particularly where repetitive). The controller must be able to demonstrate this. Refusal requires informing the data subject of the reason and their right to complain to the ICO and seek a judicial remedy. Use this ground sparingly — the ICO scrutinises it. Always escalate to DPO / solicitor before refusing or charging.

**Before proceeding to send either letter to the data subject:** Read `## Who's using this` in the practice-level CLAUDE.md. If the Role is Non-lawyer:

> Sending a DSAR response has legal consequences — the content, the exemptions claimed, and the omissions are all reviewable by the ICO, and misstatements become enforcement exposure. Have you reviewed this with a solicitor or DPO? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: data subject, right invoked, applicable regime, what was located across the systems list, what is being withheld and under which DPA 2018 Sch.2 or UK GDPR exemption, identity verification posture, response deadline, and the three things to ask the professional before the letter goes out.]
>
> If you need to find a qualified solicitor or barrister: the SRA's [Find a Solicitor](https://solicitors.lawsociety.org.uk/) service is the fastest starting point.

Do not proceed past this gate without an explicit yes.

> **Note:** Both DSAR letters are externally-facing deliverables sent to the data subject. Do **not** include the work-product header from the practice-level CLAUDE.md on either letter. Internal notes, logs, and exemption analyses are internal records — keep those separate and prepend the work-product header per the practice-level CLAUDE.md `## Outputs`.

#### Step 5a — Acknowledgment letter template

```markdown
Subject: We received your data subject request — [Company] — [date]

Dear [Name],

We received your [access / erasure / portability / rectification / objection / restriction]
request on [date received].

**Your request, as we understand it:** [one-sentence restatement — e.g., "a copy of all personal data we hold associated with your account, together with information about how we use it, followed by deletion of your account."]

**What happens next:**
- Our target date for the substantive response is [date — no later than 1 calendar month from receipt; use internal SLA if tighter]. [If identity verification is outstanding: "We need [specific verification step] before we can proceed — see below."]
- If the request is complex or we receive multiple requests from you at the same time, we may extend this by up to 2 further months. We will tell you within the first month if we need to do this and explain why. `[UK-GDPR-ART.12(3)]`
- There is no charge for this request. [Or: A charge may apply if the request is manifestly unfounded or excessive under UK GDPR Art.12(5) — describe only if applicable.]

[If identity verification is outstanding:]
**To verify your identity,** please [specific verification step — e.g., reply to this email from the address on file with the last 4 digits of your payment method]. We will continue working on your request while we await this.

If you have questions, please contact [privacy / DPO contact details].

[Sender / Controller name and contact details]
```

#### Step 5b — Substantive response letter templates

**Access request response (Art.15):**

```markdown
Subject: Your Data Subject Access Request — [Company] — [date]

Dear [Name],

We received your request on [date] for a copy of the personal data we hold about you.

**What we found:**

We hold the following categories of personal data associated with [identifier]:

| Category | Source | Purpose | Lawful basis | Retained until |
|---|---|---|---|---|
| [Account information: name, email, address] | You, at sign-up | Account management | Contract (Art.6(1)(b)) | Account deletion |
| [Usage data] | Our service | Analytics, product improvement | Legitimate interests (Art.6(1)(f)) | [period] |
| [Support correspondence] | You | Customer support | Legitimate interests | [period] |

**Your personal data is attached** in [format]. [Secure delivery note — password-protected archive, secure link with expiry, etc.]

**Recipients:** We share data with the following categories of recipients: [list categories of processors / controllers / joint controllers, or link to the relevant section of the privacy notice].

**International transfers:** [If applicable: data is transferred to [country / countries] under [UK adequacy decision / IDTA / UK Addendum to EU SCCs — identify the specific mechanism].]

**Your other rights:** You may also request [erasure / rectification / portability / object to processing]. To do so, [method].

**Data we did not include:**
- [Category] — [exemption and specific authority, e.g., "communications with our solicitors re [matter] — legal professional privilege under DPA 2018 Sch.2 para.19"]
- [Data about other individuals has been redacted from [source] — UK GDPR Art.15(4)]

If you are unhappy with this response, you have the right to complain to the Information Commissioner's Office (ICO) at [ico.org.uk/make-a-complaint](https://ico.org.uk/make-a-complaint/) or to seek a judicial remedy.

[Sender / Controller name and contact details]
```

**Erasure request response (Art.17):**

```markdown
Subject: Your Erasure Request — [Company] — [date]

Dear [Name],

We received your request on [date] to erase the personal data we hold about you.

**What we erased:**

| Category | System | Erased on |
|---|---|---|
| [Account and profile data] | Production database | [date] |
| [Analytics events] | [Analytics platform] | [date] |
| [etc.] | | |

**What we retained and why:**

| Category | Reason | Retained until |
|---|---|---|
| [Transaction records] | Legal obligation (tax records — HMRC requirements, [cite specific obligation]) | [date] |
| [Backup snapshots] | Technical backup rotation — will be overwritten on next rotation | [date — approximately] |
| [Legal proceedings data] | Establishment, exercise, or defence of legal claims — UK GDPR Art.17(3)(e) | [date / until resolution] |

**Third-party processors:** We have instructed [list processors] to erase your personal data from their systems `[UK-GDPR-ART.17(2)]`.

Your account is now closed. If you are unhappy with this response, you have the right to complain to the ICO at [ico.org.uk/make-a-complaint](https://ico.org.uk/make-a-complaint/).

[Sender / Controller name and contact details]
```

### Step 6: Log it

DSARs get audited by the ICO. Record in your DSAR register / log:
- Date received
- Date identity verified (if applicable)
- Date acknowledged
- Date substantive response sent
- What was produced / disclosed
- What was withheld and under which DPA 2018 Sch.2 / UK GDPR exemption
- Whether an extension was used and why
- Who handled it
- ICO complaint or judicial proceedings (if any)

## Escalation triggers

Per `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → Escalation table, escalate when:

- Requester is (or might be) a claimant in litigation, their solicitor, or a journalist
- Request scope is unusual ("all data including internal correspondence about me")
- There is a litigation hold on this individual's data (erasure request + lit hold = conflict — solicitor decides)
- Requester is disputing a previous DSAR response
- The ICO is cc'd or mentioned
- Requester is asserting a right to a data-protection fee waiver that suggests prior regulatory contact
- Request is from a child or on behalf of a child (additional considerations apply)

## Deadline management — summary

| Deadline | Rule | Citation |
|---|---|---|
| Acknowledgment | Promptly — target same-day to 3–5 days | Best practice |
| Substantive response | 1 calendar month from receipt | UK GDPR Art.12(3) `[UK-GDPR-ART.12(3)]` |
| Extension notice (if needed) | Within the first 1-month period | UK GDPR Art.12(3) `[UK-GDPR-ART.12(3)]` |
| Extended deadline (if extension invoked) | Up to 2 further months from original deadline | UK GDPR Art.12(3) |
| Third-party processor notification (for erasure) | Without undue delay | UK GDPR Art.17(2) `[UK-GDPR-ART.17(2)]` |

If you are going to need an extension, send the extension notice before the first 1-month deadline expires. Day-of extensions are possible but look poor to the ICO.

## What this skill does not do

- It doesn't query systems directly. It walks you through the checklist; a human (or a connected tool) does the actual queries.
- It doesn't make exemption calls on close cases. It flags them for a DPO or solicitor.
- It doesn't send the response. Draft, review, human sends.
- It doesn't run a conflicts check between the DSAR requester and any pending litigation hold — flag this for human review.
