---
name: legal-compliance-agent
title: Legal Compliance Agent
description: Generate legally compliant privacy policies, terms of service, HIPAA documentation, and compliance pages for healthcare SaaS platforms. Ensures Google Play/App Store approval and GDPR/HIPAA compliance.
author: diegosouzapw
author_url: https://github.com/diegosouzapw/awesome-omni-skill/tree/main/skills/testing-security/legal-compliance-agent
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Legal Compliance Agent

## Purpose

This skill generates comprehensive, legally compliant documentation for healthcare SaaS platforms, specifically:

- **Privacy Policies** (GDPR-compliant, Google API compliant)
- **Terms of Service** (comprehensive legal protection)
- **HIPAA Compliance Pages** (healthcare-specific regulations)
- **Cookie Policies** (EU/UK GDPR requirements)
- **Business Associate Agreements (BAA)** (HIPAA requirement)

All documentation is written to meet Google Play Store, Apple App Store, and Google API Services User Data Policy requirements.

---

## Compliance Standards

### 1. GDPR Compliance (EU/UK)

**Required Elements:**
- Legal basis for data processing (consent, legitimate interest)
- Data subject rights (access, deletion, portability, rectification)
- Data retention periods (specific durations)
- International data transfers (adequacy decisions, SCCs)
- Contact information (DPO or privacy officer)
- Right to lodge complaint with supervisory authority
- Automated decision-making disclosure

**User Rights Under GDPR:**
- Right to access personal data
- Right to rectification (correction)
- Right to erasure ("right to be forgotten")
- Right to restrict processing
- Right to data portability
- Right to object to processing
- Rights related to automated decision-making

### 2. HIPAA Compliance (US Healthcare)

**Required Elements:**
- PHI (Protected Health Information) definition
- Security measures (encryption, access controls)
- Breach notification procedures (within 60 days)
- Business Associate Agreement (BAA) availability
- Patient rights (access, amendment, accounting of disclosures)
- Minimum necessary standard
- Workforce training requirements

**Technical Safeguards:**
- AES-256 encryption at rest
- TLS 1.3 encryption in transit
- Multi-factor authentication (MFA)
- Role-based access control (RBAC)
- Audit logging (immutable, 7+ years)
- Automatic session timeout
- Intrusion detection systems

### 3. Google API Services User Data Policy

**Critical Requirements:**
- **Limited Use**: Only use Google user data for providing/improving the app's user-facing features
- **No Selling Data**: Explicit statement that Google user data is NOT sold to third parties
- **No AI Training**: Do not use Google Workspace data for training generalized AI models without explicit consent
- **Secure Transmission**: All data transmitted via modern cryptography (TLS 1.2+)
- **Privacy Policy Link**: Must be easily accessible from app (footer, settings)
- **Scope Justification**: Only request minimum necessary scopes

**Example Compliant Statement:**
> "We access your Google Calendar data solely to check availability and book appointments on your behalf. We do not sell your Google user data to third parties. We do not use your Google Workspace data for training generalized AI models without your explicit consent. All data is transmitted using industry-standard encryption (TLS 1.3)."

### 4. Google Play Store Requirements

**Privacy Policy Must Include:**
- Developer/company name and contact information
- Types of data collected (personal, sensitive, device)
- How data is used and shared
- Data retention and deletion policies
- Security measures
- User rights and choices
- Third-party service providers (with links to their privacy policies)
- Children's privacy (COPPA compliance if applicable)

**Mandatory Disclosures:**
- Calendar access (if using Google Calendar API)
- Microphone access (if using voice features)
- Phone/SMS access (if using Twilio)
- Contact access (if syncing contacts)

---

## Template Structure

### Privacy Policy Template

**Recommended Length:** 500-800 lines (2,000-4,000 words)

**Section Structure:**
1. **Introduction** (who we are, commitment to privacy)
2. **Information We Collect**
   - Information you provide directly
   - Information collected automatically
   - Information from third parties
   - Google user data (Calendar, Profile)
3. **How We Use Your Information**
   - Service provision
   - Communications
   - Analytics and improvements
   - Legal compliance
4. **Legal Basis for Processing (GDPR)**
   - Consent
   - Contractual necessity
   - Legitimate interests
5. **Data Sharing and Disclosure**
   - Service providers (Vapi, Twilio, Supabase)
   - Legal requirements
   - Business transfers
   - With your consent
6. **Google User Data Specific Policies**
   - Limited use commitment
   - No selling data
   - No AI training without consent
   - Secure transmission
7. **Data Retention**
   - Active account data (duration)
   - Inactive account data (30-90 days)
   - Legal hold requirements
