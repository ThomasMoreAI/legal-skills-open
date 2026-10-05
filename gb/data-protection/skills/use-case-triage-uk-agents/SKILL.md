---
name: use-case-triage-uk-agents
title: /use-case-triage
description: Quickly determine whether a UK processing activity needs a DPIA, a mandatory Art.35 DPIA, or can proceed — surfaces lawful basis issues, Children's Code checks, PECR implications, and privacy notice conflicts. Use when the user asks "does this need a DPIA", "triage this feature", "privacy check on X", "is this okay from a UK privacy perspective", or describes a new data processing activity, product feature, or vendor relationship.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/privacy-legal-uk/skills/use-case-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /use-case-triage

1. Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. Confirm UK privacy practice is configured — if not, stop and direct to setup.
2. Run the workflow below. Clarify the activity if vague.
3. House trigger check → mandatory DPIA trigger check (UK GDPR Art.35(3) + ICO guidance) → lawful-basis determination → Children's Code check → PECR check → privacy notice conflict check.
4. Output: classification (PROCEED / DPIA REQUIRED / DPIA MANDATORY / STOP), reasoning, conditions table, cross-plugin handoffs.
5. Offer to continue into DPIA generation if assessment is required.

```
/privacy-legal-uk:use-case-triage "New feature that uses behavioural data to personalise content recommendations"
```

---

# UK Privacy Use Case Triage

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty, vendors, and clients (for work product) could waive protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitised version for the broader channel, or (c) both.

## Purpose

Answer the question that comes up before anyone runs a DPIA: "does this thing even need one?" And if it does, what kind — house DPIA, or mandatory Art.35 DPIA? What's blocking the way?

UK privacy triage is faster than DPIA generation but upstream of it. The output is one of four classifications:
- **PROCEED** — No DPIA needed. Standard safeguards apply.
- **DPIA REQUIRED** — House assessment needed before or alongside deployment.
- **DPIA MANDATORY** — A mandatory DPIA is required under UK GDPR Art.35(3) and/or the ICO's list of processing operations. DPO consultation mandatory (Art.35(2)). If residual high risk remains after mitigations, prior ICO consultation required (Art.36).
- **STOP** — Processing activity conflicts with the privacy notice, has no identifiable lawful basis, or would breach UK GDPR as described. Needs redesign before proceeding.

## Jurisdiction assumption

This triage assumes the UK jurisdictional scope specified in your configuration (UK GDPR + DPA 2018 as the primary regime). If the processing activity also involves EU data subjects, EU GDPR applies in parallel — note this and flag it for dual-regime analysis.

## Read the config first

Before triaging, always read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md`. The DPIA trigger criteria, UK regulatory footprint, and privacy notice commitments there are authoritative. Generic privacy law reasoning is not a substitute for what this organisation has actually committed to.

If the file is missing or contains `[PLACEHOLDER]`, surface this bounce:

> I notice you haven't configured your UK privacy practice profile yet — that's how I tailor the DPIA trigger criteria, UK regulatory footprint, and privacy notice commitments to your practice.
>
> **Two choices:**
> - Run `/privacy-legal-uk:cold-start-interview` (2 minutes) to configure your profile, then I'll triage tailored to YOUR practice.
> - Say **"provisional"** and I'll triage against generic UK GDPR defaults — middle risk appetite, qualified legal-professional role, UK jurisdiction (UK GDPR + DPA 2018 + PECR) — and tag every output `[PROVISIONAL — configure your profile for tailored output]`.

### Provisional mode

If the user says "provisional," run triage normally using these generic UK defaults: middle risk appetite, qualified-professional role, UK jurisdiction (UK GDPR + DPA 2018 + PECR baselines), no configured playbook. Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end, append:

> "That was a generic run against UK GDPR defaults. Run `/privacy-legal-uk:cold-start-interview` to get output calibrated to YOUR practice — your UK regulatory footprint, your privacy notice commitments, your risk appetite. 2 minutes."

---

## Triage process

### Step 1: Understand the activity

If the description is vague, ask before classifying. Get specific on:

- What data is being collected or processed? Which categories? Is any of it UK GDPR Art.9 special category data (health, biometric data processed to uniquely identify a person, racial or ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, sex life or sexual orientation) or criminal convictions / offences data (Art.10)?
- Who are the data subjects — customers, employees, third parties? **Are any of them, or are any likely to be, children under 18?**
- What's the purpose? What problem is this solving?
- Is this new data collection, or repurposing data you already have?
- Is a third-party vendor involved? If yes: new vendor or existing? Do you have an Art.28 DPA in place?
- Is any automated decision-making involved — does the output affect anyone? Is it a decision that produces legal or similarly significant effects?
- What's the deployment context — internal only, customer-facing, public?
- Does this involve cookies or similar technologies on a website or app? (PECR check)
- Does this involve direct marketing by electronic means — email, SMS, automated calls? (PECR check)

"New feature" and "data processing activity" are not enough to triage accurately.

---

### Step 2: Check house triggers

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## DPIA house style` → Trigger criteria. Apply them.

