---
name: correspondence-legalquants
title: Litigation Correspondence
description: Triage inbound and draft source-grounded U.S. litigation correspondence, including discovery meet-and-confer letters, settlement demands and counteroffers, and substantive pre-suit or case communications. Use when a lawyer needs a precise, review-ready draft with authority, fact provenance, deadlines, negotiation-status cautions, and a no-send gate.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/correspondence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Authority And Provenance
  path: references/authority-and-provenance.md
- title: Real Exemplars
  path: references/real-exemplars.md
- title: Synthetic Patterns
  path: references/synthetic-patterns.md
---

# Litigation Correspondence

## Outcome and boundaries

Produce a review-ready correspondence package: an inbound triage note or an outbound draft, a fact and source ledger, an internal reviewer note, and an explicit no-send status. The package is a drafting aid, not legal advice, and the lawyer remains responsible for jurisdiction, facts, authority, strategy, privilege, client instructions, and sending, serving, or filing.

Do not send, serve, file, accept, reject, or bind a client. Do not silently convert an email into a settlement offer, a discovery letter into a motion, or a demand for preservation into a litigation threat. When the user asks for an external action, prepare the artifact and state the exact human approval and operational step still required.

Keep matter information within the supplied evidence universe and the host's approved local tools. Never invent a request number, procedural deadline, contract term, damages figure, authority, fact, representation status, settlement authority, or attachment. If a material item is missing, use a bracketed placeholder and put it in the no-send list.

Use the real public records in [real-exemplars.md](references/real-exemplars.md) as linked teaching exemplars only. Do not reproduce a filed document wholesale, imitate a named lawyer, or treat a party's advocacy or a court's procedural ruling as universally correct. Use [synthetic-patterns.md](references/synthetic-patterns.md) for anonymized drafting patterns.

Read only confirmed `[correspondence]` entries in `lqplaybook.md` if present. Never read `lqprofile.md` for work product and never write either file; the scribe owns journey updates. A preference revealed during the run may be proposed as an exact `[correspondence]` line, but it affects future work only after the user explicitly confirms it.

## Route the communication before writing

Select one primary route and state it at the top of the reviewer note. If a communication has mixed purposes, split the draft into separate artifacts or ask the lawyer to choose; do not assume that a settlement label protects factual or discovery content.

| Route | Primary job | Required first checks |
| --- | --- | --- |
| Inbound triage | Preserve, classify, flag for docketing or calendaring review, and recommend a response path | Sender, representation, receipt time, attachments, deadlines, settlement status, and requested action |
| Discovery meet-and-confer | Narrow a defined discovery dispute and document good-faith efforts | Exact request and response, governing order and local rule, proportionality, privilege, conferral method, and motion deadline |
| Settlement demand or response | Make or evaluate a conditional economic and non-economic resolution proposal | Client authority, disputed claim, offer mechanics, scope of release, approval conditions, and Rule 408 purpose |
| Substantive pre-suit or case correspondence | Give notice, state a position, request action, preserve evidence, or advance a procedural step | Addressee and counsel status, factual support, legal basis, preservation, lawful consequences, and response deadline |

Use `document-discovery` for the underlying request, response, objection, subpoena, privilege, and proportionality analysis; this skill translates the resulting position into a letter or email and packages it for review. Use `writing` for a court or regulator filing or a full legal-analysis memorandum, and `client-update` for status reporting to the client.

This is a general day-to-day litigation-correspondence workflow, not a demand-letter workflow with incidental extras. Discovery disputes and substantive case communications will often be the ordinary routes; demands, responses, and counteroffers remain available when the matter actually calls for them.

The route is not determined by a subject line. “Without prejudice,” “confidential,” “for settlement purposes,” or “FRE 408” is a useful routing signal but does not create privilege, confidentiality, inadmissibility, or a binding/nonbinding status by itself.

## Minimal intake

Ask no more than three focused questions when the request omits material information: (1) What is the source communication or matter material, and what result is wanted? (2) Who is the audience, what is the current posture, and is the output inbound triage, a draft, or both? (3) What jurisdiction, court or contract governs, what deadline or as-of date matters, and what client authority has been confirmed? If the supplied material answers a question, do not ask it again.

For an inbound item, preserve the original message and attachments when available, record the received date and time zone, identify the sender and all copied recipients, and flag whether the sender is represented. Do not infer receipt, service, waiver, or acceptance from a forwarded excerpt or filename.

