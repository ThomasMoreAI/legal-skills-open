---
name: privilege-log-review-uk-agents
title: /privilege-log-review
description: First-pass privilege log review — make the obvious LPP calls and flag the hard ones for solicitor/barrister review without making close calls. Use when the user says "review the privilege log", "priv log", "check privilege on these docs", or has a log to QA before production.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/privilege-log-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /privilege-log-review

1. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → review protocol, privilege log format.
2. Follow the workflow and reference below.
3. For each entry: obvious LPP / obvious not LPP / needs solicitor/barrister review. Flag reasons.
4. Output: reviewed log with flags. Solicitor/barrister reviews all flags before production.

---

# Privilege Log Review

## Disclosed-document use restrictions

Before working with a set of litigation documents, ask: "Were any of these documents obtained through disclosure in legal proceedings?" If yes:

- **England & Wales (CPR 31.22):** Documents obtained through disclosure are subject to the implied undertaking — you may only use them for the purpose of the proceedings in which they were disclosed, unless the court grants permission, the disclosing party consents, or the document has been read in open court. Using them for a different matter, a different claim, or a commercial purpose without permission is a contempt.
- **Scotland:** Equivalent undertaking principles apply. Confirm with Scottish solicitors.
- **Other jurisdictions:** Similar restrictions commonly apply. Check the local rule.

Confirm: "This use is within the proceedings in which the documents were disclosed, or I have permission / consent, or the documents are now public." If not confirmed, flag it: "⚠️ Disclosed documents may have use restrictions. Confirm this use is permitted before proceeding."

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (you work one case at a time), skip the rest of this paragraph and use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A privilege log has three kinds of entries: obviously LPP-protected, obviously not, and the ones that need thought. This skill sorts the first two kinds so the solicitor's or barrister's time goes entirely to the third.

**This is first pass. Solicitor/barrister reviews every flag. No exceptions.**

## Record fidelity — pinpoints and citation coverage

When this skill cites a rule, local variant, or authority for a privilege call (CPR 31, PD 31A, case on waiver scope, case on dominant purpose), two rules apply.

**Pinpoint cites must support the whole proposition.** If the review cites one rule or case to support a multi-part proposition — "the log must describe each document and withhold only materials subject to legal professional privilege" — verify the pinpoint covers every element. If it only covers one, split the cite or narrow the proposition. A cite that backs part of a privilege position gets the position rejected when opposing solicitors read the cite and point out it does not reach the contested element.

**Extract all citations before checking any.** When this review cites authority — or when a separate citation-check is requested on the log, a related skeleton argument, or the supporting application:

1. **First pass: extract.** Read the document and build a list of every citation (rules, cases, statutes, practice directions, record cites). Report the count: "Found [N] citations."
2. **Second pass: check.** Check each against the source. Don't sample. Don't stop at the first five.
3. **Report coverage.** "Checked [N] of [M] citations. [K] could not be retrieved — verify manually. [J] confirmed. [I] flagged as potential miscitations. [H] flagged as misgrounded (cite exists but doesn't support the proposition)."
4. **When source text is unavailable, say "could not check," never "confirmed."**
5. **The hardest errors are partial support.** Read the proposition, read the source, compare element by element.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → privilege log format, review protocol.

