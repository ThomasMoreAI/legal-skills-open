# Contract Clause Library

## Standard Clause Alternatives by Risk Position

This library provides preferred, acceptable, and fallback language for common contract provisions.

---

## 1. Confidentiality Clauses

### Definition of Confidential Information

**Preferred (Narrow)**:
```
"Confidential Information" means information disclosed by one party to the other
that is marked "Confidential" or, if disclosed orally, identified as confidential
at the time of disclosure and confirmed in writing within thirty (30) days.
```

**Acceptable (Moderate)**:
```
"Confidential Information" means any non-public technical, business, or financial
information disclosed by one party to the other, whether orally, in writing, or
by inspection, that a reasonable person would understand to be confidential given
the nature of the information and circumstances of disclosure.
```

**Avoid (Too Broad)**:
```
"Confidential Information" means all information disclosed by either party,
including all derivatives, analyses, and materials prepared using such information.
```

### Standard Exceptions

**Required Exceptions**:
```
Confidential Information does not include information that:
(a) is or becomes publicly available through no fault of the receiving party;
(b) was rightfully in the receiving party's possession prior to disclosure;
(c) is rightfully obtained from a third party without restriction;
(d) is independently developed without use of the disclosing party's information; or
(e) is required to be disclosed by law, provided the receiving party gives prompt
    notice and reasonable assistance to the disclosing party to seek protective relief.
```

---

## 2. Indemnification Clauses

### Mutual Indemnification (Preferred)

```
Each party ("Indemnifying Party") shall indemnify, defend, and hold harmless the
other party and its officers, directors, employees, and agents ("Indemnified Parties")
from and against any third-party claims, damages, losses, and expenses (including
reasonable attorneys' fees) arising out of:

(a) the Indemnifying Party's breach of this Agreement;
(b) the Indemnifying Party's gross negligence or willful misconduct; or
(c) the Indemnifying Party's violation of applicable law.
```

### IP Indemnification (Vendor to Customer)

**Preferred (Balanced)**:
```
Vendor shall indemnify Customer against third-party claims that the Services,
as provided by Vendor and used in accordance with this Agreement, infringe any
valid United States patent or copyright. Vendor's obligations do not apply to
claims arising from: (i) modifications not made by Vendor; (ii) combination with
third-party materials; (iii) Customer's specifications; or (iv) use not in
accordance with documentation.
```

**Avoid (Unlimited)**:
```
Vendor shall indemnify Customer against any and all claims that any aspect of
the Services infringes any intellectual property right anywhere in the world.
```

### Indemnification Procedures

**Standard Procedures**:
```
The Indemnified Party shall: (a) promptly notify the Indemnifying Party in writing
of any claim (provided that failure to notify shall not relieve the Indemnifying
Party except to the extent prejudiced); (b) grant the Indemnifying Party sole
control of the defense and settlement; and (c) provide reasonable cooperation
at the Indemnifying Party's expense. The Indemnifying Party shall not settle any
claim that imposes obligations on the Indemnified Party without prior written consent.
```

---

## 3. Limitation of Liability

### Consequential Damages Exclusion

**Preferred (Mutual)**:
```
NEITHER PARTY SHALL BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL,
OR PUNITIVE DAMAGES, INCLUDING LOST PROFITS, LOST REVENUE, OR LOST DATA, REGARDLESS
OF THE FORM OF ACTION OR THEORY OF LIABILITY, EVEN IF ADVISED OF THE POSSIBILITY
OF SUCH DAMAGES.
```

**Standard Carve-outs**:
```
The foregoing limitation shall not apply to: (a) breaches of confidentiality
obligations; (b) indemnification obligations; (c) infringement of intellectual
property rights; (d) gross negligence or willful misconduct; or (e) payment
obligations under this Agreement.
```

### Direct Damages Cap

**Preferred (Balanced)**:
```
EACH PARTY'S TOTAL AGGREGATE LIABILITY UNDER THIS AGREEMENT SHALL NOT EXCEED
THE AMOUNTS PAID OR PAYABLE BY CUSTOMER UNDER THIS AGREEMENT DURING THE TWELVE
(12) MONTH PERIOD IMMEDIATELY PRECEDING THE CLAIM.
```

**Alternative Structures**:
- Fixed amount: "shall not exceed $[X]"
- Per-incident cap: "shall not exceed $[X] per incident"
- Multiple of fees: "shall not exceed [2x/3x] the fees paid"

---

## 4. Termination Clauses

### Termination for Convenience

**Preferred (Mutual with Notice)**:
```
Either party may terminate this Agreement for convenience upon sixty (60) days'
prior written notice to the other party. Upon termination for convenience,
Customer shall pay for all Services rendered through the effective date of termination.
```

### Termination for Cause

**Standard Provision**:
```
Either party may terminate this Agreement immediately upon written notice if the
other party:

(a) materially breaches this Agreement and fails to cure such breach within
    thirty (30) days after receipt of written notice;
(b) becomes insolvent, makes an assignment for the benefit of creditors, or
    becomes subject to bankruptcy proceedings; or
(c) ceases to conduct business in the normal course.
```

### Effect of Termination

