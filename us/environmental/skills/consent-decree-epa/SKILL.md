---
name: consent-decree-epa
title: EPA Consent Decree
description: Drafts EPA Consent Decrees resolving federal environmental enforcement actions under CWA, CAA, RCRA, or CERCLA. Covers case caption, jurisdictional recitals, compliance obligations, civil penalties (referencing 40 CFR § 19.4 inflation-adjusted maximums), stipulated penalties, dispute resolution, force majeure, covenants not to sue, public comment requirements, and emerging-issue considerations including PFAS releases. Use when settling EPA enforcement actions, drafting environmental consent judgments, or preparing judicial settlement agreements with the EPA.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/consent-decree-epa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [litigation, regulatory, drafting, agreement]
---

# EPA Consent Decree

Drafts an enforceable federal court consent decree resolving EPA civil enforcement actions, structured for DOJ lodging requirements, 30-day public comment, and judicial entry.

---

## Related skills

- `nov-response` — for the pre-enforcement Notice-of-Violation phase that often precedes a consent decree.
- `environmental-regulation-summaries` — for governing-statute identification and current penalty figures.
- `phase-i-esa` — when AAI / CERCLA innocent landowner status is implicated.
- `brownfields-agreement` — for redevelopment consent agreements at contaminated sites.
- `environmental-indemnity` and `environmental-covenant-and-easement` — for institutional-control instruments referenced in a decree.
- `mediation-statement` — for facilitated DOJ/EPA settlement discussions before lodging.

## Prerequisites

Gather before drafting:
- **Case materials** — complaint/draft complaint, NOVs, administrative orders, inspection reports, sampling data
- **Defendant info** — exact legal name, incorporation state, principal place of business, parent/subsidiary relationships
- **Applicable statutes** — CWA, CAA, RCRA, CERCLA, or other
- **Facility details** — address, operational history, regulated activities, permit history
- **Penalty data** — economic benefit analysis, violation history, ability-to-pay documentation
- **Technical attachments** — SOW, Remedial Action Plan, or Compliance Implementation Plan

## Decree Sections

### 1. Case Caption & Parties

Caption: "United States of America, on behalf of the United States Environmental Protection Agency, Plaintiff, v. [Defendant Full Legal Name], Defendant. Civil Action No. ___"

- [ ] Verify defendant legal name against corporate registration
- [ ] Identify EPA Regional Office and Project Coordinator
- [ ] Document parent/subsidiary/successor relationships
- [ ] Address joint and several liability if multiple defendants

### 2. Jurisdictional Recitals

Include for each element:

| Element | Content |
|---|---|
| Subject matter jurisdiction | Specific statute + enforcement provision |
| Facility description | Address, operations, permit requirements |
| Violation allegations | Reference NOVs/inspections — framed as allegations (no admissions) |
| Public interest | Environmental benefits, compliance, deterrence |

Statute reference:

| Statute | Citation | Enforcement |
|---|---|---|
| CWA | 33 U.S.C. § 1251 et seq. | § 1319 |
| CAA | 42 U.S.C. § 7401 et seq. | § 7413 |
| RCRA | 42 U.S.C. § 6901 et seq. | § 6928 |
| CERCLA | 42 U.S.C. § 9601 et seq. | §§ 9606–9607 |

### 3. Compliance & Remedial Obligations

Corrective action provisions must specify:
- Equipment installation, process modifications, operational parameters
- Monitoring: sampling frequencies, analytical methods, detection limits, reporting formats
- EPA review/approval triggers for work plans, design documents, completion reports
- BMPs, training schedules, preventive maintenance, record-keeping

Cleanup standard basis — select applicable:
- [ ] ARARs
- [ ] Risk-based site-specific criteria
- [ ] Regulatory standards (effluent/emission limits)
- [ ] Institutional controls (where active remediation infeasible)

### 4. Compliance Schedule

Each milestone needs:
- Calendar date or days after triggering event (entry, EPA approval, prior task completion)
- Sequential dependency mapping (design → approval → construction → certification)
- Interim reporting intervals for multi-year projects
- Clear distinction between document-submission deadlines and physical performance deadlines

### 5. Financial Provisions

