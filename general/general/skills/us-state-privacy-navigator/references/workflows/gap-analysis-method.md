# Gap Analysis Methodology

**Purpose.** A standardized scoring framework for identifying, prioritizing, and sequencing remediation of state privacy law gaps. Applies after applicability triage and status determination.

## Method overview

For each applicable state law, walk through `references/controller-duties.md` and the relevant `states/<xx>.md` and compare each statutory duty to current practice. For each gap, assign a **Severity** (1–5) and a **Likelihood** (1–5). Multiply for a **Score** (1–25). Bucket Scores into priority lanes. Sort within lanes by dependency.

## Severity (1–5)

Severity reflects the regulatory and litigation exposure if the gap is challenged. Anchor against:

- **Statutory penalty cap and per-violation cumulation** in the applicable state(s).
- **Whether a private right of action exists** (CA data-breach PRA, BIPA-style biometric exposure, MHMDA in WA).
- **Cure availability and AG enforcement priorities** in the state.
- **Number of states implicated** by the same gap (e.g., a missing privacy notice section impacts most states).

| Score | Description | Examples |
|---|---|---|
| 1 — Minimal | Documentation polish; no regulator would prioritize. | Slight formatting inconsistency in privacy notice; minor typo in disclosure. |
| 2 — Low | Discrete violation in a state with low penalty exposure or strong cure protection. | Missing appeal-process language in IA notice; outdated effective date in privacy policy. |
| 3 — Medium | Substantive gap creating exposure in 1–3 states; modest penalty cap; some defensibility. | Failing to provide a state-specific opt-out method; missing data-protection-assessment for a specific borderline activity. |
| 4 — High | Substantive gap creating exposure in multiple states or in CA/TX/FL specifically; clear AG enforcement priority; or PRA-adjacent. | No "Do Not Sell or Share" link; failure to recognize GPC; sensitive-data processing without consent; processor contracts missing required terms. |
| 5 — Critical | Multi-state systemic gap; PRA exposure; AG-enforced violation pattern; or directly contrary to a state-specific flat ban. | Sale of sensitive data in MD; sale or targeted ads of known minors in MD; data breach without reasonable security creating CA PRA exposure; biometric processing without BIPA consent. |

## Likelihood (1–5)

Likelihood reflects the probability that a regulator, plaintiff, or consumer surfaces the gap. Anchor against:

- **Visibility**: is the gap externally observable (e.g., missing link on website, GPC handling failure)?
- **Volume**: does the practice happen frequently enough to attract complaints (e.g., consumer-facing rights-request handling, cookie consent flows)?
- **Plaintiff ecosystem**: is there an active plaintiffs' bar (e.g., BIPA, CIPA, VPPA, CCPA data-breach)?
- **AG enforcement priorities**: has the relevant AG signaled focus on the area?

| Score | Description | Examples |
|---|---|---|
| 1 — Remote | Unlikely to surface; internal-only gap; non-visible. | Minor processor-contract drafting issue with a low-risk vendor; documentation gap with no external manifestation. |
| 2 — Low | Could surface in audit but unlikely to draw spontaneous attention. | Missing internal record of a specific DPA for an activity unlikely to draw scrutiny. |
| 3 — Medium | May surface in routine compliance review, customer due-diligence question, or random consumer complaint. | Stale privacy notice not reflecting current practice; marketing email opt-out lag. |
| 4 — High | Likely to surface. AG enforcement priority. Externally visible to motivated parties (plaintiffs, regulators, advocacy groups). | Missing "Do Not Sell" link visible on landing page; CMP not handling GPC; rights-request response time exceeding statutory deadlines. |
| 5 — Near-certain | Externally visible and being actively scrutinized; PRA-adjacent; or direct AG investigation indicators. | Operating biometric-data system without BIPA consent (active class-action area); session-replay tools subject to CIPA litigation; sale of sensitive data subject to active AG sweeps. |

## Score = Severity × Likelihood

| Range | Bucket | Default lane |
|---|---|---|
| 1–6 | Low | >90 day / strategic |
| 7–12 | Medium | 31–90 day |
| 13–19 | High | 0–30 day |
| 20–25 | Critical | Immediate |

