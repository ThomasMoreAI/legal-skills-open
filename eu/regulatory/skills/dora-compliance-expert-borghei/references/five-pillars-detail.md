# DORA Five Pillars — Article-by-Article Detail

Per-pillar requirements with the governing DORA articles, incident classification and reporting deadlines, testing obligations (including TLPT), third-party contractual provisions, and information-sharing rules. Read this when assessing a specific pillar or mapping a requirement to its article.

---

## Pillar 1: ICT Risk Management (Chapter II, Articles 5–16)

The cornerstone of DORA. Financial entities must establish a comprehensive ICT risk management framework.

### Governance and Organization (Article 5)

The **management body** bears ultimate responsibility for ICT risk management:

- Define, approve, oversee, and be responsible for the implementation of the ICT risk management framework
- Define appropriate risk tolerance level for ICT risk
- Approve the digital operational resilience strategy
- Allocate adequate budget for ICT risk management
- Approve and review the ICT business continuity policy and ICT response and recovery plans
- Be informed at least once a year on findings of ICT risk reviews

**Organizational requirements:**
- Designate an ICT risk management function (second line of defense)
- Ensure adequate separation of ICT risk management, control, and internal audit functions
- Establish clear roles and responsibilities for all ICT-related functions
- Implement reporting lines ensuring the management body receives timely information

### ICT Risk Management Framework (Article 6)

Entities must establish, maintain, and implement a sound, comprehensive, and well-documented ICT risk management framework that:

- Ensures a high level of digital operational resilience
- Is documented and reviewed at least annually (or after major ICT incidents)
- Includes a digital operational resilience strategy
- Defines how the framework supports the entity's business strategy
- Sets clear information security objectives
- Defines ICT risk tolerance levels
- Commits to a continuous improvement process

**Digital Operational Resilience Strategy must include:**
- Methods for addressing ICT risk
- Explanation of how the ICT risk management framework supports the business strategy
- ICT risk tolerance level
- Key information security objectives
- Overview of ICT reference architecture and changes needed
- Mechanisms for detecting ICT anomalies
- ICT third-party risk strategy
- Digital operational resilience testing approach
- Communication strategy for incident disclosure

### ICT Systems, Protocols, and Tools (Article 7)

Requirements for ICT systems and infrastructure:
- Use and maintain updated ICT systems, protocols, and tools that are adequate to support critical operations
- Monitor effectiveness of ICT systems
- Identify all sources of ICT risk (including environmental risks and physical threats)
- Ensure appropriate network security management
- Implement mechanisms for detecting anomalous activities

### Identification (Article 8)

- Identify, classify, and adequately document all ICT-supported business functions, information assets, and ICT assets
- Identify all sources of ICT risk, particularly cyber threats
- Map the interconnections and interdependencies with ICT third-party providers
- Perform ICT risk assessments at least annually (and after major changes)
- Identify assets and systems critical to business operations

### Protection and Prevention (Article 9)

- Implement ICT security policies, procedures, protocols, and tools
- Continuously monitor and control the security and functioning of ICT systems
- Design network connection resilience mechanisms
- Deploy strong authentication mechanisms (MFA, Article 9(4))
- Implement ICT change management policies
- Apply software patching policies
- Implement data and system access policies based on least privilege

### Detection (Article 10)

- Put in place mechanisms to promptly detect anomalous activities
- Detect network performance issues and ICT-related incidents
- Deploy multiple layers of controls (including automated alerting)
- Implement detection mechanisms that enable a fast response
- Allocate sufficient resources for monitoring trading activities

### Response and Recovery (Article 11)

- Implement a comprehensive ICT business continuity policy
- Develop ICT response and recovery plans
- Activate response plans upon identification of ICT incidents
- Estimate preliminary impacts, damages, and losses
- Set communication and crisis management actions
- Execute ICT response and recovery procedures as appropriate

Specific requirements:
- Record all ICT-related incidents and significant cyber threats
- Activate containment measures and restoration of operations
- Implement backup and restoration policies and procedures
- When restoring data from backups, maintain the integrity and confidentiality of data

### Backup and Restoration (Article 12)

- Establish backup policies specifying scope, frequency, and retention
- Restore backup data on separate ICT systems (not directly connected to source)
- Regularly test backup procedures and restoration capabilities
- When restoring data, ensure integrity checks are performed
- Maintain redundant ICT capacities equipped with sufficient resources

### Learning and Evolving (Article 13)

- Gather information on vulnerabilities, cyber threats, and ICT-related incidents
- Review ICT-related incidents after recovery (post-incident reviews)
- Implement findings of post-incident reviews and digital operational resilience testing
- Monitor effectiveness of the ICT risk management framework
- Deliver mandatory annual ICT security awareness training for all staff
- Develop ICT security awareness programs for non-ICT staff

