# Demand Letter — Template

A single skeleton with three inline branch variants. Pick one branch at Step 1 (see `../SKILL.md`), keep its blocks, delete the other branch markers and their contents, then fill placeholders. Every `{{PLACEHOLDER}}` must be resolved or explicitly marked `[UNVERIFIED — client-provided]` / `[VERIFY]` before the draft leaves the skill.

**Branches**

- `<!-- BRANCH: statutory-notice -->` — Ch. 93A, DTPA, CLRA, FDCPA, FL med-mal, construction defect, any letter whose legal function is satisfying a statutory pre-suit prerequisite.
- `<!-- BRANCH: policy-limits -->` — Demand directed at an insurer/adjuster invoking bad-faith / Stowers / Holt framework; typically PI.
- `<!-- BRANCH: commercial -->` — Breach + cure, C&D (trademark / patent / trade-secret / non-compete), general demand for payment under a contract.

Placeholders in `{{DOUBLE_BRACES}}` are required. Placeholders in `[SINGLE_BRACKETS]` are conditional — keep only if the condition applies.

---

## Header block

```
{{DATE — full month, day, year}}

{{SERVICE METHOD}}
    Options (pick one or stack): "Via Certified Mail, Return Receipt Requested"
                                 "Via FedEx (Tracking No. {{TRACKING}})"
                                 "Via Hand Delivery"
                                 "Via Email to {{EMAIL}}"
                                 "Via Facsimile to {{FAX}}"

    Rule: if the governing contract specifies a notice method, use that method
    AND state that you used it. Never substitute a weaker method.

{{RECIPIENT NAME}}
{{RECIPIENT TITLE}}
{{RECIPIENT ENTITY — corporate name as filed with Secretary of State}}
{{CONTRACTUAL NOTICE ADDRESS OR REGISTERED-AGENT ADDRESS}}

[c/o {{REGISTERED AGENT}}]   ← add if service on the agent is required by statute or contract
```

## Re: line

```
Re:  {{SHORT SUBJECT — e.g., "Demand Under Mass. Gen. Laws ch. 93A, § 9"
                          or  "Time-Limited Policy-Limits Settlement Demand — Allen v. Burton"
                          or  "Notice of Breach and Demand for Cure — Master Services Agreement dated {{DATE}}"}}
     Claimant: {{CLIENT FULL LEGAL NAME}}
     Date of Incident / Breach: {{DATE}}
     [Policy No.: {{POLICY}}]     ← policy-limits only
     [Claim No.: {{CLAIM}}]       ← policy-limits only
     [Contract: {{CONTRACT TITLE, DATE}}]   ← commercial only
```

## Optional FRE 408 / state-equivalent header

```
SETTLEMENT COMMUNICATION — SUBJECT TO FRE 408
AND {{STATE}} RULE OF EVIDENCE {{NUMBER}}
```

**Keep when:** letter explicitly invites settlement, includes a term sheet, or offers a compromise number.
**Omit when:** letter is a pure statutory-prerequisite notice (Ch. 93A, DTPA, CLRA, FDCPA § 1692g), a pure cease-and-desist without a monetary ask, or a policy-limits demand that you want fully admissible as a Stowers/Holt exhibit (jurisdiction-specific — see `JURISDICTION-PRESUIT.md` and `ETHICS-AND-PRIVILEGE.md`).
**Warning:** the label is a signal, not a shield. Factual admissions inside the letter can still be used for purposes other than proving liability in some jurisdictions. Draft as if admissible.

## Salutation

```
Dear {{SALUTATION}}:
```

**Decision rule:**
- If recipient is known to be represented → address counsel (`Dear Counsel:` or `Dear Ms./Mr. {{LAST}}:`). Model Rule 4.2; see `ETHICS-AND-PRIVILEGE.md`.
- Corporate recipient, no known counsel → address by title (`Dear General Counsel:`, `Dear Risk Manager:`, `Dear Claims Adjuster:`).
- Individual recipient → `Dear Mr./Ms./Mx. {{LAST}}:` — do not use first names.

---

## §1 — Opening: Representation and Purpose

<!-- BRANCH: statutory-notice -->
```
This firm represents {{CLIENT}} in connection with {{CLAIM SUBJECT}}. This letter
serves as {{CLIENT}}'s written demand under {{STATUTE CITATION}} and satisfies
the pre-suit notice requirement of that statute. It identifies the unfair,
deceptive, or otherwise actionable conduct, the injury sustained, and the
relief demanded.
```
<!-- /BRANCH -->

<!-- BRANCH: policy-limits -->
```
This firm represents {{CLIENT}} for injuries sustained in the {{INCIDENT TYPE}}
on {{DATE}}. We write to offer {{INSURER}} a time-limited opportunity to settle
all claims arising from this incident for the available policy limits of
{{POLICY NO.}}. This offer is made in good faith, with the expectation that
{{INSURER}} will evaluate the claim in accordance with its fiduciary obligation
to its insured {{INSURED NAME}}.
```
<!-- /BRANCH -->