If the house trigger is met → at minimum **DPIA REQUIRED**.

If the house trigger is not met, continue to Steps 3-6 before concluding PROCEED.

---

### Step 3: UK GDPR mandatory DPIA trigger check (Art.35(3))

**Research the currently operative UK GDPR Art.35(3) triggers and the ICO's published list of processing operations that require a DPIA** before finalising classification. Use the uk-legal MCP where available. Cite primary sources with OSCOLA-style citation format (e.g., *Data Protection Act 2018*, s 35; UK GDPR, art 35(3)).

The three statutory mandatory triggers under UK GDPR Art.35(3) `[UK-GDPR-ART.35(3)]`:

> **Ask in order:**
>
> (a) **Systematic and extensive evaluation of personal aspects** based solely or partly on automated processing, including profiling, where decisions produce **legal or similarly significant effects** on natural persons. Does this processing evaluate personal aspects automatically and produce consequential decisions? Think: credit scoring, behavioural advertising targeting, hiring algorithms, fraud detection that blocks accounts, insurance pricing by algorithm.
>
> (b) **Large-scale processing of special category data** (UK GDPR Art.9) or data relating to criminal convictions and offences (Art.10). Does this processing involve: health data, biometric data for unique identification, racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, sex life or sexual orientation — and is it at scale? Or criminal records / offences data? There is no statutory definition of "large-scale" — ICO guidance provides indicators: number of data subjects (absolute and as proportion of population), volume of data, range of categories, duration, geographical extent. Apply judgment; flag uncertainty `[review]`.
>
> (c) **Systematic monitoring of a publicly accessible area** on a large scale. Does this processing involve CCTV, drone monitoring, WiFi tracking, or similar surveillance of publicly accessible spaces?

**In addition, check the ICO's list of processing types that always require a DPIA.** The ICO has published a list of processing operations it considers likely to result in high risk, which it updates periodically. Always use the uk-legal or govuk MCP to retrieve the current ICO guidance — model knowledge of the list may be out of date. `[ICO-GUIDANCE — verify current list via uk-legal or govuk MCP]`

ICO list typically includes (verify current version):
- Large-scale profiling
- Processing biometric data for unique identification purposes
- Processing data about children for the purposes of targeting them with advertising or marketing
- Processing location data for any purpose at scale
- Processing genetic data other than by the controller's own doctor/health professional for the primary purpose of providing healthcare
- AI / machine learning systems that process personal data to make decisions about people
- Combinations of datasets from different sources that individually seem innocuous but combined create novel risks
- Invisible processing (processing not apparent to data subjects that they would not reasonably expect)

If **any** mandatory trigger is met → **DPIA MANDATORY**, regardless of house trigger.

Strong indicators (not necessarily mandatory but treat as DPIA REQUIRED minimum):
- New technology or novel use of existing technology
- Children's data (any age, for UK Children's Code; under 13 = heightened)
- Combining datasets not collected together
- Data that could enable discrimination even accidentally
- Processing data subjects would not expect
- Re-use of data for a new, incompatible purpose (UK GDPR Art.5(1)(b) purpose limitation)
- Transfers to non-adequate countries without confirmed mechanism

