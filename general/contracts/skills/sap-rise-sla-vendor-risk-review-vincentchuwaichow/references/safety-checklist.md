# Safety checklist — RISE with SAP SLA and Vendor Risk Review

Use before making any vendor risk or SLA recommendation, especially for findings that affect data residency, exit provisions, business continuity commitments, or security responsibility boundaries.

## Non-negotiables

- Do not access, connect to, or request access to any live SAP system, SAP contract management portal, SAP for Me, or signed contract repository. This skill reviews artifacts only.
- Do not accept or request SAP contract portal credentials, customer-specific contract identifiers, or confidential commercial pricing.
- Do not provide legal advice on contract terms. This skill provides advisory risk classification. Legal counsel must be engaged for binding contract interpretation or renegotiation strategy.
- Do not classify a contractual gap as low risk without first confirming it does not affect regulatory compliance (GDPR, SOX, HIPAA, local data protection law) or business continuity.
- Do not assert that SAP's published shared responsibility model matches the user's signed contract. Published models describe the standard; the signed contract governs. Always ask the user to confirm against their contract.
- Do not conflate RISE with SAP Private Cloud Edition responsibilities with RISE with SAP Public Cloud (S/4HANA Cloud Public Edition) responsibilities. The infrastructure and application responsibility split is materially different between these two models.
- Do not recommend withholding SLA credit claims without confirming the credit request window in the user's contract. Credit windows vary and missing the window forfeits the credit.

## What people get wrong

- **Assuming RISE with SAP means SAP manages everything**: RISE with SAP is a bundling model. SAP manages infrastructure and base application operations. The customer retains responsibility for configuration, authorizations, data quality, custom code, integration endpoints, and end-user access management.
- **Treating ISO 27001 certification as coverage for the customer's configuration**: SAP's ISO 27001 certification covers SAP's managed infrastructure and operations. It does not certify the customer's application configuration, custom code, or data handling practices within the system.
- **Assuming data residency equals data sovereignty**: A contractual data residency commitment (data stored in a specific region) does not automatically address data sovereignty requirements (which law governs the data). Both must be assessed independently.
- **Missing the maintenance window impact on effective availability**: A 99.5% availability SLA that permits planned maintenance of up to 10 hours per month may effectively deliver significantly less availability during business hours. Evaluate effective availability against business continuity requirements, not just the headline SLA percentage.
- **Treating exit provisions as final at contract signature**: Data export format, timeline, and cost are often negotiable at renewal or renegotiation. Flag weak exit provisions as remediation opportunities at next contract event.
- **Confusing SAP-provided audit reports with customer audit rights**: SAP typically provides SOC 2 Type II reports and ISO certifications. These are not the same as the customer's right to commission an independent audit of SAP's operations. Confirm which mechanism the contract provides.
- **Underestimating sub-processor risk**: SAP cloud services rely on third-party infrastructure providers (hyperscalers). The data processing agreement's sub-processor list and notification obligations for sub-processor changes are a GDPR compliance dependency. An outdated or absent sub-processor list is a regulatory risk.

## When to push back

- Push back when the user asks to assess SLA adequacy without providing the actual SLA schedule or availability commitment. Do not infer SLA terms from the product name alone.
- Push back when the user asks for a legal interpretation of contract language. Classify the risk and recommend legal counsel engagement.
- Push back when a request requires access to the signed contract and the user cannot provide relevant excerpts. State that the assessment cannot be completed without the contract evidence and ask the user to provide the relevant sections.
- Push back when the user asks to recommend contract renegotiation positions. Risk classification is in scope; negotiation strategy requires legal and commercial counsel.

## Evidence labels

- `documentation-based` — grounded in SAP Trust Center publications, SAP cloud service descriptions, RISE with SAP documentation, or SAP shared responsibility model
- `user-provided evidence` — contract excerpts, SLA schedules, order forms, or written descriptions of contractual obligations provided by the user
- `inference` — derived reasoning not directly confirmed by official SAP publications or user-provided contract text; must always be labeled as such
