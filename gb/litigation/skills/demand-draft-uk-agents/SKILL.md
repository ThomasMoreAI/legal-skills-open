---
name: demand-draft-uk-agents
title: /demand-draft
description: Draft a Letter Before Action or Letter of Claim from a completed intake, gated on a privilege / without-prejudice / waiver / admission checklist, with a .docx output, post-send checklist, and an offer to create a matter. Use when the user says "draft the demand", "write the [type] letter", or has a finished demand intake ready to turn into a sendable draft.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/demand-draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /demand-draft

1. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/[slug]/intake.md`. Refuse if missing or strategic block empty (for material demands).
2. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → Letter Before Action practice, house style, seed-doc table.
3. Follow the workflow and reference below.
4. Run the pre-draft gate: privilege filter, admission risk, without-prejudice posture, waiver scan, tone, factual accuracy. Do not proceed until each is engaged.
5. Template select: seed doc if provided in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`; else soft template for the demand type.
6. Draft in-chat for review. Iterate until user approves.
7. Write `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/[slug]/draft-v[N].docx` using the docx skill.
8. Write `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/[slug]/checklist.md` (post-send checklist).
9. Assess materiality per heuristic; offer to create a matter. If yes: hand off to `matter-intake` with pre-populated fields.

---

# Demand Draft

## Purpose

Take a completed intake and produce a sendable draft. Most of the value is in refusing to draft until privilege, waiver, admission, and settlement-communication posture have been consciously addressed — the failure mode is a letter that waives LPP or constitutes an admission because no one paused to check.

## Record fidelity — quotes and pinpoints

Demand letters are advocacy, and every quoted line from a contract, an email, or a prior communication becomes an assertion the counterparty will test.

**Verbatim quotes must be verbatim.** Never put quotation marks around words attributed to the counterparty, their solicitors, a witness, or any document unless you have the exact passage in front of you. When you want to characterise without the exact words:

- **Paraphrase without quotation marks**, with a placeholder: "Your [date] email stated X `[verify exact quote — email cite pending]`."
- **Never fill the gap.** A misquoted contract provision in a demand letter is the fastest way to lose credibility with the counterparty's solicitors on the first round.
- Every `[verify exact quote]` must be flagged in the reviewer note before the letter leaves.

**Pinpoint cites must support the whole proposition.** If the demand asserts "Clause 4.2 requires payment within 30 days upon invoice receipt," the cited clause must cover the obligation AND the trigger AND the window. If it only covers one, split the cite or narrow the proposition.

## Candour about weak arguments

When the law or the record is against a point, don't dress it up as solid. When an argument in the demand is weak — the contract language is ambiguous, the authority cuts the other way, the damages theory is a stretch — flag it for the sender:

> "The [claim / theory] here is weak because [authority / fact]. Options: (a) press it and frame as `[alternative framing]`, (b) drop it and rely on [stronger claim], (c) keep it as a hook but hedge the language. `[review — strategic call]`."

## Echo vs repeat

If the matter has prior correspondence, echo the key terms — the same characterisation of the breach, the same framing of the core obligation, the same name for the transaction. Don't lift whole sentences.

> **External deliverable:** the drafted Letter Before Action is sent to the counterparty. Do NOT include a `PRIVILEGED & CONFIDENTIAL — LEGAL PROFESSIONAL PRIVILEGE` header on the outgoing letter. The post-send checklist and the intake file are internal work product and do carry the header.

## Side context

Drafting a Letter Before Action is inherently an assertion — the sender is making a claim. Read `## Side` in the practice profile:

- **Claimant (default for this skill):** demand-draft aligns with the posture. The letter is the assertion of the claim. Tone, consequence language, and relief demanded all flow from the claimant-side playbook.
- **Defendant:** demand-drafts are less common from defendants but do happen — a defendant may send a counter-demand, a contribution notice, or a demand in an unrelated matter. Confirm before drafting: "You said defendant is your default. Is this matter claimant-posture for you (you're asserting a claim), or is this a different posture?"
- **Both / varies:** ask per-draft which posture applies.

## Posture for this matter

Before the pre-draft gate, confirm the matter-level posture. Read the intake's `## Posture` section if present; asking if not:

> **Posture for this matter.** Letter Before Action tone and terms are case-by-case, not a practice default. Confirm:
> - **Tone:** measured / assertive / aggressive?
> - **Response window:** what's reasonable given the claim? (Check the applicable CPR pre-action protocol — several protocols specify mandatory response periods.)
> - **Marking:** without prejudice / without prejudice save as to costs / open assertion?
> - **Signer:** you / client / GC / instructed solicitors?
> Don't assume. Read the prior correspondence in the matter file if there is any — it establishes the register.

