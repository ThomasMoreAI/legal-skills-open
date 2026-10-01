# California Privacy Choices

**Version:** [VERSION]  
**Effective date:** [EFFECTIVE_DATE]

## 1. Assessed Practices

[CALIFORNIA_DISCLOSURE]

The final page must use the statutory terminology that matches the company's
actual practices. Do not say “we do not sell” merely because no money changes
hands; do not say “we share” merely because any vendor receives data. Review the
contracts, purposes, and legal definitions.

## 2. Do Not Sell or Share My Personal Information

If [COMPANY_NAME] sells personal information or shares it for cross-context
behavioral advertising as those terms apply to the business, provide the
frictionless opt-out method here:

- Opt-out page or control: [[REVIEW: INSERT CONTROL OR URL]]
- Privacy settings: [[REVIEW: INSERT ACCOUNT-LEVEL CONTROL]]
- Assistance/contact: [CCPA_AGENT_EMAIL]

The opt-out must be available without requiring an account. Do not require more
information than reasonably necessary to apply the preference. State how the
preference applies to the browser/device and, when the user is known, the
account. Explain any lawful request to opt back in and any waiting period before
asking again.

[[REVIEW: EXPLAIN THE ACTUAL SALE/SHARING CATEGORIES, RECIPIENT CATEGORIES, LOOK-BACK PERIOD, AND HOW THE OPT-OUT IS APPLIED]]

## 3. Global Privacy Control

Where required, [COMPANY_NAME] treats a recognized Global Privacy Control (GPC)
signal as a valid request to opt out of sale or sharing for the browser or
device and, when known, the associated consumer.

[[REVIEW: KEEP THE PRECEDING SENTENCE ONLY AFTER TESTING GPC BEFORE TAGS LOAD, AFTER LOGIN, ACROSS SUBDOMAINS, WITH CONSENT/CMP AND AD VENDORS, AND IN SERVER-SIDE PROCESSING. OTHERWISE REPLACE IT WITH AN ACCURATE IMPLEMENTATION STATUS AND FIX THE PRODUCT BEFORE CLAIMING COMPLIANCE]]

A user should not need to submit a second request to make an applicable GPC
signal effective.

## 4. Limit the Use and Disclosure of Sensitive Personal Information

[[REVIEW: ASSESS WHETHER THE COMPANY USES OR DISCLOSES SENSITIVE PERSONAL INFORMATION FOR PURPOSES THAT TRIGGER A LIMIT-USE RIGHT. IF YES, INSERT THE DEPLOYED CONTROL AND REQUIRED DISCLOSURES. IF NO, REMOVE THIS SECTION OR STATE THE ASSESSED PRACTICE ACCURATELY]]

## 5. Other California Requests

Rights may include access/know, deletion, correction, portability, and appeal or
other mechanisms depending on the applicable law and facts.

Rights-request method: [RIGHTS_REQUEST_PROCESS]

Explain:

- available request methods;
- what information is needed for the request type;
- identity and authorized-agent verification proportionate to risk;
- response and appeal process;
- circumstances in which a request may be denied or limited;
- non-discrimination protections;
- accessibility and language assistance.

Do not use the identity-verification process for access or deletion as an
unnecessary barrier to an opt-out request.

## 6. Authorized Agents

[[REVIEW: DESCRIBE THE ACTUAL AUTHORIZED-AGENT PROCESS AND THE EVIDENCE REQUIRED UNDER CURRENT RULES. REQUEST ONLY WHAT IS NECESSARY TO VERIFY AUTHORITY AND APPLY THE REQUEST]]

## 7. Notice at Collection and Full Privacy Notice

The point-of-collection notice and full privacy notice must describe the
categories of personal information, purposes, retention, and applicable sale,
sharing, and sensitive-data practices before or at collection.

- Privacy notice: [DOMAIN]/privacy
- Notice at collection: [[REVIEW: INSERT COLLECTION LINKS]]

## 8. Contact

- California/privacy email: [CCPA_AGENT_EMAIL]
- General privacy email: [CONTACT_EMAIL]
- Postal address: [COMPANY_ADDRESS]
- Rights-request method: [RIGHTS_REQUEST_PROCESS]

[[REVIEW: ADD CURRENT CALIFORNIA PRIVACY PROTECTION AGENCY INFORMATION OR OTHER REQUIRED CONTACT/COMPLAINT DETAILS FROM AN OFFICIAL SOURCE]]

## 9. Implementation Validation

Before publication, retain evidence that:

- opt-out controls work before and after login;
- GPC is recognized where required;
- downstream vendors and server-side systems receive and honor the preference;
- the preference is not overridden by a consent banner or account change;
- the company does not require unnecessary verification or account creation;
- notices, contracts, data maps, and product behavior use consistent categories;
- accessibility, language, recordkeeping, and staff procedures are operational.
