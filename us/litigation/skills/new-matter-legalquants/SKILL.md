---
name: new-matter-legalquants
title: New Matter
description: Open a litigation matter through a human-confirmed intake that records the parties, role, side, forum, engagement and authority, conflicts posture, emergency dates, preservation posture, status, stable identifiers, and field-level provenance. Use when a new dispute, claim, subpoena, regulatory inquiry, investigation, or pre-suit threat needs a controlled matter record and a handoff to organize-case-docs.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/new-matter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: First Matter Setup
  path: references/first-matter-setup.md
- title: Matter Record Template
  path: references/matter-record-template.md
- title: Preservation At Intake
  path: references/preservation-at-intake.md
---

# New Matter

## Outcome and boundaries

Create a reviewable matter record and a clear next-step handoff. This skill organizes what the human supplies; it does not decide whether a conflict exists, establish representation, give a merits opinion, compute a legal deadline, issue a legal hold, contact anyone, send or file anything, calendar an event, or mutate an external system. Any authorized read-only retrieval is a source lookup, not a clearance or other decision.

The record is an intake and routing artifact, not a pleading, legal opinion, conflict certificate, engagement letter, preservation notice, or merits assessment. Unknown, disputed, and unverified facts remain visible.

Only confirmed `[new-matter]` entries in `lqplaybook.md` may shape this work. Never read `lqprofile.md` during intake and never write either file; the scribe owns journey updates. A preference revealed during intake may be proposed as an exact `[new-matter]` line, but it affects future work only after the user explicitly confirms it. Never put client-confidential facts into a playbook or journey record.

## Tool and source cascade

Use the host's available local file and document-reading capability first. If a user-authorized matter-management, document, or legal-process system is available, use it only for the narrow read the user approved and preserve its returned receipt or locator. Durable writes stay in the user-designated workspace; if an external store is the only available destination, return the approved record as unsaved unless the user separately authorizes that external write. If a capability is unavailable, continue with user-provided files and mark the missing source; never claim that a configured integration was checked merely because it is listed.

## Intake posture

Ask no more than three focused questions in one turn, then wait. Reuse answers and documents already supplied in this session, but do not infer missing representation, party identity, side, forum, conflict status, deadline, or preservation facts from tone, filenames, or ambient context.

If the request is only “open a matter” without enough information to identify the engagement, begin with the smallest useful batch:

1. Who is the client or represented entity, who are the known opposing or affected parties, and what happened in one or two sentences?
2. What is our role and side, and what court, tribunal, regulator, arbitration forum, or pre-suit setting is involved?
3. Is there an emergency date, a human-asserted conflicts posture, or a preservation concern that must be visible now?

If the user supplies a complete intake, do not repeat these questions. Ask only for the gaps that would change routing or safety.

### Workspace defaults and first use

Perform a read-only architecture check only in the current workspace, a matter root the user identifies, or a host-selected matter root whose scope is visible. Look for an index, stable-ID marker or convention, matter-record template, workspace README, recognizable folder pattern, source manifest, or matter-management record. Report `architecture_check: found | not-found | ambiguous | unavailable`; a failed, inaccessible, or unclear check is not `not-found`.

If a usable architecture is found, summarize its markers and offer to use it while preserving its paths, identifiers, naming, and access boundaries. Do not create a parallel layout or migrate it merely because it differs from the packaged recommendation. If the result is ambiguous or unavailable, show the candidates or access gap and ask the user; do not guess.

If the check is `not-found`, or the user says this is their first matter and no architecture is known, offer to create the minimum reusable defaults before saving. Read [first-matter-setup.md](references/first-matter-setup.md) only if the user accepts that offer or asks to customize setup. A standalone matter record remains available if the user declines. Reusable behavioral preferences still require confirmed `[new-matter]` playbook entries; workspace defaults never become an ambient firm profile.

## Step 1: Establish the source boundary and check for a possible duplicate

Use, in order:

1. Facts and files the user supplies in this session.
2. A matter index or workspace the user explicitly identifies for a read-only duplicate check.
3. A user-named source system, only if the host can actually retrieve the requested record.

Assign each supplied source a stable source ID such as `SRC-001`. Record its human-readable locator, source kind, and what fields it supports. A source that cannot be opened is still recorded as `unreadable` or `unavailable`; it is not silently treated as absent.

Normalize the proposed title and principal party names only to search for possible duplicates. If an existing record could be the same engagement, show the candidate and ask whether to update it or create a distinct matter. Do not silently merge, overwrite, or create a second record. A duplicate search that was not run is recorded as `duplicate_check: not-run`, not as “no duplicate.”

## Step 2: Capture identity and parties

Record exact names as supplied, along with the role each entity or person plays:

- Matter title used by the team.
- Client or represented entity, including the internal business unit if applicable.
- Opposing, adverse, responding, investigated, issuing, or otherwise affected parties.
- Known counsel, insurer, regulator, court, agency, or arbitrator.
- Case, docket, claim, investigation, subpoena, or reference number if supplied.
- How the matter arrived: complaint, demand, subpoena, regulatory inquiry, internal report, investigation, or pre-suit threat.
- One-sentence factual description, limited to what the user or a supplied source states.

