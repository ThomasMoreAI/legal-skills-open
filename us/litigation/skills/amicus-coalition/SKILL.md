---
name: amicus-coalition
title: Amicus Coalition Management
description: Manages end-to-end workflow for multi-organization amicus coalition briefs in appellate courts. Covers single-pen drafting governance, position alignment, conflict resolution, documented sign-offs, FRAP 29/Rule 37.6 disclosures, FRAP 26.1 corporate disclosures, cover formatting for multiple amici, and compliant filing. Use when coordinating coalition amicus briefs, managing sign-offs, drafting joint friend-of-court briefs, handling multi-amici filing, or resolving inter-organization conflicts. Triggers on phrases like "coalition brief," "12 orgs joining this amicus," or "coordinate the amicus."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/amicus-coalition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Amicus Coalition Management

Coordinates multi-organization amicus briefs from intake through filing. Prevents the most common coalition failures: unauthorized org listings, missed sign-off deadlines, incomplete disclosures, version proliferation, and unresolved policy disagreements.

## Quick Start

1. Gather intake (Checkpoint A below)
2. Establish governance and backward timeline from filing deadline
3. Align positions via Issue-Framing Memo
4. Draft under single-pen authority with controlled circulation
5. Resolve conflicts; escalate if needed
6. Execute two-step sign-off protocol
7. Verify disclosures, format cover/caption, file

**Defaults** (when user says "use defaults" or "just draft"): forum-agnostic draft with `[VERIFY FORUM]` markers; single-pen authority with lead counsel; sign-off cutoff 48 hours before filing deadline.

## Checkpoint A: Pre-Draft Intake

Gather before drafting. Do not proceed until collected or gaps flagged.

1. **Docket** — court, case number, caption, all deadlines
2. **Parties' briefs** — opening, response, reply (as available); key orders
3. **Forum rules** — word/page limits, disclosure requirements, consent/leave rules, cover formatting, e-filing specs `[VERIFY per forum]`
4. **Coalition roster** — full legal names, jurisdiction of incorporation, display names, entity types
5. **Approval pathways** — authorized signatory per org, internal review chain, lead time
6. **Red lines** — positions each org cannot support or endorse
7. **Counsel-of-record** — names, bar numbers, addresses; pro hac vice needs
8. **Disclosure inputs** — per FRAP 29(a)(4)(E) / Rule 37.6: who authored, who funded
9. **Posture** — supporting which party (or neither); consent status or need for leave motion

## Core Workflow

### 1. Governance and Timeline

| Element | Action |
|---|---|
| Single-pen authority | Lead counsel controls narrative; coalition provides input, not co-drafting |
| Authority map | Per org: who commits to join, who approves final text, who speaks publicly |
| Backward timeline | Filing deadline → sign-off cutoff → final proof → near-final draft → outline |
| Hard cutoff | No sign-off by cutoff = excluded. No "pending approval" listings |

Send Workflow Memo at kickoff requiring: (1) one consolidated comment set by deadline, (2) written authorization by cutoff. State that absent authorization, the org will not be listed.

### 2. Position Alignment

1. Gather each org's desired emphasis (economic, technical, historical, policy)
2. Cross-check against parties' briefs to eliminate duplication
3. Produce **Issue-Framing Memo** (1-2 pages): proposed argument headings, key factual propositions with citations, empirical/technical materials, posture
4. Solicit red lines in writing before full draft

### 3. Draft Management

| Rule | Rationale |
|---|---|
| One official draft, one sender | Prevents version proliferation |
| Naming: `AmicusCoalition_Brief_Draft[N]_YYYYMMDD` | Version integrity |
| One point person per org, one consolidated comment set | Avoids conflicting markups |
| Triage: (a) legal/argument, (b) factual/citation, (c) policy/branding | Legal clarity governs over branding |
| All markup confidential (Model Rule 1.6) | No forwarding outside coalition |
| Late new sections require equal-length cut | Word-limit discipline |

### 4. Conflict Resolution

**Conflict types:**
- **Core** (org cannot be associated with the position) — narrow the position, modularize language, or allow withdrawal
- **Expressive** (emphasis/phrasing disagreement) — favor legal clarity and court credibility

