---
name: timenarratives-legalquants
title: Time narratives
description: Draft concise time-entry narratives from the lawyer's work in the current conversation, selected related chats, LQ skill exchanges, and supplied accounts, documents or expressly selected folders. Resolve material uncertainty about the lawyer's contribution; return an unposted draft without time figures or billability decisions.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/timenarratives
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Cli Contract
  path: references/cli-contract.md
- title: Conversation Context
  path: references/conversation-context.md
- title: Document Context
  path: references/document-context.md
- title: Evidence Rules
  path: references/evidence-rules.md
- title: User Journey
  path: references/user-journey.md
---

# Time narratives

Use this skill when the user asks for `/timenarratives` or says “do my time entries.” Start from the current work conversation, including ordinary chat and exchanges involving other LQ skills. The lawyer need not upload files, invoke another skill, or repeat an account already established in accessible messages. Return an in-memory, unposted draft with only material factual questions.

Identify the lawyer and matter from clear current context. If either is missing or ambiguous, ask one compact question for the missing detail. Do not ask again for identity, source access or a scope the user has already supplied. Bind that response to the current map internally; the user never handles digests or implementation commands.

## Select and retrieve context

A bare invocation selects the current available conversation. “Do my narratives for Cedar today” also selects accessible work conversations within that clear matter and period. A bounded, explicit standing scope can do the same; a style preference cannot authorise access. Read [conversation-context.md](references/conversation-context.md) when using conversation context or retrieving related chats. Discover available host capabilities instead of assuming a particular product, local transcript store, connector or account-wide access.

Use the host's native conversation listing and reading capabilities where available. Identify matching conversations from metadata within the authorised scope, retrieve their original messages and follow pagination. Do not search unrelated conversations, a mailbox, calendar, drive, sibling folder or device. If the project contains multiple matters, project membership alone does not establish the selected matter. Ask only when the selection is materially ambiguous. An expressly selected folder authorises bounded inventory of that folder and its ordinary subfolders; a source-root setting or the current working directory alone does not select its contents. The selected local packet is a fixed inventory; later folder additions require a new selection.

Where retrieval is unavailable, use the current context and any explicitly selected export or brief account the lawyer supplies. Do not pretend memory or a summary is a complete transcript. State material coverage gaps and retrieve the missing source when possible before asking the lawyer. A source selection never proves a complete workday.

Separate the requested work period from source-message timestamps. A later message may describe earlier work; an old draft may corroborate today's review. Keep those sources available for analysis without silently changing an explicitly requested source-date filter. A date filter never expands scope. When the requested work date remains unclear, ask about that activity, not the entire packet.

## Add work outside the conversation

Alongside the first useful draft, offer briefly: “You can add documents or point me to a matter folder for work outside this conversation.” Do not wait for uploads or repeat the offer after the user has supplied their selection. Accept additional material at any stage, including after a draft has been displayed. The lawyer can instead give a brief account of a call, meeting or other work; documents are optional corroboration.

Read [document-context.md](references/document-context.md) for supplied files or folders. Combine the additional material with existing selected conversations and the lawyer's account in one packet; identify overlap, contradictions and unsupported details. Ask who did the work only where the answer is not established. A document describing substantial work does not by itself establish the lawyer's contribution. If new evidence materially changes a draft, redisplay it and obtain approval of that version.

## Attribute the lawyer's contribution

Read [evidence-rules.md](references/evidence-rules.md) when mapping activity. Every included activity needs actor, action, object and matter support. Keep the source author, person performing the work and named timekeeper distinct.

- A substantive challenge, analysis or correction in the lawyer's own messages can evidence that contribution. A request to generate a draft evidences a request; the AI's output does not establish lawyer review, adoption, delivery or completion.
- An LQ skill's report or tool receipt records the operation it actually performed. It does not prove that the lawyer personally reviewed the report, checked its authorities or reviewed its entire source corpus. Use the lawyer's subsequent scrutiny and decisions; do not rerun other skills to create a narrative.
- Sending, receiving, opening, owning or forwarding a document does not establish drafting or substantive review. Quoted colleague text inside a user message retains the colleague's attribution. A revision author or source timestamp does not independently prove the activity.
- A lawyer's supplied account is user-attested. Documentary silence means not corroborated, not contradicted. Resolve an express conflict or leave the affected claim out. Generic “use these” approval cannot answer an unresolved actor or action question.
- Incomplete or abandoned work can still involve real lawyer analysis. Describe the supported activity without adding a successful or completed outcome. Autonomous retries and background work do not create additional lawyer activities.

