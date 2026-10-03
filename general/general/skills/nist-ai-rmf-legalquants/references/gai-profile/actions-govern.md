# GOVERN — Suggested Actions (GAI Profile)

*From NIST AI 600-1 (Generative AI Profile, July 2024), Section 3. Suggested Actions for the **GOVERN** function, grouped by AI RMF Subcategory. Each action is uniquely coded `GV-X.Y-NNN` and tagged with the GAI risks it addresses.*

Action ID format: `GV-X.Y-NNN` — function prefix, Category.Subcategory, sequential index.

## GOVERN 1.1 — Legal and regulatory requirements involving AI are understood, managed, and documented.

*AI Actor Tasks:* Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.1-001` | Align GAI development and use with applicable laws and regulations, including those related to data privacy, copyright and intellectual property law. | Data Privacy; Harmful Bias and Homogenization; Intellectual Property |

## GOVERN 1.2 — The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices.

*AI Actor Tasks:* Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.2-001` | Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches. | Data Privacy; Information Integrity; Intellectual Property |
| `GV-1.2-002` | Establish policies to evaluate risk-relevant capabilities of GAI and robustness of safety measures, both prior to deployment and on an ongoing basis, through internal and external evaluations. | CBRN Information or Capabilities; Information Security |

## GOVERN 1.3 — Processes, procedures, and practices are in place to determine the needed level of risk management activities based on the organization’s risk tolerance.

*AI Actor Tasks:* Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.3-001` | Consider the following factors when updating or defining risk tiers for GAI: Abuses and impacts to information integrity; Dependencies between GAI and other IT or data systems; Harm to fundamental rights or public safety; Presentation of obscene, objectionable, offensive, discriminatory, invalid or untruthful output; Psychological impacts to humans (e.g., anthropomorphization, algorithmic aversion, emotional entanglement); Possibility for malicious use; Whether the system introduces significant new security vulnerabilities; Anticipated system impact on some groups compared to others; Unreliable decision making capabilities, validity, adaptability, and variability of GAI system performance over time. | Information Integrity; Obscene, Degrading, and/or Abusive Content; Value Chain and Component Integration; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content; CBRN Information or Capabilities |
| `GV-1.3-002` | Establish minimum thresholds for performance or assurance criteria and review as part of deployment approval (“go/”no-go”) policies, procedures, and processes, with reviewed processes and approval thresholds reflecting measurement of GAI capabilities and risks. | CBRN Information or Capabilities; Confabulation; Dangerous, Violent, or Hateful Content |
| `GV-1.3-003` | Establish a test plan and response policy, before developing highly capable models, to periodically evaluate whether the model may misuse CBRN information or capabilities and/or offensive cyber capabilities. | CBRN Information or Capabilities; Information Security |
| `GV-1.3-004` | Obtain input from stakeholder communities to identify unacceptable use, in accordance with activities in the AI RMF Map function. | CBRN Information or Capabilities; Obscene, Degrading, and/or Abusive Content; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content |
| `GV-1.3-005` | Maintain an updated hierarchy of identified and expected GAI risks connected to contexts of GAI model advancement and use, potentially including specialized risk levels for GAI systems that address issues such as model collapse and algorithmic monoculture. | Harmful Bias and Homogenization |
| `GV-1.3-006` | Reevaluate organizational risk tolerances to account for unacceptable negative risk (such as where significant negative impacts are imminent, severe harms are actually occurring, or large-scale risks could occur); and broad GAI negative risks, including: Immature safety or risk cultures related to AI and GAI design, development and deployment, public information integrity risks, including impacts on democratic processes, unknown long-term performance characteristics of GAI. | Information Integrity; Dangerous, Violent, or Hateful Content; CBRN Information or Capabilities |
| `GV-1.3-007` | Devise a plan to halt development or deployment of a GAI system that poses unacceptable negative risk. | CBRN Information and Capability; Information Security; Information Integrity |

## GOVERN 1.4 — The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities.

*AI Actor Tasks:* AI Development, AI Deployment, Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.4-001` | Establish policies and mechanisms to prevent GAI systems from generating CSAM, NCII or content that violates the law. | Obscene, Degrading, and/or Abusive Content; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content |
| `GV-1.4-002` | Establish transparent acceptable use policies for GAI that address illegal use or applications of GAI. | CBRN Information or Capabilities; Obscene, Degrading, and/or Abusive Content; Data Privacy; Civil Rights violations |