The answers drive tone verb choice, the consequence language, the `Without prejudice` / `Without prejudice save as to costs` header (or its absence), the signature block, and the compliance deadline.

## Jurisdiction assumption

This draft assumes the governing law identified in the intake and the applicable CPR pre-action protocol (or the default Practice Direction on Pre-Action Conduct where no specific protocol applies). Failure to comply with the applicable pre-action protocol can result in costs sanctions and adverse inferences under CPR. Confirm the applicable protocol before sending.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/[slug]/intake.md` — required; refuse to proceed if missing
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → Letter Before Action practice (seed-doc paths, insurance-tender timing, materiality threshold for matter creation), house style. **Tone, compliance period, marking, and signer come from `## Posture for this matter`.**
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` — to check for existing related matters (same counterparty) and offer cross-link

### Strategic-block skipped handling

If the intake has `strategic_block: skipped` or `partial`, prompt the user before running the pre-draft gate:

> The intake skipped [all / some] of the strategic block (leverage, BATNA, tone, privilege filters). Drafting now will produce a usable letter but the strategic sections will be generic and flagged with `[SME VERIFY]`.
>
> - **Complete strategic block now** — pause, return to `/demand-intake [slug] --resume-strategic`
> - **Proceed anyway** — continue to pre-draft gate; downstream sections flagged

If "proceed anyway," every section of the draft that depends on a skipped strategic question gets `[SME VERIFY: [specific question]]` inline.

## Flags

- `--skip-gate` → bypass the pre-draft checklist. Available but logged; use only when the checklist was run separately and documented.
- `--version=N` → draft as `draft-vN.docx` (default: next version number)

## The pre-draft gate

**This runs before any drafting. If the user doesn't engage with it, stop.**

```
PRE-DRAFT CHECKLIST — [slug]

1. Privilege filter
   Per intake privilege filters: [list]
   Confirm: none of these will appear in the draft?  [y/n]

2. Admission risk
   Per intake admission risk: [list]
   For each, is the phrasing controlled or removed?  [y/n per item]

3. Without-prejudice posture
   Intake says: [without prejudice / without prejudice save as to costs / open]
   Note that protection attaches from conduct and context, not merely from
   labelling. A letter that discusses compromise in the body is a settlement
   communication regardless of the marking. A letter that makes no concession
   and asserts only rights is open.
   Draft will [include / omit] the without-prejudice marking, and will be
   structured so the substance supports the posture.
   Confirm.

4. LPP waiver scan
   Will any sentence in the draft reveal the substance of our internal
   legal analysis (not just the conclusion)?  [y/n]
   If yes, rephrase before drafting.

5. Tone posture
   Intake says: [relationship-preserving / measured / scorched-earth]
   This will drive verb choice, framing, and consequence language. Confirm.

6. CPR pre-action protocol compliance
   Applicable protocol: [name / default PD on Pre-Action Conduct]
   Does the letter comply with the protocol's content and timing requirements?
   [confirm / flag any gap]

7. Factual accuracy
   Every fact in the draft must be verified. Not "probably true" — verified.
   List any facts that are not yet verified, and they will be flagged
   [VERIFY: ___] inline.
```

Only proceed when the user has engaged with each item.

## Template selection

### Step 1: Seed doc

Check `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → Letter Before Action practice → seed-doc table for the intake's demand type.

- **Seed doc provided:** read it. Match structure, tone, signature block, privilege markings, typical section ordering.
- **No seed doc:** use the soft template below for the demand type.

### Step 2: Soft templates (used only when no seed doc)

**Payment demand / Letter Before Action skeleton:**
1. Parties and relationship context (1 paragraph)
2. Facts — the obligation and its source (contract clause / invoice / order), dates
3. The default — what's owed, when due, what happened (or didn't)
4. Demand — specific amount in sterling, deadline, method of payment
5. Consequences — referral to solicitors, interest (including Late Payment of Commercial Debts (Interest) Act 1998 if applicable), costs, proceedings
6. Preservation notice (if relevant)
7. Signature block

**Breach / cure notice skeleton:**
1. Parties and agreement (identify the contract — effective date, parties)
2. The obligation alleged breached — contract clause, plain language
3. The breach — specific facts, dates, evidence available
4. Cure — what specifically would cure; cure period (from contract or reasonable)
5. Consequences of failure to cure — termination, damages, specific remedies in the contract
6. Preservation of rights
7. Signature block

**Cease & desist skeleton:**
1. Parties and our rights (trade mark / copyright / contract / common law — identify the right under UK law)
2. The infringement / violation — specific acts, dates, evidence
3. Demand — cease immediately, remove, account for past use, confirm compliance in writing
4. Compliance deadline
5. Consequences of non-compliance — proceedings, injunctive relief, statutory remedies if applicable (e.g., Trade Marks Act 1994, Copyright, Designs and Patents Act 1988), costs
6. Preservation demand (documents, metadata, systems related to the alleged conduct)
7. Signature block

