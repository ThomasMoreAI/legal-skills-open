---
name: gdpr-expert
title: GDPR Expert
description: GDPR expert for EU privacy compliance. Deep knowledge of General Data Protection Regulation including 99 articles, 7 principles, 6 lawful bases, data subject rights, DPO requirements, DPIA, breach notification, cross-border transfers, and enforcement.
author: GRCEngClub
author_url: https://github.com/GRCEngClub/claude-grc-engineering/tree/main/plugins/frameworks/gdpr/skills/gdpr-expert
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Expert

Deep expertise in the General Data Protection Regulation (GDPR) - the European Union's comprehensive data protection law.

## Expertise Areas

### GDPR Overview

**Regulation (EU) 2016/679**: General Data Protection Regulation
**Effective Date**: May 25, 2018
**Scope**: Protection of natural persons with regard to processing of personal data and free movement of such data
**Articles**: 99 (11 chapters)
**Recitals**: 173 (interpretive guidance)

**Territorial Scope** (Article 3):

- **Establishment**: Controller/processor established in EU (regardless of where processing occurs)
- **Targeting**: Offering goods/services to EU data subjects (even if free)
- **Monitoring**: Monitoring behavior of EU data subjects
- **Applies**: Even if organization not in EU

**Material Scope**:

- Automated processing of personal data
- Non-automated processing in filing systems
- **Exemptions**: National security, law enforcement (LED applies), purely personal/household

### Key Definitions (Article 4)

**Personal Data**:

- Any information relating to identified/identifiable natural person
- Direct identifiers: Name, ID number, email
- Indirect identifiers: Location data, IP address, cookie ID, device ID
- Combination of factors: Age + ZIP code + occupation

**Special Categories of Personal Data** (Article 9 - "Sensitive Data"):

- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Biometric data (for uniquely identifying a person)
- Health data
- Sex life or sexual orientation

**Processing**:

- Any operation on personal data
- Collection, recording, storage, retrieval, use, disclosure, erasure, destruction
- Automated or manual

**Controller**:

- Determines purposes and means of processing
- Makes decisions about why and how to process
- Primary responsibility for compliance

**Processor**:

- Processes on behalf of controller
- Acts on controller instructions
- Limited independent decision-making

**Joint Controllers**:

- Two or more controllers jointly determine purposes and means
- Must arrange responsibilities via agreement
- Each liable for entire processing

**Data Subject**:

- Identified or identifiable natural person
- Individual whose data is processed
- Rights holder under GDPR

**Supervisory Authority**:

- Independent public authority (Data Protection Authority/DPA)
- Each EU Member State has one or more
- Enforces GDPR in jurisdiction

**Lead Supervisory Authority** (Article 56):

- For cross-border processing
- Main establishment's DPA
- One-stop-shop mechanism

### 7 Principles of Data Processing (Article 5)

#### 1. Lawfulness, Fairness, and Transparency

**Lawfulness**: Must have lawful basis (Article 6)
**Fairness**: No deceptive, misleading, or detrimental processing
**Transparency**: Clear, plain language communication to data subjects

**Implementation**:

- Privacy notices at collection
- Layered notices (short + full)
- Just-in-time notices
- Clear language (no legalese)
- Accessible information

#### 2. Purpose Limitation

**Requirements**:

- Specified purposes (documented, clear)
- Explicit purposes (communicated to data subjects)
- Legitimate purposes (lawful, ethical)
- No processing for incompatible purposes

**Compatible Processing**:

- Same or closely related purpose
- Consider: Link between purposes, context, nature of data, consequences, safeguards

**Exceptions**:

- Archiving in public interest
- Scientific/historical research
- Statistical purposes

#### 3. Data Minimization

**"Adequate, relevant, and limited to what is necessary"**

**Implementation**:

- Collect only what you need
- Justify each data element
- Regular review and purge
- Limit access (need-to-know)
- Pseudonymization/anonymization where possible

**Common Violations**:

- "Nice to have" data collection
- Speculative future use
- Excessive profiling data

#### 4. Accuracy

**Requirements**:

- Personal data must be accurate
- Kept up to date where necessary
- Inaccurate data erased or rectified

**Implementation**:

- Verification at collection
- Regular reviews and updates
- Easy rectification process
- Notify recipients of changes
- Quality control procedures

#### 5. Storage Limitation

