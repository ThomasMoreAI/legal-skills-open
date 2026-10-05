---
name: contract-analyzer-shashionline
title: Contract Analyzer Skill
description: Systematically analyzes contract formation, validity, performance obligations, and potential issues under Indian Contract Act 1872 and related statutes
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/contract-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: contracts
language: en
---

# Contract Analyzer Skill

## Purpose

Reusable analytical capability for systematically analyzing contract formation, validity, performance obligations, and potential issues under Indian Contract Act 1872 and related statutes.

## When to Use

- User asks about contract validity
- Need to check if agreement is enforceable
- Analyzing contract terms and obligations
- Identifying defects in formation
- Assessing compliance with statutory requirements

## Knowledge Base

**Protocols**:
- IL-CONTRACT-FORMATION
- IL-CONTRACT-CAPACITY
- IL-CONTRACT-FREE-CONSENT
- IL-CONTRACT-LEGALITY
- IL-CONTRACT-VOID-VOIDABLE
- IL-CONTRACT-PERFORMANCE

## Analytical Framework

### Phase 1: Contract Identification

**Input Required**:
1. Contract text or description
2. Parties (names, type - individual/company, age if relevant)
3. Subject matter (goods, services, property)
4. Consideration (amount, terms)
5. Date of formation
6. Oral or written

**Output**: Contract classification (type, special contract category)

### Phase 2: Validity Analysis (Section 10 Elements)

**Systematic Check**:

#### Element 1: Offer and Acceptance (Sections 2(a), 2(b))
- **Offer exists**: Clear proposal to do/abstain from doing something?
- **Acceptance**: Unconditional assent communicated to proposer?
- **Consensus ad idem**: Meeting of minds?
- **Communication**: Properly communicated (Section 4 postal rule if applicable)?

**Defects**:
- No valid offer (invitation to treat mistaken for offer)
- Conditional acceptance (counter-offer - Section 7)
- Acceptance not communicated
- Cross-offers (no contract)

