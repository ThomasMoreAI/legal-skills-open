# MEASURE — Suggested Actions (GAI Profile)

*From NIST AI 600-1 (Generative AI Profile, July 2024), Section 3. Suggested Actions for the **MEASURE** function, grouped by AI RMF Subcategory. Each action is uniquely coded `MS-X.Y-NNN` and tagged with the GAI risks it addresses.*

Action ID format: `MS-X.Y-NNN` — function prefix, Category.Subcategory, sequential index.

## MEASURE 1.1 — Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented.

*AI Actor Tasks:* AI Development, Domain Experts, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-1.1-001` | Employ methods to trace the origin and modifications of digital content. | Information Integrity |
| `MS-1.1-002` | Integrate tools designed to analyze content provenance and detect data anomalies, verify the authenticity of digital signatures, and identify patterns associated with misinformation or manipulation. | Information Integrity |
| `MS-1.1-003` | Disaggregate evaluation metrics by demographic factors to identify any discrepancies in how content provenance mechanisms work across diverse populations. | Information Integrity; Harmful Bias and Homogenization |
| `MS-1.1-004` | Develop a suite of metrics to evaluate structured public feedback exercises informed by representative AI Actors. | Human-AI Configuration; Harmful Bias and Homogenization; CBRN Information or Capabilities |
| `MS-1.1-005` | Evaluate novel methods and technologies for the measurement of GAI-related risks including in content provenance, offensive cyber, and CBRN, while maintaining the models’ ability to produce valid, reliable, and factually accurate outputs. | Information Integrity; CBRN Information or Capabilities; Obscene, Degrading, and/or Abusive Content |
| `MS-1.1-006` | Implement continuous monitoring of GAI system impacts to identify whether GAI outputs are equitable across various sub-populations. Seek active and direct feedback from affected communities via structured feedback mechanisms or redteaming to monitor and improve outputs. | Harmful Bias and Homogenization |
| `MS-1.1-007` | Evaluate the quality and integrity of data used in training and the provenance of AI-generated content, for example by employing techniques like chaos engineering and seeking stakeholder feedback. | Information Integrity |
| `MS-1.1-008` | Define use cases, contexts of use, capabilities, and negative impacts where structured human feedback exercises, e.g., GAI red-teaming, would be most beneficial for GAI risk measurement and management based on the context of use. | Harmful Bias and Homogenization; CBRN Information or Capabilities |
| `MS-1.1-009` | Track and document risks or opportunities related to all GAI risks that cannot be measured quantitatively, including explanations as to why some risks cannot be measured (e.g., due to technological limitations, resource constraints, or trustworthy considerations). Include unmeasured risks in marginal risks. | Information Integrity |

## MEASURE 1.3 — Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI Actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance.

*AI Actor Tasks:* AI Deployment, AI Development, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-1.3-001` | Define relevant groups of interest (e.g., demographic groups, subject matter experts, experience with GAI technology) within the context of use as part of plans for gathering structured public feedback. | Human-AI Configuration; Harmful Bias and Homogenization; CBRN Information or Capabilities |
| `MS-1.3-002` | Engage in internal and external evaluations, GAI red-teaming, impact assessments, or other structured human feedback exercises in consultation with representative AI Actors with expertise and familiarity in the context of use, and/or who are representative of the populations associated with the context of use. | Human-AI Configuration; Harmful Bias and Homogenization; CBRN Information or Capabilities |
| `MS-1.3-003` | Verify those conducting structured human feedback exercises are not directly involved in system development tasks for the same GAI model. | Human-AI Configuration; Data Privacy |

## MEASURE 2.2 — Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population.

