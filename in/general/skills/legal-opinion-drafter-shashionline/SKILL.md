---
name: legal-opinion-drafter-shashionline
title: Legal Opinion Drafter
description: Structure comprehensive legal opinions with proper formatting, citations, analysis, and mandatory legal disclaimers for Indian law matters. This skill should be used when drafting formal legal opinions, research memoranda, or advisory documents requiring professional legal analysis.
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/legal-opinion-drafter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: general
language: en
---

# Legal Opinion Drafter

This skill provides structured templates and guidelines for drafting professional legal opinions following Indian legal practice standards.

## Purpose

Draft well-structured legal opinions by:
1. Following standard opinion format (Issue-Rule-Analysis-Conclusion)
2. Ensuring proper legal citations (statutes + case law)
3. Including mandatory disclaimers
4. Maintaining professional tone and precision
5. Organizing complex legal analysis logically

## When to Use This Skill

Use this skill when:
- Drafting formal legal opinions for clients
- Creating research memoranda on legal issues
- Preparing advisory documents on Indian law
- Responding to legal queries requiring detailed analysis
- Documenting legal positions with supporting authorities

## Standard Opinion Structure

### Format Template

```markdown
# LEGAL OPINION

**Matter**: [Brief description]
**Date**: [Date of opinion]
**Prepared By**: Claude Code - Indian Law Knowledge System
**Reference**: [File/matter reference if applicable]

---

## 1. QUESTION(S) PRESENTED

[Concise statement of legal issue(s) to be analyzed]

Example:
1. Whether a suit for specific performance filed on November 28, 2024 for a sale agreement dated January 1, 2020 with performance date June 1, 2020 is within the limitation period prescribed under the Limitation Act, 1963?

---

## 2. BRIEF ANSWER

[1-3 sentence summary conclusion]

Example:
Yes, the suit is within limitation. Under Article 54 of the Limitation Act, 1963, the limitation period is three years from the date fixed for performance. With the COVID-19 Supreme Court extension of 531 days, the final deadline is November 28, 2024.

---

## 3. FACTS

[Relevant factual background - only material facts]

Guidelines:
- Chronological presentation
- Dates in clear format (January 1, 2020)
- Only legally relevant facts
- Numbered for easy reference

Example:
1. On January 1, 2020, the parties entered into a sale agreement for immovable property located at [address].
2. The agreement fixed June 1, 2020 as the date for performance.
3. The seller refused to execute the sale deed on June 15, 2020.
4. Prior to filing this suit, no litigation was pending between the parties.

---

## 4. APPLICABLE LAW

### 4.1 Statutory Provisions

[Cite relevant statutes with full citation on first mention]

Example:
**Limitation Act, 1963**
- Section 3: Mandatory bar on suits instituted after prescribed period
- Article 54: "For the specific performance of a contract" - Three years from date fixed for performance or, if no such date is fixed, from the date on which the plaintiff has notice that performance is refused

**Specific Relief Act, 1963** (as amended 2018)
- Section 10: Specific performance of contracts
- Section 20: Discretion as to decreeing specific performance (mandatory post-2018 Amendment)

### 4.2 Case Law

[Cite binding precedents with proper AIR/SCC citations]

Example:
**Supreme Court Precedents**:

1. **Cognizance for Extension of Limitation Period – COVID-19 v. Union of India**, Miscellaneous Application No. 21 of 2022 in Suo Motu Writ Petition (Civil) No. 3/2020
   - Held: Extension of limitation period by 531 days from March 15, 2020 to October 2, 2021
   - Applicability: All proceedings including suits, appeals, applications

2. **Basawaraj v. Land Acquisition Officer**, AIR 2013 SC 3109
   - Held: Limitation is mandatory; court has no discretion to extend (except Section 5 for appeals/applications)

---

## 5. ANALYSIS

[Detailed legal reasoning applying law to facts]

Structure:
- Start with statutory framework
- Apply case law principles
- Address counter-arguments
- Distinguish unfavorable precedents if any

Example:
### 5.1 Limitation Period Calculation

Under Article 54 of the Limitation Act, 1963, the limitation period for a suit for specific performance is three years. The critical question is determining when this period commences.

#### Starting Point
The Schedule to the Limitation Act specifies that the period begins to run "from the date fixed for performance or, if no such date is fixed, when the plaintiff has notice that performance is refused."

In the present case, the agreement fixed June 1, 2020 as the performance date. However, actual refusal occurred on June 15, 2020. Under Article 54, limitation commences from the refusal to perform (June 15, 2020), not the fixed date, when refusal occurs after the fixed date.

#### Basic Limitation Calculation
- Starting Point: June 15, 2020
- Period: 3 years
- Basic Expiry: June 15, 2023

#### COVID-19 Extension
The Supreme Court in *Cognizance for Extension* extended limitation by 531 days for the period March 15, 2020 to October 2, 2021. Since the limitation period in this case expired on June 15, 2023 (after the COVID extension ended), but was running during the extension period, the full 531-day extension applies.

- Basic Expiry: June 15, 2023
- COVID Extension: + 531 days
- Final Deadline: November 28, 2024

#### Conclusion on Limitation
The suit filed on November 28, 2024 is **on the last day** of the extended limitation period and is therefore within time under Section 3 of the Limitation Act, 1963.

### 5.2 [Additional analysis sections as needed]

---

## 6. CONCLUSION

[Definitive conclusion with legal basis]

Example:
Based on the foregoing analysis, I conclude that:

1. **Limitation**: The suit for specific performance is within the limitation period prescribed under Article 54 of the Limitation Act, 1963, as extended by the Supreme Court COVID-19 order. The final deadline is November 28, 2024.

2. **Maintainability**: Subject to compliance with other procedural requirements, the suit is maintainable.

3. **Recommendation**: Given that the suit is being filed on the final day of limitation, immediate filing is critical to avoid dismissal under Section 3 of the Limitation Act.

---

## 7. QUALIFICATIONS & ASSUMPTIONS

[State any assumptions made or qualifications to opinion]

Example:
This opinion is based on the following assumptions:
1. All facts provided are accurate and complete
2. No prior litigation between parties on same subject matter
3. No fraud, misrepresentation, or mistake alleged (which could alter limitation under Section 17)
4. Plaintiff has clean hands and is ready and willing to perform

---

## 8. REFERENCES

[List all authorities cited]

**Statutes**:
- Limitation Act, 1963
- Specific Relief Act, 1963 (as amended 2018)

**Cases**:
- Cognizance for Extension of Limitation Period – COVID-19 v. Union of India, Miscellaneous Application No. 21 of 2022 in Suo Motu Writ Petition (Civil) No. 3/2020
- Basawaraj v. Land Acquisition Officer, AIR 2013 SC 3109

---

## LEGAL DISCLAIMER

**This opinion provides legal information and analysis based on Indian law as understood by the Claude Code - Indian Law Knowledge System. It does NOT constitute legal advice, and should not be relied upon as a substitute for consultation with a qualified advocate enrolled with a Bar Council.**

**Key Limitations**:
1. This is an AI-generated analysis based on available legal information
2. Legal interpretations may vary; courts have final authority
3. Facts may change requiring different legal analysis
4. Recent developments may not be reflected
5. Jurisdiction-specific variations may apply

**Recommendations**:
- Consult a qualified advocate before taking any legal action
- Verify all statutory citations and case law independently
- Confirm current applicability of legal provisions
- Seek professional opinion for time-critical matters

**Liability Disclaimer**: No responsibility is assumed for actions taken based on this opinion. Users are solely responsible for verifying accuracy and seeking professional legal counsel.

---

**Opinion Version**: 1.0
**Generated**: [Date and Time]
**System**: Claude Code - Indian Law Knowledge Ecosystem v2.0
```

