# Gdpr Privacy - Sharp Edges

## Consent Not Freely Given

### **Id**
consent-not-freely-given
### **Severity**
critical
### **Summary**
Consent is invalid if there's a power imbalance or no real choice
### **Symptoms**
  - Employee consent for employment data
  - Service denied without consent
  - No alternative to consenting
### **Why**
  GDPR requires consent to be freely given. If data subjects have no
  genuine choice or face negative consequences for refusing, consent
  is invalid. This is especially problematic in employment contexts
  where employees can't refuse employer requests.
  
### **Gotcha**
  "By accepting this job offer, you consent to processing of your
   health data for wellness program participation."
  
  # Employees can't freely refuse! Use different legal basis.
  
### **Solution**
  1. Use appropriate legal basis instead:
     - Employment context: Contract or legal obligation
     - Marketing: Legitimate interests with opt-out
     - Essential processing: Contract performance
  
  2. If consent is required:
     - Ensure genuine choice exists
     - No penalty for refusing
     - Easy to withdraw
  

## Missed 72-Hour Breach Notification

### **Id**
missed-72-hour-breach
### **Severity**
critical
### **Summary**
Failure to notify supervisory authority within 72 hours
### **Symptoms**
  - Breach detected but not logged
  - No clear breach assessment process
  - Waiting for 'full investigation'
### **Why**
  GDPR requires notification to supervisory authority within 72 hours
  of becoming aware of a breach that poses risk to individuals. Waiting
  for complete investigation is not an excuse. Notification can be
  provided in phases.
  
### **Gotcha**
  Security team: "We detected unauthorized access 3 days ago but
                  wanted to complete the forensic investigation
                  before reporting."
  
  # Already past the 72-hour deadline!
  
### **Solution**
  1. Immediate breach logging:
     - Timestamp of detection
     - Initial assessment
  
  2. 72-hour decision framework:
     - Risk assessment within 24 hours
     - Notification decision within 48 hours
     - Submit notification or document why not required
  
  3. Phased notification:
     "We are aware of a breach affecting approximately X users.
      Investigation ongoing. Updates to follow."
  

## Inadequate or Missing DPIA

### **Id**
inadequate-dpia
### **Severity**
high
### **Summary**
High-risk processing without proper Data Protection Impact Assessment
### **Symptoms**
  - New technology processing personal data
  - Large-scale processing of sensitive data
  - Systematic monitoring of public areas
  - No DPIA documentation
### **Why**
  GDPR Article 35 requires DPIA before high-risk processing. Without it,
  you can't demonstrate compliance and may miss significant privacy risks.
  The EDPB has defined 9 criteria - meeting 2 or more triggers DPIA requirement.
  
### **Gotcha**
  "We're launching an AI-powered facial recognition for store security.
   It's just to prevent theft, so no DPIA needed."
  
  # Large-scale biometric monitoring = mandatory DPIA!
  
### **Solution**
  DPIA required when 2+ criteria met:
  1. Evaluation/scoring
  2. Automated decision-making with legal effects
  3. Systematic monitoring
  4. Sensitive data or vulnerable subjects
  5. Large scale processing
  6. Matching/combining datasets
  7. Innovative technology
  8. Preventing data subjects from exercising rights
  9. Data transfers outside EU
  
  Conduct DPIA before processing begins.
  

## Invalid International Data Transfer

### **Id**
international-transfer-invalid
### **Severity**
high
### **Summary**
Transferring data outside EU without valid mechanism
### **Symptoms**
  - Using US cloud providers
  - Offshore development team access
  - No SCCs or adequacy decision
### **Why**
  Post-Schrems II, transfers to countries without adequacy decisions
  require Standard Contractual Clauses plus supplementary measures.
  Simply using SCCs may not be enough if destination country law
  undermines protections.
  
### **Gotcha**
  "We use AWS US-East for storage but we signed their DPA,
   so we're compliant."
  
  # SCCs alone may not be sufficient. Need Transfer Impact Assessment.
  
### **Solution**
  1. Transfer Impact Assessment (TIA):
     - Assess destination country law
     - Document surveillance risks
     - Identify supplementary measures
  
  2. Supplementary measures:
     - End-to-end encryption (customer-held keys)
     - Pseudonymization before transfer
     - Contractual commitments not to comply with access requests
  
  3. Consider EU-based alternatives when possible
  