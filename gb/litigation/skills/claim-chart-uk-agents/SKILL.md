---
name: claim-chart-uk-agents
title: /claim-chart
description: Build or review an element chart — a patent claim chart (infringement, invalidity, or review) or a civil element chart for any cause of action or defence — with every cell pin-cited and gap detection as the priority output. Use when the user asks for a claim chart, element chart, proof chart, infringement or invalidity contention, element-by-element mapping, or asks "what are we missing to prove [claim]".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/claim-chart
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
sources:
- title: Element Templates
  path: references/element-templates.md
---

# /claim-chart

1. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → role, work-product header, decision posture, document storage.
2. If matter workspaces enabled, confirm or select the active matter; load `matter.md` (side, jurisdiction, phase, theory, pleadings).
3. Follow the workflow and reference below.
4. Mode selection:
   - `--patent` → patent claim chart. Require patent number and at least one asserted claim. Sub-modes: `--infringement`, `--invalidity`, `--review`.
   - `--civil` → civil element chart. Require the cause of action (or defence) and the side.
   - No flag → ask the user which.
5. For civil mode: consult `references/element-templates.md` in the skill directory for the baseline element list. Confirm the controlling pattern instruction or statute with the user before mapping.
6. For patent mode: parse asserted claims into elements, flag disputed terms for construction, apply any claim construction ruling.
7. Map elements against the target (accused product / prior art / evidence corpus / chart under review). Every cell pin-cited. Apply the apostrophe-prefix neutralisation before writing any cell value starting with `=`, `+`, `-`, `@`, tab, or CR.
8. Produce the gap list (civil) or needs-evidence list (patent) — the priority output.
9. Write markdown, CSV (values + `_sources` companion), and Excel or Sheets per user preference. Work-product header on every output.
10. Write to the matter's `claim-charts/` folder if a matter is active; otherwise the practice-level `claim-charts/` folder. Append a one-line entry to `history.md` if a matter is active.
11. Return a summary readout: claim(s), target(s), jurisdiction, phase, element counts by state, the gap list, file paths, and the reminder that every cell is a lead.

---

# Claim Chart

## Disclosed-document use restrictions

Before working with a set of litigation documents, ask: "Were any of these documents obtained through disclosure in legal proceedings?" If yes:

- **England & Wales (CPR 31.22):** Documents obtained through disclosure are subject to the implied undertaking — you may only use them for the purpose of the proceedings in which they were disclosed, unless the court grants permission, the disclosing party consents, or the document has been read in open court. Using them for a different matter, a different claim, or a commercial purpose without permission is a contempt.
- **Scotland:** Equivalent undertaking principles apply under the Rules of the Court of Session and the Sheriff Court Rules. Confirm with Scottish solicitors.
- **Other jurisdictions:** Similar restrictions commonly apply. Check the local rule.

Confirm: "This use is within the proceedings in which the documents were disclosed, or I have permission / consent, or the documents are now public." If not confirmed, flag it: "⚠️ Disclosed documents may have use restrictions. Confirm this use is permitted before proceeding."

## A CHART IS A DRAFT, NOT A FINDING OR A CONTENTION

**Put this at the top of every output. Do not drop it. Do not soften it.**

> This chart is a draft for solicitor/barrister analysis and verification, not a served contention, a skeleton argument, an opening note, or a legal opinion. Every mapping is a lead the solicitor or barrister must verify against the source. The elements listed come from English common law authorities, UK statutes, or the claim language as parsed — the **controlling** authority in the applicable court (the leading English/UK authority, the CPR, the Patents Court Guide, the IPEC Guide, or a claim construction ruling) may differ and always controls. Gap detection is a starting point for disclosure or an application; it is not a conclusion about the merits.

