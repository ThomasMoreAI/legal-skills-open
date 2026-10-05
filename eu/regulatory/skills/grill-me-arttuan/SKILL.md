---
name: grill-me-arttuan
title: Grill Me
description: Interrogate the user about their product until every regulation-relevant fact is pinned down, then gate the build on the answers
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/grill-me
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Grill Me

The gate. Before you write a line of the thing they asked for, you find out what
it actually is — in the specific, unflattering detail that regulation turns on —
and you **do not proceed** until the facts that decide lawfulness are on the
record or explicitly, attributably accepted as unknown.

This is the main skill in this repo. Every other skill consumes what it
produces.

> **Not legal advice.** This skill produces questions, findings and
> documentation. It does not produce legal conclusions, and it does not
> substitute for a lawyer or a DPO. Its highest-value output is a brief that
> makes an hour of a lawyer's time worth ten.

```
  "build me X"
       │
       ▼
  read the repo first ──► what can you answer without asking?
       │
       ▼
  orient (4 questions) ──► which branches open?
       │
       ▼
  ┌─► ask ──► grade ──► SPECIFIC? ─── yes ──► record ──┐
  │            │                                        │
  │            └── VAGUE/ASSUMED ──► re-ask narrower ───┤ (max 2)
  │            └── UNKNOWN ──────► record owner + date ─┤
  └───────────── new branch opened by the answer ───────┘
       │
       ▼
  findings ──► gate: blocked | conditional | clear
       │
       ▼
  build what is clear · refuse what is blocked · say exactly which is which
```

## Use this when

- **Before building anything that touches people in the EU.** Which is most
  software: a signup form, a log file with IPs, and an analytics snippet are
  each enough.
- Before adding AI to an existing product — the classification question is
  cheapest to answer before the model is wired in and most expensive after.
- Before a launch into a new EU market, a new user category (minors, employees,
  patients), or a new data category.
- When inheriting a codebase nobody has scoped, as a structured way to find out
  what it actually does.

**Do not use this when** the user has already been through it and the brief is
current — re-run `eu-compliance-gates` instead, which is the cheap incremental
check. And do not use it as an audit of something already shipped: it asks
"what will you build", and the honest post-hoc version is `eu-evidence-pack`
plus a lawyer.

**Do not use this to delay work that is obviously fine.** A static marketing
site with no forms, no analytics and no cookies needs four questions and a
`clear`. If the grill takes forty minutes on that, nobody will run it on the
thing that needed it.

## Ask first

Four orientation questions, before anything else. They decide which branches
open, and asking them first avoids forty questions about a regime that does not
apply.

1. **"In one paragraph, what does the product do, and who uses it?"**
   Not the pitch — the mechanics. What goes in, what comes out, who is affected
   by the output.
2. **"Are any of your users, customers or the people you hold data about
   physically in the EU or EEA?"**
   Includes employees, applicants, and visitors to the marketing site. If yes,
   GDPR is in scope regardless of where the company is (Art. 3(2)).
3. **"Does anything in it use machine learning, an LLM, or an automated rule
   that decides something about a person?"**
   Phrase it that way. "Do you use AI" gets a marketing answer; this gets an
   engineering one. Note that the last clause catches automated decisions that
   are not AI at all but still engage Art. 22 GDPR.
4. **"Is this software you host, software you ship to someone else's machine,
   or a physical product with software in it?"**
   Decides CRA, and decides whether you are a provider or a deployer under the
   AI Act.

Then, before question five: **read the repository.** The dependency manifest
names the vendors. The schema names the fields. The nginx config names the log
format. The IaC names the region. Ask about what you could not find, and show
what you did find — *"I see `stripe`, `posthog-js` and `@sentry/node` in
`package.json`. Are those the only third parties that see user data?"* is a
better question than asking cold, and it proves you looked.

See `references/how-to-ask.md` for the method: ask about the system, not about
the law, and do the legal mapping yourself.

## What the law requires

The gate is not a policy preference. Three regimes require the decision to be
made *before* the build, not audited after it:

