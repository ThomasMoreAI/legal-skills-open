# Well-Architected Notes — Compliance Documentation Requirements

## Relevant Pillars

- **Security** — Compliance documentation contains sensitive identity data (government ID numbers, dates of birth, document scans) and regulatory risk decisions. Well-Architected Security requires that these records are protected at rest and in transit, access is limited to authorized roles, and audit evidence of access patterns is captured via Event Monitoring. Named Credentials protect integration secrets. Compliant Data Sharing rules (a separate skill) control which users can see which client records.

- **Operational Excellence** — Compliance documentation workflows must be reliable and observable. The Setup Audit Trail archival process, Field Audit Trail configuration, and AML screening integration must all be monitored. Failures in the screening integration (vendor downtime, callout timeouts) must be detected and remediated before they create regulatory gaps. Operational Excellence requires documented runbooks for common failure modes: vendor API unavailability, batch re-screening job failures, and expired identity documents.

- **Reliability** — The AML screening integration is a critical compliance control. If the integration fails silently and screening results are not written, the onboarding process appears to complete successfully but compliance obligations are unmet. Reliability requires that the integration has explicit error handling, that failures surface as Cases or alerts to a compliance operations queue, and that the batch re-screening job has retry logic.

- **Scalability** — As the client portfolio grows, the volume of periodic re-screening events, `AssessmentQuestionResponse` records, and `PartyScreeningSummary` records will grow proportionally. The batch re-screening pattern must be sized against governor limits (callout limits, batch size limits) for the projected portfolio size. AssessmentQuestionResponse record accumulation over multiple KYC cycles per client per year can produce significant data volume over a 5-year retention period.

- **Performance** — synchronous AML screening callouts add latency to the onboarding workflow. Vendors that respond in under 3 seconds support a synchronous OmniScript pattern. Vendors with variable response times or SLAs above 5 seconds should use an asynchronous pattern to avoid agent-facing timeouts.

## Architectural Tradeoffs

**Synchronous vs. Asynchronous Screening:**
Synchronous screening (Integration Procedure calling vendor API inline during OmniScript) gives the agent an immediate result at the cost of coupling the onboarding workflow to the vendor's uptime and response time. Asynchronous screening (Apex callout + Platform Event) decouples the workflows and handles vendor latency but requires the onboarding process to have a "pending screening" state and a mechanism to resume when results arrive. The choice depends on vendor SLA, onboarding volume, and whether agents need to take action on screening results before advancing.

**Standard Field History vs. Shield Field Audit Trail:**
Standard field history is zero-cost, requires no add-on, and is sufficient for audit obligations with an 18-month lookback. Shield Field Audit Trail satisfies obligations requiring longer retention but adds licensing cost. The tradeoff is entirely driven by the regulatory retention obligation, not by technical preference.

**Discovery Framework vs. Custom Screen Flow:**
The Discovery Framework (OmniScript + AssessmentQuestionResponse) produces audit-ready versioned responses natively and requires no custom development for versioning. A custom Screen Flow with custom objects can achieve similar results but requires custom versioning logic, more development effort, and produces less structured data. The Discovery Framework is strongly preferred when OmniStudio is licensed.

## Anti-Patterns

1. **Treating the KYC data model as the compliance control** — having `PartyIdentityVerification` and `PartyScreeningSummary` objects populated with data does not demonstrate compliance. The data must reflect real identity verification events and real screening results from a licensed vendor. Empty or self-populated screening records (where Salesforce writes its own "clear" result without calling an external vendor) are not compliant.

2. **Conflating Compliant Data Sharing with compliance documentation** — CDS governs who can see deal and client data within Salesforce. It has nothing to do with how compliance documentation is collected, structured, or preserved. Admins sometimes implement CDS sharing rules and consider the compliance work done. The two capabilities are orthogonal and both are required.

3. **Deferring audit trail configuration to post-go-live** — Field history tracking must be enabled before data changes occur; it cannot be retroactively applied to historical changes. If Field Audit Trail is not configured before the first KYC records are created, the early field-change history is lost permanently. Audit trail configuration must be part of pre-go-live setup, not a post-launch optimization.

## Official Sources Used

- Enable Know Your Customer for FSC — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_kyc_enable.htm
- FSC KYC Data Model (Developer Guide) — https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_kyc_data_model.htm
- Set Up AML Screening Integrations — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_aml_screening_setup.htm
- Field Audit Trail — https://help.salesforce.com/s/articleView?id=sf.field_audit_trail.htm
- Setup Audit Trail — https://help.salesforce.com/s/articleView?id=sf.admin_monitorsetup.htm
- Event Monitoring — https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_resources_event_log_files.htm
- Compliant Data Sharing in FSC — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_compliant_data_sharing.htm
- Named Credentials — https://help.salesforce.com/s/articleView?id=sf.named_credentials_about.htm
- Salesforce Well-Architected Overview — https://architect.salesforce.com/docs/architect/well-architected/guide/overview.html
- Salesforce Well-Architected: Trusted Pillar — https://architect.salesforce.com/docs/architect/well-architected/trusted/overview.html
