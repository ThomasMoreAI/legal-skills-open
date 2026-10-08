---
name: cold-start-interview-lawdroidai
title: /cold-start-interview
description: Managing attorney's one-time office setup — practice areas, funding sources and eligibility guidelines, jurisdiction, supervision style (formal review queue / configurable flags / lighter-touch), conflict-check process, and seed documents (handbook, filing guides, eligibility tables, intake forms). Writes CLAUDE.md so every other skill and every staffer who runs /onboard reads from the same office context. Use on fresh install, when CLAUDE.md has placeholders, when re-doing setup with --redo, or when re-checking integrations with --check-integrations.
author: lawdroidAI
author_url: https://github.com/lawdroidAI/legal-aid-plugin/tree/main/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md`. If populated and no `--redo`, confirm before overwriting.
2. Run the managing-attorney interview below, starting with Part 0 (role check → ethical preconditions → funder restrictions → integration availability). If the user isn't the managing attorney or ED, stop and redirect.
3. Seed docs: office procedures manual, filing guides, local court rules, intake form(s), eligibility tables, conflict-check procedure, one scrubbed example case file, sample LSC/funder report if applicable.
4. Key decisions: funding-source matrix, supervision style (formal queue / flags / lighter-touch), escalation posture (handle / escalate / refer).
5. Migration: if a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/claude-for-legal/legal-aid/*/CLAUDE.md` but not at the config path, copy it to the config path and show the user what was migrated.
6. Write `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` including `## Who's using this`, `## Available integrations`, and `## Eligibility guidelines`. Show supervision choice and practice-area templates for confirmation.
7. Offer `/legal-aid:onboard` preview and a first run of `/legal-aid:eligibility-screening`.

```
/legal-aid:cold-start-interview
```

**`--check-integrations`:** Re-run only the Part 0 integration-availability check (case management system, document storage, any provider-specific intake-routing or procedural-retrieval connectors the office has licensed). Updates `## Available integrations` in `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` without touching role, ethical preconditions, funding sources, supervision style, or practice-area templates. Use after adding or removing an MCP connector.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to. Never report ✓ based on `.mcp.json` declarations alone — that misleads users into thinking something is wired up when it isn't.

---

# Cold-Start Interview: Civil Legal Aid Office

## Purpose

Civil legal aid offices are structurally capacity-constrained. A managing attorney supervises 5-20 staff, each carrying 40-80 active matters, with intake volume routinely 3x to 5x capacity. Eligibility screening, intake write-up, first drafts, status updates, referral letters, court self-help triage — the administrative load consumes hours that could go to advising clients. The waitlist grows. People give up waiting.

This plugin's job is to cut the time cost of everything *around* the lawyering — eligibility screening, intake write-up, first drafts, research starting points, status updates, funder reporting — so the same staff and managing attorney serve more clients, and staff spend more time on the analysis and strategy that actually moves cases.

This interview sets up the office context once, so every staffer who onboards via `/onboard` and every skill that runs afterward is working from the same understanding of how *this* office operates, *which funders' rules apply* to which matters, and *what the eligibility shape* looks like.

**Audience: the managing attorney or ED.** Staff don't run this — they run `/onboard`.

## Cold-start check

Read `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

## Check for the shared company profile

Look for `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [role], at [office], [type — e.g., LSC-funded legal services], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the office-level questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation, ask the office questions and write them to the shared profile (per the template at `references/company-profile-template.md` in the plugin root), then continue with the plugin-specific questions. Tell the user: "I've saved your office profile — the other legal plugins will read it and skip these questions."

Office-level facts that belong in the shared profile (and should NOT be re-asked if it exists): office name, type (LSC / non-LSC civil legal aid / hybrid / court self-help / public defender civil), jurisdictions served, headline practice areas, size (attorneys + paralegals + intake), key people. Plugin-specific facts that stay per-plugin: funding-source matrix, eligibility guidelines, conflict-check process, supervision model, escalation posture, practice-area templates, funder reporting cadence.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it. Say once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, your case management system's export folder), install user-scoped instead — see QUICKSTART.md. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding. If the working directory *is* the user's home directory, skip this check silently.

## Before the interview starts

Show this preamble first (3-4 short lines, nothing more):

> **`legal-aid` is for managing attorneys setting up a civil legal aid office, court self-help center, or public-interest legal services provider.** Law school clinic? `/legal-clinic:cold-start-interview`. Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **3 minutes** gets you practice area(s), jurisdiction, primary funding source, and supervision model basics — plus working defaults for client-letter format, IRAC scaffolding, and deadline cadence. **20 minutes** adds your full funding-source matrix, eligibility guidelines per funder, ethical-preconditions record, supervision flag triggers, per-practice-area document templates, office procedures manual feeding `/onboard`, local court rules feeding `/draft`, conflict-check procedure, and funder reporting cadence.
>
> Quick or full? (Upgrade any time with `/cold-start-interview --full`.)

## After the user picks quick or full

Once the managing attorney has picked, orient them. Cover, in your own voice:

- **What this plugin maintains:** your office profile (practice areas, funding sources and eligibility, supervision model, house templates), per-case files (eligibility screening, intake, deadlines, comms log, transfer memos), and a managing-attorney review queue.
- **What this setup does:** supports a civil legal aid office or court self-help program — eligibility screening, intake, case memos, client letters, status updates, deadlines, funder reporting — across your practice areas, with supervision and funder-restriction awareness built in. Learns the office's funding sources, eligibility shape, jurisdictions, and supervision model, and writes them into a plain-text file every skill reads from and every staffer's `/onboard` reads from. Everything can be changed later. Once it's done, the commands will work the way the office actually operates, not the way a generic template does.
- **Data sources:** setup builds a fresh office profile from the managing attorney's answers and from documents uploaded during the interview (procedures manual, filing guides, local rules, intake forms, eligibility tables, conflict-check procedure, sample funder report, scrubbed example case file). It does not read personal Claude history, other conversations, or the home-directory CLAUDE.md. If something relevant came up earlier in this conversation, ask before folding it in. Nothing gets added to configuration unless the managing attorney types or approves it.
- **Next up:** Part 0 — who's running the setup, the ethical preconditions, and funder restrictions.

**Why this matters.** Every `/onboard`, every `/eligibility-screening`, every `/client-intake`, every `/draft`, every `/client-letter`, every `/status`, and every `/lsc-report` reads from the configuration this interview writes. A generic configuration gives staff generic output — a one-size income standard that ignores your IOLTA carve-outs, default supervision flags that don't match your office's actual review triggers, generic client-letter tone — and the first month of new-staffer onboarding is spent correcting what the tool assumed about the office. Telling the plugin the funding-source matrix, eligibility guidelines, supervision style, and local formatting is what makes the difference between "a legal aid AI tool" and "a tool that runs the way your office runs." The more specific the answers, the less new staff have to unlearn.

### Quick start or full setup — branching

The managing attorney picked quick or full in the preamble. Branch:

**Quick start path:** ask only the basics (practice areas, jurisdiction, primary funding source, supervision style). Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for client-letter format, IRAC scaffolding, deadline cadence, and a single-funding-source eligibility shape (the one you named). When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/legal-aid:cold-start-interview --full` anytime to do the whole interview, or `/legal-aid:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — eligibility table, procedures manual, conflict-check SOP, intake script, sample motion, sample funder report — prompt for a link or a paste before asking the user to type it from memory. "Paste a link or a doc, or give me the short version" is the default ask for anything that's more than a sentence. An interviewer who makes people re-type what they've already written has failed the first job of an interviewer.

**Pause for real answers.** Part 0 has tap-through role and integration checks. The ethical preconditions, funder restrictions, eligibility guidelines, and the seed-documents pass need the managing attorney to type out answers or upload files. When a question needs more than a quick tap:

- **Ask the question and wait.** Say explicitly: "This one needs a typed answer — I'll wait." Do not move to the next question until the managing attorney responds.
- **For uploads (procedures manual, filing guides, eligibility tables, conflict-check SOP, intake forms, sample motions, sample client letters, sample funder reports):** "Paste the contents, share a file path, or say 'skip for now.' If you skip, I'll flag the gap in the practice profile so you can fill it later — and I'll note what that means for `/onboard`, `/eligibility-screening`, `/draft`, and `/lsc-report` (they'll be thinner or fall back to defaults)." Then actually wait.
- **Before writing the practice profile:** review the interview. List every question that was skipped or answered with a placeholder — ethical preconditions still open, funding sources without eligibility tables, practice areas without templates, supervision-flag triggers not set, conflict-check procedure promised but not uploaded. Say: "Before I write your practice profile, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?" Then wait.
- **Never** write a practice profile with silent gaps. Every placeholder should be a deliberate choice the managing attorney made to skip — not a question that scrolled past.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts. One question with 5 subparts is 5 questions. The test: can the user answer without scrolling? Prefer structured tap-through questions where possible.
- **Pause and resume.** Tell the managing attorney up front: "If you need to stop, say 'pause' (or 'stop', or 'let me come back to this') and I'll save your progress. Run `/legal-aid:cold-start-interview` again later and I'll pick up where you left off." When the managing attorney pauses, write a partial configuration to `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` with a `<!-- SETUP PAUSED AT: [section name] — run /legal-aid:cold-start-interview to resume -->` comment at the top and `[PENDING]` markers (distinct from `[PLACEHOLDER]`) on unanswered fields. When setup re-runs and finds a paused config, greet the managing attorney: "Welcome back. You paused at [section]. Your earlier answers are saved. Pick up where we left off, or start over?" Do not re-ask questions already answered.

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute number, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration. If what they said conflicts with your understanding or with something they've pasted, surface it: "You said the threshold is X; my understanding is Y — can you confirm which goes in the profile? `[premise flagged — verify]`" A wrong fact written into CLAUDE.md propagates into every future output; catching it here is one of the highest-leverage moments in the product.

**Do not assert current FPL numbers or current LSC regulation text from memory.** Income thresholds, asset caps, and citizenship-restriction details change. When the managing attorney describes their eligibility guidelines, capture them in the profile *as the managing attorney states them*, and tag the entry with the date of the conversation and the source the managing attorney pointed to (LSC poverty guidelines table, state IOLTA rules, foundation-specific letter, internal eligibility memo). `/eligibility-screening` re-reads these at runtime and tags `[VERIFY: current FPL table]` against every income comparison.

## The interview

### Part 0: Who's running this setup, ethical preconditions, funder restrictions, and what's connected (before anything else)

#### Who's running this setup?

> Are you the managing attorney or ED of this office? You need to be licensed in your jurisdiction and authorized by the office to make supervision and intake-policy decisions for this setup to be valid. (This feeds Part 0's role gate — setup can only be run by the managing attorney or ED, and the answer writes the supervising-attorney name and bar details into the profile that every skill references.)
>
> 1. **Yes, I'm the managing attorney or ED.** Continue.
> 2. **No, I'm a staff attorney / paralegal / intake specialist / administrator.** Stop. This setup writes the office's governing context — supervision model, eligibility shape, funder restrictions, client-data rules, ethical preconditions — and must be done by the person who will be accountable for it. Ask them to run `/legal-aid:cold-start-interview`. Staff run `/legal-aid:onboard` to come up to speed.

If the answer is 2, stop the interview and surface the above. Do not proceed.

If the answer is 1, record it in the plugin config under `## Who's using this` (Role: Managing attorney / ED; name and jurisdiction captured) and continue.

*Why this matters:* the office runs under supervision rules that require a licensed attorney with authority over staff work. Cold-start decisions — supervision model, eligibility, funder restrictions, ethical preconditions — are the managing attorney's call. The role question gates those decisions to the right person.

#### Ethical & confidentiality preconditions

Before the managing-attorney interview starts — and before any staffer uses this plugin on a real client matter — confirm the following with the office's compliance lead and IT. Do not skip this step.

1. **Account tier and data-handling terms.** Your Claude account tier and its data retention and training policies — Team, Enterprise, Work, and individual accounts have different guarantees about retention, use for training, and subprocessor handling. Confirm which tier the office is on and what the applicable terms say about client data, *and* confirm those terms satisfy your funders' data-handling requirements (LSC, HUD, VAWA, state IOLTA, specific foundation grants). Document the answer in the plugin config.

2. **Client consent and disclosure practices for AI-assisted work.** Review ABA Formal Opinion 512 (2024), your state bar's AI guidance (if any), and Model Rules of Professional Conduct 1.1 (competence), 1.4 (communication), 1.6 (confidentiality), and 5.3 (supervision of nonlawyer assistance). Decide whether and how the office discloses AI use to clients, and document the practice.

3. **How privileged and confidential material is handled.** What gets pasted into sessions, where outputs are stored, who has access, how long material is retained locally, how staff turnover affects access. Document the data-handling rules the office expects staff to follow. Civil legal aid practice has Rule 1.18 prospective-client duties as well — eligibility screening creates 1.18 obligations whether the office takes the matter or not, and `/eligibility-screening` output carries that confidentiality.

4. **Practice-area heightened-confidentiality considerations.** Immigration, domestic violence, family, and some civil rights and elder matters carry heightened confidentiality and security expectations that go beyond the baseline — adversary exposure risk, subpoena risk, safety risk for survivors. Confirm whether any practice area requires additional safeguards (limiting what facts are put into sessions, additional redaction, not using the plugin for a given case type at all).

Capture the managing attorney's answers. If any precondition is unresolved, flag that in the plugin config and note that staff should not use the plugin on real client matters until resolved.

#### Funder restrictions

> Civil legal aid often operates under one or more funder-specific restrictions — most commonly the LSC restrictions in 45 CFR Part 1600 (class actions, fee-generating cases, certain alien populations, lobbying, abortion, prisoner litigation, redistricting), but also HUD-specific rules, VAWA confidentiality requirements, foundation-specific scope, and state-specific carve-outs. The plugin does not enforce these rules. Your office does.
>
> Which funders' restrictions apply to your office, and have your staff been briefed on them? (This feeds the `[FUNDING RESTRICTION: ...]` flag that `/eligibility-screening`, `/draft`, and other skills raise when a contemplated action plausibly engages a funder rule.)

Ask:
- Which funders apply to this office? (LSC / IOLTA / HUD / VAWA / VOCA / state appropriation / specific foundations / private / mixed)
- For each, does the office maintain a written summary of the restrictions and exceptions, and have staff been briefed? (Yes / partial / no — paste a link or upload if you have one)
- Are there matters where the office runs *both* LSC and non-LSC funds and tracks them separately? (Common: the office is LSC-funded for most work but uses IOLTA for matters LSC restrictions would block.)

Capture the answers. Tag every `[FUNDING RESTRICTION: ...]` reference in downstream skill output against the funder named here.

#### What's connected?

> This plugin can work with a case management system (Legal Server, LegalFiles, Clio, PIKA, JusticeServer, etc.), document storage (Google Drive, SharePoint, Box), and any intake-triage or procedural-retrieval MCP your office has licensed (provider-specific — not bundled with this plugin). Let me check which connectors are configured — features that need them will work, and features that don't have them will fall back to manual gracefully instead of failing silently.

**Check what's actually connected, not what's configured.** A connector listed in `.mcp.json` is *available*. A connector that's actually responding is *connected*. These are different, and confusing them destroys trust. For each connector this plugin uses:

- If you can test the connection (call a simple MCP tool like a list or search), report ✓ only on a successful response.
- If you can't test (no way to probe from here), report ⚪ "configured but not verified — open your MCP settings to confirm" with a one-line how-to.
- Never report ✓ based on configuration alone.

For connectors that show as not connected, tell the user how to connect. Example phrasing: "Legal Server isn't connected. In Claude Cowork: Settings → Connectors → Add → Legal Server → sign in. In Claude Code: add the Legal Server MCP to your config or via `/mcp`. This plugin works without it — you'll paste case data instead of pulling it — but connecting it makes eligibility screening and conflict checks faster and lets `/lsc-report` extract case-management data directly."

Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

You don't need all of these. Core features — eligibility screening, intake, draft, client letter, research-start, deadlines, case transfer, managing-attorney review — work with local file access alone.

Write Part 0 answers to the plugin config under `## Who's using this`, `## Available integrations`, and `## Funder restrictions`. If a populated CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/claude-for-legal/legal-aid/*/CLAUDE.md` but not here, copy it forward first.

### Opening

> This is the one-time setup for your office. Fifteen to twenty minutes. I'll ask about your practice areas, jurisdiction, funding sources and the eligibility shape that goes with them, how you supervise, your conflict-check process, and then I'll ask you to point me at your procedures manual and any filing guides, eligibility tables, intake forms, or local court rules you give staff. Everything I learn here feeds the `/onboard` flow staff will run when they join the office, and every other command in this plugin.
>
> None of this replaces your judgment or your staff's analysis. The goal is to cut the hours spent on screening, intake write-up, formatting, and reporting — so more of your team's time goes to the lawyering, and more clients get served.
>
> I'll ask for materials along the way — procedures manual, filing guides, eligibility tables, conflict-check SOP, intake forms, local rules, sample motions, sample client letters, sample funder reports. Ten to twenty documents across the interview is the target. More is better. If you share fewer than ten, I'll flag the practice profile as LIMITED DATA — the plugin still works, but `/onboard` is thinner (commands but not your office's specific procedures), `/eligibility-screening` uses generic funder defaults instead of your tables, `/draft` falls back to state defaults, and `/client-letter` uses generic templates. Templates-first: if you upload a document, I read it and match your format rather than asking you to describe it.

### Part 1: The office (2-3 min)

(Feeds `/onboard` orientation, `/eligibility-screening` routing, and `/client-intake` cross-practice issue spotting.)

- Office name and parent organization (if any).
- Type: LSC-funded legal services / non-LSC civil legal aid / hybrid / court self-help center / public defender civil division / pro bono coordinator office / other.
- Practice area(s): housing, family, consumer, immigration, public benefits, civil rights, elder, DV, other? (Can be multiple — many offices handle overlapping issues.)

   **Practices that don't fit the boxes.** If the office's practice doesn't match the options (medical-legal partnership, reentry, education advocacy, language access, indigenous law, refugee resettlement, holistic defense civil arm, or anything else), offer: "It sounds like your office doesn't fit my usual categories. Tell me about it in your own words — what the office does, who it serves, what jurisdictions and forums, what the work looks like — and I'll build your office profile from that instead of forcing it into boxes that don't fit. I'll skip or adapt the questions that don't apply." Then build the profile from the free-form description.
- Staff size: how many attorneys, paralegals, intake specialists?
- How many supervising attorneys (i.e., people who can sign off on staff work)?
- Typical annual intake volume?
- Typical active caseload per staff attorney?

**Who are the clients?**
- Typical client situations — who walks in, calls in, what are they facing?
- Languages spoken beyond English?
- Common referral sources (community orgs, courts, hotlines, social services)?
- Common referral destinations for declined matters (private bar referral, court self-help, lawyer-of-the-day, mediation, other legal aid orgs)?

### Part 2: Jurisdiction (1-2 min)

(Feeds `/draft`, `/research-start`, `/memo`, and `/deadlines` — jurisdiction determines filing formats, research scope, and default deadline calculations. Civil legal aid offices commonly cover multiple counties or the whole state, so capture this carefully.)

- State(s).
- Counties served (or "statewide" if applicable).
- Primary courts: which courts do cases land in most often? Are any specialty (housing court, family division, immigration, administrative tribunals)?
- Any local rules, standing orders, or local-rule supplements that diverge from state defaults? Upload if you have them.
- For court self-help variant: which court(s) does the self-help program serve, and what's the program's authority basis (court order, statute, AOC contract)?

### Part 2b: High-volume deadlines (optional, 1-3 min)

> One optional question while we're on jurisdiction: what are the high-volume civil deadlines your staff hit constantly?
>
> I'll record these in your practice profile and use them as a sanity check when staff enter deadlines via `/legal-aid:deadlines --add` — if a staffer enters a date way outside the typical range you specify, the skill flags it for re-check. **This is not a deadline-computation tool.** Your staff and managing attorney compute against the actual local rule; this section catches arithmetic errors and date-entry typos.
>
> Tell me each deadline type, the triggering event, the typical days-out, and the source/cite. Five to fifteen entries is the sweet spot — the ones staff see weekly. Some examples (you'll likely have different ones for your state and practice areas):
>
> - Eviction response — from service — [state-specific window] — [state code cite]
> - Protective order hearing — from petition filing — [state window] — [state code cite]
> - SSI/SSDI appeal — from denial notice — 60 days — 20 CFR § 416.1413
> - SNAP fair hearing — from action notice — [state window] — [state reg cite]
> - Asylum one-year filing — from most recent entry — ~1 year — 8 USC § 1158(a)(2)(B)
> - Consumer collection statute of limitations — [varies] — [your state cite(s)]
> - Small claims appeal — from notice of entry — [state window] — [cite]
>
> Want to add some, skip entirely, or upload a deadline cheat sheet you already give staff?

For each entry the managing attorney provides, capture:
- Deadline type (one-line name)
- Triggering event (what starts the clock — service, filing, notice, decision)
- Typical days-out (or a range — "14-21 days" is acceptable; "exactly 30 days" is acceptable)
- Source / authority cite (with `[VERIFY: cite — confirm current]` tag because statutes change)

If the managing attorney uploads a deadline cheat sheet, parse it into the table format and confirm before writing.

If the managing attorney skips: note in the profile that no plausibility ranges are configured, and `/legal-aid:deadlines --add` will not perform plausibility checks (it still tracks deadlines, warns at 14/7/3/1 days, surfaces overdue). The managing attorney can add ranges later by editing CLAUDE.md directly or running `/legal-aid:cold-start-interview --redo plausibility-bands`.

Write the captured ranges into the profile under `## High-volume deadlines`.

