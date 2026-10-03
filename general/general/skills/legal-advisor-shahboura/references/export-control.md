# Export Control Guidance

Reference for evaluating export control implications in software projects.

## ECCN Classification

Encryption-related code and certain technologies may require Export Control Classification Number
(ECCN) review under the U.S. Commerce Control List (CCL).

### Encryption Items (ECCN 5A002 / 5D002)

- [ ] Identify cryptographic libraries and their ECCN classification
- [ ] Check if the project calls encryption functions beyond basic DRM/authentication
- [ ] Determine if encryption source code is publicly available (EAR 742.15(b) exception)
- [ ] Note mass-market encryption commodity exceptions where applicable

### Non-Encryption Controlled Technologies

- [ ] Check for restricted/sanctioned technologies (e.g., surveillance, military, dual-use)
- [ ] Verify no EAR99 items are re-exported to sanctioned destinations
- [ ] Review for ITAR-controlled defense articles (if applicable)

## Sanctioned Destinations and Parties

- [ ] Screen against OFAC SDN List for restricted entities
- [ ] Check geographic distribution restrictions (Cuba, Iran, North Korea, Syria, Crimea)
- [ ] Verify no denied parties in the supply chain

## Open-Source Considerations

- [ ] Confirm that publicly available source code qualifies for EAR exception
- [ ] Verify no encryption registration is required for open-source publication
- [ ] Note: contribution from sanctioned countries may require legal review

## Recommended Actions

- [ ] File encryption registration (BIS semi-annual) if required
- [ ] Add EAR classification to export/README for downstream consumers
- [ ] Consult export control counsel for ambiguous classifications