Keep entity names distinct. Do not collapse a parent, subsidiary, affiliate, officer, insurer, or counsel into “the other side.” If an entity's relationship is unclear, record it as `relationship: unknown` and ask a focused question.

## Step 3: Capture role, side, and forum

Record the human-selected values; do not infer them from the caption alone:

- **Representation role:** `plaintiff | claimant | defendant | respondent | subpoena-recipient | investigated-party | witness | neutral-third-party | other | unknown`.
- **Side:** `claimant-side | defense-side | neutral-third-party | mixed | unknown`.
- **Forum:** `court | arbitration | regulator | administrative | internal-investigation | pre-suit | unknown`.
- **Jurisdiction and venue:** exact court, tribunal, agency, governing jurisdiction, and venue when supplied.
- **Governing law:** only if supplied or identified in a source; do not treat the forum as the governing law.
- **Procedural posture and stage:** `inquiry | threatened | active | stayed | resolved | closed | unknown`, plus `pre-suit | pleadings | discovery | dispositive-motion | trial | appeal | regulatory | investigation | unknown`.

Store the basis for each choice as `user_asserted`, `source_stated`, `derived-pending-confirmation`, or `unknown`. A derived role or side is a prompt for confirmation, never a confirmed field.

## Step 4: Record conflicts and engagement as human-verified assertions

This skill records a conflicts posture; it does not run a conflicts search. Use exactly one of:

`cleared | pending | not-run | waived | unknown`

For every value, capture:

- The person's or team's assertion, in concise words.
- `verified_by` and `verified_at`, if supplied.
- `method` as the human describes it, such as firm system, client list, outside counsel, or informal review.
- Names and entity variants checked, including known affiliates, adverse counsel, and key witnesses when supplied.
- Scope, limitations, and any exception or waiver reference.
- Source IDs supporting the assertion.

Never convert absence of a conflict note into `cleared`. Never report that a database, firm system, or connector was queried unless the host actually returned a result. If the user says “cleared,” record `status: cleared`, `basis: user_asserted`, and the assertion metadata; do not upgrade it to a system-verified result.

Record engagement separately from conflicts:

- `not-engaged | proposed | signed | declined | unknown`.
- Client or represented entity, scope, effective date, and termination or expiry if supplied.
- Outside counsel or internal legal team, lead, and contact details if supplied.
- Who may instruct counsel, sign a communication, approve a settlement, authorize spend, or make an emergency decision.
- Any authority limit, reservation, or required escalation, with its source and confirmation state.

“Counsel named” is not the same as “engaged,” and “engaged” is not the same as “authorized to settle or act.” Keep those fields separate.

## Step 5: Screen emergency dates without inventing law

Ask for dates that could change the immediate route:

- Date received, served, discovered, or escalated.
- Any response, objection, cure, hearing, filing, production, interview, appeal, or preservation deadline.
- Source-stated date, time, and time zone.
- Whether the date is legal, procedural, contractual, business, or unknown.
- Whether an extension, tolling agreement, or human calculation has been confirmed.

Do not calculate a deadline from a rule, service date, business-day convention, or time zone unless the user supplies the calculation or separately authorizes a current authority check. Preserve both the source-stated date and any human-provided calculation.

For an intake as of a known date, record the as-of date and use these workflow labels only:

- `overdue` — the supplied date has passed.
- `imminent` — the supplied date is within seven calendar days.
- `near-term` — the supplied date is eight to thirty calendar days away.
- `future` — the supplied date is more than thirty calendar days away.
- `unknown` — the date or comparison basis is incomplete.

An overdue or imminent item gets a visible `URGENT — HUMAN REVIEW NOW` flag, the source and uncertainty, and a recommendation to contact qualified counsel or the official source promptly. The flag does not send, file, calendar, extend, or otherwise execute anything.

## Step 6: Record preservation posture

Ask the human to state whether a preservation duty or concern has been identified. Record the answer and its basis rather than deciding the legal question:

- `not-assessed | not-triggered-asserted | anticipated-asserted | hold-requested | hold-issued | released | unknown`.
- Triggering event and date.
- Hold owner, notice date, scope, custodians, systems, date range, and refresh or release information if supplied.
- Known gaps, including inaccessible systems, missing custodians, auto-delete concerns, or unclear ownership.
- Source IDs supporting each field.

For a new litigation matter, subpoena, investigation, or credible pre-suit threat, remind the user to raise promptly with the client or responsible legal team whether counsel has assessed the preservation trigger and whether reasonable steps have been taken to identify and preserve potentially relevant information. Do not imply that opening a matter proves a duty arose or that a litigation-hold notice alone satisfies it.

