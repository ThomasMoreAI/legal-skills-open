# Where each check comes from

Five primary sources, each read verbatim on 2026-09-16 (not summarized from a
landing page). Every deterministic check and every rubric axis traces to a line
below.

| Tag | Source | What was read |
|---|---|---|
| **LYNCH** | Michael Lynch, *How to Write an Effective Software Design Document*, refactoringenglish.com/excerpts/write-an-effective-design-doc/, published 2026-06-24 | Full essay (41,077 B HTML → 344 lines). Plus the **worked example**, `…/little-moments-design-doc/` (213,374 B → 2,667 lines), and the review companion `refactoringenglish.com/blog/useful-feedback-on-design-docs/` (31,964 B). |
| **GOOGLE** | Malte Ubl, *Design Docs at Google*, industrialempathy.com/posts/design-docs-at-google/ | Full post (80,098 B → 271 lines). |
| **RUST** | rust-lang/rfcs `0000-template.md` @ master | Template verbatim (5,705 B), plus `README.md` (13,779 B). |
| **NYGARD** | Michael Nygard, *Documenting Architecture Decisions*, cognitect.com, 2011-11-15 | Full post (45,800 B → 463 lines). Itself written in ADR form. |
| **OXIDE** | Jess Frazelle & Bryan Cantrill, *RFD 1: Requests for Discussion*, rfd.shared.oxide.computer/rfd/0001 | Full RFD (202,068 B → 478 lines). |

---

## The convergence

Five sources, four organizations, fifteen years apart. What they agree on is
short, and it is not the section list.

### 1. The inclusion rule is reversal cost, not importance

- **LYNCH** states it as a question — *"what's the penalty for being wrong?"* —
  and draws the line with two examples: C++-over-Rails is unrecoverable at 200k
  lines; a "Load more" button is *"not a design-level concern … you can fix it in
  a few hours … you definitely shouldn't waste review cycles arguing about it."*
- **GOOGLE** reaches the same rule from the other end: *"At the center of that
  decision lies whether the solution to the design problem is ambiguous."*
- **NYGARD** scopes ADRs to *"architecturally significant decisions: those that
  affect the structure, non-functional characteristics, dependencies, interfaces,
  or construction techniques."*
- **OXIDE**: *"Not every RFD is equal … weigh rigor and urgency to your best
  judgement."*

→ `C3` (reversal cost declared), rubric **R1**.

### 2. Trade-offs are the content; without them, write the code instead

**GOOGLE** is the bluntest: *"If a doc basically says 'This is how we are going
to implement it' without going into trade-offs, alternatives, and explaining
decision making … then it would probably have been a better idea to write the
actual program right away."* It calls alternatives *"one of the most important"*
sections. **RUST** makes it a required heading (*Rationale and alternatives*:
"why is this design the best in the space of possible designs?"). **OXIDE**:
*"Document the viable options … and the benefits and drawbacks of each option."*
**LYNCH** and **NYGARD** concur.

→ `C5` (≥2 alternatives, each with a reason), `C9` (implementation-manual
detector), rubric **R2**, **R4**.

### 3. A non-goal is a declined goal, not a negated requirement

**GOOGLE** gives the discriminator precisely: *"non-goals aren't negated goals
like 'The system shouldn't crash', but rather things that could reasonably be
goals, but are explicitly chosen not to be goals."*

**LYNCH's worked example** supplies the strongest form, under a heading his own
essay never mentions — `Missing features` — where every exclusion cites observed
evidence rather than asserting scope: *"TinyBeans offers this, but nobody in my
family has ever used this"*; *"I never used this feature."*

→ `C4` (negated-requirement detector), rubric **R3**.

### 4. State negative consequences explicitly

**NYGARD**: *"All consequences should be listed here, not just the 'positive'
ones."* **RUST** dedicates a heading to it — *Drawbacks: why should we* not *do
this?* Neither LYNCH nor GOOGLE names this section, and Lynch's own worked
example has no equivalent — which is why `C6` is *required* on `adr`/`rfd` and
merely *recommended* on `spec`.

→ `C6`.

### 5. A decision record is immutable and supersession is explicit

**NYGARD**: *"ADRs will be numbered sequentially and monotonically. Numbers will
not be reused. If a decision is reversed, we will keep the old one around, but
mark it as superseded"* — with *"a reference to its replacement."*
**OXIDE** formalizes this as a six-state machine: `prediscussion → ideation →
discussion → published → committed`, plus `abandoned`.

→ `C2` (status present; a terminal state must name its successor).

