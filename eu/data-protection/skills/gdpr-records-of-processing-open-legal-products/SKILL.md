---
name: gdpr-records-of-processing-open-legal-products
title: GDPR Records of Processing
description: 'Build and validate the records of processing activities (RoPA) required by GDPR Article 30: the controller register under Article 30(1) and the processor register under Article 30(2), enforcing every mandatory field - purposes, categories of data subjects and data, recipients, third-country transfers and safeguards, erasure time limits, and security measures. Flags activities that trigger a DPIA and tests the narrow Article 30(5) exemption. Use when creating a RoPA from scratch, auditing an existing register for gaps, or preparing accountability evidence for a supervisory authority. Complements the DPA review workflows, which cover the processor contract itself.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/eu-gdpr-pack/gdpr-records-of-processing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Records of Processing

The RoPA is a living accountability document, and its required content can be checked mechanically against Article 30. This workflow builds or validates the register and reports gaps; ownership of the register and every filing decision stay with the controller.

## Controller register (Article 30(1))

For each processing activity, the register must record:

- the name and contact details of the controller, any joint controller, the representative, and the DPO,
- the purposes of the processing,
- the categories of data subjects and the categories of personal data,
- the categories of recipients, including recipients in third countries or international organisations,
- transfers to third countries with the identification of the country and the documentation of safeguards (Chapter V),
- the envisaged erasure time limits for each category of data,
- a general description of the technical and organisational security measures (Article 32).

Validate completeness field by field. A missing field is a gap to report, not a value to guess.

## Processor register (Article 30(2))

The processor's register has its own mandatory field list, validated field by field like the controller's:

- the name and contact details of the processor or processors and of each controller on behalf of which the processor is acting, and, where applicable, of the controller's or the processor's representative and the DPO (Article 30(2)(a)),
- the categories of processing carried out on behalf of each controller,
- transfers to third countries or international organisations, with the identification of the country and, for transfers under the second subparagraph of Article 49(1), the documentation of suitable safeguards,
- a general description of the technical and organisational security measures (Article 32(1)).

A register that lists controllers and sub-processors but omits contact details, the representative, or the DPO is incomplete - report the gap, do not mark the activity complete.

## Cross-checks

- Flag every activity whose description meets a DPIA trigger (profiling, large-scale special-category data, systematic monitoring) so it can be taken through a DPIA.
- Test the Article 30(5) exemption honestly, disqualifier by disqualifier - any one of them removes it. The exemption is unavailable if the organisation employs 250 persons or more; and regardless of size, if the processing is likely to result in a risk to rights and freedoms, is not occasional, includes special categories of data under Article 9(1), or includes personal data relating to criminal convictions and offences under Article 10. In practice it rarely applies - most organisations process employee or customer data regularly.
- Where the register reveals a processor without a compliant processing contract, note it and route the contract itself to a DPA review workflow.

## Output

A draft register (or a gap report against an existing one) with each activity marked complete or listing its missing fields, plus the DPIA flags and contract flags.

## Governance boundary

The workflow builds and validates the register and maps gaps to the article. A human approves the content and owns the register. Nothing is filed or signed automatically.
