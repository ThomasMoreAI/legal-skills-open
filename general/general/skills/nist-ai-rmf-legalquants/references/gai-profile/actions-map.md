# MAP — Suggested Actions (GAI Profile)

*From NIST AI 600-1 (Generative AI Profile, July 2024), Section 3. Suggested Actions for the **MAP** function, grouped by AI RMF Subcategory. Each action is uniquely coded `MP-X.Y-NNN` and tagged with the GAI risks it addresses.*

Action ID format: `MP-X.Y-NNN` — function prefix, Category.Subcategory, sequential index.

## MAP 1.1 — Intended purposes, potentially beneficial uses, context specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics.

*AI Actor Tasks:* AI Deployment

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-1.1-001` | When identifying intended purposes, consider factors such as internal vs. external use, narrow vs. broad application scope, fine-tuning, and varieties of data sources (e.g., grounding, retrieval-augmented generation). | Data Privacy; Intellectual Property |
| `MP-1.1-002` | Determine and document the expected and acceptable GAI system context of use in collaboration with socio-cultural and other domain experts, by assessing: Assumptions and limitations; Direct value to the organization; Intended operational environment and observed usage patterns; Potential positive and negative impacts to individuals, public safety, groups, communities, organizations, democratic institutions, and the physical environment; Social norms and expectations. | Harmful Bias and Homogenization |
| `MP-1.1-003` | Document risk measurement plans to address identified risks. Plans may include, as applicable: Individual and group cognitive biases (e.g., confirmation bias, funding bias, groupthink) for AI Actors involved in the design, implementation, and use of GAI systems; Known past GAI system incidents and failure modes; In-context use and foreseeable misuse, abuse, and off-label use; Over reliance on quantitative metrics and methodologies without sufficient awareness of their limitations in the context(s) of use; Standard measurement and structured human feedback approaches; Anticipated human-AI configurations. | Human-AI Configuration; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content |
| `MP-1.1-004` | Identify and document foreseeable illegal uses or applications of the GAI system that surpass organizational risk tolerances. | CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Obscene, Degrading, and/or Abusive Content |

## MAP 1.2 — Interdisciplinary AI Actors, competencies, skills, and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized.

*AI Actor Tasks:* AI Deployment

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-1.2-001` | Establish and empower interdisciplinary teams that reflect a wide range of capabilities, competencies, demographic groups, domain expertise, educational backgrounds, lived experiences, professions, and skills across the enterprise to inform and conduct risk measurement and management functions. | Human-AI Configuration; Harmful Bias and Homogenization |
| `MP-1.2-002` | Verify that data or benchmarks used in risk measurement, and users, participants, or subjects involved in structured GAI public feedback exercises are representative of diverse in-context user populations. | Human-AI Configuration; Harmful Bias and Homogenization |

## MAP 2.1 — The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders).

*AI Actor Tasks:* TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-2.1-001` | Establish known assumptions and practices for determining data origin and content lineage, for documentation and evaluation purposes. | Information Integrity |
| `MP-2.1-002` | Institute test and evaluation for data and content flows within the GAI system, including but not limited to, original data sources, data transformations, and decision-making criteria. | Intellectual Property; Data Privacy |

## MAP 2.2 — Information about the AI system’s knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI Actors when making decisions and taking subsequent actions.

*AI Actor Tasks:* End Users

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-2.2-001` | Identify and document how the system relies on upstream data sources, including for content provenance, and if it serves as an upstream dependency for other systems. | Information Integrity; Value Chain and Component Integration |
| `MP-2.2-002` | Observe and analyze how the GAI system interacts with external networks, and identify any potential for negative externalities, particularly where content provenance might be compromised. | Information Integrity |

## MAP 2.3 — Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation

*AI Actor Tasks:* AI Development, Domain Experts, TEVV

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-2.3-001` | Assess the accuracy, quality, reliability, and authenticity of GAI output by comparing it to a set of known ground truth data and by using a variety of evaluation methods (e.g., human oversight and automated evaluation, proven cryptographic techniques, review of content inputs). | Information Integrity |
| `MP-2.3-002` | Review and document accuracy, representativeness, relevance, suitability of data used at different stages of AI life cycle. | Harmful Bias and Homogenization; Intellectual Property |
| `MP-2.3-003` | Deploy and document fact-checking techniques to verify the accuracy and veracity of information generated by GAI systems, especially when the information comes from multiple (or unknown) sources. | Information Integrity |
| `MP-2.3-004` | Develop and implement testing techniques to identify GAI produced content (e.g., synthetic media) that might be indistinguishable from human-generated content. | Information Integrity |
| `MP-2.3-005` | Implement plans for GAI systems to undergo regular adversarial testing to identify vulnerabilities and potential manipulation or misuse. | Information Security |

## MAP 3.4 — Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented.

*AI Actor Tasks:* AI Design, AI Development, Domain Experts, End-Users, Human Factors, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-3.4-001` | Evaluate whether GAI operators and end-users can accurately understand content lineage and origin. | Human-AI Configuration; Information Integrity |
| `MP-3.4-002` | Adapt existing training programs to include modules on digital content transparency. | Information Integrity |
| `MP-3.4-003` | Develop certification programs that test proficiency in managing GAI risks and interpreting content provenance, relevant to specific industry and context. | Information Integrity |
| `MP-3.4-004` | Delineate human proficiency tests from tests of GAI capabilities. | Human-AI Configuration |
| `MP-3.4-005` | Implement systems to continually monitor and track the outcomes of human-GAI configurations for future refinement and improvements. | Human-AI Configuration; Information Integrity |
| `MP-3.4-006` | Involve the end-users, practitioners, and operators in GAI system in prototyping and testing activities. Make sure these tests cover various scenarios, such as crisis situations or ethically sensitive contexts. | Human-AI Configuration; Information Integrity; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content |

