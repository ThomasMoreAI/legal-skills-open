---
name: witness-summons-triage-uk-agents
title: /witness-summons-triage
description: Triage a witness summons or third-party disclosure order served on the company — classify it, analyse scope/burden/privilege, cross-check the portfolio, and produce an objections framework, compliance plan, and deadline calendar. Use when the user says "we got a witness summons", "third-party disclosure order", "served with a court order for documents", or shares a witness summons, third-party disclosure order, or regulatory notice to evaluate.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/witness-summons-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /witness-summons-triage

1. Read the witness summons or order from provided path.
2. Classify (third-party-docs / witness-summons-depo / party / regulatory-notice / criminal).
3. If criminal compulsion (e.g., serious fraud / police production order) → stop, escalate per `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. Otherwise continue.
4. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` for cross-check. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → landscape, privilege conventions, escalation norms.
5. Follow the workflow and reference below.
6. Extract key fields, analyse scope/burden/privilege, produce objections framework + compliance plan + deadline calendar.
7. Write `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/[slug]/triage.md`. Copy or link document to `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/[slug]/incoming.[ext]`.
8. Hand off: `/legal-hold --issue` if hold not in place; `/matter-intake` if materiality warrants; `/matter-briefing [slug]` if party to existing matter.

---

# Witness Summons and Third-Party Disclosure Order Triage

## Purpose

Witness summonses and third-party disclosure orders arrive with deadlines. The failure modes: missing the deadline, over-producing (LPP waiver, burden we should have objected to), under-producing (contempt exposure), or missing an application-to-set-aside window. This skill classifies, analyses, and produces a compliance plan with objections framework.

## UK procedural framework

In England & Wales, the mechanisms for compelling third-party evidence and documents differ from US subpoena practice:

- **Witness summons (CPR Part 34, r 34.2–34.7):** Issued by the court requiring a person to attend to give oral evidence or produce documents at trial or at a hearing. A witness summons to produce documents at trial is issued by the court; the recipient may apply to set it aside or vary it. Separate from the party disclosure regime.
- **Third-party disclosure (CPR 31.17):** An application by a party for an order requiring a non-party to disclose documents. The court may order disclosure if the documents are likely to support the case of the applicant or adversely affect the case of another party, and disclosure is necessary to dispose fairly of the claim or to save costs. Not automatic — requires a court order.
- **Norwich Pharmacal order:** A court order requiring a third party who has facilitated wrongdoing (innocently or otherwise) to disclose information enabling the applicant to identify the wrongdoer or obtain relief. A more powerful tool than CPR 31.17 in certain contexts.
- **Bankers Trust order / disclosure for asset tracing:** Specific form of third-party disclosure in fraud and asset-recovery contexts.
- **Regulatory notices and production orders:** FCA, CMA, ICO, SFO, HMRC, and other regulators have separate statutory powers to compel document production and information disclosure. These operate under different statutory frameworks from civil procedure and require specialist regulatory advice.
- **Criminal production orders (PACE / POCA):** Police and Criminal Evidence Act 1984 (Schedule 1), Proceeds of Crime Act 2002 — criminal compulsion; escalate immediately to criminal-law specialist.
- **Scotland:** Commission and diligence procedure (RPO / commission) under the Rules of the Court of Session or Sheriff Court Rules; no direct equivalent to CPR Part 34. Flag for Scottish solicitors.
- **Northern Ireland:** Rules of the Court of Judicature (NI); broadly similar to England & Wales but flag for NI-specific advice.

## Load context

