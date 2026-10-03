---
name: worker-classification-bossmann007
title: /worker-classification
description: Classify a proposed worker engagement — employee, IC, temp, or vendor — by running the applicable jurisdiction tests and flagging misclassification gaps between the intended arrangement and what the facts actually support. Prospective use only. Use when someone says "we want to bring on a contractor", "is this a vendor or a temp", "how should we classify this person", or describes a proposed working arrangement.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/worker-classification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: en
---

# /worker-classification

Runs the applicable classification tests for the jurisdiction and flags where
the proposed arrangement doesn't match the structure you're trying to use.
Prospective only — for existing relationships, consult counsel.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, escalation table.
2. Run the full workflow below.
3. If the attorney provides details upfront, extract what's available and ask
   only about the gaps. Do not re-ask information already provided.

## Examples

```
/employment-legal:worker-classification
We want to bring on a data scientist for 6 months, working out of our
São Paulo office, using our tools, embedded in our analytics team.
```

```
/employment-legal:worker-classification
Is our recruiter contractor arrangement okay? She works exclusively for
us, sets her own hours, uses her own laptop, project fee per placement
(paid via her own MEI).
```

```
/employment-legal:worker-classification
(skill will ask for details)
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The most expensive classification decision is the one nobody made consciously.
Someone describes what they want ("a contractor"), the engagement starts, and
two years later the facts look like employment. This skill walks the applicable
tests on the proposed arrangement before it starts — and tells you when what
you're describing doesn't match the structure you're trying to use.

This skill teaches the reasoning pattern. It does not state the law. Every
test formulation, statutory citation, threshold, and carve-out must come from
current research for the applicable jurisdiction.

## Prospective-only hard gate — run BEFORE intake

**This skill analyzes a PROPOSED engagement before the work starts.** Before any substantive intake (Step 1), ask:

> Has this work already started? Is the worker currently engaged, or have they been performing work under this arrangement for any period of time (days, weeks, months, or years)?

If the answer is yes — the engagement already exists, in any form, for any duration — **STOP**. Do not proceed to Step 1 intake. Classifying an existing arrangement is not a planning exercise; it's a liability assessment with remediation implications: verbas rescisórias retroativas (aviso prévio, horas extras, férias + 1/3, 13º, FGTS + multa de 40%), INSS back-exposure (employer + employee contributions, juros e multa), unreported eSocial obligations, benefits that were denied (vale-transporte, vale-refeição), and — with ongoing work in a core-business pejotização fact pattern — the prospective exposure of letting it run another day. `[model knowledge — verify]` That analysis is privileged, led by counsel, and coupled with a remediation plan.

Output exactly this block and wait for a response:

> **Out of scope — existing arrangement.**
>
> This skill is designed to analyze a worker engagement *before it starts*, so the classification choice informs how to structure the contract and operations. You've described an arrangement that already exists. Analyzing an existing engagement retroactively is a different exercise: reclassification risk assessment coupled with remediation planning — verbas rescisórias retroativas exposure (aviso prévio, 13º salário, férias + 1/3, FGTS + multa de 40%) `[model knowledge — verify]`, INSS back-exposure (contribuições patronal e do trabalhador, com possível incidência de juros e multa) `[model knowledge — verify]`, eSocial retroactive-reporting exposure, and prospective restructuring. That work should be privileged, led by an attorney, and likely coupled with outside-counsel review given the dollar and enforcement exposure, including exposure to fiscalização do trabalho (Ministério do Trabalho e Emprego / auditores fiscais) `[model knowledge — verify]`.
>
> Recommended next step: escalate per your config's escalation table (for retroactive classification, this typically routes to GC + outside employment counsel). I've flagged this for escalation routing.
>
> **If you want to proceed with the prospective-style analysis anyway for planning purposes, say "proceed anyway" — but understand:**
>
> - The output is NOT a remediation plan and should not be treated as one.
> - The output does NOT scope verbas rescisórias retroativas, INSS/FGTS back-exposure, or eSocial correction exposure for the period already worked.
> - The output does NOT substitute for the reclassification-risk assessment that this fact pattern actually calls for.
> - The output will carry a prominent banner reflecting this scope mismatch, and the consequential-action gate will require an attorney yes before the analysis is treated as reliable.
>
> Only say "proceed anyway" if you're using this skill for forward-looking planning (e.g., "if we were structuring this fresh today, how should we think about it?") and you have a separate plan for the remediation question.

**Only proceed past this gate with an explicit `"proceed anyway"` (or equivalent user instruction). A hesitant "I guess" does not count — re-prompt. If the user proceeds anyway, prepend this banner to every output of this skill for this session:**

```
⚠️ SCOPE MISMATCH — OUT-OF-SCOPE USE
This skill analyzes prospective worker engagements. The arrangement here
already exists. This output is the prospective-style analysis the user
requested for planning purposes only — it is NOT a remediation plan, does
NOT scope existing verbas rescisórias retroativas / INSS / FGTS exposure, and does
NOT substitute for the reclassification-risk assessment this fact pattern
requires. The remediation question has been flagged for escalation to
counsel per your config's escalation table.
```

If the answer to "has this work already started?" is no (the engagement is genuinely prospective, not yet begun), proceed to load context.

---

## Load context

Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, any classification history or
prior settlements noted, escalation table, and any house classification
policy the team has recorded.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`).

