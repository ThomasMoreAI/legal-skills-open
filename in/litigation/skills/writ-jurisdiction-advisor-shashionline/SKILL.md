---
name: writ-jurisdiction-advisor-shashionline
title: 'Skill: Writ Jurisdiction Advisor'
description: Determine which type of writ applies to a legal situation, advise whether to approach Supreme Court or High Court, assess locus standi, and evaluate alternative remedy doctrine
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/writ-jurisdiction-advisor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: litigation
language: en
---

# Skill: Writ Jurisdiction Advisor

## Purpose
Determine which type of writ (habeas corpus, mandamus, certiorari, prohibition, quo warranto) applies to a legal situation, advise whether to approach Supreme Court (Article 32) or High Court (Article 226), assess locus standi (standing to file), and evaluate alternative remedy doctrine applicability.

## Capabilities

### 1. Writ Type Identification
- **Habeas Corpus** ("produce the body") - Illegal detention cases
- **Mandamus** ("we command") - Compel public authority to perform duty
- **Certiorari** ("to be certified") - Quash illegal order/decision
- **Prohibition** ("forbid") - Stop authority from exceeding jurisdiction
- **Quo Warranto** ("by what authority") - Challenge unauthorized appointment

### 2. Forum Selection (Article 32 vs Article 226)
- **Article 32 (Supreme Court)**: Only fundamental rights (Articles 14-35)
- **Article 226 (High Court)**: Fundamental rights + any legal right
- Cost-benefit analysis (HC cheaper, faster vs SC authoritative)
- Territorial jurisdiction assessment

### 3. Locus Standi Evaluation
- **Traditional Rule**: Aggrieved person only
- **PIL Exception**: Public-spirited person for public interest matters
- **Gatekeeping Test**: Genuine vs publicity PIL
- **Third-Party Standing**: When can you file for someone else?

### 4. Alternative Remedy Doctrine
- Identify statutory appellate remedies (tribunals, statutory appeals)
- Exceptions when court will still entertain (jurisdictional error, natural justice violation, perversity)
- Cost-benefit: Tribunal vs direct writ

### 5. Grounds for Judicial Review
- **Illegality** (ultra vires, beyond jurisdiction)
- **Irrationality** (Wednesbury unreasonableness)
- **Procedural Impropriety** (natural justice violation)
- **Proportionality** (action disproportionate to objective)
- **Malafide** (bad faith, abuse of power)

---

## Writ Type Decision Matrix

### Quick Reference Table

| Situation | Writ Type | Issued To | Purpose | Example |
|-----------|-----------|-----------|---------|---------|
| **Illegal detention** | Habeas Corpus | Police, Jail Superintendent | Release person from custody | Arrested without warrant, detention beyond 24 hours |
| **Government refuses to perform duty** | Mandamus | Public Authority | Compel duty performance | Govt refuses to issue license despite eligibility |
| **Want to quash illegal order** | Certiorari | Tribunal, Quasi-Judicial Authority | Quash order, bring to court | Want to cancel transfer order, tax assessment order |
| **Authority exceeding jurisdiction** | Prohibition | Tribunal acting beyond powers | Stop authority from proceeding | Labour Court hearing non-workman case (no jurisdiction) |
| **Unauthorized person holding public office** | Quo Warranto | Person holding office | Inquire into title to office | Person appointed as judge without qualifications |

---

## Detailed Writ Type Analysis

### 1. Habeas Corpus ("Produce the Body")

**When to Use**:
- Person illegally detained (police custody beyond 24 hours without magistrate order)
- Mental asylum confinement without proper procedure
- Private detention (kidnapping - though criminal remedy preferred)
- Immigration detention exceeding statutory limit

**Issued To**:
- Police officer, Jail Superintendent, Hospital Superintendent, Immigration Officer

**What Court Orders**:
- "Produce [Person Name] before this court immediately"
- Court examines legality of detention
- If illegal -> Immediate release ordered

**Statutory Basis**:
- Article 22(1): No detention beyond 24 hours without magistrate
- Article 21: Life and personal liberty (expanded by *Maneka Gandhi* case)