<!-- BRANCH: commercial -->
```
This firm represents {{CLIENT}} in connection with {{COUNTERPARTY}}'s
{{BREACH TYPE — e.g., "failure to perform under Section X of the"}} {{CONTRACT
TITLE}} dated {{CONTRACT DATE}} (the "Agreement"). This letter constitutes
formal notice of breach under {{NOTICE CLAUSE SECTION}} of the Agreement and a
demand for {{CURE | PAYMENT | CESSATION}}.
```
<!-- /BRANCH -->

**Rule for all branches:** no legal theories yet, no damages numbers yet. Section 1 establishes who, why, and the letter's formal function. Keep to 2–4 sentences.

---

## §2 — Factual Background

**Length guidance by branch:**
- Statutory-notice: 250–600 words. Must be specific enough to satisfy the statute's "identifying the unfair or deceptive act" requirement (MA 93A) or equivalent.
- Policy-limits: 400–1500 words. Liability + full injury/treatment narrative; this is your Stowers/Holt exhibit if the insurer refuses.
- Commercial: 300–800 words. Focus on contract terms + counterparty's conduct; fewer emotions, more dates and documents.

**Content rules (all branches):**
1. Chronological. Start at formation / incident, end at the moment of this letter.
2. Every fact must be source-cited inline: `(Exhibit A, p. 3)`, `(Email from {{SENDER}} to {{RECIPIENT}}, {{DATE}}, attached as Exhibit B)`, `(Medical Record, {{PROVIDER}}, {{DATE}})`. If a fact has no source, either get one, cut it, or label `[UNVERIFIED — client-provided]`.
3. Quote contract terms and adverse-party statements verbatim. Never paraphrase a clause you intend to rely on.
4. No conclusory labels ("fraudulent," "willful," "bad-faith," "criminal") without facts that supply each element of that label.
5. Adversarial awareness: every sentence is a future exhibit. If a sentence could be used against your client's position, rewrite or cut.
6. One source-cited fact per claim element, minimum. If you cannot supply a fact for every element, do not plead that cause of action in §3.

```
On {{DATE}}, {{SPECIFIC EVENT}}. (Exhibit {{X}})

On {{DATE}}, {{SPECIFIC EVENT}}. (Exhibit {{X}})

...

As of the date of this letter, {{CURRENT STATUS}}.
```

---

## §3 — Legal Basis

<!-- BRANCH: statutory-notice -->
```
The conduct described above violates {{STATUTE SHORT NAME}}, {{FULL CITATION}}.
Specifically:

(a) {{ELEMENT 1}} — {{TIE TO §2 FACTS}}. {{CITATION [VERIFY]}}
(b) {{ELEMENT 2}} — {{TIE TO §2 FACTS}}. {{CITATION [VERIFY]}}
(c) {{ELEMENT 3}} — {{TIE TO §2 FACTS}}. {{CITATION [VERIFY]}}

{{STATUTE}} provides for {{REMEDIES — actual damages, multipliers, fees, etc.}}.
See {{CITATION [VERIFY]}}.
```
<!-- /BRANCH -->

<!-- BRANCH: policy-limits -->
```
Liability is clear. {{ONE-SENTENCE LIABILITY STATEMENT TIED TO §2 FACTS}}.
See {{CONTROLLING CASE [VERIFY]}}; {{STATUTE IF ANY [VERIFY]}}.

{{INSURED}} owed {{CLIENT}} a duty of {{CARE STANDARD}}, breached that duty
by {{CONDUCT}}, and proximately caused {{HARM}}.

{{INSURER}} owes {{INSURED}} a fiduciary duty to settle within policy limits
when liability is clear and damages exceed limits. See {{LEADING BAD-FAITH OR
STOWERS/HOLT CASE [VERIFY]}}. Refusal of this demand, if liability is later
established and a verdict exceeds limits, exposes {{INSURER}} to extracontractual
damages.
```
<!-- /BRANCH -->

<!-- BRANCH: commercial -->
```
{{COUNTERPARTY}}'s conduct constitutes a material breach of {{SECTION}} of the
Agreement, which provides:

    "{{VERBATIM CONTRACT LANGUAGE}}"

{{BRIEF APPLICATION — how the facts in §2 breach this clause}}.

[Additionally, the conduct violates {{STATUTORY OR COMMON-LAW THEORY}}. See
{{CITATION [VERIFY]}}.]   ← include only if it independently unlocks a remedy
                            (fees, punitives, treble damages) OR survives a
                            foreseeable defense to the breach claim.
```
<!-- /BRANCH -->