**"Kept no longer than necessary for the purposes"**

**Implementation**:

- Retention schedules (per purpose)
- Regular deletion reviews
- Automated deletion where possible
- Document retention rationale
- Legal hold procedures

**Exceptions** (can retain longer):

- Archiving in public interest
- Scientific/historical research
- Statistical purposes
- With appropriate safeguards

#### 6. Integrity and Confidentiality (Security)

**"Appropriate security... including protection against unauthorized/unlawful processing and accidental loss, destruction or damage"**

**Implementation**: See Article 32 (Security of Processing)

#### 7. Accountability

**"Controller shall be responsible for and able to demonstrate compliance"**

**Demonstration Requirements**:

- Documentation (policies, procedures, records)
- Data Protection Impact Assessments (DPIAs)
- Privacy by Design and Default
- Data Processing Agreements (DPAs)
- Records of Processing Activities
- Training and awareness programs
- Regular audits and reviews
- Incident response and breach records

### 6 Lawful Bases for Processing (Article 6)

**Must identify ONE for each processing purpose**

#### 1. Consent (Article 6(1)(a))

**Requirements**:

- **Freely given**: No coercion, imbalance of power consideration
- **Specific**: Separate consent for separate purposes
- **Informed**: Identity, purposes, data types, rights, withdrawal
- **Unambiguous**: Clear affirmative action (no pre-ticked boxes, silence, inactivity)

**Additional for Consent**:

- Easy to withdraw (as easy as to give)
- Withdrawal does not affect lawfulness of prior processing
- Burden of proof on controller
- Record of consent (who, when, what, how)

**When Problematic**:

- Employment context (power imbalance)
- Public authorities (no free choice)
- Service bundling (cannot refuse)

**Children's Consent** (Article 8):

- Under 16: Parental consent required (Member States can lower to 13)
- Controller must make reasonable efforts to verify

#### 2. Contract (Article 6(1)(b))

**Two scenarios**:

- Processing necessary to **perform a contract** with data subject
- Processing necessary to **enter into contract** (pre-contractual steps)

**"Necessary"**:

- Objectively essential to contract
- Not just "helpful" or "customary"
- Direct relationship to contract performance

**Examples**:

- Shipping address for product delivery
- Credit card for payment processing
- Account credentials for service access

**Not Sufficient**:

- Marketing to customers (use consent or legitimate interests)
- Analytics not integral to service (use legitimate interests)

#### 3. Legal Obligation (Article 6(1)(c))

**Requirements**:

- Processing required by **EU law** or **Member State law**
- Obligation on the controller
- Must identify specific legal provision

**Examples**:

- Tax records (legal retention requirements)
- Employment records (labor law)
- AML/KYC checks (financial regulations)
- Health and safety reporting

**Not Sufficient**:

- Contractual obligations (use contract basis)
- Best practices or industry standards
- Non-EU legal obligations

#### 4. Vital Interests (Article 6(1)(d))

**"Necessary to protect the vital interests of the data subject or another"**

**Scope**:

- Life or death situations
- Serious health threats
- Last resort when other bases not available

**Examples**:

- Emergency medical treatment (unconscious patient)
- Humanitarian crises
- Pandemic response (in some cases)

**Rarely Appropriate**: Most organizations won't use this basis

#### 5. Public Task (Article 6(1)(e))

**"Necessary for task carried out in the public interest or in exercise of official authority"**

**Scope**:

- Public authorities
- Private entities exercising official authority
- Task must have basis in EU/Member State law

**Examples**:

- Government agencies
- Regulators
- Educational institutions (public tasks)

**Not Available**: Commercial organizations (use legitimate interests)

#### 6. Legitimate Interests (Article 6(1)(f))

**"Necessary for purposes of legitimate interests pursued by controller or third party, except where overridden by interests, rights and freedoms of data subject"**

**Three-Part Test**:

1. **Purpose Test**: Is interest legitimate?
2. **Necessity Test**: Is processing necessary?
3. **Balancing Test**: Do data subject's interests override?

**Legitimate Interest Assessment (LIA)** Required:

- Identify legitimate interest
- Necessity assessment (no less intrusive means)
- Balancing test (impact on data subjects)
- Document LIA

**Examples of Legitimate Interests**:

- Fraud prevention
- Network and information security
- Direct marketing (subject to right to object)
- Intra-group transfers
- Employee monitoring (limited)
- Analytics for service improvement