If preservation posture is `not-assessed`, `hold-requested`, unknown, incomplete, disputed, or urgent, read [preservation-at-intake.md](references/preservation-at-intake.md) and surface the gap prominently. For a U.S. federal civil matter, offer a focused preservation-planning handoff to `document-discovery`. For another forum, offer forum-specific preservation research and planning, using `regulatory` to retrieve controlling official text when appropriate; do not treat the federal workflow as controlling. Do not issue, release, or modify a hold from this skill.

## Step 7: Capture status and immediate routing

Status is a human-verified assertion, not a machine inference. Record:

- `status`: `inquiry | threatened | active | stayed | resolved | closed | unknown`.
- `status_basis`: `user_asserted | source_stated | derived-pending-confirmation | unknown`.
- `status_verified_by`, `status_verified_at`, and `status_source_ids` when supplied.
- Current stage, immediate decision or need, next known date, and responsible human if supplied.
- Related matters and the reason for each relationship, without reading across them unless the user explicitly authorizes that review.

If the user has not made a status call, use `unknown` or `inquiry` only with an explicit rationale such as “initial intake only”; do not silently label a matter active because a document exists.

## Step 8: Build the stable record and provenance ledger

Use the template in [matter-record-template.md](references/matter-record-template.md). The record must contain:

- A stable `matter_id` assigned once after the user accepts the proposed identity. It may use a user-approved slug and collision-safe suffix, but it must never be regenerated from a later title edit or reused for a different matter.
- `record_version`, `record_state`, creation date, last-updated date, and the approver for the current version.
- Field-level provenance: each material field points to one or more source IDs and states whether it is `user_asserted`, `source_stated`, `derived-pending-confirmation`, or `unknown`.
- A complete list of open questions, blockers, unavailable sources, and human decisions still required.
- The exact action boundary: what this skill prepared and what it did not do.

Do not store credentials, access tokens, hidden prompts, or unrelated client matters. Keep source locators relative or user-provided where possible, and preserve original source wording when a status, conflicts, authority, or date assertion matters.

## Step 9: Preview before writing

Before any durable write, show:

1. The proposed `matter_id`, title, and record state.
2. The role, side, forum, status, conflicts posture, engagement, authority, emergency dates, and preservation posture.
3. Open questions, possible duplicates, unavailable sources, and every field marked derived or unknown.
4. The proposed handoff to `organize-case-docs`, including the source IDs and requested outputs.
5. A plain statement that no conflict search, legal hold, calendar entry, contact, filing, service, upload, or other external action has occurred.

Ask for an unambiguous approval of both the displayed record and its save destination, or for an edit or pause. Ordinary language such as “looks good, save that record there” is sufficient; praise or a request to continue that does not clearly authorize the displayed save is not.

If the user does not approve, return the preview and do not write. If the host cannot write to the user-designated location, return the complete record in the template format and say that it remains unsaved.

## Step 10: Save and hand off

After explicit approval, write only the approved record to the user-designated matter workspace. Do not overwrite an existing record without an explicit update instruction and a versioned diff. If the user's canonical matter store is external, do not write to it unless the user separately authorizes that external action; return the approved record as unsaved instead. Re-read the saved bytes if the host permits and report the path or locator, record version, stable ID, and any write limitation.

Do not automatically start another skill. Offer an explicit handoff to `organize-case-docs` with:

- `matter_id` and record version.
- Approved source IDs and their locators.
- Requested outputs, such as document inventory, chronology, issue framework, claim/element chart, or source-gap report.
- Privilege, confidentiality, disclosed-document, or use restrictions the human supplied.
- Unresolved questions and inaccessible sources.
- A statement that `organize-case-docs` must independently apply its own source, privilege, and approval gates.

If no documents were supplied, the handoff says `awaiting sources`; it does not invite the next skill to invent a corpus or infer facts.

## Output contract

The terminal response contains:

- `Intake result`: `preview-ready | saved | paused | blocked-on-information | write-unavailable`.
- Stable `matter_id` and `record_version` when assigned.
- A one-screen summary of identity, role/side/forum, status, conflicts assertion, engagement/authority, urgency, and preservation.
- Open questions and blockers, with source IDs where relevant.
- Architecture-check result and the existing or proposed workspace convention, if any.
- The exact save path or an explicit unsaved notice.
- Handoff details for `organize-case-docs`.
- External actions not taken.

## Guardrails

- Never certify conflicts, representation, authority, preservation, status, or deadline accuracy on the skill's own judgment.
- Never turn a missing field into a reassuring default. Use `unknown`, `not-run`, `pending`, or `not-assessed`.
- Never compute or quote a legal deadline without a supplied source or a separately verified authority record.
- Never merge matters, cross-read another matter, or reuse an ID without explicit human direction.
- Never issue or release a legal hold, contact counsel or a party, create a calendar event, send or file a document, or upload source material.
- Keep the human's role, side, forum, and authority choices distinct; do not flatten them into a generic “client matter.”
- Treat a possible duplicate, an overdue/imminent date, an unresolved conflict, and a preservation gap as visible blockers or warnings, not silent routing decisions.