---

### Step 4: Lawful basis determination

For UK GDPR processing, a lawful basis (Art.6) must be identified before processing begins. For special category data (Art.9), an additional Art.9 condition is also required.

**UK GDPR Art.6 lawful bases:**

| Basis | When it applies | Constraints |
|---|---|---|
| Consent (Art.6(1)(a)) | Data subject freely, specifically, informedly agrees | Must be genuine, unambiguous, withdrawable; not bundled; records required |
| Contract (Art.6(1)(b)) | Processing necessary for the performance of a contract with the data subject | Strictly necessary; not "useful" |
| Legal obligation (Art.6(1)(c)) | Processing required by UK law | Must cite the specific legal obligation |
| Vital interests (Art.6(1)(d)) | Necessary to protect life | Last resort; not for routine commercial processing |
| Public task (Art.6(1)(e)) | Controller is a public authority or exercises public authority functions | Defined by UK law |
| Legitimate interests (Art.6(1)(f)) | Legitimate interest exists, processing is necessary, interests not overridden by data subject rights/interests (three-part test — requires a Legitimate Interests Assessment) | Cannot be used by public authorities in their public authority capacity; data subjects have objection right; not for processing that routinely overrides data subjects |

**Legitimate Interests Assessment (LIA):** Where the proposed lawful basis is legitimate interests, a three-part LIA is required: (1) purpose test — is the interest legitimate?; (2) necessity test — is processing necessary for that purpose?; (3) balancing test — do the interests of the controller / third party override the rights and interests of data subjects? If LI is the proposed basis, flag that a LIA is required as a condition of proceeding. `[UK-GDPR-ART.6(1)(f)]`

**For special category data (Art.9):** An additional processing condition from UK GDPR Art.9(2) (and in some cases DPA 2018 Sch.1) is required, *in addition to* an Art.6 lawful basis. The most common conditions:

- Art.9(2)(a): explicit consent
- Art.9(2)(b): employment, social security, and social protection (specific conditions in DPA 2018 Sch.1 para.1) `[DPA2018-S.10]`
- Art.9(2)(g): substantial public interest (DPA 2018 Sch.1 conditions apply) `[DPA2018-S.10, SCH.1]`
- Art.9(2)(h): healthcare purposes
- Art.9(2)(i): public health

If neither an Art.6 basis nor an Art.9 condition can be identified → **STOP**.

---

### Step 5: ICO Children's Code (Age Appropriate Design Code) check

**Run this check whenever the processing may involve children.** The Children's Code (issued under DPA 2018 s.123) applies to "information society services" (broadly: online services, apps, connected toys) that are **likely to be accessed by children** under 18 — whether or not they are designed for children. Verify against current ICO Children's Code guidance via the uk-legal or govuk MCP. `[DPA2018-S.123] [ICO-GUIDANCE]`

