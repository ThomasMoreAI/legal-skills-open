---
name: fto-triage-bossmann007
title: 'Fto triage'
description: Freedom-to-operate triage — a structured first look at potentially blocking patents, not an FTO opinion. Use when a product, process, or feature is being evaluated for blocking patents, when asked whether anything stops a launch, or to build a claim-chart first pass against the most plausible patents before patent counsel review. This skill never concludes a product is clear to launch.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ip-legal/skills/fto-triage
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: ip
language: en
---

# /fto-triage

**This is not a freedom-to-operate opinion.** A formal FTO opinion requires a
comprehensive search, full claim construction, and element-by-element
infringement analysis by registered patent counsel or Agente da Propriedade
Industrial. Patent infringement under Brazilian law (Lei 9.279/1996) is
assessed under art. 210's "greatest of" damages formula — infringer's gain,
patentee's loss, or reasonable royalty; there is no treble-damages or
willfulness-multiplier equivalent. A "no obvious blocking patents" result from
this skill means the triage didn't find one — it does not mean the product is
clear.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal:cold-start-interview`.
2. Follow the workflow below.
3. Run intake (product/process, technical detail, jurisdictions, known patents,
   timing).
4. Run a preliminary patent search if a connector is available (Solve
   Intelligence Patents, or other patent-research MCP). Otherwise say
   so in the output and proceed with the patents the user has supplied.
5. For the 2–5 most plausible patents, build a claim-chart first pass against
   each independent claim — element by element. Literal read first; flag
   doctrine-of-equivalents separately; flag indirect / divided infringement.
6. List open questions a real FTO study would resolve (enforceability,
   prosecution history, IPR outcomes, license availability, enforcement
   history of the assignee).
7. Write the triage memo to the matter folder or practice outputs folder. Apply
   the work-product header per role.
8. End with recommended next steps, a willfulness note (knowledge of specific
   patents factors into willfulness if the company proceeds without further
   counsel review), and the non-lawyer gate if the role is non-lawyer.

This skill never concludes that a product is clear to launch. If uncertain,
flag — patent counsel decides.

## Examples

```
/ip-legal:fto-triage "an on-device speech recognition model for consumer wearables, US launch first"
```

```
/ip-legal:fto-triage
```

---

## THIS IS NOT A FREEDOM-TO-OPERATE OPINION

**The loudest guardrail in the plugin. Say this at the top of every output. Do
not drop it. Do not soften it. Do not let the reader skim past it.**

> **This is not a freedom-to-operate opinion.** An FTO opinion is a professional
> legal judgment, usually by an Agente da Propriedade Industrial or registered
> patent attorney (Lei 9.279/1996, art. 216), based on a comprehensive search,
> full claim construction, and an element-by-element infringement analysis
> against each claim of each relevant patent. This triage is a structured first
> look at what might be out there. A "no obvious blocking patents" result means
> the triage didn't find one — it does not mean the product is clear. For
> BR-designated patents, infringement remedies (losses and damages, seizure,
> destruction) are governed by Lei 9.279/1996, arts. 183–210 `[verify]` — there
> is no US-style treble-damages structure, but proceeding with knowledge of a
> specific patent still affects the damages calculation and can support a
> bad-faith finding `[verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`. For US-designated patents in
> scope, willful infringement can triple damages under 35 U.S.C. § 284 — see
> the jurisdiction-specific note below. The decision to launch, make, use,
> sell, or import is a business decision informed by a formal FTO study and
> counsel's judgment — not by this triage. An Agente da Propriedade
> Industrial, registered patent attorney, or foreign patent counsel (as the
> jurisdiction requires) evaluates before anyone relies on this for a product
> decision.

Under-flagging a blocking patent is a one-way door — a product launched, a
perícia técnica a year later, perdas e danos (LPI art. 210) and an injunction
on the table. Over-flagging is a
two-way door — the attorney narrows the list in a read-through. Stay on the
two-way door side. Always.

### A note on willfulness / má-fé

Reading this triage is reading something about patents. Reading something about
patents can, in some circumstances, factor into a willfulness analysis down the
road. In the US, this is the § 284 willfulness doctrine. Under Brazilian law
(Lei 9.279/1996), there is no direct willfulness-enhancement doctrine tied to
patent damages the way § 284 works, but proceeding with actual knowledge of a
specific patent is still relevant: it can support a *litigância de má-fé*
characterization in later litigation, and knowledge of the patent bears on the
losses-and-damages calculation under art. 210 (the greatest of: the infringer's
gain, the patentee's actual loss, or a reasonable royalty) `[model knowledge —
verify]`. This is one reason the output is marked as privileged when a lawyer is
using it, and why the non-lawyer output is framed as research to take to
counsel. Do not discuss specific patents surfaced by this triage outside
privileged channels.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

Patent FTO matters are particularly common candidates for **clean-team** or
**heightened** confidentiality at matter-open. Respect the matter's confidentiality
marking from `matter.md`.

---

## Load the practice profile first

Before running triage, read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Pull:

- **Role** from `## Who's using this` (lawyer vs. non-lawyer changes the
  work-product header and the non-lawyer gate below).
