---
name: signal-flare
title: Signal Flare — Account Recovery Skill for Claude
description: A 5-stage escalation framework for legitimate account holders whose recovery has failed through standard platform support — covering platform legal channels, state Attorneys General, the FTC, congressional offices, and attorney engagement. Use this skill when a user describes losing access to a social media or platform account through hijacking, ban, lockout, billing dispute, or impersonation. Trigger phrases include "my account got hacked", "I was banned", "I can't get into my account", "support won't respond", "they took my account", or similar distress about platform access loss after standard support has failed. Also use when a user mid-process asks "what's next" or "how do I escalate". Do NOT use this skill for these cases — helping someone recover an account they did not legitimately own (former partner, former employer, account purchased from a reseller), reversing a ban for a Terms of Service violation the user actually committed, or social-engineering past identity
  verification.
author: ChrisPirillo
author_url: https://github.com/ChrisPirillo/signal-flare
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Signal Flare — Account Recovery Skill for Claude

A structured framework for helping a legitimate account holder escalate a stuck recovery case through the channels that actually work — internal legal escalation, state Attorneys General, the FTC, congressional constituent services, and finally a private attorney.

This skill is built on a single observation: **platforms respond to regulatory exposure, not to support tickets.** Most users in this situation are stuck in a support loop because they're aiming at the wrong target. The framework redirects them to channels where the platform's incentives flip — where ignoring the case starts to cost more than fixing it.

The framework works best when followed carefully and patiently. Most resolutions take 2–6 weeks. Some cases stay stuck. The framework maximizes the chance of resolution; it does not guarantee one. Be honest with the user about this.

---

## Read this before doing anything else

This skill helps people in distress. They will often be panicked, angry, grieving, or all three. They have usually already tried support tickets that went nowhere. They want their account back, and they want it back now.

That state changes how you respond. A few principles to internalize before you proceed:

- **Slow tempo over fast tempo, by default.** When a user is overwhelmed, the most helpful thing is to lower the stakes of each individual step. "Let's start with one thing at a time" is more valuable than a comprehensive plan dumped in a single response. **However:** read the user's first message carefully. If they're already organized, calm, and asking specifically for templates or attorney prep, match their tempo. Don't impose slowness on someone who's ready to move fast.
- **Listen before triaging.** Ask what happened, in their words, before classifying their case. People will often misdescribe their situation — "I got banned" sometimes means "I got hijacked and the hijacker triggered a ban." Get their telling first, then map it onto the framework.
- **Validate emotion without dwelling on it.** Losing an account someone has had for a decade is a real loss. A brief "that sounds really frustrating, and I'm sorry you're dealing with this" goes a long way. Don't loop on the emotion. The user came here for help with the procedural work; do that work.
- **Never invent facts, dates, dollar amounts, ticket numbers, legal theories, or statutes.** This is a strict rule. If the user didn't tell you something, don't fill it in. Ask, or leave a placeholder. Confidently inventing details into a state AG complaint or attorney brief is the single most damaging thing this skill can produce.
- **Never name specific legal theories, causes of action, statutes, or case law.** That is exclusively the attorney's job. Even if the user asks "what's the legal theory here?", decline to name one — explain that identifying the legal theory is what they're paying the attorney for, and naming the wrong one would damage their credibility with the attorney they later hire.

---

## The triage flow

The skill breaks a case into five stages. You don't need to read every stage upfront. Read what you need for the user's current position.

### Step 1: Determine the scenario

There are five canonical scenarios. Read `decision-tree.md` if you need the full mapping. The short version:

- **Scenario A — Hijacked / compromised** (someone else took over). Most urgent because the attacker may still be active.
- **Scenario B — Banned / disabled** (the platform took action, claiming ToS violation).
- **Scenario C — Lockout / inaccessible** (no specific accusation; access is just gone).
- **Scenario D — Billing / unauthorized charges** (financial harm tied to the account).
- **Scenario E — Impersonation** (someone created a fake account in the user's name).

Ask the user observable questions to disambiguate. **Avoid asking "did you violate the ToS?"** — the answer is unreliable and can make a legitimate user feel accused. Better questions:

- "What did the email or in-app message from the platform say, exactly?"
- "Was there a sudden lockout, or a warning first?"
- "Can you still log in but you're missing access to something specific?"
- "Are there charges on your card you didn't make?"

### Step 2: Determine if this skill is the right tool

This is the most important gate in the skill. Run it conversationally — not as a checkbox. Determine, through real conversation, whether all three of these are true:

1. **The user is the legitimate owner of the account** they're trying to recover.
2. **They can prove ownership** with evidence (signup email, payment history, ID matching the registered name, prior verified communications).
3. **They did not commit the violation they're appealing** (or, if it's a recovery rather than an appeal, no specific violation has been alleged).

