# GDPR Privacy Compliance

## Patterns

### **Golden Rules**
  
---
    ##### **Rule**
Lawful basis first
    ##### **Reason**
No processing without legal justification
  
---
    ##### **Rule**
Purpose limitation
    ##### **Reason**
Only use data for stated purposes
  
---
    ##### **Rule**
Data minimization
    ##### **Reason**
Collect only what's necessary
  
---
    ##### **Rule**
Privacy by design
    ##### **Reason**
Build compliance into systems
  
---
    ##### **Rule**
Document everything
    ##### **Reason**
Accountability requires records
### **Legal Bases**
  #### **Consent**
    ##### **Requirements**
      - Freely given
      - Specific
      - Informed
      - Unambiguous
      - Easy to withdraw
    ##### **Use When**
No other basis applies, user has genuine choice
  #### **Contract**
    ##### **Requirements**
      - Processing necessary for contract
      - Data subject is party to contract
    ##### **Use When**
Fulfilling contractual obligations
  #### **Legal Obligation**
    ##### **Requirements**
      - Required by EU or member state law
      - Document the legal requirement
    ##### **Use When**
Tax records, employment law, AML
  #### **Vital Interests**
    ##### **Requirements**
      - Life or death situation
      - No other basis available
    ##### **Use When**
Medical emergencies only
  #### **Public Task**
    ##### **Requirements**
      - Official authority or public interest
      - Basis in law
    ##### **Use When**
Government functions
  #### **Legitimate Interests**
    ##### **Requirements**
      - Conduct LIA (Legitimate Interests Assessment)
      - Balance against data subject rights
      - Document the assessment
    ##### **Use When**
Business need, fraud prevention, security
### **Data Subject Rights**
  #### **Access**
    ##### **Timeline**
1 month
    ##### **Response**
Provide copy of data being processed
  #### **Rectification**
    ##### **Timeline**
1 month
    ##### **Response**
Correct inaccurate data
  #### **Erasure**
    ##### **Timeline**
1 month
    ##### **Exceptions**
      - Legal obligation
      - Public interest
      - Legal claims
  #### **Portability**
    ##### **Timeline**
1 month
    ##### **Format**
Machine-readable (JSON, CSV)
  #### **Objection**
    ##### **Timeline**
Immediately stop processing
    ##### **Exceptions**
Compelling legitimate grounds
  #### **Restriction**
    ##### **Timeline**
1 month
    ##### **Effect**
Store but don't process
### **Breach Response**
  #### **Timeline**
    ##### **Detection**
Immediately log and assess
    ##### **Authority Notification**
72 hours if risk to rights
    ##### **Data Subject Notification**
Without undue delay if high risk
  #### **Assessment Criteria**
    - Type of data affected
    - Number of individuals
    - Severity of consequences
    - Likelihood of harm

## Anti-Patterns


---
  #### **Pattern**
Consent for everything
  #### **Problem**
Often not freely given
  #### **Solution**
Use appropriate legal basis

---
  #### **Pattern**
Dark patterns for consent
  #### **Problem**
Not freely given
  #### **Solution**
Equal prominence for accept/reject

---
  #### **Pattern**
Bundled consent
  #### **Problem**
Not specific
  #### **Solution**
Granular consent options

---
  #### **Pattern**
Pre-ticked boxes
  #### **Problem**
Not unambiguous
  #### **Solution**
Require affirmative action

---
  #### **Pattern**
Ignoring DSR deadlines
  #### **Problem**
Regulatory violation
  #### **Solution**
Automated tracking and alerts

---
  #### **Pattern**
No data retention policy
  #### **Problem**
Storage limitation violation
  #### **Solution**
Define and enforce retention periods