**Cannot Use**:

- Public authorities (for official tasks)
- When data subject's interests clearly override

**Right to Object** (Article 21):

- Data subjects can object to legitimate interests processing
- Controller must demonstrate compelling legitimate grounds to continue

### Special Category Data (Article 9)

**General Prohibition**: Processing of special categories prohibited

**Exceptions** (Must meet Article 6 basis PLUS Article 9 exception):

1. **Explicit consent** (9(2)(a))
2. **Employment, social security, social protection law** (9(2)(b))
3. **Vital interests** (cannot obtain consent) (9(2)(c))
4. **Not-for-profit body** (political, philosophical, religious, trade union) (9(2)(d))
5. **Made public by data subject** (9(2)(e))
6. **Legal claims** (9(2)(f))
7. **Substantial public interest** (with basis in law) (9(2)(g))
8. **Health/social care** (professional secrecy) (9(2)(h))
9. **Public health** (9(2)(i))
10. **Archiving, research, statistics** (safeguards) (9(2)(j))

**Criminal Conviction Data** (Article 10):

- Only under control of official authority, OR
- Authorized by EU/Member State law (safeguards)

### Data Subject Rights (Articles 12-22)

Covered in detail in `rights-check.md` command. Summary:

1. **Right to be Informed** (Articles 13-14)
2. **Right of Access** (Article 15)
3. **Right to Rectification** (Article 16)
4. **Right to Erasure** (Article 17)
5. **Right to Restriction** (Article 18)
6. **Right to Data Portability** (Article 20)
7. **Right to Object** (Article 21)
8. **Rights re: Automated Decision-Making** (Article 22)

**General Requirements** (Article 12):

- Free of charge (generally)
- Within 1 month (+2 months if complex)
- Concise, transparent, intelligible, plain language

### Security of Processing (Article 32)

**"Appropriate technical and organizational measures"**

**State of the Art**: Current best practices
**Cost**: Balanced against risk and impact
**Risk**: Likelihood and severity of harm

### Technical Measures

**Pseudonymization**:

- Separate identity from data
- Cannot attribute to individual without additional information
- Additional information kept separately with security

**Encryption**:

- At rest (storage encryption, database encryption, file encryption)
- In transit (TLS 1.2+, VPN, encrypted email)
- End-to-end (messaging, file sharing)

**Access Controls**:

- Authentication (passwords, MFA, biometrics)
- Authorization (RBAC, least privilege)
- Identity and Access Management (IAM)

**Network Security**:

- Firewalls and segmentation
- Intrusion detection/prevention
- DDoS protection
- Secure configurations

**Monitoring and Logging**:

- Security information and event management (SIEM)
- Audit logs (access, changes, deletions)
- Anomaly detection
- Log retention and protection

**Resilience**:

- Backup and recovery
- Redundancy and failover
- Disaster recovery
- Business continuity

**Testing**:

- Vulnerability scanning
- Penetration testing
- Security assessments
- Red team exercises

### Organizational Measures

**Policies and Procedures**:

- Information security policy
- Data protection policy
- Acceptable use policy
- Incident response plan
- Business continuity plan

**Staff Management**:

- Background checks (proportionate)
- Confidentiality agreements
- Security awareness training
- Role-based training
- Termination procedures

**Vendor Management**:

- Due diligence assessments
- Data Processing Agreements (Article 28)
- Ongoing monitoring
- Audit rights

**Governance**:

- Security roles and responsibilities
- Management oversight
- Compliance monitoring
- Regular reviews

**Physical Security**:

- Facility access controls
- Visitor management
- Equipment security
- Secure disposal

### Privacy by Design and Default (Article 25)

**Privacy by Design** (Article 25(1)):

- Implement appropriate technical and organizational measures
- At the time of determining means of processing
- At the time of processing itself
- Designed to implement principles (minimization, etc.)
- Integrate safeguards into processing

**7 Foundational Principles** (Cavoukian):

1. Proactive not reactive
2. Privacy as default setting
3. Privacy embedded into design
4. Full functionality (positive-sum, not zero-sum)
5. End-to-end security
6. Visibility and transparency
7. Respect for user privacy

**Privacy by Default** (Article 25(2)):

- Only process data necessary for each purpose
- By default (without user action)
- Applies to: Amount collected, extent of processing, retention period, accessibility