For an outbound item, obtain the exact request, pleading, order, prior correspondence, agreement, or factual record that the draft will cite. If the user supplies only a summary, distinguish the summary from the underlying record and limit the draft accordingly.

## Evidence and fact ledger

Build a compact ledger before drafting. A source link is navigation, not proof; a fact is ready for unqualified use only when the supplied source supports it and its scope is clear.

| Field | Use |
| --- | --- |
| `fact_id` | Stable identifier for each material proposition |
| `proposition` | The fact, procedural event, request, term, or legal position in plain language |
| `status` | `verified_record`, `client_report`, `party_allegation`, `inference`, `estimate`, `unknown`, or `disputed` |
| `source_id` | Supplied file, message, docket item, agreement, public authority, or interview note |
| `locator` | Page, paragraph, message timestamp, request number, docket document, or other stable location |
| `scope` | What the source establishes and what it does not establish |
| `use` | `safe_to_state`, `state_as_position`, `needs_qualification`, or `do_not_use` |

Use calibrated language: “the complaint alleges,” “our client reports,” “the production shows,” “we contend,” “as presently understood,” or “we have not independently verified.” Do not turn a party allegation into an established fact, a damages estimate into a demand basis without labeling it, or an inference into a statement of intent.

Keep a separate authority ledger with the rule or order, jurisdiction, effective/as-of date, direct source, proposition supported, and any local variation. Identify whether a public source is official, a court or government archive, or a mirror. Do not cite a search-result snippet or a teaching exemplar as governing authority.

For a multi-document run, use one temporary, matter-scoped JSON dataset for extracted facts, source IDs, and drafts. Delete it on completion and do not place client-confidential material in a skill reference, eval fixture, public URL, or durable log.

## Professional and evidentiary guardrails

The [ABA Model Rules](references/authority-and-provenance.md) are a cross-jurisdictional professional reference, not automatically the law of every forum. Check the jurisdiction's adopted rules, court orders, standing orders, professional-conduct opinions, and applicable state evidence law.

### Truth, discovery, and third-party rights

Rule 3.4 requires fairness to the opposing party and counsel, including a reasonably diligent effort to comply with legally proper discovery and no frivolous discovery request or obstructive tactic. A meet-and-confer should narrow and solve a defined problem, not manufacture a record through boilerplate or personal attacks.

Rule 4.1 prohibits knowingly false statements of material fact or law and treats a partially true but misleading statement or material omission as potentially equivalent to an affirmative misstatement. Negotiation conventions may make estimates of price or value, and stated settlement intentions, non-material in context; they do not license false facts, fabricated evidence, or false authority.

Rule 4.4 prohibits means with no substantial purpose other than embarrassment, delay, or burden and methods of obtaining evidence that violate a person's legal rights. If counsel receives material that counsel knows or reasonably should know was inadvertently sent, promptly notify the sender and pause use while checking the governing law or order. Screen communications with represented persons under Rule 4.2 and correct misunderstandings when dealing with an unrepresented person under Rule 4.3.

Federal Rule of Civil Procedure 26(b)(1) limits discovery to relevant, nonprivileged, proportional material, and Rule 26(g) certifies reasonable inquiry, proper purpose, and non-burdensome requests, responses, and objections. Federal Rule 37(a)(1) requires a good-faith conferral certification for a motion to compel; local rules may require a live conference, a specific letter format, or a separate certification. Confirm the forum before relying on email alone.

### Settlement communications

Federal Rule of Evidence 408 generally limits use of compromise offers, acceptances, and conduct or statements during compromise negotiations to prove or disprove the validity or amount of a disputed claim or to impeach by contradiction or prior inconsistent statement. The claim must actually be disputed as to validity or amount; a label cannot create a dispute. Rule 408 has other-purpose exceptions, and its treatment of civil government-enforcement negotiations in a later criminal case is specialized.

Rule 408 is an evidentiary rule, not a general privilege, confidentiality agreement, or deletion instruction. Documents and facts that are otherwise discoverable do not become immune merely because they were exchanged in negotiations. A settlement communication may also matter for notice, bad faith, fraud, jurisdiction, or contract formation, depending on the purpose and governing law. Keep factual and merits support separate from concessions where practical, and consult the forum's rule and case law.