## Opinion Components Explained

### 1. Question Presented
- **Purpose**: Frame precise legal issue
- **Format**: Single sentence question
- **Style**: Neutral, not leading

**Good Example**:
> Whether Section 10 of the Specific Relief Act, 1963 (as amended 2018) mandates specific performance or court retains discretion?

**Poor Example**:
> Tell me about specific performance

### 2. Brief Answer
- **Length**: 1-3 sentences max
- **Content**: Direct answer + key legal basis
- **Style**: Conclusive, not tentative

### 3. Facts
- **Relevance**: Only material facts affecting legal analysis
- **Chronology**: Present in time order
- **Neutrality**: Objective presentation, no advocacy

### 4. Applicable Law
- **Hierarchy**: Constitution → Statutes → Case Law
- **Citations**: Full citation on first mention (use legal-citation-validator skill)
- **Relevance**: Only directly applicable provisions

### 5. Analysis
- **Structure**: Issue-by-issue or element-by-element
- **Depth**: Detailed reasoning, not conclusions
- **Counter-Arguments**: Address opposing views
- **Synthesis**: Integrate statutes + case law

### 6. Conclusion
- **Definitiveness**: Clear answer to question presented
- **Basis**: Summarize key legal support
- **Recommendations**: Practical next steps if appropriate