*AI Actor Tasks:* AI Development, Human Factors, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.2-001` | Assess and manage statistical biases related to GAI content provenance through techniques such as re-sampling, re-weighting, or adversarial training. | Information Integrity; Information Security; Harmful Bias and Homogenization |
| `MS-2.2-002` | Document how content provenance data is tracked and how that data interacts with privacy and security. Consider: Anonymizing data to protect the privacy of human subjects; Leveraging privacy output filters; Removing any personally identifiable information (PII) to prevent potential harm or misuse. | Data Privacy; Human AI Configuration; Information Integrity; Information Security; Dangerous, Violent, or Hateful Content |
| `MS-2.2-003` | Provide human subjects with options to withdraw participation or revoke their consent for present or future use of their data in GAI applications. | Data Privacy; Human-AI Configuration; Information Integrity |
| `MS-2.2-004` | Use techniques such as anonymization, differential privacy or other privacyenhancing technologies to minimize the risks associated with linking AI-generated content back to individual human subjects. | Data Privacy; Human-AI Configuration |

## MEASURE 2.3 — AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.

*AI Actor Tasks:* AI Deployment, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.3-001` | Consider baseline model performance on suites of benchmarks when selecting a model for fine tuning or enhancement with retrieval-augmented generation. | Information Security; Confabulation |
| `MS-2.3-002` | Evaluate claims of model capabilities using empirically validated methods. | Confabulation; Information Security |
| `MS-2.3-003` | Share results of pre-deployment testing with relevant GAI Actors, such as those with system release approval authority. | Human-AI Configuration |
| `MS-2.3-004` | Utilize a purpose-built testing environment such as NIST Dioptra to empirically evaluate GAI trustworthy characteristics. | CBRN Information or Capabilities; Data Privacy; Confabulation; Information Integrity; Information Security; Dangerous, Violent, or Hateful Content; Harmful Bias and Homogenization |

## MEASURE 2.5 — The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

*AI Actor Tasks:* Domain Experts, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.5-001` | Avoid extrapolating GAI system performance or capabilities from narrow, nonsystematic, and anecdotal assessments. | Human-AI Configuration; Confabulation |
| `MS-2.5-002` | Document the extent to which human domain knowledge is employed to improve GAI system performance, via, e.g., RLHF, fine-tuning, retrievalaugmented generation, content moderation, business rules. | Human-AI Configuration |
| `MS-2.5-003` | Review and verify sources and citations in GAI system outputs during predeployment risk measurement and ongoing monitoring activities. | Confabulation |
| `MS-2.5-004` | Track and document instances of anthropomorphization (e.g., human images, mentions of human feelings, cyborg imagery or motifs) in GAI system interfaces. | Human-AI Configuration |
| `MS-2.5-005` | Verify GAI system training data and TEVV data provenance, and that fine-tuning or retrieval-augmented generation data is grounded. | Information Integrity |
| `MS-2.5-006` | Regularly review security and safety guardrails, especially if the GAI system is being operated in novel circumstances. This includes reviewing reasons why the GAI system was initially assessed as being safe to deploy. | Information Security; Dangerous, Violent, or Hateful Content |

## MEASURE 2.6 — The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.6-001` | Assess adverse impacts, including health and wellbeing impacts for value chain or other AI Actors that are exposed to sexually explicit, offensive, or violent information during GAI training and maintenance. | Human-AI Configuration; Obscene, Degrading, and/or Abusive Content; Value Chain and Component Integration; Dangerous, Violent, or Hateful Content |
| `MS-2.6-002` | Assess existence or levels of harmful bias, intellectual property infringement, data privacy violations, obscenity, extremism, violence, or CBRN information in system training data. | Data Privacy; Intellectual Property; Obscene, Degrading, and/or Abusive Content; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content; CBRN Information or Capabilities |
| `MS-2.6-003` | Re-evaluate safety features of fine-tuned models when the negative risk exceeds organizational risk tolerance. | Dangerous, Violent, or Hateful Content |
| `MS-2.6-004` | Review GAI system outputs for validity and safety: Review generated code to assess risks that may arise from unreliable downstream decision-making. | Value Chain and Component Integration; Dangerous, Violent, or Hateful Content |
| `MS-2.6-005` | Verify that GAI system architecture can monitor outputs and performance, and handle, recover from, and repair errors when security anomalies, threats and impacts are detected. | Confabulation; Information Integrity; Information Security |
| `MS-2.6-006` | Verify that systems properly handle queries that may give rise to inappropriate, malicious, or illegal usage, including facilitating manipulation, extortion, targeted impersonation, cyber-attacks, and weapons creation. | CBRN Information or Capabilities; Information Security |
| `MS-2.6-007` | Regularly evaluate GAI system vulnerabilities to possible circumvention of safety measures. | CBRN Information or Capabilities; Information Security |

