---
name: patent-builder
title: Patent Builder
description: Discovers patentable ideas, refines early concepts, analyzes implementations for patent potential, drafts patent disclosure materials, or reverse-lookups existing disclosures against new requirements to identify coverage gaps. Use when the user asks about patent idea mining, invention brainstorming, patentability-oriented technical analysis, invention disclosure drafting, prior-solution comparison, claim-feature extraction, or checking whether existing disclosures already cover a new feature or requirement. / 发现可专利技术想法，打磨早期发明概念，分析已有实现的专利潜力，起草专利交底材料，或根据新需求对已有交底书做覆盖度反查，识别保护空白。适用于专利点挖掘、发明构思启发、现有方案对比、专利性初步分析、专利交底书撰写与优化、或检查已有交底是否覆盖新功能或新需求。
author: VinceZcrikl
author_url: https://github.com/VinceZcrikl/vinceZcrikl-skills/tree/main/skills/patent-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Patent Builder

## Language

If the user is writing in Chinese, load [reference/zh.md](reference/zh.md) and follow its instructions instead of the English body below.

---

Use this skill to help users discover, refine, evaluate, and document potential patent ideas.

Do not provide legal conclusions. Treat novelty, inventiveness, and patentability comments as preliminary technical analysis. Recommend professional patent counsel for filing, claim drafting, clearance, or legal opinions.

## Core principles

- Focus on technical problems, technical means, and technical effects.
- Separate confirmed implementation from optional embodiments.
- Distinguish common techniques from potentially inventive combinations.
- Prefer concrete mechanisms over broad statements such as "uses AI" or "improves experience".
- Do not use real examples unless the user provides them or explicitly asks for examples.
- Use neutral placeholders: "the system", "the module", "the data object", "the candidate item", "step N", "item A".
- Avoid unsupported claims such as "novel", "unique", or "patentable" unless clearly framed as preliminary.

## Entry mode selection

Determine the user's starting point.

**Mode A: Existing implementation**
Use when the user provides a system, feature, prototype, architecture, code description, product workflow, or technical document.

**Mode B: Initial idea**
Use when the user has a preliminary concept, pain point, or possible solution but no implementation.

**Mode C: Open exploration**
Use when the user has no clear direction and wants guided brainstorming.

**Mode D: Reverse disclosure lookup**
Use when the user has one or more existing patent disclosures and wants to check whether a new requirement, feature, or implementation is already covered, identify protection gaps, or decide whether to file a new disclosure or extend an existing one.

If unclear, ask one concise question:
"Are we starting from an existing implementation, an initial idea, or open exploration?"

## Universal workflow

Use this checklist and adapt the depth to the user's material.

```text
Patent Builder Progress:
- [ ] 1. Identify the technical field and target scenario
- [ ] 2. Clarify the technical problem
- [ ] 3. Identify known or likely conventional approaches
- [ ] 4. Extract distinguishing technical features
- [ ] 5. Build candidate invention concepts
- [ ] 6. Evaluate novelty risk, inventiveness potential, feasibility, and value
- [ ] 7. Select the strongest invention direction
- [ ] 8. Draft or refine the patent disclosure
- [ ] 9. List open questions and confirmation points
```

## Mode A: Existing implementation

### Goal
Extract patentable technical combinations from an existing system, feature, workflow, codebase, architecture, or design.

### Process

1. **Decompose the implementation**
   Identify inputs, outputs, modules, data structures, processing flow, decision logic, storage or indexing logic, model/rule involvement, and user-facing or backend interactions.

2. **Abstract the technical problem**
   Convert implementation details into patent-style technical problems. Look for failures, inefficiencies, cost, latency, inaccuracy, mismatch, instability, or resource constraints.

3. **Separate common implementation from inventive combination**
   Classify features as:
   - Conventional or likely conventional
   - Implementation-specific but not inventive
   - Potentially inventive alone
   - Potentially inventive as a combination

4. **Find candidate inventive combinations**
   Look for closed-loop mechanisms such as:
   - Detect → score → rank → select → generate → validate
   - Extract → classify → associate → retrieve → constrain → output
   - Plan → execute → verify → fallback
   - Index → retrieve → rerank → decide → render

