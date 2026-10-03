---
name: writing-legal
title: Legal register (`legal`)
description: 'ALWAYS load BEFORE drafting, revising or grading LAW REVIEW prose — ''write the article'', ''draft this Part'', ''revise my note'', ''polish the law review piece'', ''does this sound like a law review article'', ''edit my seminar paper'', ''is this Part well written'', ''should I write This Article or This paper'', ''do I cross-reference by Part or Section'', ''how do I transition between Parts'', ''the sections don''t connect'', ''is pursuant to legalese''. Covers T14 flagship articles, student notes, seminar papers and any legal scholarship carrying footnotes and Bluebook short forms. This skill carries ONLY what is additional to the base register: load `writing-general` alongside it — the diction, tic, vindicated-phrase and formatting rules live there and are assumed here. Do NOT load this for a finance or accounting journal submission (use `writing-econ`) or for a comment letter, memo, brief or professional email (`writing-general` alone) — importing a law review rule into
  either of those makes the prose worse.'
author: edwinhu
author_url: https://github.com/edwinhu/workflows/tree/main/skills/writing-legal
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal register (`legal`)

**What this skill carries** — grep `references/` for any subject the names below miss:
!`d=${CLAUDE_SKILL_DIR}; command -v skill-toc >/dev/null 2>&1 && exec skill-toc "$d"; s=$HOME/.claude/skills/plugin-utils/bin/skill-toc; [ -x "$s" ] && exec "$s" "$d"; echo "(skill-toc unavailable: references and scripts are NOT listed here — install the plugin-utils plugin, or start a new session so its bin/ reaches PATH)"`

**The base is `writing-general`, and it is assumed loaded alongside this file.** Everything below is
what is *additional* for law review prose. Nothing from the base is restated here.

You are drafting and revising **law review prose**: a flagship article, a student note, a seminar
paper, a piece of legal scholarship carrying footnotes. Voice, citation form and register follow the
conventions below.

Everything here is measured, not asserted. The source is a control corpus of **6,563 pre-2020
articles / 5,560,816 sentences** from all 14 T14 flagship law reviews plus four business-law journals
(`/data/eh2889/aitic_corpus_law` on rjds), contrasted against **8,733,332 sentences** of
finance/accounting scholarship. Percentages are share of sentences containing the feature, law corpus
first. Rates written `n/M` are hits per million sentences.

## Register: what actually distinguishes this corpus

| feature | law | finance | do |
|---|---|---|---|
| `we` | **0.87%** | 7.75% | Avoid the authorial `we`. It is nine times rarer here. Prefer the impersonal construction or `This Article`. |
| `we find / show / document` | **0.02%** | 0.58% | Effectively absent — 29× rarer. Never open a claim this way. Say what is true, then cite. |
| `supra` / `infra` / `id.` | **1.91%** | 0.00% | Bluebook short forms are the norm and appear in roughly one sentence in fifty. |
| quotation marks | **8.36%** | 1.68% | Quote sources directly and often — five times the rate of the finance register. |
| `court` / `holding` / `held` / `statute` / `doctrine` | **6.41%** | 0.73% | The vocabulary of authority is the substance, not decoration. |
| semicolons | **4.33%** | 2.27% | Twice the finance rate. Long coordinate structures are idiomatic here. |
| `may` / `might` | **3.56%** | 1.99% | Hedging is register-appropriate. Do not strip it out to sound decisive. |
| `Part I` / `Part II` | **0.20%** | 0.00% | Cross-reference by **Part**, never by "Section 2". |
| `This Article` | **0.06%** | 0.00% | The self-reference. Capital A. `This Note` for student work. |
| `This paper` | 0.02% | **0.28%** | Wrong register. Do not write it. |
| parentheticals | 1.93% | **4.73%** | Less parenthetical throat-clearing than the finance register; put the qualification in a footnote. |
| `regression` / `coefficient` | 0.05% | **2.25%** | Empirical vocabulary is 45× rarer here. If the Article is empirical, it still narrates rather than tabulates. |

## Conventions

- **Footnotes carry the citations.** Substantive text goes in the body; support, parentheticals and
  qualifications go below the line. Never inline a full citation in body prose.
- **Cross-reference by Part** (`Part II.B`), not section number.
- **Signals matter**: `see`, `see also`, `cf.`, `but see`, `e.g.` — italicized, and each means
  something different. Do not use `see` where the source states the proposition directly.
- **`supra` / `infra` / `id.`** for short forms once a source is established.
- **Small caps** for journal names in citations.
- **Three body Parts is the default** — Background, the Argument with counterarguments folded in, the
  Prescription. Splitting into four or five Parts is an exception you reach, not a starting point.