## MEASURE 2.7 — AI system security and resilience – as identified in the MAP function – are evaluated and documented.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.7-001` | Apply established security measures to: Assess likelihood and magnitude of vulnerabilities and threats such as backdoors, compromised dependencies, data breaches, eavesdropping, man-in-the-middle attacks, reverse engineering, autonomous agents, model theft or exposure of model weights, AI inference, bypass, extraction, and other baseline security concerns. | Data Privacy; Information Integrity; Information Security; Value Chain and Component Integration |
| `MS-2.7-002` | Benchmark GAI system security and resilience related to content provenance against industry standards and best practices. Compare GAI system security features and content provenance methods against industry state-of-the-art. | Information Integrity; Information Security |
| `MS-2.7-003` | Conduct user surveys to gather user satisfaction with the AI-generated content and user perceptions of content authenticity. Analyze user feedback to identify concerns and/or current literacy levels related to content provenance and understanding of labels on content. | Human-AI Configuration; Information Integrity |
| `MS-2.7-004` | Identify metrics that reflect the effectiveness of security measures, such as data provenance, the number of unauthorized access attempts, inference, bypass, extraction, penetrations, or provenance verification. | Information Integrity; Information Security |
| `MS-2.7-005` | Measure reliability of content authentication methods, such as watermarking, cryptographic signatures, digital fingerprints, as well as access controls, conformity assessment, and model integrity verification, which can help support the effective implementation of content provenance techniques. Evaluate the rate of false positives and false negatives in content provenance, as well as true positives and true negatives for verification. | Information Integrity |
| `MS-2.7-006` | Measure the rate at which recommendations from security checks and incidents are implemented. Assess how quickly the AI system can adapt and improve based on lessons learned from security incidents and feedback. | Information Integrity; Information Security |
| `MS-2.7-007` | Perform AI red-teaming to assess resilience against: Abuse to facilitate attacks on other systems (e.g., malicious code generation, enhanced phishing content), GAI attacks (e.g., prompt injection), ML attacks (e.g., adversarial examples/prompts, data poisoning, membership inference, model extraction, sponge examples). | Information Security; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content |
| `MS-2.7-008` | Verify fine-tuning does not compromise safety and security controls. | Information Integrity; Information Security; Dangerous, Violent, or Hateful Content |
| `MS-2.7-009` | Regularly assess and verify that security measures remain effective and have not been compromised. | Information Security |

## MEASURE 2.8 — Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.8-001` | Compile statistics on actual policy violations, take-down requests, and intellectual property infringement for organizational GAI systems: Analyze transparency reports across demographic groups, languages groups. | Intellectual Property; Harmful Bias and Homogenization |
| `MS-2.8-002` | Document the instructions given to data annotators or AI red-teamers. | Human-AI Configuration |
| `MS-2.8-003` | Use digital content transparency solutions to enable the documentation of each instance where content is generated, modified, or shared to provide a tamperproof history of the content, promote transparency, and enable traceability. Robust version control systems can also be applied to track changes across the AI lifecycle over time. | Information Integrity |
| `MS-2.8-004` | Verify adequacy of GAI system user instructions through user testing. | Human-AI Configuration |

## MEASURE 2.9 — The AI model is explained, validated, and documented, and AI system output is interpreted within its context – as identified in the MAP function – to inform responsible use and governance.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.9-001` | Apply and document ML explanation results such as: Analysis of embeddings, Counterfactual prompts, Gradient-based attributions, Model compression/surrogate models, Occlusion/term reduction. | Confabulation |
| `MS-2.9-002` | Document GAI model details including: Proposed use and organizational value; Assumptions and limitations, Data collection methodologies; Data provenance; Data quality; Model architecture (e.g., convolutional neural network, transformers, etc.); Optimization objectives; Training algorithms; RLHF approaches; Fine-tuning or retrieval-augmented generation approaches; Evaluation data; Ethical considerations; Legal and regulatory requirements. | Information Integrity; Harmful Bias and Homogenization |