**Example Scenario**:
> **Situation**: Police arrested person on 1st January. No FIR filed, no magistrate order. Person still in custody on 5th January (4 days = illegal).
>
> **Writ Type**: **Habeas Corpus**
>
> **Prayer**: "Issue writ of Habeas Corpus directing Superintendent of Police to produce [Name] before this Hon'ble Court and release him forthwith as detention beyond 24 hours without magistrate order violates Article 22(1)."
>
> **Likely Outcome**: Court orders immediate production + release (unless police shows magistrate remand order).

---

### 2. Mandamus ("We Command")

**When to Use**:
- Public authority **refuses** to perform legal duty
- Authority has **discretion** but refuses to exercise it (must be legal duty, not mere discretion)
- Authority **delays** performing duty unreasonably

**Issued To**:
- Government departments, statutory authorities, public servants, local bodies
- **NOT issued to**: Private individuals/companies (unless performing public function)

**What Court Orders**:
- "Direct [Authority Name] to [perform specific duty] within [timeframe]"

**Conditions for Mandamus**:
1. **Legal duty** exists (not mere power/discretion)
2. Petitioner has **legal right** to compel duty
3. **No alternative remedy** (or alternative inadequate)
4. Petitioner applied and was refused (demand + refusal)

**Example Scenario 1: License Refusal**
> **Situation**: Applied for trade license on 1-Jan. Eligible as per rules. Municipal Corporation rejected on 15-Feb citing "public interest" without reasons.
>
> **Writ Type**: **Mandamus**
>
> **Prayer**: "Issue writ of Mandamus directing Municipal Commissioner to grant trade license to Petitioner, as Petitioner fulfills all statutory requirements under Municipal Act Section [X]."
>
> **Grounds**:
> - Legal duty to grant license if conditions met (Municipal Act Section X)
> - Rejection arbitrary (no reasoned order)
> - Violates Article 14 (equality) and Article 19(1)(g) (right to occupation)
>
> **Likely Outcome**: Court directs Municipal Commissioner to reconsider application and pass reasoned order within 30 days.

**Example Scenario 2: Promotion Denial**
> **Situation**: Government employee eligible for promotion (10 years service, passed exam). Promotion denied without giving reasons. Junior promoted instead.
>
> **Writ Type**: **Mandamus**
>
> **Prayer**: "Issue writ of Mandamus directing respondent department to promote petitioner to [post] as per seniority-cum-merit rule."
>
> **Grounds**:
> - Legal right to promotion (service rules)
> - Arbitrary denial violates Article 14 (equal treatment)
>
> **Likely Outcome**: Court may not directly order promotion (complex factual issues), but will direct department to reconsider with reasoned order.

**Mandamus NOT Issued When**:
- Against private parties (no public duty)
- For discretionary powers (court cannot dictate how discretion exercised)
- For contractual obligations (civil suit, not writ)
- Against legislature (separation of powers)
- Against President/Governor (constitutional immunity - Article 361)

---

### 3. Certiorari ("To Be Certified" - Quashing Order)

**When to Use**:
- Want to **quash** an order passed by inferior court/tribunal/authority
- Order is **illegal** (ultra vires, beyond jurisdiction, violates law)
- Order violates **natural justice** (no hearing given)

**Issued To**:
- Tribunals (Labour Court, NCLT, CAT, etc.)
- Quasi-judicial authorities (Collector, Commissioner, Licensing Authority)
- Inferior courts (only if jurisdictional error - rare)

**What Court Orders**:
- "Quash the order dated [date] passed by [Authority]"
- Often combined with Mandamus: "Quash order + Direct fresh decision"

**Grounds for Certiorari** (Judicial Review):
1. **Jurisdictional Error**: Authority acted beyond jurisdiction
2. **Error of Law Apparent on Face of Record**: Legal mistake obvious from order itself
3. **Violation of Natural Justice**: No hearing, biased decision-maker
4. **Perversity**: Order based on no evidence, contrary to evidence
5. **Non-Application of Mind**: Order passed mechanically without applying mind to facts