> Does this service / feature:
> - Serve or could serve users under 18? (If the service doesn't verify age, consider whether children could access it.)
> - Involve profiling children based on their data?
> - Use nudge techniques or default privacy settings that are not high-privacy for children?
> - Collect more personal data from children than strictly necessary?
> - Use children's data in ways they or their parents would not reasonably expect?
> - Involve data sharing or data use for marketing / advertising directed at children?

If any of these applies:

- Flag **Children's Code obligations apply** in the conditions table
- Add to the DPIA REQUIRED / MANDATORY conditions: Children's Code compliance assessment
- Note: the ICO Children's Code has 15 standards — a feature-level check here flags the obligation; a full Children's Code compliance review is a separate exercise. `[ICO-GUIDANCE]`
- Note: children's data processed at scale likely triggers Art.35(3)(b) mandatory DPIA (special category if health/biometric; or ICO guidance on profiling children).

---

### Step 6: PECR check

**Run this check whenever the processing involves websites, apps, electronic marketing, or electronic communications services.** PECR (SI 2003/2426) operates alongside UK GDPR — it is not subsumed by it.

> Does this processing involve:
> - **Cookies or similar tracking technologies** on a website or app? → Prior informed consent required for non-essential cookies (PECR Reg.6) `[PECR-REG.6]`. Legitimate interests is NOT a valid basis for cookies under PECR — consent is required.
> - **Email or SMS direct marketing to individuals** (including sole traders / individual partners)? → Opt-in consent required for new prospects; soft opt-in for existing customers (PECR Reg.22) `[PECR-REG.22]`. Corporate subscribers have slightly different rules under Reg.23 `[PECR-REG.23]`.
> - **Automated marketing calls** (robocalls / recorded messages) to individuals? → Prior explicit consent required (PECR Reg.19) `[PECR-REG.19]`.
> - **Traffic data or location data** generated by electronic communications services? → Strict PECR rules on use and disclosure (PECR Regs.7-12) `[PECR-REG.7-12]`.

If any PECR check applies, flag the specific regulation, state what consent or notice mechanism is required, and add to the conditions table. PECR non-compliance is a separate ICO enforcement risk — the ICO enforces PECR independently from UK GDPR.

---

### Step 7: Privacy notice conflict check

Read `~/.claude/plugins/config/uk-legal-plugins/privacy-legal-uk/CLAUDE.md` → `## Privacy notice commitments`. Check the proposed activity against every stated commitment.

**Common conflicts to catch:**
- Notice says "we collect X, Y, Z" — this activity collects W. Notice update needed before launch, or stop collecting W. (UK GDPR Art.13/14 transparency obligation)
- Notice states a lawful basis — this activity uses a different one. Inconsistency in how you describe your lawful basis to data subjects.
- Notice says retention is "no longer than necessary for [purpose]" — this activity retains data for a new purpose that isn't stated.
- Notice names specific third-party categories — this activity introduces an unnamed category of recipient.
- Notice says "we do not transfer data outside the UK" — this activity uses a processor in a non-adequate country. Add the transfer mechanism.
- Notice covers a specified set of data subject rights — this activity creates a new data category that the rights process wasn't built for.

If a direct conflict exists → **STOP**. Not "proceed with caution" — the notice conflict has to be resolved (notice update or activity redesign) before this proceeds. Proceeding with a processing activity that contradicts the privacy notice is a transparency failure under UK GDPR Art.5(1)(a).

---

### Step 8: Classification and output

```
---

### Bottom line
[DPIA required / Mandatory DPIA required / Proceed — one-sentence why]

---

**ACTIVITY:** [State the processing activity as understood]

**CLASSIFICATION:** [PROCEED / DPIA REQUIRED / DPIA MANDATORY / STOP]

**House trigger met?** [Yes / No]
**Art.35(3) mandatory DPIA trigger?** [Yes — [specific trigger] / No]
**ICO high-risk list trigger?** [Yes — [specify] / No / Could not confirm — verify current ICO list]
**Lawful basis identified?** [Yes — [basis] / Unclear — needs determination in DPIA / No — STOP]
**Art.9 / Art.10 condition identified?** [Yes — [condition] / N/A / No — STOP]
**Children's Code check?** [Applicable — [conditions] / Not applicable — [reasoning] / Unclear — [review]]
**PECR check?** [PECR applies — [specific regs] / No PECR implications identified]
**Privacy notice conflict?** [None / Yes — [specific conflict]]

**Reasoning:**
[1-3 sentences.]

---

*If DPIA REQUIRED or DPIA MANDATORY — conditions before proceeding:*

| Requirement | Owner | Done? |
|---|---|---|
| [e.g., DPIA — full Art.35 format] | [Privacy counsel / DPO] | ☐ |
| [e.g., Legitimate Interests Assessment (if LI basis)] | [Privacy counsel] | ☐ |
| [e.g., DPO consultation (Art.35(2) — mandatory DPIA track)] | [DPO] | ☐ |
| [e.g., Prior ICO consultation (Art.36) if residual high risk] | [DPO + GC] | ☐ |
| [e.g., Vendor DPA (Art.28) in place] | [Privacy / Legal] | ☐ |
| [e.g., Privacy notice update before launch] | [Privacy counsel] | ☐ |
| [e.g., PECR-compliant consent mechanism built and tested] | [Product] | ☐ |
| [e.g., Children's Code compliance assessment] | [Privacy / Product] | ☐ |
| [e.g., IDTA / UK Addendum in place for international transfer] | [Privacy / Legal] | ☐ |
| [e.g., Data subject rights process covers new data category] | [Privacy / Product] | ☐ |

**Next step — offer to continue:**

After presenting a DPIA REQUIRED or DPIA MANDATORY result, always end with:

> "Want me to start the DPIA now? I can run the intake questions and produce the assessment document without you needing to run a separate command."

If they say yes, load the `dpia-generation` skill and continue in the same conversation.

If they say no: `Run /privacy-legal-uk:dpia-generation [activity] when ready.`
```

*If STOP:*

```
**Conflict / blocking issue:** [Specific privacy notice commitment, lawful basis gap, or PECR obligation in conflict]

**To proceed, one of these has to change:**
- [Option A — redesign the activity so it doesn't create the conflict]
- [Option B — update the privacy notice to cover this processing (requires review of whether the update is itself consistent with lawful basis and UK GDPR Art.5 principles)]
- [Option C — for lawful basis gap: identify an applicable basis and document it before proceeding]
```

---

### Step 9: Cross-plugin handoffs

**AI governance handoff:** If the activity involves an AI system making or influencing decisions about individuals (including profiling and automated decision-making):

> "This activity involves AI decision-making. Automated decision-making producing legal or similarly significant effects requires a mandatory DPIA under UK GDPR Art.35(3)(a). An AI impact assessment may also be required. Use `/ai-governance-legal:aia-generation [activity]` to run that in parallel — they are not substitutes. The ICO has issued AI-specific DPIA guidance; verify against current ICO guidance `[ICO-GUIDANCE]`."

**Product counsel handoff:** If this is a new product feature or launch:

> "If this is part of a product launch, loop in product counsel. Use `/product-legal:launch-review` — it will detect the privacy component and route to this plugin."

Only flag handoffs that are actually relevant. Don't append both as boilerplate.

---

## Batch triage

If the user presents a feature list, roadmap, or backlog — summary table first, then expand each non-PROCEED entry:

| # | Activity | Classification | Key condition / blocker |
|---|---|---|---|
| 1 | [activity] | 🟢 Proceed | — |
| 2 | [activity] | 🟡 DPIA required | LIA needed; vendor DPA not in place |
| 3 | [activity] | 🟠 DPIA mandatory | Art.35(3)(a): automated decisions re employees |
| 4 | [activity] | 🔴 Stop | No lawful basis identified for special category data |

---

## Edge cases and failure modes

**"It's anonymised" doesn't automatically mean PROCEED.**
Ask how it's anonymised and whether re-identification is realistically possible given the dataset. Pseudonymised data is still personal data under UK GDPR (Recital 26). Apply the motivated intruder test (ICO anonymisation guidance).

**"We already do something similar" isn't a triage.**
Existing processing that was never assessed doesn't grandfather new processing. If the new activity is materially different in scale, purpose, or data category, triage it fresh.

**"Just a pilot" doesn't skip triage.**
A pilot that touches real personal data is subject to the same triggers. Apply the same classification.

**"The vendor handles all the privacy."**
Vendor handles the infrastructure. You're still the controller determining the purposes. An Art.28 DPA is required. Triage still applies.

**Inferred data and derived attributes count.**
If the activity generates inferred data about individuals (e.g., a behavioural score, a predicted preference, a risk rating), treat the inferred attribute as personal data for triage purposes. Where the inferred data is special category (e.g., inferred health status, political opinions), Art.9 conditions are required.

**Children's Code: "we don't have under-18 users."**
If the service has not implemented age verification, the ICO's position is that services accessible to children are likely to be accessed by children — intention is not the test. Consider whether age verification is in place and effective. If not, apply the Children's Code. `[ICO-GUIDANCE]`

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced.