### Part 3: Funding sources and eligibility (4-6 min — this is the key legal-aid section)

> Eligibility screening is the front of the funnel and the most common reason a legal aid office runs into compliance trouble. Income, assets, residency, citizenship, conflicts, and funder-specific case-type rules all have to be cleared before the office takes on a matter, and the rules vary by funding source on the same matter. Let's capture the shape so `/eligibility-screening` can apply it.

For each funder named in Part 0, capture:

**Income standard:**
- What income standard does this funder use? (Common: 125% FPL for LSC, 200% FPL for IOLTA, 300% FPL or no cap for elderly/DV programs.) Where does the office track the current dollar table — is there a posted FPL chart with this year's numbers?
- Are there carve-outs by case type? (E.g., "No income test for DV matters under VAWA"; "Elderly clients eligible regardless of income for benefits matters.")
- How recently was this updated, and who's responsible for updating it?

**Asset rules:**
- Liquid asset cap (if any)?
- Excluded assets (typically primary residence and one vehicle — confirm)?
- Are there funder-specific asset variations?

**Residency:**
- State / county / venue rules per funder?
- Length-of-residence requirements (rare but exists in some grants)?

**Citizenship / immigration status policy:**
- For LSC-funded matters: does the office apply 45 CFR § 1626 with the standard exceptions (DV survivors, trafficking victims, certain visa categories), or has the office adopted a narrower or broader interpretation?
- For non-LSC matters: what's the office's policy?
- Does the office maintain a separate intake pathway for matters that would fail LSC restrictions but qualify under non-LSC funding?