**Example Scenario 1: Tax Assessment Quashing**
> **Situation**: Income Tax Officer assessed income at Rs. 50 lakhs (actual: Rs. 10 lakhs). No hearing given before assessment. Notice sent to wrong address.
>
> **Writ Type**: **Certiorari**
>
> **Prayer**: "Issue writ of Certiorari quashing assessment order dated [date] passed by Income Tax Officer."
>
> **Grounds**:
> - Violation of natural justice (no opportunity of hearing - Section 144 of IT Act requires hearing)
> - Assessment arbitrary (Rs. 50 lakhs vs declared Rs. 10 lakhs with no basis)
>
> **Likely Outcome**: Court quashes assessment + directs fresh assessment after proper hearing.

**Certiorari vs Mandamus** (Often Combined):
- **Certiorari**: Quashes bad order (negative relief - removes illegal order)
- **Mandamus**: Compels new decision (positive relief - directs action)
- **Combined Prayer**: "Quash impugned order **AND** direct fresh decision as per law"

---

### 4. Prohibition ("Forbid" - Stop Proceeding)

**When to Use**:
- Authority is **about to act** beyond jurisdiction (prevent future illegality)
- Tribunal/court proceeding with case it has no jurisdiction over

**Difference from Certiorari**:
- **Certiorari**: Quashes order **already passed** (corrective)
- **Prohibition**: Stops authority **before** it acts (preventive)

**Issued To**:
- Tribunals, inferior courts, quasi-judicial authorities

**Example Scenario: Jurisdictional Challenge**
> **Situation**: Labour Court issued notice to non-workman (manager earning Rs. 5 lakh/year). Industrial Disputes Act only covers "workmen" (manual/clerical workers earning < Rs. 10,000/month). Manager files writ before Labour Court passes order.
>
> **Writ Type**: **Prohibition**
>
> **Prayer**: "Issue writ of Prohibition restraining Labour Court from proceeding with Reference Application No. [X] as Petitioner is not a 'workman' under Industrial Disputes Act."
>
> **Grounds**:
> - Labour Court lacks jurisdiction (Petitioner not workman as per Section 2(s) of ID Act)
> - Continuing proceedings would be waste of time + resources
>
> **Likely Outcome**: If HC agrees Petitioner is non-workman -> Prohibition issued, Labour Court proceedings stopped.

**Prohibition NOT Issued**:
- Against administrative actions (only against judicial/quasi-judicial)
- If case already decided (use Certiorari to quash)

---

### 5. Quo Warranto ("By What Authority" - Challenge Appointment)

**When to Use**:
- Person appointed to **public office** without proper authority/qualifications
- Want to challenge **unauthorized holding** of public office

**Issued To**:
- Person holding office + Appointing authority

**What Court Orders**:
- "Show cause why you are holding office of [X]"
- If no valid authority shown -> Declare appointment void, oust person from office

**Conditions**:
1. Office must be **public office** (not private employment)
2. Appointment must be **unauthorized** (violates qualifications, procedure)
3. Petitioner need NOT be aggrieved (any citizen can file - public interest)

**Quo Warranto NOT Issued**:
- Against private employment (company CEO, NGO director - not public office)
- If appointment is merely irregular (not invalid) - court may condone procedural lapses

---

## Forum Selection: Article 32 (SC) vs Article 226 (HC)

### Comparison Matrix

| Factor | Article 32 (Supreme Court) | Article 226 (High Court) |
|--------|---------------------------|--------------------------|
| **Scope** | Only Fundamental Rights (Articles 14-35) | Fundamental Rights + Any Legal Right |
| **Nature** | Guaranteed remedy (cannot refuse) | Discretionary (may refuse) |
| **Jurisdiction** | All India | Territorial (state/union territory) |
| **Cost** | Higher (court fees Rs. 5,000-Rs. 50,000, Senior Advocates Rs. 2-10 lakh) | Lower (fees Rs. 500-Rs. 5,000, Advocates Rs. 10,000-Rs. 1 lakh) |
| **Timeline** | Slower (SC backlog, 1-3 years) | Faster (6 months - 2 years) |
| **Precedent Value** | Binding on all courts (Article 141) | Binding only in state (but persuasive elsewhere) |
| **Alternative Remedy** | Generally no bar (guaranteed remedy) | May refuse if alternative remedy adequate |