- **Registered in** and **enforce where** from `## IP practice profile` and
  `## Enforcement posture` (useful for defensive-portfolio cross-check and for
  jurisdiction defaults).
- **Patent OC** from `## IP practice profile` → `Outside counsel roster` for
  the routing step.
- **Integrations** from `## Available integrations` — specifically Solve
  Intelligence, or any patent-research MCP. Determines what searches
  are available.
- **Decision posture** from `## Decision posture on subjective legal calls` —
  this skill never concludes "does not infringe."

If `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` contains `[PLACEHOLDER]` or `[Your Company Name]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run the FTO triage normally using these generic defaults: middle risk appetite, lawyer role, US jurisdiction, no playbook (do the full analysis rather than matching against a position list). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/ip-legal:cold-start-interview` to get output calibrated to YOUR practice — your playbook, your jurisdiction, your risk appetite. 2 minutes."

---

## Intake

Ask in a single batch:

> I'll run an FTO triage. A few questions first:
>
> 1. **Product, process, or feature.** What's being made, used, offered for
>    sale, sold, or imported? Describe it plainly — the technical essence, not
>    the marketing pitch.
> 2. **Technical detail.** Any architectural diagrams, claim-relevant specs, a
>    public product page, or a spec document you can share? (The more detail,
>    the more real the triage.)
> 3. **Jurisdictions.** Where will it be made, used, sold, offered for sale,
>    imported? Each act is separately relevant — in Brazil under Lei
>    9.279/1996 art. 42 `[verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]`, in the US under
>    35 U.S.C. § 271. I'll default to Brazil if you don't specify, and flag
>    if a foreign jurisdiction (US, EU, etc.) looks like it's actually in
>    scope from your description.
> 4. **Known patents.** Are there patents already on your radar — a competitor's
>    portfolio, a known SEP pool, an NPE letter, something an engineer
>    mentioned?
> 5. **Timing.** How close is this to launch? If it's months out, the triage
>    is early and design-around is on the table. If it's already shipping,
>    we're in cover-our-downside mode.

Wait for the answer. If the description is vague ("an AI agent," "a database"),
push once:

> Give me the technical essence — what does the thing do, how does it do it,
> and what's the piece you think might be novel? Patent claims live at that
> level.

---

## Scope — utility patents only

**This skill analyzes utility patents.** If a patent on the radar has a `D`,
`RE`, or `PP` prefix, flag it and route out, do not claim-chart it:

- **`D` (design patent, US) / desenho industrial (BR, INPI registration
  prefix `DI`).** Different test entirely. In the US: ordinary observer under
  *Egyptian Goddess, Inc. v. Swisa, Inc.*, 543 F.3d 665 (Fed. Cir. 2008) (en
  banc), overall ornamental appearance, no claim chart. In Brazil: industrial
  design registration under Lei 9.279/1996 arts. 94–121 protects the
  ornamental/visual form, examined for novelty and originality rather than
  claims, with a 10-year term (renewable up to 25 years) `[model knowledge —
  verify]`. Route to the `infringement-triage` design-patent / desenho
  industrial branch and to design counsel. **Design registrations are not
  analyzed in this FTO triage** — a design overlap must be flagged as a
  separate workstream.