**Priority case types per funder:**
- E.g., "Emergency eviction defense (within 5 days of writ)"; "DV protective orders"; "Benefits termination appeals"; "Consumer judgments with execution pending."

**Out-of-scope case types per funder:**
- E.g., "Class actions (LSC restricted)"; "Fee-generating cases (LSC restricted)"; "Criminal defense (out of mission)"; "Prisoner litigation (LSC restricted)."

**Conflict-check process:**
- Does the office run conflicts through a case management system, manually, or both?
- Who runs them (intake, supervising attorney, designated person)?
- What's the SOP? Upload if available.

> If you're under time pressure, the minimum is: one funder, its income standard, its citizenship policy, its priority and out-of-scope case types, and your conflict-check process. The rest can be added with `--redo eligibility`. But every funder you skip means `/eligibility-screening` defaults to the named funder's rules for matters that might actually qualify under one of the unmentioned funders.

Capture every answer in the practice profile under `## Eligibility guidelines`. Tag dollar figures with `[as stated [date]; verify against current source]`.

### Part 4: Supervision style (2-3 min)

> Offices vary a lot in how tightly staff work is reviewed before it goes out. Some want every filing and substantive advice letter in a formal review queue — staff submits, managing attorney approves, then it goes. Others are lighter-touch — case rounds, one-on-ones, file reviews. What's your model? (This feeds `/managing-attorney-review` and the flag-triggering logic across `/draft`, `/client-letter`, and `/status` — formal queue turns the review skill on; configurable flags only surface triggers; lighter-touch suppresses the queue.)

