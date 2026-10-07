# Examples — Compliance Documentation Requirements

## Example 1: KYC Workflow for New Client Onboarding Using Discovery Framework

**Context:** A wealth management firm using FSC wants to replace paper-based KYC forms with a structured, audit-ready digital collection workflow. Each new individual client must have identity data, document details, and beneficial ownership information collected and versioned before an account can be opened.

**Problem:** Without a structured collection mechanism, agents enter identity data in free-text custom fields. There is no version history of what was collected, no capture of who submitted the data, and no structured export for regulatory audit. When auditors request evidence of the KYC collection event for a specific client, the firm cannot produce a timestamped record of what was asked and what was answered.

**Solution:**

1. Enable Know Your Customer in FSC Setup (Financial Services Cloud Settings > Enable Know Your Customer).
2. Define `AssessmentQuestionSet` records for each section of the KYC questionnaire: identity data, identity document details, PEP/sanctions self-declaration, and beneficial ownership.
3. Build an OmniScript that guides the agent through each section. Map each question to an `AssessmentQuestion` record.
4. Use a DataRaptor Turbo Action at the end of each section to save `AssessmentQuestionResponse` records. Each response record captures: question, answer, submitting user, submission timestamp, and session identifier.
5. On OmniScript completion, an Integration Procedure creates:
   - `PartyIdentityVerification` with `VerificationStatus = Verified`, `VerificationDate = today`, `VerificationType = GovernmentID`
   - `IdentityDocument` with `DocumentType`, `IssuingAuthority`, `IssueDate`, and `ExpiryDate` populated from the questionnaire responses
6. A subsequent step triggers the AML screening integration (Pattern B in SKILL.md), which creates a `PartyScreeningSummary` record when the vendor responds.

**Why it works:** Each `AssessmentQuestionResponse` record is immutable after creation and carries the submitting user and timestamp. When a new periodic review cycle occurs, a new set of responses is created — the prior responses are not overwritten. This produces a version history of every KYC collection event, meeting the documentation requirements for regulatory audit. Auditors can query `AssessmentQuestionResponse` records filtered by individual and date range to reconstruct exactly what was collected and when.

---

## Example 2: AML Screening Integration Setup with Onfido via AppExchange

**Context:** An FSC org has selected Onfido as its KYC/AML screening vendor. Onfido's AppExchange managed package has been installed. The admin team must configure the integration so that screening is triggered from the onboarding OmniScript and results are written to `PartyScreeningSummary` and `PartyProfileRisk`.

**Problem:** Without proper Named Credential configuration, developers hardcode the Onfido API token in Apex code or a Custom Setting. This exposes the token in metadata exports and fails security review. Additionally, if the credential is configured as Per-User OAuth, batch re-screening jobs fail silently because there is no active user session.

**Solution:**

1. In Setup, navigate to Security > External Credentials. Create a new External Credential:
   - Label: `OnfidoAPI`
   - Authentication Protocol: Custom (for API token-based auth)
   - Add a Principal: set Principal Type to Named Principal (org-level)
   - Add a Header parameter `Authorization` with value `Token token=<onfido_api_token>` (stored as a Secret)
2. Create a Named Credential:
   - Label: `Onfido_KYC`
   - URL: `https://api.onfido.com/v3.6`
   - External Credential: `OnfidoAPI`
3. In a Permission Set assigned to the integration user (not All Users), grant access to the `OnfidoAPI` External Credential principal.
4. In the OmniStudio Integration Procedure that handles screening, configure the HTTP Action element to use Named Credential `Onfido_KYC`. Never hardcode the URL or token.
5. Map the Onfido response to `PartyScreeningSummary` fields:
   - `ScreeningStatus`: map from Onfido `result` field (clear / consider → Clear / Potential Match)
   - `VendorCaseReference`: map from Onfido `check_id`
   - `ScreeningDate`: capture `DateTime.now()` at response time
6. After creating `PartyScreeningSummary`, update `PartyProfileRisk.RiskCategory` based on the screening result per the agreed risk tier rules.

**Why it works:** The Named Credential with Named Principal authentication encrypts the API token so it is never readable from the UI, Apex, or a metadata export. The Named Principal type ensures the credential resolves in all execution contexts — interactive, batch, and scheduled — without requiring an active user session.

---

## Anti-Pattern: Relying on Standard Field History Tracking for Long-Term KYC Audit Trail

**What practitioners do:** Enable standard field history tracking on `PartyIdentityVerification` and `PartyProfileRisk` and assume this satisfies regulatory retention requirements of 5+ years.

**What goes wrong:** Standard field history is retained for a maximum of 18 months and is limited to 20 tracked fields per object. After 18 months, historical field values are automatically deleted. For an AML compliance audit covering a 5-year lookback period, the field history for changes made more than 18 months ago will not exist. This creates a compliance gap that may not be discovered until an audit request arrives.

**Correct approach:** If regulatory obligations require field-level change history beyond 18 months, license Salesforce Shield and configure Field Audit Trail Policy for the relevant fields on KYC objects. Field Audit Trail supports retention of up to 10 years. Document the Shield licensing requirement explicitly in the compliance architecture so it is not cut during budget reviews.
