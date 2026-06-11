---
name: blue-sky-filings
title: Blue Sky Filings Compliance Workflow
description: Produces a practitioner-grade Blue Sky compliance memorandum and execution plan for U.S. securities offerings. Analyzes NSMIA covered securities preemption, classifies offerings under Regulation D/Rule 506 or alternative federal exemptions, maps state jurisdictional nexus distinguishing offers from sales, and generates a state-by-state filing plan with Form D/EFD workflow, fee schedules, amendment triggers, and renewal calendars. Use this skill when advising on private placement Blue Sky compliance, Reg D notice filings, multi-state offering coordination, state securities registration exemptions, Form D filings, EFD submissions, or state fee budgeting. Also trigger when the user mentions covered securities preemption, NSMIA analysis, or asks about state notice filing requirements. Even if the user just says "Blue Sky" or "state filings for our raise," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/blue-sky-filings
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [analysis, checklist, corporate, drafting, memo, regulatory, research]
---

# Blue Sky Filings Compliance Workflow

## Why This Skill Exists

Blue Sky compliance is one of the most common sources of post-closing securities exposure. Missed state notice filings create rescission rights for investors — a powerful leverage tool in disputes. The complexity comes from the intersection of federal preemption (NSMIA) with 50+ state regimes, each with different deadlines, fees, forms, and renewal requirements. When Blue Sky is treated as a back-office afterthought, offerings close with gaps that surface as litigation risk years later.

This skill produces an integrated compliance memo and execution plan that prevents those gaps — jurisdictional nexus analysis, preemption classification, and a state-by-state filing plan with timelines and recordkeeping.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Offering summary** — security type, aggregate amount, price/valuation, planned closing dates, single-close vs. rolling/evergreen
2. **Federal legal basis** — Rule 506(b), 506(c), 504, Section 4(a)(2), Reg S, registered offering, Rule 147/147A, or other
3. **Offering documents** — PPM, investor deck, term sheet, subscription agreement, investor questionnaire, AV verification procedures (if 506(c))
4. **Investor geography** — state of residence/domicile (individuals) or principal place of business (entities); states where offers were directed
5. **Intermediaries** — identity, geographic footprint, and state registration status of any broker-dealers, finders, or placement agents
6. **First sale date** — confirmed or projected
7. **Prior filings** — existing Blue Sky matrices, prior Form D filings, ongoing offerings

**If the user doesn't respond**, apply and clearly label these defaults: Rule 506(b) offering; no general solicitation; single closing; EFD filing method where available.

Optional: priority investor states, issuer type, non-U.S. investors (Reg S interplay), expected secondary transfers or SPV structures.

---

## Step 1: Classify Federal Posture and Covered Security Status

Identify whether securities are "covered securities" under 15 U.S.C. § 77r [VERIFY].

| Category | NSMIA Section | Preempts State Registration? | State Authority Preserved |
|---|---|---|---|
| Exchange-listed securities | 18(b)(1) | Yes | Fraud enforcement |
| Registered investment company securities | 18(b)(2) | Yes (Form NF, not Form D) | Fraud enforcement |
| Rule 506(b) / 506(c) offerings | 18(b)(4)(F) | Yes | Notice filings, fees, consent to service, fraud |
| Rule 504 offerings | — | No | Full state registration authority |
| Rule 147/147A intrastate | — | No | Full state registration authority |
| Section 4(a)(2) (without Rule 506) | — | Generally no | Full state registration authority |

For non-covered securities, analyze state pathways: registration by coordination, qualification, notification/filing, or available state exemptions.

Document factual basis for exemption selection — general solicitation analysis, investor qualification method, and why all conditions are satisfied.

---

## Step 2: Map Jurisdictional Nexus (Offers vs. Sales)

For each state, document the factual hook triggering Blue Sky obligations:

- Location of investors who **received offers** (critical in 506(c) general solicitation)
- Location of investors who **completed purchases**
- Location of issuer personnel conducting solicitation
- Accessibility of marketing materials in additional states

**Entity investors:** Principal place of business, state of formation, and location of investment decision-maker may each matter — confirm which address concept the subscription agreement uses.

**Negative space:** Document states considered and excluded, with reasoning.

**Evidence to preserve:** Where subscription materials were sent, investor residency representations, acceptance location, wire origin records.

---

## Step 3: Build State-by-State Compliance Pathway

For each state:

| Field | Content |
|---|---|
| Federal basis | Exemption relied upon |
| Preempted? | Yes / No per Step 1 |
| State filing method | EFD / direct filing / state portal |
| Forms required | Form D copy, Form U-2 (consent to service), state-specific forms |
| Fee | Amount + calculation basis [VERIFY] |
| Deadline | Days after first sale [VERIFY] |
| Renewal required? | Yes/No; if yes, annual anniversary date |
| Source URL | Link to state regulator's filing page, or [VERIFY] |

