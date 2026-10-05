---
name: client-intake-canhada-labs
title: Legal Client Intake
description: Legal client intake discipline for conflict-of-interest screening, capacity assessment, scope-of-engagement definition, fee-agreement authoring, identity verification, AML/KYC compliance, and attorney-client privilege establishment. Handles full-identity PII at the contact threshold — the first intake interaction simultaneously creates privilege and opens the conflict database. Use when onboarding a prospective client, drafting an engagement letter, running a conflict database query, assessing signatory authority, structuring fee arrangements under applicable ethics rules, or evaluating AML/KYC risk on a new matter. Applies across practice areas and jurisdictions; calibrate conflict rules to OAB Código de Ética (Brazil) or ABA Model Rules (US) per deployment context.
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/domains/legal/skills/client-intake
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Legal Client Intake

First contact with a prospective client opens attorney-client privilege,
creates conflict obligations, and triggers AML/KYC duties — simultaneously.
All three regimes attach before substantive representation begins. This
skill codifies the doctrine that turns an intake call into a legally
sound engagement: structured conflict query, verified authority, written
scope, compliant fee terms, and privilege-anchored communication channels.

## Cardinal Rule

**No substantive legal advice is provided, no consultation is scheduled,
and no fee is collected until the conflict database query returns
CLEARED.** A single missed conflict can trigger disqualification,
malpractice liability, and disciplinary proceedings under OAB Cód. Ética
Art. 15 or ABA Model Rule 1.7. The conflict check is not a courtesy — it
is a structural gate that all other intake steps depend on.

## Fail-Fast Rule

Halt intake and escalate to the supervising attorney immediately if ANY
of the following conditions are true:

1. Prospective client cannot produce government-issued photo ID within
   the required verification window.
2. PEP screening or sanctions check returns a positive match against OFAC
   SDN, UN Consolidated List, or applicable national list.
3. Conflict database query returns CONFLICT or POTENTIAL-CONFLICT without
   a written waiver signed by all affected current clients.
4. Signatory presents without verified authority (unsigned board
   resolution, expired POA, contested estate administrator appointment).
5. Matter description triggers a mandatory SAR filing threshold under
   applicable AML rules before the engagement can lawfully proceed.

In each case, document the halt reason in the intake record and do not
generate an engagement letter.

## When to Apply

Apply this skill at the intake threshold — the first structured contact
at which a prospective client discloses matter facts. Scope includes:

- Initial consultation qualification calls and web-form intakes
- Conflict database queries triggered by a new matter or new adverse party
- Engagement letter drafting and fee agreement authoring
- KYC/AML risk-rating and PEP/sanctions screening for new matters
- Capacity and authority verification for individual and entity clients
- Re-engagement of former clients on a new matter (new conflict query
  required even if the client previously cleared)

Do not apply for internal administrative tasks that carry no client PII
and no conflict exposure.

## PII Handling

Client intake collects the highest-density PII in the legal engagement
lifecycle. All intake operations must observe the following controls:

**Collected categories and minimization rule:**
- Full legal name, aliases, government-issued ID number, date of birth
  (identity verification; collect only what the jurisdiction's KYC regime
  requires — do not collect passport and national ID simultaneously unless
  the matter risk-rating requires dual-document verification)
- Contact address, phone, email (communication channel discipline — see
  Attorney-Client Privilege Establishment)
- Financial information: source-of-funds declaration, beneficial-ownership
  chain for entities, trust deposit details (collect only for matters
  where fee structure or AML rules require it)
- Matter facts: incident dates, transaction amounts, adverse party
  identities, prior legal action records (collect only what is necessary
  to complete the conflict query and draft the engagement scope)
- Adverse party information: names, entity identifiers, counsel if known
  (required for conflict query; do not collect financial or personal data
  about adverse parties beyond what the conflict query demands)

**Transmission:** intake forms must use encrypted channels (TLS 1.2+);
verbal intake via phone must be recorded only with explicit consent per
applicable wiretap law; email intake must warn the prospective client
that unencrypted email is not a privileged channel until an engagement
letter is signed.

**Retention:** matter file is retained per the firm's retention schedule
anchored to the applicable limitation period for the practice area plus a
minimum seven-year floor. For declined or referred matters, retain only
the conflict record (party names, matter type, declination date) and
destroy substantive intake notes per the destruction schedule. Document
the destruction.