- **GDPR Art. 25 — data protection by design and by default.** The obligation
  attaches "at the time of the determination of the means for processing", which
  is architecture time. A control retrofitted after launch does not satisfy
  Art. 25; it mitigates a breach of it.
- **GDPR Art. 35 — DPIA.** Required *prior to* the processing where it is likely
  to result in a high risk. A DPIA written after go-live is evidence of the
  breach, not compliance with the duty.
- **AI Act Art. 9 — risk management** for high-risk systems is "a continuous
  iterative process run throughout the entire lifecycle", explicitly including
  design. And **Art. 5 prohibited practices** cannot be mitigated at all: if the
  product depends on one, there is no compliant version of it to build.
- **CRA Annex I** requires products to be designed, developed and produced to
  ensure an appropriate level of cybersecurity, and to ship with **no known
  exploitable vulnerabilities**. That is a build-time property.

And the accountability principle (**Art. 5(2) GDPR**) requires you to be able to
*demonstrate* compliance. The brief this skill produces is that demonstration —
which is why every claim in it has to trace to an answer.

## The question bank

Organised by branch. A branch opens when its trigger is met; otherwise every
question in it is skipped and that fact is recorded as a ruled-out regime.

Questions are numbered so findings can cite them (`question: Q-11`).

### Branch A — always (GDPR core)

| # | Ask | Why |
| --- | --- | --- |
| A-01 | "List every field you store about a person. Include IDs, IP addresses, device identifiers, timestamps and anything in free-text fields." | Establishes the actual scope. Almost everyone under-reports. |
| A-02 | "For each of those, what is it *for*? One purpose per line — if a field serves two purposes, list it twice." | Purpose limitation (Art. 5(1)(b)); lawful basis is per purpose, not per product. |
| A-03 | "For each purpose: if a user told you to stop that processing tomorrow, what would break?" | The best proxy question for lawful basis. "Nothing" → it was not necessary. "They cannot use the product" → contract, not consent. |
| A-04 | "Anything about health, ethnicity, politics, religion, union membership, sex life or orientation, biometrics used for identification, or genetics — including anything that could be *inferred* from what you store?" | Art. 9. The inference clause matters: a CV free-text field routinely contains all of these. |
| A-05 | "Are any of the people under 18? How would you know?" | Art. 8; national age of consent varies between 13 and 16. "We don't ask" is an answer with consequences. |
| A-06 | "How long do you keep each category, and what deletes it?" | Art. 5(1)(e). "As long as necessary" is `VAGUE` — re-ask for a number and a mechanism. |
| A-07 | "Show me the code path that deletes a person's data. If there isn't one, say so." | Art. 17. The single most reliable question in this bank, because it has a checkable answer. |
| A-08 | "Name every third party that receives or can access this data: infrastructure, analytics, error tracking, support tools, AI APIs, email, payments." | Art. 28. Cross-check against the dependency manifest — this answer is usually shorter than the manifest. |
| A-09 | "For each: where are their servers, and where is their support staff?" | Chapter V. Support access from a third country is a transfer even when the data never moves. |
| A-10 | "Who in your organisation decides what data is collected and when it is deleted?" | Settles controller vs processor, which the contract often gets wrong. |

### Branch B — opens if any automated decision or model affects a person

| # | Ask | Why |
| --- | --- | --- |
| B-01 | "What decision does the output change, and what happens to the person if it is wrong?" | The classification question, asked in engineering terms. |
| B-02 | "Is the decision made solely by the system, or does a human review it? If a human reviews it — in the last hundred cases, how often did they go against it, and did they see anything the system did not?" | Art. 22 GDPR, and AI Act Art. 14. Rubber-stamp oversight is not oversight, and the follow-up is what exposes it. |
| B-03 | "Does the system infer, rank, score or categorise individual people?" | Blocks the Art. 6(3) derogation from high-risk. |
| B-04 | "Is it used in any of: recruitment or worker management; education or exam scoring; credit or insurance decisions; access to public benefits or essential services; law enforcement; migration or borders; justice; critical infrastructure safety; biometric identification or categorisation?" | Annex III, read out as a list. Do not ask "is it high-risk". |
| B-05 | "Does it recognise emotions, categorise people by biometrics, or scrape faces to build a database?" | Art. 5 prohibited practices territory. A yes here is a potential **blocker**, not a condition. |
| B-06 | "Where did the training or fine-tuning data come from, and what is your right to use it for this?" | Art. 10 AI Act **and** Art. 6 GDPR — these are separate and both required. |
| B-07 | "Do you build the model, buy it, or call someone's API? Do you put your name on the output product?" | Provider vs deployer. Art. 25 AI Act: a deployer who rebrands, substantially modifies, or repurposes to a high-risk use becomes a provider. |
| B-08 | "Do users know they are talking to a machine, and is generated content marked as generated?" | Art. 50 transparency. Applies at *every* risk tier, including minimal. |
| B-09 | "Do the people running this understand its limitations well enough to spot a wrong answer?" | AI Act Art. 4, AI literacy. |

