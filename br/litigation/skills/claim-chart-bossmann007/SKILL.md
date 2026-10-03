---
name: claim-chart-bossmann007
title: 'Claim chart'
description: Build or review an element chart — a patent claim chart (infringement, invalidity, or review) or a civil element chart for any cause of action or defense — with every cell pin-cited and gap detection as the priority output. Use when the user asks for a claim chart, element chart, proof chart, infringement or invalidity contention, element-by-element mapping, or asks "what are we missing to prove [claim]".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/claim-chart
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: en
sources:
- title: Element templates
  path: references/element-templates.md
---

# /claim-chart

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, work-product header, decision posture, document storage.
2. If matter workspaces enabled, confirm or select the active matter; load `matter.md` (side, jurisdiction, phase, theory, pleadings).
3. Follow the workflow and reference below.
4. Mode selection:
   - `--patent` → patent claim chart. Require patent number and at least one asserted claim. Sub-modes: `--infringement`, `--invalidity`, `--review`.
   - `--civil` → civil element chart. Require the cause of action (or defense) and the side.
   - No flag → ask the user which.
5. For civil mode: consult `references/element-templates.md` in the skill directory for the baseline element list. Confirm the controlling pattern instruction or statute with the user before mapping.
6. For patent mode: parse asserted claims into elements, flag disputed terms for construction, apply any claim-construction ruling (interpretação de reivindicações, tipicamente via perícia técnica).
7. Map elements against the target (accused product / prior art / evidence corpus / chart under review). Every cell pin-cited. Apply the apostrophe-prefix neutralization before writing any cell value starting with `=`, `+`, `-`, `@`, tab, or CR.
8. Produce the gap list (civil) or needs-evidence list (patent) — the priority output.
9. Write markdown, CSV (values + `_sources` companion), and Excel or Sheets per user preference. Work-product header on every output.
10. Write to the matter's `claim-charts/` folder if a matter is active; otherwise the practice-level `claim-charts/` folder. Append a one-line entry to `history.md` if a matter is active.
11. Return a summary readout: claim(s), target(s), jurisdiction, phase, element counts by state, the gap list, file paths, and the reminder that every cell is a lead.

---

# Claim Chart

## Disclosed-document use restrictions

Before working with a set of litigation documents, ask: "Were any of these documents obtained through disclosure or discovery in legal proceedings?" If yes:

- **England & Wales (CPR 31.22):** Documents obtained through disclosure are subject to the implied undertaking — you may only use them for the purpose of the proceedings in which they were disclosed, unless the court grants permission, the disclosing party consents, or the document has been read in open court. Using them for a different matter, a different claim, or a commercial purpose without permission is a contempt.
- **US:** Protective orders and Rule 26(c) may impose similar restrictions. Check the order.
- **Other jurisdictions:** Similar restrictions commonly apply. Check the local rule.

Confirm: "This use is within the proceedings in which the documents were disclosed, or I have permission / consent, or the documents are now public." If not confirmed, flag it: "⚠️ Disclosed documents may have use restrictions. Confirm this use is permitted before proceeding."

## A CHART IS A DRAFT, NOT A FINDING OR A CONTENTION

**Put this at the top of every output. Do not drop it. Do not soften it.**

> This chart is a draft for attorney analysis and verification, not a filed contention, an MSJ brief, an opening statement, or a legal opinion. Every mapping is a lead the attorney must verify against the source. The elements listed come from the applicable law and doctrine, or the claim language as parsed — the **controlling** authority in the user's jurisdiction (a lei e a jurisprudência aplicáveis do STJ/TJ, o laudo pericial, ou a decisão de interpretação de reivindicações) may differ and always controls. Gap detection is a starting point for discovery or a motion; it is not a conclusion about the merits.

Under-flagging a gap is a one-way door — a complaint filed without plausibility on an element, an MSJ response served without evidence for a disputed element, or a case tried without proof of damages. Over-flagging is a two-way door — the attorney clears flags in review. The default is biased toward the two-way door.

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — especially the case theory, the pleading / complaint (for the elements actually alleged), the jurisdiction, any decisão de interpretação de reivindicações (perícia técnica) or stipulated constructions (patent mode), and the phase of the case. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<matter-slug>/claim-charts/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, work-product header, decision posture, document storage, case-theory scaffolding
- Active matter's `matter.md` — claims, defenses, side, jurisdiction, phase, theory
- For civil mode: the complaint or counterclaim (for the actually-pleaded counts), any answer (for the actually-pleaded affirmative defenses), the relevant pattern jury instruction source, and the governing statute if statutory. Also the evidence corpus — deposition transcripts, declarations, produced documents, expert reports.
- For patent mode: the patent, the asserted claims, the specification, prosecution history if available, the accused-product material or prior art reference, any decisão de interpretação de reivindicações (perícia técnica) or stipulated constructions.

If `CLAUDE.md` has `[PLACEHOLDER]` markers, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor risk calibration, landscape, and house style to your practice.
>
> **Two choices:**
> - Run `/litigation-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," build the claim chart normally using these generic defaults: middle risk appetite, lawyer role, US jurisdiction, no practice-level playbook (work from the matter's pleadings and the elements of the claims as pleaded). Tag the reviewer note and every row of the chart with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/litigation-legal:cold-start-interview` to get output calibrated to YOUR practice — your risk calibration, your landscape, your house style. 2 minutes."

**Conflicts gate — unbypassable.** Before building a claim chart, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build a claim chart on a matter that hasn't been intaken — the conflicts check is the gate."

Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the `_log.yaml` row this skill reads from.

---

## Mode selection

Ask at the top, before anything else:

> Which kind of chart?
>
> 1. **Patent claim chart** — element-by-element mapping of claim limitations against an accused product (`--infringement`), prior art (`--invalidity`), or another party's chart (`--review`). For patent contentions, IPR petitions / responses, FTO charts.
> 2. **Civil element chart** — elements of a cause of action (or affirmative defense) mapped against the evidence. For complaint plausibility checks, discovery planning, MSJ prep, order-of-proof outlines.

Plus intake (common to both):

- **Side.** Asserting or defending? (In civil mode this flips the burden; in patent mode it flips infringement/invalidity framing.)
- **Jurisdiction / forum.** Brazilian civil litigation has no civil jury — pattern jury instructions (CACI, NYPJI) don't exist here; the only jury is the Tribunal do Júri for certain criminal offenses (CF/88 art. 5º, XXXVIII), which is irrelevant to a civil or IP element chart. What actually varies: **comarca/vara competente** — territorial and functional competence under CPC arts. 42-53 (e.g., art. 46 domicílio do réu; art. 53 foros especiais — imóveis, alimentos, divórcio, etc.); and the **Justiça Estadual (TJ) vs. Justiça Federal (TRF) split**, which turns on the parties and matter involved (CF/88 art. 109 — União, autarquia ou empresa pública federal as party, or matters the Constitution assigns to federal jurisdiction). In patent mode specifically, note Brazil's de facto venue concentration: most patent and IP litigation runs through the **Varas Empresariais especializadas do TJRJ** (Rio de Janeiro), which developed the deepest IP docket and case law; and **INPI (Instituto Nacional da Propriedade Industrial) is a mandatory party** in nullity actions per Lei 9.279/1996 (LPI) art. 57 (patent nullity) and art. 175 (trademark nullity) — a chart or filing that omits INPI as a party in a nullity suit is procedurally defective. Flag which forum and which regime (estadual/federal) actually controls.
- **Phase.** Pre-filing, pleadings, discovery, MSJ, trial prep, post-trial. The chart is the same; the framing of the output changes.
- **Existing chart?** If `--review`, load it.

---

# MODE 1 — Patent claim chart

## Sub-modes

- `--infringement` — claim elements vs. accused product (PLR 3-1 infringement contentions, IPR/PGR response exhibits, complaint exhibits)
- `--invalidity` — claim elements vs. prior art (PLR 3-3 invalidity contentions, IPR/PGR petition exhibits, §102/§103 defenses)
- `--review` — audit a chart someone else produced

## Additional patent-mode intake

- **Patent number and asserted claims.** Which independent, which dependent. (Don't chart unasserted claims unless asked.) For a BR-designated patent, use the INPI registration/publication number by default; the USPTO number applies only when a US-designated patent is genuinely in scope.
- **Priority date.** For a BR-designated patent (default), the priority date fixes the novidade baseline under LPI arts. 11-15 (what counts as prior art / estado da técnica) and, where a foreign priority is claimed, the unionist priority under the Paris Convention (LPI art. 16) `[model knowledge — verify]`. There is no AIA/pre-AIA split in Brazilian practice — that dichotomy is a US statutory artifact. For a US-designated patent genuinely in scope, apply the §102 bar and the AIA/pre-AIA effective-filing-date regime as the explicit US fallback.
- **Existing constructions.** Brazilian civil procedure has no discrete claim-construction proceeding. Claim construction, where disputed, is developed through **perícia técnica** (expert examination, CPC arts. 464-480) conducted within the ação de nulidade or ação de infração — there is no separate pretrial claim-construction hearing or order. If a perícia has already produced a laudo pericial addressing claim scope, apply it the way a claim-construction ruling would be applied. For a US-designated patent genuinely in scope, apply any actual Markman order or stipulated constructions from that proceeding.

## Patent-mode workflow

### Step 1: Parse the claims

Parse asserted independent claims into numbered elements. Handle:

- **Preamble.** Note whether it's limiting — a question of claim construction (*Catalina Marketing Int'l, Inc. v. Coolsavings.com, Inc.*, 289 F.3d 801 (Fed. Cir. 2002)). Flag `preamble-limiting: unresolved` unless the construction order resolves it.
- **Transitional phrase.** "Comprising" (open) / "consisting of" (closed) / "consisting essentially of" (semi-open). Affects whether additional unrecited elements defeat infringement.
- **Elements** separated by commas / semicolons, numbered `[1a]`, `[1b]`, `[1c]`. Keep numbering stable — it's the chart's spine.
- **Means-plus-function (§112(f))** — every "means for [function]" or non-structural functional term. Scope is the structure disclosed in the spec plus equivalents. Cite corresponding structure by col./line. If the spec fails to disclose structure, flag `indefinite-112f`.
- **Markush groups, Jepson claims, product-by-process, method-step order dependencies** — flag with a note on unusual construction rules.
- **Dependent claims** — reference parent; chart only the additional limitations. **Execute, don't gesture.** If asserted claims include dependents, produce the actual additional-limitation rows for each dependent in Step 4 — do not emit a note that dependents "should be charted."
- **Structural-term cognates — default to `construction-dependent`.** For each element that recites a structural noun with a common cognate in the prior art of the field, default the row's state to `literal-construction-dependent` (not `literal`) unless the spec expressly defines the term or an existing decisão de interpretação de reivindicações forecloses the ambiguity. These are the terms most commonly disputed in perícia técnica — presuming a clean literal read under-flags the risk. Common cognate families to flag proactively:

  | Field | Cognate family (flag as `structural-term-cognate`) |
  |---|---|
  | Fasteners / anchors | barb / thread / projection / ridge / fin / tooth |
  | Fluidics / catheters | lumen / channel / bore / passage / conduit |
  | Mechanical housings | hub / boss / flange / collar / shoulder |
  | Fasteners / joints | socket / recess / pocket / cavity |
  | Electrical / electronic | contact / terminal / pad / lead |
  | Optical | lens / reflector / window / aperture |
  | Structural | wall / member / support / strut / rib |
  | Surfaces | surface / face / interface |

  This list is not exhaustive — if the claim recites a structural noun that could reasonably be read narrowly (pointed barb vs. any projection) or broadly (channel vs. any passage), flag `structural-term-cognate` in `_constructions` and default the row to `construction-dependent`. The attorney can demote it to `literal` after a decisão de interpretação de reivindicações or a definition in the spec forecloses the ambiguity.