**Deletion on declination:** when the firm declines representation, purge
all PII beyond the conflict record within 30 days of the declination
letter. Log the purge in the intake audit trail.

**Cross-border note:** if the prospective client is located in Brazil or
the matter involves Brazilian data subjects, `core/compliance-lgpd`
governs PII processing on top of this skill. Document the LGPD legal
basis for intake data collection (typically Art. 7, VI — legitimate
interest in assessing the professional relationship) in the data
processing registry before the first intake session.

## Conflict Screening

Conflict screening must run against the firm's conflict database BEFORE
any consultation is scheduled and BEFORE any substantive matter facts
are disclosed to an attorney.

**Query inputs (collect before running query):**
- Prospective client: full legal name + all known aliases + entity name
  and jurisdiction if corporate
- Matter type and opposing party: full legal name of every adverse party
  identified so far (the query runs again if new adverse parties emerge
  mid-representation)
- Prior relationship: whether the prospective client or any disclosed
  adverse party has previously retained the firm in any capacity

**Conflict categories:**

| Category | Trigger | Disposition |
|---|---|---|
| Direct conflict | Firm currently represents an adverse party in this or a substantially related matter | BLOCK — cannot accept without withdrawal + all-party waiver |
| Former-client conflict | Firm previously represented an adverse party in a substantially related matter | BLOCK unless waiver obtained per ABA MR 1.9 / OAB Art. 18 |
| Positional conflict | Firm argues legally inconsistent positions in simultaneous matters | Escalate to supervising partner for authorization |
| Advance waiver | Written, informed waiver signed before representation begins | CLEARED with waiver on file |
| No conflict | No database match on any party | CLEARED — document query timestamp |

**OAB Cód. Ética anchor (Brazil):** Arts. 15, 16, and 18 govern conflict
obligations. Art. 15 prohibits representing parties with opposing
interests in the same proceeding. Art. 18 restricts former-client matters
using confidential information. Advance waivers are permitted only where
both parties give informed, written consent after full disclosure.

**ABA Model Rules anchor (US):** Rules 1.7 (concurrent), 1.9
(former-client), and 1.10 (imputation within a firm). Consult applicable
state court's professional conduct rules for jurisdiction-specific
deviations.

**Running the query:** submit query to conflict database with all party
names before any consultation is booked. Document: query timestamp,
parties queried, result (CLEARED / CONFLICT / POTENTIAL-CONFLICT /
PENDING), and reviewer sign-off. Never move to the next intake step
until CLEARED appears in the record.

## Capacity Assessment

Verified capacity and authority to retain counsel is a prerequisite for
a binding engagement agreement.

**Individual clients:**
- Decisional capacity: the prospective client must understand the nature
  of legal representation, the scope of the matter, and the fee
  obligation. If capacity is in doubt (cognitive impairment, acute crisis,
  intoxication), pause intake and schedule a follow-up; do not proceed on
  a telephone intake alone.
- Minor representation: a minor cannot execute an engagement letter.
  Identify the legal guardian, verify guardianship documentation, and
  confirm the guardian's authority extends to legal proceedings on the
  minor's behalf.
- Guardianship / conservatorship: verify the court order appointing the
  guardian and confirm it has not been superseded or challenged.

**Entity clients:**
- Corporate authority: obtain board resolution or written authorization
  from the corporate secretary confirming the signatory has authority to
  bind the entity to legal representation and fee obligations.
- Partnership authority: verify the partnership agreement grants the
  signing partner authority to retain outside counsel.
- Trust: obtain the trust instrument and verify trustee authority to
  engage counsel on trust matters; confirm the trust is not under active
  court supervision that limits trustee authority.
- Insolvency and restructuring: if the entity is in bankruptcy,
  receivership, or under an administrator's control, verify that the
  trustee, receiver, or administrator (not former management) is the
  authorized principal. Former management has no authority to retain
  counsel on behalf of the estate without court approval.

Document the authority verification in the intake record with copies of
the authorizing instrument retained in the matter file.

## Scope of Engagement

The engagement scope is the written boundary of the attorney-client
relationship. Scope ambiguity is the primary driver of fee disputes and
malpractice claims.

**Scope decision matrix:**

