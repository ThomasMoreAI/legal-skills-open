---
name: organize-case-docs-legalquants
title: /organize-case-docs
description: Turn an accepted or active litigation matter’s documents and metadata into a provenance-backed case workspace with source inventory, chronology, proof charts, issue and evidence mapping, trackers, lifecycle controls, and an explicit docreview handoff. Use after controlled intake or when restructuring, updating, or closing a matter; use new-matter to create the initial matter record.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/organize-case-docs
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

# /organize-case-docs

Organize a matter around proof, provenance, ownership, and next decisions. The result is a navigable case record, not a prettier folder or an unverified narrative. The lawyer remains responsible for legal characterization, privilege, preservation, retention, deadlines, and final judgment. This skill must not contact parties, serve process, release a hold, delete records, or make a privilege ruling.

Read only confirmed `[organize-case-docs]` entries in `lqplaybook.md` if present. Never read `lqprofile.md` for work product and never write either file; the scribe owns journey updates. A preference revealed during the run may be proposed as an exact `[organize-case-docs]` line, but it affects future work only after the user explicitly confirms it.

## Inputs and authority

Use supplied pleadings, orders, productions, correspondence, transcripts, docket material, client instructions, and existing indexes first. Ask only for missing facts that change the structure: forum and posture, matter identity, source root or selected files, client objectives, and any known deadline or preservation trigger. Record an `as_of` date, source-set boundary, and missing categories. Treat client narrative and filenames as leads, not verified facts.

Confirm the forum, jurisdiction, governing law, scheduling order, standing orders, protective orders, confidentiality terms, and firm/client policy. Federal Rules of Civil Procedure 16, 26, 34, and 37(e) provide a useful federal baseline for issue definition, proportionality, preservation, ESI, and supplementation; see [sources](references/sources.md). State, arbitral, administrative, foreign, privacy, employment, regulatory, and insurer requirements may control instead.

## Tool cascade

Start with host-native document reading and local, open-source inventory or extraction. If a source cannot be read, preserve it, mark it unreadable, and ask for a readable export or user-selected tool. Legal-grade e-discovery, records, or document-management systems are optional user-selected rungs; disclose scope, retention, access, and transformations. Never require a connector, package, network service, hook, or particular model.

## Method

### 1. Confirm intake and build the working matter map

If `new-matter` has produced an approved intake record, import it rather than asking again. If no approved record exists, collect only the minimum cold-start fields needed to organize the supplied case materials and flag engagement, conflicts, identity, authority, or destination gaps for the `new-matter` workflow. Then create a working matter map with stable `matter_id`, caption, client and parties, forum, jurisdiction, venue, case number, procedural posture, engagement and conflicts status, client objectives, claims and defenses, remedies and damages, known orders and deadlines, preservation trigger and hold status, confidentiality classification, team and owners, source locations, initial risks, known unknowns, and next actions.

Separate `reported`, `source-supported`, `inferred`, `disputed`, `privileged`, and `unknown`. Record who supplied each instruction and its date where material. Do not make legal conclusions from an intake narrative or silently assume that a deadline, party identity, or preservation duty exists.

### 2. Inventory, identity, and preservation

Create one source-manifest row for every selected source, including unreadable, duplicate, privileged-candidate, and out-of-scope records. Use a stable content ID or source ID; preserve relative paths, native names, byte counts, hashes, formats, page counts, custodian, author, date range, acquisition method, and transformation history. Keep native originals read-only and work derivatives separate. Never silently overwrite a source or erase an earlier manifest.

At intake, identify potentially relevant systems, custodians, retention settings, legal-hold status, collection gaps, and destruction or overwrite risks. Record preservation actions and decision owners. The manifest documents what was examined; it does not establish relevance, privilege, authenticity, or completeness by itself.

Recommended source-manifest fields are in [source-manifest-template.csv](templates/source-manifest-template.csv). The current [EDRM Model](references/sources.md) is a conceptual lifecycle aid: identification, preservation, collection, processing, review, production, presentation, and disposition, with analysis continuing throughout.

### 3. Build a provenance-backed chronology

Use stable event IDs and one row per material event. Required fields are date/time and precision, time zone, actor or entity, source ID, exact page/Bates/line/timestamp, source quote or careful paraphrase, fact status, linked claim/element, witnesses and exhibits, confidence, attorney inference kept separately, follow-up, owner, and last verification.

