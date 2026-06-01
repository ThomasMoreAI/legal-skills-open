---
name: first-principles
title: 'First Principles: Governance Reasoning Framework'
description: Structured problem decomposition tool. Breaks complex governance questions into fundamental components. Uses Socratic method to challenge assumptions. Outputs structured analysis with assumptions, evidence, and conclusions. Useful for novel governance scenarios without precedent. Use when facing novel governance questions or designing policies for new situations.
author: aadityaparab
author_url: https://github.com/aadityaparab/sentinel-stack/tree/main/skills/first-principles
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# First Principles: Governance Reasoning Framework

This skill applies first-principles reasoning to complex governance questions without clear precedent. It decomposes problems into foundational components, challenges assumptions, and builds reasoning from evidence rather than rules.

## When to Use First Principles

**Use this skill when:**
- Facing a governance question without clear policy precedent
- Policy doesn't clearly cover a new use case
- Multiple interpretations of policy seem valid
- Need to design new policy or control from scratch
- Weighing competing governance principles (transparency vs. security, innovation vs. risk)

**Don't use when:**
- Policy clearly applies (use guardrails instead)
- Precedent already exists (check decision audit)
- Time is critical (use quick decision framework instead)

---

## First Principles Method

### Step 1: Define the Question

State the core question clearly:

```
EXAMPLE: Can we use ChatGPT to auto-generate offer letters to candidates?

Core question: What are the governance requirements for using AI to generate employment offer documents?

Related questions:
- Is this a high-risk AI application?
- What oversight is required?
- What transparency obligations exist?
- What data handling controls are needed?
```

### Step 2: Identify Assumptions

Surfacethey assume:

```
Assumptions we might make:
1. "Auto-generation means no human involvement" (false — humans will review)
2. "AI can't be used for employment decisions" (false — can be used with oversight)
3. "We need full transparency to candidates" (depends on risk tier)
4. "Offer letters are low-risk outputs" (depends on how decision was made)
5. "We have authority to set this policy unilaterally" (may need legal input)
```

**Challenge each assumption:**
- Is it stated or implied?
- What evidence supports it?
- What evidence contradicts it?
- Would we still decide the same if this assumption were false?

### Step 3: Break Into Components

Decompose into fundamental elements:

```
Using AI to generate offer letters involves:

A. DECISION COMPONENT
   - Is offer letter a "decision" or a "document"?
   - Who decides the offer terms? (AI or humans?)
   - Can candidate appeal or negotiate? 

B. DATA COMPONENT
   - What data is input? (Candidate CV, job level, salary band)
   - What data is output? (Offer document with compensation, terms)
   - Is candidate data processed by external AI? (Yes, if using ChatGPT)

C. CONTROL COMPONENT
   - Who reviews? (HR person before sending)
   - Can they override? (Yes, document is editable)
   - Is decision binding after review? (Yes, sent to candidate)

D. REGULATORY COMPONENT
   - Are there employment law implications? (Yes, offer is contract)
   - Are there GDPR implications? (Yes, candidate personal data)
   - Are there anti-discrimination laws? (Yes, salary decisions)

E. TRANSPARENCY COMPONENT
   - Must we tell candidate that AI was used? (Depends on jurisdiction, risk tier)
   - Can we explain how salary was determined? (Maybe not if algorithm-based)
```

### Step 4: Apply First Principles

Build up from fundamentals, not from rules:

```
PRINCIPLE 1: Accountability
Question: Who is responsible if offer is wrong or discriminatory?
Answer: HR person who reviewed and sent it
Implication: That person must understand terms before sending
Control: Human reviewer can't be rubber-stamp

PRINCIPLE 2: Transparency  
Question: What must be disclosed to candidate?
Fundamental: They should know if decision-making logic affects their rights
Answer: If salary was set by algorithm, they should know
Implication: Disclose if AI was used in material decisions

PRINCIPLE 3: Non-Discrimination
Question: Could AI introduce bias in offers?
Fundamental: Equal pay for equal work
Answer: If AI calibrates salary by seniority/role consistently, likely OK
Risk: If AI learned from biased historical data, could replicate bias
Control: Test offers for disparate impact (gender, race pay differences)

PRINCIPLE 4: Data Protection
Question: Is candidate personal data handled safely?
Fundamental: Minimize use of personal data
Answer: Don't send full CV to ChatGPT if job description is enough
Control: Anonymize input to extent possible (use "Senior Engineer, $150-180k band")
```

### Step 5: Evaluate Options

Generate options and reason through each:

```
OPTION A: Don't use AI for offer letters
Pros: Eliminates all AI-related risks
Cons: Misses efficiency gains; adds manual work
First principles test: Is avoiding AI the only way to manage risk?
Verdict: Overly cautious — risk is manageable with controls

OPTION B: Use AI to draft, require human sign-off
Pros: Captures efficiency; maintains human accountability
Cons: HR still needs to review carefully
First principles test: Does human review ensure accountability?
Verdict: Yes, if review is meaningful (not rubber-stamp)

OPTION C: Use AI, full transparency to candidate
Pros: Highest transparency; complies with fairness principle
Cons: May worry candidates; doesn't add value
First principles test: Is transparency the only relevant principle?
Verdict: Yes, but transparency doesn't require rejecting the practice

OPTION D: Use AI for routine offers only (standard packages)
Pros: Reduces risk for most cases; humans handle exceptions
Cons: Need to define "routine"; complex offers still need work
First principles test: Does limiting scope to low-complexity cases reduce risk?
Verdict: Yes, but complex cases may benefit more from AI assistance
```