- The document (user provides path or drops it in-session)
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` — for related matter lookup and legal hold status
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → landscape (regulators we deal with), house LPP conventions, escalation norms

## Workflow

### Step 0: Research the applicable rule

**Before analysing this document, research the applicable CPR Part, Practice Direction, and (for regulatory notices) the applicable statute. Identify: the procedural basis for the order/summons, applicable deadlines for compliance or challenge, any procedure for setting aside or varying, LPP protections available, and who bears costs. Cite with pinpoint references in OSCOLA format. Verify currency — CPR rules and statutory schemes change. Flag criminal production orders and serious regulatory notices for immediate specialist escalation.**

**No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, BAILII, legislation.gov.uk, or firm platform) returns few or no results for the applicable rule, variant, or pinpoint, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / forum / variant]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) stop here. Which would you like?" A solicitor or barrister decides whether to accept lower-confidence sources; the skill does not decide for them.

**Source attribution.** Tag every rule reference, case, statute, and regulation in the triage output with where it came from: `[uk-legal MCP]`, `[BAILII]`, `[legislation.gov.uk]`, `[gov.uk]` for citations retrieved from a legal research connector; `[web search — verify]` for citations from web search; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 1: Classify

Documents compelling third-party cooperation come in different forms with different rules; confirm the specifics against the rule you just researched:

- **Witness summons — documents (CPR r 34.2(4))** — a witness summons requiring production of documents at trial or hearing. We are not a party; someone wants our documents produced to the court. Consider: LPP, burden, relevance, application to set aside or vary (CPR r 34.3).
- **Witness summons — oral evidence (CPR r 34.2(1)–(3))** — a witness summons requiring attendance to give oral evidence. Scope, relevance, burden; possible application to set aside; witness preparation required.
- **CPR 31.17 third-party disclosure order** — a court order following an application by a party for disclosure. We are not a party; the order requires us to disclose specific documents. Challenge requires prompt action — the order has already been made.
- **Norwich Pharmacal order** — compulsion to identify a wrongdoer or provide information relating to wrongdoing. Specific legal framework; specialist advice usually required.
- **Regulatory notice / production order** — FCA (FSMA 2000, s 165/167), CMA (CA 1998, ss 26–28; Enterprise Act 2002, s 109), ICO (Data Protection Act 2018), SFO (Criminal Justice Act 1987, s 2), HMRC, Ofcom, or other regulator. **Each has its own statutory compulsion regime, LPP protections, and challenge procedure.** Treat as a separate category; recommend specialist regulatory counsel.
- **Criminal production order (PACE / POCA)** — criminal compulsion. **Escalate immediately to criminal-law specialist; this is outside the triage scope of this skill.**

### Step 2: Extract key fields

- **Issuing authority** — which court, which judge, which regulatory body
- **Requesting party** — who applied for the order (if civil)
- **Underlying case / matter caption** — the litigation or investigation
- **Document categories sought or witness topics** — numbered list
- **Compliance date** — date by which documents must be produced or witness must attend
- **Application-to-set-aside window** — time limit for challenging, if applicable
- **Geographic scope** — custodians, locations, systems implicated
- **Person/entity named** — who the order is addressed to

### Step 3: Portfolio cross-check

- **Party to existing matter → related to existing matter:** verify the caption matches a matter in `_log.yaml`. If yes, route to that matter's workflow; this triage is informational.
- **Third-party summons / order → underlying case we don't recognise:** capture the parties; log as standalone inbound.
- **Multiple orders from same case:** flag coordinated issuance; a single response strategy may apply.

### Step 4: Analyse scope, burden, privilege

**Scope / relevance**
- Do the categories map to actual documents we plausibly have?
- Is any category a fishing expedition (overbroad, untethered to issues in the underlying case)?
- Proportionality under CPR overriding objective — is the burden proportionate to the benefit to the proceedings?

**Burden**
- Custodians implicated, systems searched, time period
- Estimated volume (rough: small / medium / large / extreme)
- Cost — the court may order the requesting party to pay the witness's costs of complying (CPR r 34.7); check the researched rule.

**Legal professional privilege**
- LPP (legal advice privilege or litigation privilege) likely implicated? (Almost always yes for anything involving legal communications.)
- Other privileges or protections — confidentiality undertakings, data protection (UK GDPR), regulatory confidentiality
- LPP log will be required — flag the format per `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`

**Other objection grounds**
- LPP — confidential communications with solicitors/barristers
- Proportionality — CPR r 1.1(2)(c); disproportionate burden
- Confidentiality — protective order needed?
- Duplicative — does the requesting party already have this from another source?
- Not in possession — we do not have what they are asking for (state with specificity)
- Procedural defects — check the researched rule's service and application requirements; was proper notice given?

### Step 5: Objections framework

Draft a structured objections outline — not the final objections letter or application, but the outline of what grounds apply and why. The user (usually with external solicitors) finalises.

Each objection:
- Legal basis — cite the pinpoint from the rule researched in Step 0
- Specific application to this document (which categories, which custodians)
- Strength (strong / reasonable / weak)

### Step 6: Compliance plan

Even when objecting, we often produce some of what is requested. Plan:

- **Scope of likely production** — after objections, what we would produce
- **Custodians to search** — names and systems
- **Date range**
- **Review protocol** — who reviews for LPP (external solicitors, in-house, or both)
- **Production format** — per the order or agreed protocol
- **LPP log requirements** — format, fields, level of description

### Step 7: Deadlines

Use the deadlines identified in the Step 0 research. Compliance deadlines, application-to-set-aside windows, and any required prior-notice periods differ by document type and forum.

- **Compliance date** — per the order or summons; note if an application to set aside / vary is needed before that date
- **Application-to-set-aside window** — if pursuing that path, timing is often critical; the application should be made promptly
- **LPP log delivery date** — if separate from or earlier than production
- **Any agreed extension** — if negotiating with the requesting party's solicitors

Calendar all of them. Immediate action item.

### Step 8: Write triage

Output: `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/[slug]/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# Witness Summons / Third-Party Disclosure Order Triage

