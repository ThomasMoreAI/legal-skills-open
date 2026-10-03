# DSAR / Consumer Rights Request Routing

**Purpose.** A workflow for handling an incoming consumer rights request when the user asks "we got a request from a consumer in [state] — what do we do?" Routes by residency, the right invoked, and the controller's status under the applicable law.

## Step 1 — Identify the requester's state of residency

The applicable law is determined by where the consumer resides, not where the controller is located, not where the request comes from, and not where any data is stored. A California resident traveling in Europe still has CCPA rights against a California-business controller.

Verifying state of residency: address on record; declaration in the request; IP-based estimate (weak); existing account information. If residency cannot be verified, treat the request under the most consumer-protective applicable law.

## Step 2 — Confirm controller is subject to that state's law

Run threshold analysis (`references/applicability-matrix.md`). If the controller is not subject to the state's comprehensive privacy law, the request need not be honored under that statute — but consider:

- **State-specific data-broker law applicability** (CA, TX, OR, VT).
- **Sectoral overlay** (HIPAA, GLBA, FCRA, COPPA may impose obligations regardless of the comprehensive privacy law).
- **Federal CAN-SPAM, TCPA** for marketing-related opt-outs.
- **Voluntary response posture**: some controllers honor rights requests from non-applicable states as a matter of policy. This is fine, but document the discretionary nature.

If the controller is subject, proceed.

## Step 3 — Determine controller's status for the data at issue

Same data may be subject to different obligations depending on whether the controller acts as **business / controller** or as **service provider / processor** for that data flow.

- **As controller**: the obligation runs to the consumer. Honor the request directly per the state's procedures.
- **As processor**: the obligation runs to the controller (the customer who hired the processor). Forward the request to the controller; do not act on it directly. The processor's contractual obligations require assistance to the controller in fulfilling consumer requests.

Many SaaS B2B controllers are dual-status (controller for marketing/account data, processor for customer-end-user data). Route accordingly per data flow.

## Step 4 — Verify the requester

Verification standards vary by state but converge on "reasonably calculated to ensure the requester is the consumer about whom the data relates."

| Request type | Typical verification |
|---|---|
| Categories-only access | Match account email/phone; modest verification |
| Specific-pieces access | Two-factor or stronger; account login + secondary attestation |
| Deletion (account-level) | Account login + confirmation step |
| Deletion of sensitive data | Stronger verification — content of communications, government IDs, biometric data warrant heightened verification |
| Correction | Match account; verify identity; verify accuracy of correction |

**California** (CCPA Regs § 7060 et seq.) provides the most prescriptive guidance; reasonable practice is to align verification across states to CA standards.

**Authorized agents**: where permitted (CA broadly; CO/CT for opt-out only), verify the agent's authorization and (optionally) verify with the consumer directly that they authorized the agent.

## Step 5 — Address the specific right invoked

### Access / Right to Know

What to provide:
- Categories of PD processed.
- Specific pieces of PD (subject to verification level and sensitivity).
- Categories of sources from which PD was collected (CA-specific requirement; good practice elsewhere).
- Purposes for processing.
- Categories of third parties to whom PD has been disclosed.

Some states (OR, MN) require **specific third parties**, not categories — significantly higher operational lift.

CA-specific: The business may decline to provide certain information (e.g., SSN, account credentials, financial account numbers, government IDs not collected for purposes that include providing them) for security reasons, but must inform the consumer that the information is being withheld with sufficient particularity.

Format: machine-readable for portability requests; readable format otherwise.

### Deletion

Identify all systems where the consumer's PD is held: production database, backup, analytics warehouse, CRM, email marketing platform, support ticketing, customer success tooling, third-party processor copies.

Delete or de-identify per the state's standard. CA and most states require **direction to processors** to delete the data they hold on behalf of the controller (this is what the processor contract should already address).

Exceptions to deletion (most states):
- Necessary to complete the transaction the consumer requested.
- Detect security incidents, protect against malicious activity, prosecute those responsible.
- Fix errors that impair functionality.
- Exercise free speech, ensure the right of another consumer.
- Comply with legal obligations (e.g., SEC retention, tax retention, healthcare records retention).
- Use for solely internal use reasonably aligned with consumer expectations.
- Comply with legal obligations.

Document the exception relied on for each non-deleted data element.

### Correction

Identify the data element(s) the consumer asserts are inaccurate. Apply a "reasonable" standard to correction:
- Accept clear corrections (e.g., updated name after legal name change with documentation).
- For contested corrections, the controller may decline if the contention is not credible — but must explain why and provide appeal rights.

Note: UT, IA, KY do not provide a correction right. A request from a UT/IA/KY resident solely for correction need not be honored under state comprehensive privacy law.