**Examples**:

- Collect only necessary data
- Default privacy settings (most protective)
- Anonymization/pseudonymization
- Short retention periods
- Limited access

### Data Protection Officer (DPO) (Articles 37-39)

#### When DPO Required (Article 37)

**Mandatory DPO**:

1. **Public authority** (except courts acting in judicial capacity)
2. **Core activities require regular and systematic monitoring** of data subjects on large scale
3. **Core activities consist of large-scale processing** of special categories (Article 9) or criminal data (Article 10)

**"Core Activities"**:

- Essential to organization's operations
- Not ancillary functions

**"Large Scale"**:

- WP29 factors: Number of subjects, volume of data, duration, geographic extent
- No specific threshold
- Examples: Hospital, insurance company, search engine, telecom

**"Regular and Systematic Monitoring"**:

- Ongoing or recurring
- Planned or organized
- Examples: Online advertising, profiling, location tracking, CCTV

**Voluntary DPO**:

- Any organization can appoint
- Once appointed, same requirements apply

#### DPO Qualities and Position (Article 37)

**Professional Qualities**:

- Expert knowledge of data protection law and practices
- Understanding of processing operations
- Ability to fulfill tasks

**Position Requirements**:

- Designated on basis of professional qualities and expertise
- Adequate resources (time, budget, staff)
- Access to personal data and processing operations
- Report directly to highest management level
- Independent (no instruction on how to perform tasks)
- No conflict of interest (cannot have position determining purposes/means)

**Protection**:

- Cannot be dismissed or penalized for DPO tasks
- Minimum 2-year term recommended

#### DPO Tasks (Article 39)

1. **Inform and advise** controller, processor, employees
2. **Monitor compliance** with GDPR and policies
3. **Advise on DPIAs** and monitor performance
4. **Cooperate** with supervisory authority
5. **Act as contact point** for authority and data subjects

**Independence**:

- No instructions on performing tasks
- Controller must not interfere
- DPO decides how to perform tasks

### Records of Processing Activities (Article 30)

**Controller Records Must Include**:

- Name and contact of controller, joint controllers, representative, DPO
- Purposes of processing
- Description of categories of data subjects and data
- Categories of recipients (including third countries)
- Transfers to third countries (documentation of safeguards)
- Retention periods (or criteria)
- Description of technical and organizational security measures (general)

**Processor Records Must Include**:

- Name and contact of processor, controllers, representative, DPO
- Categories of processing on behalf of each controller
- Transfers to third countries (documentation)
- Security measures description (general)

**Exemptions** (Article 30(5)):

- Organization with **<250 employees**, UNLESS:
  - Processing likely to result in risk to rights and freedoms
  - Not occasional processing
  - Special categories or criminal data

**Practical Approach**: Most organizations should maintain records

**Format**: Written, electronic form

### Data Protection Impact Assessment (Article 35)

Covered in detail in `dpia.md` command.

**When Required**:

- Processing likely to result in high risk
- Particularly: Systematic profiling, large-scale special categories, systematic public monitoring

**Content**:

- Systematic description of processing and purposes
- Assessment of necessity and proportionality
- Assessment of risks to data subjects
- Measures to address risks

**Consultation**:

- Seek advice of DPO
- Seek views of data subjects (where appropriate)
- Consult supervisory authority if high residual risk (Article 36)

### Data Processing Agreements (Article 28)

**When Required**: Controller uses processor

**Mandatory Content**:

1. **Subject matter and duration** of processing
2. **Nature and purpose** of processing
3. **Type of personal data** and categories of data subjects
4. **Obligations and rights** of controller

**Processor Obligations**:

- Process only on documented instructions
- Ensure confidentiality of persons authorized to process
- Implement Article 32 security measures
- Respect conditions for sub-processors
- Assist controller with data subject rights
- Assist controller with Articles 32-36 obligations (security, breach, DPIA, consultation)
- Delete or return data at end of services
- Make available information for demonstrating compliance
- Allow and contribute to audits/inspections

**Sub-Processors**:

- Specific or general written authorization
- If general, inform of changes, opportunity to object
- Same obligations on sub-processor (via contract)
- Processor remains liable to controller

**Liability**: Processor directly liable under GDPR (not just to controller)

### Cross-Border Data Transfers (Chapter V)

**General Principle**: Personal data can flow freely within EU/EEA

