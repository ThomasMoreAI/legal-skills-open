---
name: colorado-government-contracting
title: Colorado Government Contracting Skill
description: Colorado state and local government contracting guidance for ENAC. Use for CORA, CGIA, procurement, prompt payment, Colorado AI Act, WCAG, immigration certification, and government contract review.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/colorado-government-contracting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Colorado Government Contracting Skill

Colorado government contracting is not the same as commercial contracting. The rules are different, the risks are different, and the negotiating posture is different. This skill is ENAC's authoritative guide to the legal landscape for Colorado state and local government work.

---

## 1. CORA: Colorado Open Records Act (C.R.S. 24-72-201 et seq.)

**The core rule:** Every document submitted to a Colorado public entity is a public record and presumptively subject to public disclosure.

**What this means for ENAC:** Your proposal. Your methodology documentation. Your emails to the county project manager. Your invoices. Your assessment frameworks. If you submit it, it can be requested.

**The trade secret exception (C.R.S. 24-72-204(3)(a)(IV)):** Confidential commercial and financial information, and trade secrets, are exempt from CORA disclosure. This is ENAC's primary protection.

**Required strategy: before submitting anything:**

1. Mark all ENAC materials "Confidential: Trade Secret" at the top of each page and in file metadata
2. Do not submit proprietary methodology details that are not required for the deliverable: if the county does not need to see how the sausage is made, do not show them
3. Negotiate CORA notice rights in the contract: the county must provide ENAC written notice within five (5) business days of receiving a CORA request for ENAC materials, and must not disclose until ENAC has had a reasonable opportunity to seek a protective order
4. The Background IP Schedule (see `background-ip-schedule` skill) should be attached to the contract, not submitted as a standalone deliverable

**When a CORA request arrives:**
1. Identify exactly which ENAC materials are responsive to the request
2. Assert the trade secret exemption for each item in writing to the county's records custodian
3. Request a copy of the CORA request and determine the response deadline
4. If the county proposes to disclose ENAC materials: seek a temporary restraining order in Colorado district court immediately: CORA deadlines are short
5. Route to `@legal-privacy` for handling

---

## 2. CGIA: Colorado Governmental Immunity Act (C.R.S. 24-10-101)

**The core rule:** The state and its political subdivisions (including counties) retain broad governmental immunity from tort claims. A government entity cannot be sued unless the legislature has specifically waived immunity.

**What this means for ENAC:**
- Asymmetric indemnification is normal, expected, and largely non-negotiable on the immunity question itself
- Adams County will not indemnify ENAC for claims against ENAC arising from ENAC's work
- ENAC will be asked to indemnify Adams County for claims against the county arising from ENAC's work

**What is negotiable:**
- The scope of ENAC's indemnification obligation (what events trigger it)
- The standard of fault (negligence vs. strict performance)
- The financial cap on ENAC's indemnification

**Required negotiation position:**
- Cap ENAC's indemnification at total fees paid
- Negligence standard: ENAC indemnifies for its own negligence, not for strict compliance failures or consequential claims
- Do not accept indemnification that extends to third-party claims without a negligence standard
- The county cannot waive its own immunity: do not negotiate for mutual indemnification; negotiate for a cap and a negligence standard on ENAC's side

---

## 3. Colorado Procurement Code (C.R.S. 24-101 et seq.)

**State agencies:** Subject to the Colorado Procurement Code. Administered by the Office of the State Architect (construction), State Purchasing Office (goods and services), and individual agency procurement offices.

**Counties and municipalities:** Subject to their own home-rule charters and local procurement policies. The state procurement code does not directly bind counties or home-rule municipalities.

**Adams County:** Operates under its own Purchasing and Contracting Policy. For every Adams County procurement:
- Read the Adams County Purchasing and Contracting Policy
- Read the state procurement code for context and to understand where Adams County may have adopted similar standards
- Do not assume state procurement rules apply to county contracts without verification

**Practical guidance:**
- Request the county's procurement rules at the start of any engagement
- Understand the dollar thresholds for competitive bidding (below which sole-source procurement is possible)
- If the contract is sole-source, understand the county's internal approval requirements

---