---

### Decision Tree: Which Forum to Approach?

```
START: Legal Right Violated
  |
  +-> Is it a FUNDAMENTAL RIGHT violation? (Articles 14-35)
  |   |
  |   +-> YES -> Both Article 32 (SC) and Article 226 (HC) available
  |   |   |
  |   |   +-> Is it a matter of NATIONAL IMPORTANCE?
  |   |   |   -> YES -> Approach Supreme Court (Article 32)
  |   |   |
  |   |   +-> Is it a LOCAL/STATE matter?
  |   |   |   -> YES -> Approach High Court (Article 226)
  |   |   |
  |   |   +-> Do you have LIMITED BUDGET?
  |   |   |   -> YES -> Approach High Court (Article 226)
  |   |   |
  |   |   +-> Do you need AUTHORITATIVE PRECEDENT?
  |   |       -> YES -> Approach Supreme Court (Article 32)
  |   |
  |   +-> NO (Not Fundamental Right) -> Only Article 226 (HC) available
  |       -> Is it a LEGAL RIGHT? -> YES -> File under Article 226 (HC)
  |
  +-> Against PRIVATE PARTY? (Not State under Article 12)
      -> Writ NOT maintainable -> File Civil Suit
```

---

## Locus Standi (Standing to File)

### Traditional Rule: Aggrieved Person

**General Principle**: Only person whose **own legal right** is violated can file writ.

### PIL Exception: Liberalized Standing

**Public Interest Litigation (PIL)**: Any public-spirited person can file for violations affecting:
- Poor, marginalized, unable to approach court
- Large section of public (diffused rights - environment, consumer rights)

**Landmark: *S.P. Gupta v. Union of India* (1982)**:
Supreme Court liberalized standing for public interest matters.

### Gatekeeping: Genuine vs Publicity PIL

**Courts Dismiss**:
- Politician filing for political mileage
- Lawyer filing for professional publicity
- Busybody with no genuine interest

**Test** (*Ashok Kumar Pandey v. State of West Bengal*, 2004):
1. Is petitioner **genuinely interested** in public welfare?
2. Or is petitioner using court for **extraneous purpose**?

---

## Alternative Remedy Doctrine

### General Rule

**L. Chandra Kumar v. Union of India (1997)**:
If **alternative statutory remedy** available, High Court may decline writ.

### Exceptions (When Court Will Entertain Despite Alternative Remedy)

1. **Jurisdictional Error**: Tribunal itself lacks jurisdiction
2. **Violation of Natural Justice**: Fair hearing principles violated
3. **Perversity**: Order based on no evidence, contrary to law
4. **Fundamental Rights Violation**: SC cannot refuse under Article 32
5. **Delay / Ineffective Remedy**: Alternative remedy illusory
6. **Public Interest / Policy Question**: Beyond individual grievance

---

## Integration Points

**Connects With**:
- **CIVIC-WRIT-BASICS**: Constitutional framework (Articles 32, 226)
- **CIVIC-WRIT-TYPES**: Detailed analysis of five writ types
- **CIVIC-TRIBUNALS**: Alternative remedy assessment

**Triggers**:
- User invokes `/pil-guidance` command
- User asks: "Which writ should I file for [situation]?"
- User needs: "Should I go to High Court or Supreme Court?"
- User requests: "Can I file PIL for this issue?"

---

## Protocols Utilized

- CIVIC-WRIT-BASICS.md (constitutional provisions, locus standi, alternative remedy)
- CIVIC-WRIT-TYPES.md (five writ types in detail)
- CIVIC-TRIBUNALS.md (statutory tribunals, alternative remedies)

---

**Version:** 1.0
**Last Updated:** December 2025
**Domain:** Constitutional Writ Jurisdiction (Articles 32, 226 - Forum Selection, Writ Type Identification, Locus Standi Assessment)