## GOVERN 1.5 — Ongoing monitoring and periodic review of the risk management process and its outcomes are planned, and organizational roles and responsibilities are clearly defined, including determining the frequency of periodic review.

*AI Actor Tasks:* Governance and Oversight, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.5-001` | Define organizational responsibilities for periodic review of content provenance and incident monitoring for GAI systems. | Information Integrity |
| `GV-1.5-002` | Establish organizational policies and procedures for after action reviews of GAI system incident response and incident disclosures, to identify gaps; Update incident response and incident disclosure processes as required. | Human-AI Configuration; Information Security |
| `GV-1.5-003` | Maintain a document retention policy to keep history for test, evaluation, validation, and verification (TEVV), and digital content transparency methods for GAI. | Information Integrity; Intellectual Property |

## GOVERN 1.6 — Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities.

*AI Actor Tasks:* Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.6-001` | Enumerate organizational GAI systems for incorporation into AI system inventory and adjust AI system inventory requirements to account for GAI risks. | Information Security |
| `GV-1.6-002` | Define any inventory exemptions in organizational policies for GAI systems embedded into application software. | Value Chain and Component Integration |
| `GV-1.6-003` | In addition to general model, governance, and risk information, consider the following items in GAI system inventory entries: Data provenance information (e.g., source, signatures, versioning, watermarks); Known issues reported from internal bug tracking or external information sharing resources (e.g., AI incident database, AVID, CVE, NVD, or OECD AI incident monitor); Human oversight roles and responsibilities; Special rights and considerations for intellectual property, licensed works, or personal, privileged, proprietary or sensitive data; Underlying foundation models, versions of underlying models, and access modes. | Data Privacy; Human-AI Configuration; Information Integrity; Intellectual Property; Value Chain and Component Integration |

## GOVERN 1.7 — Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization’s trustworthiness.

*AI Actor Tasks:* AI Deployment, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-1.7-001` | Protocols are put in place to ensure GAI systems are able to be deactivated when necessary. | Information Security; Value Chain and Component Integration |
| `GV-1.7-002` | Consider the following factors when decommissioning GAI systems: Data retention requirements; Data security, e.g., containment, protocols, Data leakage after decommissioning; Dependencies between upstream, downstream, or other data, internet of things (IOT) or AI systems; Use of open-source data or models; Users’ emotional entanglement with GAI functions. | Human-AI Configuration; Information Security; Value Chain and Component Integration |

## GOVERN 2.1 — Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization.

*AI Actor Tasks:* Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-2.1-001` | Establish organizational roles, policies, and procedures for communicating GAI incidents and performance to AI Actors and downstream stakeholders (including those potentially impacted), via community or official resources (e.g., AI incident database, AVID, CVE, NVD, or OECD AI incident monitor). | Human-AI Configuration; Value Chain and Component Integration |
| `GV-2.1-002` | Establish procedures to engage teams for GAI system incident response with diverse composition and responsibilities based on the particular incident type. | Harmful Bias and Homogenization |
| `GV-2.1-003` | Establish processes to verify the AI Actors conducting GAI incident response tasks demonstrate and maintain the appropriate skills and training. | Human-AI Configuration |
| `GV-2.1-004` | When systems may raise national security risks, involve national security professionals in mapping, measuring, and managing those risks. | CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Information Security |
| `GV-2.1-005` | Create mechanisms to provide protections for whistleblowers who report, based on reasonable belief, when the organization violates relevant laws or poses a specific and empirically well-substantiated negative risk to public safety (or has already caused harm). | CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content |

