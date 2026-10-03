# Cybersecurity Cross-Cut

When the workspace contains any of the following `regulatory_reference` entities, the proposal must explicitly address cybersecurity in a dedicated section:

## Triggers

- NIST SP 800-53 (rev 4 / rev 5)
- NIST SP 800-171 (CUI handling)
- NIST SP 800-172 (enhanced)
- CMMC (any level)
- FedRAMP (Low / Moderate / High / IL2 / IL4 / IL5)
- FISMA
- RMF (Risk Management Framework)
- DFARS 252.204-7012, -7019, -7020, -7021

## Required Coverage

Each trigger → at least one of:

- `compliance_artifact` entity for the relevant attestation (3PAO assessment, SSP, CMMC certification)
- `proposal_volume` or `document_section` tagged for cybersecurity
- `requirement` with `MEASURED_BY` a security-domain `performance_standard`

## C6 Finding Template

```
F-XXX  HIGH  C6: Cybersecurity Cross-Cut
  Trigger: NIST SP 800-171 (regulatory_reference)
  Missing: No proposal_volume tagged for cybersecurity coverage
  Remediation: Add a cybersecurity volume or sub-section addressing 800-171 control families
```
