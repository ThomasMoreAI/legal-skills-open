---
name: subpoena-triage-bossmann007
title: /subpoena-triage
description: Triage a determinação de exibição de documento por terceiro (CPC art. 401) or intimação de testemunha (CPC art. 455) served on the company — the Brazilian analogs to a US subpoena — classify it, analyze scope/burden/privilege, cross-check the portfolio, and produce an objections framework, compliance plan, and deadline calendar. Use when the user says "recebemos uma intimação/ordem de exibição", "fomos intimados como terceiro", or shares an intimação, ofício de autoridade, or third-party document request to evaluate.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/subpoena-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: en
---

# /subpoena-triage

> **Note on terminology.** This skill keeps the US name "subpoena" because that's the plugin's file/command name, but the underlying instrument doesn't exist the same way in Brazilian procedure. The real analogs are **intimação para exibição de documento por terceiro** (CPC art. 401 — a third party is ordered by the court to exhibit a document or thing) and **intimação de testemunha** (CPC art. 455 — witness summons for the audiência). There is no free-standing objection/compliance regime issued directly by counsel as in FRCP 45 practice — the order comes from the juízo, and objection is made to the court, not to the issuing lawyer. Brazil also has no grand jury; the closest analog for urgent criminal-side escalation is an intimação/exibição issued in the context of an **inquérito policial** or **ação penal**, and that still gets flagged for immediate escalation to a criminal defense lawyer (advogado criminalista) — the escalation behavior is the same even though the US institution ("grand jury") doesn't exist here.

1. Read the intimação/ordem from provided path.
2. Classify (exibição-terceiro-civil / testemunha-terceiro / parte / CID-equivalente-regulatória / inquérito-penal).
3. If inquérito policial / ação penal → stop, escalate per `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`. Otherwise continue.
4. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for cross-check. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → landscape, privilege conventions, escalation norms.
5. Follow the workflow and reference below.
6. Extract key fields, analyze scope/burden/privilege, produce objections framework + compliance plan + deadline calendar.
7. Write `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[slug]/triage.md`. Copy or link the intimação/ordem to `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[slug]/incoming.[ext]`.
8. Hand off: `/legal-hold --issue` if hold not in place; `/matter-intake` if materiality warrants; `/matter-briefing [slug]` if party-related intimação in existing matter.

---

# Triage de Intimação/Ordem de Exibição de Terceiro

## Purpose

These orders arrive with deadlines. The failure modes: missing the deadline, over-producing (waiver of sigilo, burden we should have objected to), under-producing (multa / desobediência exposure), or missing the window to impugnar. This skill classifies, analyzes, and produces a compliance plan with objections framework.

## Jurisdiction assumption

The rule cited in Step 0 is the operative one for this order in this forum. Practice varies materially: which CPC article applies (art. 401 exibição de terceiro vs. art. 455 intimação de testemunha), local provimentos, the vara/comarca's practice, and whether the matter is civil, trabalhista, or penal all change objection deadlines, escopo, requisitos de sigilo, and who bears costs. Every rule output here is a starting-point heuristic — confirm currency and the local variant before asserting in writing. [model knowledge — verify]

## Side context