### Communication (Article 14)

- Develop crisis communication plans for internal and external stakeholders
- Designate at least one spokesperson to communicate externally during incidents
- Define communication policies for responsible disclosure of ICT-related incidents
- Inform relevant clients and the public when appropriate

---

## Pillar 2: ICT-Related Incident Management (Chapter III, Articles 17–23)

### Incident Management Process (Article 17)

Financial entities must:
- Define, establish, and implement an ICT-related incident management process
- Put in place early warning indicators to trigger detection
- Establish procedures to identify, track, log, categorize, and classify ICT-related incidents
- Assign roles and responsibilities for different incident types/scenarios
- Define plans for communication to staff, external stakeholders, media, and competent authorities

### Classification of ICT-Related Incidents (Article 18)

Entities must classify incidents based on these criteria:

| Criterion | Description |
|-----------|------------|
| **Number of clients/counterparts affected** | Scale of impact on external parties |
| **Duration** | Length of the incident |
| **Geographic spread** | Jurisdictions and Member States affected |
| **Data losses** | Availability, authenticity, integrity, or confidentiality of data |
| **Criticality of services affected** | Impact on critical or important functions |
| **Economic impact** | Direct and indirect financial costs |

**Major incident** determination: An incident is classified as major if it meets the thresholds defined in the RTS on incident classification.

### Reporting Obligations (Article 19)

| Stage | Deadline | Content |
|-------|----------|---------|
| **Initial notification** | Within **4 hours** of classifying as major (or 24 hours from detection) | Basic facts, initial classification, estimated impact |
| **Intermediate report** | Within **72 hours** of initial notification | Updated information, severity, root cause assessment, recovery status |
| **Final report** | Within **1 month** of intermediate report | Root cause analysis, complete impact assessment, mitigation measures, lessons learned |

**Additional requirements:**
- Entities must inform their clients without undue delay about major ICT-related incidents that affect their financial interests
- Entities must report to the competent authority using specified templates
- Competent authorities may request additional information at any time

### Voluntary Reporting (Article 19(2))

Entities may voluntarily report:
- Significant cyber threats (even if they have not resulted in an incident)
- Near-misses that could have caused a major incident

### Centralized Reporting (Article 20)

The ESAs develop common templates and procedures for incident reporting to reduce burden and ensure consistency.

---

## Pillar 3: Digital Operational Resilience Testing (Chapter IV, Articles 24–27)

### General Requirements (Article 24)

All financial entities must establish, maintain, and review a digital operational resilience testing program as an integral part of their ICT risk management framework.

### Basic Testing (Article 25)

All entities must perform, at a minimum:

| Test Type | Frequency | Description |
|-----------|-----------|------------|
| **Vulnerability assessments and scans** | Regular (at least annually) | Automated and manual vulnerability identification |
| **Open-source analyses** | Regular | Assessment of open-source software risks |
| **Network security assessments** | Annual minimum | Network architecture, configuration, traffic analysis |
| **Gap analyses** | Annual minimum | Comparison of current controls vs requirements |
| **Physical security reviews** | Periodic | Data center, office, and facility security |
| **Questionnaires and scanning software** | Regular | Compliance checking and configuration verification |
| **Source code reviews** | Where applicable | Security-focused code review for in-house applications |
| **Scenario-based tests** | Annual | Tabletop exercises, simulations |
| **Compatibility testing** | As needed | Testing for system updates and changes |
| **Performance testing** | Regular | Load and stress testing for critical systems |
| **End-to-end testing** | Regular | Testing of complete business process chains |
| **Penetration testing** | Annual minimum | Simulated attack testing |

### Advanced Testing — Threat-Led Penetration Testing (Article 26)

**Applicable to:** Entities identified by competent authorities based on systemic importance, ICT risk profile, and criticality of services.

**TLPT requirements:**

- Based on the TIBER-EU framework
- Covers critical or important functions mapped to services, business processes, and ICT
- Conducted at least every 3 years
- Scope is determined by the financial entity, validated by the competent authority
- Must include live production systems
- The management body must approve the scope

**TLPT methodology:**

1. **Scoping phase:** Identify critical functions and supporting ICT infrastructure
2. **Threat intelligence phase:** Gather threat intelligence specific to the entity's sector and geography
3. **Red team phase:** Execute realistic attack scenarios against production systems
4. **Closure phase:** Report findings, remediation planning
5. **Purple team phase:** Collaborative exercises between red team (attackers) and blue team (defenders)

**Key rules:**
- Conducted by external testers with appropriate qualifications and independence
- Internal testers may participate under specific conditions
- Test results must be validated by competent authority
- Remediation plans must be produced and implemented
- Summary results must be shared with the competent authority