Do not merge multiple sources into one “clean” event without retaining each source location. Record contradictions, omissions, and alternative dates visibly. The chronology should answer what changed, what supports it, and what remains unknown.

### 4. Build the claim/defense proof chart

For each claim and defense, record the jurisdictional legal authority, effective date, pleading reference, element or required showing, burden, admitted/disputed/unknown status, supporting and opposing sources, witnesses, exhibits, missing evidence, discovery task, dispositive significance, settlement significance, and last review. Keep the authority for the element separate from the factual proposition intended to satisfy it.

### 5. Build the issue/evidence matrix

Use one row per issue or proposition:

```text
issue_id, issue_question, claim_or_defense, element, proposition, burden,
supporting_source_ids, opposing_source_ids, exact_locations, witness_ids,
exhibit_ids, admissibility_or_foundation, contradictions, confidence, status,
next_task, owner, due_date, last_updated
```

Every material issue must end in a status and next action. Use `verified`, `asserted`, `contradicted`, `unknown`, `privilege-held`, `needs-lawyer-decision`, and `closed` deliberately. No source-free summary may move an issue to verified.

Treat the chronology and claim/defense chart as useful starting artifacts, not a fixed ceiling. Choose the representation that answers the lawyer's actual question: an event timeline, element-by-element proof table, contradiction matrix, witness-to-issue map, relationship diagram, damages table, exhibit crosswalk, decision tree, or another chart or tabular view. Every derived view must retain the stable source IDs, exact locations, statuses, contrary evidence, and as-of date behind it. Use `client-update` for an audience-filtered report and an available legal-design or visualization capability for a polished visual companion; neither may replace the underlying evidence table or change its legal characterization.

### 6. Maintain linked trackers

The witness tracker should include role, party or nonparty status, representation/contact restrictions, knowledge topics, elements, sources, exhibits, credibility and impeachment flags, availability, subpoena or service status, preparation/deposition status, designation status, privilege/confidentiality, owner, and next action.

The exhibit tracker should include stable exhibit and Bates IDs, source ID, description, date, author, custodian, native name, hash/version, collection and production status, authentication/foundation path, linked issues, intended uses, privilege/PII/redaction, objections, designations, and last verification.

The deadline tracker should include event, authority or order, trigger event and timestamp, time zone, computation method, due date, owner and backup, dependencies, filing/service method, reminders, extension or waiver, completion timestamp, completion evidence, and status. Record or recompute a date only against the current governing rule or order, preserve the inputs and method, and require docketing review; do not assume a universal counting convention or holiday calendar.

### 7. Produce an internal matter briefing view

Generate a concise briefing from the same linked record, not from a second narrative store. Lead with current posture and client objective, then claims and defenses, proof status by material issue, adverse facts and contradictions, pending motions or discovery, deadlines, decisions needed, owners, and the next 30 days. Cite every material statement to the chronology, proof chart, issue matrix, or source manifest and show stale or missing inputs. This is an internal matter-team view; route an audience-filtered external report, insurer report, board view, or portfolio update to `client-update`.

### 8. Use a stable workspace

Before writing anything, confirm the intended destination and whether the user wants only a proposed layout or an actual workspace. Do not move or rename native originals by default; preserve them in place and use manifest references, or copy them into an approved destination only when the user authorizes that operation and the provenance record preserves the source and transformation.

Use a configurable layout with stable IDs and a manifest crosswalk:

```text
00_admin/              intake, engagement, conflicts, contacts, matter map
01_pleadings_orders/   pleadings, docket, orders, local rules, protocols
02_sources_native/     immutable originals and source manifest
03_sources_work/      OCR, normalized, and review derivatives
04_issues/             claim-defense chart, issue-evidence matrix, authorities
05_chronology/         chronology, contradiction and source-gap logs
06_witnesses/          witness tracker, interviews, deposition records
07_exhibits/           exhibit/Bates map, production, redaction, versions
08_discovery/          requests, responses, privilege and preservation records
09_calendar/           deadline tracker, reminders, notices
10_work_product/       legal work product and strategy, access-controlled
11_hearing_trial/      motions, designations, exhibits, demonstratives
90_close/               transfer, retention, hold-release, disposition logs
```

The layout is a recommendation, not a legal requirement. Keep client/source layers distinct from privileged strategy. Use relative paths in portable artifacts, stable IDs instead of semantic filenames, and a visible README/matter map containing source-set boundary, last verification, and open gaps.