- **`RE` (reissue).** Treat as a utility patent with added §252 intervening-
  rights and recapture-rule flags.
- **`PP` (plant patent).** Route to plant-patent counsel; out of scope.

Also cross-flag **trade dress**: if the product's appearance is the risk,
the same facts may be a §43(a) product-configuration claim that requires
secondary meaning (*Wal-Mart Stores, Inc. v. Samara Bros., Inc.*, 529 U.S.
205 (2000)) and non-functionality (*TrafFix Devices, Inc. v. Marketing
Displays, Inc.*, 532 U.S. 23 (2001)). Flag as a parallel track.

---

## Search

### Default jurisdiction — Brazil (INPI)

Unless the intake names a non-BR jurisdiction, default the search to
BR-designated patents (national filings and PCT national-phase entries at
INPI). **INPI is the primary source of record for BR patents** — its
search system (Busca de Patentes, e-INPI) and the *Revista da Propriedade
Industrial* (RPI) are the authoritative record of filing, publication,
grant, annuity payment, and any nullity/administrative proceedings on a
BR-designated patent `[model knowledge — verify]`. Treat USPTO/EPO records
as authoritative only for US/EP-designated patents that are actually in
scope alongside or instead of the BR filing.

### What the user has connected

Read `## Available integrations`:

- **Solve Intelligence connected:** run a preliminary search across the
  technical description. Note the date of the search, the query used, the
  jurisdictions covered, and any date window (current in-force patents; recent
  published applications).
- **INPI e-Patentes / Busca de Patentes available (directly or via MCP):**
  use it as the primary source for BR-designated patents. Note the search
  date, query, and RPI issue number checked.
- **Patent-research MCP (Google Patents Public Datasets, PatSnap
  export, EPO Espacenet): available:** use it — Espacenet and Google Patents
  both index BR filings via the INPI feed, but a hit there should still be
  cross-checked against e-INPI/RPI for current status, since third-party
  indexes lag `[model knowledge — verify]`.
- **None of the above:** explicitly say so. Do not infer patents from model
  knowledge and present them as search results.

### Fallback when no patent database is connected

Write this exact statement in the output (adapt the named databases to the
jurisdictions actually in scope):

> **No patent database search was run.** This triage did not hit INPI
> e-Patentes / Busca de Patentes, the *Revista da Propriedade Industrial*,
> Solve Intelligence Patents, USPTO Patents Full-Text, EPO Espacenet,
> Google Patents, PatSnap, or any other patent corpus. A structured search
> across the jurisdictions in scope is required before relying on this triage
> for any launch decision. The analysis below is limited to patents and
> applications the user has named or that come up in the conversation.

Then proceed. The claim-chart-first-pass work below is still valuable — just
label the scope honestly.

### Supplementary signals (not a substitute)

If available and the user allows, sweep for non-patent signals that flag a
patent concern:

- **Competitor patent filings** around the product area (INPI RPI for BR;
  USPTO/EPO filings for foreign-designated competitors).
- **Known NPE / patent-troll targeting** of the technology class. In the US
  this concentrates in specific districts (e.g., Eastern District of Texas /
  Delaware / Western District of Texas); NPE activity against BR-based
  companies is comparatively rare but not unheard of — check for both.
- **Standards-essential declarations** (IEEE, ETSI, 3GPP) if the product touches
  a relevant standard — these bind regardless of jurisdiction.
- **Reported litigation.** For BR patent disputes: **JusBrasil**, **Escavador**,
  and **PJe** (Processo Judicial Eletrônico — federal and state court dockets,
  including the specialized IP courts in São Paulo and Rio de Janeiro
  `[model knowledge — verify]`) are the primary litigation-search options —
  use whichever the practice profile has connected `[JusBrasil]` / `[Escavador]`
  / `[PJe]` per the CLAUDE.md tag vocabulary. For US litigation exposure on a
  US-designated patent: CourtListener / RECAP, Unified Patents, Lex Machina.