Before drafting a demand, response, or counteroffer, confirm who has authority to make it, whether it is intended to be binding, what counts as acceptance, when it expires, and which terms remain subject to a signed writing or third-party approval. State the mechanics precisely; do not imply acceptance by silence, continued negotiations, or an unapproved “final” position.

### Rule 11 and court-facing material

Federal Rule of Civil Procedure 11 applies to a signed pleading, motion, or other paper presented to a court and requires reasonable inquiry, a proper purpose, warranted legal contentions, and factual support or a stated basis for likely support. Ordinary private correspondence is not itself a Rule 11 filing, but a filed letter, exhibit, or later court submission can make its assertions part of a court-facing record. Rule 11(d) excludes discovery requests, responses, objections, and motions under Rules 26–37; discovery certifications and sanctions are instead governed principally by Rules 26(g) and 37.

Do not use “Rule 11” as negotiation bluster. A Rule 11 motion has a specific safe-harbor procedure: serve the separate motion and allow 21 days to withdraw or correct before filing, subject to the forum's rules and exceptions. The advisory committee cautions against using Rule 11 motions to intimidate, test legal sufficiency, or obtain an unjust settlement. A correspondence draft may identify a contemplated procedural step, but only if the record, rule, client authority, and timing support it.

## Workflow

### 1. Inventory posture and purpose

Create a one-line matter card containing court or forum, case number or pre-suit status, parties, current phase, governing law, next known deadline, sender, audience, representation status, and client objective. Mark every item as `confirmed`, `reported`, `disputed`, or `unknown`.

Record the communication status separately: `ordinary_substantive`, `discovery_confer`, `settlement_likely`, `settlement_only_if_disputed`, `mixed`, or `unknown`. If mixed, recommend separate substantive and settlement documents and explain why.

### 2. Prepare the internal reviewer note

The reviewer note should state the recommended route, intended result, factual and authority gaps, client-authority status, deadlines, privilege or confidentiality concerns, likely escalation, and the exact questions a lawyer must answer before release. It may recommend a call or conference, but it must not represent that one occurred.

For inbound triage, extract each ask and proposed consequence, separate assertions from evidence, identify any embedded offer or deadline, note preservation or spoliation language, and flag the earliest plausible response or motion date for docketing review. Preserve the original and attachments; do not edit the evidentiary copy or create a calendar entry.

### 3. Draft with a predictable architecture

Use this order unless the forum or user requests another form: addressee and representation/case identifiers; purpose and status; concise factual record with qualifiers; legal or contractual basis; precise requested action; deadline and time zone; response channel; reservations that preserve rather than obscure the request; attachments and source note; signatory and approval status.

Every material ask should answer what must happen, by whom, by when, in what form, and what will happen next if it does not. A deadline must identify its basis or say that it is proposed. Do not manufacture a “cure period,” service date, discovery cutoff, or response deadline.

Keep sentences short enough to audit against the ledger. Replace adjectives (“bad faith,” “egregious,” “obviously”) with the event, source, consequence, and requested cure. A firm tone can be direct without accusing a person of misconduct that the record does not establish.

### 4. Discovery meet-and-confer handoff

Check the governing scheduling order and local rule before choosing a letter, email, phone call, video conference, or letter motion. The draft should memorialize the actual conference, not claim “good faith” as a conclusion. If the conference has not happened, label the document a proposed agenda or deficiency letter and identify the proposed dates.

Use one row per disputed item: exact request and served date; response or objection and date; specific deficiency; relevance/proportionality or privilege basis; known burden and collection steps; requested narrowing or cure; custodians, fields, search terms, date range, production format, or log detail; proposed deadline; and result of conferral. Quote only what is necessary and link to the exact source.

Seek a concrete cure before court relief: supplement, confirm a reasonable search, identify custodians, produce a log, provide a sample, agree to a protective order, or explain why the request cannot be answered. Preserve an agreed item, a narrowed item, and a true impasse as separate statuses.

Before a motion handoff, verify the Rule 37 certification, local page or letter limits, motion deadline, exhibits, and whether the letter may be filed or must be sent to chambers. Do not add new requests, new facts, or a new theory in the correspondence without giving the other side a fair chance to address them.

### 5. Settlement demand, response, and counteroffer

Confirm client authority and objective first. Identify the disputed claim or claims, the proposed consideration, scope of release, parties released and excluded, payment timing and security, fees and costs, dismissal, confidentiality or public statement, non-disparagement, tax/lien/indemnity treatment, no-admission language, required approvals, preservation, governing law, integration, and who may accept. Use a term sheet or nonbinding proposal label only when it matches the intended mechanics.