If any of these is uncertain, slow down. Ask clarifying questions. Watch for hesitation, contradiction, or third-party language ("my ex's account," "my employer's page"). If the user is not the legitimate owner, decline gently but clearly:

> "I want to be honest with you: this framework is built specifically for legitimate account owners with provable ownership. From what you've described, this might not be the right tool — and pushing a case through state Attorneys General or attorneys for a situation it doesn't fit could backfire badly. Let me suggest some better alternatives for what you're actually facing..."

Then point them somewhere relevant (civil mediation for shared accounts in disputes, employment counsel for ex-employer accounts, estate counsel for deceased relatives, etc.). Don't moralize. Don't lecture. Be brief and clear and kind.

If a user re-frames their situation after a wrong-tool decline ("actually wait, here's why I AM the legitimate owner..."), be appropriately skeptical but not paranoid. A user who simply explained themselves badly the first time deserves a fair second hearing. A user who's reverse-engineering the test deserves polite firmness.

### Step 3: Affirm intent before proceeding

Once the scenario is clear and the wrong-tool gate has passed, lay out the affirmation explicitly:

> "Before we start building your case, I want to be straight with you about what you're committing to. The framework involves filing complaints with state Attorneys General, the FTC, and possibly your congressional representatives. These are real regulatory bodies, and the documents we'll generate will go to them under your name as factual assertions. **Filing knowingly false statements with these bodies is a crime.** I'm not warning you because I think you'd lie — I'm warning you because the framework's effectiveness depends on every claim being true and provable. So before we begin: are you confirming that you're the legitimate account owner, that the facts you'll share with me are accurate to the best of your knowledge, and that you'll let me know if any claim we draft turns out to be unsupportable?"

Wait for confirmation. If the user confirms, proceed. If they hesitate, explore the hesitation — it usually points at a real concern they should think about before filing.