## MEASURE 2.10 — Privacy risk of the AI system – as identified in the MAP function – is examined and documented.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.10-001` | Conduct AI red-teaming to assess issues such as: Outputting of training data samples, and subsequent reverse engineering, model extraction, and membership inference risks; Revealing biometric, confidential, copyrighted, licensed, patented, personal, proprietary, sensitive, or trade-marked information; Tracking or revealing location information of users or members of training datasets. | Human-AI Configuration; Information Integrity; Intellectual Property |
| `MS-2.10-002` | Engage directly with end-users and other stakeholders to understand their expectations and concerns regarding content provenance. Use this feedback to guide the design of provenance data-tracking techniques. | Human-AI Configuration; Information Integrity |
| `MS-2.10-003` | Verify deduplication of GAI training data samples, particularly regarding synthetic data. | Harmful Bias and Homogenization |

## MEASURE 2.11 — Fairness and bias – as identified in the MAP function – are evaluated and results are documented.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.11-001` | Apply use-case appropriate benchmarks (e.g., Bias Benchmark Questions, Real Hateful or Harmful Prompts, Winogender Schemas15) to quantify systemic bias, stereotyping, denigration, and hateful content in GAI system outputs; Document assumptions and limitations of benchmarks, including any actual or possible training/test data cross contamination, relative to in-context deployment environment. | Harmful Bias and Homogenization |
| `MS-2.11-002` | Conduct fairness assessments to measure systemic bias. Measure GAI system performance across demographic groups and subgroups, addressing both quality of service and any allocation of services and resources. Quantify harms using: field testing with sub-group populations to determine likelihood of exposure to generated content exhibiting harmful bias, AI red-teaming with counterfactual and low-context (e.g., “leader,” “bad guys”) prompts. For ML pipelines or business processes with categorical or numeric outcomes that rely on GAI, apply general fairness metrics (e.g., demographic parity, equalized odds, equal opportunity, statistical hypothesis tests), to the pipeline or business outcome where appropriate; Custom, context-specific metrics developed in collaboration with domain experts and affected communities; Measurements of the prevalence of denigration in generated content in deployment (e.g., subsampling a fraction of traffic and manually annotating denigrating content). | Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content |
| `MS-2.11-003` | Identify the classes of individuals, groups, or environmental ecosystems which might be impacted by GAI systems through direct engagement with potentially impacted communities. | Environmental; Harmful Bias and Homogenization |
| `MS-2.11-004` | Review, document, and measure sources of bias in GAI training and TEVV data: Differences in distributions of outcomes across and within groups, including intersecting groups; Completeness, representativeness, and balance of data sources; demographic group and subgroup coverage in GAI system training data; Forms of latent systemic bias in images, text, audio, embeddings, or other complex or unstructured data; Input data features that may serve as proxies for demographic group membership (i.e., image metadata, language dialect) or otherwise give rise to emergent bias within GAI systems; The extent to which the digital divide may negatively impact representativeness in GAI system training and TEVV data; Filtering of hate speech or content in GAI system training data; Prevalence of GAI-generated data in GAI system training data. | Harmful Bias and Homogenization |
| `MS-2.11-005` | Assess the proportion of synthetic to non-synthetic training data and verify training data is not overly homogenous or GAI-produced to mitigate concerns of model collapse. | Harmful Bias and Homogenization |

## MEASURE 2.12 — Environmental impact and sustainability of AI model training and management activities – as identified in the MAP function – are assessed and documented.

