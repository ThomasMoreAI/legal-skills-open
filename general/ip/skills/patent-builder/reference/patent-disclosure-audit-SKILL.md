---
name: patent-disclosure-audit
description: Reviews drafted patent disclosure materials from an internal patent review perspective. Use when checking whether a disclosure has enough technical problem definition, inventive features, implementation detail, distinguishing points, and filing-readiness before IPP or patent committee review.
---

# Patent Disclosure Audit

Use this skill to self-check a drafted patent disclosure by asking reviewer-style questions. The goal is to expose gaps before internal patent review, IPP review, or patent counsel drafting.

This skill does not provide legal opinions or guarantee patentability. It provides structured technical review questions and improvement prompts.

## Review mode

Use this workflow when the user provides:
- a drafted patent disclosure;
- invention points;
- a technical proposal intended for patent filing;
- reviewer feedback;
- an internal invention submission.

If the draft is missing, ask the user to provide the disclosure text or the main invention summary.

## Core review workflow

Copy and use this checklist:

```text
Patent Disclosure Audit Progress:
- [ ] 1. Identify the claimed technical problem
- [ ] 2. Check known-solution comparison
- [ ] 3. Test the technical solution for specificity
- [ ] 4. Verify distinguishing features
- [ ] 5. Check implementation sufficiency
- [ ] 6. Test technical effect support
- [ ] 7. Identify weak or abstract points
- [ ] 8. Generate reviewer questions
- [ ] 9. Produce revision recommendations
- [ ] 10. List must-confirm items before IPP review
```

## Reviewer mindset

Review the disclosure as if asking:

1. What exactly is the technical problem?
2. Why is this problem not already solved by conventional methods?
3. What technical features distinguish the proposal?
4. Are the distinguishing features concrete enough to implement?
5. Are the effects caused by the technical features, not just asserted?
6. What would a skeptical reviewer challenge?
7. Which statements need evidence, examples, or narrowing?
8. Which parts are common implementation rather than invention?

## Audit dimensions

### 1. Technical problem

Ask:
- Is the problem framed as a technical problem, not only a business goal?
- Does the disclosure identify a specific failure, inefficiency, mismatch, instability, latency, cost, accuracy issue, or resource constraint?
- Is the problem tied to a concrete technical scenario?
- Is it clear why conventional approaches fail under that scenario?
- Is the problem too broad, such as "make it smarter", "improve user experience", or "use AI"?

Flag if:
- the problem is vague;
- the problem is only about business value;
- the problem is not connected to system behavior or technical constraints.

### 2. Known solutions and drawbacks

Ask:
- What known or conventional approaches are described?
- Are their drawbacks technical rather than only commercial?
- Does the draft explain why an additional solution is required?
- Are common methods distinguished from the proposed solution?
- Does the draft avoid overstating that no similar solution exists?

Flag if:
- known solutions are missing;
- drawbacks are generic;
- the proposed difference is unclear;
- the draft depends on unsupported novelty claims.

### 3. Inventive feature identification

Ask:
- What are the one to three strongest distinguishing technical features?
- Are they single features or a coordinated combination?
- Which features should be the main invention, and which are optional embodiments?
- Does each feature solve a stated problem?
- Are common tools, models, placeholders, indexes, prompts, or UI rendering mechanisms presented as inventions without further technical mechanism?

Flag if:
- the draft lists functions instead of technical mechanisms;
- the alleged invention is only "using AI";
- the feature is conventional unless combined with a specific workflow;
- the main inventive point is buried in implementation details.

### 4. Implementation sufficiency

Ask:
- Could an engineer implement the solution from the disclosure?
- Are the input, processing, intermediate data, and output defined?
- Are key data structures or metadata fields identified?
- Are scoring, matching, ranking, routing, filtering, or selection rules described?
- Are thresholds, weights, confidence rules, or fallback behavior described at least conceptually?
- Are model-based and rule-based parts clearly separated?
- Are confirmed implementation and optional embodiments separated?

Flag if:
- the disclosure says "the system determines" without explaining how;
- no data structures are described;
- no execution sequence is described;
- optional features are written as mandatory facts.

### 5. Distinction over conventional approaches

Ask:
- If a reviewer says "this is just a conventional implementation", what is the response?
- Is the difference in the data flow, scoring, control loop, constraint, validation, fallback, or technical architecture?
- Does the disclosure explain why the combination is not merely an aggregation?
- Are there technical interactions among the features?
- Is there a before/after contrast with known approaches?

Flag if:
- the only difference is automation;
- the only difference is replacing manual work with a model;
- the only difference is using a common index, prompt, classifier, or vector search;
- the combination lacks a clear technical effect.

### 6. Technical effects

Ask:
- What measurable or observable technical effects result from the invention?
- Are the effects directly caused by the claimed technical features?
- Are effects stated as reduced error, improved stability, lower latency, lower storage, lower bandwidth, better matching, fewer retries, more deterministic output, or improved resource control?
- Is there an explanation of why the effect occurs?
- Would the effect still occur if one key feature were removed?