Under-flagging a gap is a one-way door — a claim form issued without plausibility on an element, a summary judgment response served without evidence for a disputed element, or a case tried without proof of loss. Over-flagging is a two-way door — the solicitor or barrister clears flags in review. The default is biased toward the two-way door.

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — especially the case theory, the pleading (particulars of claim, defence) (for the elements actually alleged), the jurisdiction, any claim construction ruling or agreed constructions (patent mode), and the phase of the case. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/<matter-slug>/claim-charts/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → role, work-product header, decision posture, document storage, case-theory scaffolding
- Active matter's `matter.md` — claims, defences, side, jurisdiction, phase, theory
- For civil mode: the particulars of claim or counterclaim (for the actually-pleaded counts), any defence (for the actually-pleaded defences), the relevant UK authority or statute, and the evidence corpus — witness statements, expert reports, produced documents, disclosed documents.
- For patent mode: the patent, the asserted claims, the specification, prosecution history if available, the accused-product material or prior art reference, any claim construction ruling or agreed constructions.

If `CLAUDE.md` has `[PLACEHOLDER]` markers, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor risk calibration, landscape, and house style to your practice.
>
> **Two choices:**
> - Run `/litigation-legal-uk:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — England & Wales jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," build the claim chart normally using these generic defaults: middle risk appetite, lawyer role, England & Wales jurisdiction, no practice-level playbook (work from the matter's pleadings and the elements of the claims as pleaded). Tag the reviewer note and every row of the chart with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/litigation-legal-uk:cold-start-interview` to get output calibrated to YOUR practice — your risk calibration, your landscape, your house style. 2 minutes."