**Transfers to Third Countries**: Require safeguards (Article 44-50)

#### Transfer Mechanisms

**1. Adequacy Decision** (Article 45):

- European Commission determines third country has adequate protection
- No additional safeguards needed
- **Adequate Countries**: Andorra, Argentina, Canada (commercial orgs), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, South Korea, Switzerland, UK, Uruguay
- **US**: No general adequacy (Privacy Shield invalidated by Schrems II)

**2. Standard Contractual Clauses (SCCs)** (Article 46(2)(c)):

- EU Commission approved contract clauses
- 2021 SCCs (modernized post-Schrems II)
- Four modules: C2C, C2P, P2C, P2P
- Transfer Impact Assessment (TIA) required
- Supplementary measures if laws in third country may impinge on SCCs

**3. Binding Corporate Rules (BCRs)** (Article 46(2)(b)):

- Multinational groups
- Binding internal policies
- Approved by competent supervisory authority
- Complex, resource-intensive

**4. Certification Mechanisms** (Article 46(2)(f)):

- Approved certification + binding enforceable commitments
- Limited use to date

**5. Ad Hoc Contractual Clauses** (Article 46(3)(a)):

- Custom contracts
- Require supervisory authority approval
- Rarely used

**6. Derogations for Specific Situations** (Article 49):

- **Explicit consent** (informed of risks)
- **Performance of contract** with data subject
- **Important reasons of public interest**
- **Legal claims**
- **Vital interests**
- **Public register** (within conditions)
- **Legitimate interests** (not repetitive, limited subjects, appropriate safeguards)
- Use only when transfer mechanisms not available
- Not for regular transfers

#### Schrems II Impact

**CJEU Case C-311/18** (July 2020):

- Invalidated EU-US Privacy Shield
- SCCs remain valid BUT:
  - Must assess whether third country law ensures adequate protection
  - **Transfer Impact Assessment (TIA)** required
  - **Supplementary measures** may be needed (encryption, pseudonymization, etc.)
- Particular concern: US surveillance laws (FISA 702, EO 12333)

**Practical Impact**:

- **US transfers**: Challenging, require TIA and often supplementary measures
- **China, Russia**: High-risk jurisdictions
- Other countries: Case-by-case assessment

### Personal Data Breaches (Articles 33-34)

Covered in detail in `breach-process.md` command.

**72-Hour Rule**:

- Notify supervisory authority within 72 hours (Article 33)
- Notify data subjects if high risk (Article 34)

**Documentation** (Article 33(5)):

- Record all breaches (even if not notified)
- Facts, effects, remedial action
- Demonstrate compliance

### Supervisory Authorities (Articles 51-59)

**Independence** (Article 52):

- Act with complete independence
- Free from external influence
- Adequate resources

**Tasks** (Article 57):

- Monitor and enforce GDPR
- Promote awareness
- Advise on legislative measures
- Handle complaints
- Conduct investigations
- Authorize contractual clauses, BCRs
- Issue opinions, warnings, guidelines

**Powers** (Article 58):

1. **Investigative**: Audits, access to data/premises, obtain information
2. **Corrective**: Warnings, reprimands, orders (compliance, rectification, erasure), processing bans, fines
3. **Authorization**: Approve SCCs, BCRs, certifications

**Lead Supervisory Authority** (Article 56):

- One-stop-shop for cross-border processing
- Based on main establishment
- Coordinates with other concerned authorities

**European Data Protection Board (EDPB)** (Article 68):

- Replaces Article 29 Working Party
- Ensures consistent application
- Issues guidelines, recommendations, best practices
- Dispute resolution (consistency mechanism)

### Enforcement and Penalties (Articles 82-84)

#### Administrative Fines (Article 83)

**Up to €10 Million or 2% of global annual turnover** (whichever higher):

- Processors not meeting obligations (Article 28)
- Certification body violations
- Monitoring body violations

**Up to €20 Million or 4% of global annual turnover** (whichever higher):

- Principles violations (Article 5)
- Lawful basis violations (Article 6)
- Consent violations (Article 7)
- Special categories violations (Article 9)
- Data subject rights violations (Articles 12-22)
- Transfer violations (Articles 44-49)
- Non-compliance with supervisory authority orders

**Factors Considered** (Article 83(2)):

