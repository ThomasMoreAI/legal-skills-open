---
name: triage-nda-nmoralescyber
title: legal:triage-nda — NDA Pre-Screening
description: Rapidly triage an inbound standalone NDA (mutual or unilateral) and classify it GREEN (sign under standard delegation), YELLOW (counsel review needed), or RED (full legal review / counterproposal). Use when the user attaches or pastes an NDA and asks "is this standard?", "can we sign this?", "any landmines in this NDA?", "screen this NDA", "GREEN/YELLOW/RED this", or any equivalent fast-screen request — especially to catch embedded non-solicits, non-competes, residuals, perpetual confidentiality, hidden IP grants, or missing carveouts. Do NOT use for full multi-page commercial agreements with confidentiality sections embedded (use legal:review-contract), for drafting an NDA from scratch or responding to an NDA request (use legal:legal-response or legal:review-contract for the counterproposal pass), for checking what NDAs are already on file with a counterparty (use legal:vendor-check), for auditing the user's own NDA template (use legal:legal-audit), or for sending an already-approved
  NDA for signature (use legal:signature-request).
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/triage-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# legal:triage-nda — NDA Pre-Screening

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Triage an inbound standalone NDA against screening criteria and classify it for routing: **GREEN** (standard approval), **YELLOW** (counsel review), **RED** (full legal review).

**Important**: This is a pre-screening tool, not legal advice. A qualified attorney should review anything you are uncertain about.

## When to use this skill vs. an adjacent one

| If the user wants to… | Use this skill | Use instead |
|---|---|---|
| Triage a standalone NDA in 2 minutes | legal:triage-nda | — |
| Negotiate a multi-clause MSA / SOW (even with confidentiality section) | — | legal:review-contract |
| Draft a fresh NDA from scratch or respond to an NDA request | — | legal:legal-response (template) → legal:review-contract (if counterproposal needed) |
| Find out what NDAs are already signed with a counterparty | — | legal:vendor-check |
| Audit the user's own NDA template | — | legal:legal-audit |
| Send an already-finalized NDA for signature | — | legal:signature-request |

## Invocation

```
legal:triage-nda
```

Triage the NDA: @$1

## Workflow

### Step 1: Confirm it is actually an NDA

Before anything else, confirm the document is a **standalone confidentiality agreement** of <20 pages with confidentiality as the primary purpose.

**STOP and redirect** if any of the following are true:
- Document contains substantive commercial terms (pricing, deliverables, SOW) → recommend `legal:review-contract`
- Document is a confidentiality section embedded in a larger MSA / SOW → recommend `legal:review-contract`
- User is asking for a draft, not a triage → recommend `legal:legal-response` for templated draft, or `legal:review-contract` for counterproposal review
- User is asking what is on file → recommend `legal:vendor-check`

If it is genuinely a standalone NDA, proceed.

### Step 2: Fast-path screen (target: <2 minutes)

**Skip the context-gathering turn for triage.** Unlike contract review, NDA triage should not stop to ask the user questions before screening — the document itself contains everything needed. Run the screen first, classify, and only ask for context if the classification depends on it (e.g., is this for an M&A discussion? — only matters if a standstill is present).

Run the **6-checkpoint fast screen**. If all 6 pass cleanly, the NDA is GREEN — emit the report immediately without running the deep checklist or the embedded-term hunt.

| # | Fast checkpoint | Pass condition |
|---|---|---|
| 1 | **Type / direction** | Mutual (or unilateral in the right direction for the relationship) |
| 2 | **Term** | Agreement ≤3 yrs; confidentiality survival ≤5 yrs (trade secrets may extend); NOT perpetual |
| 3 | **All 5 standard carveouts present** | Public knowledge, prior possession, independent development, third-party receipt, legal compulsion |
| 4 | **No prohibited embedded terms** | No non-solicit, no non-compete, no exclusivity, no standstill (unless M&A), no liquidated damages, no IP assignment / license, no broad residuals |
| 5 | **Definition scope** | Reasonable; not "all information of any kind whether or not marked" |
| 6 | **Governing law** | Established commercial jurisdiction; consistent with venue |