Three options to offer:

**Formal review queue:** Staff output that's client-facing or court-bound goes into a queue. Managing attorney reviews, approves or edits, then it releases. Every approval logged. (`managing-attorney-review` skill active.)

**Configurable flags, informal review:** Certain triggers (deadlines, sensitive topics, court filings, funding-restriction risk) flag the output with "CHECK WITH MANAGING ATTORNEY BEFORE SENDING" — but no formal queue mechanism. Staff responsible for checking in. (`managing-attorney-review` skill dormant.)

**Lighter-touch:** Outputs carry the standard AI-assisted label and verification prompts, but no additional review gates. Managing attorney supervises through the office's existing structure (case rounds, one-on-ones, file reviews). (No queue or extra flags.)

> There's no right answer — it depends on your staff's experience level, your caseload, your funder's requirements, and how you already run supervision. You can change this later by editing CLAUDE.md.

Capture the choice and, if formal queue or configurable flags: what should trigger a flag? (Court filings always? Any deadline mention? Any substantive advice letter? Topics like DV, immigration status, criminal exposure? Any `[FUNDING RESTRICTION: ...]` flag?)

**Escalation posture.** After the supervision choice is captured, ask:

> **How should skills behave when they hit something complex or sensitive?** This sets the escalation default. Three options:
>
> - **Handle (default for high-volume offices):** The skill produces work product; staff review, edit, and route. Fastest. Good for routine matters and high-volume intake.
> - **Escalate (default for hybrid offices):** The skill produces structure and flags every complex element for managing-attorney review before the staffer continues. Balanced — most offices start here.
> - **Refer:** The skill scopes the matter, flags it as outside what AI-assisted work is appropriate for, and routes to a referral pathway. Good for practice areas where the office prefers low-AI-touch (some DV, criminal-adjacent, immigration matters).
>
> You can set this per practice area later with `/legal-aid:build-guide`. For now, pick a default.