### Step 6: Synthesize Conclusion

Build your reasoned position:

```
GOVERNANCE DECISION: Limited use of AI for offer letter generation

REASONING:
1. Accountability: Human HR person reviews and sends all offers
2. Transparency: Disclose AI use in candidate communication (e.g., FAQ)
3. Non-discrimination: Test offers monthly for disparate impact
4. Data protection: Don't send full CVs; use anonymized summaries
5. Scope: Use for standard roles (IC1-L4); exceptions reviewed manually

REQUIREMENTS:
- AI-generated offer must be reviewed by HR Lead before sending
- Reviewer sees both AI draft and supporting reasoning
- Reviewer can edit any terms
- Monthly audit of all offers for: accuracy, disparate impact, consistency
- Candidate FAQs disclose "AI-assisted generation with human review"

RATIONALE:
- Respects all first principles (accountability, transparency, fairness)
- Captures efficiency gains (saves HR ~5 hours/week in routine drafting)
- Maintains human control over final decision
- Provides transparency without unnecessarily alarming candidates
- Detects discriminatory patterns through regular auditing

WHAT COULD GO WRONG:
- HR reviewer doesn't actually review (mitigation: spot-check, audit)
- AI generates discriminatory offers (mitigation: monthly disparate impact test)
- Candidate disputes, claims discrimination (mitigation: document review, offer rationale)
- Candidate is concerned about AI (mitigation: transparent disclosure)

MONITORING:
- Monthly: Review sample of all offers (10% random)
- Quarterly: Disparate impact analysis (salary by gender, race, tenure)
- Annually: Decision audit of HR reviewer effectiveness
```

---

## Socratic Question Framework

When reasoning through governance questions, ask yourself:

### Clarification Questions

- What exactly is being asked?
- What are we trying to achieve?
- What would success look like?
- What would failure look like?

### Assumption Questions

- What are we assuming to be true?
- Why do we believe that?
- What if that assumption were wrong?
- What evidence would change our mind?

### Evidence Questions

- What facts do we know?
- What facts are we inferring?
- What could prove us wrong?
- What haven't we considered?

### Implications Questions

- If we decide X, what follows from that?
- What principles support this decision?
- What principles contradict it?
- How does this affect other decisions?

### Justification Questions

- Why is this the right answer?
- Who might disagree? Why?
- What's the strongest argument against our position?
- Could we defend this decision to an auditor?

---

## Structured Analysis Output

Use this template for first-principles conclusions:

```markdown
# Governance Decision: [Title]

## Question
[Clear statement of the governance question]

## Key Assumptions
- Assumption 1: [State and challenge]
- Assumption 2: [State and challenge]
- Assumption 3: [State and challenge]

## Fundamental Components
1. [Component 1 and analysis]
2. [Component 2 and analysis]
3. [Component 3 and analysis]

## Applicable Principles
- **Principle 1:** [Definition and application]
- **Principle 2:** [Definition and application]
- **Principle 3:** [Definition and application]

## Options Considered
1. [Option A]
   - First principles test: [Pass/Fail and why]
2. [Option B]
   - First principles test: [Pass/Fail and why]
3. [Option C]
   - First principles test: [Pass/Fail and why]

## Recommended Decision
[Clear, specific recommendation]

## Reasoning
[Synthesis of first-principles analysis]

## Requirements and Controls
- [Specific requirement]
- [Specific control]
- [Specific monitoring]

## Risks and Mitigations
- [Risk]: [How we mitigate]
- [Risk]: [How we mitigate]

## What Could Change This Decision
[Scenarios that would warrant revisiting]

## Audit Defense
"Why this decision?" — [Short explanation that would hold up to scrutiny]
```

---

## Common Governance Dilemmas

### Innovation vs. Caution
```
Dilemma: Move fast with new AI tool vs. ensure all controls in place
First principles: 
- Risk management says: understand risks before deploying
- Innovation says: experimentation requires some risk tolerance
Resolution: Pilot program with time limit; use "learning by doing" with limits
```

### Transparency vs. Simplicity
```
Dilemma: Full disclosure vs. avoiding decision-paralysis
First principles:
- Transparency principle: affected parties deserve to know
- Autonomy principle: people can choose if informed
Resolution: Disclose material facts; don't disclose technical minutiae
```

### Control vs. Trust
```
Dilemma: Strict policies prevent good decisions; loose policies enable bad ones
First principles:
- Accountability: someone must own the decision
- Competence: trust people to make good decisions if empowered
Resolution: Clear guidelines + human judgment; audit for patterns
```

---

## Integration with Other Skills

- **policy-drafter**: New policies designed using first principles
- **ai-governance**: Novel risk tiers assessed from first principles
- **decision-audit**: First principles reasoning forms basis for audit criteria
- **guardrails**: Hard policies derived from first-principles reasoning