> **NOT A SUBSTITUTE FOR EXTERNAL SOLICITORS.** This is a structured classification and scoping read to support fast decisions on deadlines, preservation notices, and engagement. Every rule reference is a starting-point heuristic; jurisdiction-specific analysis, objections finalisation, applications to court, and merit calls on privilege require a licensed solicitor or barrister familiar with the forum. Engage external solicitors for anything above routine third-party document scope.

**Slug:** [slug]
**Served / received:** [YYYY-MM-DD]
**Served on:** [entity / registered address]
**Incoming file:** [path]
**Classification:** [third-party-docs-witness-summons / witness-summons-oral / CPR-31.17-order / Norwich-Pharmacal / regulatory-notice / criminal-production-order]

---

## Key fields

- **Issuing authority:** [court/regulatory body]
- **Requesting party:** [name]
- **Underlying case / investigation:** [caption or reference]
- **Compliance date:** [date]
- **Application-to-set-aside window:** [date range if applicable]
- **Specialist escalation required:** [yes/no — if regulatory or criminal]

## Categories sought (summary)

[numbered list, concise]

## Custodians / systems likely implicated

[list]

---

## Portfolio cross-check

**Related matter:** [slug or "none"]
**If party compulsion:** [routed to existing matter or new matter?]
**If third-party:** [standalone inbound]

---

## Scope & burden analysis

**Scope:** [relevance assessment by category]
**Burden estimate:** [small / medium / large / extreme — with reasoning]
**Proportionality issues:** [any — CPR r 1.1(2)(c)]

## LPP analysis

*LPP scoping is a first-pass read; final call is the solicitor's/barrister's, not this skill's.*

**Legal advice privilege likely implicated:** [yes/no + which categories] `[SME VERIFY]`
**Litigation privilege likely implicated:** [yes/no + which categories] `[SME VERIFY]`
**Other protections:** [data protection, confidentiality undertakings, regulatory] `[SME VERIFY]`
**LPP log format required:** [per `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`]

---

## Objections framework

*Every row below requires `[SME VERIFY]` before asserting in writing — jurisdiction, rule currency, waiver risk.*

| Objection | Legal basis | Applies to | Strength | SME verified? |
|---|---|---|---|---|
| Legal professional privilege | CPR 31.19 / common law LPP | [categories — all producing docs] | strong (always) | [ ] |
| Proportionality / burden | CPR r 1.1(2)(c) | [categories] | [strong/reasonable/weak] | [ ] |
| Relevance | [rule] | [categories] | | [ ] |
| Duplicative | [doctrine] | [if applicable] | | [ ] |
| Procedural defect | [rule] | [if applicable] | | [ ] |
| [other] | | | | [ ] |

---

## Compliance plan (if responding)