Flag if:
- effects are only "better experience" or "more intelligent";
- effects are not linked to specific steps;
- the draft lacks a causal chain from feature to result.

### 7. Claim-readiness

Ask:
- Can the disclosure support an independent method claim?
- Can it support system and computer-readable medium claims?
- Which features are essential for the independent claim?
- Which features should be dependent claims?
- Are there enough alternatives to avoid over-narrowing?
- Are optional embodiments clearly identified?

Flag if:
- the disclosure only supports a narrow product implementation;
- all details are tied to one platform or tool;
- no fallback or variant is provided;
- key terms are undefined.

### 8. IPP review readiness

Ask:
- Is the invention title specific enough?
- Are inventors' contributions tied to inventive concepts, not routine implementation?
- Are confirmed facts separated from assumptions?
- Are diagrams or flowcharts suggested?
- Are open questions listed?
- Are prior or conventional solutions acknowledged?
- Are risks and weak points disclosed honestly?

Flag if:
- contributor roles are only engineering tasks;
- review questions remain unanswered;
- the disclosure lacks a clear strongest invention direction.

## Scoring rubric

Score each item from 0 to 2.

```text
0 = missing or weak
1 = partially present but needs strengthening
2 = clear and sufficient
```

Audit categories:
1. Technical problem clarity
2. Known-solution comparison
3. Distinguishing feature clarity
4. Implementation sufficiency
5. Technical effect support
6. Conventional-technique differentiation
7. Claim-readiness
8. IPP readiness

Suggested interpretation:
- 14-16: strong draft, ready for attorney review after minor cleanup
- 10-13: workable but needs targeted strengthening
- 6-9: significant gaps; revise before IPP review
- 0-5: not yet ready; return to invention-definition stage

## Output format

When reviewing a disclosure, provide this structure:

```text
# Patent Disclosure Audit

## 1. Overall assessment
[Strong / moderate / weak / not ready]

## 2. Scorecard
| Category | Score | Reviewer concern | Suggested fix |
|---|---:|---|---|

## 3. Highest-risk reviewer questions
1. ...
2. ...
3. ...

## 4. Missing or weak technical details
- ...

## 5. Distinguishing features to emphasize
- ...

## 6. Suggested revisions
- Background:
- Invention points:
- Detailed description:
- Drawings:
- Claims support:

## 7. Must-confirm items before IPP review
- ...
```

## Question bank

Use these questions to pressure-test the disclosure.

### Problem questions
- What fails in the existing technical process?
- Under what conditions does the failure occur?
- Why is this not just a user preference or business problem?
- What technical resource or system constraint is involved?

### Prior-solution questions
- What would a conventional system do?
- Which part of that conventional system is insufficient?
- Is the proposed solution merely adding a model or automation?
- Which specific workflow step changes?

### Technical-mechanism questions
- What data is created, transformed, stored, scored, or transmitted?
- What metadata or intermediate state is required?
- What rule, model, threshold, score, or ranking changes the outcome?
- What happens when confidence is low or inputs are incomplete?
- What is the fallback path?

### Inventiveness questions
- What is the smallest combination of features that produces the technical effect?
- Which feature would be hardest for a conventional system to infer?
- What is the interaction between features?
- Why would a simple substitution not achieve the same result?

### Implementation questions
- Can the method be performed without a specific vendor, model, or platform?
- Are optional implementations described?
- Are enough details provided for scoring, matching, selection, or validation?
- Are input/output examples abstract and non-confidential?

### Output and validation questions
- How is output correctness checked?
- How is mismatch, duplication, inconsistency, or missing data handled?
- What information is logged for audit or replay?
- Can the system explain why it made a selection?

## Revision rules

When suggesting revisions:
- Prefer adding concrete technical mechanisms over broad claims.
- Convert vague benefits into technical effects.
- Convert feature lists into process flows.
- Convert isolated tools into coordinated combinations.
- Separate main flow from optional enhancement.
- Add fallback logic where uncertainty exists.
- Avoid real examples unless the user provided them.
- Avoid legal conclusions such as "patentable" or "will pass"; use "stronger", "weaker", "needs support", or "likely reviewer concern".

## Common weak phrases to challenge

Challenge and rewrite phrases like:
- "uses AI to improve"
- "automatically determines"
- "intelligently matches"
- "improves user experience"
- "reduces cost"
- "more accurate"
- "optimizes the result"

Ask:
- By what data?
- By what processing step?
- By what score or rule?
- Compared to what?
- What technical effect follows?
- What happens if it fails?

## Final decision labels

Use one of these labels:

- **Ready for IPP review:** strong technical mechanism, clear distinction, sufficient implementation detail.
- **Needs targeted revision:** promising idea, but specific sections need strengthening.
- **Needs invention refocus:** current draft has too many broad or conventional points; select a narrower technical combination.
- **Not ready:** technical problem, mechanism, or distinguishing features are not yet clear.