### Branch C — opens if anything is stored on or read from a user's device

| # | Ask | Why |
| --- | --- | --- |
| C-01 | "List everything that writes to or reads from the browser before the user clicks anything — cookies, `localStorage`, `sessionStorage`, pixels, fonts loaded from a third party, fingerprinting." | ePrivacy Art. 5(3). Much broader than cookies. |
| C-02 | "For each: strictly necessary to deliver what the user asked for, or not?" | The only exemption. Analytics is not strictly necessary, however much you want it to be. |
| C-03 | "Is rejecting as easy as accepting — same number of clicks, same prominence?" | EDPB position, and DSA Art. 25 dark patterns where it applies. |
| C-04 | "When someone withdraws consent, what actually stops?" | Art. 7(3). Frequently nothing stops. |

### Branch D — opens if you place a product with digital elements on the market

| # | Ask | Why |
| --- | --- | --- |
| D-01 | "Is it sold, licensed, bundled, or monetised in any way — including open source with a paid tier or paid support?" | Decides CRA scope. Non-monetised FOSS is outside; monetised is not. |
| D-02 | "How long will you ship security updates, starting when?" | The support period. Must be stated, and there is a five-year expectation. |
| D-03 | "Can you produce an SBOM from your build today?" | Annex I Part II. If the answer is no, that is a concrete, closeable finding. |
| D-04 | "Where does someone report a vulnerability to you, and who reads it?" | Coordinated disclosure policy. A `security.txt` and a monitored inbox is the minimum. |

### Branch E — opens if the entity may be in a NIS2 sector

| # | Ask | Why |
| --- | --- | --- |
| E-01 | "Headcount and annual turnover?" | The size cap. Ask early; it also decides EAA and DSA exemptions. |
| E-02 | "Is any part of the business in energy, transport, banking, health, water, digital infrastructure, cloud, data centres, managed IT services, public administration, postal, waste, chemicals, food, manufacturing, online marketplaces, search, social networking, or research?" | Annex I and II, read out. Many SaaS companies are 'cloud computing service providers' and do not know it. |
| E-03 | "Which Member States are you established in?" | NIS2 is a Directive. The binding text is national and the transpositions differ. |
| E-04 | "Has your board or management formally approved your security measures, and been trained on them?" | Art. 20. Personal accountability for management; usually the first thing asked for. |

### Branch F — opens if users can post content others see

| # | Ask | Why |
| --- | --- | --- |
| F-01 | "Can a user publish something another user sees? Comments, profiles, uploads, reviews, messages?" | Makes you a hosting service under the DSA. |
| F-02 | "How does someone report illegal content, and what happens then?" | Art. 16 notice and action. |
| F-03 | "When you remove something or suspend an account, is the user told why?" | Art. 17 statement of reasons. |
| F-04 | "Do you rank or recommend content, or run ads? Are minors involved?" | Arts. 26-28. Profiling-based ads to minors are prohibited. |

### Branch G — opens if it is a consumer product or service in an EAA category

| # | Ask | Why |
| --- | --- | --- |
| G-01 | "Is it e-commerce, consumer banking, e-books, transport, telephony, or audiovisual media — sold to consumers in the EU?" | EAA scope. |
| G-02 | "Can the primary task be completed with a keyboard only, at 200% zoom, with a screen reader?" | The testable version of "is it accessible". |
| G-03 | "Headcount and turnover?" | Microenterprise service exemption needs **both** under 10 staff **and** turnover or balance sheet at or below €2M. |