## Boundaries: the objection hinge

**Every Part and Section boundary is a hinge. The reader crosses the heading already holding a
reasonable objection, plus a commitment that the next unit answers it and a statement of what the
answer is.** This is a brief's discipline carried into an Article, and the source is Bebchuk &
Kastiel, *Controllers Unbound* (2026). **Copy its structure, not its sentences.** The prose is
brief-like rather than good. A variant of "it might be argued" carries six boundaries (III.A, III.B.1, VIII.A–D), and
"We would like to stress" and "ten times(!)" appear too. Build the hinge the
way the table shows, then write each sentence to the `writing-general` rules. A hinge has two
halves, and a boundary missing either half has no transition:

1. **The objection**, stated the way a reasonable reader would state it, without attribution:
   `It might be argued, however, that…`, `Some might question our conclusions on the grounds
   that…`. Concede the part that is true (`We fully agree with this proposition.`). Say who holds
   the view in a footnote, never at the hinge.
2. **The promise, and it names the answer, not the topic.** Write `As explained below, however,
   SB 21 leaves public investors vulnerable to partial freezeouts`, never `We now turn to partial
   freezeouts`. Bebchuk's `as we now explain` and `the question to which we now turn` are his
   idiolect, at 0.00/M and 0.18/M in the law corpus. Use the form, not the phrase.

**Measured** with `ai-tic`'s `fp-check.sh` triage (line-level, so absolute rates undercount phrases
that wrap across lines; the law/finance ratio is like for like). The law corpus averages about 850
sentences per article.

| phrase | law | finance | what it tells you |
|---|---|---|---|
| `it might be argued` | **52.7/M** | 6.5/M | The objection voice is legal register, 8× the finance rate |
| `some might question / argue / object` | **11.7/M** | 2.1/M | 5.7× |
| `one might argue` · `it could be argued` | 39.4 · 35.4/M | 22.4 · 19.0/M | Under 2×, so these forms are shared rather than marked |
| all four objection openers | ~139/M | ~50/M | About **one every eight law articles**. Bebchuk's six in one Article is roughly 50× the norm |
| `as explained below, however` | **2.7/M** | 0.46/M | The answer-naming promise is law-marked (5.9×) |
| `we (now) turn to` | 24.5/M | **140.8/M** | The topic-only promise is finance register (5.8×) |
| `the next section` · `in this section` | 56 · 137/M | **377 · 1,165/M** | Finance signposts by Section, 7–8× the law rate |
| `this Part` · `the next Part` | **598 · 53/M** | 31 · 2.4/M | Law signposts by Part |
| `thus far` | 158/M | 123/M | Shared, and safe for lifting an assumption |

| boundary | the move in *Controllers Unbound* |
|---|---|
| Section → Section (hinge closes the unit) | III.A ends: "It might be argued, however, that fiduciary duties and norms … generally lead directors who are independent … to oppose decisions that would adversely affect public investors. Whether this is in fact the case is the question to which we now turn." III.B's first sentence answers it: controllers "should commonly be able to have in place at least two independent directors that tend to go along." |
| Subsection → subsection | III.B.1 ends: "It might nonetheless be argued that … Independent directors are moral agents and might elect 'to do the right thing.' We fully agree with this proposition. However, as we now explain, the constraint this places on controlling shareholders is far weaker than it may appear given controllers' power to select, and reselect as needed …" |
| Part → Part by lifting an assumption (hinge opens the unit) | Part V opens: "Thus far, the discussion has examined the rules governing controlled companies taking the existence and number of such companies as given. An important conclusion of our analysis, however, is that SB 21 … will also have a major impact on the incidence and nature of control blocks." VI.B uses the same move. |
| An objection Part, in the roadmap and its opener | Intro: "Some might question our conclusions on the grounds that … various mechanisms could provide substitute protections. Part VIII addresses such objections." The Part VIII opener ends with the verdict first: "these four 'mechanisms,' will fail to adequately make up for the weakening of controller constraints." |
| A rebuttal Section's opener | VIII.A: "One might argue that controllers could be partially deterred … However, as explained below, … the expected decline in the market value of the controller's block rarely discourages the controller …, and almost never does it in dual-class controlled companies." The objection comes in sentence one and the verdict in sentence two. |
| A Section with no natural objection | IV.D: "The drafters of SB 21 accepted that controller-favoring freezeouts raise especially serious concerns … As explained below, however, SB 21 leaves public investors vulnerable to … 'partial freezeouts.'" The concession stands in for the objection. |

