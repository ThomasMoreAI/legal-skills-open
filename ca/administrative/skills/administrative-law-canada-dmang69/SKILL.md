---
name: administrative-law-canada-dmang69
title: Administrative Law — Canadian Doctrine
description: 'Canadian administrative law doctrine — the Vavilov framework for judicial review, standards of review (correctness and reasonableness at common law; patent unreasonableness preserved by BC''s ATA s.58), duty of procedural fairness (the Baker factors), legitimate expectations, bias and the reasonable apprehension of bias test (Committee for Justice and Liberty; Wewaykum), jurisdictional error (as reconstituted post-Vavilov), delegated legislation, sub-delegation, fettering of discretion, improper purposes, taking irrelevant considerations into account, and the doctrine of legitimate deference to administrative decision-makers. Focused on Canadian and BC practice where the RTB, Human Rights Tribunal, and other statutory decision- makers operate. ALWAYS trigger when: user asks about judicial review, procedural fairness, standards of review, tribunal decisions, Vavilov, Baker, patent unreasonableness, or the doctrine underlying their BC judicial review petition. Sits underneath
  bc-judicial-review-guide as the substantive doctrine layer.'
author: dmang69
author_url: https://github.com/dmang69/bc-legal-ai/tree/master/skills/administrative-law-canada
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: administrative
language: en
sources:
- title: Baker Factors Worked Examples
  path: references/baker-factors-worked-examples.md
- title: Bias Doctrine Guide
  path: references/bias-doctrine-guide.md
- title: Standards Of Review Decision Tree
  path: references/standards-of-review-decision-tree.md
- title: Vavilov Framework Detail
  path: references/vavilov-framework-detail.md
---

# Administrative Law — Canadian Doctrine

The doctrine governing statutory decision-makers and the courts'
supervisory jurisdiction over them.

Distinguished from `bc-judicial-review-guide` (which is procedural —
how to bring a JR) and `owings-sanghera-jr-strategy` (case-specific).
This skill is the substantive law that governs both.

---

## Skill Tree

| Module | Domain |
|---|---|
| 1 | The Framework — Vavilov and Its Aftermath |
| 2 | Standards of Review — Correctness, Reasonableness, Patent Unreasonableness |
| 3 | Duty of Procedural Fairness — The Baker Factors |
| 4 | Components of Procedural Fairness |
| 5 | Bias and the Reasonable Apprehension Test |
| 6 | Legitimate Expectations |
| 7 | Jurisdictional Error Post-Vavilov |
| 8 | Discretion and Its Limits |
| 9 | Delegated Legislation and Sub-Delegation |
| 10 | Remedies on Judicial Review |

---

## Module 1: The Framework — Vavilov and Its Aftermath

### The Vavilov Restatement

*Canada (Minister of Citizenship and Immigration) v Vavilov* 2019 SCC
65 restated Canadian administrative law. Key holdings:

1. **Reasonableness is the presumptive standard** for judicial review
   of administrative decisions on merit.

2. **Correctness applies in five categories**:
   - Constitutional questions
   - General questions of law of central importance to the legal system
   - Questions regarding jurisdictional boundaries between two or more
     administrative bodies
   - Where the legislature has provided for a right of appeal
   - Where the legislature has clearly indicated an intent for
     correctness (e.g. by statute)

3. **"True jurisdictional questions" as a separate correctness category
   are eliminated.** No more asking whether the tribunal had
   jurisdiction to decide as it did (as a threshold matter).

4. **Reasonableness review requires attention to reasons.** A
   reasonable decision is one that is transparent, intelligible, and
   justified. Reasons must be responsive to the parties' submissions
   and the record.

5. **Procedural fairness continues to be reviewed under Baker.**
   Procedural fairness is treated as a separate question from merit
   review, not on a standard-of-review analysis.

### The Post-Vavilov Landscape

- Deference is real. Reasonableness review is not correctness in
  disguise.
- But reasonableness has teeth. Reasons matter. A decision that
  ignores central arguments, misconstrues the statute, or produces
  arbitrary results may be unreasonable.
