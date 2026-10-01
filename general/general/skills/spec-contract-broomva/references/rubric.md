# The judgment layer — what `spec_check.py` cannot decide

`spec_check.py` decides whether a document has the *shape* of a design doc:
sections present, alternatives plural, acceptance numeric, status resolvable.
Every one of those is decidable from the text alone.

None of them answer the question the document exists for: **is this the right
set of decisions, argued honestly?** A document can pass every
deterministic checks and still be worthless — two strawman alternatives, a
non-goal nobody would have assumed, an SLO picked because it was easy to
measure. That failure mode is not a gap in the script. It is the half of the
problem that is irreducibly a judgment, and this file is where it lives.

Run the judgment layer with a **different model than the one that wrote the
doc** (bstack P20; the writer cannot be the final judge of the writing). Score
every axis; a single 0 blocks regardless of total.

---

## Scoring

Five axes, 0-3 each, 15 total. **Pass: ≥ 11 and no axis at 0.**

The bar is high because the deterministic layer has already removed the easy
failures. A doc reaching this layer is well-formed by construction; what is
being graded is whether it is *true*.

---

### R1 — Reversal-cost fit (the inclusion rule)

> *Does every documented decision actually have a high cost of being wrong, and
> is every high-cost decision documented?*

This is Lynch's rule — "what's the penalty for being wrong?" — and it cuts in
**both directions**. The common failure is not omission; it is a doc padded with
cheap decisions (a pagination style, a log format, a directory name) that
consume review cycles, while the one irreversible choice (the storage engine,
the wire format, the trust boundary) is a single unargued sentence.

| Score | Condition |
|---|---|
| 3 | Every documented decision is expensive to reverse; no expensive decision is undocumented. The doc names its own one-way doors. |
| 2 | The expensive decisions are all present, but cheap ones are argued alongside them at similar length. |
| 1 | An expensive decision is present but asserted rather than argued, or the doc's emphasis is inverted (most space on the cheapest choice). |
| 0 | A one-way door is made silently — the doc commits to a language, storage engine, protocol, vendor or trust boundary without ever marking it as a decision. |

**How to grade it:** list every decision the doc makes, including the implicit
ones. For each, answer *"if this is wrong, what does it cost to undo — an
afternoon, a sprint, or a rewrite?"* Anything in the third bucket that is not
argued is a 0.

---

### R2 — Alternative realism

> *Would a competent engineer have actually chosen one of these alternatives?*

`C5` counts alternatives and looks for a rejection reason. It cannot tell a real
contender from a strawman erected to be knocked down. A doc that rejects
"do nothing" and "rewrite everything in assembly" has satisfied the script and
evaded the question.

| Score | Condition |
|---|---|
| 3 | At least two alternatives that a reasonable engineer would defend, each rejected on a stated trade-off against *this doc's own goals*. |
| 2 | Real alternatives, but rejected on generic grounds ("too complex") rather than against the stated goals. |
| 1 | One real contender padded with strawmen. |
| 0 | All alternatives are strawmen, or the obvious contender a reader will immediately think of is absent. |

**How to grade it:** before reading the alternatives section, write down the two
options *you* would have considered. If neither appears, that is at most a 1.

---

### R3 — Non-goal load-bearing-ness

> *Would a reader have assumed these were in scope?*

Google's definition is the test: a non-goal is *"something that could reasonably
be a goal, but is explicitly chosen not to be"* — not a negated requirement, and
not something nobody would have expected anyway. `C4` catches the negated-
requirement form. It cannot catch the vacuous form: "Non-goal: solving world
hunger" is well-formed and useless.

| Score | Condition |
|---|---|
| 3 | Each non-goal is something a reader would plausibly have assumed in scope, and (best case) says *why* it was declined with evidence. |
| 2 | Load-bearing non-goals, declined without justification. |
| 1 | A mix of load-bearing and vacuous entries. |
| 0 | No non-goals, or all vacuous — the scope boundary is undefended and will be relitigated in review. |