Distinguish alternatives with focused questions: “Did you revise the provisions, review someone else's revisions, or only circulate them?” Preserve the answer in the wording. If a call is supported but revisions are only planned, draft the call and ask about the revisions separately. Do not withhold every activity because one remains uncertain.

A single activity may span chats, skills and artifacts. Reconcile overlapping evidence without multiplying entries; preserve separate activities where supported. Do not include generating these narratives as part of the underlying legal work. Scheduling, forwarding without substantive review and access logistics are outside this skill's substantive-work scope; that does not decide their billability or deny that they occurred.

## Internal stages

When the bundled scripts are available, run [cli-contract.md](references/cli-contract.md) internally. Conversation snapshots enter the same packet, source identity, anchoring, map validation and publication path as documents. Keep speaker roles and original message locators; AI, tool, quoted and unknown-role units are context and cannot support included activity. Preserve source integrity, deduplicate selections and account for every supported source unit. The model supplies exact quotes; the anchoring helper computes byte spans and hashes.

Supported file adapters accept strict UTF-8 TXT/Markdown, EML and tracked-change DOCX. Use the versioned conversation snapshot adapter for host messages or selected exports; never disguise an assistant response as a user note. Unsupported or partly readable material remains visible as such. Do not silently truncate evidence or claim missing content was reviewed.

The model judges semantic support. Deterministic checks enforce source linkage, structural validity, prohibited output fields and snapshot freshness; passing them does not prove the factual truth of an attribution. If the bundled scripts cannot run, label the result **Unvalidated preview**. Do not call it copy-ready or final, do not publish machine-readable artifacts, and state which checks could not run. No extra user command is required to use a supported runtime.

## Firm style

Read only confirmed `[timenarratives]` entries in `lqplaybook.md`, if available. Never read the journey profile for work product. Use a concise neutral default when no style is configured; do not delay the draft for setup. Offer a one-time style choice alongside the first useful draft, or when the user requests it. Show the exact proposed preference and persist it only after explicit agreement.

Style controls brevity, grammatical form, abbreviations and workstream presentation. It cannot add activities, stronger responsibility, outcomes, time figures or billability judgments. Do not store client examples or matter facts as style settings. A session correction applies immediately to that draft; it is not automatic consent to change future preferences. This version retrieves related chats from the current request's clear scope; automatic recurring scope needs a host-managed, explicit and revocable policy, not an invented preference file.

## Review and output

Begin with **Draft entries**, followed by **Needs your check** only where facts could materially change an entry. Give one concise narrative per supported workstream, with short source labels or locators and a compact statement of the conversations/sources actually used. Do not put an uncertain activity verb into a copy-ready draft with a disclaimer. Preserve the withheld question separately. A supported first-response draft can be useful without filling every gap.

Keep source counts, digests and implementation vocabulary out of the normal flow. Use one or two brief plain-text paragraphs per workstream, within the existing narrative contract. Do not add advice, strategy or completed outcomes beyond the supported contribution. No durations, clock values, rates, fees, amounts, billing codes, billability decisions or posting instructions in model-authored narratives, JSON, Markdown or receipts. The skill does not calculate time or reconstruct the whole workday.

Retain the validated map digest when displaying the draft, before the user replies. The user may say “use these” or describe corrections. Factual answers resolve only the questions they actually answer. If a correction adds or changes material wording, show the revised entries before final approval. An unanswered question stays withheld; approval of supported entries need not wait for it.

Only then publish the machine-readable JSON/Markdown artifacts and final unposted draft after validation and freshness checks. Use the renderer's ordinary-approval mode with the digest retained from the displayed version; never recompute that reviewed digest from a changed map after approval. Any source or map change invalidates prior confirmation. Approval is session-recorded, not authenticated factual verification. No confirmation token is displayed or requested.

Show the final entries in full, followed by anything still withheld and what would resolve it, and the artifact locations. If no supportable activity remains, say so plainly and ask the focused question that could change that result. Do not equate an empty valid map with satisfying a request that had supported work.

Always include this scope sentence:

> Checked only the sources you selected; this drafts narrative text for review and does not estimate time, decide billability, or post entries.

Raw and derived source text stays in the owned temporary run. Retain the user's draft and receipt; delete owned temporary material on completion. Do not create a persistent matter store, write a companion journey log, or send client material elsewhere for validation. Keep source names and paths out of reusable settings. Published files inherit their parent's access control; use the user's private workspace.
