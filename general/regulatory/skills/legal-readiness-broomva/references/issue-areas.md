# Jurisdiction-neutral legal-readiness issue areas

## Contents

- [Source hierarchy](#source-hierarchy)
- [Applicability predicates](#applicability-predicates)
- [Issue areas](#issue-areas)
- [Closure rule](#closure-rule)
- [Official examples](#official-examples)

## Source hierarchy

Use sources in this order:

1. Current binding legislation, regulation, and holdings from competent courts.
2. Nonbinding regulator guidance and standards, labeled as such rather than
   silently converted into obligations.
3. Executed contracts, policies, registry receipts, dashboard exports, invoices,
   audit reports, and operational records for the actual project.
4. Repository and live interaction evidence.
5. Reputable secondary analysis to find issues—not to close them.
6. Vendor marketing and model memory only as leads.

Record retrieval dates. Recheck law, vendor terms, prices, and technical
standards because they change.

Do not put legal advice or privileged/confidential communications in a
repository manifest. Use an authorized sanitized conclusion plus a private
record ID and digest; ask counsel how privilege must be preserved.

## Applicability predicates

Never declare an obligation universal until these are known:

- operator entity/type/location and where decisions are made;
- user/customer residence and whether the service targets or monitors them;
- B2C/B2B/public-sector posture and adhesion/negotiated contract shape;
- web/native-store/API/marketplace/payment channels;
- data categories, minors/sensitive data, controller/processor/recipient roles;
- AI provider/deployer/model/content role and whether people interact with AI;
- where processing, vendors, and recipients are located;
- pricing currency, taxes, recurring billing, credit/usage mechanics;
- industry-specific regulated activity;
- supported/excluded territories and whether geofencing is actually enforced.

## Issue areas

| Area | Evidence before closure |
|---|---|
| Operator and authority | Registry/tax facts, exact public identity, addresses/contact channels, authority to contract. |
| Terms and assent | Applicable language, conspicuous action, version/hash receipt, amendment/reacceptance, mandatory-rights savings. |
| Privacy and authorization | Data map, roles, purposes/bases or authorization, recipients, transfers, retention, rights and withdrawal. |
| Children/minors | Enforced age posture or validated guardian/best-interests flow. |
| AI transparency and safety | Role/use classification, interaction/content disclosures, risk assessment, human escalation where needed. |
| Product and commercial claims | Exact match across marketing, docs, configuration, runtime, invoices, support and sales materials. |
| Payments and renewals | Merchant, all-in price/currency/tax, renewal, refund/remedy, consent, receipt, cancellation, webhook integrity. |
| Vendor/subprocessor/transfer | Actual provider/route inventory, roles, locations, contract/transfer basis, retention/training/ZDR settings and tests. |
| Security and incident response | Threat model, access control, tenant isolation, storage exposure, logs, incident owners/clocks/reporting/exercises. |
| Retention and rights | Record-level schedule, validated request workflow, backup/legal-hold exceptions, provider propagation and receipts. |
| IP and open source | Hosted-vs-OSS boundary, dependency licenses, contributor chain of title, AI input/output/provider terms. |
| Accessibility/marketing/export | Applicability decision and implemented process—or explicit not-audited gate. |
| Insurance/MSA/DPA/SLA | Executed, supportable, scoped documents/policies; never infer from a template or recommendation. |
| Tax/registrations | Qualified tax/registry determination and filed/current receipts. |

## Closure rule

An issue is closed only when the record contains:

1. applicable rule and source;
2. verified factual predicate;
3. implemented control;
4. operating/interaction evidence;
5. retained receipt and owner;
6. counsel or specialist validation where judgment is material.

If one element is unavailable, use `qualified`, `unverified`, `partial`, or
`blocked-external`. Do not substitute a page, clause, vendor, or scanner result.

## Official examples

These illustrate the method; they are not a universal checklist:

- The U.S. FTC requires a reasonable basis before objective advertising claims
  are disseminated: https://www.ftc.gov/legal-library/browse/ftc-policy-statement-regarding-advertising-substantiation
- GDPR accountability requires the controller to be able to demonstrate
  compliance, and Article 24 requires appropriate measures based on processing
  risk: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Colombia's SIC explains that silence, pre-checked boxes, and inaction do not
  constitute valid authorization: https://sedeelectronica.sic.gov.co/publicaciones/boletin-juridico/boletin/el-silencio-las-casillas-premarcadas-por-defecto-y-la-inaccion-no-constituyen-el-consentimiento-conforme-con
- RFC 9116 defines the `security.txt` format and scope; its existence is a
  disclosure mechanism, not a security certification: https://www.rfc-editor.org/rfc/rfc9116.html