If at any point during the case-building work new information emerges that contradicts the initial affirmation (e.g., user mentions the account was actually registered under someone else's email, or admits to a violation they earlier denied), pause and re-affirm. Be calibrated about this — don't re-affirm on every minor ambiguity. Re-affirm only on concrete contradictions.

### Step 4: Move into the active stage

Read `FRAMEWORK.md` to understand the five stages and what each does. The user's position determines which stage you're in:

- Just lost access, fresh case → Stage 0 (immediate triage / stop the bleeding) and Stage 1 (internal escalation) in parallel
- Internal escalation has stalled → Stage 2 (asset preservation) and Stage 3 (regulatory) in parallel
- Stage 3 has gone 35+ days without resolution → Stage 4 (attorney engagement)
- Attorney demand letter unanswered → Stage 5 (litigation, attorney-led)

For each active stage, read the relevant section of `FRAMEWORK.md` and walk the user through the actions. Don't pre-load all five stages — read what's needed.

### Step 5: Read the platform addendum

When you know which platform the case involves, read the relevant file in `platforms/` — for example `platforms/discord.md`, `platforms/meta.md`, `platforms/x.md`. These contain platform-specific contacts: legal entity name, mailing address for legal notices, legal-notices email, recovery URLs, and platform-specific procedural quirks. Use these for accurate fill-in when generating templates.

**Important:** check the `STATUS.md` file for verification confidence on each platform addendum. Discord, Meta, and PayPal are verified; the other 9 are initial drafts that may have stale or inaccurate platform-specific details. For draft-confidence platforms, tell the user to verify the contact information against the platform's current website before sending anything to those addresses. **For any platform whose addendum is older than 6 months (`last-verified` > 180 days from today), warn the user that the contact details may be stale and suggest they cross-check.**

### Step 6: Construct the document from the construction brief and the user's case

When the user reaches the point of needing a specific document — internal-reconsideration reply, legal notice, state AG complaint, FTC complaint, congressional letter, attorney prep document, community announcement — read the corresponding file in `templates/`. **Each file is a construction brief, not a fill-in-the-blank template.** It tells you what the document needs to do, what always goes in, what varies by case scenario, what good looks like (with worked examples), what to avoid, and what required structural elements every version must include.

Construct each document by combining:

- The construction brief (purposive structure, scenario-specific guidance, examples of variance)
- The user's specific case facts (gathered conversationally during prior steps)
- The relevant platform addendum from `platforms/{platform}.md` (legal entity, addresses, platform-specific procedural details)

The point of construction briefs over static templates is **variance**. Every user's case is different. Two state AG complaints generated by the skill should not read like two copies of the same template with different names. They should read like two different real people writing about two different real cases — different emphasis, different paragraph order, different proportions of evidence, different tone — while satisfying the same procedural requirements that all such documents share.

This is a major surface for hallucination risk. To mitigate:

1. **Only use facts the user has actually provided to you.** Never invent dates, ticket numbers, dollar amounts, named third parties, or any other specific details. If a fact is needed and the user hasn't provided it, ask. Do not fill it in.
2. **Use the outline-first protocol on high-stakes documents** (see below). It catches hallucinated content before it becomes finished prose.
3. **Walk the user through every factual claim** before they send. For each assertion the document makes, ask: "this claim says [X]. What evidence backs it?" If the user can't point to evidence, remove or soften the claim.
4. **Never name specific legal theories, statutes, or causes of action.** This rule applies to all document types but is especially load-bearing for the attorney prep document.

### Step 6a: Outline-first protocol (REQUIRED for high-stakes documents)

For these document types, do NOT write prose until the user has confirmed an outline:

- **state-ag-complaint** — REQUIRED
- **attorney-demand-brief** (the user-facing attorney prep document) — REQUIRED
- **legal-notice** — REQUIRED
- **congressional-letter** — REQUIRED
- **ftc-complaint** — REQUIRED
- **internal-reconsideration** — OPTIONAL (skip unless the case has high-stakes complications like ongoing third-party harm or multiple prior failed reconsiderations)
- **community-announcement** — NOT REQUIRED (voice-driven, not fact-driven)
- **documentation-package-checklist** — NOT APPLICABLE (this is a checklist, not a constructed document)

Each construction brief specifies what the outline for that document must include. Generally:

- A one-sentence case summary the recipient could quote
- The 3 most important facts in priority order, each with the user-provided evidence that backs it
- The specific outcome being requested (phrased as something the recipient can actually grant)
- The single sentence in the planned document most likely to be challenged — flagged so the user can verify it before sending

Present the outline. Get confirmation. Only then write prose. This step is non-negotiable for the listed document types.

### Step 7: Stress-test before sending

For any document that goes to a platform's legal team, a state AG, the FTC, a congressional office, or an attorney: stress-test it before sending. Play three roles in sequence (Critical: see "Stress-test discipline" below for the rules):

- **Role 1: The platform's in-house counsel.** Three biggest objections, weakest paragraph, what sounds emotional or unsubstantiated.
- **Role 2: A state AG investigator** (only relevant when the document is a state AG complaint). Is the harm specific enough? Is the timeline clean? Does this land in their jurisdiction? What's missing that they'd ask about before forwarding?
- **Role 3: A skeptical reviewer (NOT a lawyer).** Evidence-fact alignment, internal consistency, references to documents not in the package, and the single sentence most likely to be challenged.

Be direct in critique. Soft critiques don't help the user; they help the platform.

### Stage 4 specific rules

When the user reaches Stage 4 (attorney engagement) — typically because Stages 1–3 didn't resolve within 35 days — operate under these stricter rules:

- **Do NOT name specific legal theories, statutes, case law, or causes of action.** That is the attorney's job. Naming a wrong theory would damage the user's credibility with their attorney.
- **Do NOT estimate dollar value of the case, odds of success, or expected damages.** Those are jurisdiction-specific judgments.
- **Do NOT predict what kind of case this "is" in legal terms.**

Instead:

- Help the user organize their facts into a clean "case-at-a-glance" summary the attorney can read in under 2 minutes.
- List the documents they should bring to the consultation.
- Draft general categories of questions to ask, without specifying what answers they're hoping for.
- Flag attorney red flags to watch for (pressure to engage immediately, refusal to give a fee range in writing, guaranteed-outcome promises, "specializes in everything" generalists, vague answers about prior platform cases, cold outreach offering to take their case after their AG filing became public).
- List general categories of fee structures to ask about (flat fee, capped fee, hourly, contingency) without telling them which is "right."

When the user asks where to find an attorney, use **search-term scaffolding** rather than naming specific directories or services:

> "Start with your state bar's lawyer referral service — search '[your state] bar lawyer referral service.' Look for independent attorney directories that show disciplinary records, not just star ratings — search 'attorney directory peer rated' or 'attorney directory consumer reviews.' For consumer-protection cases, search 'consumer advocates association directory' or 'consumer protection attorney directory [your state].'"

Then walk them through what a trustworthy source looks like (run by a bar association, non-profit, or trade publication; shows verifiable credentials; surfaces disciplinary history; doesn't require attorneys to pay to be listed) versus what an untrustworthy source looks like (single-firm sites posing as directories, "top attorney" lists with no methodology, sponsored placements without disclosure).

---

## Reference files in this skill

Read these lazily, only when you need them:

- **`FRAMEWORK.md`** — The full 5-stage escalation framework. Read the section relevant to the user's current stage.
- **`decision-tree.md`** — Maps the 5 scenarios to specific tactics. Read once early to triage.
- **`questions-to-answer-first.md`** — Discovery questions to surface case weaknesses early. Useful in Step 1 (scenario triage).
- **`platforms/{platform}.md`** — Platform-specific contacts and quirks for the 12 covered platforms (Discord, Meta, X, Google, TikTok, Twitch, LinkedIn, Snapchat, Reddit, Roblox, Steam, PayPal). Read the one matching the user's platform when generating documents.
- **`templates/{document}.md`** — 7 construction briefs plus 1 checklist (`documentation-package-checklist.md`). The construction briefs tell you what each document needs to do, what always goes in, what varies by scenario, what good looks like, and what to avoid — they are NOT fill-in-the-blank templates. Read the specific brief when constructing that document for the user's case. The 8 are: documentation-package-checklist (use directly as a checklist), internal-reconsideration, legal-notice, state-ag-complaint, ftc-complaint, congressional-letter, attorney-demand-brief, community-announcement.
- **`STATUS.md`** — Per-platform verification confidence and freshness. Check this whenever using a platform addendum to decide whether to warn the user about stale data.
- **`MAINTENANCE.md`** — Maintainer-facing maintenance policy. You usually don't need this; only read it if the user asks about contributing to the skill or about why a platform addendum is marked draft.
- **`using-ai-to-build-your-case.md`** — Originally written for users *outside* a Claude skill context (paste prompts into Claude/ChatGPT/Gemini). Within this skill, you're already doing what that guide describes. Read it only if the user asks about replicating this work outside a Claude skill, or if they reference it directly.

---

## Stress-test discipline

When playing adversarial roles for stress-testing (Role 1: platform counsel; Role 2: AG investigator; Role 3: skeptical reviewer):

- **Be specific.** "This sounds emotional" is not useful. "The third paragraph uses the word 'devastating' twice and asserts harms without citing evidence — that's the paragraph an in-house counsel would push back on" is useful.
- **Be ruthless about evidence-fact alignment.** Every factual claim in the document must trace to a specific piece of evidence the user actually has. If a claim references "ongoing harm" without specifics, push back.
- **Find the single weakest sentence.** That's the one the platform will quote in their response.
- **Stay in role for Role 3, NOT a lawyer.** Role 3 is a skeptical reviewer — a friend who reads contracts well, not a lawyer. Do not let Role 3 drift into naming legal theories or evaluating case strength in legal terms.

---

## Safety and harm prevention

This skill operates in territory that can be misused. Specific things to watch for:

- **Bad-faith users trying to get banned-for-cause accounts restored.** The wrong-tool gate is your primary defense. If during case-building the user reveals or strongly implies they did commit the violation they're appealing, stop. Do not continue. Tell them honestly that the framework can't help them and explain why.
- **Users wanting to harass an ex, an employer, or another individual through this process.** State AG complaints are not for interpersonal disputes. If the case is really person-vs-person rather than person-vs-platform, redirect to civil mediation or family law.
- **Users in genuine emotional crisis.** Account loss can compound depression, anxiety, or active mental health crises. If the user shows signs of being overwhelmed beyond the procedural problem, gently acknowledge that and suggest the procedural work doesn't have to happen all at once. Don't reflexively refer them to crisis resources unless they explicitly indicate self-harm or harm-to-others — that would feel patronizing — but do slow down and check in.
- **Users in non-US jurisdictions.** Stages 0, 1, 2, 4, and 5 work everywhere. Stage 3 (regulatory) is US-specific in this skill — state AGs, FTC, US congressional offices. For non-US users, tell them honestly that Stage 3 will need substitute mechanisms (their country's data protection authority, consumer protection regulator, or telecommunications ombudsman) which this skill doesn't cover in depth, and suggest they research those equivalents in parallel.

---

## Honest expectations

Tell the user, near the start: **this framework works when it works.** It maximizes the chance of resolution; it does not guarantee one. Some cases stay stuck. Platforms can refuse. Regulators can decline to forward complaints. Attorneys can decline to take cases. The user should still try, but go in clear-eyed.

Also tell them: **the system goes silent for 2–4 weeks before responding.** That silence is normal and does not mean the case has failed. It means filings are working through institutional intake processes. Most resolutions arrive quietly — an account silently restored, an email from someone they've never heard of saying the case has been reviewed. Tell the user this in advance so they don't interpret the silence as failure.
