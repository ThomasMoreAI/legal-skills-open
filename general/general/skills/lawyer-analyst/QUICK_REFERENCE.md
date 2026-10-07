# Lawyer Analyst - Quick Reference

## TL;DR

Analyze through legal lenses: contract obligations and risks, intellectual property protection, privacy/data compliance (GDPR, CCPA), regulatory requirements, liability exposure, and terms of service. Use IRAC reasoning and identify legal risks before they become problems.

**IMPORTANT DISCLAIMER**: This provides legal information and frameworks, not legal advice. Always consult licensed attorneys for actual legal matters.

## When to Use

**Perfect For:**

- Contract review and negotiation
- Privacy policy and terms of service drafting
- Regulatory compliance assessment (GDPR, CCPA, HIPAA)
- Intellectual property strategy (patents, copyright, trademarks)
- Open source license evaluation
- Data protection and security requirements
- Employment agreements and HR policies
- Risk assessment and liability analysis
- Content moderation and platform governance

**Skip If:**

- No legal or regulatory dimensions
- Pure technical or scientific analysis
- Focused on psychology or user experience

## Core Frameworks

### IRAC Legal Reasoning

Structure legal analysis:

1. **Issue**: What's the legal question?
2. **Rule**: What law, statute, or precedent applies?
3. **Application**: How does the rule apply to these facts?
4. **Conclusion**: What's the legal outcome?

Example:

- **Issue**: Is our AI training on copyrighted works fair use?
- **Rule**: Fair use considers: purpose, nature, amount, market effect
- **Application**: Transformative use for training, not substituting original
- **Conclusion**: Likely fair use but litigation risk remains

### GDPR Core Principles

Eight principles for data protection:

1. **Lawfulness, fairness, transparency** - Clear legal basis and notice
2. **Purpose limitation** - Use only for stated purposes
3. **Data minimization** - Collect only what's necessary
4. **Accuracy** - Keep data correct and current
5. **Storage limitation** - Don't keep longer than needed
6. **Integrity and confidentiality** - Secure data appropriately
7. **Accountability** - Demonstrate compliance

**Individual Rights**: Access, rectification, erasure, portability, objection

### Intellectual Property Types

Four main categories:

- **Patents**: Inventions, processes (20 years, must be novel, non-obvious, useful)
- **Copyrights**: Creative works, software (life + 70 years, automatic upon creation)
- **Trademarks**: Brands, logos (renewable, must be distinctive and used in commerce)
- **Trade Secrets**: Confidential business info (no expiration if protected)

### Contract Essentials

Valid contract requires:

1. **Offer** - Clear proposal
2. **Acceptance** - Agreement to terms
3. **Consideration** - Value exchanged (money, services, promises)
4. **Capacity** - Parties legally able to contract
5. **Legality** - Purpose must be legal

## Quick Analysis Steps

### Step 1: Identify Legal Domains (3 min)

- What legal areas are implicated? (contract, IP, privacy, regulatory, tort)
- What jurisdictions apply? (US federal, state, EU, international)
- What industry regulations? (healthcare, finance, telecom)
- Who are the parties and their relationships?

### Step 2: Contract Risk Spotting (8 min)

If contracts are involved:

- What are the core obligations? (deliverables, timelines, payments)
- What are liability limitations and caps?
- What are indemnification requirements?
- What are termination conditions?
- What's the dispute resolution process?
- Are terms one-sided or unusual?
- What's the governing law and jurisdiction?

### Step 3: Privacy and Data Compliance (10 min)

If data is collected/processed:

- What data is collected? (personal, sensitive, children's)
- What's the legal basis? (consent, contract, legitimate interest)
- Is data minimized to what's necessary?
- Are individual rights supported? (access, deletion, portability)
- Are there adequate security measures?
- Are cross-border transfers lawful?
- Is there a breach notification process?

### Step 4: IP Analysis (8 min)

- What IP is created or used?
- Who owns it? (employer, contractor, joint)
- Are there third-party IP rights to respect?
- What open source is used? (license compatibility)
- Are there patent risks? (freedom to operate)
- How is IP protected? (registration, confidentiality)
- Are there licensing obligations?

### Step 5: Regulatory Compliance (7 min)

- What regulations apply? (GDPR, CCPA, HIPAA, SOX, PCI-DSS, industry-specific)
- What are key requirements for each?
- Are there certifications needed? (SOC 2, ISO 27001)
- What documentation is required?
- What are penalties for non-compliance?
- Are there gaps in current practices?

### Step 6: Liability and Risk Assessment (4 min)

- What are potential legal claims? (breach of contract, negligence, infringement)
- What's the likelihood and severity?
- What insurance coverage exists?
- How can liability be limited? (disclaimers, indemnification, LLC structure)
- What's the worst-case scenario?
- Are there risk mitigation strategies?

## Key Regulations

### Data Protection

- **GDPR** (EU): Comprehensive data protection, extraterritorial reach, fines up to €20M or 4% revenue
- **CCPA/CPRA** (California): Consumer privacy rights, opt-out, private right of action for breaches
- **HIPAA** (US Healthcare): Protected health information security and privacy
- **COPPA** (US Children): Special protections for children under 13

### Industry-Specific

- **PCI-DSS**: Payment card data security standards
- **SOX**: Financial reporting and internal controls (US public companies)
- **FERPA**: Student education records (US)
- **GLBA**: Financial institution privacy (US)
- **FTC Act**: Prohibits unfair/deceptive practices (US)

### Intellectual Property

- **DMCA**: Copyright safe harbor, takedown notices (US)
- **Section 230**: Platform immunity for user content (US)
- **Copyright Term Extension Act**: Life + 70 years (US)
- **Patent laws**: Vary by jurisdiction, generally 20 years from filing

## Common Contract Clauses

### Boilerplate (Important!)

- **Force majeure**: Excuse for non-performance due to unforeseeable events
- **Entire agreement**: This document supersedes prior agreements
- **Severability**: Invalid provisions don't void entire contract
- **Assignment**: Can rights/obligations be transferred?
- **Notice**: How parties communicate formally
- **Waiver**: Failing to enforce once doesn't waive future enforcement

### Risk Allocation

- **Limitation of liability**: Caps on damages (often contractual damages only)
- **Indemnification**: One party covers other's losses from specified events
- **Warranty disclaimers**: "AS IS" disclaims implied warranties
- **Insurance requirements**: Required coverage amounts

## Resources

### Quick Legal References

- **Justia**: Free case law and statutes
- **Google Scholar**: Legal documents search
- **Creative Commons**: Open licensing tools
- **IAPP**: Privacy professional resources

### Templates and Guides

- **Y Combinator SAFE**: Simple investment agreements
- **Cooley GO**: Startup legal documents
- **Creative Commons Chooser**: Select appropriate license
- **GDPR.eu**: GDPR compliance guides

### Regulatory Guidance

- **FTC.gov**: Privacy and consumer protection
- **ICO (UK)**: Data protection authority guidance
- **NIST**: Cybersecurity and privacy frameworks
- **OWASP**: Application security guidance with legal implications

## Red Flags

**Contract Red Flags:**

- Unlimited liability or indemnification
- One-sided termination rights
- Auto-renewal without notice
- Intellectual property assignment of all future work
- Broad confidentiality covering illegal activity
- Waiver of right to jury trial without consideration
- Class action waivers (may be unenforceable in some jurisdictions)

**Privacy/Data Red Flags:**

- Collecting more data than necessary
- No legal basis for processing
- Sharing data with third parties without consent
- No encryption for sensitive data
- No breach notification process
- Processing children's data without parental consent
- Cross-border transfers without safeguards

**IP Red Flags:**

- Unclear IP ownership in contracts
- Mixing incompatible open source licenses (GPL + proprietary)
- Using trademarks without permission
- Copying substantial portions of copyrighted works
- No IP assignment from contractors/employees
- No patent searches before product launch

## Integration Tips

Combine with other skills:

- **Cybersecurity**: Legal requirements for data security
- **Engineer**: Implementation of privacy/security controls
- **Ethicist**: Ethical vs. legal obligations (law is minimum)
- **Systems Thinker**: Regulatory compliance as system property
- **Economist**: Cost-benefit of legal risk mitigation

## Success Metrics

You've done this well when:

- Legal risks are identified early
- Contracts are reviewed for key terms and risks
- Privacy compliance is assessed (GDPR, CCPA)
- IP ownership and licensing are clear
- Regulatory requirements are mapped to practices
- Liability is appropriately limited
- Terms of service protect business interests
- Legal analysis is documented for future reference
- Attorneys are consulted for important matters
- Legal obligations are integrated into system design

## Important Reminder

**This is legal information, not legal advice.** For actual legal matters:

- Consult licensed attorneys in relevant jurisdictions
- Laws change frequently - verify current law
- Facts matter enormously - small differences change outcomes
- This analysis does not create attorney-client relationship
- When in doubt, get professional legal counsel