## GOVERN 3.2 — Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems.

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-3.2-001` | Policies are in place to bolster oversight of GAI systems with independent evaluations or assessments of GAI models or systems where the type and robustness of evaluations are proportional to the identified risks. | CBRN Information or Capabilities; Harmful Bias and Homogenization |
| `GV-3.2-002` | Consider adjustment of organizational roles and components across lifecycle stages of large or complex GAI systems, including: Test and evaluation, validation, and red-teaming of GAI systems; GAI content moderation; GAI system development and engineering; Increased accessibility of GAI tools, interfaces, and systems, Incident response and containment. | Human-AI Configuration; Information Security; Harmful Bias and Homogenization |
| `GV-3.2-003` | Define acceptable use policies for GAI interfaces, modalities, and human-AI configurations (i.e., for chatbots and decision-making tasks), including criteria for the kinds of queries GAI applications should refuse to respond to. | Human-AI Configuration |
| `GV-3.2-004` | Establish policies for user feedback mechanisms for GAI systems which include thorough instructions and any mechanisms for recourse. | Human-AI Configuration |
| `GV-3.2-005` | Engage in threat modeling to anticipate potential risks from GAI systems. | CBRN Information or Capabilities; Information Security |

## GOVERN 4.1 — Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts.

*AI Actor Tasks:* AI Deployment, AI Design, AI Development, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-4.1-001` | Establish policies and procedures that address continual improvement processes for GAI risk measurement. Address general risks associated with a lack of explainability and transparency in GAI systems by using ample documentation and techniques such as: application of gradient-based attributions, occlusion/term reduction, counterfactual prompts and prompt engineering, and analysis of embeddings; Assess and update risk measurement approaches at regular cadences. | Confabulation |
| `GV-4.1-002` | Establish policies, procedures, and processes detailing risk measurement in context of use with standardized measurement protocols and structured public feedback exercises such as AI red-teaming or independent external evaluations. | CBRN Information and Capability; Value Chain and Component Integration |
| `GV-4.1-003` | Establish policies, procedures, and processes for oversight functions (e.g., senior leadership, legal, compliance, including internal evaluation) across the GAI lifecycle, from problem formulation and supply chains to system decommission. | Value Chain and Component Integration |

## GOVERN 4.2 — Organizational teams document the risks and potential impacts of the AI technology they design, develop, deploy, evaluate, and use, and they communicate about the impacts more broadly.

*AI Actor Tasks:* AI Deployment, AI Design, AI Development, Operation and Monitoring

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-4.2-001` | Establish terms of use and terms of service for GAI systems. | Intellectual Property; Dangerous, Violent, or Hateful Content; Obscene, Degrading, and/or Abusive Content |
| `GV-4.2-002` | Include relevant AI Actors in the GAI system risk identification process. | Human-AI Configuration |
| `GV-4.2-003` | Verify that downstream GAI system impacts (such as the use of third-party plugins) are included in the impact documentation process. | Value Chain and Component Integration |

## GOVERN 4.3 — Organizational practices are in place to enable AI testing, identification of incidents, and information sharing.

*AI Actor Tasks:* AI Impact Assessment, Affected Individuals and Communities, Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-4.3-002` | Establish organizational practices to identify the minimum set of criteria necessary for GAI system incident reporting such as: System ID (auto-generated most likely), Title, Reporter, System/Source, Data Reported, Date of Incident, Description, Impact(s), Stakeholder(s) Impacted. | Information Security |
| `GV-4.3-003` | Verify information sharing and feedback mechanisms among individuals and organizations regarding any negative impact from GAI systems. | Information Integrity; Data Privacy |

## GOVERN 5.1 — Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts related to AI risks.