**Comprehensive Provision**:
```
Upon termination or expiration:
(a) all rights and licenses granted hereunder shall terminate;
(b) each party shall return or destroy the other party's Confidential Information;
(c) Customer shall pay all amounts due for Services rendered;
(d) the following sections shall survive: [Confidentiality, Limitation of Liability,
    Indemnification, Governing Law, General Provisions].
```

---

## 5. Intellectual Property

### Work Product Ownership (Customer-Favorable)

**Preferred (Customer Owns)**:
```
All Work Product developed by Vendor specifically for Customer under this Agreement
shall be owned exclusively by Customer. Vendor hereby assigns to Customer all right,
title, and interest in and to such Work Product, including all intellectual property
rights therein. Vendor retains ownership of its pre-existing materials and general
knowledge, skills, and experience.
```

### Work Product Ownership (Vendor-Favorable)

**Alternative (Vendor Owns, License to Customer)**:
```
Vendor retains all right, title, and interest in the Deliverables, including all
intellectual property rights. Subject to payment, Vendor grants Customer a perpetual,
non-exclusive, royalty-free license to use the Deliverables for Customer's internal
business purposes.
```

### License Grant (SaaS)

**Standard SaaS License**:
```
Subject to the terms of this Agreement, Vendor grants Customer a non-exclusive,
non-transferable right to access and use the Services during the Subscription Term,
solely for Customer's internal business purposes in accordance with the Documentation.
```

---

## 6. Data Protection

### Data Processing

**Standard Data Protection Clause**:
```
To the extent Vendor processes Personal Data on Customer's behalf, Vendor shall:
(a) process such data only in accordance with Customer's documented instructions;
(b) implement appropriate technical and organizational security measures;
(c) assist Customer in responding to data subject requests;
(d) notify Customer promptly of any data breach;
(e) delete or return all Personal Data upon termination; and
(f) make available information necessary to demonstrate compliance.
```

### Data Security

**Minimum Security Requirements**:
```
Vendor shall implement and maintain administrative, technical, and physical
safeguards designed to: (a) protect the security and confidentiality of Customer
Data; (b) protect against anticipated threats to such data; and (c) protect
against unauthorized access or use. Such measures shall include, at minimum:
encryption in transit and at rest, access controls, audit logging, and regular
security assessments.
```

---

## 7. Warranties

### Service Warranty (SaaS)

**Standard SaaS Warranty**:
```
Vendor warrants that the Services will perform materially in accordance with the
Documentation during the Subscription Term. Customer's sole remedy for breach of
this warranty is, at Vendor's option: (a) correction of the non-conforming Services;
or (b) termination and refund of prepaid fees for the unused portion of the term.
```

### Professional Services Warranty

**Standard Professional Services Warranty**:
```
Vendor warrants that the Services will be performed in a professional and workmanlike
manner by qualified personnel in accordance with generally accepted industry standards.
Customer must report any warranty claim within thirty (30) days of performance.
Vendor's sole obligation is to re-perform the non-conforming Services at no additional cost.
```

### Warranty Disclaimer

**Standard Disclaimer**:
```
EXCEPT AS EXPRESSLY SET FORTH HEREIN, VENDOR MAKES NO WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
OR NON-INFRINGEMENT. VENDOR DOES NOT WARRANT THAT THE SERVICES WILL BE UNINTERRUPTED
OR ERROR-FREE.
```

---

## 8. Force Majeure

### Standard Force Majeure

```
Neither party shall be liable for any failure or delay in performance due to causes
beyond its reasonable control, including acts of God, natural disasters, war, terrorism,
riots, embargoes, labor disputes, government actions, or failures of third-party
telecommunications or power supply. The affected party shall promptly notify the
other party and use reasonable efforts to mitigate the impact. If the force majeure
event continues for more than [sixty (60)] days, either party may terminate this
Agreement without liability.
```

**Note**: Pandemics and cyberattacks should be explicitly addressed post-2020.

---

## 9. Governing Law and Disputes

### Governing Law

**Neutral Jurisdiction**:
```
This Agreement shall be governed by and construed in accordance with the laws of
the State of Delaware, without regard to its conflicts of law principles.
```

### Dispute Resolution

**Tiered Approach**:
```
Any dispute arising under this Agreement shall be resolved as follows:
(a) Negotiation: The parties shall first attempt to resolve the dispute through
    good faith negotiation between senior executives within thirty (30) days;
(b) Mediation: If negotiation fails, the parties shall submit the dispute to
    mediation under [JAMS/AAA] rules;
(c) Litigation: If mediation fails, either party may pursue litigation in the
    courts of [jurisdiction], and each party consents to such jurisdiction.
```

---

## 10. Assignment

### Standard Anti-Assignment

**Preferred**:
```
Neither party may assign this Agreement without the prior written consent of the
other party, which consent shall not be unreasonably withheld. Notwithstanding
the foregoing, either party may assign this Agreement without consent to an
affiliate or in connection with a merger, acquisition, or sale of substantially
all of its assets, provided the assignee agrees in writing to be bound by this
Agreement's terms.
```

---

## Usage Notes

1. **Customization Required**: These clauses are templates; customize for specific transaction context
2. **Jurisdiction Check**: Review for compliance with applicable law
3. **Consistency**: Ensure defined terms align throughout agreement
4. **Risk Allocation**: Balance with overall deal economics and relationship
5. **Version Control**: Track which clause version is used in each agreement