This skill is inherently defensive — an order has been directed at the recipient and the posture is respond/object/comply. Read `## Side` in the practice profile. If the user's default side is **plaintiff**, note that receiving such an order is common for plaintiffs too (intimação de testemunha, third-party requests directed at the plaintiff's own records) but the framing here is always "order directed at us, how do we respond." If the user is **defense** (typical), the framing aligns with the default. If the matter has a different posture than the default (e.g., defense practitioner receiving an order in a matter where they're pro se for a family member), prompt the user to confirm posture before proceeding.

## Load context

- The intimação/ordem document (user provides path or drops it in-session)
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — for related matter lookup and legal hold status
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → landscape (regulators we deal with), house privilege conventions, escalation norms

## Workflow

### Step 0: Research the applicable rule

**Before analyzing this order, research the applicable rule of civil procedure for the forum (CPC art. 401 for exibição by a third party, or art. 455 for intimação de testemunha, conforme a natureza da diligência) and observe the modalidades de citação/intimação (CPC arts. 269-275). Identify: prazos, requisitos de forma, requisitos de sigilo/exibição, and who bears costs. Cite with pinpoint references. Verify currency — rules and local variants change. Flag orders arising in an inquérito policial or ação penal for immediate criminal-counsel escalation.**

**No silent supplement.** If a research query to the configured legal research tool (JusBrasil, Escavador, PJe, or firm platform) returns few or no results for the forum's rule, variant, or pinpoint, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / forum / variant]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) stop here. Which would you like?" A lawyer decides whether to accept lower-confidence sources; the skill does not decide for them.

**Source attribution.** Tag every rule reference, case, statute, and regulation in the triage output with where it came from: `[JusBrasil]`, `[Escavador]`, `[PJe]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for citations from web search; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied (e.g., from the order or prior matter work). Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags — they are counsel's fastest signal about which citations to verify before asserting in objections or filings.

### Step 1: Classify

These orders come in flavors with different rules; confirm the specifics against the rule you just researched:

- **Exibição de documento por terceiro, civil (CPC art. 401)** — we're not a party to the litigation; the court has ordered us, as a third party, to exhibit a document or thing. Usual objection categories: relevance, burden, sigilo profissional/legal, alcance territorial.
- **Intimação de testemunha (CPC art. 455)** — someone wants an employee to testify at the audiência. Scope, relevance, burden; possible impugnação; witness prep required.
- **Intimação em matéria própria (parte)** — we ARE a party; this is a regular procedural act in litigation we're tracking. Treat as normal case management, not inbound — it should map to an existing matter.
- **CID-equivalente regulatório** — ofício/requisição de CVM, BACEN, CADE, ANPD, Ministério Público, or other regulator. Different rules, different posture; often more deferential but also more consequential.
- **Inquérito policial / ação penal** — criminal. Escalate immediately to advogado criminalista; different skill path (outside this skill's scope — flag for escalation).

### Step 2: Extract key fields

- **Issuing authority** — court (which), agency (which), counsel (if civil)
- **Issuing party** — who requested (if civil)
- **Case / matter caption** — the litigation we're being asked about
- **Document categories sought** — numbered list
- **Testimony topics** (if depo) — Rule 30(b)(6) designations
- **Deadline for response/objection** — date served + computing the response window per applicable rule
- **Production date** — date by which documents must be produced
- **Geographic scope** — custodians, locations, systems implicated
- **Custodian of record designation** — who at the company is the witness/signatory

### Step 3: Portfolio cross-check

- **Party-related intimação → related to existing matter:** verify the caption matches a matter in `_log.yaml`. If yes, route to that matter's workflow; this triage is informational.
- **Third-party order → caption we don't recognize:** capture the parties; log as standalone inbound.
- **Multiple orders from same case:** flag coordinated issuance; a single response strategy may apply.

### Step 4: Analyze scope, burden, privilege

**Scope / relevance**
- Do the categories map to actual documents we plausibly have?
- Is any category a fishing expedition (overbroad, untethered to claims/defenses of the underlying case)?
- Place of compliance / geographic reach — apply the researched rule; limits differ by subpoena type (trial vs. document vs. deposition).

**Burden**
- Custodians implicated, systems searched, time period
- Estimated volume (rough: small / medium / large / extreme)
- Cost — third-party responders may have cost-shifting available; check the researched rule.

**Sigilo profissional / privilege**
- Sigilo profissional do advogado (CPC art. 404; Estatuto da OAB art. 7º, XIX) likely implicated? (Almost always yes for anything legal-related; often yes for communications involving in-house or outside counsel.)
- Other confidentiality grounds — segredo industrial/comercial, dados sensíveis (LGPD), sigilo bancário/fiscal se aplicável
- A justificativa de recusa de exibição will likely be required — flag the format per `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` (see `/litigation-legal:privilege-log-review`)

**Other objection grounds**
- Confidentiality — protective order needed?
- Duplicative — do they already have this from another party?
- Not possessed — we don't have what they're asking for (document with specificity)
- Improperly served — check the researched rule's service requirements

### Step 5: Objections framework

Draft a structured objections outline — not the final objections letter, but the outline of what objections apply and why. The user (often with outside counsel) finalizes.

Each objection:
- Legal basis — cite the pinpoint from the rule researched in Step 0
- Specific application to this subpoena (which categories, which custodians)
- Strength (strong / reasonable / weak)

### Step 6: Compliance plan

Even when objecting, we often produce some of what's requested. Plan:

- **Scope of likely production** — after objections, what we'd produce
- **Custodians to search** — names and systems
- **Date range**
- **Review protocol** — who reviews for privilege (us, outside counsel, contract reviewers)
- **Production format** — per the subpoena or per negotiated protocol (TIFF+load file, native, PDF)
- **Privilege log requirements** — format, fields

### Step 7: Deadlines

Use the deadlines identified in the Step 0 research. Note that objection deadlines often run from the EARLIER of the compliance date or a fixed number of days after service — do not default to a single number without checking the applicable rule and local variant.

- **Response deadline** — per researched rule; note if user needs more time (meet-and-confer to extend is standard)
- **Objection deadline** — per researched rule (federal / state rule + any local variant)
- **Production date** — if no objections succeed
- **Motion to quash window** — if pursuing that path, timing is critical

Calendar all of them. Immediate action item.

### Step 8: Write triage

Output: `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[slug]/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# Subpoena Triage

> **NOT A SUBSTITUTE FOR OUTSIDE COUNSEL.** This is a structured classification and scoping read to support fast decisions on deadlines, holds, and engagement. Every rule reference is a starting-point heuristic; jurisdiction-specific analysis, objections finalization, motions practice, and merit calls on privilege require licensed counsel familiar with the forum. Engage outside counsel for any subpoena above routine third-party document scope.

**Slug:** [slug]
**Served:** [YYYY-MM-DD]
**Served on:** [entity / registered agent]
**Incoming file:** [path]
**Classification:** [third-party-docs / third-party-depo / party / CID / grand-jury]

---

## Key fields

- **Issuing authority:** [court/agency]
- **Issuing party:** [name]
- **Case caption:** [caption]
- **Response deadline:** [date]
- **Production date:** [date]
- **Motion-to-quash window:** [date range]

## Categories sought (summary)

[numbered list, concise]

## Custodians / systems likely implicated

[list]

---

## Portfolio cross-check

**Related matter:** [slug or "none"]
**If party subpoena:** [routed to existing matter or new matter?]
**If third-party:** [standalone inbound]

---

## Scope & burden analysis

**Scope:** [relevance assessment by category]
**Burden estimate:** [small / medium / large / extreme — with reasoning]
**Geographic reach issues:** [any]

## Privilege analysis

*Privilege scoping is a first-pass read; final call is counsel's, not this skill's.*

**Attorney-client / work product likely implicated:** [yes/no + which categories] `[SME VERIFY]`
**Other privileges:** [sigilo profissional do advogado (Estatuto OAB art. 7º), segredo de justiça (CPC art. 189), sigilo bancário/fiscal (LC 105/2001), segredo industrial, dados protegidos pela LGPD] `[SME VERIFY]`
**Privilege log format required:** [per `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`]

---

## Objections framework

*Every row below requires `[SME VERIFY]` before asserting in writing — jurisdiction, rule currency, waiver risk.*

| Objection | Legal basis | Applies to | Strength | SME verified? |
|---|---|---|---|---|
| Relevance | [rule] | [categories] | [strong/reasonable/weak] | [ ] |
| Burden | [rule] | [categories] | | [ ] |
| Privilege | A/C, WP | [all producing docs] | strong (always) | [ ] |
| Duplicative | [rule/doctrine] | [if applicable] | | [ ] |
| [other] | | | | [ ] |

---

## Compliance plan (if responding)

- **Scope of likely production:** [after objections]
- **Custodians / systems:** [list]
- **Date range:** [range]
- **Review protocol:** [who, how]
- **Production format:** [format]
- **Privilege log:** [format, est. entries]

---

## Deadlines (calendar these)

*All deadlines below come from the Step 0 rule research. `[SME VERIFY]` confirms the rule, variant, and computation for this forum and this subpoena type — state variants and local rules differ.*

- **Response deadline:** [date] `[SME VERIFY]`
- **Objection deadline:** [date] — cite: [rule + pinpoint] `[SME VERIFY]`
- **Meet-and-confer by:** [date] (typically before objection deadline) `[SME VERIFY]`
- **Production date:** [date]

---

## Immediate actions

- [ ] Legal hold issued — [yes/no] — if no, run `/legal-hold [slug] --issue` with subpoena scope
- [ ] Outside counsel engaged — [yes/who/TBD]
- [ ] Meet-and-confer scheduled — [date]
- [ ] Matter created in log — [yes/no/TBD — usually yes for anything above the smallest third-party docs subpoena]
- [ ] Insurance / cost-shifting analysis — [if burden is large]
- [ ] Internal escalation — [who]

---

## Recommendation

[Two paragraphs: what to do. Objection posture. Production posture. Whether outside counsel handles objections or we do. Whether to move to quash.]

---

## Citation verification

Every rule reference, case, statute, and regulation in this triage — including the Step 0 research citations, objection bases, and the sigilo/exibição format pointer — is AI-generated and unverified. Before relying on any cite (especially in objections, an impugnação, or correspondence with the issuing party/juízo), run a verification pass against a legal research tool (JusBrasil, Escavador, PJe, or your firm's platform) for accuracy, good law status, and local variants. Fabricated or misquoted citations in filed documents can trigger a finding of **litigância de má-fé** (CPC arts. 79-81) against the party and, for the lawyer, potential disciplinary exposure under the Estatuto da OAB (Lei 8.906/1994) art. 34 — the closest Brazilian analogs to US "Rule 11"-style sanctions for misrepresenting the record to a court. Source tags on each citation (e.g., `[JusBrasil]`, `[web search — verify]`) show where it came from; `verify` tags carry higher fabrication risk and should be checked first.
```

### Step 9: Hand off

**Before responding to the order (apresentando impugnação, exhibiting documents, appearing to testify, or any substantive response to the issuing party or juízo):** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Responding to this order has legal consequences — missing a deadline risks multa/desobediência, over-producing waives sigilo, under-producing risks sanctions. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the order type, issuing authority, deadlines, scope of what's sought, objections framework and strength, sigilo and burden issues, proposed response posture, what could go wrong, what to ask the attorney.]
>
> If you need to find a licensed attorney in your jurisdiction: the OAB seccional's referral service (or your jurisdiction's equivalent) is the fastest starting point.

Do not proceed past this gate without an explicit yes. Triage, scoping, and internal calendaring do not require the gate — the response to the issuing authority does.

- If classified as **inquérito policial / ação penal** → stop, flag for escalation per `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`, do not proceed with standard triage.
- If classified as **CID-equivalente regulatório**: flag that regulator-specific norms apply; recommend outside regulatory counsel.
- Otherwise: offer to create a matter (usually yes — these orders are almost always material enough to track).
- If a legal hold isn't issued with the order's scope, hand off to `/legal-hold --issue` immediately.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Draft the final objections letter/petição.** Produces the framework; the impugnação is drafted by user + outside counsel (future: a dedicated objections-draft skill).
- **File the impugnação or agravo.** Surfaces the option; the motion is legal work that requires jurisdiction-specific analysis.
- **Validate rules across jurisdictions.** The Step 0 research produces the operative rule for this order; the skill doesn't independently confirm currency or local variants. Flag for counsel verification before acting.
- **Handle inquérito policial / ação penal escalations.** Escalates to criminal counsel. This is outside the triage scope.
