---
name: merit-review
title: State Merit Review Analysis
description: Analyzes state merit review for non-covered securities offerings, applying NASAA Statements of Policy to cheap stock, promoter equity investment, voting rights, and promoter compensation. Produces examiner-ready comment responses with cap table analysis and negotiation strategy. Use when filing Reg A, Rule 504, intrastate, or direct public offerings in merit review states, responding to Blue Sky examiner comments, structuring offerings to avoid conditioning, or analyzing NASAA SOPs. Also trigger on cheap stock analysis, promoter equity tests, unequal voting rights review, state examiner correspondence, or phrases like "merit review issues" or "the state examiner sent comments."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/merit-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# State Merit Review Analysis

Produces pre-filing risk analysis and examiner-ready comment responses for non-covered securities offerings subject to state merit review. Covers cheap stock, promoter equity investment, voting rights, and promoter compensation under NASAA Statements of Policy.

## Quick Start

1. Confirm offering is NOT a covered security under 15 U.S.C. Section 77r
2. Gather intake documents (offering doc, charter, cap table, state list)
3. Run analysis steps 1-6 below
4. Draft comment response package or pre-filing memo
5. Prepare negotiation fallback positions per issue area

## Intake (Mandatory)

Gather before analysis unless user says "use defaults" or "just draft":

1. **Offering document** — Form 1-A, prospectus, PPM, or offering circular
2. **Charter documents** — Articles/certificate of incorporation, bylaws, amendments
3. **Cap table** — All issuances with dates, prices, consideration type, vesting, holder identity (Promoter vs. Non-Promoter)
4. **Issuance chronology** — Board consents, subscription agreements, service agreements
5. **Promoter compensation schedule** — Cash, equity, consulting, related-party contracts, loans
6. **Selling compensation terms** — Underwriter/placement agent agreements, warrants
7. **Historical financials** — Balance sheets for promoter equity calculation
8. **Target state list** — Filing pathway per state
9. **Federal exemption** — Reg A Tier 1/2, Rule 504, intrastate, direct registration
10. **Prior examiner correspondence** — Deficiency/comment letters if any

**Defaults if user doesn't respond:** NASAA SOP standards applied; Rule 405 promoter definition; 10% promoter equity investment benchmark.

### Threshold Questions

- Are securities "covered securities" under 15 U.S.C. Section 77r? (If yes, stop — no merit review)
- Shares issued for nominal cash or services within 36 months of filing?
- Promoters received equity disproportionate to cash/tangible asset contributions?
- Voting or control rights deviate from economic ownership?
- Offering proceeds repay insiders?
- State informally flagged issues?

## Step 1: Confirm Merit Review Applicability

| Covered (No Merit Review) | Not Covered (Merit Review Applies) |
|---|---|
| Listed on national exchange (NYSE, NASDAQ) | Reg A Tier 1 & 2 in merit states |
| Rule 506(b) / 506(c) | Rule 504 |
| Sold only to "qualified purchasers" | Intrastate offerings |
| | Direct public offerings not on national exchange |

Produce short posture memo: pathway, why merit review applies, verified citations. Flag risks to covered status (general solicitation, bad actor, integration).

## Step 2: Map Jurisdictional Standards

For each target state, verify:

| Factor | Source |
|---|---|
| Denial standard ("unfair, unjust, or inequitable") | State securities act |
| Registration method and merit review intensity | State regulator website |
| NASAA SOP adoption (Cheap Stock, Promoter's Equity, Unequal Voting) | State admin code |
| Coordinated Review availability (e.g., CR-3(b) for Reg A) | NASAA website |

**Key divergences** `[VERIFY current status]`:
- **California**: Own standards; Cal. Code Regs. Tit. 10, Section 260.140 et seq.
- **Texas**: Strict merit; arm's-length required for affiliated transactions
- **Washington**: Heightened scrutiny for development-stage; may require proceeds impoundment
- **New York**: Generally notice-filing; Martin Act may affect certain types

All cited standards must include verified URLs or `[VERIFY]` flag.

## Step 3: Analyze Cheap Stock

**Scope**: All equity issued to Promoters below public offering price within 36-month look-back.

**Quantitative analysis:**
1. Identify all Promoters per merit review definition
2. Calculate effective price per share (including conversion, warrants, liquidation preferences)
3. Compute dilutive effect: promoter price vs. public offering price
4. Calculate post-money ownership percentages

**Qualitative justification:** Early-stage risk, documented services rendered, vesting/lock-up/repurchase rights, milestones.

**Common remedies:** Escrow until earnings milestones, lock-ups, cancellations/reverse splits, operational use-of-proceeds conditions, enhanced dilution disclosure.

## Step 4: Analyze Promoter's Equity Investment

NASAA benchmark: promoter equity >= 10% of total aggregate offering price.

**Calculation (NASAA methodology, not GAAP):**
- Count: cash, tangible assets at documented fair value
- Exclude: imputed services value, goodwill
- State-specific: verify whether personal guarantees count

**Shortfall strategy:** Document tangible asset contributions, personal guarantees if permitted. Note: cheap stock + inadequate promoter investment is the highest-risk combination.

## Step 5: Review Voting Rights and Governance

NASAA SOP: voting rights proportionate to equity unless compelling justification.

| Issue | Risk |
|---|---|
| Dual-class super-voting shares | High — most merit states reject for retail |
| Blank check preferred stock | High |
| Minority shareholder elects majority of board | High |
| No class vote on mergers/liquidations/asset sales | Medium |
| No sunset on control provisions | Medium |

**Mitigation:** Sunset provisions, independent directors, class votes on major transactions, plain-English disclosure.

Verify "Description of Securities" matches actual charter/bylaws exactly.

## Step 6: Review Promoter Compensation

Build schedule: cash comp, equity grants, consulting fees, bonuses, company loans, related-party leases, IP payments, reimbursements. Connect each to use of proceeds.

Flag if proceeds repay insiders. Promoter definition may be broader than expected — examiners may classify control persons, significant consultants, or paid finders as promoters.

## Drafting Comment Response Package

**Components:**
1. Cover letter — point-by-point response to each examiner comment
2. Redline of offering document
3. Supporting exhibits (revised charter, escrow/lock-up agreements, updated cap table)

**Per-comment structure:**
1. Quote examiner comment verbatim
2. Cite applicable NASAA SOP or state admin code
3. Explain compliance or justify deviation
4. Reference specific redline page/section for remedy

**Tone:** Respectful, solution-oriented, legally precise. Not a litigation brief.

**Consistency:** Every factual assertion cites the record. Every legal assertion has verified citation or `[VERIFY]`. Restrictions promised must appear in binding agreements AND offering document.

## Negotiation Strategy

| Issue | Primary Position | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Cheap stock | Dilution disclosure + time-based lock-up | Lock-up + repurchase on bad acts | Milestone-based escrow |
| Promoter investment | Tangible assets + guarantees | Defer insider comp until minimum raise | Restructure founder equity |
| Voting rights | Sunset + independent directors | Reduce super-voting + class vote on majors | Eliminate dual-class |
| Promoter comp | Full disclosure + market comparables | Cap reimbursements + defer consulting | Escrow promotional shares |

Cross-state: concession in one state may require disclosure updates for all states. Don't concede early without knowing other states' positions.

## Post-Draft Alignment

After delivering initial analysis, confirm:
1. Cap table and issuance chronology reconciled to charter authority?
2. Examiner indicated priority concerns or informal guidance?
3. Pursue coordinated review (CR-3(b))?
4. Concessions client has already decided to accept or reject?

## Quality Checklist

- [ ] Preemption determination confirmed with verified citation
- [ ] NASAA methodology (not GAAP) for promoter equity
- [ ] Cap table reconciles to charter authority, matches "Principal Shareholders" and "Dilution" sections
- [ ] All promoters identified under merit review definition (broader than typical)
- [ ] Cheap stock covers all issuances within 36-month look-back
- [ ] Voting rights match actual charter/bylaws, not just offering document
- [ ] Every citation verified or flagged `[VERIFY]`
- [ ] Adversarial scrub: would examiner find inconsistencies?
- [ ] Negotiation fallbacks prepared per issue area
- [ ] Assumptions and open items listed prominently

## Pitfalls

- **Never fabricate citations.** All NASAA policy text, statutory sections, and case citations must be verified via research or flagged `[VERIFY]`.
- **Separate strategy from response.** Comment response letters become public records in many states; keep privileged analysis in internal memos.
- **Anti-fraud overlay.** Never obscure a merit issue — disclose cheap stock, promoter comp, and unequal voting plainly.
- **NASAA SOPs are not uniform.** Always verify state-specific adoption before citing.
- **Recommend CR-3(b) coordinated review** where available.
- **Cap table errors:** Excluding intangible-property shares, not reconciling to charter authority, omitting derivatives, conclusory justifications without documentation.
- **Ethics:** Model Rules 1.1 (competence), 1.3 (diligence), 1.4 (communicate concession impact), 3.3/4.1 (candor to examiners).
- **Attorney review required.** All output requires review by a licensed securities attorney before submission.