**The 3 looks like this** (Lynch's own doc): *"No support for albums — there's no
special grouping for photos"*, *"No per-item privacy settings — I never used this
feature."* Each names a capability a reader expects and cites observed behavior
for declining it. A non-goal backed by evidence survives review; one asserted as
scope does not.

---

### R4 — Trade-off substance

> *Does the doc show why THIS design beats the alternatives given the goals, or
> does it assert it?*

This is Google's implementation-manual anti-pattern at full strength. `C9`
detects the degenerate case — no trade-off vocabulary anywhere. It cannot detect
a doc that uses the vocabulary fluently while arguing nothing.

| Score | Condition |
|---|---|
| 3 | The chosen design is connected to the stated goals through explicit trade-offs, and the doc states what it gives up. |
| 2 | Trade-offs are stated but not connected back to the goals — the reader must do the join. |
| 1 | Trade-off language is present but decorative; the decision would read identically with it removed. |
| 0 | An implementation manual: *this is what we will build*, with no argument that it is the right thing to build. |

**The tell for a 0:** delete the alternatives section and the drawbacks section.
If the rest of the doc is unchanged in meaning, it was never an argument.

---

### R5 — Inverted-pyramid legibility

> *Is the first screen intelligible to the widest reader you expect?*

From Lynch's review companion: the early sections must make sense to anyone —
partner teams, a reviewer with no context, someone reading it in a year — and
later sections may assume progressively more. A doc that opens on internal tool
names has lost the readers whose review was most worth having.

| Score | Condition |
|---|---|
| 3 | The first screen is complete and jargon-free: what this is, why now, what changes. Context narrows monotonically after it. |
| 2 | First screen is legible but incomplete — the reader must jump to understand the motivation. |
| 1 | Undefined internal jargon on the first screen, or the motivation appears only after the design. |
| 0 | The doc is unreadable without a conversation the author had with someone else. |

**How to grade it:** read only until the first `<h2>` boundary past the opening.
Write one sentence on what the doc is proposing and why. If you cannot, ≤ 1.

---

## Verdict format

```
R1 reversal-cost fit      _/3  — <one line: which decision, what it costs to undo>
R2 alternative realism    _/3  — <one line: the contender you expected; present?>
R3 non-goal load-bearing  _/3  — <one line: the strongest and weakest entry>
R4 trade-off substance    _/3  — <one line: does deleting alternatives change meaning?>
R5 legibility             _/3  — <one line: your one-sentence summary from the first screen>
                         --/15   VERDICT: pass | revise
```

## Escalation

- **R2 or R4 at 0-1** → the design itself is unargued, not the writing. Route to
  P20 cross-review before the doc goes wider. Rewriting prose will not fix it.
- **R1 at 0** → stop. A silent one-way door is the single failure a design doc
  exists to prevent, and it is the one that cannot be fixed after implementation.
- **R5 at 0-1 only** (everything else ≥2) → this is the preliminary-review case.
  Lynch: fix the *explanation* with one reviewer before widening, and do not
  touch the design in that pass.

## Review ordering (not scored — sequencing)

The rubric grades a draft. How the draft gets reviewed is a separate discipline,
and the ordering is counterintuitive enough to state:

1. **One preliminary reviewer, on comprehension only.** Sending a first draft to
   ten people triggers the bystander effect — everyone skims, assuming someone
   else is reading carefully. Ask one person, and ask them to fix your
   explanation, not your design.
2. **Then widen**, on substance.
3. **The meeting is last**, not first, and its written agenda names only the open
   issues — otherwise attendees read the invitation as licence to reopen settled
   decisions.
4. **Every answer goes back into the doc.** Resolving a reviewer's confusion in a
   thread fixes nothing; the next reader hits the same wall. Escalate a thread to
   an appendix open issue after two or three round trips, then resolve the thread
   with a link to it.

---

## A worked score

Grading the rubric's own reference document — Lynch's *Little Moments* design
doc, which the deterministic layer passes with zero failures. A rubric with no
scored example is not usable; this is what a 14/15 looks like and, more
usefully, what docks the missing point.

```
R1 reversal-cost fit      2/3  — language, storage, hosting and email vendor are all
                                 present and argued, but reversal cost is never NAMED.
                                 fly.io is chosen on familiarity ("I have the most
                                 hosting experience"), not on what switching would cost.
R2 alternative realism    3/3  — Google Photos, Momatu, PhotoCircle as products; three
                                 media-delivery designs; four licences; seven SMTP
                                 vendors with dated first-hand testing. Every one is a
                                 contender a competent engineer would defend.
R3 non-goal load-bearing  3/3  — "no albums", "no calendar view", "no per-item privacy",
                                 "can't reply by email". Each is something a TinyBeans
                                 user assumes in scope, and most cite observed behaviour
                                 for declining it.
R4 trade-off substance    3/3  — "SQLite … doesn't support strong types … but we only
                                 need to scale to tens of users" ties the choice to the
                                 stated goal. Delete the alternatives and closed issues
                                 and the document's meaning changes.
R5 legibility             3/3  — Objective is one jargon-free sentence; Background is the
                                 ad-injection grievance. Motivation precedes mechanism.
                         ----
                          14/15   VERDICT: pass
```

**What the score is worth knowing for.** The axis that docked a point, `R1`, is
the same one the deterministic layer flags (`C3-no-reversal-cost`, a warning on
this document). The two layers disagreed about *severity* and agreed about
*where the weakness is* — which is the property that makes running both worth
the cost. If they routinely disagreed about location, one of them would be
measuring noise.

**Known gap.** This is one worked example graded once. `skillify`'s TIER-J bar
asks for held-out cases and a *measured* inter-rater floor — two models scoring
the same document and agreeing within a stated tolerance. That has not been
done, so the rubric ships with a demonstrated instrument and an unmeasured
agreement rate. Treat a single grader's score as one opinion with a structure,
not as a number.