## Workflow

### Step 1 — Information gathering

Ask all of the following in a single block. Do not drip questions one at a
time. Briefly explain why you're asking — attorneys answer better when they
understand what the question is testing.

> To run the right classification tests I need to understand the proposed
> arrangement in detail. Please answer as many of these as you can — the more
> complete the picture, the more accurate the analysis:
>
> **The work**
> - What will this person actually do day-to-day?
> - Is this work part of your company's core business, or peripheral to it?
>   (e.g., a software engineer at a software company = core; an IT
>   contractor at a law firm = more peripheral)
> - Is this a defined project with a clear end, or ongoing indefinite work?
> - How specialized is the skill? Does this person have expertise your team
>   doesn't?
>
> **Control**
> - Who sets their hours and schedule — them or you?
> - Where will they work — your office, their location, or either?
> - Will you direct how they do the work (methods, process, sequence), or
>   just what the end result should be?
> - Will they supervise any of your employees?
>
> **Economics**
> - How will they be paid — hourly, daily, or fixed project fee?
> - Will you provide equipment, tools, or software, or do they use their own?
> - Do they work for other companies, or will this be exclusive?
> - Will they bear any financial risk — can they profit beyond the fee, or
>   lose money on the engagement?
> - Do they have their own business entity (MEI, EIRELI, Ltda, sole trader) they'll invoice through — i.e., is this a pejotização arrangement?
>
> **The arrangement**
> - How do you want to structure this — direct contractor, staffing agency
>   temp, or vendor/SOW (company-to-company)?
> - If staffing agency: who pays the worker — the agency or you? Who controls
>   day-to-day work?
> - Will there be a written contract? Do you have a template in mind?
> - Roughly how long is the engagement — weeks, months, over a year?
> - Will they work alongside your employees doing similar work?
>
> **Purpose(s) of the classification**
> - What legal purposes does the classification need to serve — eSocial
>   registration, INSS contributions, FGTS deposits, CLT wage/hour
>   protections (horas extras, férias, 13º), benefits eligibility (vale-
>   transporte, vale-refeição)? Under CLT the classification test itself
>   (art. 3º) is generally unified across these purposes, unlike the
>   multi-purpose, multi-test US framework — but confirm this in research
>   for the current jurisdiction and note any purpose-specific carve-outs.
>   `[model knowledge — verify]`
>
> **Jurisdiction**
> - Where will this person physically perform the work? (Confirm Brazilian
>   state/município, or whether the work is cross-border — a foreign worker
>   under Brazilian control may still trigger CLT exposure.)

