# Official sources — RISE with SAP SLA and Vendor Risk Review

Use this reference when grounding responsibility split classification, SLA and credit mechanism assessment, availability and DR commitments, data residency obligations, exit and portability provisions, shared security responsibilities, and audit rights.

**Evidence level**: documentation-based (SAP Trust Center, SAP Help Portal, SAP cloud service descriptions). No live-system evidence is collected by this skill.

## RISE with SAP contractual framework

- RISE with SAP
  https://help.sap.com/docs/RISE/rise-with-sap/rise-with-sap
  source_owner: SAP SE
  topic_supported: RISE with SAP commercial model, included services scope, infrastructure and application layer responsibilities, bundled SAP BTP entitlements
  why_needed: Primary reference for understanding what is included in RISE with SAP and where the boundary between SAP-managed and customer-managed scope lies
  evidence_level: primary
  last_verified: 2026-06-19

- SAP Trust Center: Cloud Service Agreements
  https://www.sap.com/about/trust-center/cloud-service-agreements.html
  source_owner: SAP SE
  topic_supported: SAP cloud service level agreements, cloud service descriptions, supplemental terms, data processing agreements, order forms
  why_needed: Primary contractual reference for SLA tier definitions, credit mechanisms, availability commitments, and the legal framework governing RISE with SAP and other SAP cloud services
  evidence_level: primary
  last_verified: 2026-06-19

- SAP Trust Center: Shared Responsibility Model
  https://www.sap.com/about/trust-center/shared-responsibility-model.html
  source_owner: SAP SE
  topic_supported: SAP vs customer responsibility matrix for infrastructure, platform, application, and data layers across RISE with SAP and SAP BTP
  why_needed: Canonical reference for the shared responsibility split — defines what SAP manages and what the customer manages, which is the foundation for all responsibility gap findings
  evidence_level: primary
  last_verified: 2026-06-19

## Security and trust

- SAP Trust Center: Security
  https://www.sap.com/about/trust-center/security.html
  source_owner: SAP SE
  topic_supported: SAP security framework, security certifications (ISO 27001, SOC 2, BSI C5), penetration testing, vulnerability management, security incident response
  why_needed: Required to assess what security obligations SAP fulfills contractually versus what the customer must implement, and to evaluate the adequacy of third-party certification evidence
  evidence_level: primary
  last_verified: 2026-06-19

- SAP Trust Center: Availability
  https://www.sap.com/about/trust-center/availability.html
  source_owner: SAP SE
  topic_supported: SAP cloud service availability status, historical uptime, planned maintenance windows, incident communication
  why_needed: Provides the published availability track record against which SLA commitments can be contextually evaluated; also defines the maintenance window model that affects effective availability
  evidence_level: primary
  last_verified: 2026-06-19

## Data privacy and residency

- SAP Trust Center: Data Privacy
  https://www.sap.com/about/trust-center/data-privacy.html
  source_owner: SAP SE
  topic_supported: SAP data processing agreements, GDPR compliance posture, data residency options, cross-border data transfer mechanisms (SCCs, BCRs), data subject rights
  why_needed: Primary reference for data residency and cross-border transfer obligations — required to assess whether contractual data residency clauses are backed by adequate legal transfer mechanisms and technical controls
  evidence_level: primary
  last_verified: 2026-06-19

## System and contract administration

- SAP Customer Administration Center (SAP for Me / CAC)
  https://support.sap.com/en/my-support/systems-installations/cac.html
  source_owner: SAP SE
  topic_supported: SAP contract and system administration, system details, license and contract information access, system provisioning status
  why_needed: Reference for understanding how customers access and manage their SAP contractual system information — relevant when assessing whether exit and portability provisions are practically accessible
  evidence_level: supplementary
  last_verified: 2026-06-19

## Grounding rule

SAP Trust Center and cloud service agreement documentation describe SAP's published contractual framework, standard SLA terms, and stated security and privacy commitments. They do not prove what terms are in the user's specific signed contract, what SLA credits have been granted historically, or whether SAP's operational practices match the published commitments. Users must supply their signed contract excerpts, SLA schedules, or order forms for concrete contractual risk assessment. This skill does not provide legal advice.