- **Scope of likely production:** [after objections]
- **Custodians / systems:** [list]
- **Date range:** [range]
- **Review protocol:** [who, how]
- **Production format:** [format]
- **LPP log:** [format, est. entries]

---

## Deadlines (calendar these)

*All deadlines below come from the Step 0 rule research. `[SME VERIFY]` confirms the rule, variant, and computation for this forum and this document type — rules and local directions differ.*

- **Compliance date:** [date] `[SME VERIFY]`
- **Application-to-set-aside-or-vary window:** [date range] — cite: [rule + pinpoint] `[SME VERIFY]`
- **LPP log delivery:** [date]
- **External solicitors briefed by:** [date — internal]

---

## Immediate actions

- [ ] Preservation notice issued — [yes/no] — if no, run `/legal-hold [slug] --issue` with summons/order scope
- [ ] External solicitors engaged — [yes/who/TBD]
- [ ] Application-to-set-aside assessed — [yes/no/TBD]
- [ ] Matter created in log — [yes/no/TBD — usually yes for anything above the smallest third-party document request]
- [ ] Cost-recovery analysis — [if burden is large: consider costs application under CPR r 34.7 or equivalent]
- [ ] Internal escalation — [who]

---

## Recommendation

[Two paragraphs: what to do. Objection posture. Production posture. Whether external solicitors handle the application/objections or we do. Whether to apply to set aside or vary.]

---

## Citation verification

Every rule reference, case, statute, and practice direction in this triage — including the Step 0 research citations, objection bases, and the LPP log format pointer — is AI-generated and unverified. Before relying on any cite (especially in an application, correspondence with the requesting party or the court, or an objections letter), run a verification pass against a legal research tool (uk-legal MCP, BAILII, legislation.gov.uk) for accuracy, currency, and local variations. Source tags on each citation (e.g., `[uk-legal MCP]`, `[web search — verify]`) show where it came from; `verify` tags carry higher fabrication risk and should be checked first.
```

### Step 9: Hand off

**Before responding to the summons or order (producing documents, attending to give evidence, or making an application — any substantive response to the court, the requesting party's solicitors, or the regulatory body):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Responding to a court order or witness summons has legal consequences — missing a deadline risks contempt of court, over-producing waives LPP, under-producing risks sanctions. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the document type, issuing authority, deadlines, scope of what is sought, objections framework and strength, LPP and burden issues, proposed response posture, what could go wrong, what to ask the solicitor/barrister.]
>
> If you need to find a licensed solicitor, barrister, or other authorised legal professional: the SRA (solicitors.lawsociety.org.uk) or Bar Standards Board (barstandardsboard.org.uk/find-a-barrister) for England & Wales; the Law Society of Scotland (lawscot.org.uk) for Scotland; the Law Society of Northern Ireland (lawsoc-ni.org) for Northern Ireland.

Do not proceed past this gate without an explicit yes. Triage, scoping, and internal calendaring do not require the gate — the response to the court or regulatory authority does.

- If classified as **criminal production order** → stop, flag for escalation per `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`, do not proceed with standard triage.
- If classified as **regulatory notice**: flag that regulator-specific norms apply; recommend external regulatory counsel as a priority.
- Otherwise: offer to create a matter (usually yes — witness summonses and third-party disclosure orders are almost always material enough to track).
- If a preservation notice is not issued covering the summons/order scope, hand off to `/legal-hold --issue` immediately.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the solicitor or barrister picks.

## What this skill does not do

- **Draft the final objections letter or application.** Produces the framework; the letter or application is drafted by user + external solicitors.
- **Make the application to set aside.** Surfaces the option; the application is legal work that requires jurisdiction-specific analysis.
- **Validate rules across UK forums.** The Step 0 research produces the operative rule for this document; the skill does not independently confirm currency or local directions. Flag for solicitor/barrister verification before acting.
- **Handle criminal production orders.** Escalates. This is outside the triage scope.
- **Assess regulatory powers.** Flags that specialist regulatory counsel is needed; does not purport to analyse the scope of FCA, CMA, ICO, SFO, or other regulator compulsion powers.