Wait for responses before proceeding. If the attorney can't answer certain
questions, note the gaps — they affect the analysis.

### Step 2 — Identify the applicable tests

> **Research the applicable tests before proceeding.** For the jurisdiction(s)
> and purpose(s) identified in intake, research the currently operative
> classification test(s). The core test under Brazilian labor law is the
> employment-relationship (relação de emprego) test of CLT art. 3º, which
> requires four cumulative elements: **subordinação** (the worker follows
> the company's direction and control), **pessoalidade** (the work must be
> performed personally, not delegable to a substitute), **não-eventualidade
> / habitualidade** (the work is ongoing/recurring, not a one-off), and
> **onerosidade** (the worker is paid for the work). If all four elements
> are present in fact, an employment relationship exists under CLT
> regardless of how the parties labeled or contracted the arrangement — the
> label the parties chose is not controlling; the primazia da realidade
> (primacy of fact over form) principle governs. `[model knowledge — verify]`
> Separately, research the **pejotização** doctrine: engaging a worker
> through their own legal entity (MEI, EIRELI, Ltda) specifically to avoid
> CLT protections, where the underlying facts still show subordinação,
> pessoalidade, habitualidade, and onerosidade, is treated by Brazilian
> courts (and, since the 2017 reforma trabalhista and Lei 13.467/2017's
> art. 442-B, subject to ongoing interpretive dispute) as a disguised
> employment relationship. `[model knowledge — verify]` Note that the
> validity of pejotização for genuinely autonomous, specialized, or
> highly-compensated professionals has been the subject of recent TST and
> STF jurisprudence (including debate over the scope and constitutionality
> of art. 442-B) — cite current case law and confirm currency, as this area
> has moved quickly. `[model knowledge — verify]` Cite the controlling
> statute, regulation, súmula, or case (CLT, TST súmulas/OJs, STF
> precedents). Note the effective date of each rule and whether it has been
> recently amended. Identify any carve-outs or exceptions that may apply
> (e.g., trabalho autônomo genuíno, profissional liberal, representante
> comercial autônomo under Lei 4.886/1965, contrato de prestação de
> serviços B2B). Verify currency. If you are uncertain about the current
> state of the law in any jurisdiction, flag it for attorney verification —
> do not state a test you haven't confirmed.

If `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` records the company's house classification policy, apply it
first and flag any tension with the researched test.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a jurisdiction-and-purpose combination, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / purpose / test]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation — each classification test, statute, regulation, or case — with where it came from: `[JusBrasil]`, `[Escavador]`, `[PJe]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the attorney supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 3 — Apply the researched tests to the facts

For each test identified in Step 2, apply it to the intake facts. Score each
factor or prong explicitly — do not summarize. The attorney needs to see which
factors are clean and which are problems.

Use a structure like the one below, but populate the *factors* from the
researched test, not from this file:

```
Test: [name of test, per research]
Purpose: [what this test governs — eSocial / INSS / FGTS / CLT wage-hour / etc.]
Source: [pinpoint cite to statute/regulation/case]
Currency: [verified as of date]

| Factor / prong | Intake facts | Signal / pass-fail |
|---|---|---|
| [Factor 1 from researched test] | [from intake] | [direction or pass/fail] |
| [Factor 2] | [from intake] | [direction or pass/fail] |
| ...                            |                |                   |

Structure of the test:
[How the test weighs factors — e.g., a multi-factor balancing test, or a
conjunctive test where each prong must be satisfied, or a hybrid. State this
from research, not from memory.]