**Civil penalty elements:**
- Total in USD; itemize components (penalty / NRD / past costs / oversight costs)
- Reflect statutory factors: seriousness, economic benefit, ability to pay, history, culpability
- Use **40 CFR § 19.4** for current per-violation-per-day statutory maximums — EPA adjusts the table annually under the Federal Civil Penalties Inflation Adjustment Act (28 U.S.C. § 2461 note). Recent annual rules in early 2025 set CWA § 309(d) at $66,712/day, CAA § 113(b) at $121,275/day, and RCRA § 3008(g) at $93,058/day; figures change each calendar year.
- Civil penalties paid to a government entity for violation of law are generally non-deductible under 26 U.S.C. § 162(f) as amended by the Tax Cuts and Jobs Act (Pub. L. 115-97, 2017) and Treas. Reg. § 1.162-21 (2021). Restitution and amounts paid to come into compliance may be deductible if specifically identified in the decree per § 162(f)(2). Tax counsel should confirm before relying on any portion as deductible.

**Payment:** Payee is U.S. Treasury via DOJ Consolidated Debt Collection System. Specify lump sum or installment schedule, wire/certified check, proof of payment to EPA and DOJ within 5–10 business days. Installment default triggers acceleration + interest at federal judgment rate.

**Financial assurance** (for significant remedial work): surety bond, letter of credit, trust fund, or corporate guarantee. Amount per EPA-approved estimate plus contingency. Reduction/release tied to milestone completion.

### 6. Stipulated Penalties

Tiered daily rates:

| Category | Days 1–30 | Days 31–60 | Day 61+ |
|---|---|---|---|
| Major (cleanup standards, critical milestones) | $[X]/day | $[2X]/day | $[3X]/day |
| Minor (reports, documentation) | $[Y]/day | $[2Y]/day | $[3Y]/day |

- EPA issues written demand (violation, penalty amount, basis)
- 15 days to invoke dispute resolution; otherwise due within 30 days of demand
- In addition to — not in lieu of — all other remedies
- No accrual during valid force majeure; resume upon FM cessation

### 7. Dispute Resolution

| Tier | Participants | Timeframe |
|---|---|---|
| Informal negotiation | Party representatives | 20–30 days |
| Senior escalation | Senior EPA + defendant officials | 15–20 additional days |
| Court resolution | Motion to district court | After Tiers 1–2 exhausted |

Defendant complies with EPA position during pendency unless irreparable harm. Stipulated penalty demands or material breach may go directly to court.

### 8. Force Majeure

**Qualifying:** Acts of God, wars/riots, unanticipated government action (statutory changes, permit denial despite good faith).

**Excluded:** Economic conditions, financial inability, defendant's labor disputes, contractor failures (unless caused by qualifying FM event).

**Invocation** (written notice to EPA within ___ days): describe event, anticipated delay duration, affected milestones, mitigation measures. Defendant must exercise best efforts to minimize delay.

### 9. Covenant Not to Sue & Reservation of Rights

Covenant scope — define precisely:
- *Temporal:* violations up to decree entry date
- *Geographic:* named facility with legal description
- *Substantive:* named statutes only