**Intermediary check:** NSMIA does not preempt state broker-dealer registration. Confirm placement agents/finders are registered in each solicitation state — an unregistered intermediary can jeopardize the issuer's exemption.

**State-specific flags** (all require verification):
- **New York** — Rule 506 offerings accepted via EFD; legacy GBL § 359-e may add complexity [VERIFY]
- **California** — Section 25102(f) for non-Rule-506 private placements requires pre-existing relationships [VERIFY]
- **Texas / Washington** — Known to issue comments on notice filings if disclosures deemed insufficient [VERIFY]
- **Merit review states** — Confirm state does not impose additional conditions beyond Form D + fee

---

## Step 4: Execute Form D and EFD Filing Workflow

**SEC Form D timing:** File via EDGAR no later than **15 calendar days** after first sale [VERIFY current instructions].

"First sale" = issuer first receives irrevocable consideration (subscription accepted + payment received — not distribution of materials or expressions of interest).

**Filing checklist:**
- [ ] Confirm first sale date and implicated states
- [ ] Verify Form D fields match offering documents (issuer name, jurisdiction, officers, amount, exemption)
- [ ] File Form D via EDGAR
- [ ] Submit state notices via EFD or direct filing; pay applicable fees
- [ ] Save conformed copies, fee receipts, and state acceptances to closing binder
- [ ] Complete **Rule 506(d) bad actor screening** for all covered persons — a disqualifying event eliminates Rule 506 and NSMIA preemption entirely

**Multi-closing offerings:** File additional state notices for each new investor state at or before first sale in that state.

**Fee budgeting:** Fees range from ~$100 flat to percentage-based with caps, varying significantly by state [all specific amounts require current verification].

---

## Step 5: Manage Amendments, Renewals, and Closing Filings

**Form D amendment triggers:**
- Adding general solicitation (requires restructuring 506(b) to 506(c))
- Change to minimum investment amount
- Addition or change of placement agent
- Expansion into new investor states
- Material change to use of proceeds
- Increase in total offering amount

**Renewal obligations:** Many state notices expire **12 months** after initial filing. Rolling/evergreen offerings must renew before expiration — a lapse may create rescission exposure.

**Closing/final filing:** File Form D amendment reporting total amount sold and offering close.

**Escalation protocol:** "If any investor is added in a state not on the current Blue Sky tracker, counsel must be notified before circulating final subscription documents, and no funds shall be accepted until state notice filing requirements are confirmed."

---

## Step 6: Produce Deliverables

Three integrated layers:

1. **Executive Summary** (for CFOs/board) — plain language: what must be done, by when, who is responsible
2. **Legal Analysis** — covered securities/preemption framework, chosen exemption and conditions, limits of state authority
3. **Implementation Section** — state-by-state filing plan, recordkeeping requirements, escalation rules, compliance calendar

### Mandatory Front Matter

Include **Assumptions and Open Items** listing every [VERIFY] item with:
- What needs to be confirmed
- Where/how to confirm it
- Who is responsible and by when

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial memo, ask:

1. Are there additional investor states not yet included in the filing plan?
2. Is the first sale date confirmed, or should the timeline remain provisional?
3. Should local Blue Sky counsel be engaged for any specific states?
4. Does the client need the compliance calendar delivered in a specific format?

---

## Quality Audit

Before finalizing, verify:

- Preemption determination confirmed with verified statutory citation
- Every state-specific requirement cites a verifiable source or carries [VERIFY]
- Offer states and sale states distinguished (not conflated)
- Form D fields consistent with offering documents
- Intermediary registration confirmed for each solicitation state
- Rule 506(d) bad actor screening included in workflow
- Amendment triggers and renewal dates documented
- Fee budget aggregated across all filing states
- Escalation protocol included for new investor states
- Assumptions and open items listed prominently
- No state law requirements stated as facts without sourcing

---

## Guidelines

- **Anti-hallucination**: Every state-specific requirement (deadline, fee, form, portal) must cite a verifiable primary source URL or carry `[VERIFY]` — never state state law requirements as facts without sourcing
- **Rescission framing**: Primary litigation risk is investor rescission under Section 12 of the Securities Act and analogous state provisions — frame all compliance gaps in terms of this exposure
- **Offer ≠ Sale**: Do not conflate; Rule 506(c) general solicitation may expand the offer footprint significantly beyond sales
- **No merit review for covered securities**: NSMIA preempts substantive review for Rule 506 — but confirm state is not attempting to impose it
- **Form D consistency**: Total offering amount on state EFD filings must match SEC Form D Part C, Question 1
- **Local counsel**: Recommend for merit review states, high-profile offerings, or aggressive enforcement states
- **Confidentiality**: Treat all drafts as privileged work product under Model Rule 1.6
- **Attorney review required**: All output is draft guidance requiring attorney review before use or filing. State administrative rules and fee schedules change frequently; verify all state-specific requirements via primary sources before reliance