- Nature, gravity, duration of infringement
- Intentional or negligent
- Actions to mitigate damage
- Degree of responsibility
- Previous relevant infringements
- Degree of cooperation with authority
- Categories of data affected
- Manner authority became aware (proactive notification vs. complaint)
- Compliance with prior orders
- Adherence to approved codes of conduct or certifications
- Aggravating or mitigating factors (financial gain, vulnerable data subjects)

#### Compensation (Article 82)

**Right to Compensation**:

- Any person who suffered material or non-material damage
- Due to GDPR infringement
- Has right to receive compensation from controller or processor

**Material Damage**: Financial loss, costs
**Non-Material Damage**: Distress, anxiety, loss of control over data

**Liability**:

- Controller/processor liable for damage caused by processing
- Processor liable only if failed to comply with processor obligations or acted outside controller's instructions
- Not liable if proves not responsible for damage

**Joint and Several Liability**: For joint controllers or controller-processor chains

### Notable GDPR Enforcement Cases

**Large Fines**:

- **Amazon** (2021): €746M (Luxembourg) - Inadequate lawful basis for advertising
- **WhatsApp** (2021): €225M (Ireland) - Transparency violations
- **Google** (2019): €50M (France) - Inadequate consent for advertising
- **British Airways** (2020): £20M (UK) - Poor security leading to breach
- **Marriott** (2020): £18.4M (UK) - Insufficient due diligence (acquisition), breach

**Common Violation Themes**:

- Lack of valid lawful basis (especially consent, legitimate interests)
- Inadequate transparency and privacy notices
- Failure to implement data subject rights
- Insufficient security measures
- Cross-border transfer violations
- Failure to notify breaches
- Lack of DPIAs
- Missing or inadequate DPAs with processors

### International Variations and Related Laws

**UK GDPR**:

- Post-Brexit UK version
- Materially same as EU GDPR
- ICO (Information Commissioner's Office) enforces
- Adequacy decision from EU

**Swiss FADP** (Federal Act on Data Protection):

- Swiss data protection law
- Similar to GDPR (adequacy decision)
- Some differences (e.g., legal entities protected)

**National Implementations**:

- GDPR is directly applicable (Regulation, not Directive)
- Member States can specify certain provisions
- National laws for public sector, employment, etc.
- "Margin of discretion" in some articles

### Sector-Specific Considerations

#### Healthcare

- Health data is special category (Article 9)
- Processing for healthcare (Article 9(2)(h))
- Professional secrecy requirements
- Research provisions (Article 89)
- National health data laws

#### Employment

- Power imbalance (consent problematic)
- Legal obligation and legitimate interests primary bases
- Member State laws specify employment processing
- Employee monitoring (necessity, proportionality, transparency)
- Works council involvement (some jurisdictions)

#### Financial Services

- AML/KYC (legal obligation)
- Credit scoring (automated decisions - Article 22)
- Payment data (PSD2 interaction)
- Supervisory authority coordination (financial regulators + DPAs)

#### Marketing

- Direct marketing (right to object - Article 21(2))
- Consent for electronic marketing (ePrivacy Directive)
- Profiling for marketing (legitimate interests with right to object)
- Transparency about targeting

#### Public Sector

- Public task lawful basis (Article 6(1)(e))
- Cannot use legitimate interests for official tasks
- DPO mandatory (Article 37(1)(a))
- Often subject to additional national laws (FOI, etc.)

### Relationship with Other Regulations

**ePrivacy Directive** (2002/58/EC):

- Governs electronic communications
- Cookies and tracking (consent required)
- Marketing emails/calls/SMS (opt-in/opt-out)
- "Lex specialis" to GDPR (takes precedence in its scope)
- **ePrivacy Regulation**: Proposed replacement (pending)

**PSD2** (Payment Services Directive 2):

- Open banking data sharing
- Explicit consent for third-party access
- GDPR applies to payment data

**NIS Directive** (Network and Information Security):

- Critical infrastructure security
- Incident reporting
- Complements GDPR Article 32

**DORA** (Digital Operational Resilience Act):

- EU financial sector ICT resilience
- Overlaps with GDPR security/breach requirements

**AI Act** (Proposed):

- Regulation of artificial intelligence
- Interaction with GDPR (automated decisions, profiling)
- Additional requirements for high-risk AI

### Best Practices and Recommendations

#### Data Mapping

- Comprehensive inventory (systems, databases, files, third parties)
- Data flows (collection → storage → use → transfer → deletion)
- Categories of data and data subjects
- Lawful bases and purposes
- Retention periods
- Recipients and processors

#### Policy Framework

- Data protection policy
- Privacy notices (collection, updates)
- Data subject rights procedures
- Breach response plan
- Vendor management policy
- Retention and deletion policy
- Privacy by Design standard

#### Governance

- DPO appointment (where required or beneficial)
- Privacy steering committee
- Defined roles and responsibilities
- Regular management reporting
- Board oversight

#### Training and Awareness

- All staff: GDPR awareness, data protection principles
- Developers: Privacy by Design
- Customer-facing: Data subject rights
- IT/Security: Security measures, breach response
- Leadership: Accountability, risk

#### Ongoing Compliance

- Regular GDPR audits (internal, external)
- Privacy impact assessments (new projects)
- Vendor assessments and DPA reviews
- Monitoring of supervisory authority guidance
- Incident and breach tracking
- Metrics (rights requests, training completion, audit findings)
- Continuous improvement

#### Documentation (Demonstrating Accountability)

- Records of processing activities (Article 30)
- Lawful basis documentation
- Legitimate interest assessments (LIAs)
- DPIAs for high-risk processing
- Data processing agreements (DPAs)
- Records of consent
- Data subject rights request logs
- Breach register (Article 33(5))
- Policies and procedures
- Training records
- Audit reports

### Common Compliance Challenges

1. **Lack of data visibility**: Don't know what data is held or where
2. **Weak lawful bases**: Relying on invalid consent or vague legitimate interests
3. **Inadequate transparency**: Privacy notices unclear or incomplete
4. **Complex data subject rights**: Cannot locate or provide data efficiently
5. **Vendor ecosystem**: Numerous processors, inconsistent DPAs
6. **Cross-border transfers**: US and other third countries
7. **Legacy systems**: Old technology, poor data controls
8. **Shadow IT**: Unsanctioned tools and data storage
9. **Resource constraints**: Small privacy/compliance teams
10. **Organizational silos**: Legal, IT, business not aligned

### Emerging Topics

**Cookies and Tracking**:

- Cookie consent banners (ePrivacy + GDPR)
- "Cookie walls" (recent guidance: generally not valid consent)
- Legitimate interests for analytics (limited acceptance)
- Tracking technologies (fingerprinting, pixels, etc.)

**Artificial Intelligence and Profiling**:

- Automated decision-making (Article 22)
- Transparency and explainability
- Bias and fairness
- Data minimization challenges
- Proposed AI Act interaction

**Children's Data**:

- Age verification challenges
- Parental consent requirements
- Age-appropriate design (UK Age Appropriate Design Code)
- Online services and social media

**Biometric Data**:

- Special category (Article 9)
- Facial recognition (high-risk DPIA required)
- Regulatory scrutiny and bans (some public uses)
- Workplace biometrics (proportionality)

**Dark Patterns**:

- Manipulative UX design
- EDPB Guidelines 03/2022 on deceptive design patterns
- Cookie banners, consent flows, account deletion

**International Data Transfers Post-Schrems II**:

- US transfers (supplementary measures, new EU-US framework discussions)
- Transfer Impact Assessments (TIAs)
- Encryption and pseudonymization as safeguards
- Data localization pressures

## Capabilities

- GDPR compliance assessments and gap analysis
- Lawful basis determination and documentation
- Legitimate interest assessments (LIAs)
- Privacy notice and transparency review
- Data subject rights implementation (all 8 rights)
- Data Protection Impact Assessments (DPIAs)
- DPO requirement evaluation and role definition
- Records of Processing Activities (Article 30) creation
- Data Processing Agreement (DPA) drafting and review
- Security measures assessment (Article 32)
- Privacy by Design and Default integration
- Breach notification procedures (72-hour rule)
- Cross-border transfer mechanism selection and implementation
- Transfer Impact Assessments (TIAs)
- Vendor and processor risk assessments
- Cookie consent and tracking compliance
- Special category data processing authorization
- Automated decision-making (Article 22) compliance
- Supervisory authority interactions and complaint responses
- GDPR training program development
- Policy and procedure creation
- Consent management systems
- Data mapping and inventory
- Retention and deletion schedules
- Incident response planning
- GDPR audit preparation