If any checkpoint fails or is ambiguous, escalate to the **deep checklist** in Step 3.

### Step 3: Deep checklist (only when fast screen flagged something)

#### Load NDA playbook
Look for `legal.local.md` or similar. Defaults if not present:
- Mutual obligations required (unless the user is solely disclosing)
- Term: 2–3 yrs standard, up to 5 for trade secrets
- All 5 standard carveouts required
- No non-solicit, non-compete, exclusivity, standstill, residuals (or narrowly-scoped residuals only)
- Reasonable commercial governing law

#### Full screening criteria

**Agreement structure** — type identified; appropriate for context; standalone (not embedded).

**Definition of confidential information** — reasonable scope; workable marking requirements (written marking within 30 days of oral disclosure is standard); no problematic inclusions of public/independently-developed material.

**Receiving party obligations** — reasonable standard of care; use restricted to stated purpose; disclosure restricted to need-to-know recipients under similar obligations; no impractical operational obligations.

**Standard carveouts (all 5 must be present):** public knowledge, prior possession, independent development, third-party receipt, legal compulsion (with notice where legally permitted).

**Permitted disclosures** — employees, contractors/advisors under similar obligations, affiliates if needed for the purpose, legal/regulatory.

**Term & duration** — agreement 1–3 yrs standard; confidentiality survival 2–5 yrs (longer for trade secrets); NOT perpetual.

**Return & destruction** — triggered on termination or request; reasonable scope; retention exception for legal/compliance/backup; certification of destruction OK, sworn affidavit is onerous.

**Remedies** — injunctive relief acknowledgment is standard; no liquidated damages; mutual remedies in mutual NDAs.

**Problematic provisions** — flag any of: non-solicit, non-compete, exclusivity, standstill (non-M&A), broad residuals, IP assignment/license, audit rights, liquidated damages.

**Governing law & venue** — reasonable jurisdiction; consistent law/venue; no mandatory arbitration in standard NDAs.

### Step 4: Classify

**YELLOW vs. RED boundary (when in doubt):**
- If the issue can be fixed by **adding or tightening language** without changing the deal, it's YELLOW.
- If the issue requires **deleting an entire embedded provision** (non-solicit, non-compete, exclusivity, IP grant, liquidated damages), it's RED.
- If the issue requires **counterproposing the user's standard form** because the counterparty's paper is structurally hostile, it's RED.
- If the issue **could trigger regulatory exposure** (missing carveout for legal compulsion in a regulated-data context, perpetual confidentiality on PII), it's RED.
- When you would need to draft >2 separate redlines to fix a single document, escalate from YELLOW to RED — it's no longer a "single review pass".


#### GREEN — Sign under standard delegation
**All** of the following true:
- Mutual (or correctly-directed unilateral)
- All 5 standard carveouts present
- Term within standard range
- No non-solicit, non-compete, exclusivity, standstill, residuals (or narrowly scoped)
- No hidden IP grant, no liquidated damages
- Reasonable governing law
- Permitted disclosures cover employees/contractors/advisors
- Return/destruction has retention exception
- Definition reasonably scoped

**Action**: Approve under delegated authority. Same-day signature.

#### YELLOW — Counsel review (likely resolvable in one redline pass)
One or more of:
- Definition broader than preferred but not unreasonable
- Term longer than standard but within market (e.g., 5 yr agreement, 7 yr survival)
- One standard carveout missing but easily added
- Narrowly-scoped residuals clause limited to unaided memory
- Non-preferred but acceptable governing law
- Minor mutual-NDA asymmetry
- Workable marking requirements
- Missing explicit retention exception (likely implied)
- Unusual but non-harmful obligations (e.g., breach-notification duty)

**Action**: Send to counsel with the specific issues flagged; expect 1–2 business days.