**Compromise patterns:**
- Statutory avoidance: resolve on statutory grounds; address constitutional only if reached
- Narrow consensus: "Amici take no position on outer bounds of [test], but under any formulation, [party] prevails"
- Procedural framing: reframe around procedural deficiency vs. substantive policy

**Escalation:** Written issue log (contested text, positions, proposed resolution, deadline) → lead attorney → supported party's counsel if needed. Treat log as privileged work product.

Never draft language suggesting consensus where none exists (Model Rule 3.3).

### 5. Sign-Off Protocol

**Two-step authorization:**

1. **Join authorization** on near-final draft — written confirmation from authorized person that org joins the brief substantially as circulated, with counsel authorized for non-substantive edits
2. **Final confirmation** on filing version (if time permits)

| Rule | Detail |
|---|---|
| Written only | No verbal approvals |
| Verify signatory authority | Policy staff enthusiasm ≠ institutional authorization |
| Track entity names precisely | Distinguish association from its foundation |
| Re-confirm after substantive changes | Post-sign-off changes require new authorization |
| Default to exclusion | Missed cutoff = not listed |

### 6. Filing

**Cover format** `[VERIFY per forum]`:
```
BRIEF OF [LEAD AMICUS] AND [N] OTHER ORGANIZATIONS AS AMICI CURIAE
IN SUPPORT OF [PARTY]
```

**Disclosures checklist:**
- [ ] FRAP 29(a)(4)(E) / Rule 37.6 authorship and funding — every member
- [ ] FRAP 26.1 corporate disclosure — every corporate amicus
- [ ] Consent of parties stated, or motion for leave attached

**Filing checklist:**
- [ ] Consent/leave requirements verified `[VERIFY]`
- [ ] Service requirements confirmed (all parties, method, paper copies)
- [ ] Final cite-check — every citation verified
- [ ] All listed amici have timely written authorization
- [ ] Counsel info complete; bar admissions satisfy forum requirements
- [ ] PDF requirements met (bookmarks, fonts, OCR, color covers)
- [ ] Word/page count within limits
- [ ] Amicus list consistent across cover, interest statement, signature block, disclosures

**Internal filing certification** — record: authorizations received, orgs removed for missed cutoff, final word/page count, disclosure verification, filing method.

## Checkpoint B: Post-Draft Review

After delivering initial draft, confirm:

1. All orgs confirmed sign-off authority and review timeline?
2. Remaining red-line conflicts needing escalation?
3. Cover/caption format matches forum requirements?
4. All disclosure inputs (authorship, funding) collected from every member?

## Jurisdiction Notes

| Forum | Key Requirements |
|---|---|
| **Federal circuits** | FRAP 29; word limit varies by circuit; local rules on covers, e-filing, corporate disclosures; D.C. Circuit strict on non-duplication |
| **U.S. Supreme Court** | Rule 37, Rule 33.1 (booklet format), green cover for merits; Rule 37.3 timing strictly enforced |
| **State appellate** | Varies dramatically; many require motion for leave; different disclosure regimes `[VERIFY]` |
| **Admin tribunals** | Unique rules/customs; require rule-based confirmation, not inference |

Always retrieve and cite current official rules for the specific forum. Flag all unverifiable procedural statements with `[VERIFY]`.

## Common Pitfalls

- **Unauthorized listing** — never list an org without timely written authorization from a verified signatory
- **Disclosure gaps** — collect authorship/funding info from every member, not just lead org
- **Name mismatches** — verify entity names character-by-character across all brief sections
- **Fabricated consensus** — do not attribute positions to orgs that have not approved them (Model Rule 3.3)
- **Restating party briefs** — brief must deliver unique contribution the parties' briefs do not
- **Hallucinated rules** — never fabricate forum rules or filing requirements; use `[VERIFY]` for unconfirmed details

## Guidelines

- **Ethics**: Treat each amicus as client for conflicts (Model Rules 1.7-1.10) and confidentiality (1.6); check conflicts before accepting any org
- **Citations**: Every non-record factual claim needs a pinpoint citation; flag unverifiable with `[VERIFY]`
- **Adversarial lens**: Before filing, ask whether opponent could move to strike based on misstatements, undisclosed funding, or noncompliance
- **Anti-hallucination**: Use `[VERIFY]` for all unconfirmed procedural details
- **Attorney review required**: All outputs require attorney review before filing
