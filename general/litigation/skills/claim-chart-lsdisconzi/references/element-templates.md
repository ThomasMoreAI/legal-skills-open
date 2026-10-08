# Element Templates — BR/CL Civil Law Claims

This file defines the element-by-element templates for the main civil law claims in the current case. Each template maps the legal elements a plaintiff must prove (or a defendant must disprove) for each claim type across the BR, CL, and INT jurisdictions.

The `claim-chart` skill uses these templates to construct element-by-element claim charts: for each element, map the fact, evidence, and confidence rating.

---

## Brazil (BR) — CDC Consumer Protection Code

### CDC Art. 14 — Supplier Strict Liability (Service Defect)

| Element | Code | Proof Required |
|---|---|---|
| Supplier relationship | CDC.14.1 | Defendant is a service supplier |
| Service defect | CDC.14.2 | Service was defective in safety or quality |
| Consumer harm | CDC.14.3 | Consumer suffered actual harm |
| Causal nexus | CDC.14.4 | Defect caused the harm |

**Defenses to anticipate:** Force majeure, exclusive fault of consumer, exclusive fault of third party (CDC Art. 14, §3).

### CDC Art. 39 — Abusive Practices

| Element | Code | Proof Required |
|---|---|---|
| Consumer relationship | CDC.39.1 | Plaintiff is a consumer |
| Abusive practice | CDC.39.2 | Supplier engaged in enumerated or general abusive practice |
| Consumer vulnerability | CDC.39.3 | Consumer was in vulnerable position |

**Specific abusive practices alleged:**
- **CDC Art. 39, I:** Conditioning supply on excessive requirements
- **CDC Art. 39, IV:** Exploiting consumer weakness
- **CDC Art. 39, V:** Excessive disadvantage

### CDC Art. 42 — Improper Collection

| Element | Code | Proof Required |
|---|---|---|
| Debt claim | CDC.42.1 | Supplier claimed a debt |
| Improper basis | CDC.42.2 | Debt was not owed or was improperly calculated |
| Consumer affected | CDC.42.3 | Consumer suffered consequences |

**Double-payment penalty:** CDC Art. 42, sole paragraph — improper collection entitles consumer to double the amount overpaid.

### CF/88 Art. 5, V + X — Moral Damages (Constitutional)

| Element | Code | Proof Required |
|---|---|---|
| Protected right | CF88.5.1 | Right to dignity, honour, image, privacy |
| Violation | CF88.5.2 | State or private action violated right |
| Proportional damages | CF88.5.3 | Damages proportional to violation |

---

## Chile (CL) — Codigo Aeronautico

### CACH Art. 131 — Denied Boarding / Derecho a Embarque

| Element | Code | Proof Required |
|---|---|---|
| Valid booking | CACH.131.1 | Passenger held confirmed reservation |
| Carrier refusal | CACH.131.2 | Carrier refused boarding without lawful cause |
| No statutory exception | CACH.131.3 | None of the statutory grounds for refusal applied |

### CACH Art. 133 — Nullity of Denied Boarding Without Notice

| Element | Code | Proof Required |
|---|---|---|
| Denied boarding occurred | CACH.133.1 | Passenger was denied boarding |
| No written notice | CACH.133.2 | Carrier failed to provide written notice with reasons |
| Nullity consequence | CACH.133.3 | Denied boarding is null |

---

## Chile (CL) — Ley de Proteccion al Consumidor

### LPDC Art. 3(b) — Right to Truthful Information

| Element | Code | Proof Required |
|---|---|---|
| Consumer relationship | LPDC.3b.1 | Plaintiff is a consumer |
| False information | LPDC.3b.2 | Supplier provided false or misleading information |
| Timely disclosure | LPDC.3b.3 | Information was not provided in timely manner |

### LPDC Art. 23 — Right to Legal and Contractual Compliance

| Element | Code | Proof Required |
|---|---|---|
| Supplier obligation | LPDC.23.1 | Supplier had legal or contractual obligation |
| Non-compliance | LPDC.23.2 | Supplier failed to comply |
| Consumer harm | LPDC.23.3 | Consumer suffered harm |

---

## International — Montreal Convention 1999

### MC99 Art. 17 — Death or Injury of Passengers

| Element | Code | Proof Required |
|---|---|---|
| Accident | MC99.17.1 | An "accident" (unusual, unexpected event external to passenger) occurred |
| On board or embarking/disembarking | MC99.17.2 | Occurred on board or during embarkation/disembarkation |
| Bodily injury | MC99.17.3 | Passenger suffered bodily injury |

### MC99 Art. 19 — Delay

| Element | Code | Proof Required |
|---|---|---|
| Delay | MC99.19.1 | Carrier caused a delay in carriage |
| No reasonable measures | MC99.19.2 | Carrier did not take all reasonable measures to avoid delay |

---

## International — ACHR (American Convention on Human Rights)

### ACHR Art. 7 — Right to Personal Liberty

| Element | Code | Proof Required |
|---|---|---|
| Detention | ACHR.7.1 | Person was detained or deprived of liberty |
| No legal basis | ACHR.7.2 | Detention lacked legal grounds |
| State actor | ACHR.7.3 | State agent performed or authorized detention |

### ACHR Art. 8 — Right to a Fair Trial / Due Process

| Element | Code | Proof Required |
|---|---|---|
| Rights determination | ACHR.8.1 | State made determination affecting rights |
| No due process | ACHR.8.2 | No hearing, no reasons, no opportunity to contest |
| State actor | ACHR.8.3 | State agent made determination |

### ACHR Art. 25 — Right to Judicial Protection

| Element | Code | Proof Required |
|---|---|---|
| Violation of fundamental right | ACHR.25.1 | A Convention-protected right was violated |
| No effective remedy | ACHR.25.2 | State failed to provide effective remedy |

---

## Usage by `claim-chart` Skill

For each claim:
1. Select the applicable jurisdiction and framework
2. For each element in the template, map:
   - **Fact:** The specific case fact that satisfies the element
   - **Evidence:** The specific evidence item(s) supporting the fact
   - **Confidence:** 0.0–1.0 rating for the element
   - **Gaps:** What additional evidence or legal argument is needed
3. Aggregate confidence across elements to rate the overall claim
4. Flag any element where confidence < 0.60 for attorney review

**Cross-jurisdictional note:** Some facts satisfy elements across multiple jurisdictions (e.g., a false accusation may satisfy CDC Art. 39 AND CACH Art. 131 AND MC99 Art. 17). The claim chart should track these overlaps for forum strategy.
