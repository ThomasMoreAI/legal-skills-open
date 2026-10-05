---
name: legal-billing-canhada-labs
title: Legal Billing
description: 'Legal billing and time-tracking discipline for law firms and legal

  departments. Covers billable vs. non-billable classification, ABA Model Rule

  1.5 reasonableness factors, contemporaneous time entry requirements, UTBMS

  task-code mapping for litigation, expense pass-throughs, retainer lifecycle

  (true / replenishing / evergreen), trust and IOLTA client-funds segregation,

  jurisdictional fee-rule compliance (US state bars, EU bar associations, OAB

  Brazil), and billing anti-pattern detection. PII-touching: client matter

  data, adversary information, privileged communications, and work product are

  all personal or confidential data subject to legal professional privilege and

  data-protection law. Use when: classifying time entries for a matter invoice;

  reviewing trust account reconciliation; advising on fee arrangement structure;

  auditing billing narratives for ABA compliance; applying LGPD Art. 11

  controls to legal-sector data; or vetting expense pass-through ethics.'
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/domains/legal/skills/legal-billing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Legal Billing

## Cardinal Rule

Every time entry, invoice, and trust transaction must be accurate, honest, and
contemporaneous. ABA Model Rule 1.5 requires fees to be reasonable; Rule 1.15
requires client funds to be held inviolate. Neither rule admits exceptions for
administrative convenience, workload pressure, or revenue targets. A billing
decision that cannot survive bar disciplinary scrutiny must not be made.

## Fail-Fast Rule

Stop and escalate to the responsible attorney when any of the following is
detected:

- A time entry is being reconstructed from memory more than seven days after
  the work was performed — label it estimated-reconstruction and flag for
  attorney review before invoicing.
- A trust account disbursement would produce a negative client-ledger balance
  — reject and require source-of-funds clarification first.
- Block billing appears on a matter whose client guidelines explicitly prohibit
  it — hold the invoice and require entry decomposition.
- A fee agreement for a contingency arrangement is not confirmed in writing
  before the matter proceeds — oral contingency arrangements are unenforceable
  in most jurisdictions.
- Personally identifiable data from a client matter is being transmitted,
  stored, or shared outside encrypted channels — halt and apply the PII
  controls below before proceeding.

## When to Apply

Apply this skill when:

- Classifying individual time entries as billable, non-billable, or write-down
  candidates under ABA Rule 1.5 reasonableness factors.
- Drafting or reviewing billing narratives for specificity and professional
  ethics compliance.
- Designing or auditing IOLTA / trust account procedures, including three-way
  monthly reconciliation.
- Structuring a fee arrangement (hourly, flat, contingency, hybrid) or advising
  on retainer replenishment thresholds.
- Evaluating expense pass-through eligibility and markup ethics.
- Applying jurisdictional fee-rule compliance for US state bars, EU bar
  associations, or OAB Brazil.
- Auditing a billing system for PII exposure risk or cross-border data-transfer
  compliance under LGPD Art. 11 or GDPR Art. 9.

Do not apply when the task is general accounts-receivable management outside a
legal context — use `domains/finance-accounting/skills/bookkeeper-controller`
for that.

## PII Handling

Legal billing data is inherently PII-dense and may carry legal professional
privilege. The following controls are mandatory.

**Data categories and classification:**

| Category | Classification | Legal basis required |
|---|---|---|
| Client name, address, matter description | Personal data | LGPD Art. 7 / contract |
| Adversary identity, case strategy, work product | Confidential + privileged | Legal privilege + LGPD Art. 7 |
| Settlement amounts, financial terms | Confidential personal data | LGPD Art. 7 / contract |
| Privileged communications (email, memo, call notes) | Legal privilege + personal data | Legal privilege; restrict access strictly |
| Time entry narratives referencing third parties | Personal data (third party) | LGPD Art. 7 / legitimate interest |
| Trust account balances and transaction records | Financial personal data | LGPD Art. 7 / legal obligation |

**Mandatory controls:**

- Never transmit client matter data over unencrypted channels (plain email,
  HTTP, unencrypted file share). Use end-to-end encrypted legal portals or
  TLS-in-transit with at-rest encryption.
- Retention schedules must be matter-type-specific: active matters — retain
  for the duration plus the applicable limitation period (varies by
  jurisdiction; minimum seven years in most US states; OAB Brazil resolves
  to five years post-matter-close); trust transaction records — retain for
  the full limitation period applicable to bar disciplinary proceedings.
- LGPD Art. 11 sensitive-category analysis: health information appearing in
  personal-injury or workers'-compensation billing narratives, racial or
  ethnic origin in discrimination matters, and religious affiliation in
  estate-planning context are sensitive personal data. Processing requires
  explicit legal basis beyond the general Art. 7 list; consent or legal-
  obligation bases are typical. Document the basis in the data-processing
  registry.
- Cross-border transfer of client matter data (e.g., cloud billing platform
  hosted outside Brazil) requires a valid transfer mechanism under LGPD Art.
  33: adequacy decision, standard contractual clauses, or explicit client
  consent. Verify transfer mechanism at platform onboarding, not after.