**Primary-vs-secondary rule (all branches):** State the primary claim (the one with the best-supported elements AND whose remedy matches the client's objective). Add secondary claims only if they independently unlock a remedy the primary does not, OR if they survive a foreseeable defense to the primary. Otherwise omit — over-pleading weakens the letter's credibility as a future exhibit.

**Citation verification:** every statutory cite → `legal-research`; every case cite → `citation-bluebook` for format and good-law status. Unverified → `[VERIFY]` inline.

---

## §4 — Damages and Relief

Use the rules in `DAMAGES-METHODOLOGY.md`. Format choice:

- **Inline narrative** for letters with 1–3 damage categories (typical statutory-notice, simple commercial).
- **Table** for letters with 4+ categories or multiple line items per category (typical policy-limits, complex commercial).
- **Appendix** for letters with extensive billing records or expert reports supporting the numbers.

```
{{CLIENT}} has suffered the following damages as a direct and proximate result
of the conduct described above:

| Category                         | Amount        | Support                       |
|----------------------------------|---------------|-------------------------------|
| Direct / expectation             | $ {{AMOUNT}}  | {{EXHIBIT/RECORD}}            |
| Consequential                    | $ {{AMOUNT}}  | {{EXHIBIT/RECORD}}            |
| [Statutory multiplier ({{BASIS}})] | $ {{AMOUNT}}  | {{STATUTE CITATION [VERIFY]}} |
| [Prejudgment interest ({{RATE}})] | $ {{AMOUNT}}  | {{STATUTE/CONTRACT [VERIFY]}} |
| [Attorney's fees and costs]      | $ {{AMOUNT}}  | {{CONTRACT/STATUTE [VERIFY]}} |
|                                  |               |                               |
| **Total demand**                 | **$ {{TOTAL}}** |                             |

{{MITIGATION DISCLOSURE — if facts suggest a mitigation defense, address
affirmatively: what {{CLIENT}} did to mitigate, why further mitigation was not
feasible}}.

{{OFFSETS AND CREDITS — any payments already received, insurance offsets, or
collateral-source amounts accounted for}}.
```

**Rules:** apply the "Cross-cutting rules" in `DAMAGES-METHODOLOGY.md` — no client totals as computed, every line needs a source, no fees without a verified basis, no walkaway number.

---

## §5 — Evidence Preservation

```
Litigation is now reasonably anticipated. {{COUNTERPARTY OR INSURER}} is hereby
on notice of its duty to preserve all documents and electronically stored
information ("ESI") that may be relevant to the claims described above,
including but not limited to:

 - emails, text messages, instant messages, and other electronic communications
 - calendar entries, call logs, and voicemail
 - internal reports, memoranda, and notes
 - database records and metadata
 - backup media, cloud storage, and archival systems
 - [{{INCIDENT-SPECIFIC ITEMS — e.g., surveillance footage from {{LOCATION}},
    EDR/black-box data from vehicle VIN {{VIN}}, product exemplars}}]

Routine destruction and retention policies must be suspended immediately as to
these materials. Failure to preserve may result in spoliation sanctions,
adverse-inference instructions, and independent tort liability where recognized.
```

**Scope rule:** the paragraph above is a trigger + catch-all. If the matter involves specific high-risk evidence (surveillance video with short retention, vehicle EDR, medical devices, ESI on custodian-controlled systems), do not rely on this paragraph alone — invoke the `spoliation-letter` skill to produce a dedicated preservation demand with full itemization and a confirmation deadline.

---

## §6 — Demand and Proposed Resolution

<!-- BRANCH: statutory-notice -->
```
Pursuant to {{STATUTE}}, {{CLIENT}} demands:

 1. {{MONETARY RELIEF}} — $ {{AMOUNT}}, payable to {{PAYEE}} by {{METHOD — wire,
    check, ACH}} at {{ADDRESS/ACCOUNT}};
 2. {{NON-MONETARY RELIEF — e.g., cessation, correction, retraction, recall}};
 3. [{{STATUTORY-SPECIFIC RELIEF — injunctive relief, rescission, restitution}}].

A written response meeting the requirements of {{STATUTE §}} must be delivered
to this office no later than {{CALENDAR DATE — computed from statutory period}}.
```
<!-- /BRANCH -->

<!-- BRANCH: policy-limits -->
```
{{CLIENT}} offers to settle all claims against {{INSURED}} arising from the
incident of {{DATE}}, including any and all bodily-injury, property-damage,
consequential, and loss-of-consortium claims, in exchange for payment of the
available {{POLICY NO.}} limits of $ {{LIMITS}}.

This offer is open until {{CALENDAR DATE AND TIME, TIMEZONE}}. Payment must be
delivered to this office by {{METHOD}}, accompanied by a limited release in
substantially the form {{ATTACHED | TO BE PROVIDED}}.

Any counteroffer, conditional acceptance, or request to modify the terms above
will be treated as a rejection.
```
<!-- /BRANCH -->

<!-- BRANCH: commercial -->
```
{{CLIENT}} demands:

 1. {{PRIMARY RELIEF — cure, payment, cessation, return of property,
    corrective action}}, on or before {{CALENDAR DATE}};
 2. {{ANCILLARY RELIEF — written confirmation, accounting, destruction
    certificate, etc.}};
 3. Reimbursement of {{CLIENT}}'s damages as set forth in §4.

[If settlement is offered: the following release framework would be acceptable:
 - Release scope: {{MUTUAL | UNILATERAL | CARVE-OUTS}};
 - Confidentiality: {{STANDARD | REQUIRED WITH CARVE-OUTS FOR COUNSEL AND
   REGULATORS}};
 - Non-disparagement: {{MUTUAL | ONE-WAY}};
 - No admission of liability.]
```
<!-- /BRANCH -->

**Term-sheet inclusion rule:** include release / confidentiality / non-disparagement language only when the letter explicitly invites settlement. Omit from pure statutory-notice (93A, DTPA, CLRA, FDCPA § 1692g) — those terms belong in the response-negotiation phase.

---

## §7 — Consequences of Non-Compliance

```
Failure to satisfy the demand above by {{CALENDAR DATE}} will result in
{{CLIENT}} pursuing all available remedies, including:

 - Filing suit in {{FORUM — e.g., "the United States District Court for the
   {{DISTRICT}}"  |  "the {{COUNTY}} District Court of {{STATE}}"}},
   seeking {{LIST OF REMEDIES — compensatory damages, statutory multipliers,
   injunctive relief, fees and costs}};
 - [{{STATUTORY ESCALATION — e.g., "treble damages and attorney's fees under
   {{STATUTE}}"}}];
 - [{{REGULATORY REFERRAL WHERE APPROPRIATE — e.g., "notification to
   {{AGENCY}}"}}]    ← see "Forbidden phrasings" in ETHICS-AND-PRIVILEGE.md;
                        regulatory referral is permissible as information, not
                        as criminal-threat leverage.

This letter is not a threat of criminal prosecution and nothing herein should
be construed as one.
```

**Deadline rule:** default 30 calendar days. Override to the statutory period where applicable (MA 93A: 30; TX DTPA: 60; CLRA: 30; FDCPA § 1692g: 30). Sub-14-day only for imminent-harm scenarios (ongoing infringement, spoliation risk, foreclosure sale date) — justify the shorter deadline in the letter text.

**Forum rule:** contract forum-selection clause controls. Absent a clause, default to a forum with (a) personal jurisdiction over the recipient and (b) venue under 28 U.S.C. § 1391 or the state equivalent. When multiple valid forums exist, choose per client preference from intake. If the client has not decided, flag and ask — do not name a forum you have not confirmed.

---

## §8 — Closing and Signature

```
This letter is written with full awareness that it may be received by counsel
for {{COUNTERPARTY}}. {{CLIENT}} remains prepared to discuss resolution on the
terms above. Communications regarding this matter should be directed to the
undersigned.

[Settlement Communication — Subject to FRE 408 / State Equivalent]   ← if kept

Sincerely,


{{ATTORNEY NAME}}
{{BAR NUMBER, STATE}}
{{FIRM}}
{{ADDRESS}}
{{PHONE}}  |  {{EMAIL}}

Enclosures: {{EXHIBIT LIST}}
cc: {{CLIENT NAME}}
    [{{CO-COUNSEL}}]
    [{{OPPOSING COUNSEL IF KNOWN}}]
```

---

## Before delivering — branch-consistency checklist

- [ ] Exactly one branch kept; no `<!-- BRANCH: ... -->` markers or alternate-branch text remain in the draft.
- [ ] Every `{{PLACEHOLDER}}` resolved or marked `[VERIFY]` / `[UNVERIFIED — client-provided]`.
- [ ] Every legal citation verified via `legal-research` / `citation-bluebook` or marked `[VERIFY]`.
- [ ] Deadline is a specific calendar date.
- [ ] Recipient entity name matches Secretary of State record; notice address matches contract or agent-on-file.
- [ ] FRE 408 header kept or omitted per the rule in §8; choice is defensible.
- [ ] No conclusory labels ("fraudulent," "criminal," "willful") unsupported by §2 facts.
- [ ] No criminal-threat leverage; no defamatory statements.
- [ ] §5 preservation paragraph included; dedicated `spoliation-letter` invoked when high-risk evidence is in play.
- [ ] §6 term-sheet language included only where the letter invites settlement.
- [ ] Signature block includes bar number.
- [ ] Attorney review required before sending — flagged to user.
