---
name: depositions-legalquants
title: /depositions
description: Prepare, conduct, and close the loop on a deposition using claims, elements, chronology, exhibits, admissions, impeachment, ethics, and transcript evidence. Use when planning a deposition, preparing a witness, structuring Rule 30(b)(6) topics, or extracting deposition follow-up.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/depositions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Sources
  path: references/sources.md
---

# /depositions

Prepare a deposition as a decision-focused evidence workflow. The lawyer remains responsible for the forum, current law, strategy, witness contact, admissibility, and final use of testimony. This skill may organize supplied material and draft work product; it must not contact a witness, issue a subpoena, file a notice, direct a witness to testify, or make an undisclosed legal or factual assumption.

Read only confirmed `[depositions]` entries in `lqplaybook.md` if present. Never read `lqprofile.md` for work product and never write either file; the scribe owns journey updates. A preference revealed during the run may be proposed as an exact `[depositions]` line, but it affects future work only after the user explicitly confirms it.

## Inputs and authority

Use supplied pleadings, orders, discovery, productions, prior testimony, witness materials, and applicable authority first. Ask only for missing facts that would change the plan: forum and posture, witness type, deposition date or time limit, and the primary objective. Record an `as_of` date and mark unknowns rather than filling them from memory.

Select the governing procedural and evidence rules before planning. Read local rules, scheduling orders, standing orders, protective orders, and any remote-deposition protocol. The federal baseline is Federal Rules of Civil Procedure 26, 30, 32, 34, 37, and 45 and Federal Rules of Evidence 401, 403, 602, 607, 608, 609, 611, 612, 613, 801, 804, 803, and 901 as applicable; see [sources](references/sources.md). State, arbitral, administrative, foreign, and judge-specific practice can change notice, service, fees, place of compliance, leave, duration, breaks, objections, oath, contact, admissibility, and transcript use.

## Tool cascade

Start with host-native document reading and local, open-source extraction. If that is unavailable, ask the user for readable text or exports. A legal-grade comparison, transcript, or e-discovery platform is an optional user-selected rung; disclose what it receives, preserve originals, and keep the same source and provenance contract. Never require a connector, package, network service, hook, or particular model.

## Method

### 1. Define witness posture and decision objective

Create a witness profile covering party or nonparty status, current or former employee status, represented-person and contact restrictions, role, source of knowledge, likely testimony, documents and systems touched, credibility risks, availability, subpoena or notice status, and privilege or confidentiality boundaries.

State one primary objective and no more than three to five secondary objectives. Examples are discovering facts and sources, locking an admission, establishing foundation, preserving testimony, testing credibility, narrowing issues, evaluating exposure, or obtaining the organization’s position. Tie every objective to a claim, defense, element, burden, remedy, or procedural decision.

### 2. Map objectives to proof

For each objective, create a proof row with the proposition, claim or defense element, burden, source IDs and exact locations, witness or exhibit, desired answer, fallback proof, expected objection or privilege issue, and downstream use. Distinguish an admission from a useful fact, a disputed assertion, and a legal conclusion.

Do not draft a generic biography outline. Use the claim and defense chart to identify material facts, disputed issues, missing evidence, and the smallest sequence that can establish or test each proposition.

### 3. Build the chronology and witness map

Use source-backed events with stable IDs, date precision and time zone, actor, source ID, exact page/Bates/line/timestamp, fact status, linked elements, linked witnesses and exhibits, confidence, and follow-up. Keep attorney inference and legal characterization in separate fields. Mark asserted, verified, contradicted, undisputed, unknown, and privileged material explicitly.

For each event, decide whether to ask open questions first, then controlled foundation questions, then the proposition or admission. Record what the witness could know personally, what is organizational knowledge, and what requires another witness or record.

### 4. Prepare exhibit, admission, and impeachment plans