- Access control: billing personnel access must be scoped to matters they
  administer. Role-based access with audit logging. No bulk export without
  attorney approval and logged justification.
- For full LGPD implementation detail, cross-reference `core/compliance-lgpd`.

## Billable Classification

**ABA Model Rule 1.5 reasonableness factors** (applied as a classification
checklist before entry approval):

1. Time and labour required; novelty and difficulty of the questions involved.
2. Likelihood that acceptance of the engagement precludes other employment.
3. Customary fee in the locality for similar legal services.
4. Amount involved and results obtained.
5. Time limitations imposed by the client or circumstances.
6. Nature and length of the professional relationship with the client.
7. Experience, reputation, and ability of the attorney performing the work.
8. Whether the fee is fixed or contingent.

**Non-billable taxonomy:**

| Category | Examples | Disposition |
|---|---|---|
| Firm overhead | Rent, IT infrastructure, malpractice insurance | Firm absorbs; never passed to client |
| Billing and collections admin | Preparing invoices, chasing payments | Non-billable unless fee agreement specifies |
| General training | CLE attendance unrelated to a specific matter | Non-billable |
| Duplicative work | Two attorneys attending a routine call with no division of labour | Write-down to single timekeeper |
| Excessive research on settled law | Basic research a competent practitioner would not bill | Write-down to reasonable time |
| Clerical tasks | Photocopying, filing, scheduling | Non-billable or billed at administrative rate if disclosed |

**Rounding ethics:** Round to the nearest 0.1-hour increment (six-minute
minimum). Rounding up consistently to the nearest 0.5 or 1.0 hour is an
ethical violation under Rule 1.5 and subject to fee arbitration.

**Block-billing restriction:** On any matter where client billing guidelines
or a court fee application prohibit block billing, each discrete task must
appear as a separate line entry with individual time. A single narrative
combining multiple tasks is permissible only where the guidelines explicitly
allow it and each constituent task is still described.

## Time Entry Discipline

**Contemporaneous capture requirement:** Time must be captured on the day
work is performed. Entries reconstructed from memory carry elevated dispute
risk and reduced ethical defensibility. The outer limit for reconstruction
without labelling is seven calendar days; beyond that, entries must be marked
estimated-reconstruction and reviewed by the responsible attorney before
invoicing.

**Narrative quality standard:** Each entry must answer three questions:
(1) what action was taken; (2) on what subject-matter or document; (3) to
what purpose or result. Entries that answer fewer than two of the three
questions are rejected and returned for revision before billing review.

**UTBMS task-code mapping (litigation matters):**

| Phase | Code range | Examples |
|---|---|---|
| Case assessment / development | L100-L190 | L110 fact investigation, L120 analysis |
| Pre-trial pleadings / motions | L200-L290 | L210 complaint, L230 motion to dismiss |
| Discovery | L300-L390 | L310 written discovery, L330 depositions |
| Trial preparation / trial | L400-L490 | L420 experts, L450 trial attendance |
| Appeal | L500-L590 | L510 appellate briefs |

Transactional, real estate, and estate-planning matters use the B-series
and P-series UTBMS codes respectively. Confirm the applicable code set with
the client billing guidelines at engagement inception.

**Matter-aware coding:** Each entry must be associated with the correct matter
number. Cross-matter time allocation (one activity spanning two matters) must
be split at entry time with separate entries for each matter; never apportion
retroactively via journal adjustment without attorney sign-off.

## Trust / IOLTA Accounting

**Segregation of client funds:** Client funds held in advance of earning, cost
advances, settlement proceeds pending distribution, and escrow must be
maintained in a dedicated trust account separate from the firm operating
account. Commingling — depositing firm funds into the trust account or using
client funds for firm expenses — is bar discipline misconduct in every
jurisdiction.

**Permitted trust-to-operating transfers:** Transfer of earned fees from trust
to operating occurs only after the fee is earned and the client has been
notified. Transfers in anticipation of earning fees are premature and
constitute commingling.

**Three-way monthly reconciliation requirement:**

1. Bank statement ending balance.
2. Sum of individual client-ledger balances (each client's sub-account).
3. Trust journal or system balance.

All three figures must agree. Any variance requires same-day investigation and
written explanation before the month closes. Unresolved variances are reported
to the supervising attorney immediately; they are not carried forward.

**Per-jurisdiction trust rules:** IOLTA rules in the United States are
state-specific: minimum-balance thresholds for separate vs. pooled accounts,
interest remittance schedules, and reporting obligations vary. EU bar
associations maintain client account rules under national professional-conduct
codes. OAB Brazil (Estatuto da OAB, Lei 8.906/1994, Art. 22 and Código de
Ética Art. 50) requires separate management of client advances. Verify the
operative rules at engagement inception; do not assume one jurisdiction's
rules apply to another.

## Expense Pass-Through

**Cost vs. charge distinction:** Pass-through expenses must represent actual
third-party costs incurred on behalf of the client. The recoverable amount is
the actual cost paid unless the fee agreement explicitly authorises a markup
and specifies the markup rate.

**Markup ethics:** Charging above actual cost for photocopying, courier
services, or computer-assisted research beyond what the fee agreement
authorises is subject to Rule 1.5 reasonableness analysis and, in some
jurisdictions, bar discipline. Disclose any markup in the fee agreement.

**Receipt retention:** Receipts or vendor invoices must be retained for all
pass-through expenses above the firm's threshold (minimum: receipts for
expenses above $25 USD-equivalent; recommended: all pass-throughs). Retention
period: same as matter-close retention schedule.