8. **Your Rights (GDPR)**
   - Access, rectification, erasure
   - Portability, restriction, objection
   - How to exercise rights
9. **Security Measures**
   - Encryption (AES-256, TLS 1.3)
   - Access controls
   - Monitoring and auditing
10. **International Data Transfers**
    - EU-US Data Privacy Framework
    - Standard Contractual Clauses (SCCs)
11. **Children's Privacy** (if applicable)
12. **Changes to This Policy**
13. **Contact Us** (email, address, phone)

### Terms of Service Template

**Recommended Length:** 600-1,000 lines (3,000-5,000 words)

**Section Structure:**
1. **Acceptance of Terms**
2. **Definitions** (Service, User, Organization, PHI, etc.)
3. **Service Description**
   - AI voice receptionist features
   - Third-party integrations (Google Calendar, Twilio)
   - Limitations and disclaimers
4. **Account Registration**
   - Eligibility requirements
   - Account security
   - Accurate information requirement
5. **User Obligations**
   - Acceptable use policy
   - Prohibited activities
   - Compliance with laws (HIPAA, state regulations)
6. **Payment Terms**
   - Pricing and billing cycles
   - Payment methods
   - Late fees and collection
7. **Cancellation and Refunds**
   - Cancellation process
   - Refund policy (pro-rata or no refunds)
   - Data export upon cancellation
8. **Intellectual Property**
   - Our IP (platform, algorithms, trademarks)
   - Your IP (customer data, recordings)
   - License grants
9. **HIPAA and Data Protection**
   - BAA availability for enterprise clients
   - PHI handling obligations
   - User responsibilities for HIPAA compliance
10. **Service Level Agreement (SLA)**
    - Uptime commitments (99.9%)
    - Service credits for downtime
    - Scheduled maintenance windows
11. **Limitation of Liability**
    - Disclaimers (no guarantees of 100% accuracy)
    - Liability cap (12 months of fees or $10,000)
    - Exclusion of consequential damages
12. **Indemnification**
    - User indemnifies us for their misuse
    - We indemnify user for our IP infringement
13. **Dispute Resolution**
    - Informal negotiation (30 days)
    - Binding arbitration (AAA rules)
    - Class action waiver
14. **Governing Law** (Delaware or UK)
15. **Modifications to Terms**
16. **Termination**
17. **Entire Agreement and Severability**
18. **Contact Information**

### HIPAA Compliance Page Template

**Recommended Length:** 400-600 lines (2,000-3,000 words)

**Section Structure:**
1. **HIPAA Overview**
   - What is HIPAA?
   - Why it matters for healthcare providers
   - Our commitment to compliance
2. **What is PHI?**
   - Definition and examples
   - How Voxanne AI handles PHI
3. **Security Safeguards**
   - Administrative safeguards (policies, training)
   - Physical safeguards (data center security)
   - Technical safeguards (encryption, access controls)
4. **Encryption Standards**
   - AES-256 encryption at rest
   - TLS 1.3 encryption in transit
   - End-to-end encryption for voice calls
5. **Access Controls**
   - Role-based access control (RBAC)
   - Multi-factor authentication (MFA)
   - Audit logging
6. **Business Associate Agreement (BAA)**
   - What is a BAA?
   - When is it required?
   - How to request a BAA (enterprise clients)
7. **Breach Notification**
   - Our breach response plan
   - 60-day notification requirement
   - Contact: security@voxanne.ai
8. **Patient Rights Under HIPAA**
   - Right to access medical records
   - Right to request amendments
   - Right to accounting of disclosures
9. **Compliance Certifications**
   - SOC 2 Type II (in progress/completed)
   - Annual security assessments
10. **Workforce Training**
11. **Contact Information**
    - Security Officer: security@voxanne.ai
    - Privacy Officer: privacy@voxanne.ai

### Cookie Policy Template

**Recommended Length:** 300-400 lines (1,500-2,000 words)

**Section Structure:**
1. **What Are Cookies?**
2. **Types of Cookies We Use**
   - Essential cookies (authentication, security)
   - Analytics cookies (Google Analytics)
   - Marketing cookies (if applicable)
3. **Third-Party Cookies**
   - Google Analytics
   - Stripe (payment processing)
   - Intercom (customer support chat)
4. **Cookie Duration**
   - Session cookies (deleted when browser closes)
   - Persistent cookies (specific durations)
5. **How to Control Cookies**
   - Browser settings
   - Opt-out links (Google Analytics opt-out)
   - Do Not Track (DNT) signals