### Branch H — always, closing

| # | Ask | Why |
| --- | --- | --- |
| H-01 | "Who is accountable for this if a regulator writes to you next month?" | Every finding needs an owner. "Nobody" is a finding in itself. |
| H-02 | "Do you have a DPO, or outside counsel who has seen this?" | Decides whether findings go to someone or nowhere. |
| H-03 | "Is there anything you have been hoping I would not ask?" | Ask it exactly like this, at the end. It works more often than it has any right to. |

## The grading

Every answer is graded before it is recorded. This is the mechanism that makes
this a gate instead of a form.

```python
from dataclasses import dataclass
from enum import Enum


class Grade(str, Enum):
    SPECIFIC = "specific"   # names fields, vendors, countries, days, people
    VAGUE = "vague"         # "standard stuff", "the usual", "as long as needed"
    ASSUMED = "assumed"     # "I think", "should be", "probably"
    EVASIVE = "evasive"     # answers a different question
    UNKNOWN = "unknown"     # "I don't know" - a PASSING answer


PASSES = {Grade.SPECIFIC, Grade.UNKNOWN}

HEDGES = ("i think", "should be", "probably", "pretty sure", "i believe", "afaik")
VAGUE_MARKERS = ("standard", "the usual", "normal stuff", "as long as needed",
                 "as needed", "not much", "nothing special", "just the basics",
                 "industry standard", "best practice")


def grade(answer: str, *, expects: str) -> tuple[Grade, str]:
    """`expects` is what a specific answer must contain: 'list' | 'duration' |
    'country' | 'person' | 'yes_no_plus_detail'."""
    text = answer.strip().lower()
    if not text:
        return Grade.VAGUE, "empty"
    if any(marker in text for marker in ("don't know", "do not know", "no idea",
                                         "unsure", "nobody knows")):
        return Grade.UNKNOWN, "explicitly unknown - record an owner and a date"
    if any(hedge in text for hedge in HEDGES):
        return Grade.ASSUMED, "hedged - convert to a verification task"
    if any(marker in text for marker in VAGUE_MARKERS):
        return Grade.VAGUE, "non-specific phrasing"
    if expects == "duration" and not any(c.isdigit() for c in text):
        return Grade.VAGUE, "no number given"
    if expects == "list" and len(text.split()) < 4:
        return Grade.VAGUE, "too short to be a list"
    if expects == "person" and len(text.split()) < 2:
        return Grade.VAGUE, "no named person"
    return Grade.SPECIFIC, "ok"
```

The heuristics are a floor, not a judgement. **You still read the answer.** A
fluent paragraph that never names a vendor is `VAGUE` no matter how long it is,
and the regex will not catch that.

Three rules that matter more than the code:

1. **`UNKNOWN` passes; `VAGUE` does not.** A recorded "we do not know where our
   CV vendor stores data, Sam is checking by 22 September" is an honest artifact
   a regulator can read and an engineer can close. "Standard vendors, should be
   fine" is a liability written in the voice of diligence.

2. **Two re-asks, then record `UNKNOWN`.** A third re-ask produces a fabricated
   answer, which is worse than a gap: gaps get closed, fabrications get built on.

3. **Never convert an `UNKNOWN` into an assumption to keep moving.** The
   temptation is enormous because an assumption unblocks the build. It is also
   exactly how the wrong thing gets built and then documented as deliberate.

## The gate

After the interview, every finding gets a severity, and the severities decide
what you are allowed to build.

```python
def decide(findings, unknowns) -> tuple[str, str]:
    blockers = [f for f in findings if f.severity == "blocker" and f.status == "open"]
    conditions = [f for f in findings if f.severity == "condition" and f.status == "open"]
    if blockers:
        return "blocked", f"{len(blockers)} open blocker(s): {[f.id for f in blockers]}"
    if conditions or unknowns:
        return "conditional", (f"{len(conditions)} condition(s), "
                               f"{len(unknowns)} open unknown(s)")
    return "clear", "no open findings"
```