United States always retains right to pursue:
- Criminal liability (non-waivable)
- Post-entry violations
- Newly discovered imminent/substantial endangerment
- Unaddressed statutes and natural resource damages
- Decree enforcement (contempt, stipulated penalties, specific performance)
- Cost recovery (attorney's fees, expert fees, oversight costs)
- Claims against third parties (PRPs, contractors, successors)

### 10. Public Participation & Judicial Approval

Required sequence:
1. Lodge decree with court (with or after complaint filing)
2. Federal Register notice → **30-day** minimum public comment period
3. Local newspaper notice / public meeting if warranted
4. United States files responsiveness summary
5. Court enters decree after comment period and responsiveness summary
6. United States may withdraw if comments show decree is inappropriate

**Withdrawal effect:** Decree is null and void; defendant cannot use settlement statements in later litigation.

### 11. Modification & Termination

- **Modification:** All-party written agreement + court approval
- **Termination:** Defendant completes all obligations → United States files termination motion → court order
- **Effective date:** Date of judicial entry (all deadlines run from this date)

### 12. Execution

| Signatory | Authorization |
|---|---|
| Defendant (corporate) | Officer with authority + corporate resolution |
| United States | U.S. Attorney + DOJ ENRD trial attorney(s) |
| EPA | Regional Counsel + Project Coordinator |
| Court | U.S. District Judge + entry date |

Include counterparts clause and specify service addresses for all decree-related notices.

## Emerging issues: PFAS and CERCLA consent decrees

EPA designated PFOA and PFOS (and their salts and structural isomers) as CERCLA hazardous substances by final rule effective **July 8, 2024** (89 FR 39124, May 8, 2024; codified at 40 CFR § 302.4). Reportable quantity is 1 lb in any 24-hour period. EPA announced on **September 17, 2025** its intent to develop a CERCLA Section 102(a) Framework Rule; further PFAS designations are expected.

Practical implications for consent decrees:

- **PFAS releases now trigger CERCLA liability and reporting.** Pre-2024 site assessments may not have evaluated PFAS at all — verify whether the decree covers PFAS-related releases and whether the covenant scope is intended to reach them.
- **Covenant scope drafting.** Specify whether the covenant covers (a) only the named hazardous substances at issue in the underlying complaint or (b) "all CERCLA hazardous substances released at the facility." The latter formulation now sweeps in PFAS by operation of 40 CFR § 302.4 and may exceed the parties' settlement intent.
- **Cost-recovery reservation.** Reserve future CERCLA cost recovery for newly designated PFAS substances (and any post-decree designations under § 102(a)) where appropriate. EPA's CERCLA PFAS Enforcement Discretion Policy (Apr 19, 2024) focuses on parties that significantly contributed to PFAS releases — federal facilities, manufacturers, and parties that used PFAS in manufacturing — but private cost-recovery actions are not similarly constrained.
- **Site characterization.** RAPs and SOWs at sites with foreseeable PFAS use (AFFF storage, electroplating, textile coating, paper manufacturing, certain landfills) should specify PFAS analytical methods (EPA Method 1633 for non-potable water; EPA Method 537.1 for drinking water).

## Critical Checks

- **No admissions:** All violation references use "neither admits nor denies" language.
- **DOJ concurrence:** Required before lodging — coordinate with ENRD trial attorney throughout.
- **Penalty caps:** Use **40 CFR § 19.4** for current per-violation-per-day maximums; EPA updates the table annually each January. Underlying statutory authorities: CWA § 1319(d), CAA § 7413(b), RCRA § 6928(g), CERCLA § 9609.
- **CERCLA-specific:** Include § 122 settlement provisions, § 113(f)(2) contribution protection, § 122(f) covenant; address NCP consistency. For PFAS-relevant sites, calibrate covenant scope against post-July-2024 designation (see Emerging Issues above).
- **RCRA financial assurance:** Verify 40 C.F.R. Parts 264/265 Subpart H for TSD facilities; financial-assurance amounts and acceptable instruments revised in part by the 2017 Final Rule on Financial Responsibility for Solid Waste Disposal Facilities and subsequent updates.
- **Multi-statute cases:** Address each statute's liability framework, penalty authority, and penalty factors independently.
- **Exhibit consistency:** Cross-reference all SOWs, RAPs, and compliance plans by exhibit number.
- **State involvement:** Confirm whether state agency must be a party/signatory and whether state-specific notice requirements apply (some states require state attorney-general concurrence on consent decrees affecting state water quality standards).

---

## Troubleshooting

- **Defendant cannot pay the proposed penalty.** Document the ability-to-pay analysis with audited financials; EPA's ABEL/INDIPAY models inform the penalty negotiation but the underlying statutory factors (CWA § 309(d), CAA § 113(e), RCRA § 3008(a)(3)) require explicit consideration. If the agreed penalty deviates materially from the statutory factors, the lodged decree's responsiveness summary will need to address it.
- **Public comment is hostile during the 30-day window.** The U.S. may modify or withdraw the decree per the public-comment regulations (28 C.F.R. § 50.7). Anticipate this in the negotiation; build in a "decree withdrawal" provision specifying that decree statements cannot be used in later litigation if the U.S. withdraws.
- **State-law claims pending alongside federal claims.** Coordinate with state AG; either bring the state in as a party or carefully scope the federal covenant to avoid prejudicing parallel state proceedings.
- **PFAS exposure surfaces post-lodging.** If newly designated CERCLA hazardous substances are identified at the facility after lodging but before entry, evaluate whether to amend the decree (28 C.F.R. § 50.7 supplemental notice may be required) or proceed and address PFAS via a separate proceeding.
- **Force-majeure invocation contested.** EPA's pre-litigation FM dispute process is the first stop; if irreconcilable, the dispute-resolution tier proceeds to district court motion. Document FM-event evidence contemporaneously.

---

## References

- `references/AUTHORITY-STATUS.md` — date-stamped record of authoritative sources consulted for this skill.
