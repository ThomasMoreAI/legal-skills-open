---
name: gdpr-dpia-open-legal-products
title: GDPR DPIA
description: 'Assess whether a Data Protection Impact Assessment is required under GDPR Article 35 and draft it to the Article 35(7) structure: run the threshold test against the EDPB WP248 criteria, the Article 35(3) mandatory cases, and the national supervisory authority blacklist, then build the systematic description, the necessity and proportionality assessment, the risk assessment, and the mitigating measures, and decide whether Article 36 prior consultation applies. Use for profiling, CCTV, AI systems, large-scale monitoring, or any processing that may be high risk. The workflow drafts; the controller accepts residual risk and files.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/eu-gdpr-pack/gdpr-dpia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR DPIA

A DPIA is not a checkbox - it is a process for managing risk to the rights and freedoms of natural persons. This workflow runs the process and produces a draft; the residual-risk acceptance and the go/no-go decision belong to the controller.

## Step 1 - Is a DPIA required (Article 35(1) threshold)

A DPIA is mandatory where processing is likely to result in a high risk. Check three routes:

1. The supervisory authority's mandatory list (Article 35(4)) - each EU supervisory authority publishes a list of operations that always require a DPIA. Check the relevant national list.
2. The nine EDPB criteria (WP248 rev.01), with the rule of thumb that meeting two or more criteria means a DPIA is required: evaluation or scoring; automated decisions with significant effect (Article 22); systematic monitoring; sensitive or highly personal data; large-scale processing; matching or combining datasets; vulnerable data subjects (children, employees); innovative technology (AI, IoT); and processing that prevents exercising a right or using a service.
3. The explicit cases in Article 35(3): systematic and extensive evaluation including profiling, large-scale processing of special-category or criminal data, and large-scale systematic monitoring of publicly accessible areas.

Record the verdict as required, recommended, or not required, with a per-criterion justification. This is a screening, not a clearance - the controller documents the decision.

## Step 2 - DPIA structure (Article 35(7) minimum)

Draft the four pillars:

- (a) A systematic description of the processing and its purposes, including the legitimate interest where relied on.
- (b) An assessment of necessity and proportionality against the purposes: minimisation, legal basis, purpose limitation, retention, data subject rights, transfers.
- (c) A risk assessment to rights and freedoms: risk sources, confidentiality, integrity, and availability scenarios, likelihood times severity.
- (d) The measures envisaged to address the risks and demonstrate compliance, plus the residual risk.

Record the DPO's advice (Article 35(2)) and any consultation with data subjects (Article 35(9)).

## Step 3 - Prior consultation (Article 36)

If the residual risk remains high despite the measures, the controller must consult the supervisory authority before processing. Draft the consultation request to the scope of Article 36(3) - a human files it.

## Governance boundary

The workflow classifies the criteria, drafts the DPIA, and prepares the consultation request. A human approves the risk assessment, decides on deployment, signs, and files. The outward act of filing with the supervisory authority is never automatic.
