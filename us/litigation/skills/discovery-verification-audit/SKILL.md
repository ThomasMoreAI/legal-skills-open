---
name: discovery-verification-audit
title: Discovery Verification and Proof of Service Audit
description: Produces an attorney-grade audit memorandum assessing whether written discovery responses are legally binding and timely. Use this skill when the user mentions verification audit, discovery verification, proof of service review, signature authority, perjury clause compliance, deadline computation, mailbox rule extensions, service defects, waiver risk, or motion-to-compel deadline analysis. Also trigger when the user references FRCP 33(b)(3) verification, CCP 2015.5, 28 U.S.C. 1746, attorney vs. party verification, or asks for help checking whether discovery responses are properly executed. Even if the user just says "check these responses for defects" or "is this verification valid," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-verification-audit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, drafting, memo]
---

# Discovery Verification and Proof of Service Audit

## Why This Skill Exists

Unverified or improperly verified discovery responses are a legal nullity in many jurisdictions — they can be treated as no response at all, waiving objections and restarting motion-to-compel clocks. Yet verification defects are among the most overlooked issues in practice because they sit on back pages that attorneys rarely scrutinize. A single wrong signature (attorney where party is required), a missing perjury clause, or a botched deadline computation can be either a devastating vulnerability for your client or a powerful weapon against an opponent.

This skill produces a structured audit memorandum covering verification sufficiency, signature authority, proof of service, deadline computation, and defect risk assessment across federal and state forums.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Discovery set and responses** — propounding requests and full response package as served, including all signature/verification pages and attachments
2. **Proof(s) of service** — for both the requests and the responses; ECF notices, certified mail receipts, courier confirmations, or email headers if e-service is authorized
3. **Forum identification** — jurisdiction (state + county or federal district), governing procedural rules (FRCP, CCP, etc.), and any applicable local rules or standing orders
4. **Deadline modifiers** — stipulations, court orders, or extensions modifying response deadlines
5. **Party identity** — responding party type (individual, corporation, LLC, government entity), signer's name and title, and basis of authority
6. **Master service list** — all parties and counsel of record to verify service completeness
7. **Audit posture** — outgoing (pre-service QA) or incoming (opponent defect analysis)

**If the user doesn't respond**, apply and clearly label these defaults: incoming audit (opponent defect analysis); federal court; FRCP governing rules.

> If the verification page(s), proof of service, or any deadline-modifying order is missing, request those documents before reaching conclusions.

---

## Step 1: Confirm Scope and Posture

Document the audit scope:
- Discovery instruments audited (interrogatories / RFPs / RFAs / supplemental / amended responses)
- Audit posture: outgoing (pre-service QA) or incoming (opponent defect analysis)
- Governing rule set confirmed; any inferences flagged for attorney confirmation

---

## Step 2: Audit Verification Sufficiency

| Element | Required | Present | Notes |
|---|---|---|---|
| Affirmation responses are true and correct | ✓ | | |
| "Under penalty of perjury" language | ✓ | | |
| Correct jurisdictional reference in perjury clause | ✓ | | |
| Signed by party (not counsel, unless permitted) | ✓ | | |
| Date of signing | ✓ | | |
| Verification references specific discovery set | ✓ | | |
| Verification date ≤ proof-of-service date | ✓ | | |

**Perjury clause standards:**
- **Federal (28 U.S.C. § 1746):** "I declare under penalty of perjury under the laws of the United States of America that the foregoing is true and correct."
- **California (CCP § 2015.5):** Must state "under the laws of the State of California"; must include city and state of signing; if signed outside California, must specify CA law or be notarized.
- **Other forums:** Web-verify perjury statute language; flag `[VERIFY]` if unconfirmed.

---

## Step 3: Check Signature Authority and Capacity

| Party Type | Required Signer | Attorney Verification Permitted? |
|---|---|---|
| Individual | The individual party | Generally no |
| Corporation / LLC | Officer, managing agent, or authorized representative with knowledge | No (CA: only if party absent from county — but triggers privilege risk) |
| Partnership | General partner or authorized agent | No |
| Government entity | Authorized official | Forum-specific — confirm |

> Attorney verification where party verification is required = **fatal defect**. Flag privilege waiver risk as to sources.

---

## Step 4: Audit Proof of Service

Required elements:
- [ ] Date of service stated
- [ ] Method of service identified (must be an authorized method under applicable rules)
- [ ] Name and address / e-service address of each recipient
- [ ] Server's identity and signature (with perjury declaration where required)
- [ ] All parties on master service list included

**Service method authorization check:**
- Email/electronic service requires written consent, ECF registration, stipulation, or court order — flag "served via email" without documented authorization as potentially invalid
- Discrepancy between stated address and current service list = flag
- Responses served but verification mailed separately = flag; determine operative service date

---

## Step 5: Compute Deadlines

Show each step explicitly:

```
Trigger date (day of service, excluded):  [Date]
Baseline response period:                 [30 days — FRCP 33/34/36; state-specific]
End of baseline period:                   [Date]
Weekend/holiday rollover:                 [Next business day if Sat/Sun/holiday]
Service method extension:                 [See table]
Final deadline:                           [Date]
```

