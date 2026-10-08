# DORA Implementation Roadmap, Infrastructure Checks & Troubleshooting

The 9-month implementation plan, quick wins, infrastructure verification checklists, the troubleshooting table for the assessment tools, and the success criteria. Read this when planning a DORA program, validating technical resilience controls, or diagnosing unexpected assessment results.

---

## DORA Implementation Roadmap

### 9-Month Plan

| Month | Phase | Key Activities |
|-------|-------|---------------|
| 1 | **Assessment** | Map ICT risk landscape, identify applicable DORA requirements, gap analysis against 5 pillars |
| 2 | **Framework Design** | Design ICT risk management framework, define governance structure, establish policies |
| 3 | **ICT Risk Management** | Implement risk identification, protection, detection, and response procedures |
| 4 | **Incident Management** | Deploy incident classification, establish reporting procedures, prepare templates |
| 5 | **Third-Party Risk** | Build ICT third-party register, assess critical providers, update contracts |
| 6 | **Third-Party Risk (cont.)** | Complete contractual updates, develop exit strategies, assess concentration risk |
| 7 | **Resilience Testing** | Design testing program, execute basic tests (vulnerability scanning, gap analysis) |
| 8 | **Advanced Testing** | Conduct penetration testing, scenario-based exercises, TLPT preparation (if applicable) |
| 9 | **Validation** | Internal audit, remediation, management body reporting, continuous improvement setup |

### Quick Wins (Month 1–2)

1. Establish ICT risk management governance (management body accountability)
2. Begin building the ICT third-party register
3. Review and update incident response procedures for DORA timelines (4h/72h/1mo)
4. Ensure management body receives regular ICT risk reporting
5. Verify MFA deployment for critical systems
6. Document existing BCP/DRP for ICT systems

---

## Infrastructure Checks

### ICT Asset Inventory

- Maintain a comprehensive register of all ICT assets (hardware, software, network, cloud)
- Classify assets by criticality and map to business functions
- Include dependencies on ICT third-party providers
- Update inventory upon any changes to ICT infrastructure

### Network Resilience Testing

- Annual network security assessments
- Network architecture review and segmentation validation
- DDoS resilience testing for public-facing services
- Redundant network path verification
- Network monitoring and anomaly detection validation

### Data Center Redundancy

- Active-active or active-passive redundancy for critical systems
- Geographic separation of primary and secondary data centers
- Automated failover mechanisms tested regularly
- Power and cooling redundancy verification
- Physical security assessment of data centers

### Business Continuity Testing

- Annual BCP exercise for all critical business functions
- ICT disaster recovery testing covering failover and restoration
- Scenario-based testing (cyber incident, natural disaster, provider failure)
- Recovery time and recovery point validation against targets
- Post-exercise improvement tracking

### Disaster Recovery Capabilities

- Documented DRP for all critical ICT systems
- Backup restoration tested on separate environments
- Immutable backup storage for ransomware resilience
- Communication plans for disaster scenarios
- Coordination procedures with ICT third-party providers

### Third-Party Dependency Mapping

- Map all ICT third-party providers to business functions
- Identify critical dependencies and single points of failure
- Assess concentration risk across providers
- Document sub-contractor chains for critical services
- Verify provider business continuity capabilities

---

## Troubleshooting

| Problem | Possible Cause | Resolution |
|---------|---------------|------------|
| Readiness score unexpectedly low on Pillar 1 (ICT Risk Management) | Management body has not formally approved the ICT risk management framework | Ensure the management body signs off on the framework, digital resilience strategy, and ICT risk tolerance level per Article 5; document board meeting minutes |
| Incident classification tool returns "major" for minor service interruptions | Threshold parameters set too conservatively or default values used | Review classification criteria against actual RTS thresholds; adjust `--clients-affected`, `--duration-hours`, and `--economic-impact` inputs to match your entity's context |
| Third-party register incomplete despite significant outsourcing | ICT service arrangements not systematically tracked or sub-contractor chains undocumented | Inventory all contractual ICT arrangements; use the register template from `references/dora-third-party-management.md`; include sub-processing chains and data processing locations |
| Resilience testing program scored as non-compliant | Only basic vulnerability scanning performed; no scenario-based or penetration testing | Design a comprehensive testing program per Article 25 covering all 12 test types; schedule annual penetration testing and scenario-based exercises; plan for TLPT if designated by competent authority |
| Pillar 5 (Information Sharing) shows zero compliance | Organization has not joined any cyber threat intelligence sharing arrangement | Evaluate participation in an ISAC (Information Sharing and Analysis Center) relevant to your financial sub-sector; notify competent authority of participation per Article 45 |
| Exit strategies missing for critical ICT third-party providers | Contracts lack termination, transition, and data recovery provisions | Update all contracts for critical functions to include comprehensive exit strategies per Article 28(8); test transition plans and document alternative provider options |
| Proportionality assessment unclear | Organization unsure whether simplified framework applies | Assess entity size, risk profile, and systemic importance per DORA proportionality principle; small and non-interconnected firms may qualify for simplified requirements |

---

## Success Criteria

- **Overall readiness score of 75+ across all 5 pillars** -- indicating the organization can demonstrate compliance with core DORA requirements to competent authorities
- **ICT risk management framework formally approved by the management body** -- with documented digital operational resilience strategy, risk tolerance levels, and annual review cycle
- **Incident classification and reporting procedures operational** -- with capability to submit initial notification within 4 hours of major incident classification and intermediate report within 72 hours
- **Complete ICT third-party register maintained** -- covering all contractual arrangements, distinguishing critical/important functions, with entity identification, service details, and sub-contractor chains
- **Resilience testing program covers all 12 required test types** -- with annual penetration testing, scenario-based exercises, and TLPT preparation (if applicable) per Articles 24-27
- **Exit strategies documented and tested for all critical ICT providers** -- with comprehensive transition arrangements, alternative provider identification, and data recovery procedures
- **Annual ICT security awareness training delivered to all staff** -- with records maintained and specialized training for ICT and security personnel per Article 13