6. **Cookie Consent**
   - EU/UK users: consent required for non-essential cookies
   - Cookie banner implementation
7. **Cookie Table** (name, purpose, duration, type)
8. **Contact Us**

---

## Company Information Template

Use the following standard information for all legal documents:

**Company Name:** Voxanne AI (a product of Call Waiting AI)

**Legal Entity:** Call Waiting AI Ltd.

**Registered Address:**
Collage House, 2nd Floor
17 King Edward Road
Ruislip, London HA4 7AE
United Kingdom

**Contact Emails:**
- General Support: support@voxanne.ai
- Privacy Inquiries: privacy@voxanne.ai
- Security Issues: security@voxanne.ai
- Legal Matters: legal@voxanne.ai
- Sales: sales@voxanne.ai

**Governing Law:**
- For UK/EU customers: England and Wales
- For US customers: State of Delaware
- For international: Delaware (default)

**Data Protection Officer (if applicable):**
Email: dpo@voxanne.ai

---

## Third-Party Services to Disclose

**Infrastructure Providers:**
- **Supabase** (database, authentication) - https://supabase.com/privacy
- **Vercel** (hosting) - https://vercel.com/legal/privacy-policy
- **Google Cloud** (infrastructure) - https://policies.google.com/privacy

**Communication Services:**
- **Vapi** (voice AI) - https://vapi.ai/privacy
- **Twilio** (telephony, SMS) - https://www.twilio.com/legal/privacy
- **Google Calendar API** - https://policies.google.com/privacy

**Payment Processing:**
- **Stripe** (payments) - https://stripe.com/privacy

**Monitoring & Analytics:**
- **Google Analytics** - https://policies.google.com/privacy
- **Sentry** (error tracking) - https://sentry.io/privacy/

**Customer Support:**
- **Intercom** (if used) - https://www.intercom.com/legal/privacy

---

## Data Retention Policy Template

**Standard Retention Periods:**
- **Active account data:** Retained while account is active
- **Inactive accounts:** 30 days after last login, then flagged for deletion
- **Deleted account data:** 90 days (soft delete), then permanent deletion
- **Call recordings:** 30 days (adjustable per organization, max 7 years)
- **Transcripts:** 90 days (adjustable per organization)
- **Audit logs:** 7 years (HIPAA requirement)
- **Payment records:** 7 years (tax/legal requirement)
- **Support tickets:** 3 years

**Legal Hold:** Data subject to legal proceedings is retained until matter is resolved.

---

## Security Measures to Document

**Encryption:**
- AES-256 encryption for data at rest
- TLS 1.3 for data in transit
- End-to-end encryption for voice calls (where applicable)

**Access Controls:**
- Role-based access control (RBAC)
- Multi-factor authentication (MFA) for admin accounts
- Principle of least privilege
- Automatic session timeout (15 minutes)

**Monitoring:**
- 24/7 security monitoring
- Intrusion detection systems (IDS)
- Automated vulnerability scanning
- Penetration testing (annually)

**Backup & Disaster Recovery:**
- Daily encrypted backups
- 30-day backup retention
- Multi-region redundancy
- Disaster recovery plan (RTO: <1 hour, RPO: <24 hours)

**Incident Response:**
- Dedicated security team
- 24-hour breach notification to affected users
- Forensic investigation procedures
- Post-incident review and remediation

---

## Usage Examples

### Example 1: Generate Privacy Policy

```markdown
Generate a GDPR-compliant privacy policy for Voxanne AI with the following:

- Company: Voxanne AI (Call Waiting AI Ltd.)
- Address: Collage House, 2nd Floor, 17 King Edward Road, Ruislip, London HA4 7AE
- Services: AI voice receptionist for healthcare providers
- Data collected: Name, email, phone, clinic info, call recordings, transcripts, Google Calendar data
- Third parties: Vapi, Twilio, Supabase, Google Calendar API, Stripe
- Retention: 30 days inactive, 90 days soft delete, 7 years audit logs
- Contact: privacy@voxanne.ai
- Google API compliance: Yes (Calendar access)
- Target length: 500+ lines
```

### Example 2: Generate HIPAA Compliance Page

```markdown
Generate a comprehensive HIPAA compliance page for Voxanne AI:

- Audience: Healthcare providers (dental, medical clinics)
- PHI handled: Patient names, phone numbers, appointment details, medical queries
- Encryption: AES-256 at rest, TLS 1.3 in transit
- BAA: Available for enterprise clients (contact sales@voxanne.ai)
- Security contact: security@voxanne.ai
- Certifications: SOC 2 Type II (in progress)
- Target length: 400+ lines
```