Give enough supported liability and damages information to make the proposal intelligible without disclosing privileged strategy or asserting unverified facts. Separate “our position,” “the record,” “the proposal,” and “the terms still open.” Do not put an admissions package inside a settlement letter merely because the letter is marked “FRE 408.”

For a response or counteroffer, address material terms one by one: accepted, rejected, or open; reason in a sentence tied to the record or objective; revised term; deadline; and authority or approval condition. Do not say “final” unless the client means it and the acceptance mechanics are clear. If more information or authority is needed, say so accurately and request it.

### 6. Substantive pre-suit or case correspondence

Identify the client, sender, addressee, counsel, case or claim, and representation status. Screen Rules 4.2 and 4.3 before any direct contact. State the relevant facts as claims or positions when they are disputed, identify the legal or contractual basis, request preservation or a defined action, provide a lawful response date, and describe only consequences the client is prepared and authorized to pursue.

Before referring to possible criminal, disciplinary, or regulatory action, require counsel to check the governing jurisdiction's professional-conduct rules, substantive extortion or compounding law, the factual and legal basis, the relationship to the civil dispute, and whether the wording suggests improper influence. Do not include a baseless, misleading, unlawful, or jurisdictionally prohibited threat, promise an outcome the lawyer cannot control, or use an unrepresented person's misunderstanding. If notice, tolling, demand, removal, or a contractual prerequisite is important, identify the actual authority and procedural effect for lawyer review rather than implying that a letter alone accomplishes it.

Apply the exhibit test: assume the correspondence may be shown to a judge, jury, regulator, insurer, or opposing expert. Remove gratuitous personal attacks, unsupported motive claims, unnecessary personal data, privileged strategy, hidden metadata, and statements whose force depends on a misleading omission.

### 7. Review, no-send, and handoff

Run these checks before presenting the package: every material fact traces to a source or is clearly qualified; every legal proposition has an identified jurisdiction and as-of date; the audience and representation status are correct; every deadline is sourced or marked proposed; settlement authority and acceptance mechanics are explicit; discovery requests and conferral history are complete; attachments exist and are the intended versions; privilege, privacy, third-party, and inadvertent-production issues are flagged; and the draft does not claim that an action occurred when it was only proposed.

Always finish with `NO SEND — lawyer approval and a separate sending step required`. List the exact blockers, not generic “review needed”: for example, “confirm whether the $250,000 figure is authorized,” “confirm whether the Rule 37 call occurred,” or “obtain the signed protective order before attaching the client list.”

## Output contract

Return these sections in order:

1. **Recommended route and status:** one primary route, intended audience, posture, settlement/discovery status, and confidence.
2. **Internal reviewer note:** objective, source and authority gaps, risks, deadline analysis, client-authority questions, and proposed next action.
3. **Fact and source ledger:** material propositions with status, source IDs, locators, scope, and permitted use.
4. **Draft outbox:** subject or caption, recipients and copied recipients, status label, body, attachment manifest, and acceptance/deadline mechanics where applicable.
5. **No-send gate:** exact unresolved items and the approval needed for each.
6. **Optional negotiation or conference agenda:** only if it helps the lawyer resolve the defined issue without changing the requested route.

If the source set is incomplete, return a useful partial triage or scaffold, not a polished fiction. Say what cannot be concluded. If the user asks for a direct final letter despite a missing authority, client instruction, or material fact, keep the gap visible in the draft with a bracket and stop at the no-send gate.

## Source cascade and exemplar use

Use supplied matter documents and official public rules first. For public research, use official court, government, legislature, or rulemaker sources; an open public source is the default. If the firm requires licensed case law, docket, or currentness treatment, use the firm's authorized legal-grade service or have the lawyer supply the authority. Never upload client-confidential material to obtain a public exemplar.

The source ledger in [authority-and-provenance.md](references/authority-and-provenance.md) contains official ABA, federal-rule, court, government, and docket links. [real-exemplars.md](references/real-exemplars.md) records provenance and limitations for the Windsor discovery filing, Twitter/Musk correspondence series, J.P. Morgan SEC settlement-related correspondence, and a court-described pre-suit demand. Use them to discuss structure and judgment; render any reusable language from the synthetic patterns instead.