- **The promise is a debt.** The first paragraph of the next unit must deliver the proposition the
  promise named, and deliver that exact one. A hinge that promises Y and then delivers Y′ is worse
  than no hinge.
- **Cross-references are directional and numbered:** `In Part II above`, `As Part V below will
  further detail`, `as explained in Section B`.
- **Grading TRANSITION on a legal draft** (`writing/references/writing-checks.md`) means quoting
  both halves at every boundary. If either half is missing, report a finding.

| About to | Why wrong | Do instead |
|---|---|---|
| End a unit on `In sum, …` and open the next with its topic | Nothing is handed forward. It is the one boundary in *Controllers Unbound* without a hinge: VI.A and VI.B end on the same "In sum" paragraph, word for word | End on the objection the next unit answers, or open the next unit by lifting an assumption (`Thus far … taking X as given. However, …`) |
| Write `We now turn to X` / `The next section examines X` | The promise names only a topic, so the reader has no claim to test the next unit against. It is also the finance register's signpost: `we turn to` runs at 140.8/M in finance and 24.5/M in law | `As explained below, however, [answer]`, or `Part V shows that [answer]` |
| Open a Section with `This Section discusses X` | Meta-commentary with no claim | `In this Section, we explain that [claim]`, or objection + `however` |
| Reuse one objection formula (`It might be argued`) at boundary after boundary | This is Bebchuk's tic, not his method. The law corpus uses the four objection openers together about once every eight articles | Use a formula for at most one or two hinges per Article. Elsewhere state the objection as a plain claim (`Fiduciary duties might seem to restrain these directors.`) or use a concession (`The drafters accepted that …`) |
| Attribute the hinge objection to a named scholar in the body | Turns the boundary into a literature review | Keep the voice impersonal at the hinge and put the name in the footnote |

## Volokh, run through the law corpus

The source guide is Volokh's *Academic Legal Writing*, distilled in full at
`${CLAUDE_PLUGIN_ROOT}/skills/writing/references/volokh-distilled.md` — read it there for the full
text of any rule below. **Where this file and that guide disagree, this file controls.** Volokh's
prescriptions were checked against the same corpora and sorted three ways.

### Ship

| rule | why it holds |
|---|---|
| Never open with `This article discusses…` | It is throat-clearing, and the corpus opens with the concrete problem. Hook with the question or the controversy. |
| Confront counterarguments **in the Part that makes the claim** | Deferring them to a separate Part reads as evasion and forces the reader to hold the objection unanswered. |
| Read the original source | A case cited from a headnote, a treatise, or training data is an unverified claim presented as fact. Even Supreme Court opinions misstate precedents. |
| Synthesize precedents; do not summarize case by case | `Courts generally hold X, except when Y` — not a sequential digest. |
| Be precise with terms | `murder` ≠ `homicide` ≠ `killing`; `foreign-born` ≠ `noncitizen`; `children` is ambiguous until you give the age range. |
| Understate criticism | `mistaken`, not `idiotic`. Overstating raises your own burden of proof. |
| Unpack the metaphor | `slippery slope` and `chilling effect` hide the argument rather than making it. Name the mechanism. |

### Advisory

| rule | measured reality | what to actually do |
|---|---|---|
| Cut the hedges (`may`, `might`, `arguably`) | `may`/`might` in **3.56%** of law sentences, 1.8× the finance rate | Hedging is register-appropriate here. Cut `arguably` where it substitutes for the argument; leave the rest. |
| Prefer active voice | passive 7.91% law vs 8.55% finance — not a register marker | Ask who acted. Do not convert on principle. |
| Avoid long coordinate sentences | semicolons **4.33%**, twice the finance rate | Long coordinate structures are idiomatic in this corpus. Break the ones that lose the reader, not the ones that are merely long. |

### Dropped

| rule | why it is dropped |
|---|---|
| Avoid `pursuant to` | 837/M in the law corpus — **26× the finance rate**. This is not legalese to be purged; it is the legal register. Flagging it teaches the drafter to write like an economist. |
| Avoid the passive throughout | See above. The measurement refutes the rule as a register claim. |

## Vindicated in this corpus specifically

Beyond the shared list in `writing-general`: `To be sure,` runs **194.0/M** here (against 11.5/M in
finance) and `Admittedly,` **63.3/M**. `cuts against` (13.1/M) and `cuts the other way` are standard
analytical vocabulary. A reviewer who flags any of these as an AI tell is wrong, and the corpus says
so.