| Representation type | Use when |
|---|---|
| Full representation | Client retains counsel for all aspects of the matter through resolution |
| Limited scope (unbundled) | Client retains counsel for a defined discrete task (e.g., contract review only; single hearing appearance) — disclose limitations and confirm client understands attorney will not monitor related issues |
| Advisory only | Counsel provides legal analysis without appearing or filing — no attorney of record status |

**Scope document requirements:**
1. Identify the specific legal matter (proceeding, transaction, or
   advisory question) with enough specificity that a future court or
   disciplinary tribunal can determine what was and was not covered.
2. Carve out explicitly any related or adjacent matters the firm is NOT
   handling (e.g., "This engagement covers the commercial lease dispute
   at [address] only; related employment claims are outside scope").
3. State the geographic and jurisdictional limits of the representation.
4. State the temporal scope: does the engagement terminate on a specific
   event (e.g., execution of settlement agreement), or does it require a
   written termination notice?
5. For limited-scope representations, include an explicit unbundled-
   services disclosure per applicable jurisdiction ethics rules.

**Scope expansion:** any expansion of scope beyond the original
engagement letter requires a written amendment signed by the client
before the additional work begins. Verbal scope expansion is not binding
and exposes the firm to unpaid fee disputes.

## Fee Agreement

Fee agreements are required to be in writing in most jurisdictions before
work commences. Oral fee agreements are an anti-pattern (see
Anti-Patterns table).

**Fee structures:**

| Structure | When appropriate | Ethics anchors |
|---|---|---|
| Hourly | Complex litigation, corporate transactional work, advisory mandates | Billing rate, time-keeping increment, and billing frequency must be stated; OAB Art. 35 / ABA MR 1.5(a) reasonableness standard applies |
| Contingency | Personal injury, consumer protection, select employment matters | Percentage must be stated for pre-settlement, post-settlement, and post-trial outcomes separately; prohibited in criminal defense and domestic relations in most jurisdictions per ABA MR 1.5(d) |
| Flat fee | Document drafting, will preparation, trademark registration, routine immigration petitions | Specify whether flat fee is earned-on-receipt or refundable pro-rata; billing disputes hinge on this distinction |
| Hybrid | Complex litigation with unpredictable resolution path | Document the split clearly (e.g., reduced hourly + 15% contingency on recovery above threshold) |

**Trust deposit (IOLTA / client account):**
- State the deposit amount required before work commences.
- Confirm the deposit is held in a jurisdiction-compliant client trust
  account (IOLTA in the US; OAB trust account rules in Brazil).
- State the draw-down frequency and the obligation to provide a
  contemporaneous billing statement on each draw.
- Replenishment threshold: state the balance below which the client must
  replenish the deposit to avoid suspension of representation.

**Jurisdictional compliance:**
- Brazil: OAB Tabela de Honorários provides minimum fee guidance per
  practice area and procedural act; below-table fees must be justified
  and documented.
- US: ABA Model Rule 1.5 governs reasonableness; check state rules for
  mandatory fee agreement writing requirements (California, Texas, and
  others impose statutory requirements for written agreements in specific
  matter types).

## Identity and AML/KYC

Identity verification and AML/KYC screening apply at the engagement
opening, regardless of matter type, in regulated legal-services
jurisdictions. Even in non-regulated jurisdictions, AML risk awareness
is professional-responsibility best practice for matters involving
significant asset transfers.

**Identity verification steps:**
1. Collect government-issued photo ID (passport, national identity card,
   or equivalent); for entities, collect certificate of incorporation,
   current registered-office confirmation, and beneficial-ownership
   declaration.
2. Verify the ID is current and not expired.
3. For remote intake, use a compliant video-ID or e-KYC service that
   produces an audit trail; do not accept unwitnessed self-certified
   scans as sole verification on high-risk matters.

**PEP screening:** query the prospective client and all disclosed
beneficial owners against:
- OFAC SDN List (US nexus matters)
- UN Security Council Consolidated List (universal)
- EU Consolidated Financial Sanctions List (EU nexus)
- Brazilian COAF / Receita Federal watchlists (Brazil nexus)

A PEP match does not automatically block engagement but triggers enhanced
due diligence: document source of funds, beneficial-ownership chain to
the natural person level, and obtain partner-level sign-off before
accepting the engagement.

**FATF risk-rating:** assign a risk rating (Low / Medium / High) per the
FATF risk-based approach:

| Factor | Elevated risk indicators |
|---|---|
| Client type | PEP, shell company, bearer-share entity, cash-intensive business |
| Matter type | Real estate purchase, M&A, trust formation, cross-border asset transfer |
| Geography | High-risk or high-secrecy jurisdiction per FATF / BCBS greylist |
| Transaction size | Above AML reporting threshold for the jurisdiction |

**SAR triggers:** file a Suspicious Activity Report (FinCEN in the US /
COAF in Brazil) if the matter facts, after engagement, reveal reasonable
grounds to suspect money laundering or terrorist financing. Legal
privilege does not shield the attorney from SAR filing obligations where
applicable law requires disclosure. Document the tipping-off prohibition:
the client must not be notified that a SAR has been filed.

## Attorney-Client Privilege Establishment

The engagement letter is the privilege anchor. Privilege attaches to
communications made in confidence for the purpose of seeking legal
advice. The intake process must establish the channel discipline before
the first privileged communication occurs.

**Engagement letter as privilege anchor:**
- Sign and date the engagement letter before discussing substantive
  matter strategy or legal analysis.
- The letter must identify the attorney-client relationship, confirm
  confidentiality, and state the scope of representation.
- For prospective clients who are not yet retained, intake communications
  are protected as prospective-client communications under ABA MR 1.18 /
  OAB Art. 7, §2; document this status explicitly in the intake record.

**Communication channel discipline:**
- Designate a specific channel for privileged communications (firm email
  domain, secure client portal, or encrypted messaging service).
- Warn the client in the engagement letter that communications via
  personal, unencrypted email or social media may not be protected.
- Document the agreed channel in the intake record; flag any future
  communications received outside the agreed channel for client
  notification.

**Privileged vs. non-privileged classification:**

| Communication type | Privileged |
|---|---|
| Client describes facts to attorney for legal advice | Yes |
| Attorney's legal analysis and recommendations | Yes |
| Underlying business documents attached to privileged email | No (document itself is not privileged merely by transmission to attorney) |
| Intake intake forms submitted before engagement letter | Protected as prospective-client communication |
| Communications forwarded to non-attorney third parties | Waiver risk — advise client before forwarding |
| Communications in furtherance of a crime or fraud | Not privileged — crime-fraud exception |

**Work-product doctrine:** distinguish attorney-client privilege
(protects confidential client communications) from work-product doctrine
(protects attorney mental impressions and litigation preparation). Both
protections must be invoked separately and logged when privilege is
asserted in discovery.

## Anti-Patterns

| Anti-pattern | Risk | Correct practice |
|---|---|---|
| Scheduling consultation before conflict check completes | Disqualification; malpractice; disciplinary proceedings | Run conflict query on all party names before any appointment is booked |
| Oral fee agreement only | Unpaid fee disputes; billing complaints; ethics violation in jurisdictions requiring written agreements | Execute signed written fee agreement before work commences |
| Scope creep without written amendment | Client disputes additional fees; malpractice for work outside scope | Draft and sign scope amendment before beginning additional work |
| Ignored capacity flags | Voidable engagement agreement; guardianship dispute; malpractice | Pause intake; verify capacity with supervising attorney; document resolution |
| Collecting PII beyond KYC minimization | LGPD / GDPR violation; data subject complaints; regulatory fine | Collect only the identity fields the jurisdiction's KYC regime requires for the matter risk level |
| SAR filed without tipping-off analysis | Criminal liability for the attorney if client is notified | File SAR; review tipping-off prohibition before any client communication post-filing |
| Engagement letter without channel designation | Privilege waiver risk for out-of-channel communications | State the designated privileged channel in the engagement letter |
| Re-engaging former client without new conflict query | Former-client conflict under ABA MR 1.9 / OAB Art. 18 missed | Run full conflict query on new matter and new adverse parties; prior CLEARED status does not carry forward |

## Cross-References

- `core/compliance-lgpd` — LGPD legal basis for intake PII processing,
  data subject rights obligations, and breach notification if intake
  records are exposed
- `domains/legal/skills/document-review` — privilege log preparation
  and document-by-document privilege classification during discovery
- `domains/legal/skills/legal-billing` — billing statement format,
  trust account draw-down procedures, and IOLTA reconciliation

## ADR Anchors

- **ADR-058** — two-pass adversarial review doctrine: all intake
  deliverables (engagement letters, fee agreements, conflict reports)
  undergo a second-pass review by a supervising attorney before execution;
  intake specialist output is a draft, not a final instrument