#### RED — Full legal review / counterproposal
One or more of:
- Unilateral when mutual is required (or wrong direction)
- Missing critical carveouts (especially independent development or legal compulsion)
- **Non-solicitation or non-compete embedded in the NDA**
- **Exclusivity or standstill** without business justification
- **Unreasonable term** (10+ yrs or perpetual without trade-secret basis)
- **Overbroad definition** capturing public or independently-developed material
- **Broad residuals clause** functioning as a use license
- **Hidden IP assignment or license grant**
- **Liquidated damages or penalty**
- Audit rights without reasonable scope/notice
- Highly unfavorable jurisdiction with mandatory arbitration
- Document is not actually an NDA

**Action**: Do not sign. Engage counsel. Counterpropose with the user's standard form NDA (3–5 business days).

### Step 4a: Counsel escalation decision tree (what auditor counsel would actually escalate)

Real counsel does not escalate proportionally to the number of issues — they escalate by **risk asymmetry**. Apply this decision tree before emitting classification:

```
Q1. Does the document create a restraint on the SIGNER's future business conduct
    (non-solicit, non-compete, exclusivity, standstill, IP grant)?
    YES → RED. Counsel always escalates these — state-by-state enforceability,
          downstream M&A friction, employee mobility risk. Even "narrow" ones.
    NO  → Q2.

Q2. Does the document create REGULATORY exposure if signed as-is?
    (perpetual confidentiality on PII; missing legal-compulsion carveout; AI training
    carve-in absent or overbroad; bilingual NDA with ambiguous governing language;
    PR-resident personal data in scope without DPA path; PHI without BAA path)
    YES → RED if exposure is concrete (regulator could fine); YELLOW if it's a
          gap that can be closed by a side letter or addendum.
    NO  → Q3.

Q3. Is the issue STRUCTURAL (counterparty's paper is hostile by design)
    or COSMETIC (one or two sloppy clauses)?
    STRUCTURAL → RED. Counterpropose your standard form.
                 Examples: definition captures public info AND no carveouts AND
                 perpetual term — the paper was drafted to be one-sided.
    COSMETIC   → YELLOW. Single redline pass.

Q4. Does the issue compound? (e.g., overbroad definition + missing independent-
    development carveout + 7-yr survival together create the same effect as a
    use license, even though no single clause is RED)
    YES → Escalate from YELLOW to RED. Counsel reads cumulative effect.
    NO  → Hold YELLOW.

Q5. Is the counterparty in a regulated or sensitive sector that changes the
    risk profile? (cybersec vendor, healthcare, financial services, government,
    foreign-government-adjacent)
    YES → Escalate one step. GREEN→YELLOW, YELLOW→RED.
    NO  → Hold classification.
```

**Counsel-asymmetry rules (commit these to behavior):**
- Counsel will sign a sloppy NDA missing one carveout faster than a clean NDA with a 1-year non-solicit. Restraints on future conduct outrank carveout completeness.
- Counsel treats AI/LLM-training carve-ins as a top-three issue in 2026 — flag absence or overbroad presence as YELLOW minimum.
- Counsel treats missing AI carve-out + cybersec/security customer + counterparty operates ML systems = RED (training on confidential pen-test data is a material risk).
- Counsel treats bilingual (EN-ES) NDAs as YELLOW by default unless governing-language clause is explicit and unambiguous.
- Counsel treats unilateral-receiving NDAs from prospects evaluating the user's security product as a different risk profile (the user is the disclosing party of customer data and pen-test findings — apply stricter scrutiny on counterparty's use restrictions).

### Step 5: Generate triage report