## MAP 4.1 — Approaches for mapping AI technology and legal risks of its components – including the use of third-party data or software – are in place, followed, and documented, as are risks of infringement of a third-party’s intellectual property or other rights.

*AI Actor Tasks:* Governance and Oversight, Operation and Monitoring, Procurement, Third-party entities

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-4.1-001` | Conduct periodic monitoring of AI-generated content for privacy risks; address any possible instances of PII or sensitive data exposure. | Data Privacy |
| `MP-4.1-002` | Implement processes for responding to potential intellectual property infringement claims or other rights. | Intellectual Property |
| `MP-4.1-003` | Connect new GAI policies, procedures, and processes to existing model, data, software development, and IT governance and to legal, compliance, and risk management activities. | Information Security; Data Privacy |
| `MP-4.1-004` | Document training data curation policies, to the extent possible and according to applicable laws and policies. | Intellectual Property; Data Privacy; Obscene, Degrading, and/or Abusive Content |
| `MP-4.1-005` | Establish policies for collection, retention, and minimum quality of data, in consideration of the following risks: Disclosure of inappropriate CBRN information; Use of Illegal or dangerous content; Offensive cyber capabilities; Training data imbalances that could give rise to harmful biases; Leak of personally identifiable information, including facial likenesses of individuals. | CBRN Information or Capabilities; Intellectual Property; Information Security; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content; Data Privacy |
| `MP-4.1-006` | Implement policies and practices defining how third-party intellectual property and training data will be used, stored, and protected. | Intellectual Property; Value Chain and Component Integration |
| `MP-4.1-007` | Re-evaluate models that were fine-tuned or enhanced on top of third-party models. | Value Chain and Component Integration |
| `MP-4.1-008` | Re-evaluate risks when adapting GAI models to new domains. Additionally, establish warning systems to determine if a GAI system is being used in a new domain where previous assumptions (relating to context of use or mapped risks such as security, and safety) may no longer hold. | CBRN Information or Capabilities; Intellectual Property; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content; Data Privacy |
| `MP-4.1-009` | Leverage approaches to detect the presence of PII or sensitive data in generated output text, image, video, or audio. | Data Privacy |
| `MP-4.1-010` | Conduct appropriate diligence on training data use to assess intellectual property, and privacy, risks, including to examine whether use of proprietary or sensitive training data is consistent with applicable laws. | Intellectual Property; Data Privacy |

## MAP 5.1 — Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented.

*AI Actor Tasks:* AI Deployment, AI Design, AI Development, AI Impact Assessment, Affected Individuals and Communities, EndUsers, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-5.1-001` | Apply TEVV practices for content provenance (e.g., probing a system's synthetic data generation capabilities for potential misuse or vulnerabilities. | Information Integrity; Information Security |
| `MP-5.1-002` | Identify potential content provenance harms of GAI, such as misinformation or disinformation, deepfakes, including NCII, or tampered content. Enumerate and rank risks based on their likelihood and potential impact, and determine how well provenance solutions address specific risks and/or harms. | Information Integrity; Dangerous, Violent, or Hateful Content; Obscene, Degrading, and/or Abusive Content |
| `MP-5.1-003` | Consider disclosing use of GAI to end users in relevant contexts, while considering the objective of disclosure, the context of use, the likelihood and magnitude of the risk posed, the audience of the disclosure, as well as the frequency of the disclosures. | Human-AI Configuration |
| `MP-5.1-004` | Prioritize GAI structured public feedback processes based on risk assessment estimates. | Information Integrity; CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Harmful Bias and Homogenization |
| `MP-5.1-005` | Conduct adversarial role-playing exercises, GAI red-teaming, or chaos testing to identify anomalous or unforeseen failure modes. | Information Security |
| `MP-5.1-006` | Profile threats and negative impacts arising from GAI systems interacting with, manipulating, or generating content, and outlining known and potential vulnerabilities and the likelihood of their occurrence. | Information Security |

## MAP 5.2 — Practices and personnel for supporting regular engagement with relevant AI Actors and integrating feedback about positive, negative, and unanticipated impacts are in place and documented.

*AI Actor Tasks:* AI Deployment, AI Design, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, EndUsers, Human Factors, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `MP-5.2-001` | Determine context-based measures to identify if new impacts are present due to the GAI system, including regular engagements with downstream AI Actors to identify and quantify new contexts of unanticipated impacts of GAI systems. | Human-AI Configuration; Value Chain and Component Integration |
| `MP-5.2-002` | Plan regular engagements with AI Actors responsible for inputs to GAI systems, including third-party data and algorithms, to review and evaluate unanticipated impacts. | Human-AI Configuration; Value Chain and Component Integration |