#### Element 2: Consideration (Sections 2(d), 25)
- **Present**: Something given at time of contract?
- **Past**: Something already done (valid if at promisor's desire)?
- **Future**: Promise to do something?
- **From promisee or third party**: Can move from any person (Chinnaya v. Ramaya)?
- **Real but need not be adequate**: Some value, but adequacy not relevant?

**Section 25 Exceptions** (no consideration required):
1. Love and affection (written, registered, near relation)
2. Past voluntary services (written, signed)
3. Time-barred debt promise (written, signed)

**Defects**:
- No consideration (unless Section 25 exception)
- Illusory consideration
- Past consideration (not at promisor's desire)

#### Element 3: Capacity (Sections 10-12)
- **Age of majority**: Not minor (under 18)?
- **Sound mind**: Capable of understanding + forming rational judgment?
- **Not disqualified**: Not alien enemy, undischarged insolvent, convict during sentence?

**Mohori Bibee Principle**: Minor's agreement VOID ab initio (not voidable)

**Defects**:
- Minor party (VOID)
- Unsound mind (lack capacity at contract time)
- Disqualified person

#### Element 4: Free Consent (Sections 13-22)
**Section 14**: Consent free when not caused by:

**A. Coercion** (Section 15):
- Committing/threatening IPC offense?
- Unlawful detention/threat of detention of property?

**B. Undue Influence** (Section 16):
- Dominant position exists (authority, fiduciary, mental weakness)?
- Position used to obtain unfair advantage?
- Section 16(3) presumption if dominant + unconscionable?

**C. Fraud** (Section 17):
- False suggestion (believed true by speaker)?
- Active concealment of material fact?
- Promise without intention to perform?
- Act fitted to deceive?
- Act declared fraudulent by law?

**D. Misrepresentation** (Section 18):
- Innocent false statement (speaker believes true)?
- Breach of duty causing other party error?
- Party causing consent has no knowledge/belief in truth?

**E. Mistake** (Section 20-22):
- **Bilateral mistake of fact** (essential to agreement) → VOID
- **Unilateral mistake**: Generally valid (except identity, non est factum)
- **Mistake of law**: Valid (Section 21)

**Defects**:
- Vitiated consent (coercion, fraud, misrepresentation, undue influence) → **Voidable** (Section 19)
- Mutual mistake of fact → **Void** (Section 20)

#### Element 5: Lawful Object and Consideration (Section 23)
**Void if**:
- Forbidden by law
- Defeats provisions of law
- Fraudulent
- Involves injury to person/property
- Immoral
- Opposed to public policy

**Section 27**: Restraint of trade void (exception: sale of goodwill - reasonable restraint)
**Section 28**: Restraint of legal proceedings void (exception: arbitration valid)
**Section 30**: Wagering agreements void

**Defects**:
- Unlawful object/consideration → **Void**
- Restraint of trade (Section 27) → **Void**
- Wagering (Section 30) → **Void**

#### Element 6: Not Expressly Void (Sections 26-30)
- **Section 26**: Restraint of marriage → Void
- **Section 27**: Restraint of trade → Void (with exceptions)
- **Section 28**: Restraint of legal proceedings → Void (except arbitration)
- **Section 29**: Uncertainty/wagering → Void
- **Section 30**: Wagering agreements → Void

**Defects**: Falls under Sections 26-30 → **Void**

#### Element 7: Certainty (Section 29)
- Terms definite and ascertainable?
- No vagueness or ambiguity?
- Performance possible to determine?

**Defects**: Vague/uncertain terms → **Void** (Section 29)

#### Element 8: Possibility of Performance (Section 56)
- Performance possible (not impossible by nature)?
- Not forbidden by law?

**Defects**: Impossible act → **Void** (Section 56)

### Phase 3: Classification Determination

**Decision Tree**:

1. **All Section 10 elements satisfied** → **VALID** (enforceable)

2. **Element defect - vitiated consent** (coercion, fraud, misrepresentation, undue influence) → **VOIDABLE** at option of aggrieved party (Section 19, 19A)

3. **Element defect - capacity** (minor) → **VOID AB INITIO** (Mohori Bibee)

4. **Element defect - unlawful object, restraint, uncertainty, impossibility** → **VOID** (no effect)

### Phase 4: Consequences and Remedies

**If VALID**:
- Enforceable by both parties
- Performance required per terms
- Breach remedies available (damages, specific performance, injunction, rescission)

**If VOIDABLE**:
- Aggrieved party options:
  - **Rescind** (Section 64): Cancel + restore status quo
  - **Affirm**: Continue with contract
- **Section 19**: Voidable when consent caused by coercion, fraud, misrepresentation
- **Section 19A**: Voidable when consent caused by undue influence
- **Remedies**: Rescission + damages (if fraud/breach)

**If VOID**:
- No legal effect
- Cannot be enforced
- **Section 65**: Restitution (restore advantage received)
- Exception: *In pari delicto* (both equally guilty) - no restitution

### Phase 5: Performance Obligations Analysis

**(If contract VALID)**

**Section 37-50 Analysis**:

#### Who Must Perform? (Section 40)
- Promisor himself (if personal skill/confidence required)
- Promisor or agent (if not personal)
- Legal representatives (if not personal + promisor dies - Section 37)

#### When to Perform? (Section 46-47)
- Specified time: At that time
- Specified day: During business hours (9am-6pm)
- No time specified: Within reasonable time
- **Time of essence**: Delay = breach

#### Where to Perform? (Section 49)
- Where agreed
- Where reasonable from contract nature
- Promisor's place of business (if nothing specified)

#### How to Perform? (Sections 37-50)
- Exact performance (unless contract allows substantial)
- Standard: As specified or as reasonable person would
- Tender of performance valid (Section 38) even if not accepted (discharges)

#### Reciprocal Promises (Sections 51-58)
- **Mutual and independent**: Performed simultaneously
- **Mutual and dependent**: Order of performance matters
- **Section 53**: If prevented by other party → Contract voidable + compensation

## Output Format

```
## Contract Validity Analysis

### Contract Details
- **Type**: [Contract type]
- **Parties**: [Name, capacity status]
- **Subject Matter**: [Description]
- **Consideration**: Rs. [amount] / [description]
- **Date**: [DD/MM/YYYY]

### Section 10 Validity Check

| Element | Status | Analysis |
|---------|--------|----------|
| **1. Offer & Acceptance** | ✓/✗ | [Clear proposal and unconditional acceptance communicated / Issue: ...] |
| **2. Consideration** | ✓/✗ | [Present/past/future consideration identified / Issue: ...] |
| **3. Capacity** | ✓/✗ | [Both parties competent / Issue: Minor/Unsound mind/Disqualified] |
| **4. Free Consent** | ✓/✗ | [No vitiation / Issue: Coercion/Fraud/Misrepresentation/Undue Influence/Mistake] |
| **5. Lawful Object** | ✓/✗ | [Lawful / Issue: Section 23 violation - specify ground] |
| **6. Not Expressly Void** | ✓/✗ | [Compliant / Issue: Section 26-30 violation] |
| **7. Certainty** | ✓/✗ | [Terms certain / Issue: Vague/ambiguous - Section 29] |
| **8. Possibility** | ✓/✗ | [Performance possible / Issue: Impossible - Section 56] |

### Classification

**Status**: ✓ VALID / ⚠ VOIDABLE / ✗ VOID

**Grounds** (if VOIDABLE or VOID):
- [Specific statutory section + reasoning]

### Consequences

**If VALID**:
- Enforceable by both parties
- Performance required
- Breach remedies: Damages, specific performance, injunction, rescission

**If VOIDABLE**:
- Aggrieved party ([party name]) can:
  - Rescind (Section 64): Cancel + restore benefit
  - Affirm: Continue with contract
- Remedies: Rescission + damages (Section 75 if fraud/breach)

**If VOID**:
- No legal effect
- Not enforceable
- Section 65 restitution: Restore advantage received

### Performance Obligations

[If contract VALID]

**[Party 1] must**:
- [Obligation 1 - Section reference]
- [Obligation 2 - Section reference]

**[Party 2] must**:
- [Obligation 1 - Section reference]
- [Obligation 2 - Section reference]

**Timeline**: [When performance due]
**Place**: [Where performance]
**Standard**: [How to perform]

### Risks and Issues

**Legal Risks**:
1. [Risk 1 + mitigation]
2. [Risk 2 + mitigation]

**Performance Risks**:
1. [Risk 1 + mitigation]
2. [Risk 2 + mitigation]

### Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
...

### Statutory Basis
- Sections: [List all applicable sections]
- Case Law: [Relevant precedents]
```

## Integration

- Use within `/contract-advice` command
- Use within `contract-law-specialist` agent
- Combine with `remedies_evaluator` skill for breach scenarios

---
**Version**: 1.0.0
**Domain**: Contract Law (India)