Give each exhibit one stable matter-wide ID and preserve its source ID, Bates or version, native filename, hash where available, author, custodian, production status, authenticity and foundation path, linked element, planned question sequence, expected admission, impeachment use, privilege/PII status, and designation status. Keep documents needed to prove the case distinct from documents reserved for impeachment. Preserve context and completeness; an “impeachment” label does not itself resolve production or admissibility.

For admissions, use one proposition per sequence. Establish role, personal or organizational knowledge, opportunity to observe, document or event foundation, and the answer. Record obtained, denied, qualified, cannot recall, privileged, or follow-up status with the transcript page and line. Do not describe testimony as automatically binding; later use depends on Rule 32, evidence law, posture, and jurisdiction.

For impeachment, record the current testimony, prior statement, exact source locations, contradiction versus omission versus clarification, predicate questions, opportunity to explain, extrinsic-proof plan, materiality, expected objection, and context pages or lines. Use Federal Evidence Rules 607, 608, 609, 611, 612, 613, and 801(d)(1)(A) only as a federal baseline and flag local differences.

### 5. Draft the question outline

Use the smallest useful sequence: orientation and role, knowledge boundaries, chronology, issue-specific foundations, exhibits, admissions, credibility or impeachment, damages or remedy, and open-source/follow-up questions. Each row should contain `topic`, `purpose`, `source_premise`, `question`, `expected_answer`, `follow_up`, `exhibit_id`, and `stop_condition`.

Write questions in advance but do not turn the outline into a script. Avoid cumulative loops, compound propositions, argument, and questions whose only purpose is to display a document. Reserve time for high-value objectives, unforeseen testimony, and clean closing questions.

### 6. Apply witness-preparation ethics

Preparation may explain the oath and process, require truthful testimony, explain that a truthful “I do not recall” is acceptable, review documents and chronology, explore the witness’s own recollection, discuss likely topics and cross-examination, and improve listening, clarity, and demeanor. Use [ABA Formal Opinion 508](references/sources.md) and the adopted jurisdictional ethics rules.

Never coach a witness to give false testimony, create a scripted story, conceal or evade, disobey an order, miss testimony, or use a false lack-of-memory answer. Do not use suggestive speaking objections, gestures, winks, private chat, text messages, or other covert signals. Agree breaks and communications in advance and follow the court’s order; do not use a break to change a pending answer without authority. If false testimony is discovered, escalate to the responsible lawyer for the jurisdiction’s remedial-candor analysis. Store preparation topics, reviewed sources, unresolved discrepancies, and completion status, not a model answer script.

### 7. Handle Rule 30 and Rule 30(b)(6) controls

For an ordinary deposition, check notice, subpoena, leave, recording method, location or remote authority, time and numerical limits, exhibits, interpreter or oath needs, and protective-order issues under the current Rules 30 and 45 baselines and local law. For a nonparty subpoena, confirm the issuing court; any required notice and copy before service of a document command; valid service; attendance fee and mileage tender; place-of-compliance limits; and the compliance-court, quash, enforcement, or transfer path. Under Rule 30(c)(2), objections ordinarily remain concise, nonargumentative, and nonsuggestive, examination proceeds, and an instruction not to answer is limited to privilege, a court-ordered limitation, or relief under Rule 30(d)(3). Log objections, privilege instructions, unresolved disputes, and any waiver-sensitive defect.

For Rule 30(b)(6), create a topic-to-designee matrix. Confirm reasonable particularity, the good-faith meet-and-confer, each designee, organizational role, custodians and systems searched, documents reviewed, information known or reasonably available, gaps, supplementation, and compel or protective-order risk. Prepare the organization’s position rather than only the individual’s memory. Never state that a designee’s answer has universal binding effect; circuit and state authority controls.

### 8. Run an in-session checkpoint when a live transcript is available

If counsel is authorized to receive a real-time or rough transcript and the governing order, stipulation, reporter terms, confidentiality controls, and technology permit its use, use a substantial break such as lunch for a bounded checkpoint. Mark every page as real-time, rough, uncertified, and potentially incomplete; preserve the reporter's identifiers and do not cite it as the certified record.