## 4. Colorado Prompt Payment Act (C.R.S. 24-91-103)

**The core rule:** State agencies must pay contractors within statutory deadlines. Interest accrues on late payments.

**Practical obligations for ENAC:**
- Invoice promptly and consistently. Monthly in arrears is ENAC's standard.
- Track the 30-day clock from the date the invoice is received by the county
- If payment is late, send a formal written notice referencing the Prompt Payment Act
- Build a dunning calendar: invoice on the 1st, follow up on the 31st, escalate on the 46th

**Note for counties:** The Prompt Payment Act directly applies to state agencies. County payment obligations are governed by the PSA terms. Always negotiate a Net 30 payment term and late payment interest into the PSA.

---

## 5. Non-Compete Restrictions (C.R.S. 8-2-113, 2022 Amendments)

**The core rule:** Non-competes for employees and contractors in Colorado are extremely limited since the 2022 amendments. See `employment-labor` skill for the full analysis.

**For government contracting purposes:** Some RFPs include "organizational conflict of interest" provisions that restrict ENAC from working for other government clients on competing procurements. This is different from a non-compete and may be enforceable in the procurement context even if a commercial non-compete would not be.

**Protect ENAC's methodology through:**
- Trade secret classification (not non-competes)
- NDAs with all personnel on the engagement
- Background IP Schedule in every contract

---

## 6. Colorado AI Act (SB 24-205, February 2026)

See `colorado-ai-act` skill for full compliance guide.

**In the government contracting context:** Every proposal for a Colorado government engagement after February 1, 2026 must include AI disclosure language. If the engagement uses AI tools for analysis affecting employment, government services, or similar consequential decisions, ENAC must have a risk management program in place.

---

## 7. Adams County PSA: Known Risk Map

The standard Adams County Professional Services Agreement contains the following specific risks. Review each on every Adams County contract:

| Section | Issue | Rating | Required Action |
|---------|-------|--------|----------------|
| §1.2 | Emergency services obligations, potentially unlimited | YELLOW | Define "emergency," require change order for emergency scope, or price separately |
| §4.2.2 | Price reduction right: county may demand price reduction if similar services offered cheaper | YELLOW | Narrow to identical service scope; document what services are comparable |
| §4.3 | Missing payment terms: no payment schedule defined | RED | Add: Net 30 from invoice receipt, monthly in arrears, interest on late payment |
| §7.1 | Uncapped, one-sided indemnification | RED | Cap at fees paid; negligence standard; do not sign uncapped |
| §8 | Insurance requirements | YELLOW | Verify current ENAC coverage meets requirements; confirm additional insured endorsement available |
| §11.1 | Termination for cause with no cure period | RED | Add 30-day notice + 30-day cure period before termination effective |
| §12.12 | All documentation becomes county property: IP assignment | RED | Insert Background IP Schedule carve-out; walk-away issue without it |
| §13 | Confidentiality: no CORA trade secret protection | RED | Add CORA notice requirement and trade secret assertion rights |
| §14 | PII obligations: C.R.S. 24-73-101 | YELLOW | Confirm ENAC's data handling procedures meet standard; route to `@legal-privacy` |
| §15 | WCAG 2.1 AA accessibility indemnification | YELLOW | Confirm all deliverables will meet WCAG standard; build into production workflow |
| §16, Exhibit B | Immigration certification: signed under penalty of perjury | RED | Verify accuracy before signing; calendar annual renewal date immediately |

---

## 8. Mandatory Negotiation Positions for Adams County PSA

These are ENAC's non-negotiable positions. Prepare these redlines before the first review conversation.

### IP (Walk-Away Issue)
"Contractor retains all right, title, and interest in and to its pre-existing intellectual property, methodologies, frameworks, templates, tools, prompts, and know-how ('Background IP'), including any improvements, modifications, or derivatives thereof developed during the engagement. Contractor grants County a perpetual, royalty-free, non-exclusive, non-transferable license to use Background IP solely to the extent embedded in the final deliverables specifically identified in the Statement of Work for County's internal business purposes only. Final deliverables specifically prepared for and delivered to County ('Foreground IP') are owned by County, excluding Background IP incorporated therein. Contractor may use de-identified findings, learnings, and methodological improvements for portfolio, case study, and marketing purposes, subject to the confidentiality provisions herein."