### Purple Teaming

DORA introduces purple teaming as a key element:
- Collaborative exercise between red team and blue team
- Red team shares tactics, techniques, and procedures (TTPs) used
- Blue team reviews detection and response capabilities
- Joint identification of gaps and improvement areas
- Mandatory as part of the TLPT closure phase

---

## Pillar 4: ICT Third-Party Risk Management (Chapter V, Articles 28–44)

### General Principles (Article 28)

Financial entities must:
- Manage ICT third-party risk as an integral component of ICT risk management
- Be responsible at all times for compliance, regardless of outsourcing
- Define strategy on ICT third-party risk (part of the digital resilience strategy)
- Maintain and update a register of information relating to all contractual arrangements on ICT services

### Preliminary Assessment (Article 28(4))

Before entering into a contractual arrangement, entities must:
- Identify and assess all relevant risks (including concentration risk)
- Assess whether the arrangement covers critical or important functions
- Conduct appropriate due diligence on prospective ICT third-party providers
- Identify and assess conflicts of interest
- Verify the ICT third-party provider's ability to comply with applicable regulations

### Key Contractual Provisions (Article 30)

Contracts with ICT third-party service providers must include:

| Provision | Description |
|-----------|------------|
| **Clear service descriptions** | Complete description of all services, including SLAs |
| **Location requirements** | Where data will be processed and stored, including sub-processing |
| **Data protection provisions** | Measures ensuring availability, authenticity, integrity, and confidentiality |
| **Service level commitments** | Quantitative and qualitative performance targets |
| **Assistance obligations** | ICT provider must assist with ICT incidents affecting the entity |
| **Cooperation with authorities** | Provider must cooperate with competent authorities and resolution authorities |
| **Termination rights** | Clear termination rights, including for performance failures and regulatory changes |
| **Transition and exit provisions** | Adequate transition periods and assistance for orderly transfer of services |
| **Participation in TLPT** | ICT provider must participate in entity's threat-led penetration testing |
| **Audit rights** | Full access and audit rights, including on-site inspections of the ICT provider |
| **Unrestricted right to monitor** | Right to continuously monitor provider's performance |
| **Exit strategies** | Mandatory exit strategies for critical or important function outsourcing |

**For critical or important functions**, additional contractual requirements apply:
- More detailed service level descriptions
- Notice periods and reporting obligations for material developments
- Full access to performance and security data
- ICT provider must implement and test business continuity plans
- Provider must provide staff training on ICT security awareness

### Register of ICT Third-Party Arrangements (Article 28(3))

Entities must maintain a register containing:
- All contractual arrangements with ICT third-party providers
- Distinction between critical/important and non-critical functions
- Entity identification details (LEI, type, group structure)
- Service details (type, start date, end date, governing law, data processing locations)
- Sub-contractor chain information
- Exit strategy information

The register must be reported to competent authorities upon request.

### Exit Strategies (Article 28(8))

For critical or important functions, entities must:
- Develop exit strategies that are comprehensive, documented, and tested
- Ensure sufficient transition arrangements that avoid disruption or degradation of services
- Consider alternative solutions and transition plans
- Enable recovery of data and applications

### Oversight Framework for Critical ICT Third-Party Providers (Articles 31–44)

The ESAs designate CTPPs and assign a Lead Overseer. The oversight framework includes:

- Direct supervision powers over CTPPs
- On-site inspections of CTPPs
- Power to request information and issue recommendations
- Annual oversight plans
- CTPPs must cooperate with the Lead Overseer
- Non-compliance may result in periodic penalty payments

### Concentration Risk (Article 29)

Entities must:
- Identify and assess risks arising from concentrating ICT service arrangements on a single provider
- Assess whether planned ICT outsourcing leads to material concentration risk
- Consider the substitutability of the ICT third-party provider
- Develop multi-vendor strategies where appropriate

---

## Pillar 5: Information Sharing (Chapter VI, Article 45)

### Voluntary Cyber Threat Intelligence Sharing

Financial entities **may** exchange amongst themselves cyber threat intelligence information including:
- Indicators of compromise (IoCs)
- Tactics, techniques, and procedures (TTPs)
- Cybersecurity alerts and configuration tools
- Tools and methods for detecting cyberattacks

### Requirements for Sharing Arrangements

- Sharing must aim to enhance digital operational resilience
- Must be within trusted communities of financial entities
- Arrangements must respect business confidentiality and data protection
- Must protect personal data in accordance with GDPR
- Sharing may be enabled through information sharing and analysis centers (ISACs)

### Notification Requirements

Entities must notify competent authorities of their participation in information-sharing arrangements.