**Tax categorisation:** Distinguish between costs the firm advances as agent
(no revenue recognition; balance-sheet asset) and costs billed as firm
charges (revenue at billing). Mis-categorisation creates accounting and
tax-reporting errors. Coordinate with the bookkeeper-controller skill for
treatment within the firm's chart of accounts.

## Retainer Lifecycle

**Retainer type definitions:**

| Type | Mechanism | Depletion handling |
|---|---|---|
| True (classic) retainer | Lump sum paid to secure availability; earned on receipt | Non-refundable absent breach; held in operating account |
| Replenishing retainer | Client advance held in trust; replenished when balance falls below threshold | Replenishment notice sent at threshold; matter pauses if not replenished |
| Evergreen retainer | Replenishing retainer with automatic replenishment triggered by invoice | Client authorises automatic debit; agreement must specify amount and timing |

**Depletion tracking:** Replenishing and evergreen retainers require per-matter
trust-ledger tracking with balance-alert rules set at the replenishment
threshold. Invoices drawn against trust must simultaneously update the client
ledger and the trust reconciliation.

**Refund on termination:** On matter close or client-initiated termination, any
unearned retainer balance held in trust must be returned to the client promptly.
Failure to return unearned funds is commingling and a Rule 1.15 violation.

## Jurisdictional Compliance

Fee rules, billing guideline requirements, and trust account obligations are
jurisdiction-specific. The following is a mapping of operative sources; verify
current rules at engagement inception.

| Jurisdiction | Operative rules |
|---|---|
| US (state bar) | State Rules of Professional Conduct (Model Rule 1.5 + 1.15 as baseline); IOLTA rules published by state bar foundation; court-specific local rules for fee applications |
| EU / EEA | National bar association professional conduct codes; CCBE Code of Conduct for EU Lawyers (Arts. 3.3 and 3.4 on fees); GDPR Art. 9 for sensitive client data |
| OAB Brazil | Estatuto da OAB (Lei 8.906/1994); Código de Ética e Disciplina da OAB; LGPD (Lei 13.709/2018) for client data processing |

No rule in this skill supersedes the jurisdiction-specific operative rule. When
rules conflict, apply the stricter obligation and document the conflict.

## Anti-patterns

| Anti-pattern | Failure mode | Correction |
|---|---|---|
| Block billing on prohibited matters | Client guidelines or court rules disallow; invoice reduced or rejected | Decompose to discrete task entries before submitting invoice |
| Padded entries | Billing more time than actually spent; Rule 1.5 violation; bar discipline risk | Bill actual time only; reduce narrative-padded entries before approval |
| Commingling client funds | Trust balance used for firm operations or firm funds deposited in trust; Rule 1.15 violation | Immediate reversal; written explanation to supervising attorney; report if required by jurisdiction |
| Retroactive reconstruction beyond 7 days | Memory-based entries are inaccurate and dispute-prone; reduced credibility in fee arbitration | Label as estimated-reconstruction; attorney review gate before invoicing |
| Non-billable time on invoice | Overhead, billing admin, or purely clerical tasks billed to client; Rule 1.5 reasonableness failure | Classify against non-billable taxonomy; write off before invoice generation |
| Missing billing-guideline compliance check | Corporate or insurance client guidelines violated (minimum increments, prohibited codes, block billing); invoice rejected or reduced | Validate against client-specific guidelines as a mandatory pre-invoice gate |
| Unencrypted PII transmission | Client matter data in plain email or unencrypted storage; LGPD / privilege breach | Enforce encrypted channels; audit transmission logs; apply PII controls above |
| Oral contingency agreement | Unenforceable in most jurisdictions; fee recovery risk | Require signed fee agreement before matter proceeds; no verbal confirmation |

## Cross-References

- `core/compliance-lgpd` — LGPD legal bases, data-subject rights, breach
  notification, and cross-border transfer mechanisms for client data
  processing; this skill inherits and specialises those controls.
- `domains/legal/skills/client-intake` — conflict-of-interest checks, engagement
  letter requirements, and client identity verification; precedes billing
  engagement.
- `domains/finance-accounting/skills/bookkeeper-controller` — chart-of-accounts
  treatment of retainer advances, cost pass-throughs, and revenue recognition;
  coordinate for accounting entries that mirror trust-account transactions.

## ADR Anchors

- **ADR-058** — two-pass review gate; applies to all billing deliverables
  (invoice review, trust reconciliation, fee agreement structure) before
  client transmission or matter-file lodgement.