- Statutory standards persist. Where a statute (like BC's ATA)
  prescribes a standard, that standard applies.

---

## Module 2: Standards of Review

### Correctness

The court substitutes its own judgment. No deference. The court asks
whether the decision was right.

Applied to:
- Constitutional questions
- General questions of law of central importance
- Jurisdictional boundaries between tribunals
- Statutory rights of appeal on questions of law
- Statutorily prescribed correctness

Practical implication: on correctness review, the tribunal's reasoning
matters little. The court decides the question anew.

### Reasonableness

The court defers to the tribunal's decision if it is reasonable — even
if the court would have decided differently.

A decision is reasonable if:
- The reasoning is coherent (internally rational)
- The decision is justified in relation to the constraints (legal and
  factual)
- The reasons are responsive to the submissions and the record
- The outcome falls within a range of acceptable outcomes

A decision is unreasonable where:
- Reasons ignore key submissions
- The interpretation ignores text, context, or purpose
- The decision misapplies binding law
- The outcome is arbitrary or logically unsupportable
- The reasoning is unintelligible

### Patent Unreasonableness

Preserved in BC by the Administrative Tribunals Act (ATA) s.58 for
tribunals to which s.58 applies (including the RTB).

Under ATA s.58:
- For discretionary decisions: patent unreasonableness
- For findings of fact: patent unreasonableness
- For interpretation of the home statute (in some tribunals):
  patent unreasonableness
- For procedural fairness: separate analysis (Baker)
- For jurisdictional questions and other legal questions: various

A decision is patently unreasonable if it is:
- Made without any evidence
- Based on a finding of fact no reasonable tribunal could make
- Based on legally incorrect reasoning so defective that no reasonable
  tribunal could adopt it

Patent unreasonableness is more deferential than reasonableness. The
bar is very high. See *Speckling v BC (WCB)* 2005 BCCA 80.

### The Standard Selection Process

For any JR under BC's ATA:

```
1. Identify the type of question:
   - Question of fact → patent unreasonableness (s.58(2)(a))
   - Discretionary decision → patent unreasonableness (s.58(2)(a))
   - Interpretation of home statute → patent unreasonableness (for
     tribunals where s.58 says so)
   - Procedural fairness → Baker analysis, not merit standard
   - Jurisdictional / other question of law → other standards per s.58

2. State the standard and its source (specific ATA subsection)

3. Apply the standard rigorously
```

---

## Module 3: Duty of Procedural Fairness — The Baker Factors

Every administrative decision-maker owes some degree of procedural
fairness to those affected by their decisions. The content of that
duty varies.

*Baker v Canada (MCI)* [1999] 2 SCR 817 set out five factors for
determining the content:

### Factor 1 — Nature of the Decision

The more the decision resembles a judicial process, the greater the
duty of fairness. Purely administrative decisions may attract lower
fairness requirements.

### Factor 2 — Nature of the Statutory Scheme

If the statute creates procedural rights explicitly, those govern. If
appeal rights exist, the fairness required at first instance may be
lower.

### Factor 3 — Importance of the Decision to the Individual

Decisions with severe consequences (deportation, loss of tenancy,
professional discipline) attract higher fairness requirements.

### Factor 4 — Legitimate Expectations

Where a party has a legitimate expectation of a particular procedure
(from past practice, promises, or public policy), that expectation
informs the required procedure.

### Factor 5 — Choices of Procedure Made by the Agency Itself

Respect for the agency's own procedural choices, particularly where the
statute grants discretion.

### Applying the Factors

The factors are weighed together. No factor is decisive. The result is
a determination of the specific content of the duty in the specific
context.

---

## Module 4: Components of Procedural Fairness

Once the content is determined, it typically includes some or all of:

### The Right to Be Heard (Audi Alteram Partem)

- Notice of the case to be met
- Adequate time to prepare
- Opportunity to make submissions (oral or written)
- Opportunity to challenge adverse evidence
- Right to counsel in serious proceedings (usually not required in
  routine administrative matters)

### The Right to an Unbiased Decision-Maker (Nemo Judex)

- Actual bias — decision-maker has decided in advance
- Reasonable apprehension of bias — informed observer would perceive
  bias
- Both institutional (structural) and personal bias apply

### The Right to Reasons

Duty to give reasons where the decision affects important interests.
Post-Vavilov, reasons matter substantially — they are the vehicle for
justification.

### Adequate Notice

Notice of:
- The proceedings
- The case to be met (allegations, evidence relied on)
- The procedure
- The consequences

### Disclosure

The affected party is entitled to know what evidence the decision-
maker is relying on, subject to limited exceptions for confidential or
privileged material.

### Right to Present Evidence and Argument

Meaningfully. Not just formally.

### Right of Response to Adverse Material

If the decision-maker is going to rely on material adverse to a party,
the party must have opportunity to address it.

---

## Module 5: Bias and the Reasonable Apprehension Test

### The Test

*Committee for Justice and Liberty v National Energy Board* [1978] 1
SCR 369:

"What would an informed person, viewing the matter realistically and
practically — and having thought the matter through — conclude?"

The test asks whether the informed observer would think it more likely
than not that the decision-maker, whether consciously or not, would
not decide fairly.

### Refined in Wewaykum

*Wewaykum Indian Band v Canada* 2003 SCC 45 emphasized:

- The threshold for finding bias or its appearance is high
- Judges and decision-makers are presumed to be impartial
- The party alleging bias bears the burden
- Cogent evidence is required
- Speculation is insufficient

### Actual Bias vs Reasonable Apprehension

**Actual bias** — evidence the decision-maker actually decided in
advance or was predisposed. Rarely provable.

**Reasonable apprehension** — the more usual claim. The question is
about appearance, not proven mental state.

### Institutional Bias

Bias arising from the structure of the decision-making body itself.
Examples:

- Investigator and adjudicator are the same person
- Financial interest of the tribunal in the outcome
- Statutory scheme creates structural conflict

Test: *2747-3174 Québec Inc v Régie des permis d'alcool* [1996] 3 SCR
919 — would an informed observer, having examined the institutional
framework, have a reasonable apprehension of bias in a substantial
number of cases?

### Individual Bias

Bias arising from the specific decision-maker's:
- Prior involvement in the matter
- Financial interest
- Personal relationships
- Public statements on the issue
- Conduct during the proceedings

### Common Sources of Perceived Bias

- Rushed or pressured proceedings
- Cutting off submissions
- Comments suggesting the decision was made in advance
- Consistent one-sided rulings
- Prior public statements

### Discipline in Raising Bias

Bias allegations damage credibility if unwarranted. Reserve them for
situations where the evidence genuinely supports the reasonable
apprehension.

If bias is a live issue:
- Object at the time (waiver risk if not)
- Document specific concerns
- Consider raising at the tribunal level first
- Raise on JR with specific factual basis

---

## Module 6: Legitimate Expectations

Where a party has a legitimate expectation of a specific procedure or
consultation — arising from past practice, express promises, or public
policy — that expectation may inform the required procedure.

### The Limits

- Legitimate expectations are procedural only, not substantive (in
  Canada, unlike some jurisdictions)
- The expectation must be reasonable
- The expectation cannot conflict with statutory duties
- The expectation is a factor in the Baker analysis, not a
  standalone doctrine

### Sources

- Past practice of the decision-maker
- Express promises
- Published policies
- Legitimate representations by government officials

### Example

If a tribunal has consistently held oral hearings in a particular type
of case, a party may have a legitimate expectation of an oral hearing.
Departing from this practice without notice may attract procedural
fairness concerns.

---

## Module 7: Jurisdictional Error Post-Vavilov

Pre-Vavilov, "true jurisdictional questions" attracted correctness
review as a separate category. Post-Vavilov, this category is
eliminated.

However, jurisdictional error can still exist:

- Decisions truly outside the tribunal's grant of authority remain
  reviewable
- The analysis is now done under reasonableness (or correctness where
  applicable), not under a separate jurisdictional category

### What Still Matters as Jurisdictional

- The tribunal must actually have been given the authority to decide
  the type of question at issue
- The tribunal must not exceed the scope of its enabling statute
- The tribunal must not decide matters reserved for other bodies

These are reviewed as questions of statutory interpretation of the
enabling statute, under whatever standard applies to that
interpretation.

### The Change in Framing

Rather than "did the tribunal have jurisdiction?", the question is
"was the tribunal's interpretation of its enabling statute
reasonable?"

Practical consequence: the strategy of framing a case as
"jurisdictional" to attract correctness review is less available.
Cases must be built on the applicable standard directly.

---

## Module 8: Discretion and Its Limits

Administrative decision-makers often have discretion. But discretion
is never absolute.

### Fettering Discretion

A decision-maker cannot rigidly apply a policy without considering the
specific case. Fettering discretion is a reviewable error.

Signals of fettering:
- Policy applied without consideration of individual circumstances
- Refusal to consider exceptions
- Treating a guideline as binding when it is discretionary

### Sub-Delegation

A decision-maker cannot delegate their discretion to someone else
without statutory authority. Sub-delegation renders the decision
invalid.

Exception: routine administrative sub-delegation (support staff
carrying out clerical functions) is generally permitted.

### Improper Purposes

Discretion must be exercised for the purposes for which it was
granted. Using discretion to punish, favour, or achieve unrelated
objectives is improper.

### Irrelevant Considerations

The decision-maker must consider all relevant factors and disregard
irrelevant ones. Weighting a factor not authorized by the statute is
an error.

### Bad Faith

Exercising discretion in bad faith — with malice, ulterior motive, or
dishonesty — is reviewable.

### The Structure

For any discretionary decision, the reviewing court asks:

- Did the decision-maker consider all relevant factors?
- Did they consider any irrelevant factors?
- Was the discretion fettered by rigid policy?
- Was the discretion exercised for a proper purpose?
- Was it exercised in good faith?
- Was the resulting decision reasonable?

---

## Module 9: Delegated Legislation and Sub-Delegation

### Delegated Legislation

Statutes often authorize the making of regulations. Regulations must:

- Be within the scope of the delegation
- Comply with applicable procedural requirements (e.g. gazette
  publication)
- Not exceed the statutory authority

Regulations exceeding statutory authority are ultra vires.

### Rules and Policies

Administrative bodies may make rules and policies. Distinction:

- **Rules** — binding on both the body and affected parties
- **Policies** — guide the exercise of discretion but don't bind

Treating a policy as binding = fettering discretion.

### Sub-Delegation

The general rule: a statutory power cannot be sub-delegated without
authority. But:

- Routine administrative functions can be sub-delegated
- Investigation may be sub-delegated even where decision cannot
- Statutory authority for sub-delegation may be express or implied

### Common Sub-Delegation Issues

- Where a statute grants authority to "the Minister" or "the
  Registrar," delegation to staff may be problematic
- Some statutes explicitly authorize delegation
- The specificity of the statutory grant matters

---

## Module 10: Remedies on Judicial Review

### The Traditional Remedies

- **Certiorari** — setting aside the impugned decision
- **Prohibition** — preventing further action
- **Mandamus** — compelling performance of a legal duty
- **Declaration** — declaring the legal position
- **Injunction** — enjoining conduct

In modern practice, these are usually sought as JR under the JRPA
rather than as separate prerogative writs.

### The JRPA Framework (BC)

Under the *Judicial Review Procedure Act* (BC), a JR petition may
seek:

- Setting aside the decision
- Referring the matter back for reconsideration
- Declaratory relief
- Restraining relief

### Remedy on Success

Where the JR succeeds, common outcomes:

- **Set aside and remit** — decision quashed, matter sent back
- **Set aside without remit** — where remit would be pointless
- **Substitute a decision** — rare; usually only where one outcome is
  the only reasonable one
- **Declaration** — clarifying the legal position

### Discretion in Remedies

Even where a JR succeeds on the merits, the court has discretion to
withhold a remedy:

- Delay
- Waiver
- Adequate alternative remedy exists
- Mootness
- No practical benefit

### Interim Relief

Available pending final determination:

- **Interim stay** — suspending the effect of the impugned decision
  (see *RJR-MacDonald* test)
- **Interim injunction** — restraining specific conduct

The tests are the *RJR-MacDonald* three-part framework:
1. Serious issue to be tried
2. Irreparable harm to the applicant if relief not granted
3. Balance of convenience

For stays of eviction, the stakes of losing housing typically weigh
heavily on irreparable harm.

---

## Reference Files

- `references/vavilov-framework-detail.md` — extended Vavilov analysis
- `references/baker-factors-worked-examples.md` — Baker applied to RTB and similar tribunals
- `references/standards-of-review-decision-tree.md` — which standard applies
- `references/bias-doctrine-guide.md` — bias analysis in detail

## Templates

- `templates/procedural-fairness-analysis.md` — full Baker analysis
- `templates/standard-of-review-analysis.md` — selecting and applying standards
- `templates/discretion-review.md` — reviewing a discretionary decision

---

## Integration Points

- `bc-judicial-review-guide` → the procedural companion to this substantive skill
- `owings-sanghera-jr-strategy` → case-specific application
- `statutory-interpretation` → interpreting the enabling statute for standard-of-review analysis
- `evidence-law-canada` → evidence in JR proceedings
- `argument-architecture` → structuring administrative law arguments
- `bc-tenancy-substantive` → the RTA substantive law underlying most RTB decisions