```
## NDA Triage Report

**Classification**: [GREEN / YELLOW / RED]
**Parties**: [names]
**Type**: [Mutual / Unilateral (disclosing) / Unilateral (receiving)]
**Term**: [agreement / survival]
**Governing Law**: [jurisdiction]
**Review Basis**: [Playbook / Default Standards]
**Time-to-classify**: [fast-path / deep-checklist]

## Fast-Screen Results
| # | Checkpoint | Status | Notes |
|---|---|---|---|
| 1 | Type / direction | [PASS / FLAG / FAIL] | |
| 2 | Term | | |
| 3 | Standard carveouts (5) | | |
| 4 | No prohibited embedded terms | | |
| 5 | Definition scope | | |
| 6 | Governing law | | |

## Issues Found
### [Issue 1 — YELLOW/RED]
**What**: [description, with section reference]
**Risk**: [what could go wrong, in business terms]
**Suggested Fix**: [specific language or approach]

[Repeat per issue]

## Recommendation
[Approve / Send to reviewer with notes / Reject and counterpropose]

## What slips through under standard delegation (GREEN only)
For every GREEN classification, explicitly enumerate what the NDA does NOT cover, so the user understands the boundaries of what they just approved. Include where applicable:

- **Personal data**: NDA is not a DPA. If counterparty will process EU/PR/CA personal data, a DPA is still required (GDPR Art. 28; PR Ley Núm. 111).
- **PHI**: NDA is not a BAA. If PHI will be exchanged, HIPAA still requires a separate BAA.
- **Card data**: NDA does not impose PCI-DSS obligations.
- **AI / LLM training**: standard NDAs do not bar counterparty from using inputs to "improve services" — call this out explicitly if the receiving party operates AI/ML systems.
- **Data residency**: confidentiality ≠ residency commitment.
- **Right to audit**: GREEN NDAs typically have none. If the relationship later requires assurance over confidentiality controls, a separate addendum is needed.
- **Non-solicit / non-compete**: GREEN means there are NONE. If the user expected one, it must be in a separate agreement.
- **IP ownership / license**: GREEN means there is NO IP grant in either direction. Pre-existing IP stays put; no work product is licensed.
- **Survival window**: name the exact survival period and the date it ends, so the user knows when obligations expire.

## Next Steps
1. [Action]
2. [Action]
```

### Step 6: Routing

| Classification | Recommended action | Typical timeline |
|---|---|---|
| GREEN | Approve and route per delegation of authority | Same day |
| YELLOW | Send to designated reviewer with flagged issues | 1–2 business days |
| RED | Engage counsel; prepare counterproposal or send standard form | 3–5 business days |

For YELLOW/RED, name the reviewer/role if defined in the playbook; include a 3-bullet summary of issues.

**Connector-driven auto-routing.** Check `CONNECTORS.md` for available integrations and route accordingly:
- **Slack present**: post YELLOW summary to `#legal-nda-review`; post RED summary + redline ask to `#legal-counsel-escalation` (or playbook-defined channel). Use `mcp__plugin_product-management_slack__*`.
- **Gmail / MS365 present**: draft YELLOW email to designated reviewer; draft RED email to outside counsel with NDA attached and 3-bullet issue summary. Do NOT auto-send — surface as draft for user approval.
- **Docusign present**: for GREEN only, hand off to `legal:signature-request` (do not route directly to Docusign from this skill — keep separation of concerns).
- **No integrations connected**: emit routing recommendation as plain text in the report; do not block.

For RED matters with regulatory exposure (PII, PHI, AI training, perpetual confidentiality on regulated data), additionally recommend invoking `legal:legal-risk-assessment` for severity-by-likelihood scoring.

## Common NDA issues — standard positions

**Overbroad definition**: limit to information marked or that a reasonable person would understand to be confidential given nature and circumstances.

**Missing independent-development carveout**: high-priority add. Risk if missing: claims that internally-developed products were derived from counterparty's confidential information.

**Non-solicitation of employees**: does not belong in an NDA. Delete entirely; if pushed, limit to targeted (not general) solicitation, 12-month max.

**Broad residuals**: resist; if required, limit to (a) general ideas/concepts/know-how/techniques in unaided memory of authorized recipients; (b) explicitly exclude trade secrets and patentable info; (c) does not grant any IP license.