**What each decision means for what you do next — be precise about this, because
a vague refusal is useless:**

- **`clear`** — build it.

- **`conditional`** — **build it**, and write the conditions into the plan with
  owners and dates. Conditional is the normal outcome for real software, and
  treating it as a stop is how the gate gets switched off in week two.

- **`blocked`** — **build everything that is not implicated, and refuse the
  specific component that is.** Name it precisely:

  > I can build the application intake, the storage layer and the recruiter
  > dashboard now.
  >
  > I am not going to build the ranking model yet. F-001: the historical CVs you
  > want to train on have no identified lawful basis (Art. 6 GDPR), and training
  > is a separate purpose from the ranking you already assessed. That is not a
  > documentation gap I can paper over in the code — there is no version of the
  > training step that is lawful without it.
  >
  > Two ways forward: (a) Priya identifies and documents a basis — if it is
  > legitimate interests it needs a balancing test, and applicants' reasonable
  > expectations are the hard part; or (b) we descope to ranking on the fields
  > applicants submit for this role, which is a different and much easier
  > question. Either way, say which and I will keep going.

  Note what that refusal does: names the component, cites the article, explains
  why code cannot fix it, and offers two concrete routes. A refusal that just
  says "this may not be compliant" tells the user nothing and gets ignored.

**Never refuse the whole task because one branch is blocked.** That is the
failure mode that makes people uninstall the skill, and it is not what the
regulation requires either.

## The escape hatch

Users will want to proceed anyway. Sometimes they are right — they have context
you do not, or counsel has already cleared it, or the launch is an internal
pilot with ten colleagues.

Refusing any escape hatch means the skill gets deleted. So provide one, and make
using it produce a better artifact than not using it:

```
<command> accept F-001 --by "Dana Ruiz, CTO" --review-by 2026-11-01 \
  --rationale "Counsel cleared LI on 2026-09-12; LIA attached at decisions/0004-li-training.md"
```

Required, and enforced: **a named human**, a **rationale**, and a **review
date**. An acceptance with no name is not an acceptance, it is a bypass.

Then:

- The acceptance is written into `accepted_risks` in the brief, and rendered
  prominently in the Markdown — not in a footnote.
- The gate moves to `conditional`, never to `clear`. Accepted is not resolved.
- `eu-compliance-gates` fails the build again when the review date passes.
- You say plainly, once, what was accepted and by whom. Then you build. Do not
  re-litigate it every turn — the decision is recorded, and nagging is how this
  becomes something people route around.

A dated, attributed, reasoned acceptance is itself a compliance artifact, and is
far better than the realistic alternative, which is the same decision made
silently by someone who never wrote it down.

## What to produce

Two files, in the repository, next to the code:

```
compliance/
├── compliance.yaml        # the machine-readable brief - the spine
└── COMPLIANCE-BRIEF.md    # generated from it, never hand-edited
```

The schema is in `references/compliance-brief.md` and `schema/compliance.schema.json`.
Non-negotiable properties:

- **Every claim carries a `source`**: `{kind: answered, question: A-07}` or
  `{kind: inferred, reasoning: "nginx log format in ops/nginx.conf"}`. A brief
  with untraceable claims is a fabrication wearing the clothes of a record, and
  a regulator will reasonably read every claim in it as one the company made.
- **`status` is derived, never typed.** If a human can set `status: clear` by
  editing the file, the gate is decorative.
- **Findings are append-only.** Resolving one sets `status: resolved` with a
  note. The history *is* the accountability record (Art. 5(2) GDPR).
- **Ruled-out regimes carry `expires_if`** — the fact that would make them apply
  again. "Below the NIS2 size cap" stops being true at the 50th hire.
- **The brief carries a `trace`** — `screened_regimes`, `answers` with grades,
  `verifications` (citation + CELEX + date), `directives` (Member State,
  transposition read or not), `confirmations` (named human, date). `certainty`
  is **derived from this trace by `tools/certainty_engine.py`**, never typed.
  A brief without a trace has no evidence from which to derive a number, and
  `tools/hard_gate.py --policy block` refuses it — that is the deterministic
  back end this repo ships.