### 6. Ambition has a ceiling

**GOOGLE**: *"The sweet spot for a larger project seems to be around 10-20ish
pages. If you get way beyond that, it might make sense to split up the problem
into more manageable sub problems"* — and blesses the *"1-3 page mini design
doc."* **NYGARD**, at the opposite scale: *"The whole document should be one or
two pages long … Large documents are never kept up to date."*

→ `C10` (advisory only — never blocking), and the `note` profile.

### 7. Acceptance must be objective

**LYNCH**: *"Your manager's idea of 'performant' might be <2ms of latency, and
you don't want to wait until code complete to find out. A well-defined SLO
prevents ambiguity by expressing goals in concrete, objective terms."*

→ `C8` (a number with a unit, or a runnable command).

---

## Where they disagree

Worth knowing, because the disagreements are where a house style has to choose.

| Axis | LYNCH | GOOGLE | RUST | NYGARD | OXIDE |
|---|---|---|---|---|---|
| Length | 1 page – 50 pages | 10-20 pages | unbounded | **1-2 pages** | varies by urgency |
| Cross-cutting sections | fixed list (security, privacy, legal, logging, monitoring, SLO) | *"Teams should standardize what these concerns are in their case"* | none | none | economic / customer / performance / security |
| Prior art | absent | absent | **required heading** | absent | the RFD-9 landscape survey |
| Review venue | Google Docs or code review | Google Docs ("the vast majority") | GitHub PR + FCP | repo markdown | GitHub PR |
| Formal meeting | **last step**, agenda-scoped | *"a dangerous trap of overhead"* | async default | n/a | async default |

Two are adopted here as house style: **GOOGLE's** stance that the cross-cutting
list is per-organization (so `PROFILES` is configurable rather than fixed), and
**LYNCH/GOOGLE's** shared position that the meeting is the last resort, not the
first move (rubric §Review ordering).

**RUST's `Prior art`** is the section the other four lack and the one this
workspace most needs — it is the build-vs-reuse question in doc form. It is
folded into the `alternatives` class here rather than given its own required
heading, because a survey nobody acts on is decoration; the acting is the
alternatives comparison.

---

## What LYNCH's own example teaches that his essay does not

The essay enumerates 22 candidate sections. The worked example — written to
these principles by the same author — carries a **different set**: it adds
`User roles`, `Missing features`, `Users`, `Notifications`, `Data retention`,
`Licensing` and a JSON-format appendix, and omits Glossary, Constraints, Related
documents and any standalone Monitoring section. Two structural conventions in
the artifact outrank the section list:

1. **Alternatives appear at two depths.** Each architecture decision carries its
   rationale inline — *"SQLite minimizes cost and complexity … the downside is it
   doesn't support strong types … we only need to scale to tens of users"* — with
   a cross-link (*See Alternative frontend stacks considered*) to an appendix
   holding the deliberation. Body carries the decision; appendix carries the
   working. `C5` accepts both idioms for this reason.

2. **Closed issues retain the dead ends, dated.** The SMTP-vendor record stamps
   the decision at the top, then the criteria, then seven candidates with
   first-hand notes *including the unflattering ones*: *"Tried on 2026-01-21 …
   Bad: Seems like I have to wait up to 2 days for manual verification … Good:
   actual manual activation was in about 12 hours."* Keeping the dead ends is the
   counter-practice to documentation-as-performance-bias — an edited record
   teaches legibility, not effectiveness.

## Calibration

Run against **LYNCH's own worked example** at `--profile spec`, the contract
returns **zero failures**. Run against this workspace's 105 existing
`docs/specs|plans|adrs` documents, **one passes** — an ADR carrying its state under NYGARD's own `## Status` heading, a form the checker could not read until round 4.

Both halves have been load-bearing in review. The gold standard broke once —
a positional rule for the status field treated Lynch's `## Metadata` block as
body and reported the calibration reference as having no status — and that is
exactly what a calibration artifact is for: it fails loudly when a rule is
wrong, where the corpus figure would have moved by one and said nothing.

Read that second number carefully. It says what this corpus is like; it says
nothing about where the bar belongs. An earlier draft reported it as evidence
that the required/recommended split was well-chosen — the re-measurement that
cross-model review forced shows both the all-nine-required arm and the shipped
split pass 0/105, so the split buys no existing document and the claim was
unsupported. The split is derived from the table above: `required` is the
intersection of what all five sources independently call load-bearing.

The evidence that the gate is demanding rather than miscalibrated runs the other
way, and it is the first line: a design doc written to published best practice
clears it.