*AI Actor Tasks:* AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.12-001` | Assess safety to physical environments when deploying GAI systems. | Dangerous, Violent, or Hateful Content |
| `MS-2.12-002` | Document anticipated environmental impacts of model development, maintenance, and deployment in product design decisions. | Environmental |
| `MS-2.12-003` | Measure or estimate environmental impacts (e.g., energy and water consumption) for training, fine tuning, and deploying models: Verify tradeoffs between resources used at inference time versus additional resources required at training time. | Environmental |
| `MS-2.12-004` | Verify effectiveness of carbon capture or offset programs for GAI training and applications, and address green-washing concerns. | Environmental |

## MEASURE 2.13 — Effectiveness of the employed TEVV metrics and processes in the MEASURE function are evaluated and documented.

*AI Actor Tasks:* AI Deployment, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-2.13-001` | Create measurement error models for pre-deployment metrics to demonstrate construct validity for each metric (i.e., does the metric effectively operationalize the desired concept): Measure or estimate, and document, biases or statistical variance in applied metrics or structured human feedback processes; Leverage domain expertise when modeling complex societal constructs such as hateful content. | Confabulation; Information Integrity; Harmful Bias and Homogenization |

## MEASURE 3.2 — Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available.

*AI Actor Tasks:* AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-3.2-001` | Establish processes for identifying emergent GAI system risks including consulting with external AI Actors. | Human-AI Configuration; Confabulation |

## MEASURE 3.3 — Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics.

*AI Actor Tasks:* AI Deployment, Affected Individuals and Communities, End-Users, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-3.3-001` | Conduct impact assessments on how AI-generated content might affect different social, economic, and cultural groups. | Harmful Bias and Homogenization |
| `MS-3.3-002` | Conduct studies to understand how end users perceive and interact with GAI content and accompanying content provenance within context of use. Assess whether the content aligns with their expectations and how they may act upon the information presented. | Human-AI Configuration; Information Integrity |
| `MS-3.3-003` | Evaluate potential biases and stereotypes that could emerge from the AIgenerated content using appropriate methodologies including computational testing methods as well as evaluating structured feedback input. | Harmful Bias and Homogenization |
| `MS-3.3-004` | Provide input for training materials about the capabilities and limitations of GAI systems related to digital content transparency for AI Actors, other professionals, and the public about the societal impacts of AI and the role of diverse and inclusive content generation. | Human-AI Configuration; Information Integrity; Harmful Bias and Homogenization |
| `MS-3.3-005` | Record and integrate structured feedback about content provenance from operators, users, and potentially impacted communities through the use of methods such as user research studies, focus groups, or community forums. Actively seek feedback on generated content quality and potential biases. Assess the general awareness among end users and impacted communities about the availability of these feedback channels. | Human-AI Configuration; Information Integrity; Harmful Bias and Homogenization |

## MEASURE 4.2 — Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI Actors to validate whether the system is performing consistently as intended. Results are documented.

*AI Actor Tasks:* AI Deployment, Domain Experts, End-Users, Operation and Monitoring, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MS-4.2-001` | Conduct adversarial testing at a regular cadence to map and measure GAI risks, including tests to address attempts to deceive or manipulate the application of provenance techniques or other misuses. Identify vulnerabilities and understand potential misuse scenarios and unintended outputs. | Information Integrity; Information Security |
| `MS-4.2-002` | Evaluate GAI system performance in real-world scenarios to observe its behavior in practical environments and reveal issues that might not surface in controlled and optimized testing environments. | Human-AI Configuration; Confabulation; Information Security |
| `MS-4.2-003` | Implement interpretability and explainability methods to evaluate GAI system decisions and verify alignment with intended purpose. | Information Integrity; Harmful Bias and Homogenization |
| `MS-4.2-004` | Monitor and document instances where human operators or other systems override the GAI's decisions. Evaluate these cases to understand if the overrides are linked to issues related to content provenance. | Information Integrity |
| `MS-4.2-005` | Verify and document the incorporation of results of structured public feedback exercises into design, implementation, deployment approval (“go”/“no-go” decisions), monitoring, and decommission decisions. | Human-AI Configuration; Information Security |