### 9. Make an explicit docreview handoff

If documents need document-level responsiveness, privilege, confidentiality, issue coding, family/thread, or production review, create an explicit handoff to [docreview](../docreview/SKILL.md). Do not silently perform or imply a privilege ruling during organization.

The handoff should contain:

- `matter_id`, scope, purpose, review questions, forum, and as-of date.
- The exact manifest or source-set digest and relative source paths.
- Stable source IDs, hashes, byte counts, format/readability, custody, and known transformations.
- Included, excluded, unreadable, duplicate, and held-source partitions.
- Requested review lenses such as responsiveness, privilege candidate, confidentiality, issue, or family/thread.
- Known limitations, proposed sampling or approval step, and the lawyer’s decision needed.
- A return contract naming where review findings, privilege rulings, gaps, and source-to-issue links should be reconciled.

The handoff is a request, not authorization to review or release a hold. If the source set has drifted, the manifest is incomplete, or a required file is unreadable, emit `blocked` or `needs-review` rather than a clean handoff. Align machine fields with the sibling docreview manifest, review-plan, and privilege-ruling contracts; do not copy its scripts or invent a parallel schema.

### 10. Reconcile, update, and close

After each material filing, production, interview, deposition, order, or client instruction, update linked artifacts and record what changed, why, source location, owner, and next deadline. Preserve prior versions and an append-only audit log. Surface stale or conflicting rows; do not silently choose one.

For closeout, check judgment or settlement effectiveness, appeals and enforcement, indemnity/audit/insurance/malpractice holds, outstanding deadlines, client property and transfer instructions, legal-hold release authority, retention trigger, applicable jurisdiction and firm policy, authorized disposition method, date, operator, and certificate. Retain a final read-only matter index and transfer/disposition record. Retention is configurable and jurisdiction-specific; never hard-code a universal period.

## Deliverables

Produce a human-readable matter map plus structured artifacts where practical:

- `matter-map.md/json` using the [template](templates/matter-map.md).
- `source-manifest.csv/jsonl` using the [template](templates/source-manifest-template.csv).
- Provenance-backed chronology.
- Claim/defense proof chart and issue/evidence matrix.
- Witness, exhibit, and deadline trackers.
- Preservation, gap, version, and audit logs.
- Internal matter briefing with posture, proof status, adverse facts, decisions, deadlines, owners, and next-30-day work.
- Explicit `docreview-handoff.json` or a recorded `no-handoff` decision using the [handoff template](templates/docreview-handoff.md).
- Closeout, transfer, retention, and disposition record.

Lead with `Known`, `Unverified or disputed`, `Missing`, `Needs lawyer decision`, and `Next actions`. Include `as_of`, source-set boundary, jurisdiction, confidence/status, and exact source locations. Do not invent party facts, dates, legal authority, or document contents.

## Quality gate

Before delivery, verify that:

- Matter identity, forum, posture, authority, source-set boundary, and as-of date are explicit.
- Every selected source—including unreadable and duplicate material—is represented in the manifest or an explicit exclusion partition.
- Native originals, derivatives, IDs, hashes, paths, custody, and transformations reconcile.
- Every chronology assertion and issue/evidence row has an exact source location and status.
- Every claim/defense element has evidence or an explicit gap and next action.
- Witness, exhibit, and deadline trackers link to the relevant issues and have owners.
- The internal briefing reconciles to the linked matter artifacts and does not masquerade as an audience-cleared client update.
- Deadline arithmetic, time zone, service method, order, and local-rule assumptions are visible.
- Privilege, confidentiality, PII, legal hold, and work-product material are not silently classified or released.
- A docreview handoff is explicit, digest-bound, scope-complete, and blocked on drift or unreadable required material.
- Material updates preserve prior versions and explain changes.
- Closeout checks transfer, appeal, insurance, malpractice, retention, hold release, and disposition authority.
- A lawyer reviews legal characterization, privilege, preservation, retention, deadlines, and final strategy.

## Limits

This skill builds a structured case workspace; it is not a docketing system, records-retention opinion, legal-hold release, privilege determination, or substitute for the governing forum’s rules and professional judgment. It must not autonomously contact anyone, file or serve anything, issue process, release a hold, waive a right, or delete matter material.