Result under this test:
[Employee-leaning / IC-leaning / Fails prong X / Uncertain — contested prong]
```

Repeat for each applicable test.

**Notes on contested prongs.** Some prongs of some tests are heavily contested
in case law and fact-sensitive. Identify contested prongs explicitly — do not
paper over them. The fact that a test is stated does not mean its application
to these facts is settled; flag prongs that require attorney judgment or that
have generated recent litigation in the jurisdiction.

### Step 4 — Classify and flag gaps

**The classification call**

Based on the test results, state the most accurate classification for this
proposed arrangement:

- **Employee (CLT / carteira assinada):** Facts satisfy the four CLT art. 3º
  elements (subordinação, pessoalidade, habitualidade, onerosidade).
- **Independent Contractor (autônomo / pejotizado):** Facts support genuine
  autonomous status — no subordination, work is delegable or intermittent,
  worker bears real business risk — under CLT art. 3º and current
  pejotização jurisprudence. `[model knowledge — verify]`
- **Temp via staffing agency (trabalho temporário, Lei 6.019/1974):** Worker
  will be on the agency's payroll; company is the tomador de serviços —
  co-employment / vínculo direto risk exists if the company exercises
  day-to-day subordinating control or the engagement exceeds the statutory
  time limits. Research current Lei 6.019 limits and the applicable
  terceirização standard (including STF Tema 725 on lawful outsourcing of
  core activities) if relevant. `[model knowledge — verify]`
- **Vendor/SOW (contrato de prestação de serviços PJ):** Company-to-company
  engagement; worker is employed by the vendor entity — cleanest structure
  if facts support it, but still vulnerable to pejotização reclassification
  if the vendor entity is a single-person shell with no real autonomy.
- **Unclear / close call:** Facts cut both ways under one or more tests —
  state which test is the problem and why.

If different purposes point to different answers (e.g., defensible as
autônomo for FGTS/eSocial structuring purposes but the day-to-day facts
still show subordinação sufficient to fail CLT art. 3º), say so explicitly
and name the controlling purpose and jurisdiction.

**The gap analysis**

This is the most important output. Compare the intended structure against what
the facts actually support:

```
Intended structure: [what they said they want]
What the facts suggest: [what the researched tests say this actually is]

Gaps — where the arrangement doesn't match the intended structure:
🔴 [Factor]: [What they described] conflicts with [intended classification]
   because [specific researched test language + cite]. This is a significant
   misclassification risk if the engagement proceeds as described.
🟡 [Factor]: [What they described] is a weaker point under [test]. Not
   disqualifying alone, but combined with other factors increases risk.
✅ [Factor]: Supports [intended classification]. No issue.
```

**Escalation trigger**

Escalate per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` if any of the following, or any team-specific
triggers recorded in that config:
- The proposed work is core to the company's business (atividade-fim, not
  atividade-meio) and the worker will be engaged as pejotizado/autônomo — do
  not proceed without counsel review, given heightened reclassification risk.
  `[model knowledge — verify]`
- Prior misclassification settlement, autuação (labor-inspection citation),
  or reclamatória trabalhista noted in the config — heightened scrutiny
  applies.
- Worker will supervise employees or have significant budget authority.
- Engagement expected to exceed 12 months with no clear project endpoint.
- Any contested prong where the outcome changes the classification.

### Step 5 — Output

> **Research-connector pre-flight.** Before emitting the analysis, check whether a legal research connector is reachable for this session — JusBrasil, Escavador, PJe, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if no connector returns results in Step 2 (or none is configured at run time), record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; the highest-fabrication pinpoints in classification analyses are os requisitos do art. 3º da CLT (subordinação, pessoalidade, habitualidade, onerosidade), a distinção pejotização vs. autonomia real, e a jurisprudência do TST sobre o tema — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the output.