### Portability

Provide the PD in a portable, structured, commonly-used, machine-readable format. JSON, CSV, or XML are typically acceptable. Avoid PDF for portability requests — not machine-readable in a useful sense.

### Opt-out of sale, sharing, targeted advertising, profiling

- **Opt-out of sale**: stop selling the consumer's PD. Notify downstream third parties to whom data was sold of the opt-out.
- **Opt-out of sharing** (CA): stop disclosing PI for cross-context behavioral advertising.
- **Opt-out of targeted advertising** (most other states): stop using the consumer's PD to display targeted ads.
- **Opt-out of profiling**: stop subjecting the consumer to profiling that produces legal or similarly significant decisions.

Persist the opt-out across the consumer's devices and accounts. Do not require the consumer to repeat the opt-out for each property or session.

### Limit Use of Sensitive PI (CA-only)

Restrict use of sensitive PI to that necessary to perform the services or provide the goods reasonably expected by the consumer. Excludes:
- Helping ensure security and integrity.
- Detecting and resisting malicious or fraudulent actions.
- Resisting illegal actions directed at the business.
- Short-term, transient use.
- Performing services on behalf of the business (e.g., maintaining accounts, providing customer service, processing orders, processing payments).
- Verifying or maintaining the quality of the service.

## Step 6 — Respond within the statutory window

| State | Initial response | Extension |
|---|---|---|
| Most states | 45 days | +45 days with notice |
| Iowa | 90 days | +45 days with notice |
| FL | 45 days | +15 days with notice |

Acknowledge receipt promptly (10 days is typical guidance, particularly under CCPA Regs).

Track and document:
- Date of receipt.
- Verification steps and outcome.
- Date of response.
- Disposition (granted in full, granted in part, denied — with reasons).
- Appeal information provided (if applicable).

## Step 7 — Handle appeals

States providing an appeal right require the consumer to be informed of the appeal procedure when a request is denied. Appeal windows: typically 45–60 days from the consumer's submission of the appeal.

If the appeal is denied at the controller level, the controller must provide the consumer with means to contact the AG (or equivalent regulator). VA, CO, and several others impose this requirement explicitly.

CA does not have a formal appeal right (CPPA-level mechanisms exist for complaints).

## Step 8 — Decline the request only on a documented basis

A request may be declined if:
- The requester cannot be reasonably verified.
- The request is manifestly unfounded, excessive, or repetitive.
- An exception applies (e.g., deletion exception for legal obligation).
- The data does not exist or is not subject to the relevant statute.

Document the basis for declination. Communicate it clearly to the consumer with the appeal procedure (where applicable).

## Special routing scenarios

### Authorized agent request

Verify the agent's authorization. Optionally verify with the consumer directly. Process as if from the consumer.

### Request from a parent for a minor

For under-13: COPPA's parental review and deletion right governs. Honor.

For 13+: state laws vary. Generally the minor consumer holds the right; parental requests may be processed if the parent is a verified guardian. Document.

### Request from an attorney

Attorney representations are permissible — process as agent of the consumer. Verify representation.

### Request via a broker / privacy-rights-platform

CA has multiple authorized-agent platforms (Permission Slip, Mine, etc.). Process per the agent procedure. Multi-consumer batch requests are increasingly common; confirm the controller's intake supports them.

### Request after a data breach

Sensitive context. Coordinate with breach response. Be especially careful about deletion requests during an investigation — preservation obligations may temporarily override deletion duties (document carefully).

### Request crossing multi-state coverage

A consumer with documented residence in multiple states (rare but happens) — process under the most consumer-protective applicable law.

## Documentation

Maintain a rights-request log. For each request:
- Receipt date, channel, content.
- Requester's identifier, residency.
- Verification steps and outcome.
- Routing decision (controller vs. processor; applicable state law).
- Right invoked.
- Action taken or basis for declination.
- Appeal information (if applicable).
- Response date.
- Final disposition.

This log supports response-time metrics, audit, and (in CA, for large-volume businesses) annual public disclosure (CCPA Regs § 7102).

## Common errors in DSAR handling

1. **Defaulting to "we'll honor it" without checking applicability or status**. Generates work and exposure on data the controller doesn't actually hold or for consumers in non-applicable states.
2. **Excessive verification** that effectively denies access. CCPA Regs § 7060 cautions against this; *Honda* settlement specifically addressed it.
3. **Treating a deletion request as an opt-out** or vice versa. They are different rights with different scope.
4. **Not propagating to processors**. The processor contract should require deletion on directive; failing to issue the directive leaves the data in place.
5. **Missing the response window**. The single most common documented violation. Build a tracker.
6. **Ignoring the appeal right**. Where it exists (most states), the denial must include the appeal procedure.
