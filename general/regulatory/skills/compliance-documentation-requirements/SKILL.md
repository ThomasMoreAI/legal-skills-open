---
name: compliance-documentation-requirements
title: Compliance Documentation Requirements
description: 'Use when setting up or auditing how compliance documentation is structured, collected, and preserved for regulatory audit in Salesforce FSC — covering KYC data collection workflows, AML screening integration setup, audit trail configuration, and regulatory reporting readiness. Triggers: KYC form setup, AML integration configuration, compliance data collection, audit trail setup, regulatory documentation workflow, Field Audit Trail configuration, Setup Audit Trail, Event Monitoring, Discovery Framework, FSC KYC objects, Identity Document setup, Party Identity Verification. NOT for security implementation, NOT for designing AML/KYC architecture (use architect/aml-kyc-process-architecture), NOT for configuring who can access deal or client data (use admin/compliant-data-sharing-setup).'
author: PranavNagrecha
author_url: https://github.com/PranavNagrecha/AwesomeSalesforceSkills/tree/main/skills/admin/compliance-documentation-requirements
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
tags: [compliance, kyc, aml, fsc, audit-trail, field-audit-trail, discovery-framework, identity-verification, financial-services, regulatory-documentation]
---

# Compliance Documentation Requirements

Use this skill when configuring how compliance documentation is structured, collected, and preserved in Salesforce FSC for regulatory purposes. This skill covers the admin-layer setup of KYC data collection workflows using FSC's native data model and Discovery Framework, the integration setup for AML screening via third-party vendors, and the layered audit trail configuration required for regulatory audit readiness. It produces configured org metadata and documented compliance data flows — not architecture design artifacts.

This skill is distinct from `admin/compliant-data-sharing-setup`, which governs WHO can see deal and client data (Compliant Data Sharing). This skill governs HOW compliance documentation is structured, collected, and preserved for regulatory audit obligations.

---

## Before Starting

- **Verify FSC license type.** The FSC KYC data model objects — `PartyIdentityVerification`, `IdentityDocument`, `PartyProfileRisk`, and `PartyScreeningSummary` — are part of the FSC data model and require an FSC license. They are not available in standard CRM.
- **Confirm OmniStudio licensing for Discovery Framework.** The Discovery Framework — the recommended FSC mechanism for structured, versioned data collection — is backed by OmniStudio (OmniScript + DataRaptor). It requires OmniStudio or Industries Cloud licenses. Without OmniStudio, custom Screen Flows must substitute but lose native versioning.
- **Determine whether Shield is in scope.** Field Audit Trail — required to retain historical values of sensitive KYC fields beyond the standard 18-month field history — is a Salesforce Shield add-on. It is not included in base FSC. If the regulatory retention obligation exceeds 18 months for field-level data (common under BSA/FinCEN: 5 years), Shield must be licensed. Setup Audit Trail and Event Monitoring have different scopes and different add-on requirements.
- **Do not assume FSC has a native AML engine.** FSC provides objects to store screening results but has no internal watchlist, PEP database, or sanctions list matching capability. Every AML screening decision comes from a third-party vendor integrated via the Set Up Integrations pattern. This is non-negotiable for regulatory compliance.
- **Identify which audit trail components address which regulatory obligation.** Setup Audit Trail covers configuration changes; Field Audit Trail covers field value history at scale; Event Monitoring covers user activity and login behavior. All three serve distinct compliance documentation purposes and are often required in combination.

---

## Core Concepts

### FSC KYC Data Model — Four Core Objects

FSC provides four standard objects that form the KYC documentation layer for financial institutions:

- **`PartyIdentityVerification`** — records the outcome of a specific identity verification event for an individual or account. Fields include verification type, verification status (Verified / Unverified / Expired), verification date, and the method used (e.g., government ID check, biometric). One individual can have multiple verification records as they pass through periodic review cycles.
- **`IdentityDocument`** — stores document-level detail for identity evidence collected during KYC. Fields include document type (Passport, National ID, Driver's License), issuing authority, issue date, expiry date, and document number. Linked to a `PartyIdentityVerification` record. Never store raw document images in a standard text field — use Salesforce Files with Content Version if document scans must be stored.
- **`PartyProfileRisk`** — stores the regulatory risk assessment record for an individual or account. Core fields: `RiskCategory` (Low / Medium / High / Prohibited), `RiskScore`, `RiskReason`, `RiskReviewDate`. This is the canonical store for the customer's AML risk tier.
- **`PartyScreeningSummary`** — stores the result of an AML screening event. Fields capture the screening vendor reference, match status (Clear / Potential Match / Confirmed Match), and screening type (sanctions, PEP, adverse media). Created by the AML integration process and linked to the Individual and the associated `PartyProfileRisk` update workflow.

All four objects associate to the `Individual` object (the FSC person record), not directly to `Contact`. Ensure every onboarded individual has a linked `Individual` record before attempting to create these child records.

### Discovery Framework for Structured, Versioned Data Collection

The Discovery Framework is the FSC-native mechanism for collecting compliance questionnaire data — KYC questionnaires, suitability assessments, periodic review forms — in a structured, versioned, audit-ready format. It is built on OmniStudio (OmniScript + DataRaptor + Integration Procedures) and stores responses as versioned `AssessmentQuestion` and `AssessmentQuestionResponse` records.

Key compliance-relevant properties:
- **Versioned responses:** Each submission creates a new version, preserving the history of what was collected and when. Prior versions remain immutable and available for audit.
- **Structured schema:** Questions are defined in a managed schema (`AssessmentQuestion`, `AssessmentQuestionSet`), not as free text. This enables regulatory-quality data exports.
- **Audit timestamps:** Response records capture the submitting user, submission date, and channel (agent-assisted vs. self-service). These are required for audit trail completeness.

Without OmniStudio, you must build equivalent structured collection using Screen Flows and a custom versioning pattern (e.g., creating new custom records on each update rather than overwriting). This is significantly more effort and produces weaker audit properties.

### Layered Audit Trail — Three Components for Three Scopes

FSC compliance documentation requires three distinct audit trail tools, each covering a different scope:

1. **Setup Audit Trail** — built into every Salesforce org (no add-on). Records configuration changes made in Setup: profile changes, permission set assignments, metadata deployments, user account changes. Retained for 180 days in the standard org. Required for demonstrating that system configuration has not been altered without authorization. Export periodically and archive externally to satisfy retention obligations beyond 180 days.

2. **Field Audit Trail (Shield add-on)** — extends field history retention from the standard 18-month limit to up to 10 years for defined fields on specified objects. Required when regulatory obligation mandates long-term retention of field-level change history (e.g., who changed a customer's risk category, from what value, on what date, and who approved it). Configure via Field Audit Trail Policy in Setup, available only with Salesforce Shield license. Without Shield, field history is capped at 18 months and limited to 20 tracked fields per object.

3. **Event Monitoring (Shield add-on)** — captures detailed user activity logs: login events, API calls, report exports, record views, field access on sensitive records. Delivered as hourly or daily log files queryable via the EventLogFile object. Required for demonstrating that sensitive KYC data was accessed only by authorized users during the audit period. Also available in a lighter Event Monitoring Analytics App form.

---

## Common Patterns

### Pattern A: KYC Data Collection via Discovery Framework OmniScript

**When to use:** New client onboarding in FSC where an agent or self-service portal collects identity data (name, date of birth, nationality, government ID details) and the data must be versioned and audit-ready.

**How it works:**

1. Enable the Discovery Framework feature in FSC Setup (Financial Services Cloud Settings > Enable Know Your Customer).
2. Define `AssessmentQuestionSet` records for the KYC questionnaire (identity data, document details, beneficial ownership if applicable).
3. Build an OmniScript that drives the agent through the questionnaire. Each step maps to an `AssessmentQuestion`.
4. Use a DataRaptor Turbo Action to save responses as `AssessmentQuestionResponse` records linked to the individual and the onboarding event.
5. On completion, trigger creation of `PartyIdentityVerification` and `IdentityDocument` records using a DataRaptor or Integration Procedure based on the questionnaire responses.
6. The response records carry submitting user, timestamp, and version — meeting audit trail requirements for the collection event.

**Why not a custom Flow with free-text fields:** Unstructured data in custom text fields cannot be versioned natively, produces no audit timestamp on the collection event itself, and is difficult to export in a regulatory-quality structured format for audit.

### Pattern B: AML Screening Integration Setup via Named Credential

**When to use:** Configuring the Salesforce side of an AML screening integration with a third-party vendor (e.g., Onfido, Refinitiv World-Check, LexisNexis) after the architectural pattern has been selected.

**How it works:**

1. In Setup, create an External Credential (or Named Credential for Legacy auth) for the screening vendor endpoint. Select Named Principal authentication (not Per-User) so batch and scheduled contexts can resolve the credential.
2. Create a Named Credential referencing the External Credential. Set the endpoint URL to the vendor's API root.
3. Grant permission to the Named Credential via a Permission Set assigned to the integration user (not to all users).
4. Configure the Integration Procedure or Apex callout to use the Named Credential label — never hardcode the endpoint URL or API key in OmniStudio procedure JSON or Apex code.
5. Create a custom field or configure the standard `PartyScreeningSummary` fields to capture the vendor's case reference number, match result, and screening timestamp.
6. Test the integration using a single record in a sandbox before enabling for bulk onboarding.

**Why not store the API key in Custom Metadata or Custom Settings:** API keys in Custom Metadata or Custom Settings are visible to admins and exportable via metadata retrieval. Named Credentials encrypt the credential value and prevent it from being read back through the UI or API, satisfying security review requirements for credential management.

---

## Decision Guidance

| Situation | Recommended Approach | Reason |
|---|---|---|
| Collecting KYC questionnaire data with audit-ready versioning | Discovery Framework OmniScript + AssessmentQuestionResponse | Native versioning, structured schema, audit timestamps |
| FSC org without OmniStudio license | Screen Flow + custom versioning records | OmniStudio unavailable; custom versioning is manual but auditable |
| Storing identity document metadata | IdentityDocument object linked to PartyIdentityVerification | Standard FSC object; avoids custom schema duplication |
| AML screening vendor integration (Named Principal auth) | External Credential (Named Principal) + Named Credential | Works in batch/scheduled contexts; encrypts credential |
| Field-level change history beyond 18 months | Field Audit Trail (Shield add-on) | Standard history is capped at 18 months; Shield extends to 10 years |
| Demonstrating no unauthorized configuration changes | Setup Audit Trail + external archival | Built-in, no add-on; export and archive beyond 180 days |
| Demonstrating authorized data access for audit | Event Monitoring (Shield add-on) | Captures per-user field access and report export events |
| Storing AML screening results | PartyScreeningSummary + PartyProfileRisk update | Standard FSC objects purpose-built for this purpose |

---

## Recommended Workflow

Step-by-step instructions for an AI agent or practitioner setting up compliance documentation in FSC:

1. **Confirm prerequisites** — verify FSC is enabled, confirm whether OmniStudio is licensed (required for Discovery Framework), determine whether Salesforce Shield is in scope (required for Field Audit Trail and Event Monitoring), and identify the AML screening vendor if applicable. Record the regulatory retention obligation in months/years for each data type.

2. **Enable FSC KYC feature and verify data model** — navigate to Financial Services Cloud Settings in Setup, enable "Know Your Customer." Verify that `PartyIdentityVerification`, `IdentityDocument`, `PartyProfileRisk`, and `PartyScreeningSummary` objects are present and accessible. Confirm that every onboarded individual will have a linked `Individual` record (check the Person Account or Contact-to-Individual linking configuration).

3. **Configure the Discovery Framework for data collection** — define `AssessmentQuestionSet` and `AssessmentQuestion` records for the KYC questionnaire. Build an OmniScript to drive the collection flow. Ensure responses are saved as `AssessmentQuestionResponse` records with user and timestamp fields populated. If OmniStudio is unavailable, build a Screen Flow with a custom versioned response object.

4. **Set up AML screening integration** — create an External Credential with Named Principal authentication for the screening vendor. Create a Named Credential referencing it. Configure the Integration Procedure or Apex callout to call the vendor API using the Named Credential label. Map vendor response fields to `PartyScreeningSummary` and trigger a `PartyProfileRisk` update workflow on receipt of results.

5. **Configure audit trail components** — enable field history tracking on `PartyIdentityVerification`, `IdentityDocument`, and `PartyProfileRisk` for key fields. If Shield is licensed, configure Field Audit Trail Policy for fields requiring retention beyond 18 months. Set up Event Monitoring log file retrieval (if Shield licensed) and establish a process to archive Setup Audit Trail exports beyond the 180-day platform retention.

6. **Validate data collection completeness** — run a test onboarding end-to-end. Confirm that after completion, the following records exist: `Individual`, `PartyIdentityVerification` (status = Verified), at least one `IdentityDocument` with document type and expiry, `PartyProfileRisk` with RiskCategory populated, `PartyScreeningSummary` with screening result from the vendor.

7. **Review against regulatory checklist** — confirm that each regulatory obligation (identity collection, screening, risk rating, documentation retention) is covered by a concrete Salesforce record or log artifact. Document which audit trail layer covers which obligation and identify any gaps requiring external archival.

---

## Review Checklist

Run through these before marking compliance documentation setup complete:

- [ ] FSC KYC feature is enabled; all four KYC objects (PartyIdentityVerification, IdentityDocument, PartyProfileRisk, PartyScreeningSummary) are accessible and mapped to onboarding workflow
- [ ] Discovery Framework OmniScript (or equivalent) produces versioned AssessmentQuestionResponse records with user and timestamp fields
- [ ] AML screening integration uses Named Credential with Named Principal auth — no hardcoded API keys in metadata or code
- [ ] PartyScreeningSummary records capture vendor case reference, match result, and screening timestamp
- [ ] Field history tracking is enabled on key KYC fields; Field Audit Trail policy configured if Shield is licensed
- [ ] Setup Audit Trail export and archival process is documented and scheduled
- [ ] Event Monitoring log retrieval process is in place if Shield is licensed
- [ ] Every onboarded individual has a linked Individual record (not just Contact)
- [ ] Retention period for each data type is documented and coverage is confirmed (Shield vs. standard history vs. external archive)
- [ ] Regulatory documentation checklist reviewed; no gaps between obligations and platform artifacts

---

## Salesforce-Specific Gotchas

Non-obvious platform behaviors that cause real production problems:

1. **Field Audit Trail requires Shield — it is not part of base FSC** — Admins sometimes enable standard field history tracking (up to 20 fields, 18-month limit) and believe it satisfies regulatory retention requirements. For obligations requiring 5–7 year field-level retention (common under BSA/FinCEN), only Field Audit Trail (Salesforce Shield add-on, separately licensed) meets the requirement. Confirm Shield licensing before designing the audit trail architecture.

2. **PartyIdentityVerification and IdentityDocument require an Individual record parent** — These objects relate to `Individual`, not `Contact`. In orgs where contacts are created without the FSC Individual linking feature, or where bulk data imports bypassed Individual creation, there is no valid parent to attach KYC records. Validate the Contact-to-Individual mapping at the start of any KYC setup project.

3. **Setup Audit Trail retains only 180 days natively** — The built-in Setup Audit Trail in all Salesforce orgs retains entries for 180 days only. Organizations with multi-year compliance audit requirements must establish a process to export Setup Audit Trail records (via SOQL on `SetupAuditTrail`) and archive them externally on a recurring schedule. This is not automated by default.

4. **AML screening has no native FSC engine — third-party integration is mandatory** — FSC does not contain any watchlist data, sanctions lists, or PEP databases. The `PartyScreeningSummary` object stores results from external screening calls but performs no screening itself. Any compliance workflow that omits the third-party integration and relies solely on the FSC object schema will produce empty screening records and fail regulatory review.

5. **Named Credentials with Per-User authentication fail in batch and scheduled contexts** — If the AML screening integration uses a Named Credential configured for Per-User OAuth, callouts will fail in any context that does not have an active user session: batch jobs, scheduled Apex, future methods, and Platform Event triggers. Use Named Principal (org-level) authentication on Named Credentials that back automated compliance workflows.

---

## Output Artifacts

| Artifact | Description |
|---|---|
| Configured FSC KYC objects | PartyIdentityVerification, IdentityDocument, PartyProfileRisk, PartyScreeningSummary with appropriate fields tracked and layouts configured |
| Discovery Framework questionnaire | OmniScript with AssessmentQuestionSet producing versioned, audit-ready AssessmentQuestionResponse records |
| Named Credential (AML vendor) | Named Credential with Named Principal auth backing the AML screening integration |
| Audit trail configuration plan | Documented coverage of Setup Audit Trail, Field Audit Trail (if Shield), and Event Monitoring against each regulatory retention obligation |
| Regulatory documentation checklist | Mapping of each compliance obligation to the Salesforce artifact that satisfies it |

---

## Related Skills

- `architect/aml-kyc-process-architecture` — use when designing the architecture for AML/KYC orchestration; this skill covers admin-layer setup after the architecture decision is made
- `admin/compliant-data-sharing-setup` — use to configure who can see deal and client data (Compliant Data Sharing rules); distinct from how compliance documentation is collected and preserved
- `admin/fsc-action-plans` — use to configure task-based onboarding checklists that drive KYC collection steps
- `admin/health-cloud-consent-management` — parallel pattern for consent documentation in Health Cloud; useful reference for versioned consent record design

## Official Sources Used

- Enable Know Your Customer for FSC — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_kyc_enable.htm
- FSC KYC Data Model (Developer Guide) — https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_kyc_data_model.htm
- Set Up AML Screening Integrations — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_aml_screening_setup.htm
- Compliant Data Sharing in FSC — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_compliant_data_sharing.htm
- Field Audit Trail — https://help.salesforce.com/s/articleView?id=sf.field_audit_trail.htm
- Setup Audit Trail — https://help.salesforce.com/s/articleView?id=sf.admin_monitorsetup.htm
- Event Monitoring — https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_resources_event_log_files.htm
- Named Credentials — https://help.salesforce.com/s/articleView?id=sf.named_credentials_about.htm