**Mailbox Rule Extensions by Forum and Method:**

| Forum | Mail | Overnight | Electronic / ECF | Personal |
|---|---|---|---|---|
| Federal (FRCP 6(d)) | +3 calendar days | +3 calendar days [VERIFY] | **None** (eliminated by 2016 amendment) | None |
| California (CCP § 1013) | +5 cal. days (in-state) / +10 cal. days (out-of-state) | +2 cal. days | +2 **court** days (CCP § 1010.6) | None |
| New York [VERIFY] | +5 cal. days | — | — | None |
| Other jurisdictions | Web-verify statute; flag `[VERIFY]` if unconfirmed | | | |

> **CA critical distinction:** Electronic service adds 2 **court days** (not calendar days) — a long weekend shifts the deadline further.

---

## Step 6: Inventory Defects and Assess Risk

| Defect | Severity | Consequence | Cure |
|---|---|---|---|
| No verification where party verification required | **Fatal** | Response = legal nullity; objections may be waived | Serve corrected party verification immediately |
| Attorney verification where party required | **Fatal** | Treated as unverified; privilege waiver risk | Party must re-execute |
| Missing "penalty of perjury" language | **Fatal** | Declaration ineffective | New verification |
| Wrong jurisdictional reference in perjury clause | **Fatal** | Declaration ineffective | New verification |
| Verification dated after proof-of-service date | **High** | Suggests responses served before verified | Investigate; may require re-service |
| "Floating" verification not identifying discovery set | **High** | Opponent may argue it doesn't cover served responses | Amended verification with specific reference |
| Unauthorized service method | **High** | Operative service date may be disputed or void | Confirm authorization; re-serve if needed |
| Not all parties served | **High** | Absent party not bound; motion deadlines may not run | Re-serve; reconcile against master service list |
| Wrong address on proof of service | **Technical** | Arguable invalid service | Corrected proof; confirm actual receipt |
| Missing date on verification | **Technical** | Curable | Serve corrected verification |

---

## Step 7: Produce Adversarial Risk and Strategic Notes

- Identify whether defects favor the auditing party (opponent's responses) or expose the client (client's responses)
- **CA motion-to-compel clock: CCP § 2030.300 — 45-day deadline is jurisdictional.** Filing on day 46 permanently forfeits the right to compel. Connect all computed dates to this risk.
- Unverified interrogatory responses in CA = no response at all (*Appleton v. Superior Court* (1988) 206 Cal.App.3d 632 [VERIFY])
- FRCP 26(g) counsel signature certification is separate from FRCP 33(b)(3) party verification — both layers must be present
- Document all service evidence now: ECF notices, email headers, postmarks

### Recommended Next Steps

- [ ] Serve corrected/amended verification page (outgoing defect)
- [ ] Send meet-and-confer letter demanding cure by [date]
- [ ] Obtain stipulation confirming operative service date / extending deadline
- [ ] Calendar motion-to-compel deadline based on corrected service date
- [ ] Preserve proof-of-service evidence in case file

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the audit memorandum, ask:

1. Does the audit cover all discovery sets at issue — any additional responses to review?
2. Are the defect severity classifications aligned with your litigation strategy?
3. Should I draft a meet-and-confer letter based on the defects identified?
4. Are there any deadline-modifying stipulations or orders I should factor in?

If the user doesn't answer, recommend calendaring the computed deadlines and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Every conclusion tied to a specific exhibit, Bates number, or PDF page
- Verification elements checked against the correct forum-specific standard
- Deadline computation shows all steps explicitly with extensions
- Defect severity correctly classified (fatal vs. technical)
- Signature authority verified for the correct party type
- Service method authorization confirmed
- All parties on master service list accounted for
- CA court days vs. calendar days distinction applied correctly
- No invented case citations
- All forum-specific rules confirmed or flagged `[VERIFY]`

---

## Guidelines

- **No hallucinated citations** — every jurisdiction-specific extension day count must be web-verified against current statutory text or flagged `[VERIFY]`
- **Document every factual assertion** — tie each conclusion to a specific exhibit, Bates number, or PDF page; do not assume what "must have happened"
- **Distinguish defect severity** — fatal (response = nullity) vs. technical (curable); never declare waiver or sanctions automatic without confirming the forum's standard
- **Attorney verification trap** — flag any instance where counsel signed an instrument requiring party execution; the single most frequent fatal defect in practice
- **Do not recommend filing motions or threatening sanctions as a definitive step** — present as options for attorney evaluation
- **Privilege and confidentiality** — minimize quoting substantive discovery content; reference by paragraph/page number; flag HIPAA-protected, PII, or protective-order-designated material
- **International service** — if any party is outside the U.S., flag Hague Service Convention applicability and require separate attorney review
- **Anti-hallucination** — all case citations must be verified or left as explicit placeholders
- **Attorney review required** — supervising attorney must personally verify signatures and the final computed deadline before calendaring, client communications, or court filings
