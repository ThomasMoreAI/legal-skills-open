---
name: patient-consent-simplifier
title: Patient Consent Simplifier
description: Simplifies informed consent documents into patient-friendly language while maintaining regulatory compliance. Readability assessment targeting 6th-8th grade level, risk/benefit clarification in table format, and FDA 21CFR50/ICH-GCP/HIPAA compliance validation.
author: aipoch
author_url: https://github.com/aipoch/medical-research-skills/tree/main/scientific-skills/Other/patient-consent-simplifier
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

> **Source**: [https://github.com/aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)

# Patient Consent Simplifier

Transform complex informed consent documents into patient-friendly language while maintaining regulatory compliance and ethical standards.

## Quick Check

Use this command to verify that the packaged script entry point can be parsed before deeper execution.

```bash
python -m py_compile scripts/main.py
```

## Audit-Ready Commands

Use these concrete commands for validation. They are intentionally self-contained and avoid placeholder paths.

```bash
python -m py_compile scripts/main.py
python scripts/main.py --help
python scripts/main.py --text "Audit validation sample with explicit methods, findings, and conclusion."
```

## When to Use

- Use this skill when simplifying informed consent documents or translating medical procedures for patients.
- Use this skill when creating patient-friendly research summaries or adapting clinical trial information for lay audiences.
- Use this skill when the user says "simplify consent", "plain language consent", or "patient-friendly consent form".

## Workflow

1. **Receive document and target**: Collect the consent document text and confirm target reading level (default: 8th grade for general population; 6th grade for vulnerable populations; 4th-5th grade for health literacy challenges).
2. **Extract legal elements**: Catalog all required regulatory elements: purpose, procedures, risks, benefits, alternatives, confidentiality, compensation, contacts, voluntary participation statement.
3. **Checkpoint**: Verify with user that all required legal elements are captured before simplification begins. If elements are missing, list them explicitly.
4. **Simplify each section**: Break sentences >20 words; replace jargon with common terms (use active voice, "you/your"); add visual aid placeholders.
5. **Clarify risks and benefits**: Present risk/benefit information in table format with likelihood and severity. Use emoji or color scales for accessibility.
6. **Checkpoint**: User confirms that risk/benefit balance is accurately preserved after simplification. If risk is downplayed, revise.
7. **Assess readability**: Run readability assessment. If target grade not met, iterate on complex sections.
8. **Check compliance**: Validate against FDA 21CFR50, ICH-GCP, HIPAA. Flag any missing elements.
9. **Output**: Deliver simplified document with readability metrics (grade level, suggestions) and compliance status.
10. **Fallback**: If source document is too fragmentary to simplify, return a structured checklist of missing elements and a partial simplification of available sections.

## Quick Start

```python
from scripts.consent_simplifier import ConsentSimplifier

simplifier = ConsentSimplifier()

# Simplify consent form
simplified = simplifier.simplify(
    document="clinical_trial_consent.pdf",
    reading_level="8th_grade",
    preserve_legal=True
)
```

## Core Capabilities

### 1. Document Simplification

```python
result = simplifier.simplify_section(
    section="procedure_description",
    text="Lumbar puncture will be performed under sterile conditions...",
    max_sentences=3
)
```

**Simplification Rules:**
- Break long sentences (>20 words)
- Replace medical jargon with common terms
- Use active voice
- Add visual aids placeholders
- Maintain key legal elements

### 2. Risk/Benefit Clarification

```python
risks = simplifier.clarify_risks(
    original_text="Potential adverse events include...",
    format="table",
    severity_scale="emoji"  # or "color", "text"
)
```

**Risk Presentation:**
| Risk | Likelihood | Severity |
|------|-----------|----------|
| Headache | Common (1 in 10) | Mild 😊 |
| Infection | Rare (1 in 1000) | Serious ⚠️ |

### 3. Reading Level Assessment

```python
metrics = simplifier.assess_readability(document)
print(f"Current grade level: {metrics.grade_level}")
print(f"Suggested improvements: {metrics.suggestions}")
```

**Target Levels:**
- **General population**: 8th grade
- **Vulnerable populations**: 6th grade
- **Health literacy challenges**: 4th-5th grade

### 4. Regulatory Compliance Check

```python
compliance = simplifier.check_compliance(
    simplified_document,
    regulations=["FDA_21CFR50", "ICH-GCP", "HIPAA"]
)
```

**Required Elements:**
- [ ] Purpose of research
- [ ] Procedures involved
- [ ] Risks and discomforts
- [ ] Benefits
- [ ] Alternatives
- [ ] Confidentiality
- [ ] Compensation
- [ ] Contact information
- [ ] Voluntary participation

## CLI Usage

```text
# Simplify PDF
python scripts/consent_simplifier.py \
  --input consent_form.pdf \
  --output simplified_consent.pdf \
  --grade-level 8

# Check compliance only
python scripts/consent_simplifier.py \
  --check compliance \
  --input document.pdf
```

## Best Practices

**Do:**
- Use "you" and "your"
- Define terms on first use
- Use bullet points for lists
- Include visual aids
- Test with patient advocates

**Don't:**
- Remove required legal elements
- Downplay significant risks
- Use coercive language
- Exceed recommended length

---

**Skill ID**: 208 | **Version**: 1.0 | **License**: MIT

## Output Requirements

Every final response should make these items explicit when they are relevant:

- Objective or requested deliverable
- Inputs used and assumptions introduced
- Workflow or decision path
- Core result, recommendation, or artifact
- Constraints, risks, caveats, or validation needs
- Unresolved items and next-step checks

## Error Handling

- If required inputs are missing, state exactly which fields are missing and request only the minimum additional information.
- If the task goes outside the documented scope, stop instead of guessing or silently widening the assignment.
- If `scripts/main.py` fails, report the failure point, summarize what still can be completed safely, and provide a manual fallback.
- Do not fabricate files, citations, data, search results, or execution outcomes.

## Input Validation

This skill accepts requests that match the documented purpose of `patient-consent-simplifier` and include enough context to complete the workflow safely.

Do not continue the workflow when the request is out of scope, missing a critical input, or would require unsupported assumptions. Instead respond:

> `patient-consent-simplifier` only handles its documented workflow. Please provide the missing required inputs or switch to a more suitable skill.

## Response Template

Use the following fixed structure for non-trivial requests:

1. Objective
2. Inputs Received
3. Assumptions
4. Workflow
5. Deliverable
6. Risks and Limits
7. Next Checks

If the request is simple, you may compress the structure, but still keep assumptions and limits explicit when they affect correctness.