> **Jurisdiction assumption.** This analysis applies the tests operative in the jurisdiction(s) identified in intake. CLT art. 3º's four-element test is federal (national) in Brazil, but sector-specific statutes (e.g., Lei 6.019/1974 for trabalho temporário, Lei 4.886/1965 for representantes comerciais) and convenções/acordos coletivos can layer additional or divergent standards. If the work will be performed outside Brazil, or under a foreign-law arrangement, or if a new purpose is added later, this analysis may not apply as written. [verified: https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://www.planalto.gov.br/ccivil_03/leis/l6019.htm; https://www.planalto.gov.br/ccivil_03/leis/l4886.htm]

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Worker Classification Analysis
**Proposed arrangement:** [what they described]
**Jurisdiction:** [state/country]
**Purpose(s):** [eSocial / INSS / FGTS / CLT wage-hour / benefits]
**Tests applied:** [list, each with pinpoint cite and currency date]

---

### Bottom line

[Can you proceed / Need to fix X first / Stop — one-sentence why]

---

### Classification

**Closest classification:** [Employee / IC / Temp via agency / Vendor-SOW / Unclear]

[One paragraph summary of why — test results in plain language, tied to the
cited sources.]

---

### Test results

#### [Test name — per research]
Purpose: [...] | Source: [...] | Currency: [...]
[Scored table from Step 3]
**Result:** [Employee-leaning / IC-leaning / Fails prong X / Mixed]

#### [Additional researched tests — repeat the block]

---

### Gap analysis

[Flags as structured in Step 4 — 🔴 significant risks, 🟡 weaker points,
✅ clean factors]

---

### Escalation

[None needed | Escalate to [name] before proceeding — [reason]]

---

### Next steps

[If IC viable: "Proceed — ensure the written agreement reflects the terms that
support IC status under the researched test."]
[If gaps exist: "Address the following before using IC structure: [list]"]
[If agency/vendor is cleaner: "Consider restructuring as [agency/SOW] — here's
why it's cleaner for this fact pattern."]
[If escalation needed: "Do not proceed until counsel reviews the [specific
issue]."]
[If employee confirmed: "Classification confirmed as CLT employee — run
`/employment-legal:hiring-review` to review the contrato de trabalho, cláusulas
restritivas, and jurisdiction-specific requirements."]
[If IC confirmed: "Classification confirmed as autônomo/PJ — no CLT contract
review needed. Ensure the written contrato de prestação de serviços reflects
autonomy-supporting terms before the engagement starts."]
[If agency/vendor: "Engagement should be structured through [agency/vendor
entity] — coordinate with them on worker agreement. No `/hiring-review` needed."]
```

## Consequential-action gate (classify a worker)

**Before producing a "Proceed as IC / employee / agency / vendor" final recommendation:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Classifying a worker has legal consequences — misclassification (pejotização declarada disfarçada) exposes the company to verbas rescisórias retroativas, INSS/FGTS back-exposure, penalties, and reclamatória trabalhista risk. Have you reviewed this classification call with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - The arrangement (work, control, economics, structure) as described
> - Jurisdiction and which tests were applied
> - Test-by-test results with cites and currency
> - Gap analysis (🔴 / 🟡 / ✅) with the weak prongs called out
> - Open questions and what's unresolved
> - What could go wrong (the misclassification theory this arrangement most likely fails on; prior-audit/settlement overlay if any)
> - What to ask the attorney (is IC viable here; would restructuring through an agency or vendor remove the risk; what contract terms do we need to support the classification)
>
> If you need to find a lawyer: contact your local OAB (Ordem dos Advogados do Brasil) seccional for a referral service, or your jurisdiction's equivalent bar association if the engagement crosses borders.

Do not produce a final "IC viable" / "use this classification" output past this gate without an explicit yes. A marked-DRAFT analysis for attorney review is fine.

---

## What this skill does NOT do

- Analyze an existing relationship retroactively — this is prospective only.
- Draft the contractor agreement or SOW.
- Advise on remediation if misclassification has already occurred.
- State the law for any jurisdiction on its own — every test, factor, and
  carve-out must come from verified current research.
- Substitute for outside counsel on close calls — pejotização of core-business
  work, contested elements, and prior-audit/reclamatória situations should
  always get a human review before the engagement starts.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.