### Example 3: Review Existing Policy for Google API Compliance

```markdown
Review this privacy policy for Google API Services User Data Policy compliance:

[paste existing policy]

Check for:
- Limited use statement
- No selling data statement
- No AI training statement
- Secure transmission mention
- Calendar data specific disclosures
- Easy-to-find location in app
```

---

## Best Practices

### 1. Plain Language
- Avoid legalese where possible
- Use short sentences (15-20 words)
- Define technical terms (e.g., "PHI" = Protected Health Information)
- Use examples (e.g., "call recordings may contain PHI such as...")

### 2. Transparency
- Be specific about data collection ("we collect your email address" vs. "we collect information")
- Explain WHY data is collected (not just what)
- Disclose all third parties (with links to their privacy policies)

### 3. User-Friendly Formatting
- Use headings and subheadings
- Use bullet points for lists
- Highlight key information (bold or colored text)
- Provide table of contents for long documents

### 4. Regular Updates
- Review policies every 6 months
- Update "Last Updated" date whenever changes are made
- Notify users of material changes (email + in-app banner)

### 5. Legal Review
- All generated documents should be reviewed by a qualified attorney
- Especially important for healthcare (HIPAA) and EU markets (GDPR)
- Consider hiring specialized privacy counsel

---

## Compliance Checklist

Use this checklist to verify compliance before publishing:

### GDPR Compliance
- [ ] Legal basis for processing disclosed
- [ ] All data subject rights documented
- [ ] Data retention periods specified
- [ ] International transfer mechanisms disclosed
- [ ] Right to lodge complaint mentioned
- [ ] DPO or privacy contact provided
- [ ] Cookie consent mechanism implemented

### HIPAA Compliance
- [ ] PHI definition provided
- [ ] Security safeguards documented (admin, physical, technical)
- [ ] BAA availability disclosed
- [ ] Breach notification procedure documented
- [ ] Patient rights under HIPAA listed
- [ ] Security contact provided

### Google API Compliance
- [ ] Limited use statement included
- [ ] No selling data statement included
- [ ] No AI training statement included
- [ ] Secure transmission mentioned
- [ ] Calendar-specific disclosures included
- [ ] Privacy policy linked from app footer

### App Store Compliance (Google Play / Apple)
- [ ] Company name and contact information visible
- [ ] Types of data collected listed
- [ ] How data is used explained
- [ ] Third-party services disclosed (with links)
- [ ] Data retention policy documented
- [ ] User rights and choices explained
- [ ] Security measures described

---

## Output Format

When generating legal documents, use this structure:

1. **File Header** (component metadata)
2. **Document Title** (e.g., "Privacy Policy")
3. **Last Updated Date** (current date)
4. **Table of Contents** (for long documents)
5. **Main Content** (sections with headings)
6. **Contact Information** (footer)

**Example Output:**

```tsx
import React from 'react';

export default function PrivacyPolicy() {
    return (
        <div className="min-h-screen bg-slate-50 py-20 px-6">
            <div className="max-w-4xl mx-auto bg-white p-12 rounded-2xl shadow-sm border border-slate-200">
                <h1 className="text-4xl font-bold text-slate-900 mb-8">Privacy Policy</h1>
                <p className="text-slate-500 mb-8">Last Updated: January 30, 2026</p>

                <div className="prose prose-slate max-w-none">
                    {/* Content sections */}
                </div>
            </div>
        </div>
    );
}
```

---

## Legal Disclaimers

**IMPORTANT:** This skill provides template legal documentation based on common best practices and regulatory requirements. However:

- Generated documents are NOT a substitute for legal advice
- All documents should be reviewed by a qualified attorney
- Compliance requirements vary by jurisdiction
- Healthcare regulations (HIPAA) require specialized counsel
- EU/UK regulations (GDPR) may require Data Protection Officer
- This skill is for informational purposes only

**Recommended:** Consult with:
- Privacy attorney (for GDPR/CCPA compliance)
- Healthcare attorney (for HIPAA compliance)
- Corporate attorney (for terms of service, liability)

---

## Version History

- **v1.0** (2026-01-30): Initial skill creation
  - Privacy policy template
  - Terms of service template
  - HIPAA compliance page template
  - Cookie policy template
  - Google API compliance guidelines

---

## Support

For questions about this skill or legal compliance:
- **Documentation Issues:** Open GitHub issue
- **Legal Questions:** Consult qualified attorney
- **Compliance Guidance:** privacy@voxanne.ai

---

**End of Legal Compliance Agent Skill**