**Employment separation demand skeleton:**
1. Parties and relationship context (ex-employee, dates of employment)
2. The obligation — post-employment obligations breached (confidentiality, non-solicitation, non-compete, IP assignment); cite the agreement
3. The specific conduct alleged
4. Demand — cease, return property/IP, confirm compliance, non-disparagement reinforcement if applicable
5. Consequences — proceedings, injunctive relief, damages; note garden leave / restrictive covenant enforceability under English law `[SME VERIFY: restrictive covenant enforceability is highly fact-specific under English law — confirm with external solicitors before sending]`
6. Offer of informal resolution (if strategically appropriate)
7. Preservation demand
8. Signature block

**Preservation demand skeleton:**
1. Parties and context — what dispute is anticipated
2. Scope — categories of documents, data, systems, communications
3. Custodians — named individuals expected to have relevant material
4. Date range
5. Affirmative preservation obligation — suspend auto-delete, preserve metadata, preserve devices
6. Consequences of spoliation — adverse inference, applications for specific disclosure, wasted costs
7. Acknowledgment request
8. Signature block

## Drafting rules

1. **Specificity over adjectives.** "On 14 March 2026, you sent X" beats "You repeatedly and improperly sent X." Adjectives are the draftsperson's tell that the facts are thin.

2. **Facts traceable to sources.** Every factual assertion maps to a document, date, or witness. If not verifiable yet: `[VERIFY: specific claim]`.

3. **Citations as placeholders.** `[CITE: statute/clause/case]` wherever legal authority goes. Do not invent citations. If the user provided authorities in the intake, use them faithfully. Use OSCOLA citation style.

4. **Consequence language matches tone posture.**
   - `relationship-preserving`: "We hope to resolve this without further action."
   - `measured`: "If not remedied within [N] days, we will consider our options, including issuing proceedings."
   - `scorched-earth`: "Failure to remedy within [N] days will result in immediate legal proceedings, including an application for injunctive relief."

5. **Inline alternative phrasings.** Where tone could shift, the draft includes a compact alternative. Format:
   > *The attached invoice of £X remains unpaid.* [or more assertive: *You have failed to pay the attached invoice of £X, due [date].*]

6. **No settlement discussion on the record unless intended.** If the intake flagged the communication as open (not without prejudice), the draft does not include any offer to compromise, any without-prejudice framing, or any language that could be characterised as a settlement communication.

7. **LPP markings per house style.** Apply `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` privilege conventions exactly.

## Output

### Primary: `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/[slug]/draft-v[N].docx`

Use the `docx` skill to produce a letter-formatted .docx:
- Letterhead / sender address block
- Date
- Recipient address block
- Re: line (concise; does not reveal privileged strategy)
- Salutation
- Body (per template + drafting rules)
- Closing
- Signature block per intake

### In-chat review

Show the draft as readable plain text for the user to review and request edits. Iterate before writing the final .docx. Once approved, write to disk.

### Send gate (closing note on the draft)

Append the following, set apart from the body, to the in-chat presentation and to any internal preview — it is a reviewer-facing note, not letter text, and is stripped before the letter goes out:

> This is a draft Letter Before Action / Letter of Claim for solicitor/barrister review, not a letter ready to send. Sending it may start the clock on limitation periods, trigger CPR pre-action protocol obligations, and create without-prejudice / without-prejudice-save-as-to-costs implications. A licensed solicitor or barrister reviews, edits, and takes professional responsibility before sending. Do not send this draft unreviewed.

### Citation verification

Every `[CITE:___]` placeholder — and any citation pulled from the intake or the seed doc — is unverified until a human runs it through a research tool. Before sending, run a verification pass: check each case, statute, and regulation against the uk-legal MCP, BAILII, or legislation.gov.uk for accuracy, good-law status, and whether the provision is still in force. Fabricated or misquoted citations in sent Letters Before Action have consequences for the sender's credibility and, if proceedings follow, for the claim.

**Source attribution.** Tag every citation in the draft with where it came from: `[uk-legal MCP]`, `[BAILII]`, `[legislation.gov.uk]`, `[gov.uk]`, or the specific MCP tool name for citations retrieved via a legal research connector; `[web search — verify]` for citations surfaced by web search; `[model knowledge — verify]` for citations the model recalled from training data; `[user provided]` for citations supplied in the intake or seed doc. Citations tagged `verify` carry higher fabrication risk and should be checked first.

