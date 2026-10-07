# LLM Anti-Patterns — Compliance Documentation Requirements

Common mistakes AI coding assistants make when generating or advising on compliance documentation requirements in Salesforce FSC. These patterns help the consuming agent self-check its own output.

## Anti-Pattern 1: Claiming FSC Natively Screens Against Watchlists or Sanctions Lists

**What the LLM generates:** "FSC's AML screening feature checks customer records against OFAC, UN, and EU sanctions lists automatically when you enable KYC. The `PartyScreeningSummary` object will be populated with the screening results after you turn on the feature."

**Why it happens:** The LLM sees `PartyScreeningSummary` and `PartyProfileRisk` in the FSC data model documentation and infers that Salesforce performs the screening. Training data conflates "FSC has objects for screening results" with "FSC performs screening." The word "native" in feature descriptions is often misinterpreted.

**Correct pattern:**

```
FSC provides data model objects (PartyScreeningSummary, PartyProfileRisk) to store
the results of AML screening — but FSC contains no watchlist data, no sanctions list,
and no screening engine. Every AML screening result must come from a third-party
vendor (e.g., Onfido, Refinitiv World-Check, LexisNexis) integrated via the
Set Up Integrations pattern. Without a third-party integration, PartyScreeningSummary
records will remain empty and no regulatory screening is occurring.
```

**Detection hint:** Any sentence containing "FSC natively screens," "Salesforce checks against OFAC/UN/EU," or "PartyScreeningSummary is automatically populated" is almost certainly wrong.

---

## Anti-Pattern 2: Omitting That Field Audit Trail Requires a Salesforce Shield Add-On

**What the LLM generates:** "Enable Field Audit Trail in Setup > Field History Tracking. This lets you retain field change history for up to 10 years on KYC objects, satisfying your 5-year regulatory retention requirement."

**Why it happens:** LLMs often conflate standard field history tracking (free, built-in, 18-month max) with Field Audit Trail (Shield add-on, 10-year max). The name "Field Audit Trail" sounds like a standard audit feature, and training data includes documentation for both features without always disambiguating the licensing requirement.

**Correct pattern:**

```
Field Audit Trail is a Salesforce Shield add-on and is NOT included in base FSC or
standard Salesforce editions. Standard field history tracking (available in all editions)
retains up to 18 months of history for up to 20 fields per object.

If regulatory obligations require retention beyond 18 months, Salesforce Shield must
be licensed separately. Field Audit Trail (Shield) supports up to 10 years of retention.
Confirm Shield licensing before designing compliance documentation retention architecture.
```

**Detection hint:** Any recommendation to use Field Audit Trail without explicitly noting the Shield licensing requirement is incomplete and potentially misleading.

---

## Anti-Pattern 3: Treating Setup Audit Trail as a Long-Term Audit Record

**What the LLM generates:** "To demonstrate no unauthorized configuration changes occurred during the audit period, point auditors to the Setup Audit Trail in Setup > Security > View Setup Audit Trail. This provides a complete history of all configuration changes."

**Why it happens:** Setup Audit Trail is a real, useful feature and is correctly described as tracking configuration changes. LLMs often do not mention the 180-day retention limit because it is a constraint rather than a feature and is frequently omitted from documentation excerpts used in training.

**Correct pattern:**

```
Setup Audit Trail retains entries for 180 days only. For annual regulatory audits
(which typically cover a 12-month lookback period), entries older than 180 days
will have already rolled off. Organizations must establish a recurring export
and archival process — querying the SetupAuditTrail object via SOQL and storing
results externally — to maintain a complete record beyond 180 days.

The 180-day limit is not extended by Salesforce Shield.
```

**Detection hint:** Any Setup Audit Trail recommendation that does not mention the 180-day retention limit or an external archival process is incomplete for compliance contexts.

---

## Anti-Pattern 4: Confusing Compliant Data Sharing with Compliance Documentation

**What the LLM generates:** "To meet compliance requirements for financial data access control, configure Compliant Data Sharing in FSC. This ensures that only authorized users can see client records, satisfying your KYC and AML documentation obligations."

**Why it happens:** "Compliance" appears in the name "Compliant Data Sharing" and in the phrase "compliance documentation," causing LLMs to conflate two unrelated FSC capabilities. Compliant Data Sharing (CDS) governs who sees which records via sharing rules. KYC and AML compliance documentation governs how identity and screening data is collected, stored, and preserved for audit. They are orthogonal.

**Correct pattern:**

```
Compliant Data Sharing (CDS) controls WHO can see deal and client data in FSC —
it is a record visibility and access control feature. It does not configure KYC data
collection, AML screening integration, or audit trail for regulatory documentation.

KYC/AML compliance documentation requires:
- FSC KYC objects (PartyIdentityVerification, IdentityDocument, PartyProfileRisk, PartyScreeningSummary)
- Discovery Framework for structured data collection
- Third-party AML screening integration
- Audit trail (Setup Audit Trail + Field Audit Trail + Event Monitoring)

These are separate admin tasks from CDS configuration.
```

**Detection hint:** Any answer to a KYC/AML documentation question that mentions Compliant Data Sharing as the solution is likely off-topic.

---

## Anti-Pattern 5: Using Per-User Authentication on Named Credentials for AML Screening Integrations

**What the LLM generates:** "Create a Named Credential for your AML vendor with Per-User OAuth authentication. This ensures each compliance officer's credentials are used for screening calls, providing better audit trail of who initiated each screening."

**Why it happens:** Per-User OAuth is a legitimate Named Credential configuration for interactive integrations where user-level access tokens are appropriate. LLMs apply this pattern broadly without recognizing that AML screening integrations run in non-interactive execution contexts (batch jobs, scheduled Apex, Platform Event triggers) where no user session exists.

**Correct pattern:**

```
AML screening integrations must use Named Principal (org-level) authentication
on Named Credentials. Per-User authentication requires an active user session to
resolve the OAuth token. Batch re-screening jobs, scheduled Apex, future methods,
and Platform Event subscribers run without a user session and will throw a
CalloutException if the Named Credential uses Per-User authentication.

Use Named Principal with a service account credential. For audit purposes, capture
the triggering user or process in the PartyScreeningSummary record payload, not
through the credential identity.
```

**Detection hint:** Any Named Credential configuration for an AML screening integration that specifies Per-User OAuth without explicitly noting the batch/scheduled context restriction is likely to cause production failures.

---

## Anti-Pattern 6: Assuming FSC Identity Verification Is a KYC Verification Control

**What the LLM generates:** "FSC Identity Verification handles your KYC requirements. Configure it in Setup to verify customer identities during the onboarding process. It checks government-issued IDs and confirms the customer's identity against Salesforce records."

**Why it happens:** "Identity Verification" in the FSC product name describes a contact-center feature for authenticating phone callers against stored identity records. LLMs conflate this caller authentication feature with KYC identity proofing (which involves verifying a new customer's identity against external government records or databases).

**Correct pattern:**

```
FSC Identity Verification is a contact-center feature that authenticates inbound
callers (existing customers) against identity records already stored in Salesforce.
It does NOT perform identity proofing for new customers, does NOT check government
ID databases, and does NOT satisfy KYC identity verification obligations.

KYC identity proofing for new clients requires:
1. Collecting identity data via the Discovery Framework OmniScript
2. Creating PartyIdentityVerification and IdentityDocument records
3. Integrating with a third-party identity verification vendor (e.g., Onfido) for
   document verification or biometric checks where required
```

**Detection hint:** Any response that cites "FSC Identity Verification" as satisfying KYC identity proofing requirements for new client onboarding is misdirected.