5. **Draft disclosure sections**
   Provide background, invention points, detailed description, technical effects, optional drawings, and open questions.

### Mode A output
Provide:
- Implementation summary
- Technical problem abstraction
- Candidate inventive features
- Strongest invention direction
- Known-solution comparison
- Patent disclosure draft or improvement suggestions

## Mode B: Initial idea

### Goal
Turn a preliminary idea into an implementable technical solution and candidate patent disclosure.

### Process

1. **Clarify the idea**
   Determine the problem, affected user/system, current approach, drawback, and desired result.

2. **Structure the idea**
   Convert the idea into input data, processing modules, intermediate outputs, decision rules or scoring logic, final output, and feedback/validation/fallback behavior.

3. **Make it technically implementable**
   Add details for data representation, matching/scoring, ranking/selection, thresholds/constraints, state management, validation, and recovery.

4. **Generate invention variants**
   Create 2-3 candidate directions, such as algorithm/process, system architecture, or interaction/control-loop direction.

5. **Evaluate and select**
   Compare directions on technical specificity, difference from conventional approaches, feasibility, technical effect, and drafting strength.

### Mode B output
Provide:
- Refined problem statement
- Implementable technical solution
- Candidate invention directions
- Preferred direction
- Disclosure draft
- Open questions

## Mode C: Open exploration

### Goal
Guide the user from no clear direction to one or more patent idea candidates.

### Process

1. **Choose a field or context**
   Ask the user to identify a field, product area, workflow, user group, or technical environment.

2. **Surface pain points**
   Explore repetitive work, error-prone decisions, high latency/cost, low accuracy, poor data utilization, manual judgment, fragmented workflows, and limited resources.

3. **Transform pain points into invention seeds**
   Use patterns such as:
   - Multi-source evidence fusion
   - Structured planning before generation or action
   - Dynamic scoring and budgeted selection
   - Lightweight references instead of heavy data transfer
   - Confidence-based fallback
   - Context-aware routing
   - User-state or device-state adaptation
   - Verifiable intermediate plans

4. **Create candidate ideas**
   For each candidate, include problem, technical mechanism, required data, output, difference from conventional approaches, technical effect, and open questions.

5. **Select one idea for development**
   Recommend the strongest idea and continue using Mode B.

### Mode C output
Provide:
- Pain point list
- Candidate invention ideas
- Patent-potential ranking
- Recommended direction
- Questions needed to develop the idea

## Mode D: Reverse disclosure lookup

### Goal
Analyze one or more existing patent disclosures against a new requirement, feature set, or implementation to determine coverage status, identify protection gaps, and recommend actions.

### Inputs required

Before starting, confirm:
- **Existing disclosures:** full text, invention-point summaries, or abstract-level descriptions of one or more filed or drafted disclosures.
- **Requirements to check:** a new feature, implementation description, product spec, or set of specific technical points to audit against the disclosures.

If either input is missing, ask the user to provide it before proceeding.

### Process

1. **Inventory existing disclosures**
   For each disclosure, extract:
   - Technical field and target scenario
   - Core technical problem addressed
   - Key technical means and distinguishing features
   - Strongest invention direction or independent claim scope
   - Coverage keywords (data structures, processing steps, decision logic, control loops)

2. **Parse the requirements**
   Decompose the requirements into:
   - A numbered list of discrete technical feature points or functional behaviors
   - Data, modules, or flows involved
   - Technical vocabulary that may overlap with existing disclosures

3. **Map requirements to disclosures**
   For each requirement feature, assign one status:
   - **Covered:** the core technical mechanism in an existing disclosure directly encompasses this feature.
   - **Partially covered:** meaningful overlap exists, but key variants, steps, or data flows are not covered.
   - **Gap:** no existing disclosure covers this feature.

4. **Identify protection gaps**
   For each Gap or Partially covered item, analyze:
   - What specific technical distinction is missing from existing coverage?
   - Does the uncovered distinction produce an independent technical effect?
   - Is the gap narrow (implementation variant) or broad (different technical mechanism)?
   - Could it be addressed by supplementing an existing disclosure with additional embodiments?