### 7. Qualifications
- **Assumptions**: State what opinion assumes to be true
- **Limitations**: Note scope of analysis
- **Caveats**: Identify areas of uncertainty

### 8. References
- **Completeness**: List ALL authorities cited
- **Format**: Consistent citation style
- **Organization**: By source type (statutes, cases, secondary)

### 9. Disclaimer
- **Mandatory**: ALWAYS include
- **Comprehensive**: Cover all limitation scenarios
- **Professional**: Emphasize need for qualified counsel

## Writing Style Guidelines

### Tone
- **Professional**: Formal legal language
- **Objective**: Neutral analysis, not advocacy
- **Precise**: Exact legal terminology
- **Clear**: Avoid unnecessary jargon

### Language Rules
- Use "shall" for mandatory provisions
- Use "may" for discretionary provisions
- Avoid contractions (don't → do not)
- Use present tense for legal principles
- Use past tense for facts
- Use "I conclude" not "I think" or "I believe"

### Formatting
- **Headings**: Numbered, hierarchical
- **Lists**: Numbered for steps, bullet for items
- **Emphasis**: Bold for case names, italics for emphasis
- **Citations**: Inline with proper punctuation

## Integration

### With Skills
- **legal-citation-validator**: Validate all citations before finalizing
- **legal-research-assistant**: Research authorities cited
- **limitation-calculator**: For time-sensitive opinions

### With Agents
- All specialized agents use this format for formal outputs
- Master orchestrator invokes for comprehensive responses

### With Commands
- `/legal-opinion <question>` triggers this skill

## Templates by Opinion Type

Refer to @references/opinion-templates.md for:
- Contractual interpretation opinion
- Constitutional law opinion
- Litigation viability opinion
- Compliance opinion
- Transactional opinion

Refer to @assets/opinion-templates/ for pre-formatted templates

## Quality Checklist

Before finalizing opinion:
- [ ] Question clearly presented
- [ ] Brief answer matches detailed conclusion
- [ ] All facts material and verified
- [ ] Statutes cited with full title + year (first mention)
- [ ] Cases cited with proper AIR/SCC format
- [ ] Analysis addresses question directly
- [ ] Counter-arguments considered
- [ ] Conclusion is definitive
- [ ] Assumptions stated explicitly
- [ ] References complete
- [ ] **LEGAL DISCLAIMER included**
- [ ] No spelling/grammatical errors
- [ ] Citations validated (use legal-citation-validator)

## Tools Required

This skill uses:
- **Read**: Access templates and references
- **Write**: Draft opinion document
- **legal-citation-validator**: Validate citations

## Disclaimer

This skill provides opinion drafting guidance following Indian legal practice standards. It does not constitute legal advice. All opinions generated must:
- Include mandatory legal disclaimer
- Be reviewed by qualified advocates
- Not be relied upon without professional verification
- State limitations explicitly

**REMEMBER**: Every legal opinion MUST include clear disclaimer that it is NOT legal advice and professional consultation is required.

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-12-05
**Part of**: Indian Law Knowledge Ecosystem
**Dependencies**: legal-citation-validator
**Critical Requirement**: MANDATORY LEGAL DISCLAIMER