## Lane assignments — operational sequencing

### Immediate (within 7 days, where feasible)

Critical-bucket gaps that create active exposure. Examples:

- Stop processing sensitive data of MD residents for sale (per MD flat ban) — a flat ban does not have a remediation runway.
- Stop processing PD of known minors for targeted advertising in MD.
- Suppress data-broker-data sales pending registration where required.
- Pause an enforcement-attracting feature (e.g., a session-replay tool subject to active CIPA litigation) pending review.

### 0–30 days

High-bucket gaps. Typically:

- Add missing notices, links, and opt-out methods (Do Not Sell, Limit Use of Sensitive PI, etc.).
- Configure CMP to recognize GPC.
- Update privacy notice to address missing required content.
- Implement state-specific consent flows for sensitive data.
- Suppress non-compliant pixels on logged-in pages.

### 31–90 days

Medium-bucket gaps and dependencies. Typically:

- Update processor / service-provider contracts to meet state-specific requirements (CCPA Regs § 7051, etc.).
- Conduct or update data protection assessments for high-risk activities.
- Build an authorized-agent verification workflow.
- Document the privacy program in writing (TIPA affirmative defense, CT cure-period prerequisite, etc.).
- Implement rights-request workflow with response-time tracking.

### >90 days / strategic

Low-bucket gaps and structural projects. Typically:

- Data inventory / data mapping (often a precursor to many higher-priority items).
- Vendor inventory and DPA refresh project.
- Privacy training program.
- Privacy-by-design integration into product lifecycle.
- Pursuing TIPA NIST PF affirmative-defense documentation.
- Strategic platform changes (e.g., re-architecting analytics for opt-out compliance).

## Dependencies

Surface and document dependencies. Common patterns:

- **Privacy notice update** depends on **data inventory** (you can't accurately disclose categories until you've inventoried them). If the inventory is missing, the inventory itself becomes a 31–90 day item, and the notice update follows.
- **DPA refresh** depends on **vendor inventory**.
- **Risk assessments** depend on knowing what processing activities exist, which depends on the inventory.
- **GPC handling** depends on **CMP capabilities**, which may depend on **CMP replacement** (a 31–90 day project).

When dependencies require the lower-priority precursor to land first, the gap-analysis output must surface this — otherwise the user will sequence the work incorrectly.

## Cross-cutting prioritization

Beyond per-gap scores, certain gaps should be elevated due to cross-cutting impact:

1. **Single fix, multi-state benefit.** A privacy notice update that addresses missing required content under 8 statutes is higher-leverage than a CA-specific edge-case fix.
2. **Foundational data inventory.** Without a data inventory, multiple downstream items remain incompletable. Elevate to 31–90 days even if no individual gap demands it sooner.
3. **Documented program for affirmative defense (TN) or cure-period eligibility (MN, others).** The marginal cost is modest; the defensibility benefit is significant.
4. **CMP capability fix.** Resolves multiple gaps (GPC handling, consent specificity, dark-pattern audit, sensitive-data consent) in one project.

## Output format

Produce a gap log as a table:

| ID | State(s) | Statute Section | Gap | Current State | Required State | Severity | Likelihood | Score | Lane | Dependencies | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

Sort by Score descending. Group dependent items visually.

For executive readers, accompany with a narrative summary identifying the top 5 priorities and the cross-cutting fixes that resolve multiple gaps.

## Common gap-analysis errors

1. **Counting one gap per state for a single defect.** A missing "Do Not Sell" link is one issue, not 18. Mark the state(s) implicated; don't multiply.
2. **Over-scoring on visibility.** Visibility is one factor among several; a visible defect with a 30-day cure period is not necessarily Critical.
3. **Ignoring dependencies.** Listing a "0–30 day" item that depends on a "31–90 day" precursor without flagging the dependency creates an unworkable plan.
4. **Pretending the program is more mature than it is.** Honest gap analysis sometimes finds that the program is closer to "needs build" than "needs polish." Frame accordingly.
5. **Treating remediation as one-and-done.** Privacy programs degrade as the business changes. The output should include a recommended cadence for re-assessment (annually at minimum; more frequently with material business changes).