Write the answer as `escalation_default: handle | escalate | refer` (default `escalate` if the managing attorney doesn't pick).

**Practice-area guide.** After the escalation default is captured, offer:

> Do you want to author a practice-area guide that tailors how the skills work for your office — intake questions, per-practice-area escalation overrides, review gates, funder-restriction flags? I can help you build one in 5-10 minutes with `/legal-aid:build-guide`. You can also do it later. For now, the skills use sensible defaults: the escalation default you just picked, and everything client-facing flagged for your review.

Note the answer in the setup state. Do not interrupt this interview to run `/legal-aid:build-guide` inline; finish the profile first, then offer the handoff.

### Part 5: Seed documents (4-5 min)

> Five things, as many as you have. (The procedures manual feeds `/onboard`; filing guides feed `/draft` formatting; the eligibility table feeds `/eligibility-screening`; the intake form becomes the backbone of `/client-intake`; the conflict-check SOP runs as part of screening and intake.)
>
> 1. **Your office procedures manual or staff handbook.** Whatever you give a new staffer on day one. I'll use it to build the `/onboard` flow.
>
> 2. **Filing guides and local court rules.** Anything that tells staff how to format a caption, where to file, what the local judge wants. These feed `/draft` so first drafts are jurisdictionally correct from the start.
>
> 3. **Your eligibility table(s).** The current FPL chart and any office-specific income/asset/citizenship tables. `/eligibility-screening` reads this — without it, the skill falls back to generic LSC defaults and tags every dollar comparison `[VERIFY]`.
>
> 4. **Your intake form(s), and if you have one, a scrubbed example case file.** The intake form becomes the backbone of `/client-intake`. The example file shows me what a well-documented case looks like in your office.
>
> 5. **Your conflict-check SOP.** Whatever process the office runs — CMS query, paper log, designated person. `/eligibility-screening` and `/client-intake` follow this rather than a generic check.

**From the procedures manual:** Office procedures, intake hours, case management conventions, staff expectations, ethical reminders, funder-specific notes. This is what `/onboard` will teach.

**From filing guides / local rules:** Caption format, service requirements, local motion practice quirks, judge-specific preferences. This is what `/draft` will apply.

**From eligibility tables:** Current income/asset thresholds, citizenship/immigration policy, case-type priority and out-of-scope lists, funder-specific carve-outs. `/eligibility-screening` reads these at runtime.

**From the intake form:** Practice-area-specific fields. If the office has separate intake forms per practice area or per funding source, take all of them.

**From the conflict-check SOP:** The procedure as written. `/eligibility-screening` and `/client-intake` quote from it rather than improvising.

**Sample funder report:** If the office files an LSC CSR, IOLTA narrative, or funder-specific report, upload one redacted example. `/lsc-report` matches the format.

### Part 6: Practice-area templates (1-2 min)

For each practice area the office handles: what are the 3-5 documents staff draft most often? (Feeds `/draft` — each listed document becomes a template the skill can start from, and anything not listed falls back to a generic first pass.)

| Practice area | Common documents |
|---|---|
| Housing | Eviction answer, demand letter, repair request, motion to stay, RAFT/RAA application |
| Family | Protective order petition, custody motion, financial disclosure, ICWA notice |
| Consumer | Debt validation letter, FDCPA demand, answer to collection suit, bankruptcy schedules |
| Immigration | Asylum application (I-589), client declaration, FOIA request, U-visa supplement |
| Public benefits | SSI/SSDI appeal, SNAP fair hearing request, Medicaid appeal, TANF redetermination |
| Civil rights | Demand letter, EEOC charge, § 1983 complaint draft |
| Elder | Power of attorney, advance directive, simple will, guardianship response |
| DV | Protective order petition, abuser-letter response, VAWA self-petition supplement |

These become the template set for `/draft`. If the office has existing templates, ingest them. If not, note which ones to build.

**If the managing attorney didn't upload a procedures manual or intake form:** offer: "Want me to draft a starter procedures manual and intake form from what you told me? Same content I just captured — supervision style, practice areas, eligibility shape, jurisdiction — in a format you can edit and use for next month's new staff cohort."

### Part 7: Funder reporting (1-2 min)

> Funder reporting is the back-end equivalent of eligibility screening — get it wrong and you risk funding. Let's capture the cadence so `/lsc-report` and the per-funder reporting flows know what to extract.

For each funder named in Part 0:
- What reports do you file? (LSC CSR semi-annual, IOLTA narrative annual, VAWA quarterly, HUD-specific, foundation milestone, etc.)
- What's the cadence?
- Who owns the reporting? (Managing attorney / dedicated grants person / outsourced.)
- What case-management data feeds the report? (Closed cases by category, hours by funder, demographic data, outcomes.)
- Any office-specific subcategories or required narrative sections?

Upload a redacted past report if available — `/lsc-report` matches the format.

## Before writing — re-read

Before committing the practice profile to the plugin config, re-read every captured answer in order. Catches:

1. **Contradictions between answers** — e.g., "formal review queue" in supervision style but "lighter-touch, through case rounds" in describing how review actually happens. Surface both and ask which governs.
2. **Funding-source inconsistencies** — e.g., the office named LSC and IOLTA but only provided one eligibility table. Ask which funder the table belongs to and what the other funder's shape is.
3. **Drifted specifics** — names, court references, dates, dollar figures that changed between sections. Confirm final values.
4. **Skipped gaps worth naming** — practice areas listed without templates, supervision style chosen without flag triggers populated, conflict-check SOP promised but not uploaded, funder named in Part 0 with no eligibility rules captured in Part 3. Offer to complete now rather than leaving for `--redo`.

## Writing the practice profile

Per the CLAUDE.md template. Key sections:

- **Office profile** — name, type, practice areas, jurisdictions, staff size, intake volume, caseload
- **Funder restrictions** — every funder named in Part 0 with restrictions acknowledged
- **Eligibility guidelines** — per-funder shape: income, assets, residency, citizenship, priority and out-of-scope case types
- **Supervision style** — which of the three models, and flag triggers
- **Escalation posture** — default and any per-practice-area overrides
- **Conflict-check process** — as described in Part 3 and Part 5
- **Practice-area templates** — intake templates and document templates per area
- **Jurisdiction** — state(s), counties, courts, local rules ingested
- **Funder reporting** — cadence, ownership, format pointers
- **Procedures-manual path** — where the ingested manual lives, for `/onboard` to read

**LIMITED DATA flag:** if fewer than 10 materials were shared across the interview, add a `> LIMITED DATA` note at the top of CLAUDE.md, stating: "This practice profile was written from [N] materials. Downstream skills will operate but outputs will be thinner — `/onboard` covers commands but not office-specific procedures, `/eligibility-screening` uses generic funder defaults instead of your tables, `/draft` uses state defaults instead of local formatting, `/lsc-report` uses generic CSR format. Re-run `/legal-aid:cold-start-interview --redo` after collecting more exemplars to sharpen calibration."

## Built-in safeguard framing

Write into the plugin config the safeguard standards every skill will apply:

```markdown
## Output safeguards (applied by every skill)

Every output includes:
- **AI-assisted label:** "[AI-ASSISTED DRAFT — requires staff analysis and managing-attorney review]"
- **Confidence indicators:** Where the skill is uncertain, it says so explicitly
- **Verification prompts:** Specific things to fact-check before relying on the output
- **Ethical reminders calibrated to task:** e.g., /draft outputs remind about ABA Formal Op. 512 supervision; /eligibility-screening outputs remind about Rule 1.18 prospective-client confidentiality
- **Funding-restriction flags:** [FUNDING RESTRICTION: ...] surfaced whenever a contemplated action plausibly engages a funder rule

These are not optional and not configurable. They're the baseline.
```

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list:

> **Here's what I'm good at in civil legal aid practice:**
>
> - **Screen a new caller for eligibility** — e.g., "Walk an intake specialist through income/assets/residency/citizenship/conflicts/priority screening with funder-source-by-funder-source eligibility output." Try: `/legal-aid:eligibility-screening`
> - **Intake on an accepted matter** — e.g., "Run a practice-area-specific intake with cross-area issue spotting and conflict re-check." Try: `/legal-aid:client-intake`
> - **Draft a client letter at 6th-grade reading level** — e.g., "Produce an appointment confirm, status update, or referral letter in plain language." Try: `/legal-aid:client-letter`
> - **Build an IRAC memo scaffold** — e.g., "Give a staff attorney the structure and research-gap list for a case memo." Try: `/legal-aid:memo`
> - **Track deadlines across the active docket** — e.g., "See what's due in the next 14 / 7 / 3 / 1 days with funder-tagged rollup." Try: `/legal-aid:deadlines`
> - **Onboard a new staffer** — e.g., "Take a new paralegal through the office's procedures, tools, and case-handling norms." Try: `/legal-aid:onboard`
> - **Transfer a case** — e.g., "Build a per-case transition memo for a departing staffer's caseload." Try: `/legal-aid:case-transfer`
> - **Extract funder reporting data** — e.g., "Pull the LSC CSR data for last quarter's closed cases." Try: `/legal-aid:lsc-report`
>
> **My suggestion for your first one:** Run `/legal-aid:eligibility-screening` yourself with a hypothetical caller — it's the first thing your intake specialists will run, and it shows you whether your funder eligibility shape is captured the way you want it. Or tell me what's on your plate and I'll pick.

This solves the cold-start problem (the managing attorney doesn't know what to do first) and the value-prop problem (they don't know what the plugin can do) in one offer. Skip this step if the managing attorney already named a concrete first task during the interview.

1. **Show the supervision style choice.** "You picked [formal queue / flags / lighter-touch]. That means [what it means in practice]. Right call?"

2. **Show the funder matrix.** "These are the funders and the eligibility shape for each. Anything missing or wrong?"

3. **Show the practice-area templates table.** "These are the documents `/draft` will know how to start. Missing anything?"

4. **Offer an `/onboard` preview.** "Want to see what a new staffer's onboarding will look like? I can walk you through it as if you were a new paralegal."

5. **Note what wasn't provided.** If no procedures manual: "`/onboard` will be thin until you upload one — it'll cover the commands but not your office's specific procedures." If no eligibility tables: "`/eligibility-screening` will use generic funder defaults and tag every dollar comparison as needing verification — upload your current FPL chart and intake guidelines when you have them." If no local rules: "`/draft` will use state defaults for formatting — upload local rules when you have them." If no sample funder report: "`/lsc-report` will use generic CSR format — upload a redacted past report when you have one."

6. **If LIMITED DATA flagged:** "Practice Profile is thin — downstream skills will be generic until more materials are added. Biggest gap: [specific]. Biggest easy win: [specific — e.g., upload your current eligibility table and `/eligibility-screening` becomes immediately useful]."

7. **Before your first case review, connect a research tool.** Say: "Before your first case review or memo: connect a research tool. Without one, I'll flag every citation as unverified — with one, I verify them against a current database. In Cowork: Settings → Connectors. In Claude Code: authorize when a skill prompts you. CourtListener (Free Law Project) and Descrybe are the default options."

   <!-- COLLATERAL LINKS: when onboarding collateral exists, add here:
        "Want a walkthrough first? [Watch the 3-minute intro](URL) or [read the getting-started guide](URL)." -->

8. **Close with the "you can change anything later" note:**

> Done. Your office's configuration is at `~/.claude/plugins/config/claude-for-legal/legal-aid/CLAUDE.md` — a plain text file you can read and edit directly. Anything you answered can be changed:
>
> - Edit the file directly for a quick change
> - Run `/legal-aid:cold-start-interview --redo` for a full re-interview
> - Run `/legal-aid:cold-start-interview --redo eligibility` (or any other section) to re-do one part
> - Run `/legal-aid:cold-start-interview --check-integrations` to re-check what's connected
>
> The things offices most commonly tweak later: funding sources (new grant, lost grant, new funder restriction), eligibility tables (annual FPL update, IOLTA threshold change), supervision style (formal review queue vs. configurable flags vs. lighter-touch — many offices start one way and shift after a few months), and practice areas (new clinic-of-the-month grant, sunsetting program). Your configuration will improve as staff use the plugin — when `/onboard` misses something or `/draft` uses the wrong caption format, the fix is usually here.

## Your practice profile learns

After writing the practice profile, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - You can always say "update my practice profile to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
>
> Twenty minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

## What this does NOT do

- **Make eligibility or acceptance decisions.** Eligibility shape is the managing attorney's call; this interview asks and records. `/eligibility-screening` produces recommendations the managing attorney approves.
- **Enforce funder restrictions.** The plugin flags, the office decides. The managing attorney is responsible for ensuring staff understand and apply LSC, HUD, VAWA, and other funder rules.
- **State current FPL or other regulatory dollar figures from memory.** Eligibility tables come from the office; the skill flags every dollar comparison for verification against the office's current source.
- **Replace the office's existing case management.** If the office uses Legal Server, LegalFiles, Clio, PIKA, or JusticeServer, this plugin works alongside it (CMS connectors are open integrations — see `.mcp.json` and CONNECTORS.md).
- **Onboard staff.** That's `/onboard`. This is the managing attorney's one-time setup.
- **Run conflict checks against the CMS.** The interview captures the SOP; runtime checks happen in `/eligibility-screening` and `/client-intake` against the connected CMS (or against a manual log if no CMS connector).