Write incrementally, as answers arrive. A session that dies at question 30 must
not lose the first 29.

Then hand off: `eu-applicability` fills the regime lists, and each regime skill
appends its own findings. Before building anything gated, run
`python3 tools/hard_gate.py --brief compliance/compliance.yaml --policy record`
— it normalizes the derived numbers and records any lingering violation
append-only, and the recorded blocker is what stops the build, not a mood.

**Every assessment carries a certainty.** Each finding, each applicable or
ruled-out regime, and the headline of the brief carry `certainty` (0–100) — the
honest percent of the assessment that rests on verified sources and confirmed
facts rather than inference, open unknowns and interpretation. Wherever you
state an applicability, a classification, a citation-backed obligation or a
finding, show the percentage **and the single largest reason it is not higher**:
"ruled out NIS2 — certainty 66%: the national transposition was not read".
`references/certainty.md` holds the anchors; the rules that matter here: an
answer graded `UNKNOWN` caps anything resting on it at 70, an unread Directive
transposition caps at 60, a classification pending counsel caps at 50, and a
`100` requires every deciding fact SPECIFIC, every citation verified on EUR-Lex,
every transposition read and every regime screened. Certainty is visibility, not
a free pass — VAGUE stays rejected, an open blocker stays blocked.

## Failure modes

- **The interview becomes a form.** Questions asked, answers accepted, brief
  written, nothing gated. Symptom: no answer was ever graded `VAGUE` and
  re-asked. If the re-ask count across a real session is zero, the grading is
  not running.

- **Assumptions filled from the model's priors.** The agent does not know where
  a vendor stores data, guesses plausibly, and the guess is recorded as a fact
  the user supplied. This is the most damaging failure in the skill because it
  is invisible. Mark every inference `inferred`, with the reasoning.

- **Refusing the whole task.** One blocker in the ranking model, and the agent
  refuses to build the signup form. The skill gets uninstalled that afternoon.
  Build what is clear; refuse what is implicated; name which is which.

- **Blocker inflation.** Everything is a blocker, so the gate is disabled.
  Blockers are for: a prohibited practice, no lawful basis at all, special
  categories with no Art. 9 condition, a high-risk classification with no path to
  conformity. Everything else is a condition. Measure blocker precision the
  first few times a lawyer reviews a brief.

- **Interviewing about the law.** "What's your lawful basis?" gets a wrong
  answer confidently. Ask what would break if the user said stop, and map it
  yourself.

- **Not reading the repo first.** Asking which vendors see user data when
  `package.json` already answers it wastes the user's patience on the questions
  that had answers, and spends none of it on the ones that did not.

- **Stopping when the user gets tired.** The uncomfortable questions are the
  ones at the end. H-03 exists because of this.

- **One long wall of questions.** Twenty at once gets one paragraph back that
  answers four. Batch by topic, one at a time where the answer branches.

- **Legal conclusions.** "This is not high-risk" is not yours to say. Write it
  as a finding with the facts, the citation, and the open question. See
  `references/legal-citations.md`.

- **The brief drifts.** Written once, never re-run, and six months later it
  describes a product that no longer exists. That is what `eu-compliance-gates`
  is for, and it should be wired up in the same session.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, and `validate` a fixture brief against the
   schema.

2. **Tier 1** — `pytest -q`, offline, against scripted answers. Mandatory:

```python
def test_vague_answer_is_re_asked_and_never_recorded(session):
    session.answer("A-06", "we keep it as long as needed")
    assert session.last_grade is Grade.VAGUE
    assert session.re_asks("A-06") == 1
    assert "A-06" not in session.brief.recorded


def test_unknown_passes_and_records_an_owner(session):
    session.answer("A-09", "I genuinely don't know where they host")
    assert session.last_grade is Grade.UNKNOWN
    unknown = session.brief.unknowns[-1]
    assert unknown.question == "A-09" and unknown.owner and unknown.due


def test_two_re_asks_then_unknown(session):
    for _ in range(3):
        session.answer("A-08", "the usual vendors")
    assert session.brief.unknowns[-1].question == "A-08"
    assert session.re_asks("A-08") == 2          # stopped at two, did not fabricate


def test_trigger_answer_opens_the_branch(session):
    session.answer("orient-3", "yes, an LLM ranks applicants")
    assert "B" in session.open_branches
    assert "B-04" in session.pending


def test_interview_cannot_exit_with_an_open_branch(session):
    session.answer("orient-3", "yes, an LLM ranks applicants")
    with pytest.raises(RuntimeError, match="branch B has 9 unanswered"):
        session.finish()


def test_no_ai_answer_rules_out_the_branch_explicitly(session):
    session.answer("orient-3", "no models, no automated decisions, all manual")
    session.finish()
    assert any(r["regime"] == "ai_act" for r in session.brief.regimes["ruled_out"])


def test_prohibited_practice_is_a_blocker_not_a_condition(session):
    session.answer("B-05", "yes, it infers emotion from interview video")
    finding = session.findings_for("B-05")[0]
    assert finding.severity == "blocker"
    assert finding.citation.startswith("Art. 5")


def test_profiling_blocks_the_art_6_3_derogation(session):
    session.answer("B-03", "yes, it scores individual candidates")
    assert session.brief.ai["systems"][0]["art_6_3_derogation_claimed"] is False


def test_gate_blocks_on_an_open_blocker(brief_with_blocker):
    decision, reason = decide(brief_with_blocker.findings, brief_with_blocker.unknowns)
    assert decision == "blocked" and "F-001" in reason


def test_blocked_refuses_only_the_implicated_component(session):
    plan = session.build_plan()
    assert "applicant intake" in plan.allowed
    assert "ranking model" in plan.refused
    assert plan.refusal_for("ranking model").citation == "Art. 6(1)"


def test_accept_requires_a_named_human_and_a_review_date(session):
    with pytest.raises(ValueError, match="named human"):
        session.accept("F-001", by="", rationale="fine", review_by="2026-11-01")
    with pytest.raises(ValueError, match="review date"):
        session.accept("F-001", by="Dana Ruiz, CTO", rationale="fine", review_by=None)


def test_accepted_risk_never_reaches_clear(session):
    session.accept("F-001", by="Dana Ruiz, CTO", rationale="counsel cleared",
                   review_by="2026-11-01")
    assert session.brief.gate["decision"] == "conditional"


def test_every_recorded_claim_has_a_source(session_after_full_interview):
    for claim in session_after_full_interview.brief.claims():
        assert claim.source and claim.source["kind"] in ("answered", "inferred")
        if claim.source["kind"] == "inferred":
            assert claim.source["reasoning"]


def test_no_legal_conclusions_in_output(session_after_full_interview):
    text = session_after_full_interview.render_markdown().lower()
    for phrase in ("is compliant", "is gdpr compliant", "is not high-risk",
                   "this is lawful"):
        assert phrase not in text


def test_status_is_derived_not_settable(tmp_path):
    path = write_brief(tmp_path, status="clear", findings=[open_blocker()])
    assert load_brief(path).status == "blocked"


def test_worst_case_fixture_is_blocked():
    assert run_gate(load("fixtures/worst-case.yaml")).decision == "blocked"


def test_static_site_fixture_is_clear():
    assert run_gate(load("fixtures/static-site.yaml")).decision == "clear"
```

   The last two are the negative controls and they matter most. A gate that
   passes `worst-case.yaml` is measuring nothing; a gate that blocks
   `static-site.yaml` will be switched off by the first person trying to ship.

3. **Tier 2** — run a real interview and report: questions asked, answers by
   grade, re-ask count, unknowns with owners and dates, findings by severity,
   trace coverage (must be 1.0) and inference share (should be under 0.3).

4. **Tier 3** — a lawyer or DPO reads the brief, not the code. The honest
   measure is whether they say it saved them time or created work. Then re-run
   the gate with their corrections and confirm the decision actually moves.

Then tell the user what ran, and be explicit about **what you could not
verify**: every date you could not check against EUR-Lex, every national
transposition you could not read, every classification that needs counsel. Close
with what is decided, what is open, and who has to decide the rest — never with
a claim about compliance.