**Perpetual confidentiality**: replace with 2–5 yrs; offer trade-secret carveout for longer protection of qualifying info only.

**Cybersec / PR-specific watchouts (the operator's context)**:
- If the NDA covers exchange of personal data of EU/PR/CA residents, note that confidentiality is **not** a substitute for a DPA — flag and recommend a DPA execute alongside.
- If the NDA is for a pen-test or red-team engagement, ensure carveouts permit disclosure to law enforcement on discovered illegality, and that confidentiality does not bar publishing aggregated/anonymized findings.
- If the counterparty is processing PHI, confidentiality is not a BAA — flag separately.
- Watch for AI/LLM-training clauses in the definition section — increasingly common, often hidden as "use of inputs to improve services".

**Embedded-pattern taxonomy (run before classifying — covers the 6 categories of things that hide in NDAs):**

Each pattern: regex-like signal → why it matters → default class → false-positive caveat.

#### Category 1 — Restraints on future conduct (almost always RED)

| Pattern | Why | Default | FP caveat |
|---|---|---|---|
| `solicit\|hire\|employ\|recruit` + `employee\|personnel\|staff\|contractor` | Non-solicit | RED | Mutual no-poach between joint-venture partners may be defensible — still escalate |
| `compete\|competing\|competitive` + `business\|product\|service\|line of business` | Non-compete | RED | "Non-circumvention" wording is a milder cousin — still RED until counsel reviews |
| `exclusive\|exclusivity\|sole.{0,20}(provider\|source)` + `discussions\|negotiations\|relationship` | Exclusivity lock-in | RED unless M&A context | "Exclusive remedy" (legal phrase) is NOT exclusivity — different concept |
| `standstill\|will not acquire\|will not purchase\|tender offer` | Standstill | RED unless M&A | M&A standstills are normal in deal NDAs but require business confirmation |
| `non-circumvention\|circumvent\|bypass.{0,20}direct` | Non-circumvention | RED | Common in broker / introducer contexts — still escalate |
| `right of first refusal\|right of first offer\|ROFR\|ROFO` | ROFR/ROFO | RED | Does not belong in an NDA |

#### Category 2 — Hidden IP grants (RED)

| Pattern | Why | Default | FP caveat |
|---|---|---|---|
| `assign\|assignment` + `intellectual property\|IP\|inventions\|improvements\|derivative works` | IP assignment | RED | "No assignment" or "shall not assign this Agreement" is the opposite — confirm direction |
| `license\|grant.{0,20}right` + `confidential information\|disclosing party.{0,20}material` | Use license | RED | Reasonable license-back to use the info for the stated purpose only is normal — flag if scope exceeds purpose |
| `feedback\|suggestions\|improvements\|comments` + `perpetual\|irrevocable\|royalty-free\|sublicensable` | Feedback grant | YELLOW→RED if sublicensable | Receiving party may need a narrow license-back to act on feedback — limit scope |
| `work product\|work-for-hire\|works made for hire` | Hidden work-for-hire | RED | Belongs in an SOW, not an NDA |
| `joint.{0,20}invention\|jointly.{0,20}developed` | Joint-IP rules | YELLOW | Common in collaborative R&D NDAs but needs explicit ownership rules |

#### Category 3 — Hidden liability and remedy expansion (RED)

| Pattern | Why | Default | FP caveat |
|---|---|---|---|
| `liquidated damages\|stipulated damages\|US?\$[\d,]+.{0,20}(per.{0,20}breach\|each.{0,20}violation)` | Liquidated damages | RED | "Reasonable estimate of actual damages" framing is still LD — escalate; PR civil-code "cláusula penal" follows same rule |
| `indemnif(y\|ication)` + `confidential information\|breach` | Indemnity expansion | YELLOW | Mutual narrow indemnity for IP infringement is OK; broad indemnity for any breach is RED |
| `consequential\|indirect\|special.{0,20}damages` without `excluded\|disclaim` | Consequential damages NOT carved out | YELLOW | Default rule varies by jurisdiction — flag if absent |
| `attorney(s)?'? fees\|legal fees\|costs of enforcement` + `prevailing party` | Fee-shifting | YELLOW | Normal in some jurisdictions; one-sided fee-shifting is RED |
| `personal guarantee\|personally liable` | Individual liability | RED | Should never appear in a corporate NDA |

#### Category 4 — Term and survival traps (RED unless trade-secret limited)

| Pattern | Why | Default | FP caveat |
|---|---|---|---|
| `perpetual\|in perpetuity\|forever\|no expiration\|indefinite` | Perpetual confidentiality | RED unless trade-secret only | Trade-secret-only perpetual survival is acceptable — confirm scope is limited |
| `survive.{0,30}termination` without explicit period | Open-ended survival | YELLOW | Common drafting tic; ask for explicit period |
| `automatic.{0,20}renew\|auto-renew\|evergreen` | Evergreen term | YELLOW | NDAs rarely need renewal — ask why |

#### Category 5 — Regulatory carve-in / carve-out gaps (YELLOW or RED depending on data type)

| Pattern | Why | Default | FP caveat |
|---|---|---|---|
| `improve.{0,20}services\|train.{0,20}model\|machine learning\|artificial intelligence\|AI.{0,20}system\|LLM` | AI-training carve-in | YELLOW (RED if cybersec/pen-test data in scope) | Look for whether it's a carve-in (counterparty allowed to train) or carve-out (counterparty barred) |
| Absent: `legal compulsion\|required by law\|court order\|subpoena` | Missing legal-compulsion carveout | RED | Critical for regulated-data contexts — without it, contract conflicts with discovery / subpoena obligations |
| Absent: `independently developed\|independent development` | Missing ID carveout | RED | Highest-impact missing carveout |
| Absent: `publicly known\|public domain\|public knowledge` | Missing public-info carveout | RED | Definitional flaw — definition would capture unprotectable info |
| `personal data\|personally identifiable\|PII\|personal information` without DPA reference | Privacy-data scope without DPA path | YELLOW (RED if EU/PR/CA residents in scope) | NDA is not a DPA — flag GDPR Art. 28 / PR Ley 111 / CCPA |
| `protected health information\|PHI\|HIPAA` without BAA reference | PHI without BAA path | RED | NDA is not a BAA |
| `cardholder data\|payment card\|PCI` | Card data in scope | RED | NDA does not impose PCI-DSS — refer separately |
| `vulnerability\|pen.?test\|penetration test\|red team\|exploit` + `disclos\|publish\|report` restriction | Cybersec disclosure restriction | RED | Must permit law-enforcement disclosure and CVE publication |

#### Category 6 — Operational booby-traps (YELLOW)

| Pattern | Why | Default | FP caveat |
|---|---|---|---|
| `audit\|inspect.{0,20}records\|on-site.{0,20}inspection` | Audit rights | YELLOW | Unusual for NDA — common in DPAs / vendor agreements; flag for migration |
| `notif(y\|ication).{0,30}(breach\|disclosure).{0,30}\d+.{0,20}(hour\|day)` | Tight breach-notification SLA | YELLOW | Sub-24-hour SLAs are operationally hard — flag |
| `most favored\|MFN\|most-favored-nation` | MFN clause | RED | Does not belong in an NDA |
| `affiliate\|subsidiary\|parent.{0,30}bound` | Affiliate-binding | YELLOW | Defines who is on the hook; reasonable but flag scope |
| `unilateral.{0,20}amend\|change at any time\|sole discretion.{0,20}modify` | Unilateral amendment | RED | One-sided modification right is structurally hostile |
| `governing language\|controlling language\|equally authentic` | Bilingual language clause | YELLOW | If "equally authentic" with no controlling — flag PR addendum |

#### Category 7 — Drafting tells that suggest a hostile template (raise scrutiny one notch)

These don't classify on their own but signal counterparty's paper is one-sided — escalate one classification level:
- Defined terms used before defined (sloppy drafting → may hide more)
- "Sole discretion" appearing 5+ times
- All obligations one-directional in a "mutual" NDA
- Definition section longer than obligations section
- Any clause titled "Additional Provisions" or "Miscellaneous" buried at the end (always read these — landmines hide here)

#### Cumulative effect rule
If multiple patterns hit across categories 1-5, classify RED even if each individually is YELLOW. Counsel reads cumulative effect (see Step 4a Q4).

## Puerto Rico-specific addendum

When governing law is Puerto Rico, when the disclosing or receiving party is PR-domiciled, or when PR-resident personal data is in scope:

- **Bilingual EN-ES NDAs**: confirm the **governing-language clause** is explicit. If both versions are stated as "equally authentic" without a controlling language, classify YELLOW — ambiguity in interpretation is a material risk.
- **Ley Núm. 111-2005 (PR data protection)**: any NDA that touches PR-resident personal data triggers a DPA-required carveout. NDA alone is insufficient. Flag in GREEN report; treat absence-of-DPA-path as YELLOW.
- **PR civil-law tradition**: liquidated-damages ("cláusula penal") is enforceable under PR Civil Code Art. 1106 but courts may moderate excessive amounts. Still treat as RED for triage — counsel needs to size.
- **Non-compete enforceability in PR**: PR follows reasonableness review (Arthur Young v. Vega III, 1991). Embedded non-competes are still RED — refer to counsel.
- **Forum-selection in PR**: federal District of PR vs. Tribunal de Primera Instancia distinction matters; do not classify as ambiguous, just flag for counsel review.

## Worked examples

### Example A — Clear GREEN
**Input**: Mutual NDA between Acme Corp (Delaware) and the user's company. 2-yr term, 3-yr survival. All 5 carveouts present. No non-solicit, no IP grant, no residuals. Definition limited to "information marked confidential or that a reasonable person would understand to be confidential". Delaware governing law. Standard return/destruction with retention exception.
**Decision**: GREEN.
**Reasoning**: All 6 fast-screen checkpoints pass. No restraints on future conduct (Q1: NO). No regulatory exposure flagged (Q2: NO). Cosmetic if anything. No counterparty sector escalation.
**Routing**: Approve under delegated authority; same-day signature via `legal:signature-request`. Triage report enumerates GREEN-coverage gaps (no DPA, no BAA, no audit rights) so user knows the boundaries.

### Example B — Clear YELLOW
**Input**: Mutual NDA from a SaaS prospect. 5-yr agreement / 7-yr survival (longer than standard). 4 of 5 carveouts present (independent-development carveout missing). Definition slightly broader than preferred. No embedded restraints. California governing law. Otherwise clean.
**Decision**: YELLOW.
**Reasoning**: Q1 NO (no restraints). Q2 NO (no regulatory exposure). Q3 COSMETIC (two issues, both fixable with a single redline pass: add ID carveout + tighten definition or accept term as within market). Q4 cumulative effect not amounting to use license.
**Routing**: Send to designated reviewer with two-bullet issue list. Slack post to `#legal-nda-review` if connected. 1–2 business days.

### Example C — RED with embedded landmines
**Input**: Mutual NDA from a Fortune-500 enterprise customer. Looks standard at first pass. But buried in section 9 ("Permitted Uses") is a sentence: *"Receiving Party shall not, for a period of 24 months, directly or indirectly solicit for employment any employee of Disclosing Party with whom Receiving Party had contact under this Agreement."* Section 12 contains a **perpetual** confidentiality obligation. Section 14 includes liquidated damages of "$50,000 per breach". Definition is reasonable; carveouts present.
**Decision**: RED.
**Reasoning**: Q1 YES — non-solicit (24 months). RED immediately. Even if Q1 were NO, Q2 catches the perpetual confidentiality (regulatory exposure on PII over time) and Q3 catches liquidated damages (structural hostility — these are drafted in deliberately). High-signal embedded-term hunt would also fire on `solicit|hire` + `employee` and `perpetual|forever` and `liquidated damages`.
**Routing**: Do not sign. Engage counsel; counterpropose user's standard form. Slack post to `#legal-counsel-escalation`. Invoke `legal:legal-risk-assessment` for the perpetual-confidentiality + PII risk. 3–5 business days.

### Example D — RED with multi-clause non-solicit/non-compete
**Input**: Mutual NDA from a strategic partner. Section 7: "Non-Solicitation" — 18 months, all employees and contractors. Section 8: "Non-Competition" — Receiving Party agrees not to develop "competing products" in defined verticals for 12 months. Section 11: IP — "any improvements, derivative works, or feedback related to Disclosing Party's confidential information shall be assigned to Disclosing Party". Otherwise reasonable definition, term, carveouts.
**Decision**: RED — escalated.
**Reasoning**: Q1 YES, three times (non-solicit + non-compete + IP assignment). This is not an NDA — it's a partnership-restraint agreement disguised as an NDA. Counsel-asymmetry rule: restraints on future conduct outrank everything. Multi-clause restraint = automatic counterproposal. Q5 if counterparty is in cybersec/regulated sector, escalate further.
**Routing**: Do not sign. Engage counsel. Counterpropose user's standard NDA AND require these three sections be deleted in their entirety. If counterparty insists on non-solicit, refer to `legal:review-contract` for full multi-clause negotiation — this is no longer NDA triage. Slack post to `#legal-counsel-escalation` with explicit "structural hostility" flag.

### Example E — Ambiguous borderline (the hard case)
**Input**: Mutual NDA from a PR-domiciled cybersecurity vendor. Bilingual EN-ES, both "equally authentic" with no controlling-language clause. 3-yr term / 5-yr survival. All 5 carveouts present. No non-solicit. But: (a) definition includes "any information regarding security vulnerabilities or pen-test findings, in perpetuity"; (b) AI/LLM training clause absent; (c) PR governing law (Tribunal de Primera Instancia, San Juan); (d) the user is the disclosing party of pen-test findings.
**Decision**: RED.
**Reasoning**: Looks YELLOW on first pass. But apply decision tree: Q1 NO (no restraints). Q2 YES — the perpetual carve-in for security findings is regulatory-adjacent (could prevent disclosure to law enforcement on discovered illegality, could prevent CVE publication). Q3 borderline structural — bilingual ambiguity + perpetual security-finding clause + missing AI carveout + PR forum together compound. Q4 cumulative effect is material. Q5 cybersec sector + user is disclosing party = escalate. PR addendum: bilingual without governing language = YELLOW alone, RED in combination.
**Routing**: Do not sign. Engage counsel familiar with PR civil law and cybersec disclosure norms. Counterpropose: (i) controlling-language clause (English controls; Spanish translation for convenience), (ii) carveout permitting CVE publication and law-enforcement disclosure, (iii) AI-training prohibition, (iv) survival period not perpetual. Slack post to `#legal-counsel-escalation` flagged as bilingual + PR + cybersec.

## Notes
- Document not actually an NDA → flag immediately as RED and recommend `legal:review-contract`.
- NDA embedded in a larger agreement → broader context affects analysis; recommend `legal:review-contract`.
- This is a screening tool — counsel should review anything the user is uncertain about.
- For full multi-clause contract negotiation beyond NDA scope, defer to `legal:review-contract`.
- For paperwork inventory rather than triage of a new doc, defer to `legal:vendor-check`.
- For post-triage signing workflow, defer to `legal:signature-request`.
- For drafting an NDA from scratch (templated response), defer to `legal:legal-response`.
- For severity-by-likelihood risk scoring on RED matters, invoke `legal:legal-risk-assessment`.