**Conflicts gate — unbypassable.** Before reviewing a privilege log, check `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal-uk:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't review a privilege log on a matter that hasn't been intaken — the conflicts check is the gate, and a privilege log review is work product that needs to live in the matter file."

**Jurisdiction matters.** Legal professional privilege (LPP) scope, waiver doctrine, and log-form requirements vary across England & Wales, Scotland, and Northern Ireland, as well as across different UK courts (High Court, Chancery, CAT, Employment Tribunal, etc.). This review applies the rules for the forum specified in the configuration. If the matter involves a different forum, a transferred case, multi-jurisdictional production, or a choice-of-law question on privilege, the calls here may not transfer — re-run against the controlling forum.

**EU competition / regulatory matters.** Under *Akzo Nobel Chemicals and Akcros Chemicals v European Commission* (C-550/07 P) `[model knowledge — verify]`, in-house counsel communications are NOT privileged in EU competition proceedings before the European Commission. Similarly, CMA investigation powers may reach in-house counsel communications in certain contexts. Flag any matter involving the CMA, FCA, or a European regulatory body for specialist review — in-house documents that appear clearly privileged under UK civil procedure may not be protected in those regulatory contexts.

## Step 0: Research the forum's privilege-log rules

**Before reviewing entries, research the forum's privilege-log requirements (CPR 31.10, Practice Direction 31A, or the tribunal-specific equivalent), any applicable court guide provisions, and the judge's directions. Identify the required fields, the level of description, and any category-log or metadata-log accommodations. Cite primary sources in OSCOLA format.**

**No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, BAILII, legislation.gov.uk, or firm platform) returns few or no results for the forum's rule, waiver doctrine, or local variant, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / doctrine]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) leave the `[UNCERTAIN]` marker and stop here. Which would you like?" A solicitor or barrister decides whether to accept lower-confidence sources; the skill does not decide for them.

**Source attribution.** Tag every rule reference and authority in the review output with where it came from: `[uk-legal MCP]`, `[BAILII]`, `[legislation.gov.uk]`, `[gov.uk]` for citations retrieved in this session; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the reviewing solicitor supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

**UK LPP has two limbs — distinguish them:**

- **Legal advice privilege (LAP):** protects confidential communications between a lawyer (external or in-house, acting in a legal capacity) and client for the dominant purpose of giving or receiving legal advice. Does not require proceedings to be in contemplation. Waiver: generally broad subject-matter waiver when LAP is waived — sweeps related communications on the same subject.
- **Litigation privilege (LP):** protects documents created when adversarial proceedings are reasonably in contemplation, for the dominant purpose of those proceedings. Extends to communications with third parties (e.g., experts, witnesses). Narrower waiver doctrine than LAP — waiving LP over one document does not automatically waive LP over unrelated documents. LP does NOT protect the underlying facts.

Confirm which limb is claimed for each entry. Both may apply to the same document. The description must be sufficient to enable the court to assess the claim without seeing the document — vague descriptions invite in camera review.

**In-house counsel LPP — strictly applied.** Communications with in-house lawyers attract LPP only when the lawyer is acting in a legal (not commercial or business) capacity, and the dominant purpose of the communication is legal advice or litigation. The dual-capacity problem (in-house lawyers often act as both lawyer and businessperson) means the dominant-purpose test is strictly applied by English courts. Flag any in-house communication where the legal vs. business capacity distinction is not immediately clear.

## The calls

**Three-state rule. The skill never silently decides a subjective threshold is not met.** On any uncertain call — dominant purpose unclear, litigation contemplation borderline, mixed legal/business content, ambiguous third-party presence — the skill keeps the privilege designation on and adds a ⚠️ flag for the solicitor or barrister. Under-marking waives LPP (one-way door); over-marking is corrected by counsel in review (two-way door). Prefer the recoverable error.

### Confidently privileged (✅) — keep designation, no flag

- Communication between client and external solicitors or barristers seeking/providing legal advice, no third parties outside the privilege circle copied
- Communication between client and in-house solicitor, clearly in a legal (not business) capacity, no third parties
- Documents created for the dominant purpose of adversarial litigation reasonably in contemplation, by or for a solicitor or barrister
- Communications within the privilege circle about legal strategy

### Uncertain — keep designation AND flag (✅ + ⚠️)

The default for anything that is not confidently in ✅ or ❌. The skill does not withhold a privilege designation on its own assessment of a subjective test. Examples:

- **In-house counsel doing both legal and business** — was this communication legal advice or business advice? The dominant-purpose call is the solicitor's/barrister's, not the skill's.
- **Third party present** — is the third party within the privilege circle (common interest, agent) or does their presence waive? Keep the designation; flag for counsel.
- **Mixed purpose documents** — part legal, part business. Partial redaction? Full withhold? Produce? Keep the designation; flag for counsel to decide the treatment.
- **Attachments** — analyse separately and keep each attachment's designation unless confidently ❌; flag the ones where privilege turns on a subjective call.
- **Pre-litigation documents** — "reasonable contemplation of litigation" is fact-specific; keep the designation; flag.
- **Expert communications** — only protected by litigation privilege if created when proceedings were in contemplation for the dominant purpose of those proceedings; flag if this test is not clearly satisfied.
- **Waiver risk** — later-sharing history is ambiguous; keep the designation; flag the waiver question.
- **Regulatory context** — if the matter involves the CMA, FCA, European Commission, or another body with potentially different privilege rules: flag every in-house counsel document for specialist review. There is no ✅ tier for in-house documents in regulatory proceedings without that specialist review.

Each flag records the specific open question and the evidence cutting each way, so the solicitor or barrister can decide without re-reading the document cold.

### Confidently not privileged (❌) — recommend remove, but note the assessment

Only for the unambiguous cases. The output still records the assessment rationale so the solicitor can spot-check; it does not remove the designation from the log on its own.

- No solicitor or barrister involved anywhere
- Business advice with a lawyer CC'd (CC'ing legal does not make it privileged)
- The underlying facts (facts are not privileged — communications *about* facts for a legal purpose may be)
- Third party copied who is clearly outside privilege (breaks confidentiality)
- Attachments that are independently non-privileged (the email may be privileged; the attached product specification is not)

If any of these is *close* — the third party might be an agent, the lawyer's CC might actually be on a legal request — it is uncertain, not ❌. Route it to the uncertain bucket and flag.

## Workflow

### Step 1: Format check

Does the log have what it needs?

| Field | Present? |
|---|---|
| Date | |
| Author | |
| Recipients (all — TO, CC, BCC) | |
| Document type | |
| LPP limb claimed (legal advice privilege / litigation privilege / both) | |
| Description (enough to assess without revealing privileged content) | |

Missing fields → flag for completion before substantive review.

### Step 2: Entry-by-entry

For each entry:

```
Entry [N] ([document ref / Bates]): [✅ LPP | ✅ LPP + ⚠️ Flag | ❌ Not LPP (assessed)]
[If ✅ (no flag): one-line reason, LPP limb identified]
[If ✅ + ⚠️: keep designation; the specific question the solicitor/barrister needs to answer; evidence cutting each way]
[If ❌: one-line reason — but the designation stays on the log until the solicitor removes it]
```

**Never produce an entry that silently strips a privilege designation based on the skill's own subjective call.** A ❌ is a recommendation logged alongside the flag; the solicitor or barrister acts on it.

### Step 3: Pattern flags

Across the log:

- Same issue repeating? (E.g., same third party on 50 entries — one decision resolves 50 flags)
- Over-designation pattern? (If everything is designated without differentiation, surface it for the solicitor — but the call to narrow the log is the solicitor's/barrister's, not the skill's. Under-designation waives; over-designation is correctable.)
- Under-description? (Descriptions so vague a court would order in camera review or a solicitor's summons to justify the claim)
- Regulatory-matter flagging? (If the matter has a regulatory dimension, flag the in-house counsel documents for specialist review rather than ✅-ing them)

## Output

**Before the privilege log is served on the opposing party (the consequential act — this includes serving the log AND designating documents withheld or produced under a protective-order designation):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Submitting a privilege log and designating documents in disclosure both have legal consequences — over-designation risks costs sanctions and loss of credibility; under-designation risks waiver of LPP; a misdesignated production may be unrecallable. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the matter, log entry counts, the ⚠️ flags and close calls, pattern observations (over-designation, vague descriptions), LPP limb by limb waiver-doctrine posture, what could go wrong on service or designation, what to ask the solicitor/barrister.]
>
> If you need to find a licensed solicitor, barrister, or other authorised legal professional: the SRA (solicitors.lawsociety.org.uk) or Bar Standards Board (barstandardsboard.org.uk/find-a-barrister) for England & Wales; the Law Society of Scotland (lawscot.org.uk) for Scotland; the Law Society of Northern Ireland (lawsoc-ni.org) for Northern Ireland.

Do not treat the log as service-ready without an explicit yes. First-pass review, sorting, and flagging do not require the gate — service and designation do.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Privilege Log Review: [Matter] — [date]

**Applicable rule:** [CPR 31.10 / PD 31A / tribunal rule / standing direction — pinpoint cites] `[UNCERTAIN — verify currency]`
**LPP limbs in issue:** [legal advice privilege / litigation privilege / both]
**Entries reviewed:** [N]
**Results:** [N] ✅ confident LPP / [N] ✅+⚠️ LPP kept & flagged / [N] ❌ recommend remove (solicitor/barrister confirms)

### ✅ + ⚠️ Flagged — designation kept, solicitor/barrister decides

| Entry | Doc ref | Issue | Evidence for LPP | Evidence against | Question |
|---|---|---|---|---|---|
| [N] | [ref] | [what's subjective] | [one line] | [one line] | [the specific call to make] |

### ❌ Recommend remove designation (solicitor/barrister confirms before stripping)

| Entry | Doc ref | Reason |
|---|---|---|

*Recorded, not executed. The skill does not remove LPP designations from the log — the solicitor or barrister does, after reviewing the rationale.*

### ✅ Privileged (no action)

[Count. List available on request.]

### Pattern observations

[Repeating issues, over-designation, description problems, regulatory-context flags]

### Marker discipline

- `[VERIFY: factual assertion about document/custodian/date]`
- `[UNCERTAIN: close LPP call / waiver scope / doctrine question]`
- `[CITE NEEDED: rule, court guide provision, or authority supporting a call]`
- `[LPP]` — legal professional privilege flag requiring qualified solicitor/barrister assessment

---

**Solicitor/barrister must review all ⚠️ and ❌ before any action.**

**Privileged source material.** This review reads entries and underlying documents that are, by definition, LPP-candidate material. The review output inherits that status — keep it with privileged materials, mark it appropriately, and do not circulate outside the LPP circle. Distributing it can itself waive protection.
```

## What this skill emphatically does not do

- Make close calls. ⚠️ means "a solicitor or barrister decides." On any subjective test (dominant purpose, reasonable contemplation, common-interest scope, waiver by later sharing) the skill keeps the privilege designation on and flags.
- Strip a privilege designation from the log based on its own assessment. ❌ is a *recommendation* recorded for the solicitor/barrister, not an action taken against the log.
- Produce or withhold documents. It advises; solicitor/barrister decides; solicitor/barrister acts.
- Guarantee correctness on ✅ calls. The solicitor/barrister is responsible for the log. This is a first pass.
- Make calls on in-house documents in regulatory proceedings without flagging for specialist review.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the solicitor or barrister picks.