*AI Actor Tasks:* AI Design, AI Impact Assessment, Affected Individuals and Communities, Governance and Oversight

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-5.1-001` | Allocate time and resources for outreach, feedback, and recourse processes in GAI system development. | Human-AI Configuration; Harmful Bias and Homogenization |
| `GV-5.1-002` | Document interactions with GAI systems to users prior to interactive activities, particularly in contexts involving more significant risks. | Human-AI Configuration; Confabulation |

## GOVERN 6.1 — Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights.

*AI Actor Tasks:* Operation and Monitoring, Procurement, Third-party entities

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-6.1-001` | Categorize different types of GAI content with associated third-party rights (e.g., copyright, intellectual property, data privacy). | Data Privacy; Intellectual Property; Value Chain and Component Integration |
| `GV-6.1-002` | Conduct joint educational activities and events in collaboration with third parties to promote best practices for managing GAI risks. | Value Chain and Component Integration |
| `GV-6.1-003` | Develop and validate approaches for measuring the success of content provenance management efforts with third parties (e.g., incidents detected and response times). | Information Integrity; Value Chain and Component Integration |
| `GV-6.1-004` | Draft and maintain well-defined contracts and service level agreements (SLAs) that specify content ownership, usage rights, quality standards, security requirements, and content provenance expectations for GAI systems. | Information Integrity; Information Security; Intellectual Property |
| `GV-6.1-005` | Implement a use-cased based supplier risk assessment framework to evaluate and monitor third-party entities’ performance and adherence to content provenance standards and technologies to detect anomalies and unauthorized changes; services acquisition and value chain risk management; and legal compliance. | Data Privacy; Information Integrity; Information Security; Intellectual Property; Value Chain and Component Integration |
| `GV-6.1-006` | Include clauses in contracts which allow an organization to evaluate third-party GAI processes and standards. | Information Integrity |
| `GV-6.1-007` | Inventory all third-party entities with access to organizational content and establish approved GAI technology and service provider lists. | Value Chain and Component Integration |
| `GV-6.1-008` | Maintain records of changes to content made by third parties to promote content provenance, including sources, timestamps, metadata. | Information Integrity; Value Chain and Component Integration; Intellectual Property |
| `GV-6.1-009` | Update and integrate due diligence processes for GAI acquisition and procurement vendor assessments to include intellectual property, data privacy, security, and other risks. For example, update processes to: Address solutions that may rely on embedded GAI technologies; Address ongoing monitoring, assessments, and alerting, dynamic risk assessments, and real-time reporting tools for monitoring third-party GAI risks; Consider policy adjustments across GAI modeling libraries, tools and APIs, fine-tuned models, and embedded tools; Assess GAI vendors, open-source or proprietary GAI tools, or GAI service providers against incident or vulnerability databases. | Data Privacy; Human-AI Configuration; Information Security; Intellectual Property; Value Chain and Component Integration; Harmful Bias and Homogenization |
| `GV-6.1-010` | Update GAI acceptable use policies to address proprietary and open-source GAI technologies and data, and contractors, consultants, and other third-party personnel. | Intellectual Property; Value Chain and Component Integration |

## GOVERN 6.2 — Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk.

*AI Actor Tasks:* AI Deployment, Operation and Monitoring, TEVV, Third-party entities

| Action ID | Suggested Action | GAI Risks |
|---|---|---|
| `GV-6.2-001` | Document GAI risks associated with system value chain to identify over-reliance on third-party data and to identify fallbacks. | Value Chain and Component Integration |
| `GV-6.2-002` | Document incidents involving third-party GAI data and systems, including opendata and open-source software. | Intellectual Property; Value Chain and Component Integration |
| `GV-6.2-003` | Establish incident response plans for third-party GAI technologies: Align incident response plans with impacts enumerated in MAP 5.1; Communicate third-party GAI incident response plans to all relevant AI Actors; Define ownership of GAI incident response functions; Rehearse third-party GAI incident response plans at a regular cadence; Improve incident response plans based on retrospective learning; Review incident response plans for alignment with relevant breach reporting, data protection, data privacy, or other laws. | Data Privacy; Human-AI Configuration; Information Security; Value Chain and Component Integration; Harmful Bias and Homogenization |
| `GV-6.2-004` | Establish policies and procedures for continuous monitoring of third-party GAI systems in deployment. | Value Chain and Component Integration |
| `GV-6.2-005` | Establish policies and procedures that address GAI data redundancy, including model weights and other system artifacts. | Harmful Bias and Homogenization |
| `GV-6.2-006` | Establish policies and procedures to test and manage risks related to rollover and fallback technologies for GAI systems, acknowledging that rollover and fallback may include manual processing. | Information Integrity |
| `GV-6.2-007` | Review vendor contracts and avoid arbitrary or capricious termination of critical GAI technologies or vendor services and non-standard terms that may amplify or defer liability in unexpected ways and/or contribute to unauthorized data collection by vendors or third-parties (e.g., secondary data use). Consider: Clear assignment of liability and responsibility for incidents, GAI system changes over time (e.g., fine-tuning, drift, decay); Request: Notification and disclosure for serious incidents arising from third-party data and systems; Service Level Agreements (SLAs) in vendor contracts that address incident response, response times, and availability of critical support. | Human-AI Configuration; Information Security; Value Chain and Component Integration |