Create a short hit list for the remaining examination: uncovered high-priority objectives, qualified or equivocal admissions that need clarification, foundation gaps, contradictions requiring fair context, newly identified witnesses or sources, exhibits not yet used, questions promised for follow-up, and time remaining. Link every item to the objective-to-proof map and the exact rough page or timestamp. Revise the outline only where the checkpoint reveals a concrete gap; do not use a break to coach a pending answer, communicate covertly with the witness, or turn an unverified transcript artifact into a factual conclusion.

### 9. Close the loop after testimony

Obtain the certified transcript, recording, exhibits, and errata or review status where applicable. Normalize page/line and exhibit crosswalks. Start with a concise takeaway sheet stating what changed, the strongest admission or useful testimony, the strongest answer for the other side, material proof gaps, credibility or foundation issues, and the next decisions. Then extract admissions, denials, qualifications, contradictions, new custodians or sources, privilege issues, sanctions or meet-and-confer issues, and follow-up discovery.

For a federal deposition, check whether the deponent or a party requested Rule 30(e) review before the deposition was completed under Rule 30(e)(1). If properly requested, track the 30-day period after notice that the transcript or recording is available, the deponent's signed statement listing each change in form or substance and the reason for it under Rule 30(e)(1)(A)–(B), and the officer's attachment of the changes under Rules 30(e)(2) and 30(f)(1). Preserve the original answer alongside every proposed change. Flag whether and how a substantive change may be used, challenged, or affect reopening, costs, impeachment, or summary judgment because circuit, state, local, and case-specific authority varies; do not treat an errata sheet as automatically accepted, rejected, or harmless.

Update the chronology, claim/defense chart, issue/evidence matrix, witness and exhibit trackers, and deadline tracker. Record each material change, its source and exact location, owner, due date, and downstream use. A deposition plan is complete only when its post-transcript actions are reconciled into the matter record.

## Deliverables

Produce a concise human-readable brief and, where practical, structured rows using the [deposition plan template](templates/deposition-plan.md). Include:

- Witness posture and authority/currentness note.
- Objective-to-proof map and time budget.
- Source-backed chronology and issue map.
- Question outline with exhibit sequence and stop conditions.
- Exhibit, admission, and impeachment matrices.
- Objection, privilege, break, remote-technology, and confidentiality plan.
- Real-time or rough-transcript checkpoint and remaining-examination hit list when available and authorized.
- Rule 30(b)(6) topic/designee and knowledge-search matrix when applicable.
- Ethical preparation log without scripted answers.
- Post-deposition takeaway, errata, extraction, and action report using the [transcript extract template](templates/transcript-extract.md).

Begin with `Known`, `Unverified or disputed`, `Missing`, and `Decision points`. Cite supplied sources with stable IDs and exact locations. Do not invent testimony, facts, legal holdings, or transcript citations.

## Quality gate

Before delivery, verify that:

- The forum, posture, current rules, local orders, and as-of date are explicit.
- Every objective maps to an element or decision, question sequence, source, and fallback.
- Every factual premise has a source ID and exact location, with inference separated.
- Every exhibit has one stable ID, foundation path, status, and issue link.
- Admissions and impeachment preserve context and transcript locations.
- Rule 30(b)(6) topics, conference, designees, organizational knowledge, and gaps are tracked.
- Objections and instructions not to answer comply with the applicable rule baseline and local order.
- Ethics and confidentiality controls prohibit false testimony, coaching, covert communication, and improper contact.
- Time, real-time transcript status, hit-list follow-through, certified transcript, Rule 30(e) request and deadline, original and changed answers, reasons, follow-up, and issue-matrix updates are complete or visibly pending.
- A lawyer reviews final strategy, characterization, admissibility, and intended use.

## Limits

This skill organizes litigation work; it is not a substitute for the governing rules, local practice, a court order, a licensed transcript service, or professional judgment. It must not autonomously contact witnesses, issue process, make a privilege ruling, waive an objection, file anything, release a hold, or delete matter material.