**Conflicts gate — unbypassable.** Before building a claim chart, check `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal-uk:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build a claim chart on a matter that hasn't been intaken — the conflicts check is the gate."

Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the `_log.yaml` row this skill reads from.

---

## Mode selection

Ask at the top, before anything else:

> Which kind of chart?
>
> 1. **Patent claim chart** — element-by-element mapping of claim limitations against an accused product (`--infringement`), prior art (`--invalidity`), or another party's chart (`--review`). For patent contentions, IPR proceedings, FTO charts. UK patents are governed by the Patents Act 1977 and the European Patent Convention; proceed on the applicable basis and flag the UK/EP distinction where it matters.
> 2. **Civil element chart** — elements of a cause of action (or affirmative defence) mapped against the evidence. For particulars-of-claim plausibility checks, disclosure planning, summary judgment (CPR Part 24) preparation, order-of-proof outlines.

Plus intake (common to both):

- **Side.** Asserting or defending? (In civil mode this flips the burden; in patent mode it flips infringement/invalidity framing.)
- **Jurisdiction / forum.** Which UK court — IPEC, Patents Court, King's Bench Division, Chancery Division, CAT, County Court — and whether the patent is a UK patent or a European patent (UK). Procedure and pleading requirements vary by forum. Flag the applicable court guide (IPEC Guide, Patents Court Guide, Chancery Guide, CPR Part 63).
- **Phase.** Pre-filing, pleadings, disclosure, witness statements / expert evidence, trial preparation, post-trial. The chart is the same; the framing of the output changes.
- **Existing chart?** If `--review`, load it.

---

# MODE 1 — Patent claim chart

## Sub-modes

- `--infringement` — claim elements vs. accused product (infringement contentions, response exhibits, particulars of infringement)
- `--invalidity` — claim elements vs. prior art (invalidity contentions, petition exhibits, §2/§3 PA 1977 / Art. 54/56 EPC defences)
- `--review` — audit a chart someone else produced

## Additional patent-mode intake

- **Patent number and asserted claims.** Which independent, which dependent. (Don't chart unasserted claims unless asked.)
- **Priority date.** Establishes the novelty/obviousness bar and the effective date.
- **Existing constructions.** Any claim construction ruling, agreed constructions, or constructions proposed in pleadings.
- **UK or EP(UK) patent.** Affects the applicable statute and rules; flag for patent counsel.

## Patent-mode workflow

### Step 1: Parse the claims

Parse asserted independent claims into numbered elements. Handle:

- **Preamble.** Note whether it limits the claim — a question of construction. Flag `preamble-limiting: unresolved` unless a ruling resolves it.
- **Transitional phrase.** "Comprising" (open) / "consisting of" (closed) / "consisting essentially of" (semi-open). Affects whether additional unrecited elements defeat infringement.
- **Elements** separated by commas / semicolons, numbered `[1a]`, `[1b]`, `[1c]`. Keep numbering stable — it's the chart's spine.
- **Means-plus-function / functional language** — flag where a claim element is purely functional; UK courts construe such claims purposively. Cite the specification's disclosed embodiment. If the specification fails to disclose sufficient structure, flag `insufficiency-risk`.
- **Markush groups, Jepson-style claims, product-by-process, method-step order dependencies** — flag with a note on unusual construction considerations.
- **Dependent claims** — reference parent; chart only the additional limitations. **Execute, don't gesture.** If asserted claims include dependents, produce the actual additional-limitation rows for each dependent in Step 4 — do not emit a note that dependents "should be charted."
- **Structural-term cognates — default to `construction-dependent`.** For each element that recites a structural noun with a common cognate in the prior art of the field, default the row's state to `literal-construction-dependent` (not `literal`) unless the specification expressly defines the term or an existing ruling forecloses the ambiguity. These are the terms most commonly disputed at a claim construction hearing — presuming a clean literal read under-flags the risk. Common cognate families to flag proactively:

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

  This list is not exhaustive — if the claim recites a structural noun that could reasonably be read narrowly or broadly, flag `structural-term-cognate` in `_constructions` and default the row to `construction-dependent`. The solicitor or barrister can demote it to `literal` after a ruling or a definition in the specification forecloses the ambiguity.

Show the parse to the user. Confirm before mapping. A wrong parse poisons every row below it.

### Step 2: Claim construction check

Flag disputed terms:

- Coined terms or terms defined in the specification
- Terms with prosecution history (amendments, arguments, disclaimers)
- Functional language ("configured to", "adapted to", "operable to")
- Relative terms ("substantially", "about") — sufficiency / clarity risk under UK law
- Computer-implemented terms — potential patentable-subject-matter / excluded matter (Patents Act 1977, s 1(2)) exposure for invalidity

For each flagged term, state the construction(s) under which the mapping works and the construction(s) under which it fails. If a claim construction ruling exists, apply it. If pleadings are underway, chart under each side's proposed construction.

In the UK, claims are construed purposively in light of the specification (following *Kirin-Amgen Inc v Hoechst Marion Roussel Ltd* [2004] UKHL 46 `[model knowledge — verify]` and *Actavis UK Ltd v Eli Lilly and Co* [2017] UKSC 48 on equivalents `[model knowledge — verify]`). Flag where equivalents may be relevant and where prosecution history disclaimer may limit scope.

### Step 3: Map

For each element, for each target:

1. **Find evidence.** Accused product: documentation, manuals, data sheets, source code, teardowns, witness statements, expert reports. Prior art: column/paragraph/page for the relevant document; for prior art, flag whether the reference qualifies (published before priority date, public availability).
2. **Quote verbatim.** Character-for-character. No paraphrase. Cut at sentence boundaries and mark elision.
3. **Characterise the mapping.**

   | Mapping | Meaning | Where |
   |---|---|---|
   | `literal` | Claim language reads on the accused feature / prior-art disclosure | Both |
   | `literal-construction-dependent` | Literal under X; fails under Y | Both |
   | `equivalent` | Equivalent under the *Actavis* doctrine (variant immaterial, unobvious to person skilled in art, not excluded by prosecution history) | Infringement only |
   | `anticipation` | Every element in a single reference, arranged as claimed | Invalidity only |
   | `obviousness-combination` | Secondary reference supplies the missing element; motivation to combine required | Invalidity only |
   | `partial` | Some of the element is present | Both |
   | `not-found` | Element not present | Both |
   | `needs-evidence` | Can't tell from available material | Both |
   | `construction-dependent` | Turns on how a disputed term is construed | Both |

4. **State per cell.** `mapped` / `mapped-equivalent` / `partial` / `not-found` / `needs-evidence` / `construction-dependent` / `anticipation` / `obviousness-combination`.
5. **Flag open questions.** "This maps if [X]. Need [teardown / source code / witness statement / expert] to confirm."

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

### Step 4.5: Equivalents supplements — execute, don't gesture

For every element charted as `literal` where the accused feature is structurally similar but not literally identical — or every element where the `literal` mapping turns on a contested construction — produce a **paired equivalents candidacy row** (infringement mode). Do not footnote "equivalents analysis is separate" without producing the actual equivalents mapping.

Under the *Actavis* doctrine, an equivalent is a variant from the claimed language where: (1) the variant does not materially affect the way the invention works, (2) it would be obvious to the person skilled in the art that the variant achieves substantially the same result in substantially the same way, and (3) the person skilled in the art would not have understood the patentee to have intended strict compliance to be an essential requirement. Flag prosecution disclaimer as a potential exclusion.

A equivalents candidacy row adds a one-paragraph analysis under the *Actavis* criteria, flags prosecution history disclaimer risks, and cites the evidence that would support the equivalent. If equivalents are inapplicable (the element reads literally on the accused product beyond dispute), skip. If `literal` is construction-dependent and equivalents would be the solicitor's/barrister's fallback under the narrower construction, produce the equivalents row.

Format:

```markdown
| [#-EQ] | Element | Accused feature | Actavis analysis | Prosecution disclaimer? | State |
|---|---|---|---|---|---|
| 1b-EQ | "at least one barb" | three-barb opposing-face array | (1) does not materially affect function — anchor retention; (2) obvious to skilled person that array achieves same retention; (3) no indication patentee intended strict numerical compliance. | [needs-evidence: prosecution history] | construction-dependent |
```

As with dependents: if the skill can't produce the equivalents rows for a reason (no accused-product evidence to ground the *Actavis* analysis, no prosecution history available), say so explicitly and route to `needs-evidence`. Do not skip equivalents silently.

### Step 5: Indirect infringement (infringement only)

Flag, don't opine:

- **Indirect infringement (Patents Act 1977, s 60(2))** — supply of means relating to an essential element of the invention, knowing (or it being obvious) that those means are suitable and intended for putting the invention into effect. Distinguish from s 60(1) direct infringement.
- **Joint tortfeasance** — common design between the direct infringer and the defendant.

### Step 6: Invalidity thresholds (invalidity only)

For anticipation (PA 1977, s 2 / EPC Art. 54): every element in a single reference, arranged as claimed.

For obviousness (PA 1977, s 3 / EPC Art. 56): primary reference + secondary reference(s) + a step that is obvious to the person skilled in the art at the priority date. Apply the structured approach from *Pozzoli SPA v BDMO SA* [2007] EWCA Civ 588 `[model knowledge — verify]`:

1. Identify the person skilled in the art and the common general knowledge.
2. Identify the inventive concept of the claim.
3. Identify the differences between the claimed invention and the prior art.
4. Ask whether those differences are obvious to the skilled person or require any degree of invention.

Also flag:
- **PA 1977, s 14(3) / EPC Art. 83** — insufficiency / enablement
- **PA 1977, s 1(2)** — excluded matter (computer programs as such, mental acts, discoveries, etc.)
- **Added matter (PA 1977, s 76 / EPC Art. 123(2))** — claim extended beyond the application as filed
- **Unenforceability** — abuse of process, acquiescence, estoppel (solicitor-only flags)

Invalidity must be proved on the balance of probabilities in UK proceedings.

### Step 7 (review sub-mode): Audit

For each row: is the mapping supported? Is the pin cite accurate? Is the element fully accounted for? What's the strongest counter? What's the rebuttal opportunity? Output verdicts per row (`supported` / `weak` / `unsupported`) and the chart's vulnerabilities.

## Patent-mode guardrails (in addition to shared guardrails)

- **Statement of case requirements.** Infringement and invalidity particulars must be pleaded in the Patents Court or IPEC with the required level of detail per the applicable court guide. A chart out of this skill is a draft, not served particulars.
- **Claim construction candour.** Every construction-dependent row states the construction assumed and the construction under which the mapping fails.
- **Equivalents candour.** An equivalents mapping is not equivalent to a literal one. Flag prosecution history disclaimer per element.
- **Indirect is separate.** Don't fold indirect infringement into direct-infringement rows.
- **Invalidity burden.** State the balance-of-probabilities standard.

---

# MODE 2 — Civil element chart

Map the elements of a cause of action (or defence) against the evidence. The killer outputs are (a) a chart that says what evidence goes with what element and (b) a gap list that tells the solicitor or barrister what's missing.

## Workflow

### Step 1: Identify the claim(s)

- What cause of action? (Or defence?) If multiple counts, chart each separately.
- Which side? Claimant's prima facie case, defendant's defence, defendant's challenge to claimant's prima facie case (summary judgment mode, CPR Part 24). Read `## Side` in the practice profile for the default — `claimant` defaults to mapping the prima facie case (proving the elements); `defendant` defaults to mapping gaps and defences (disproving or avoiding the elements). Confirm the posture matches this matter before starting.
- Which jurisdiction? England & Wales, Scotland, or Northern Ireland. **Elements and authority can differ.** The template library is a baseline for English law; the controlling UK authority or statute controls.
- Which pleading? Load the particulars of claim / counterclaim / defence so the chart tracks the counts actually pleaded, not a generic version.

### Step 2: Load the elements

Three paths:

**(a) Template library.** Reference `references/element-templates.md` (in this skill's directory). Baseline elements for common English law causes of action and common defences, with citations to the leading English authorities. Select the template that matches the pleaded count.

**(b) Custom.** User defines elements, or pastes a jury / bench instruction, a statute, or a count from the particulars of claim to parse. Parse into numbered elements.

**(c) Defences.** Also support mapping defences — limitation (Limitation Act 1980), laches, estoppel, waiver, contributory negligence, volenti non fit injuria, set-off, etc. Defences have their own elements the defendant must prove (or, for some, the claimant must negate once raised).

**Jurisdiction-specific formulations — surface proactively.** If the practice profile's `## Company profile → Core jurisdictions` or the active matter's `matter.md` names **England & Wales, Scotland, or Northern Ireland**, confirm the applicable formulation proactively. Do not assume the English law baseline applies to Scottish or Northern Irish facts without flagging the difference.

Divergences to surface without being asked (non-exhaustive — add to this list as patterns recur):

| Cause of action / defence | England & Wales baseline | Scotland / NI note |
|---|---|---|
| Breach of contract | *Chitty on Contracts* formulation — offer, acceptance, consideration, intention to be legally bound, performance / breach, loss | **Scotland:** Scots contract law has material differences (no consideration requirement; formation rules differ; *mutuality of contract* doctrine). Flag for Scottish solicitors on any Scotland-seated contract. |
| Negligence | *Donoghue v Stevenson* / *Caparo v Dickman* three-part test (proximity, foreseeability, fair/just/reasonable) `[model knowledge — verify]` | **Scotland:** same common-law duty structure broadly, but the system is Scots law. |
| Breach of statutory duty | Statutory tort — the statute must expressly or impliedly create a private right of action | Confirm whether the statute extends to Scotland / NI with the same effect. |
| Defamation | Defamation Act 2013 (England & Wales) — serious harm threshold, publication, identification, defamatory meaning, defences | **Scotland:** Scots law of defamation differs; Defamation and Malicious Publication (Scotland) Act 2021. **NI:** Defamation Act 1955 (NI). Flag jurisdiction carefully. |

When a jurisdiction-specific formulation differs materially from the baseline, the chart opens with a one-line callout:

> **Jurisdiction note:** You told me this is a [Scotland/NI/England & Wales] matter. Here's how [jurisdiction]'s formulation differs from the baseline: [divergence]. The chart below uses the [jurisdiction] formulation. If that's wrong, say so and I'll reload.

Confirm the element list with the user before mapping. If the user's jurisdiction has particular nuances (specialist tribunal, regulatory overlay, specific statutory scheme), ask: "Does the applicable court's procedural rules or this statute's cause-of-action elements add / drop / reword any of these?" If yes, use their version.

### Step 3: Map

For each element:

- **Evidence supporting** — what proves this element? Cite the source with a pin cite.
  - Witness statement — `[Smith WS ¶ 12]`
  - Expert report — `[Jones Expert Rep at 18]`
  - Disclosed document — `[DEF00012345 at 3]`
  - Admission — `[Def's Response to RFI No. 5]`
  - Exhibit — `[Trial Bundle A/14/2]`
  - Contract / document — `[Exhibit C, clause 4.1]`
  - Statute / authority — for purely legal elements
- **Verbatim quote** where the evidence is documentary. No paraphrase.
- **Evidence contradicting** — what cuts the other way? Cite it. This is the row's vulnerability.
- **Strength** — `strong` / `moderate` / `weak` / `none`. Keep it simple. Over-calibrated strength scores are noise; `weak` and `none` are the rows that matter.
- **State per cell** — `supported` / `partial` / `disputed` / `gap` / `needs-disclosure`.

### Step 4: Gap detection — the killer output

After mapping, produce a gap list. This is the point of the chart.

> **Elements with thin or no evidence:** [list]
>
> - If asserting (claimant): these defeat your particulars of claim's viability, your summary judgment (CPR Part 24) response, or your case at trial. Close them before the next application.
> - If defending: these are your CPR Part 24 targets and your no-case-to-answer submission. The claimant has to prove each element; a gap is a defence.
> - If pre-disclosure: these are your disclosure priorities — the witness interviews, document requests, and interrogatories that turn a gap into `supported` or confirm `none`.

Gap detection is not a conclusion about the merits. It's a map of where the case is light.

### Step 5: Phase-aware framing

Ask the phase. Same chart; different framing on the output:

- **Pre-filing / pleadings.** Does the particulars of claim plead each element with sufficient detail? Any element pleaded in conclusory terms without factual underpinning is a strike-out / summary judgment target under CPR Part 24 or a request for further information under CPR Part 18.
- **Disclosure (CPR Part 31 / PD 51U).** For each `gap` or `needs-disclosure` element, what disclosure is needed? Which custodians, which document categories, which specific searches.
- **Summary judgment (CPR Part 24).** For each element, is there a real prospect of success? A `supported` cell for the applicant with no realistic counter is summary judgment ammunition; a `disputed` cell is summary-judgment-defeating.
- **Trial.** Order of proof. Which witness proves element 1, which exhibit proves element 2, who authenticates, what is the foundation. The chart becomes the trial outline.

### Step 6 (review sub-mode): Audit

For an opposing party's CPR Part 24 application, a strike-out application, or external solicitors' draft: for each element, does their cited evidence actually prove it? Where is their chart thin? What is your strongest counter?

## Civil-mode guardrails (in addition to shared guardrails)

- **Jurisdiction.** The element list is a baseline for English law. Always confirm the controlling UK authority, statute, or Practice Direction. State the source on the chart's `_elements` sheet.
- **Pleaded counts only.** Chart what is actually pleaded. Don't add a count the particulars of claim doesn't allege just because the facts might support it — that's a different analysis.
- **Defences.** If mapping defences, note whether the burden is on the defendant (most) or whether raising the defence shifts a burden to the claimant.
- **"Gap" ≠ "case over."** A gap is a lead. Disclosure, a witness statement, or an expert report can close it. The chart shows where to dig.

---

# Shared chassis (both modes)

## Output

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` `## Outputs`.

### Markdown table (always)

One table per claim / defence / patent-claim per target.

**Patent mode example:**

```markdown
| [#] | Element (verbatim) | Accused feature | Evidence (pin-cited) | Mapping | State | Verified |
|---|---|---|---|---|---|---|
| 1a | "a processor configured to..." | SoC per datasheet | [Datasheet p. 7] "..." | literal-construction-dependent | mapped | ☐ |
| 1b | "means for [function]" | [alleged equiv.] | [source, file.c:124] "..." | needs-evidence | needs-evidence | ☐ |
```

**Civil mode example:**

```markdown
| [#] | Element | Evidence supporting (pin-cited) | Evidence contradicting | Strength | State | Verified |
|---|---|---|---|---|---|---|
| 1 | Existence of a contract | [Ex. 3, MSA cl. 1; Smith WS ¶ 22] | none | strong | supported | ☐ |
| 2 | Claimant's performance | [Jones WS ¶¶ 4–9] | [Doe WS ¶ 101: "they never delivered Phase 2"] | moderate | disputed | ☐ |
| 3 | Defendant's breach | — | [Doe WS ¶ 101] | none | gap | ☐ |
| 4 | Causation | — | — | none | needs-disclosure | ☐ |
| 5 | Loss | [Expert Rep at 18 — £2.4M lost profits] | [Def's Expert Rep at 6 — critiques methodology] | moderate | disputed | ☐ |
```

Follow with:
- **Defences / thresholds** (patent mode: invalidity / indirect / sufficiency flags; civil mode: defence flags, strike-out / summary judgment flags pre-pleading)
- **Gap list** (civil mode) / **needs-evidence list** (patent mode) — **the priority output**
- **What cuts which way — summary** — strongest elements, weakest elements
- **Conclusion line** — *"This skill does not conclude."* Elements mapped/supported: [list]. Elements needing evidence / in a gap state: [list]. Elements construction-dependent (patent) / disputed (civil): [list]. Solicitor / barrister judgment required.
- **Citation verification** — every pin cite, case, paragraph, witness statement page, document reference must be verified against the source.

### CSV (always)

Two files per chart:
- `[chart-slug].csv` — values
- `[chart-slug]_sources.csv` — verbatim quotes, pin cites, notes

**CSV / spreadsheet cell safety.** Before writing any cell value, check the first character. If it is `=`, `+`, `-`, `@`, tab (`\t`), or carriage return (`\r`), prepend a single apostrophe (`'`) to neutralise Excel/Sheets formula interpretation. Verbatim evidence from adversarial sources (opposing solicitors' contentions, competitor product manuals, third-party prior art, scraped web pages, witness statements, disclosure productions) can contain strings that a spreadsheet will execute as formulas, turning the chart into a data-exfiltration vector when a solicitor opens it. RFC 4180 quoting alone does not defeat this. Apply the apostrophe prefix in CSV, XLSX, and Sheets outputs. Log cells where this was applied so the reviewer can see which quotes were neutralised.

### Spreadsheet (Excel or Sheets)

Ask which the team works in. Use a consistent cell-level citation model, state-based colour coding, `Verified` column, and schema sheet:

- One row per element (or element × target if comparing multiple targets)
- Each evidence column paired with a hidden source column containing the verbatim quote and pin cite; cell comments (Excel) or notes (Sheets) surface the quote on hover
- Colour coding by state:
  - *Patent:* white = `mapped`, yellow = `construction-dependent` / `partial` / equivalents, orange = `needs-evidence`, red = `not-found`
  - *Civil:* white = `supported`, yellow = `partial` / `disputed`, orange = `needs-disclosure`, red = `gap`
- `Verified` column per evidence column, blank by default — reviewer marks it
- `_elements` sheet documenting the element source: leading English authority, statute (cite in OSCOLA), or patent-claim parse. This is what makes the chart auditable — a reader can see where the elements came from.
- `_gaps` sheet listing every `gap`, `needs-evidence`, or `needs-disclosure` row with what's still needed
- For patent mode only: `_claim-parse` sheet (element decomposition), `_constructions` sheet (disputed terms and assumed constructions)

Apply the apostrophe-prefix neutralisation to every cell written into the spreadsheet.

Prepend the work-product header as the top row. Alongside it, include:

> This chart is derived from source documents that may be privileged (legal advice privilege or litigation privilege), confidential, or both. It inherits the sources' LPP and confidentiality status — distribution beyond the LPP circle can waive privilege. Store with the matter's privileged files and make distribution decisions deliberately. Nothing in this chart has been filed or served; it is a draft for solicitor/barrister review.

### Filename and location

- Patent infringement: `claim-chart-infringement-[patent#]-claim[#]-[target]-YYYY-MM-DD.{md,csv,xlsx}`
- Patent invalidity: `claim-chart-invalidity-[patent#]-claim[#]-[ref]-YYYY-MM-DD.{md,csv,xlsx}`
- Civil: `element-chart-[count-slug]-[side]-YYYY-MM-DD.{md,csv,xlsx}`
- Review: `chart-review-[subject]-YYYY-MM-DD.{md,csv,xlsx}`

If matter workspaces enabled and a matter is active: `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/<matter-slug>/claim-charts/`. Otherwise: `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/claim-charts/`. Surface the path. Append a one-line entry to the matter's `history.md`.

## Summary readout

After the chart is written, give a one-screen readout:

- Claim(s) / count(s) / patent claim(s), target(s), jurisdiction, phase
- Elements charted · supported/mapped · partial · disputed · gap / needs-evidence · not-found
- The gap list (civil) or needs-evidence list (patent) — **this is the priority list**
- Where the output files are
- Reminder: every cell is a lead. The chart is a draft, not a contention / skeleton argument / order of proof.

## Non-lawyer gate

If `## Who's using this` Role is Non-lawyer:

> This chart is a research draft, not a legal filing. Serving contentions, issuing proceedings, or relying on this for a merits opinion has professional-responsibility and substantive legal consequences. A solicitor or barrister in the relevant jurisdiction must review before this is used for any legal purpose.
>
> Here's a one-page brief to bring to a solicitor or barrister:
>
> [Generate: claim / patent, side, jurisdiction, phase, elements, supported / gap / needs-disclosure counts, the three most load-bearing open questions.]

Deliver the chart alongside the brief.

## Shared guardrails — checklist

- **Citation verification.** Every pin cite (paragraph, page, witness statement page:line, document reference) is a claim about the source. The solicitor or barrister verifies. The skill does not fabricate cites — if a cite cannot be produced, the cell is `needs-evidence` or `gap`.
- **Source attribution.** Every verbatim quote has its source in the companion CSV and the spreadsheet's hidden source column. A quote without a source is not evidence.
- **No silent supplement.** Thin evidence means `needs-evidence` / `gap`, not "extrapolate." Do not fill from web search, training data, or "how these cases usually go" to close a gap.
- **Matter workspace check.** Confirm the active matter before writing. Never write matter A's chart into matter B's folder.
- **Decision posture.** When uncertain whether an element is met, flag; do not decide. `partial` tells the solicitor what part is missing.
- **Formula injection.** Every cell written to CSV / XLSX / Sheets is checked for leading `=`, `+`, `-`, `@`, `\t`, `\r` and prefixed with `'`. Default: neutralise-then-write.
- **Elements are jurisdiction-specific.** The template library is a baseline. The controlling UK authority or statute controls.
- **A chart is not a skeleton argument, a filing, or a contention.** Every output is a draft.

---

## Relationship to other skills

- `litigation-legal-uk:chronology` — the chronology is the timeline; the element chart is the proof matrix. A chronology entry often becomes a cell's evidence cite.
- `litigation-legal-uk:witness-examination-prep` — a `needs-disclosure` cell often becomes a witness preparation topic. After witness statements, new evidence fills cells.
- `litigation-legal-uk:brief-section-drafter` — a summary judgment application's skeleton argument fact section is often built directly off the supported rows of an element chart.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the solicitor or barrister picks.

## What this skill does not do

- **It does not conclude.** Not infringement, not non-infringement, not liability, not non-liability. Ever.
- **It does not decide claim construction** (patent) or **the controlling elements** (civil). It flags disputed terms / baseline elements and charts under stated assumptions.
- **It does not meet the balance-of-probabilities burden for invalidity** or **the civil standard at trial**. It produces a prima facie draft for solicitor/barrister review.
- **It does not substitute for expert analysis.** Source code review, teardowns, technical experts, quantum experts are separate work products this chart routes to, not replaces.
- **It does not serve, file, or sign anything.** Every output is a draft. A solicitor or barrister serves and files.
- **It does not extrapolate.** If the evidence isn't there, the cell is `needs-evidence` / `gap` — never a guess.