Show the parse to the user. Confirm before mapping. A wrong parse poisons every row below it.

### Step 2: Claim construction check

**No separate claim-construction hearing under Brazilian civil procedure (default).** For a BR-designated patent, disputed claim terms are resolved through **perícia técnica** (CPC arts. 464-480) — a court-appointed expert (perito) examines the claim scope within the ação de nulidade or ação de infração, and the parties may name assistentes técnicos to contest the laudo. There is no discrete, bifurcated claim-construction hearing that precedes the infringement/validity merits the way a Markman hearing does in US practice `[model knowledge — verify]`. Flag disputed terms below as "pending perícia" rather than "pending claim construction" unless a US-designated patent is genuinely in scope.

Flag disputed terms:

- Coined terms or terms defined in the spec
- Terms with prosecution history (amendments, arguments, disavowals — *Phillips v. AWH Corp.*, 415 F.3d 1303 (Fed. Cir. 2005); *Festo* estoppel)
- Functional language ("configured to", "adapted to", "operable to")
- Relative terms ("substantially", "about") — definiteness risk under *Nautilus, Inc. v. Biosig Instruments, Inc.*, 572 U.S. 898 (2014)
- Computer-implemented terms — Alice / §101 exposure for invalidity

For each flagged term, state the construction(s) under which the mapping works and the construction(s) under which it fails. If a claim-construction ruling (laudo pericial / decisão de interpretação de reivindicações) exists, apply it. If briefing is underway, chart under each side's proposed construction.

### Step 3: Map

For each element, for each target:

1. **Find evidence.** Accused product: documentation, manuals, data sheets, source code, teardowns, deposition testimony, expert reports. Prior art: column/line for US patents, paragraph for published apps, page/figure for NPL. For prior art, flag whether the reference qualifies (§102(a)(1), (a)(2), (b); AIA vs. pre-AIA cutoffs). If prior-art status isn't obvious, mark `prior-art-status: needs-evidence`.
2. **Quote verbatim.** Character-for-character. No paraphrase. Cut at sentence boundaries and mark elision.
3. **Characterize the mapping.**

   | Mapping | Meaning | Where |
   |---|---|---|
   | `literal` | Claim language reads on the accused feature / prior-art disclosure | Both |
   | `literal-construction-dependent` | Literal under X; fails under Y | Both |
   | `doe` | Equivalent (function-way-result or insubstantial differences) | Infringement only |
   | `anticipation` | Every element in a single reference, arranged as claimed (*Net MoneyIN, Inc. v. VeriSign, Inc.*, 545 F.3d 1359 (Fed. Cir. 2008)) | Invalidity only |
   | `obviousness-combination` | Secondary reference supplies the missing element; motivation to combine required under *KSR Int'l Co. v. Teleflex Inc.*, 550 U.S. 398 (2007) | Invalidity only |
   | `partial` | Some of the element is present | Both |
   | `not-found` | Element not present | Both |
   | `needs-evidence` | Can't tell from available material | Both |
   | `construction-dependent` | Turns on how a disputed term is construed | Both |

4. **State per cell.** `mapped` / `mapped-doe` / `partial` / `not-found` / `needs-evidence` / `construction-dependent` / `anticipation` / `obviousness-combination`.
5. **Flag open questions.** "This maps if [X]. Need [teardown / source code / deposition / expert] to confirm."

**No silent supplement.** Thin documentation means `needs-evidence`, not extrapolation from similar products.

### Step 4: Dependent claims — execute, don't gesture

For each asserted dependent claim, produce an actual row (or set of rows) charting the additional limitation(s) against the target. The parent dependency is noted, and infringement / invalidity of the dependent requires the parent's. **Produce the rows, not a placeholder note that rows should be produced.**

If the user provided a list of asserted claims that includes dependents, the chart's output MUST contain rows for each of them. If the user gave only the independent claim and said "chart the independents for now," fine — then the output doesn't chart dependents, but it surfaces the dropped ones explicitly ("Asserted dependents [X, Y, Z] not charted in this run — request: rerun with `--include-dependents` or paste the dependent claim text"). Do not silently skip dependents.

A dependent-claim row format:

```markdown
| [#] | Element (verbatim) | Accused feature (or prior-art disclosure) | Evidence (pin-cited) | Mapping | State | Verified |
|---|---|---|---|---|---|---|
| 2 [add'l] | "wherein the barb extends at an angle of 15° to 30° from the body axis" | AnchorFast Mini barb angle 18° per [CM-AM-2026-03 Fig. 4 + §2.3] | [CM-AM-2026-03 §2.3] "barb angle 18° ±2°" | literal-construction-dependent | mapped | ☐ |
```

### Step 4.5: DOE supplements — execute, don't gesture

For every element charted as `literal` where the accused feature is structurally similar but not literally identical — or every element where the `literal` mapping turns on a contested construction — produce a **paired DOE candidacy row** (infringement mode). Do not footnote "DOE analysis is separate" without producing the actual DOE mapping.

A DOE candidacy row adds a one-paragraph function-way-result sketch, flags prosecution history estoppel and dedication-to-the-public risks per element, and cites the evidence that would support the equivalent. If DOE is inapplicable (the element reads literally on the accused product beyond dispute), skip. If `literal` is construction-dependent and DOE would be the attorney's fallback under the narrower construction, produce the DOE row.