**No silent supplement.** If a research query to the configured legal research tool returns few or no results for an authority the draft needs, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [issue]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]`, or (4) leave the `[CITE:___]` placeholder and stop here. Which would you like?"

### `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/[slug]/checklist.md` — the post-send checklist

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`. This header applies to the internal checklist file; the outgoing letter does NOT carry it.]

# Post-Send Checklist — [slug]

**Draft version sent:** [v1 / v2 / etc.]
**Sent date:** [YYYY-MM-DD — filled in after send]
**Signer:** [name]

## Pre-send (before the letter goes out)

- [ ] Final read-through by signer
- [ ] Factual accuracy: all [VERIFY] flags resolved
- [ ] Citations: all [CITE] placeholders filled and verified against uk-legal MCP / BAILII / legislation.gov.uk
- [ ] Applicable CPR pre-action protocol: content and timing requirements met
- [ ] LPP markings applied per house style — note: this is an external deliverable; do not include the `PRIVILEGED & CONFIDENTIAL — LEGAL PROFESSIONAL PRIVILEGE` header in the version sent to the counterparty
- [ ] Without-prejudice markers [present / absent] as intake specified, and substance aligns with posture
- [ ] Internal copies cleared (per intake distribution list)
- [ ] Insurance tender sent (if required per house practice)
- [ ] Conflicts confirmed (if not yet cleared)

**Before the letter is sent (the consequential act):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Sending this Letter Before Action has legal consequences — it creates a record, can trigger limitation periods and counterclaims, and may waive legal professional privilege or constitute admissions. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty and dispute, the demand and deadline, tone posture, without-prejudice status, privilege and admission risks flagged in the pre-draft gate, what could go wrong, what to ask the solicitor/barrister before sending.]
>
> If you need to find a licensed solicitor, barrister, or other authorised legal professional: the SRA (solicitors.lawsociety.org.uk) or Bar Standards Board (barstandardsboard.org.uk/find-a-barrister) for England & Wales; the Law Society of Scotland (lawscot.org.uk) for Scotland; the Law Society of Northern Ireland (lawsoc-ni.org) for Northern Ireland.

Do not mark as sent — do not execute the Send mechanics below — without an explicit yes.

## Send mechanics

- [ ] Delivery method executed: [recorded post / email / both]
- [ ] Proof of delivery retained (proof of posting, email read-receipt, courier confirmation)
- [ ] Copies sent per distribution list

## After send

- [ ] Compliance deadline calendared: [YYYY-MM-DD]
- [ ] Escalation plan if no response: [next step + date]
- [ ] Follow-up check-in calendared: [date — typically deadline + 2 business days]
- [ ] Matter created in `_log.yaml`: [yes / no — see materiality below]

## Materiality call

**Heuristic says:** [material / immaterial]
**Reason:** [demand type / exposure / counterparty type]
**Your call:** [material → create matter] [immaterial → demand-letters record only]

If material: `/litigation-legal-uk:matter-intake` with `source: letter-before-action` pre-populated from this intake.
```

### Matter auto-creation offer

After drafting and writing the checklist, assess materiality per heuristic:

- **Default yes if ANY of:**
  - Demand type is `cease-desist`, `breach-cure`, `employment-separation`, or `preservation`
  - Desired outcome ≥ `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` medium-severity band
  - Counterparty is a customer, competitor, or frequent adversary per landscape
- **Default no otherwise**

Present the call:
> Materiality heuristic: [result]. [One-sentence reason.]
> Create a tracked matter in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml`? (default: [yes/no])

If user accepts: trigger `matter-intake` with fields pre-populated from the intake (counterparty, type, jurisdiction, `source: letter-before-action`, initial theory, internal stakeholders). User reviews pre-filled fields and confirms.

If user declines: update intake `status: drafted` (later `sent` when user confirms). The record stays in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/demand-letters/` only.

## Versioning

Never overwrite a draft that has been sent. If revising after send, `draft-v2.docx`. The sent-version history is itself the record of what the counterparty received.

## What this skill does not do

- **Send the letter.** Drafting only. The user sends.
- **Research citations.** `[CITE:___]` placeholders stay as placeholders. If the user provided authorities in the intake, they're used; otherwise, blanks. Inventing cites is a professional responsibility risk.
- **Bypass the pre-draft gate.** Even with `--skip-gate`, the skill notes in the draft file that the gate was skipped and why.
- **Rewrite the intake.** If the intake is thin, send the user back to `demand-intake`. The draft is only as good as what it reads from.
- **Decide materiality.** The heuristic offers a default; the user's call is the record.
- **Verify CPR pre-action protocol compliance.** It checks the intake for the named protocol and flags gaps, but confirming compliance is for the signing solicitor/barrister.