### Indemnity (Must Negotiate)
"Contractor shall indemnify, defend, and hold harmless County from and against third-party claims arising from Contractor's negligence or willful misconduct in performance of the services under this Agreement, up to the total fees paid by County to Contractor under this Agreement."

### Termination for Cause (Must Negotiate)
"County may terminate this Agreement for cause upon thirty (30) days written notice specifying the alleged deficiency. Contractor shall have thirty (30) days from receipt of such notice to cure the identified deficiency. If the deficiency is cured within such period, termination shall be of no effect. If the deficiency is not cured within such period, termination shall be effective on the thirtieth day following the expiration of the cure period."

### Payment Terms (Must Negotiate)
"County shall pay each invoice submitted by Contractor within thirty (30) days of receipt. Contractor shall submit invoices monthly in arrears on or before the fifth business day of each month for services performed in the preceding month. Invoices not paid within thirty (30) days of receipt shall accrue interest at the rate of 1.5% per month on the outstanding balance."

### Scope Definition
"The scope of services, deliverables, fees, and schedule are governed by Exhibit A (Contractor's Proposal). This Agreement governs the legal terms and conditions. In the event of any conflict between this Agreement and Exhibit A regarding scope, fees, or schedule, Exhibit A shall control."

### CORA Trade Secret Protection
"County acknowledges that all methodologies, frameworks, tools, and proprietary approaches submitted by Contractor constitute trade secrets under C.R.S. 24-72-204(3)(a)(IV) and are marked accordingly. Prior to disclosing any Contractor materials in response to any request made pursuant to the Colorado Open Records Act (C.R.S. 24-72-201 et seq.), County shall provide Contractor written notice within five (5) business days of receiving such request and shall afford Contractor a reasonable opportunity to seek appropriate relief."

---

## 9. Cooperative Purchasing Provision

Adams County contracts often include a provision allowing other Colorado state and local entities to purchase from the same contract (cooperative purchasing or "piggyback" provisions).

**Opportunity:** This is a growth channel. If ENAC wins an Adams County contract with cooperative purchasing rights, other Colorado jurisdictions can contract directly without a separate competitive procurement.

**Risk:** Cooperative purchasing requires offering the same pricing to all participating entities. If ENAC offers lower rates later to another client, it may trigger a price reduction obligation.

**Strategy:**
- Price cooperative purchasing contracts at sustainable rates
- Scope the services specifically enough that different engagements (different scope) are not "the same services"
- Proactively market to Colorado jurisdictions that can piggyback on existing contracts

---

## 10. WCAG 2.1 AA Compliance (C.R.S. § 24-85-103)

**Required for all deliverables submitted to Colorado state and local government agencies.**

Every Word document, PDF, and slide deck must:
- Use a heading hierarchy (H1, H2, H3 in logical order; no skipped levels)
- Include alt text for all images, charts, and graphics
- Have a logical reading order (verify with Accessibility Checker)
- Meet color contrast requirements: 4.5:1 for normal text, 3:1 for large text
- Not use color as the only means of conveying information
- Have all linked text describe the destination (not "click here")

**Build this into the production workflow.** WCAG compliance is not a last step: it is a requirement throughout the drafting and design process. Communicate this requirement to `@cco` and `@cw` at the start of every government engagement producing deliverables.

**Adams County PSA §15:** ENAC indemnifies the county for inaccessible deliverables. The cheapest way to manage this indemnification risk is to make all deliverables accessible before delivery.

---

## Anti-Generic Rules

- NEVER submit ENAC materials to a Colorado government entity without marking them "Confidential: Trade Secret"
- NEVER sign an Adams County PSA without a Background IP carve-out: it is a walk-away issue
- NEVER accept unlimited indemnification from a Colorado county: cap at fees paid is reasonable and routinely accepted
- NEVER forget the annual immigration certification renewal: it is signed under penalty of perjury
- NEVER deliver a document to a Colorado government client without running WCAG 2.1 AA accessibility check