Each signal is a reason to look harder, not a patent hit. Mark them as signals
in the output, not as identified patents, and tag the source per the CLAUDE.md
tag vocabulary (`[JusBrasil]`, `[Escavador]`, `[PJe]`, `[INPI]`, etc.).

---

## For each relevant patent found or supplied

Capture:

- **Patent number** (with application number if different) and **jurisdiction**
- **Title**
- **Assignee and inventors**
- **Priority date and issue date**
- **Expiration date.** For a BR patent: term is 20 years from the filing date
  (invention patents) or 15 years from filing (utility models), per
  Lei 9.279/1996 art. 40. The sole paragraph of art. 40 originally guaranteed
  a *minimum* term of 10 (invention) or 7 (utility model) years from grant when
  examination ran long — but the STF declared that minimum-term guarantee
  unconstitutional in ADI 5.529 (May 2021), so it no longer applies to grants
	  issued after that ruling. `[verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm; https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=465506]` Confirm the actual
  expiration in **e-INPI / RPI**, not by calculating from the priority date
  alone — the filing date that starts the clock, any divisional filings, and
  any annuity lapse all affect the real date. For a US-designated patent in
  scope: expiration per USPTO PAIR / PatentCenter, checking term adjustments
  (PTA), term extensions (PTE), and terminal disclaimers. For an EP-designated
  patent: EPO Espacenet / national register of the designated state.
- **Annuity / maintenance fee status — in-force status.** BR patents are kept
  alive by annual **anuidades** (retribuições anuais) starting from the 3rd
  year of the filing date and payable every year thereafter for the life of
  the patent, with a grace period (currently understood as up to 6 months
	  with surcharge) before lapse for non-payment `[verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]` —
  a materially different schedule from the US 3.5/7.5/11.5-year fixed
  maintenance-fee points (Lei 9.279/1996 arts. 84–87 govern the anuidade
  regime; verify current fee schedule and grace period directly against
  INPI). If a BR patent has lapsed for unpaid anuidade (caducidade
  administrativa) and the grace period has passed without payment or
  restoration, it is not a bar — but confirm the lapse in e-INPI, since
  reinstatement windows sometimes apply. If a US patent in scope has failed a
  3.5/7.5/11.5-year maintenance fee, it's expired and not a bar (confirm in
  PatentCenter).
- **Claim count — independent and dependent**
- **Independent claims as issued** (and any relevant amended claims from
  post-grant proceedings)
- **Related proceedings** — IPRs, PGRs, reexaminations, litigation history,
  PTAB outcomes
- **File wrapper highlights** — prosecution disclaimers, amendments that
  narrowed the claims, statements about scope

**Do not supplement silently.** If a search surfaces a patent, attribute the
result. If the user mentioned a patent, say that. Never invent a patent
number, never "fill in" a claim element the file doesn't support, never
imagine an expiration date. If annuity/maintenance status isn't available,
write "anuidade / maintenance fee status not verified from search result —
confirm in e-INPI (BR) or PatentCenter/PAIR (US) before relying on in-force
status."

---

## Claim-chart first pass

This is the core of the triage. Pick the patents with the most plausible read
on the product — usually the 2–5 with the closest technical mapping — and walk
each independent claim element-by-element.

**For each selected patent, write out one claim chart per independent claim:**

| Claim element | Does the product practice this? | Basis |
|---|---|---|
| "A [preamble phrase]" | [yes / no / possibly / depends on construction] | [one sentence — what in the product maps; what doesn't; what's ambiguous] |
| "comprising [element 1]" | [yes / no / possibly] | [mapping or gap] |
| "wherein [element 2]" | [yes / no / possibly] | [mapping or gap] |
| [continue for every element] | | |

**Rules for the chart:**

- **Every element matters.** A claim is infringed only if the accused product
  practices every element of at least one claim (all-elements rule). Missing one
  element literally means no literal infringement on that claim. Do not skip.
- **Doctrine of equivalents is a separate pass.** First chart literal
  infringement. Then, for any "no" elements, note whether a DOE read is
  plausible (insubstantial differences / function-way-result). Flag DOE
  analysis as requiring attorney judgment — prosecution history estoppel and
  claim vitiation are common bars and the triage does not adjudicate them.
