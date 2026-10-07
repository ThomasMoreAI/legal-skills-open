# Compliance Documentation Requirements — Work Template

Use this template when setting up or auditing compliance documentation workflows in Salesforce FSC. Covers KYC data collection, AML screening integration setup, and audit trail configuration for regulatory readiness.

## Scope

**Skill:** `compliance-documentation-requirements`

**Request summary:** (fill in what the practitioner or stakeholder asked for)

---

## Prerequisites Confirmed

Before starting work, record answers to these questions:

- **FSC enabled and version:** (e.g., Spring '25, FSC standard / FSC Plus)
- **OmniStudio licensed?** Yes / No — (required for Discovery Framework)
- **Salesforce Shield licensed?** Yes / No — (required for Field Audit Trail and Event Monitoring)
- **AML screening vendor selected?** Yes / No — if Yes, name: ________________
- **Regulatory obligations in scope:** (e.g., BSA/FinCEN 5-year retention, FATF, EU AMLD)
- **Required field-level retention period:** _______ months/years
- **Individual record linked to all Contacts?** Confirmed / Not confirmed / Unknown

---

## Context Gathered

- **Setting / configuration:** (current state of KYC feature, existing data model, existing integrations)
- **Known constraints:** (Shield not yet licensed, OmniStudio not available, vendor API not yet signed off, etc.)
- **Failure modes to watch for:** (missing Individual records, Per-User Named Credential, standard history only)

---

## Approach

(Which pattern from SKILL.md applies? Check one or both)

- [ ] Pattern A: KYC Data Collection via Discovery Framework OmniScript
- [ ] Pattern B: AML Screening Integration Setup via Named Credential
- [ ] Other: ______________

Rationale: (why does this pattern apply to this request?)

---

## KYC Data Model Setup Checklist

- [ ] FSC Know Your Customer feature enabled in Setup
- [ ] `PartyIdentityVerification` object accessible; required fields confirmed
- [ ] `IdentityDocument` object accessible; DocumentType picklist values configured
- [ ] `PartyProfileRisk` object accessible; RiskCategory picklist values match regulatory risk tier definitions
- [ ] `PartyScreeningSummary` object accessible; ScreeningStatus picklist values aligned with vendor response codes
- [ ] All KYC objects linked to `Individual` (not Contact directly) — Individual-Contact link verified
- [ ] Page layouts and record types configured for agent-facing KYC views

---

## Discovery Framework / Data Collection Checklist

- [ ] `AssessmentQuestionSet` records defined for each questionnaire section
- [ ] `AssessmentQuestion` records created with appropriate data types
- [ ] OmniScript built and tested for guided data collection
- [ ] DataRaptor Turbo Action saves `AssessmentQuestionResponse` records with user + timestamp
- [ ] Prior response versions are not overwritten on re-submission (new records created per cycle)
- [ ] On completion, `PartyIdentityVerification` and `IdentityDocument` records created correctly

---

## AML Screening Integration Checklist

- [ ] External Credential created with Named Principal authentication
- [ ] Named Credential created referencing External Credential; URL correct
- [ ] Permission Set grants access to External Credential principal (not All Users)
- [ ] Integration Procedure / Apex callout uses Named Credential label — no hardcoded URL or token
- [ ] `PartyScreeningSummary` fields mapped: ScreeningStatus, VendorCaseReference, ScreeningDate
- [ ] `PartyProfileRisk.RiskCategory` updated after screening result received
- [ ] Error handling implemented: vendor downtime surfaces a Case or alert, does not silently skip
- [ ] Tested in sandbox with a real vendor API response

---

## Audit Trail Configuration Checklist

- [ ] Field history tracking enabled on key fields (PartyIdentityVerification, PartyProfileRisk, PartyScreeningSummary)
- [ ] If Shield licensed: Field Audit Trail Policy configured for fields requiring >18-month retention
- [ ] Setup Audit Trail export and archival process documented and scheduled (interval < 180 days)
- [ ] If Shield licensed: Event Monitoring log file retrieval process established
- [ ] Retention period coverage documented per obligation (field history vs. Shield vs. external archive)

---

## Regulatory Documentation Checklist

| Regulatory Obligation | Salesforce Artifact | Coverage Confirmed? |
|---|---|---|
| Identity collected and verified | PartyIdentityVerification + IdentityDocument records | [ ] |
| AML screening performed | PartyScreeningSummary with vendor case reference | [ ] |
| Customer risk rating assigned | PartyProfileRisk with RiskCategory, RiskReason, RiskReviewDate | [ ] |
| KYC collection timestamped and attributed | AssessmentQuestionResponse with user + timestamp | [ ] |
| Configuration change history | Setup Audit Trail + external archival | [ ] |
| Field-level change history (long-term) | Field Audit Trail (Shield) if retention > 18 months | [ ] |
| Data access history | Event Monitoring (Shield) | [ ] |

---

## Notes

(Record any deviations from the standard patterns, decisions made, and rationale.)

---

## Official Sources Referenced

- Enable Know Your Customer for FSC — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_kyc_enable.htm
- FSC KYC Data Model — https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_kyc_data_model.htm
- Set Up AML Screening Integrations — https://help.salesforce.com/s/articleView?id=sf.fsc_admin_aml_screening_setup.htm
- Field Audit Trail — https://help.salesforce.com/s/articleView?id=sf.field_audit_trail.htm
- Named Credentials — https://help.salesforce.com/s/articleView?id=sf.named_credentials_about.htm