Format:

```markdown
| [#-DOE] | Element | Accused feature | Function-way-result | PH estoppel? | Dedication risk? | State |
|---|---|---|---|---|---|---|
| 1b-DOE | "at least one barb" | three-barb opposing-face array | function: resist withdrawal; way: mechanical engagement with cancellous bone; result: anchor remains seated under tensile load. | [needs-evidence: prosecution history] | [needs-evidence: disclosed-but-unclaimed alternatives in spec] | construction-dependent |
```

As with dependents: if the skill can't produce the DOE rows for a reason (no accused-product evidence to ground function-way-result, no prosecution history available), say so explicitly and route to `needs-evidence`. Do not skip DOE silently.

### Step 5: Indirect, divided, willfulness (infringement only)

**BR-designated patent (default).** LPI does not codify separate categories of "induced" or "contributory" infringement the way 35 U.S.C. §271(b)/(c) does, and it has no divided/joint-infringement doctrine like *Akamai*. Brazilian practice reaches a third party's participation in the infringement through general civil co-authorship of the unlawful act (Código Civil arts. 186, 927, 942) rather than a patent-specific indirect-infringement statute `[model knowledge — verify]`. Flag, don't opine:

- **Third-party participation (civil co-authorship)** — did the accused party knowingly supply a component, service, or instruction that enabled another's direct infringement? Frame as a Código Civil arts. 186/927/942 flag, not as "induced" or "contributory" under a US label.
- **Divided performance across parties** — LPI art. 42 defines the exclusive right in terms of the patentee's own exploitation; there is no codified "directs or controls" test for splitting a claimed process across multiple actors. Flag as an open question for attorney analysis rather than applying *Akamai*'s test.
- **No willfulness-multiplier doctrine.** There is **no treble-damages or willfulness-enhancement equivalent** under Brazilian law. Knowledge of the patent bears on the "greatest of" damages calculation under LPI art. 210 (see Step 6) and can support a *litigância de má-fé* characterization (CPC arts. 79-81) in later litigation, but it does not multiply the damages award the way §284 does `[model knowledge — verify]`. Do not describe BR exposure using "willfulness" or "treble damages" vocabulary — flag it as a *má-fé* / bad-faith consideration instead.

**US-designated patent or US-territorial conduct genuinely in scope (fallback).** Apply the US framework:
- **Induced (§271(b))** — *Commil USA, LLC v. Cisco Systems, Inc.*, 575 U.S. 632 (2015); *Global-Tech Appliances, Inc. v. SEB S.A.*, 563 U.S. 754 (2011)
- **Contributory (§271(c))** — component especially made for infringing use
- **Divided / joint (§271(a))** — *Akamai Techs., Inc. v. Limelight Networks, Inc.*, 797 F.3d 1020 (Fed. Cir. 2015) (en banc) directs/controls test
- **Willfulness** — *Halo Elecs., Inc. v. Pulse Elecs., Inc.*, 579 U.S. 93 (2016); treble damages under §284

### Step 6: Invalidity thresholds (invalidity only)

**BR-designated patent (default framework) — LPI arts. 8, 11-15, 18, 24.**

- **Novidade (novelty)** — LPI arts. 8, 11-15. Every element must be absent from a single prior-art reference (estado da técnica) for the claim to be novel; a reference disclosing all elements defeats novelty outright.
- **Atividade inventiva (inventive step)** — LPI art. 8, 13. Roughly analogous in function to US non-obviousness but not identical in doctrinal structure — Brazilian practice does not apply *Graham*/*KSR* factors as codified law; flag combination-of-references arguments and any evidence of technical obviousness to a person skilled in the art (técnico no assunto) as attorney-judgment calls `[model knowledge — verify]`.
- **Aplicação industrial (industrial applicability)** — LPI art. 8, 15.
- **Matéria não patenteável** — LPI art. 10 (discoveries, scientific theories, mathematical methods, purely aesthetic creations, computer programs as such, business methods, natural biological processes) and art. 18 (contrary to morals/public order/safety/health; substances from nuclear transformation; living beings other than transgenic microorganisms meeting the three patentability requirements). This is the closest BR analogue to a US §101 subject-matter-eligibility flag — do not import *Alice*/*Mayo* two-step analysis onto it without flagging the doctrinal mismatch.
- **Suficiência descritiva (sufficiency of disclosure)** — LPI art. 24. The claim must be fully and clearly supported by the specification; this is the closest BR analogue to §112 written description/enablement. There is no separate BR statutory analogue to §112's definiteness or means-plus-function provisions — flag ambiguous or functionally-claimed terms as attorney-judgment calls rather than citing §112 ¶2/¶6 directly.
- **Unenforceability-adjacent flags** — no direct LPI equivalent to US inequitable conduct doctrine; frame deceptive procurement as fraud voiding the act under general civil law `[model knowledge — verify]`. No equitable laches doctrine — check the applicable prescription period (Código Civil art. 206) instead of assuming laches.

**Invalidity venue (BR default).** Two tracks, both flag-only — this skill does not opine on which will succeed:
- **Administrative nullity** (LPI art. 51) — INPI-initiated or third-party petition before the agency, no deadline while the patent is in force.
- **Judicial nullity action** (LPI art. 56) — filed in the federal courts at any point during the patent's term, **with INPI as a mandatory co-defendant (litisconsórcio passivo necessário) per LPI art. 57** — a nullity contention or claim chart that omits INPI as a party is procedurally defective. There is **no US-style inter partes review (IPR) or post-grant review (PGR) administrative-litigation hybrid** at INPI; the administrative track (art. 51) and the judicial track (art. 56) are the closest analogues, and neither functions like an IPR/PGR proceeding before a specialized tribunal. This claim-chart context is the judicial ação de nulidade (art. 56), not the administrative track.
- **Standard of proof.** Brazilian civil procedure does not use a "clear and convincing evidence" evidentiary standard — the general civil standard is preponderância da prova (preponderance), assessed by the judge's free evaluation of evidence (livre convencimento motivado, CPC art. 371) `[model knowledge — verify]`. A prima facie chart is not proof at trial regardless of jurisdiction; do not import the US clear-and-convincing framing onto a BR nullity action.