5. **Recommend action**
   For each gap, assign one of three actions:
   - **No action needed:** the requirement falls within the scope of existing protection.
   - **Supplement existing disclosure:** add embodiments or extend the claim scope of an identified existing disclosure.
   - **File new disclosure:** the gap is technically distinct enough to warrant a new disclosure; provide a brief invention-point direction.

### Mode D output

```text
# Reverse Disclosure Lookup

## Existing disclosures indexed
| # | Title / Summary | Core technical mechanism | Coverage keywords |
|---|---|---|---|

## Requirements analyzed
[Numbered list of requirement feature points]

## Coverage map
| # | Requirement feature | Status | Matched disclosure | Gap description |
|---|---|---|---|---|
| 1 | ... | Covered / Partial / Gap | ... | ... |

## Protection gaps
1. [Gap description — missing technical distinction and scope]
2. ...

## Recommended actions
| Gap # | Action | Rationale |
|---|---|---|
| ... | No action / Supplement / New disclosure | ... |

## Open questions
- ...
```

## Patent disclosure structure

When drafting a disclosure, use this structure unless the user provides another template.

### 1. Background
Include technical field, problem to be solved, known or likely conventional solutions, drawbacks of known solutions, and why an additional solution is needed.

### 2. Invention points
Include core technical idea, main modules or steps, distinguishing features, advantages over known solutions, and technical effects.

### 3. Detailed description
Include system architecture, processing flow, data structures, scoring/matching/ranking/decision logic, optional embodiments, fallback or validation logic, and neutral implementation illustration.

### 4. Optional drawings
Suggest drawings such as overall architecture, data flow, preprocessing/building phase, query/response phase, scoring/decision flow, and output/rendering flow.

### 5. Open questions
List facts to confirm before finalizing, including implementation status, optional embodiments, available data, rule/model/hybrid logic, main flow versus fallback flow, and desired protection scope.

## Output templates

### Technical problem
```text
The technical problem is that [system/process] cannot reliably [desired technical result] under [technical constraint], leading to [technical failure or inefficiency].
```

### Invention concept
```text
The proposed solution performs [technical process] by:
1. [technical step 1]
2. [technical step 2]
3. [technical step 3]

This produces [technical effect] compared with [known approach].
```

### Known-solution comparison
```text
Known approach: [conventional mechanism]
Limitation: [technical drawback]
Proposed difference: [distinguishing technical feature]
Effect: [technical improvement]
```

### Disclosure summary
```text
This invention relates to [technical field]. It addresses [technical problem] by [core technical mechanism]. The system includes [main components]. Compared with conventional approaches, it improves [technical effects].
```

## Quality checks

Before finalizing any patent-oriented output, verify:

- The technical problem is specific.
- The solution includes concrete technical steps.
- The difference from conventional approaches is explicit.
- The invention is not framed only as a business rule or abstract idea.
- Confirmed implementation and optional embodiments are separated.
- The disclosure does not rely on real examples unless user-provided or requested.
- Legal or filing advice is framed as requiring patent counsel.
- Open questions are listed.

## Handling uncertainty

Use these labels when facts are not confirmed:

- **Confirmed:** supported by user-provided facts.
- **Assumption:** inferred but not confirmed.
- **Optional embodiment:** possible implementation variant.
- **Needs confirmation:** must be checked before filing or final drafting.

## Common pitfalls to avoid

- Do not treat a generic AI application as an invention without technical mechanisms.
- Do not treat a placeholder, index, cache, vector search, or classifier alone as automatically inventive.
- Do not collapse multiple stages into vague language such as "the AI processes the data".
- Do not ignore implementation constraints.
- Do not overfit the claim direction to one embodiment.
- Do not include confidential names unless the user explicitly includes them and wants them used.
- Do not include real-world examples unless provided or requested.

## Recommended response formats

For analysis tasks:
```text
1. Technical problem
2. Existing or conventional approaches
3. Candidate inventive features
4. Strongest invention concept
5. Technical effects
6. Risks and open questions
7. Suggested next step
```

For disclosure drafting:
```text
1. Background
2. Invention points
3. Detailed description
4. Optional drawings
5. Open questions
```

For brainstorming:
```text
1. Clarifying questions
2. Pain points
3. Candidate ideas
4. Patent-potential ranking
5. Recommended idea to develop
```
