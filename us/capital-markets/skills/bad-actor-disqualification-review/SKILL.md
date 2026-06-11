---
name: bad-actor-disqualification-review
title: Bad Actor Disqualification Review (Rule 506(d))
description: Produces a Rule 506(d) bad actor disqualification review for private securities offerings, including a covered persons register, tailored questionnaires mapping to each disqualifying event category, a documented reasonable-care diligence record, and classification analysis of flagged events with remediation or disclosure recommendations. Use this skill when conducting Rule 506(d) diligence, identifying covered persons for a Regulation D offering, drafting bad actor questionnaires, or analyzing potential disqualifying events involving criminal convictions, SEC orders, SRO sanctions, or state regulatory actions. Also trigger when the user mentions bad actor screening, covered persons analysis, Rule 506(d) questionnaire, disqualification waiver, or reasonable care defense. Even if the user just says "bad actor check" or "506(d) diligence," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bad-actor-disqualification-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [analysis, checklist, corporate, drafting, memo, regulatory]
---

# Bad Actor Disqualification Review (Rule 506(d))

## Why This Skill Exists

A single disqualifying event involving any covered person eliminates the Rule 506 exemption — and with it, NSMIA preemption across all 50 states. This is not a theoretical risk: offerings have been unwound, rescission rights have been triggered, and issuers have faced enforcement actions because bad actor screening was treated as a checkbox exercise rather than a defensible diligence process. The covered persons net is broader than most practitioners realize (it catches specific individuals at broker-dealers, not just entities), and the lookback periods vary by event category.

This skill executes a structured reasonable-care review that builds a defensible record: covered persons register, tailored questionnaires, independent verification, event classification, and remediation pathways.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Offering perimeter** — Rule 506(b) vs. 506(c), expected sale date(s), staged closing schedule
2. **Cap table** — full beneficial ownership chains, voting agreements, convertible instruments, super-voting stock; sufficient to calculate voting power (not just equity %)
3. **Organizational documents** — charter/bylaws or operating agreement, board consents
4. **Officer/director list** — full legal names, roles, description of involvement in investor-facing activities
5. **Promoter arrangements** — any person who founded/organized the issuer or receives compensation in connection with founding (Rule 405 definition)
6. **Solicitation arrangements** — placement agent, finder, broker-dealer, and portal agreements; identify the specific individuals soliciting, not just the firm entity
7. **Prior Form D filings** and known enforcement history
8. **Per-person identifiers** — full legal name, aliases, DOB, current/prior addresses, FINRA/SEC registrations

**If the user doesn't respond**, apply and clearly label these defaults: all persons meeting Rule 506(d)(1) categories included; err toward inclusion for borderline covered persons; all lookback periods applied from expected first sale date.

If screening identifiers are unavailable for any covered person, propose a risk-based path (remove from covered role, restructure, delay) before proceeding.

---

## Step 1: Build Covered Persons Register

Map each person/entity to their Rule 506(d)(1) category. Update at every material deal change.

| Category | Rule Ref | Persons/Entities | Basis for Inclusion |
|---|---|---|---|
| Issuer + affiliated/predecessor issuers | 506(d)(1)(i) | | |
| Directors and executive officers | 506(d)(1)(ii) | | Rule 405 "executive officer" definition |
| Other officers participating in the offering | 506(d)(1)(ii) | | Participation = road shows, investor comms, preparing materials; err toward inclusion |
| General partners / managing members | 506(d)(1)(iii) | | Read operating agreement; title alone insufficient in DE LLCs |
| 20%+ voting equity holders | 506(d)(1)(iv) | | Voting power, not equity %; aggregate holdings under common control |
| Promoters | 506(d)(1)(v) | | Rule 405 definition |
| Compensated solicitors | 506(d)(1)(vi) | | Direct or indirect remuneration for solicitation |
| GPs/directors/EOs/MMs of compensated solicitors | 506(d)(1)(vii) | | Check specific individuals at each broker-dealer |

**Voting power traps**: Aggregate related-entity holdings under common control; account for voting agreements, preferred stock as-converted, and super-vote share classes. A fund at 15% through one entity + 6% through an affiliate = 21% covered person.

---

## Step 2: Draft Questionnaires

Draft a signed questionnaire for each covered person. Questions must mirror the disqualifying event categories in 17 C.F.R. § 230.506(d)(1). **[VERIFY all lookback periods against current rule text before finalizing.]**

| Category | Lookback | Key Notes |
|---|---|---|
| Criminal convictions — securities, false SEC filings, securities-business conduct | 10 years | Include guilty pleas and nolo contendere |
| Court injunctions/restraining orders — same subjects | 5 years [VERIFY] | Final orders only |
| Final orders — state securities/banking/insurance/federal banking/NCUA | 10 years | Bars or fraud-based; confirm "finality" from actual document |
| SEC disciplinary orders — broker, dealer, IA, funding portal | [VERIFY] | Suspension, revocation, or limitation |
| SEC cease-and-desist orders — scienter-based anti-fraud or §5 | 5 years [VERIFY] | §17(a) trigger requires scienter |
| SRO suspension/expulsion — FINRA, etc. | 10 years [VERIFY] | Confirm "associated with a member" at time of sanction |
| U.S. Postal Service false representation orders | 5 years [VERIFY] | |

**Questionnaire requirements:**
- Define key terms in plain English tied to rule text
- Require supporting documents for every "yes" response
- Signature block: (i) certification of completeness, (ii) agreement to update through final sale, (iii) reliance acknowledgment
- Require refresh if closing is delayed or staged

---

## Step 3: Conduct Independent Verification

Search all covered persons independently. Document date, scope, and results for every search.

