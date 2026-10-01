# SOC 2 Type II Report Review — Analyst Methodology

## Report anatomy (AICPA structure)
1. **Independent Service Auditor's Report** — the opinion. Unqualified = controls suitably designed AND operated effectively over the period. Qualified = one or more criteria not met; read the basis-for-qualification paragraph and decide whether the failure touches the service you consume. Check the **period** (Type II covers a span, commonly 6 or 12 months; Type I is a point in time — far weaker assurance) and the **trust services categories** in scope (Security/common criteria always; Availability, Confidentiality, Processing Integrity, Privacy only if elected).
2. **Management's Assertion** — management owns the description and control claims.
3. **System Description** — verify the product/service and infrastructure YOU consume is inside the described system boundary; watch for descriptions covering only one product line or data center.
4. **Description of tests and results** — the exceptions live here. For each: what failed, sample size, auditor's noted cause, and whether it maps to a criterion relevant to you.
5. **Other Information** (unaudited) — management responses/remediation claims. Useful, not assured.

## Subservice organizations
- **Carve-out method** (most common): the subservice org's controls are excluded from description and testing. The report must disclose **CSOCs** — Complementary Subservice Organization Controls the service org ASSUMES operate at the carved-out provider. Analyst duty: identify carved-out providers (typically the cloud/hosting layer) and obtain THEIR assurance reports separately.
- **Inclusive method**: subservice org controls included and tested — rare, stronger.
- Management must monitor subservice orgs under either method (AICPA guide) — ask how.

## CUECs — Complementary User Entity Controls
Controls the CUSTOMER must operate for the vendor's control environment to achieve its objectives (e.g., "user entities are responsible for provisioning and deprovisioning their users," MFA enablement, configuring retention). Extract every CUEC into a checklist, assign an internal owner, and verify implementation — an unowned CUEC is an audit finding waiting on YOUR side.

## Exception triage
For each exception: (1) which criterion and control; (2) relevant to the service you consume? (3) systemic (design) or isolated (operating, small sample miss)? (4) management response and remediation date; (5) compensating controls on your side. Roll up to a verdict: accept / accept-with-conditions (contractual commitments, follow-up evidence) / reject.

## Coverage gaps and bridge letters
If the report period ended more than ~3 months ago, request a **bridge (gap) letter**: issued by the SERVICE ORGANISATION'S MANAGEMENT (never the auditor — auditors cannot attest to untested periods), stating whether material changes to the control environment occurred since period end. Reasonable coverage is up to ~3 months; a bridge letter is a representation, not assurance. A report older than ~15 months with no successor in flight is a red flag.

## Quick red-flag list
Qualified opinion touching your service; Security-only scope when you need availability commitments; your product absent from the system description; carve-out of the entire hosting layer with no subservice assurance; >5 exceptions in access management; no CUEC section (suggests a thin report); Type I offered where Type II expected; refusal to provide the full report (accepting only a "letter of attestation").