**US-designated patent genuinely in scope (fallback).** Apply the US framework:

For §102: every element in a single reference. Partial across references is §103.

For §103: primary reference + secondary reference(s) + documented motivation under *KSR*. Flag explicit teaching/suggestion/motivation, market or design-need motivation, reasonable expectation of success, and **secondary considerations** (*Graham v. John Deere Co.*, 383 U.S. 1 (1966)) — commercial success, long-felt need, failure of others, industry praise, copying.

Also flag:
- **§101** — *Alice Corp. Pty. Ltd. v. CLS Bank Int'l*, 573 U.S. 208 (2014); *Mayo Collaborative Servs. v. Prometheus Labs., Inc.*, 566 U.S. 66 (2012)
- **§112 ¶ 1** — written description, enablement (*Amgen Inc. v. Sanofi*, 598 U.S. 594 (2023))
- **§112 ¶ 2** — definiteness (*Nautilus*, supra)
- **§112 ¶ 6** — means-plus-function structure
- **Unenforceability** — inequitable conduct, prosecution laches, assignor/licensee estoppel (attorney-only flags)

Invalidity must be shown by clear and convincing evidence — *Microsoft Corp. v. i4i Ltd. P'ship*, 564 U.S. 91 (2011). Prima facie in a chart is not proof at trial.

### Step 7 (review sub-mode): Audit

For each row: is the mapping supported? Is the pin cite accurate? Is the element fully accounted for? What's the strongest counter? What's the rebuttal opportunity? Output verdicts per row (`supported` / `weak` / `unsupported`) and the chart's vulnerabilities.

## Patent-mode guardrails (in addition to shared guardrails)

- **Dever de boa-fé processual (CPC art. 77) / litigância de má-fé (CPC arts. 79-81).** Brazil has no formal "patent local rule" contentions regime — infringement/nullity allegations in the petição inicial or contestação still require reasonable inquiry and a non-frivolous basis under the general duty of good faith in litigation; asserting facts without basis risks a finding of má-fé. A chart out of this skill is a draft, not a pleading.
- **Claim construction candor.** Every construction-dependent row states the construction assumed (perícia técnica finding, if any, for a BR-designated patent; Markman order for a US-designated patent) and the construction under which the mapping fails.
- **DOE candor.** A DOE mapping is not equivalent to a literal one. For a BR-designated patent, flag "equivalência" as `[model knowledge — verify]` per the DOE note in Step 5's cross-reference — Brazilian courts recognize infringement by equivalent means but LPI does not codify a function-way-result test, so do not import *Festo*-style prosecution-history-estoppel doctrine wholesale. For a US-designated patent, flag prosecution history estoppel and dedication-to-the-public risks per element.
- **Indirect is separate.** Don't fold third-party civil co-authorship (BR default) or induced / contributory (US fallback) into direct-infringement rows.
- **Invalidity burden on the chart.** For a BR-designated patent (default), state the general civil preponderância da prova standard (CPC art. 371) — do not import the US clear-and-convincing standard. For a US-designated patent genuinely in scope, state the clear-and-convincing standard.
- **Damages posture flagged, not computed.** For a BR-designated patent (default), flag LPI art. 210's "greatest of" formula (infringer's gain / patentee's loss / reasonable royalty) and note explicitly that **there is no treble-damages or willfulness-multiplier equivalent** — do not let a US-pattern rewrite smuggle in a "willfulness = automatic multiplier" framing. For a US-designated patent genuinely in scope, flag the Georgia-Pacific reasonable-royalty factors and §284 willfulness enhancement instead. Damages computation itself is an expert's job in either regime — this chart flags the posture, it does not quantify.

---

# MODE 2 — Civil element chart

Map the elements of a cause of action (or affirmative defense) against the evidence. The killer outputs are (a) a chart that says what evidence goes with what element and (b) a gap list that tells the attorney what's missing.

## Workflow

### Step 1: Identify the claim(s)

- What cause of action? (Or defense?) If multiple counts, chart each separately.
- Which side? Plaintiff's prima facie case, defendant's affirmative defense, defendant's challenge to plaintiff's prima facie case (MSJ mode). Read `## Side` in the practice profile for the default — `plaintiff` defaults to mapping the prima facie case (proving the elements); `defense` defaults to mapping gaps and affirmative defenses (disproving or avoiding the elements). Confirm the posture matches this matter before starting.
- Which jurisdiction? State and court. **Elements and pattern-instruction language vary by jurisdiction.** The template library is a baseline; the controlling pattern instruction or statute controls.
- Which pleading? Load the complaint / counterclaim / answer so the chart tracks the counts actually pleaded, not a generic version.

### Step 2: Load the elements

Three paths:

**(a) Template library.** Reference `references/element-templates.md` (in this skill's directory). Baseline elements for common causes of action and common affirmative defenses, with citations to the Restatement / pattern instructions and a jurisdiction caveat. Select the template that matches the pleaded count.

**(b) Custom.** User defines elements, or pastes a jury instruction / statute / a count from the complaint to parse. Parse into numbered elements.

**(c) Affirmative defenses.** Also support mapping defenses — statute of limitations, laches, estoppel, waiver, unclean hands, release, accord and satisfaction, failure to mitigate, comparative fault, contributory negligence, assumption of risk, etc. Defenses have their own elements the defendant must prove (or, for some, the plaintiff must negate once raised).

**Regional formulations — surface proactively.** Brazil is a unitary civil-law system, not a federalism-of-common-law system like the US where each state can have its own substantive law of contract or tort — so "state-specific formulation of a cause of action" is the wrong frame here. Substantive law (Código Civil, CDC, CLT, Lei 9.279/1996, etc.) is federal and uniform nationwide; there is no Delaware-vs-New York-vs-California divergence in the elements themselves. What DOES vary regionally: (a) **local TJ case-law tendencies and súmulas** — a Tribunal de Justiça's consolidated súmulas or its chamber-level "entendimento consolidado" can read a codified element more broadly or narrowly than another TJ, even though the statute is the same nationwide; (b) for labor claims, **TRT regional variance** in how a given Tribunal Regional do Trabalho interprets CLT provisions (e.g., configuração de vínculo, cálculo de horas extras, dano moral trabalhista) before TST unifies it. If the practice profile's `## Company profile → Core jurisdictions` or the active matter's `matter.md` names **São Paulo, Rio de Janeiro, or Justiça do Trabalho** as the relevant forum, surface the relevant regional súmula or entendimento consolidado proactively alongside the baseline — do not ask "does your região add/drop/reword" first. The user shouldn't have to teach the skill the local tendency; the skill should offer it and let the user choose.

Divergences to surface without being asked (non-exhaustive — add to this list as patterns recur):

| Cause of action / defense | Baseline (Código/Lei) | Regional formulation |
|---|---|---|
| Responsabilidade civil contratual (inadimplemento) | CC arts. 389, 395, 475 — mora, inadimplemento absoluto, resolução | **TJSP** súmulas em matéria de cláusula penal e correção monetária tendem a ser mais restritivas quanto à cumulação com perdas e danos; confirmar súmula vigente da Seção de Direito Privado do TJSP antes de assumir cumulação automática. |
| Abuso de direito / ato ilícito (interferência em relação contratual) | CC arts. 186, 187 | **TJRJ** tem jurisprudência mais desenvolvida em concorrência desleal e abuso de direito no contexto empresarial (Varas Empresariais) — verificar precedentes daquelas câmaras antes de assumir a formulação genérica do CC. |
| Dano moral (honra, imagem) | CC arts. 11-21, 186, 927 | Tabelamento/parâmetros de quantum indenizatório variam por TJ — alguns tribunais (e.g., TJSP) publicam tabelas de referência internas para balizar valores; confirmar a tabela ou súmula do tribunal competente antes de estimar o quantum. |
| Horas extras / vínculo empregatício (CLT) | CLT arts. 3º, 58-61, 59 | **TRT regional** pode ter entendimento consolidado próprio sobre configuração de vínculo (subordinação estrutural/algorítmica em plataformas digitais, por exemplo) até o TST uniformizar via súmula ou IRR (incidente de resolução de demandas repetitivas). Surfar a súmula/OJ do TRT da região antes do TST pacificar. |
| Assédio moral no trabalho | CC arts. 186, 927 c/c CLT art. 483 | Cada TRT tem seus próprios critérios de gravidade e quantum para dano moral trabalhista — parâmetros do TRT-2 (SP) e TRT-1 (RJ) divergem sensivelmente dos de TRTs menores. |

When a regional formulation differs materially from the baseline, the chart opens with a one-line callout:

> **Nota de jurisdição:** Você indicou que este é um caso em [SP/RJ/Justiça do Trabalho]. Veja como o entendimento consolidado / súmula de [tribunal] diverge da base nacional: [divergência]. O chart abaixo usa a formulação de [tribunal]. Se isso estiver errado, me avise e eu recarrego.

Confirm the element list with the user before mapping. If the matter isn't in SP, RJ, or before Justiça do Trabalho, ask: "Há alguma súmula ou entendimento consolidado do seu tribunal que adiciona / remove / reformula algum desses elementos?" If yes, use their version.

### Step 3: Map

For each element:

- **Evidence supporting** — what proves this element? Cite the source with a pin cite.
  - Deposition testimony — `[Doe Dep. 42:15–43:7]`
  - Declaration — `[Smith Decl. ¶ 12]`
  - Produced document — `[DEF00012345 at 3]`
  - Admission — `[Def.'s Resp. to RFA No. 5]`
  - Exhibit — `[Trial Ex. 14 at 2]`
  - Expert report — `[Jones Expert Rep. at 18]`
  - Discovery response — `[Pl.'s Resp. to Interrog. No. 8]`
  - Statute / case — for purely legal elements
- **Verbatim quote** where the evidence is testimonial or documentary. No paraphrase.
- **Evidence contradicting** — what cuts the other way? Cite it. This is the row's vulnerability.
- **Strength** — `strong` / `moderate` / `weak` / `none`. Keep it simple. Over-calibrated strength scores are noise; `weak` and `none` are the rows that matter.
- **State per cell** — `supported` / `partial` / `disputed` / `gap` / `needs-discovery`.

### Step 4: Gap detection — the killer output

After mapping, produce a gap list. This is the point of the chart.

> **Elements with thin or no evidence:** [list]
>
> - If asserting (plaintiff): these defeat your complaint's plausibility (Iqbal/Twombly), your MSJ opposition, or your case at trial. Close them before the next motion.
> - If defending: these are your MSJ targets and your directed-verdict motion. The plaintiff has to prove each element; a gap is a defense.
> - If pre-discovery: these are your discovery priorities — the depositions, document requests, and interrogatories that turn a gap into `supported` or confirm `none`.

Gap detection is not a conclusion about the merits. It's a map of where the case is light.

### Step 5: Phase-aware framing

Ask the phase. Same chart; different framing on the output:

- **Pre-filing / pleadings.** Does the complaint allege each element with plausibility (*Ashcroft v. Iqbal*, 556 U.S. 662 (2009); *Bell Atl. Corp. v. Twombly*, 550 U.S. 544 (2007))? Any element pleaded on information and belief without factual support is a 12(b)(6) target.
- **Discovery.** For each `gap` or `needs-discovery` element, what discovery is needed? Which witnesses, which document custodians, which interrogatories, which RFAs.
- **MSJ.** For each element, is there a genuine dispute of material fact? A `supported` cell for the movant with no contradicting evidence is summary-judgment ammunition; a `disputed` cell is MSJ-defeating.
- **Trial.** Order of proof. Which witness proves element 1, which exhibit proves element 2, who authenticates, what's the foundation. The chart becomes the trial outline.

### Step 6 (review sub-mode): Audit

For an opposing party's MSJ brief, a motion to dismiss, or outside counsel's draft: for each element, does their cited evidence actually prove it? Where is their chart thin? What's your strongest counter?

## Civil-mode guardrails (in addition to shared guardrails)

- **Jurisdiction.** The element list is a baseline. Always confirm the controlling pattern instruction (CACI, NYPJI, federal circuit pattern charge, etc.) or statute. State the source on the chart's `_elements` sheet.
- **Pleaded counts only.** Chart what's actually pleaded. Don't add a count the complaint doesn't allege just because the facts might support it — that's a different analysis.
- **Affirmative defenses.** If mapping defenses, note whether the burden is on the defendant (most) or whether raising the defense shifts a burden to the plaintiff.
- **"Gap" ≠ "case over."** A gap is a lead. Discovery, a declaration, or an expert report can close it. The chart shows where to dig.

---

# Shared chassis (both modes)

## Output

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` `## Outputs`.

### Markdown table (always)

One table per claim / defense / patent-claim per target.

**Patent mode example:**

```markdown
| [#] | Element (verbatim) | Accused feature | Evidence (pin-cited) | Mapping | State | Verified |
|---|---|---|---|---|---|---|
| 1a | "a processor configured to..." | SoC per datasheet | [Datasheet p. 7] "..." | literal-construction-dependent | mapped | ☐ |
| 1b | "means for [function]" (§112(f)) | [alleged equiv.] | [source, file.c:124] "..." | needs-evidence | needs-evidence | ☐ |
```

**Civil mode example:**

```markdown
| [#] | Element | Evidence supporting (pin-cited) | Evidence contradicting | Strength | State | Verified |
|---|---|---|---|---|---|---|
| 1 | Existence of a contract | [Ex. 3, MSA § 1; Smith Dep. 22:4–14] | none | strong | supported | ☐ |
| 2 | Plaintiff's performance | [Jones Decl. ¶¶ 4–9] | [Doe Dep. 101:3–11: "they never delivered Phase 2"] | moderate | disputed | ☐ |
| 3 | Defendant's breach | — | [Doe Dep. 101:3–11] | none | gap | ☐ |
| 4 | Causation | — | — | none | needs-discovery | ☐ |
| 5 | Damages | [Expert Rep. at 18 — $2.4M lost profits] | [Def.'s Expert Rep. at 6 — critiques methodology] | moderate | disputed | ☐ |
```

Follow with:
- **Defenses / thresholds** (patent mode: invalidity / indirect / willfulness flags; civil mode: affirmative-defense flags, Iqbal/Twombly flags pre-pleading)
- **Gap list** (civil mode) / **needs-evidence list** (patent mode) — **the priority output**
- **What cuts which way — summary** — strongest elements, weakest elements
- **Conclusion line** — *"This skill does not conclude."* Elements mapped/supported: [list]. Elements needing evidence / in a gap state: [list]. Elements construction-dependent (patent) / disputed (civil): [list]. Attorney judgment required.
- **Citation verification** — every pin cite, case, column/line, deposition page:line must be verified against the source.

### CSV (always)

Two files per chart:
- `[chart-slug].csv` — values
- `[chart-slug]_sources.csv` — verbatim quotes, pin cites, notes

**CSV / spreadsheet cell safety.** Before writing any cell value, check the first character. If it is `=`, `+`, `-`, `@`, tab (`\t`), or carriage return (`\r`), prepend a single apostrophe (`'`) to neutralize Excel/Sheets formula interpretation. Verbatim evidence from adversarial sources (opposing counsel's contentions, competitor product manuals, third-party prior art, scraped web pages, deposition transcripts, discovery productions) can contain strings that a spreadsheet will execute as formulas (`=HYPERLINK(...)`, `=cmd|...!A1`, `+WEBSERVICE(...)`), turning the chart into a data-exfiltration or RCE vector when an attorney opens it. RFC 4180 quoting alone does not defeat this — the leading `=` is still interpreted. Apply the apostrophe prefix in CSV, XLSX, and Sheets outputs. Log cells where this was applied so the reviewer can see which quotes were neutralized.

### Spreadsheet (Excel or Sheets)

Ask which the team works in. Use the pattern from `corporate-legal`'s `tabular-review` skill — same cell-level citation model, same state-based color coding, same `Verified` column, same schema sheet:

- One row per element (or element × target if comparing multiple targets)
- Each evidence column paired with a hidden source column containing the verbatim quote and pin cite; cell comments (Excel) or notes (Sheets) surface the quote on hover
- Color coding by state:
  - *Patent:* white = `mapped`, yellow = `construction-dependent` / `partial` / DOE, orange = `needs-evidence`, red = `not-found`
  - *Civil:* white = `supported`, yellow = `partial` / `disputed`, orange = `needs-discovery`, red = `gap`
- `Verified` column per evidence column, blank by default — reviewer marks it
- `_elements` sheet documenting the element source: pattern jury instruction (CACI No. X, NYPJI §Y, federal circuit pattern charge), statute (cite), Restatement section, or patent-claim parse. This is what makes the chart auditable — a reader can see where the elements came from.
- `_gaps` sheet listing every `gap`, `needs-evidence`, or `needs-discovery` row with what's still needed
- For patent mode only: `_claim-parse` sheet (element decomposition), `_constructions` sheet (disputed terms and assumed constructions)

Apply the apostrophe-prefix neutralization to every cell written into the spreadsheet.

Prepend the work-product header as the top row. Alongside it, include:

> This chart is derived from source documents that may be privileged, confidential, or both. It inherits the sources' privilege and confidentiality status — distribution beyond the privilege circle can waive privilege. Store with the matter's privileged files and make distribution decisions deliberately. Nothing in this chart has been filed or served; it is a draft for attorney review.

### Filename and location

- Patent infringement: `claim-chart-infringement-[patent#]-claim[#]-[target]-YYYY-MM-DD.{md,csv,xlsx}`
- Patent invalidity: `claim-chart-invalidity-[patent#]-claim[#]-[ref]-YYYY-MM-DD.{md,csv,xlsx}`
- Civil: `element-chart-[count-slug]-[side]-YYYY-MM-DD.{md,csv,xlsx}`
- Review: `chart-review-[subject]-YYYY-MM-DD.{md,csv,xlsx}`

If matter workspaces enabled and a matter is active: `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<matter-slug>/claim-charts/`. Otherwise: `~/.claude/plugins/config/claude-for-legal/litigation-legal/claim-charts/`. Surface the path. Append a one-line entry to the matter's `history.md`.

## Summary readout

After the chart is written, give a one-screen readout:

- Claim(s) / count(s) / patent claim(s), target(s), jurisdiction, phase
- Elements charted · supported/mapped · partial · disputed · gap / needs-evidence · not-found
- The gap list (civil) or needs-evidence list (patent) — **this is the priority list**
- Where the output files are
- Reminder: every cell is a lead. The chart is a draft, not a contention / brief / order of proof.

## Non-lawyer gate

If `## Who's using this` Role is Non-lawyer:

> This chart is a research draft, not a legal filing. Filing a petição/contestação, or relying on this for a merits opinion, has litigância de má-fé (CPC arts. 79-81) and substantive legal consequences. An attorney in the relevant jurisdiction must review before this is used for any legal purpose. For patent-mode charts: representation before INPI in an administrative nullity or prosecution matter is through an **Agente da Propriedade Industrial** (LPI art. 216); a judicial ação de nulidade or ação de infração requires an advogado inscrito na OAB — the OAB referral service can direct you to one `[model knowledge — verify]`. For a US-designated patent, a registered patent attorney before the USPTO OED is the equivalent gate.
>
> Here's a one-page brief to bring to an attorney:
>
> [Generate: claim / patent, side, jurisdiction, phase, elements, supported / gap / needs-discovery counts, the three most load-bearing open questions.]

Deliver the chart alongside the brief.

## Shared guardrails — checklist

- **Citation verification.** Every pin cite (column/line, page, deposition page:line, Bates, ¶) is a claim about the source. The attorney verifies. The skill does not fabricate cites — if a cite cannot be produced, the cell is `needs-evidence` or `gap`.
- **Source attribution.** Every verbatim quote has its source in the companion CSV and the spreadsheet's hidden source column. A quote without a source is not evidence.
- **No silent supplement.** Thin evidence means `needs-evidence` / `gap`, not "extrapolate." Do not fill from web search, training data, or "how these cases usually go" to close a gap.
- **Matter workspace check.** Confirm the active matter before writing. Never write matter A's chart into matter B's folder.
- **Decision posture.** When uncertain whether an element is met, flag; do not decide. `partial` tells the attorney what part is missing.
- **Formula injection.** Every cell written to CSV / XLSX / Sheets is checked for leading `=`, `+`, `-`, `@`, `\t`, `\r` and prefixed with `'`. Default: neutralize-then-write.
- **Elements are jurisdiction-specific.** The template library is a baseline. The controlling pattern instruction or statute controls.
- **A chart is not a brief, a filing, or a contention.** Every output is a draft.

---

## Relationship to other skills

- `ip-legal:infringement-triage` (patent mode) — the first-pass flag list. This skill is the full chart that comes next.
- `ip-legal:fto-triage` — FTO uses the same mechanics from the potentially-accused posture. If evaluating own product vs. a third-party patent, route to FTO and use this skill's format.
- `corporate-legal:tabular-review` — the underlying cell-level citation and verification-state pattern. A claim / element chart is a specialized tabular review.
- `litigation-legal:chronology` — the chronology is the timeline; the element chart is the proof matrix. A chronology entry often becomes a cell's evidence cite.
- `litigation-legal:deposition-prep` — a `needs-discovery` cell often becomes a depo topic. After a depo, new testimony fills cells.
- `litigation-legal:brief-section-drafter` — an MSJ brief's fact section is often built directly off the supported rows of an element chart.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **It does not conclude.** Not infringement, not non-infringement, not liability, not non-liability. Ever.
- **It does not decide claim construction** (patent) or **the controlling elements** (civil). It flags disputed terms / baseline elements and charts under stated assumptions.
- **It does not meet the clear-and-convincing burden for invalidity** or **the preponderance at trial**. It produces a prima facie draft for attorney review.
- **It does not substitute for expert analysis.** Source code review, teardowns, technical experts, damages experts are separate work products this chart routes to, not replaces.
- **It does not serve, file, or sign anything.** Every output is a draft. An attorney serves and files.
- **It does not extrapolate.** If the evidence isn't there, the cell is `needs-evidence` / `gap` — never a guess.