| Database | Scope |
|---|---|
| SEC EDGAR (litigation releases, admin proceedings) | All covered persons |
| FINRA BrokerCheck | Registered broker-dealer personnel |
| SEC IAPD | Investment advisers |
| PACER | Federal criminal and civil matters |
| State securities regulator databases (NASAA sites) | State-licensed persons |
| GSA SAM (debarment) | All covered persons |

Calibrate depth to risk: deeper investigation for promoters, compensated solicitors, persons with regulatory friction, penny-stock backgrounds, or complex ownership chains. Refresh all searches shortly before sale if offering extends beyond initial diligence. Flag FCRA applicability if consumer reports are obtained.

---

## Step 4: Classify Disqualifying Events

For each flagged item, produce a memo section covering:

1. **What happened** — nature, issuing authority, date of order/conviction
2. **Lookback math** — date of event to date of intended sale; within applicable period?
3. **Category match** — quote the order/judgment text and map to a specific Rule 506(d)(1) category; do not paraphrase
4. **"Final order" analysis** — for state regulatory actions, confirm finality from the document itself
5. **SRO analysis** — confirm "associated with a member" status and that the sanction qualifies
6. **Pre-September 23, 2013 events** — no disqualification, but **mandatory Rule 506(e) disclosure** to investors; frequent trap
7. **Conclusion** — disqualifying / not disqualifying / requires attorney verification, with rationale

---

## Step 5: Determine Remediation and Disclosure Pathways

| Scenario | Path |
|---|---|
| Pre-Sept. 23, 2013 event | No disqualification; draft Rule 506(e) investor disclosure |
| Event discovered, no prior knowledge | Document reasonable-care record supporting Rule 506(d)(2)(iv) exception |
| SEC waiver | Available but rare and slow; flag for attorney evaluation |
| Remove person from covered category | End solicitation role; resign officer role before sale; restructure below 20% voting threshold — flag sham risk |
| Replace placement agent | Engage FINRA-member with clean record; obtain their own 506(d) certifications for specific soliciting individuals |
| Change exemption strategy | Evaluate Section 4(a)(2); analyze Blue Sky implications of losing §18(b)(4)(E) preemption |

**Rule 506(e) disclosure**: Must be accurate, complete, and not misleading; review against §17(a) and Rule 10b-5 before delivery.

**Post-closing caution**: Remediation after sales may not cure past noncompliance. Evaluate rescission exposure and supplemental disclosure obligation.

---

## Step 6: Produce Final Work Product

Deliver:
1. **Executive conclusion** — (a) no disqualifying events identified; (b) potential event requiring remediation; or (c) disqualifying event — do not rely on Rule 506 absent waiver or restructure
2. **Covered persons register** with basis for each inclusion/exclusion
3. **Diligence log** — dates, databases searched, attached logs or vendor reports
4. **Per-item analysis** for each flagged event
5. **Open items list** — pending questionnaires, outstanding searches, unresolved classifications; state whether closing should be conditioned on completion
6. **Next steps** with responsible owners (legal vs. company)

### Mandatory Front Matter

At the top of every output, include:
1. **Assumptions Used** — offering type, sale date, covered persons included/excluded, databases searched
2. **Open Items / Needed Inputs** — pending questionnaires, outstanding searches, unresolved items

Cross-check any transaction document representations about 506(d) status against the diligence record. Do not permit a blanket "no bad actors" representation when diligence is incomplete or items are pending.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial review, ask:

1. Are all covered persons accounted for, including specific individuals at the placement agent?
2. Are there any pending questionnaire responses or outstanding searches?
3. Should closing be conditioned on completion of any open diligence items?
4. Does the transaction documentation need carve-outs for known issues in the 506(d) representation?

---

## Quality Audit

Before finalizing, verify:

- All Rule 506(d)(1) categories analyzed — no category skipped
- Covered persons register includes specific individuals at broker-dealers, not just entities
- Voting power calculated on voting basis (not equity %) with related-entity aggregation
- All lookback periods verified against current rule text
- Questionnaires require document production and update obligations
- Independent verification covers all databases listed and is current as of expected sale date
- Pre-September 23, 2013 events identified and Rule 506(e) disclosure drafted
- Every flagged event analyzed against the actual order/judgment text
- Remediation recommendations are operationally implementable
- Assumptions and open items listed prominently
- No fabricated CDI, no-action letter, or case law citations

---

## Guidelines

- **Verify rule text first**: Search 17 C.F.R. § 230.506(d) before finalizing — do not rely on cached lookback periods or category lists
- **No invented citations**: Any CDI, no-action letter, or case law reference must include a verified URL or be marked `[VERIFY]`
- **Voting power ≠ equity**: Always calculate 20% threshold on voting power; aggregate related-entity holdings
- **Participation is broad**: Any officer with investor contact is likely a covered person; err toward inclusion
- **Questionnaires are evidence**: A plaintiff will use a poorly drafted questionnaire against the issuer; signed certifications with document production are non-negotiable
- **Diligence currency**: Searches must be current as of sale date; refresh if closing delayed
- **Blue Sky exposure**: Loss of Rule 506 = loss of §18(b)(4)(E) preemption; California (§25102(f) [VERIFY]), New York, and Texas have aggressive state regimes
- **Privilege**: Analysis memo can be privileged; questionnaires and certifications may be discoverable — draft accordingly
- **Conflicts**: Monitor for conflicts where firm represents both issuer and a covered person disclosing wrongdoing (Model Rules 1.7, 1.13); separate counsel may be required
- **Anti-hallucination**: Do not fabricate rule text, lookback periods, or CDI references. Verify against current regulations before finalizing
- **Attorney review required**: All output requires review by licensed counsel before use in an offering, sharing with investors, or reliance for filings (Model Rules 1.1, 1.3, 5.3)