- **Claim construction is the attorney's job.** Where a term could be
  construed narrowly or broadly and the answer changes the infringement read,
  flag the term and note both constructions. Do not pick one silently.
- **Indirect infringement (induced, contributory) and divided infringement**
  are flags only. Do not attempt a full analysis; note that these may apply and
  require patent counsel.

> **Patent systems differ by jurisdiction — the claim-chart mechanics below
> (all-elements rule, element-by-element mapping) are broadly portable, but
> the surrounding doctrine is not.** For a BR-designated patent, run the
> chart against the Brazilian framework:
> - **Brazil (INPI / Lei 9.279/1996):** infringement analysis still proceeds
>   element-by-element against the granted claim as issued (arts. 41–42), but
>   the applicable damages regime is art. 210 (greatest of infringer's gain,
>   patentee's loss, or reasonable royalty) rather than US §284/§289; there is
>   no direct equivalent to the US treble-damages willfulness enhancement
>   `[verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]`. Prosecution-history estoppel and DOE exist
>   in BR practice in less codified form than in the US and are decided
>   case-by-case by the courts (patent litigation in Brazil runs through the
>   ordinary federal/state judiciary — specialized IP chambers exist in
>   São Paulo and Rio de Janeiro — rather than a dedicated patent court)
>   `[unverified: not found in primary source]`. Flag DOE and estoppel reads as attorney
>   judgment calls, same as for the US, but do not import the US doctrinal
>   tests (function-way-result, *Festo*) without confirming they apply.
> - **United States:** all-elements rule, doctrine of equivalents,
>   prosecution history estoppel, §284/§289 damages — apply when a
>   US-designated patent is in scope alongside or instead of the BR filing.
> - **Germany:** Utility models (Gebrauchsmuster), the Schneidmesser/Kunststoffrohrteil questions for DOE, bifurcated validity/infringement proceedings.
> - **China:** Utility models (shiyong xinxing), CNIPA examination, different claim construction.
> - **Japan:** Utility models, JPO examination, a narrower DOE.
> - **Europe (unified patent court):** UPC procedure as of 2023.
>
> When multiple jurisdictions are in scope: "This chart maps the claim
> elements against the product; the doctrine that decides close calls
> (equivalents, estoppel, indirect infringement) is jurisdiction-specific. A
> product made in Brazil and sold in the US needs INPI/BR analysis for the
> BR-designated patent and USPTO/§284 analysis for the US-designated one —
> not one chart doing both. I can flag the issues the element mapping
> surfaces, but the infringement and validity calls require
> [jurisdiction]-specific review by counsel qualified in that jurisdiction."

**Decision posture:** per the practice profile, this skill never concludes "no
infringement." Either:

- "Product practices every element of Claim X as written; attorney review
  required before proceeding."
- "One or more elements are not clearly present; attorney review required to
  assess literal infringement and doctrine of equivalents."
- "Claim construction is dispositive on element [Y]; attorney construction
  required before proceeding."

---

## Open questions

Every patent surfaced in the triage should produce a list of open questions
that a real FTO study would answer. Examples:

- Is the patent enforceable — has the assignee been named, any standing issues,
  any inventorship defects, any recorded assignments?
- What did the applicant say about term [X] in prosecution, and does that
  limit the claim?
- Has this claim been the subject of an IPR or reexamination — what did the
  PTAB say about scope or validity?
- Is there a license already available (standards pool, patent marking, open
  patent non-assertion commitment)?
- What's the real-world enforcement history of this assignee?

List them plainly.

---

## Recommended next steps

Bucket by what the triage found:

- **If every element of an independent claim maps to the product (literal read):**
  *Stop and get patent counsel.* Options typically include formal FTO opinion,
  design-around, license, challenge validity (IPR/PGR), or (rarely) proceed at
  risk. The choice is a business decision informed by counsel.
- **If elements cut both ways or claim construction is dispositive:**
  Full FTO study by registered patent counsel. Do not launch on this triage.
- **If the patent appears expired, abandoned, or unenforceable:** Attorney
  confirms the in-force status — the triage does not.
- **If no patents were identified in the search but no database access
  existed:** Formal search is the next step, not a launch decision.
- **Always:** flag the knowledge risk. If the triage surfaces a specific
  patent, the company now has knowledge of it. For US-designated patents,
  proceeding without further analysis can support a §284 willfulness finding.
  For BR-designated patents, proceeding with knowledge still bears on the
  art. 210 damages calculation and can support a *litigância de má-fé*
  characterization `[verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`. Counsel — Agente da
  Propriedade Industrial / patent attorney for BR, registered patent
  attorney for US — should document the path forward.

---

## Output format

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` `## Outputs`. Mark the document as privileged if the role is lawyer; see the non-lawyer gate below if not.

```markdown
[WORK-PRODUCT HEADER]

# FTO Triage — First Pass (NOT AN OPINION)

**This is not a freedom-to-operate opinion.** A formal FTO opinion requires a
comprehensive search, full claim construction, and element-by-element
infringement analysis by an Agente da Propriedade Industrial / registered
patent attorney qualified in each jurisdiction in scope. A "no obvious blocking
patents" result means the triage didn't find one — it does not mean the product
is clear. Willful infringement of a US-designated patent can triple damages
under 35 U.S.C. § 284; infringement of a BR-designated patent is assessed
under Lei 9.279/1996 arts. 183–210 `[verify]`, a different remedies regime. A
qualified patent professional in each relevant jurisdiction evaluates before
anyone relies on this for a product decision.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Subject

- **Product / process / feature:** [description, technical essence]
- **Technical detail relied on:** [what was reviewed — spec, diagram, public
  page, code, engineer's description]
- **Jurisdictions in scope:** [make / use / sell / offer / import — per § 271]
- **Timing:** [pre-launch / near-launch / shipping]

## Search scope

- **Databases searched:** [INPI e-Patentes / Busca de Patentes / RPI —
  Solve Intelligence / Google Patents / Espacenet / PatSnap — or "no
  database search run"]
- **Query / approach:** [query text, technology classes, keywords, classifications]
- **Date / date window:** [search date; in-force patents + applications
  published since YYYY-MM-DD; RPI issue number if BR search]
- **Jurisdictions covered by the search:** [list — BR unless stated otherwise]
- **What wasn't searched:** [named-assignee sweeps, SEP declarations, NPE
  portfolios, design patents (desenho industrial), foreign equivalents — as
  applicable]

*If no database search was run:* **No patent database search was run.** This
triage did not hit INPI e-Patentes / Busca de Patentes / RPI, Solve
Intelligence Patents, USPTO Patents Full-Text, EPO Espacenet, Google Patents,
PatSnap, or any other patent corpus. A structured search across the
jurisdictions in scope is required before relying on this triage for any
launch decision.

## Patents identified

| Patent | Jurisdiction | Assignee | Priority / Issue | Expiration | In-force? (anuidade/maintenance) | Source |
|---|---|---|---|---|---|---|
| [number] | [BR/US/EP/...] | [assignee] | [dates] | [date] | [yes/no/unverified] | [search result link, `[INPI]`/`[JusBrasil]`/`[Escavador]`/`[PJe]` tag, or "user-supplied"] |

## Claim charts — first pass

### [Patent number] — independent Claim [N]

> "[Exact text of Claim N]"

| Element | Practiced by the product? | Basis |
|---|---|---|
| [element 1] | [yes/no/possibly] | [mapping or gap] |
| [element 2] | [yes/no/possibly] | [mapping or gap] |

**Literal read:** [every element maps / one or more elements do not clearly
map / claim construction is dispositive on element [Y]]

**Doctrine of equivalents (flag only):** [DOE read plausible on element [Y] —
attorney construction required / not plausible on the surfaced elements /
prosecution history suggests estoppel]

**Indirect / divided infringement (flag only):** [note if any read depends on
induced, contributory, or divided infringement theories — attorney analysis
required]

*(Repeat for each independent claim of each selected patent.)*

## Open questions

- [question 1]
- [question 2]

## Signals (not confirmed patents)

- [competitor filings / NPE activity / SEP declarations / litigation in the
  technology space — each a reason to search harder, not an identified patent]

## Recommended next steps

- [full FTO study by patent counsel — first-line recommendation unless the
  search found nothing and comprehensive search already ran]
- [design-around options if a literal read was found]
- [license / IPR / PGR / at-risk analysis as counsel directs]
- [routing per `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` —
  patent OC named in the practice profile]

## Willfulness / má-fé note

This triage surfaces specific patents. For a US-designated patent, proceeding
without further counsel review after this knowledge can support a willfulness
finding and enhanced damages under § 284. For a BR-designated patent,
proceeding with this knowledge bears on the losses-and-damages calculation
under Lei 9.279/1996 art. 210 and can support a *litigância de má-fé*
characterization `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm; https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]` — there is no direct BR
equivalent to the US treble-damages enhancement, so do not describe BR
exposure in those terms. The path forward should be documented by qualified
patent counsel in each jurisdiction in scope; the business decision to
launch, design around, or license is informed by a formal FTO opinion and
counsel's judgment, not by this triage.

## Citation verification

Every patent number, claim quote, date, and prosecution fact in this memo must
be verified against the authoritative source before relying on it — **e-INPI
/ RPI** for BR-designated patents, USPTO PatentCenter / PAIR for
US-designated patents, EPO register / national equivalent for other
jurisdictions. Claim quotes are the most common error site — a single word
changes the analysis. Do not cite a result you cannot open.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Launching, continuing to
> sell, or investing in this product based on this triage alone has legal
> consequences — including strict liability for patent infringement, with
> enhanced damages for willfulness. Patent counsel needs to evaluate before
> you move.
>
> Here's a brief to bring to an attorney — it'll cut the time the conversation
> takes:
>
> [Generate a 1-page summary: the product description, the jurisdictions in
> scope, the search run (and what wasn't searched), the patents surfaced and
> the claim-chart-first-pass reads, the open questions, and the three
> questions to ask the attorney.]
>
> If you need to find a qualified patent professional: for Brazilian patent
> work, representation before INPI is through an **Agente da Propriedade
> Industrial** (Lei 9.279/1996, art. 216) — the INPI registry lists qualified
> agents, and the OAB (Ordem dos Advogados do Brasil) can refer a patent
> litigator for court proceedings `[unverified: LPI Art. 216 estabelece que os atos são praticados por partes ou procuradores qualificados perante o INPI; não confirma sigilo agente-cliente — https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]`. For US patent
> work, a registered patent attorney or patent agent is required (not every
> lawyer is registered — the USPTO Office of Enrollment and Discipline
> maintains a directory). For other jurisdictions, use the relevant patent
> office register (EPO, UK IPO, etc.). Your professional regulator's referral
> service is a starting point (OAB in Brazil, state bar in the US, SRA/Bar
> Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/
> Canada/Australia, or your jurisdiction's equivalent); specifically ask for
> registered patent counsel or an Agente da Propriedade Industrial as the
> jurisdiction requires.

Deliver the full triage memo alongside the brief. Do not withhold the analysis.
Flag that the triage itself is a privileged research document and should not
be forwarded to non-attorney third parties.

---

## Output location

If matter workspaces are enabled and a matter is active, write the output to
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`
and surface the path.

Append a one-line entry to the matter's `history.md` if a matter is active.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Issue an FTO opinion.** Ever. The loudest guardrail in the plugin.
- **Construe claims.** Where construction is dispositive, it flags the term and
  both plausible constructions. It does not pick one.
- **Adjudicate validity.** It may note known PTAB proceedings; it does not
  opine on novelty, obviousness, § 112, § 101, or enablement.
- **Draft patent claims.** This plugin does not go there; route to prosecution
  counsel.
- **Assess damages exposure.** Damages modeling is an expert's job.
- **Handle trade-secret or trademark analysis** — use `/ip-legal:infringement-triage`
  with the right mode.
- **Quote outputs to counterparties or non-privileged audiences.** This is a
  privileged research document.

---

## Tone

Technically precise. Element-by-element. Every flag is specific to a claim
element or a known patent. No hedging prose in the body — the guardrails at
the top and bottom do the scope work, and the analysis does the analysis. The
reader should leave knowing what the triage looked at, what it didn't, and
what the next step is.
