# Primary GAI Considerations (GAI Profile Glossary)

*From NIST AI 600-1, Appendix A. Cross-cutting GAI topics: governance, third-party, pre-deployment testing, structured public feedback, content provenance, incident disclosure.*

## Overview

The following primary considerations were derived as overarching themes from the GAI PWG consultation process. These considerations (Governance, Pre-Deployment Testing, Content Provenance, and Incident Disclosure) are relevant for voluntary use by any organization designing, developing, and using GAI and also inform the Actions to Manage GAI risks. Information included about the primary considerations is not exhaustive, but highlights the most relevant topics derived from the GAI PWG.

Acknowledgments: These considerations could not have been surfaced without the helpful analysis and contributions from the community and NIST staff GAI PWG leads: George Awad, Luca Belli, Harold Booth, Mat Heyman, Yooyoung Lee, Mark Pryzbocki, Reva Schwartz, Martin Stanley, and Kyra Yee.

## A.1. Governance

## A.1.1. Overview

Like any other technology system, governance principles and techniques can be used to manage risks related to generative AI models, capabilities, and applications. Organizations may choose to apply their existing risk tiering to GAI systems, or they may opt to revise or update AI system risk levels to address these unique GAI risks. This section describes how organizational governance regimes may be reevaluated and adjusted for GAI contexts. It also addresses third-party considerations for governing across the AI value chain.

## A.1.2. Organizational Governance

GAI opportunities, risks and long-term performance characteristics are typically less well-understood than non-generative AI tools and may be perceived and acted upon by humans in ways that vary greatly. Accordingly, GAI may call for different levels of oversight from AI Actors or different human-AI configurations in order to manage their risks effectively. Organizations’ use of GAI systems may also warrant additional human review, tracking and documentation, and greater management oversight.

AI technology can produce varied outputs in multiple modalities and present many classes of user interfaces. This leads to a broader set of AI Actors interacting with GAI systems for widely differing applications and contexts of use. These can include data labeling and preparation, development of GAI models, content moderation, code generation and review, text generation and editing, image and video generation, summarization, search, and chat. These activities can take place within organizational settings or in the public domain.

Organizations can restrict AI applications that cause harm, exceed stated risk tolerances, or that conflict with their tolerances or values. Governance tools and protocols that are applied to other types of AI systems can be applied to GAI systems. These plans and actions include:

- • Accessibility and reasonable accommodations

- • AI actor credentials and qualifications

- • Alignment to organizational values

- • Auditing and assessment

- • Change-management controls

- • Commercial use

- • Data provenance

- • Data protection

- • Data retention

- • Consistency in use of defining key terms

- • Decommissioning

- • Discouraging anonymous use

- • Education

- • Impact assessments

- • Incident response

- • Monitoring

- • Opt-outs

- • Risk-based controls

- • Risk mapping and measurement

- • Science-backed TEVV practices

- • Secure software development practices

- • Stakeholder engagement

- • Synthetic content detection and labeling tools and techniques

- • Whistleblower protections

- • Workforce diversity and interdisciplinary teams

Establishing acceptable use policies and guidance for the use of GAI in formal human-AI teaming settings as well as different levels of human-AI configurations can help to decrease risks arising from misuse, abuse, inappropriate repurpose, and misalignment between systems and users. These practices are just one example of adapting existing governance protocols for GAI contexts.

## A.1.3. Third-Party Considerations

Organizations may seek to acquire, embed, incorporate, or use open-source or proprietary third-party GAI models, systems, or generated data for various applications across an enterprise. Use of these GAI tools and inputs has implications for all functions of the organization – including but not limited to acquisition, human resources, legal, compliance, and IT services – regardless of whether they are carried out by employees or third parties. Many of the actions cited above are relevant and options for addressing third-party considerations.

Third party GAI integrations may give rise to increased intellectual property, data privacy, or information security risks, pointing to the need for clear guidelines for transparency and risk management regarding the collection and use of third-party data for model inputs. Organizations may consider varying risk controls for foundation models, fine-tuned models, and embedded tools, enhanced processes for interacting with external GAI technologies or service providers. Organizations can apply standard or existing risk controls and processes to proprietary or open-source GAI technologies, data, and third-party service providers, including acquisition and procurement due diligence, requests for software bills of materials (SBOMs), application of service level agreements (SLAs), and statement on standards for attestation engagement (SSAE) reports to help with third-party transparency and risk management for GAI systems.

## A.1.4. Pre-Deployment Testing Overview

The diverse ways and contexts in which GAI systems may be developed, used, and repurposed complicates risk mapping and pre-deployment measurement efforts. Robust test, evaluation, validation, and verification (TEVV) processes can be iteratively applied – and documented – in early stages of the AI lifecycle and informed by representative AI Actors (see Figure 3 of the AI RMF). Until new and rigorous

early lifecycle TEVV approaches are developed and matured for GAI, organizations may use recommended “pre-deployment testing” practices to measure performance, capabilities, limits, risks, and impacts. This section describes risk measurement and estimation as part of pre-deployment TEVV, and examines the state of play for pre-deployment testing methodologies.

## Limitations of Current Pre-deployment Test Approaches

Currently available pre-deployment TEVV processes used for GAI applications may be inadequate, nonsystematically applied, or fail to reflect or mismatched to deployment contexts. For example, the anecdotal testing of GAI system capabilities through video games or standardized tests designed for humans (e.g., intelligence tests, professional licensing exams) does not guarantee GAI system validity or reliability in those domains. Similarly, jailbreaking or prompt engineering tests may not systematically assess validity or reliability risks.

Measurement gaps can arise from mismatches between laboratory and real-world settings. Current testing approaches often remain focused on laboratory conditions or restricted to benchmark test datasets and in silico techniques that may not extrapolate well to—or directly assess GAI impacts in realworld conditions. For example, current measurement gaps for GAI make it difficult to precisely estimate its potential ecosystem-level or longitudinal risks and related political, social, and economic impacts. Gaps between benchmarks and real-world use of GAI systems may likely be exacerbated due to prompt sensitivity and broad heterogeneity of contexts of use.

## A.1.5. Structured Public Feedback

Structured public feedback can be used to evaluate whether GAI systems are performing as intended and to calibrate and verify traditional measurement methods. Examples of structured feedback include, but are not limited to:

- • Participatory Engagement Methods: Methods used to solicit feedback from civil society groups, affected communities, and users, including focus groups, small user studies, and surveys.

- • Field Testing: Methods used to determine how people interact with, consume, use, and make sense of AI-generated information, and subsequent actions and effects, including UX, usability, and other structured, randomized experiments.

- • AI Red-teaming: A structured testing exercise used to probe an AI system to find flaws and vulnerabilities such as inaccurate, harmful, or discriminatory outputs, often in a controlled environment and in collaboration with system developers.

Information gathered from structured public feedback can inform design, implementation, deployment approval, maintenance, or decommissioning decisions. Results and insights gleaned from these exercises can serve multiple purposes, including improving data quality and preprocessing, bolstering governance decision making, and enhancing system documentation and debugging practices. When implementing feedback activities, organizations should follow human subjects research requirements and best practices such as informed consent and subject compensation.

## Participatory Engagement Methods

On an ad hoc or more structured basis, organizations can design and use a variety of channels to engage external stakeholders in product development or review. Focus groups with select experts can provide feedback on a range of issues. Small user studies can provide feedback from representative groups or populations. Anonymous surveys can be used to poll or gauge reactions to specific features. Participatory engagement methods are often less structured than field testing or red teaming, and are more commonly used in early stages of AI or product development.

## Field Testing

Field testing involves structured settings to evaluate risks and impacts and to simulate the conditions under which the GAI system will be deployed. Field style tests can be adapted from a focus on user preferences and experiences towards AI risks and impacts – both negative and positive. When carried out with large groups of users, these tests can provide estimations of the likelihood of risks and impacts in real world interactions.

Organizations may also collect feedback on outcomes, harms, and user experience directly from users in the production environment after a model has been released, in accordance with human subject standards such as informed consent and compensation. Organizations should follow applicable human subjects research requirements, and best practices such as informed consent and subject compensation, when implementing feedback activities.

## AI Red-teaming

AI red-teaming is an evolving practice that references exercises often conducted in a controlled environment and in collaboration with AI developers building AI models to identify potential adverse behavior or outcomes of a GAI model or system, how they could occur, and stress test safeguards”. AI red-teaming can be performed before or after AI models or systems are made available to the broader public; this section focuses on red-teaming in pre-deployment contexts.

The quality of AI red-teaming outputs is related to the background and expertise of the AI red team itself. Demographically and interdisciplinarily diverse AI red teams can be used to identify flaws in the varying contexts where GAI will be used. For best results, AI red teams should demonstrate domain expertise, and awareness of socio-cultural aspects within the deployment context. AI red-teaming results should be given additional analysis before they are incorporated into organizational governance and decision making, policy and procedural updates, and AI risk management efforts. Various types of AI red-teaming may be appropriate, depending on the use case:

- • General Public: Performed by general users (not necessarily AI or technical experts) who are expected to use the model or interact with its outputs, and who bring their own lived experiences and perspectives to the task of AI red-teaming. These individuals may have been provided instructions and material to complete tasks which may elicit harmful model behaviors. This type of exercise can be more effective with large groups of AI red-teamers.

- • Expert: Performed by specialists with expertise in the domain or specific AI red-teaming context of use (e.g., medicine, biotech, cybersecurity).

- • Combination: In scenarios when it is difficult to identify and recruit specialists with sufficient domain and contextual expertise, AI red-teaming exercises may leverage both expert and

- general public participants. For example, expert AI red-teamers could modify or verify the prompts written by general public AI red-teamers. These approaches may also expand coverage of the AI risk attack surface.

- • Human / AI: Performed by GAI in combination with specialist or non-specialist human teams. GAI-led red-teaming can be more cost effective than human red-teamers alone. Human or GAIled AI red-teaming may be better suited for eliciting different types of harms.

## A.1.6. Content Provenance Overview

GAI technologies can be leveraged for many applications such as content generation and synthetic data. Some aspects of GAI outputs, such as the production of deepfake content, can challenge our ability to distinguish human-generated content from AI-generated synthetic content. To help manage and mitigate these risks, digital transparency mechanisms like provenance data tracking can trace the origin and history of content. Provenance data tracking and synthetic content detection can help facilitate greater information access about both authentic and synthetic content to users, enabling better knowledge of trustworthiness in AI systems. When combined with other organizational accountability mechanisms, digital content transparency approaches can enable processes to trace negative outcomes back to their source, improve information integrity, and uphold public trust. Provenance data tracking and synthetic content detection mechanisms provide information about the origin and history of content to assist in GAI risk management efforts.

Provenance metadata can include information about GAI model developers or creators of GAI content, date/time of creation, location, modifications, and sources. Metadata can be tracked for text, images, videos, audio, and underlying datasets. The implementation of provenance data tracking techniques can help assess the authenticity, integrity, intellectual property rights, and potential manipulations in digital content. Some well-known techniques for provenance data tracking include digital watermarking, metadata recording, digital fingerprinting, and human authentication, among others.

## Provenance Data Tracking Approaches

Provenance data tracking techniques for GAI systems can be used to track the history and origin of data inputs, metadata, and synthetic content. Provenance data tracking records the origin and history for digital content, allowing its authenticity to be determined. It consists of techniques to record metadata as well as overt and covert digital watermarks on content. Data provenance refers to tracking the origin and history of input data through metadata and digital watermarking techniques. Provenance data tracking processes can include and assist AI Actors across the lifecycle who may not have full visibility or control over the various trade-offs and cascading impacts of early-stage model decisions on downstream performance and synthetic outputs. For example, by selecting a watermarking model to prioritize robustness (the durability of a watermark), an AI actor may inadvertently diminish computational complexity (the resources required to implement watermarking). Organizational risk management efforts for enhancing content provenance include:

- • Tracking provenance of training data and metadata for GAI systems;

- • Documenting provenance data limitations within GAI systems;

- • Monitoring system capabilities and limitations in deployment through rigorous TEVV processes;

- • Evaluating how humans engage, interact with, or adapt to GAI content (especially in decision making tasks informed by GAI content), and how they react to applied provenance techniques such as overt disclosures.

Organizations can document and delineate GAI system objectives and limitations to identify gaps where provenance data may be most useful. For instance, GAI systems used for content creation may require robust watermarking techniques and corresponding detectors to identify the source of content or metadata recording techniques and metadata management tools and repositories to trace content origins and modifications. Further narrowing of GAI task definitions to include provenance data can enable organizations to maximize the utility of provenance data and risk management efforts.

## A.1.7. Enhancing Content Provenance through Structured Public Feedback

While indirect feedback methods such as automated error collection systems are useful, they often lack the context and depth that direct input from end users can provide. Organizations can leverage feedback approaches described in the Pre-Deployment Testing section to capture input from external sources such as through AI red-teaming.

Integrating pre- and post-deployment external feedback into the monitoring process for GAI models and corresponding applications can help enhance awareness of performance changes and mitigate potential risks and harms from outputs. There are many ways to capture and make use of user feedback – before and after GAI systems and digital content transparency approaches are deployed – to gain insights about authentication efficacy and vulnerabilities, impacts of adversarial threats on techniques, and unintended consequences resulting from the utilization of content provenance approaches on users and communities. Furthermore, organizations can track and document the provenance of datasets to identify instances in which AI-generated data is a potential root cause of performance issues with the GAI system.

## A.1.8. Incident Disclosure Overview

AI incidents can be defined as an “event, circumstance, or series of events where the development, use, or malfunction of one or more AI systems directly or indirectly contributes to one of the following harms: injury or harm to the health of a person or groups of people (including psychological harms and harms to mental health); disruption of the management and operation of critical infrastructure; violations of human rights or a breach of obligations under applicable law intended to protect fundamental, labor, and intellectual property rights; or harm to property, communities, or the environment.” AI incidents can occur in the aggregate (i.e., for systemic discrimination) or acutely (i.e., for one individual).

State of AI Incident Tracking and Disclosure Formal channels do not currently exist to report and document AI incidents. However, a number of publicly available databases have been created to document their occurrence. These reporting channels make decisions on an ad hoc basis about what kinds of incidents to track. Some, for example, track by amount of media coverage.

Documenting, reporting, and sharing information about GAI incidents can help mitigate and prevent harmful outcomes by assisting relevant AI Actors in tracing impacts to their source. Greater awareness and standardization of GAI incident reporting could promote this transparency and improve GAI risk management across the AI ecosystem.

## Documentation and Involvement of AI Actors

AI Actors should be aware of their roles in reporting AI incidents. To better understand previous incidents and implement measures to prevent similar ones in the future, organizations could consider developing guidelines for publicly available incident reporting which include information about AI actor responsibilities. These guidelines would help AI system operators identify GAI incidents across the AI lifecycle and with AI Actors regardless of role. Documentation and review of third-party inputs and plugins for GAI systems is especially important for AI Actors in the context of incident disclosure; LLM inputs and content delivered through these plugins is often distributed, with inconsistent or insufficient access control.

Documentation practices including logging, recording, and analyzing GAI incidents can facilitate smoother sharing of information with relevant AI Actors. Regular information sharing, change management records, version history and metadata can also empower AI Actors responding to and managing AI incidents.

- Appendix B. References Acemoglu, D. (2024) The Simple Macroeconomics of AI https://www.nber.org/papers/w32487 AI Incident Database. https://incidentdatabase.ai/

Atherton, D. (2024) Deepfakes and Child Safety: A Survey and Analysis of 2023 Incidents and Responses. AI Incident Database. https://incidentdatabase.ai/blog/deepfakes-and-child-safety/

Badyal, N. et al. (2023) Intentional Biases in LLM Responses. arXiv. https://arxiv.org/pdf/2311.07611 Bing Chat: Data Exfiltration Exploit Explained. Embrace The Red. https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/

Bommasani, R. et al. (2022) Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization? arXiv. https://arxiv.org/pdf/2211.13972

Boyarskaya, M. et al. (2020) Overcoming Failures of Imagination in AI Infused System Development and Deployment. arXiv. https://arxiv.org/pdf/2011.13416

Browne, D. et al. (2023) Securing the AI Pipeline. Mandiant. https://www.mandiant.com/resources/blog/securing-ai-pipeline

Burgess, M. (2024) Generative AI’s Biggest Security Flaw Is Not Easy to Fix. WIRED. https://www.wired.com/story/generative-ai-prompt-injection-hacking/

Burtell, M. et al. (2024) The Surprising Power of Next Word Prediction: Large Language Models Explained, Part 1. Georgetown Center for Security and Emerging Technology. https://cset.georgetown.edu/article/the-surprising-power-of-next-word-prediction-large-languagemodels-explained-part-1/

Canadian Centre for Cyber Security (2023) Generative artificial intelligence (AI) - ITSAP.00.041.

https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041 Carlini, N., et al. (2021) Extracting Training Data from Large Language Models. Usenix. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting

- Carlini, N. et al. (2023) Quantifying Memorization Across Neural Language Models. ICLR 2023. https://arxiv.org/pdf/2202.07646

- Carlini, N. et al. (2024) Stealing Part of a Production Language Model. arXiv. https://arxiv.org/abs/2403.06634

Chandra, B. et al. (2023) Dismantling the Disinformation Business of Chinese Influence Operations. RAND. https://www.rand.org/pubs/commentary/2023/10/dismantling-the-disinformation-business-ofchinese.html

Ciriello, R. et al. (2024) Ethical Tensions in Human-AI Companionship: A Dialectical Inquiry into Replika. ResearchGate. https://www.researchgate.net/publication/374505266_Ethical_Tensions_in_HumanAI_Companionship_A_Dialectical_Inquiry_into_Replika

Dahl, M. et al. (2024) Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models. arXiv. https://arxiv.org/abs/2401.01301

De Angelo, D. (2024) Short, Mid and Long-Term Impacts of AI in Cybersecurity. Palo Alto Networks. https://www.paloaltonetworks.com/blog/2024/02/impacts-of-ai-in-cybersecurity/

De Freitas, J. et al. (2023) Chatbots and Mental Health: Insights into the Safety of Generative AI. Harvard Business School. https://www.hbs.edu/ris/Publication%20Files/23-011_c1bdd417-f717-47b6-bccb5438c6e65c1a_f6fd9798-3c2d-4932-b222-056231fe69d7.pdf

Dietvorst, B. et al. (2014) Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err. Journal of Experimental Psychology. https://marketing.wharton.upenn.edu/wpcontent/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf

Duhigg, C. (2012) How Companies Learn Your Secrets. New York Times. https://www.nytimes.com/2012/02/19/magazine/shopping-habits.html

Elsayed, G. et al. (2024) Images altered to trick machine vision can influence humans too. Google DeepMind. https://deepmind.google/discover/blog/images-altered-to-trick-machine-vision-caninfluence-humans-too/

Epstein, Z. et al. (2023). Art and the science of generative AI. Science. https://www.science.org/doi/10.1126/science.adh4451

Feffer, M. et al. (2024) Red-Teaming for Generative AI: Silver Bullet or Security Theater? arXiv. https://arxiv.org/pdf/2401.15897

Glazunov, S. et al. (2024) Project Naptime: Evaluating Offensive Security Capabilities of Large Language Models. Project Zero. https://googleprojectzero.blogspot.com/2024/06/project-naptime.html

Greshake, K. et al. (2023) Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv. https://arxiv.org/abs/2302.12173

Hagan, M. (2024) Good AI Legal Help, Bad AI Legal Help: Establishing quality standards for responses to people’s legal problem stories. SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4696936

Haran, R. (2023) Securing LLM Systems Against Prompt Injection. NVIDIA. https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/

Information Technology Industry Council (2024) Authenticating AI-Generated Content. https://www.itic.org/policy/ITI_AIContentAuthorizationPolicy_122123.pdf

Jain, S. et al. (2023) Algorithmic Pluralism: A Structural Approach To Equal Opportunity. arXiv. https://arxiv.org/pdf/2305.08157

Ji, Z. et al (2023) Survey of Hallucination in Natural Language Generation. ACM Comput. Surv. 55, 12, Article 248. https://doi.org/10.1145/3571730

Jones-Jang, S. et al. (2022) How do people react to AI failure? Automation bias, algorithmic aversion, and perceived controllability. Oxford. https://academic.oup.com/jcmc/article/28/1/zmac029/6827859]

Jussupow, E. et al. (2020) Why Are We Averse Towards Algorithms? A Comprehensive Literature Review on Algorithm Aversion. ECIS 2020. https://aisel.aisnet.org/ecis2020_rp/168/

Kalai, A., et al. (2024) Calibrated Language Models Must Hallucinate. arXiv. https://arxiv.org/pdf/2311.14648

Karasavva, V. et al. (2021) Personality, Attitudinal, and Demographic Predictors of Non-consensual Dissemination of Intimate Images. NIH. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9554400/

Katzman, J., et al. (2023) Taxonomizing and measuring representational harms: a look at image tagging. AAAI. https://dl.acm.org/doi/10.1609/aaai.v37i12.26670

Khan, T. et al. (2024) From Code to Consumer: PAI’s Value Chain Analysis Illuminates Generative AI’s Key Players. AI. https://partnershiponai.org/from-code-to-consumer-pais-value-chain-analysis-illuminatesgenerative-ais-key-players/

Kirchenbauer, J. et al. (2023) A Watermark for Large Language Models. OpenReview. https://openreview.net/forum?id=aX8ig9X2a7

Kleinberg, J. et al. (May 2021) Algorithmic monoculture and social welfare. PNAS. https://www.pnas.org/doi/10.1073/pnas.2018340118

Lakatos, S. (2023) A Revealing Picture. Graphika. https://graphika.com/reports/a-revealing-picture Lee, H. et al. (2024) Deepfakes, Phrenology, Surveillance, and More! A Taxonomy of AI Privacy Risks. arXiv. https://arxiv.org/pdf/2310.07879 Lenaerts-Bergmans, B. (2024) Data Poisoning: The Exploitation of Generative AI. Crowdstrike. https://www.crowdstrike.com/cybersecurity-101/cyberattacks/data-poisoning/ Liang, W. et al. (2023) GPT detectors are biased against non-native English writers. arXiv. https://arxiv.org/abs/2304.02819 Luccioni, A. et al. (2023) Power Hungry Processing: Watts Driving the Cost of AI Deployment? arXiv. https://arxiv.org/pdf/2311.16863 Mouton, C. et al. (2024) The Operational Risks of AI in Large-Scale Biological Attacks. RAND. https://www.rand.org/pubs/research_reports/RRA2977-2.html. Nicoletti, L. et al. (2023) Humans Are Biased. Generative Ai Is Even Worse. Bloomberg.

- https://www.bloomberg.com/graphics/2023-generative-ai-bias/.

National Institute of Standards and Technology (2024) Adversarial Machine Learning: A Taxonomy and

Terminology of Attacks and Mitigations https://csrc.nist.gov/pubs/ai/100/2/e2023/final National Institute of Standards and Technology (2023) AI Risk Management Framework. https://www.nist.gov/itl/ai-risk-management-framework

National Institute of Standards and Technology (2023) AI Risk Management Framework, Chapter 3: AI Risks and Trustworthiness. https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Foundational_Information/3-sec-characteristics

National Institute of Standards and Technology (2023) AI Risk Management Framework, Chapter 6: AI RMF Profiles. https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Core_And_Profiles/6-sec-profile

- National Institute of Standards and Technology (2023) AI Risk Management Framework, Appendix A: Descriptions of AI Actor Tasks.

- https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Appendices/Appendix_A#:~:text=AI%20actors% 20in%20this%20category,data%20providers%2C%20system%20funders%2C%20product

- National Institute of Standards and Technology (2023) AI Risk Management Framework, Appendix B: How AI Risks Differ from Traditional Software Risks.

- https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Appendices/Appendix_B

National Institute of Standards and Technology (2023) AI RMF Playbook. https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook

National Institue of Standards and Technology (2023) Framing Risk https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Foundational_Information/1-sec-risk

National Institute of Standards and Technology (2023) The Language of Trustworthy AI: An In-Depth Glossary of Terms https://airc.nist.gov/AI_RMF_Knowledge_Base/Glossary

National Institue of Standards and Technology (2022) Towards a Standard for Identifying and Managing Bias in Artificial Intelligence https://www.nist.gov/publications/towards-standard-identifying-andmanaging-bias-artificial-intelligence

Northcutt, C. et al. (2021) Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks. arXiv. https://arxiv.org/pdf/2103.14749

- OECD (2023) "Advancing accountability in AI: Governing and managing risks throughout the lifecycle for trustworthy AI", OECD Digital Economy Papers, No. 349, OECD Publishing, Paris. https://doi.org/10.1787/2448f04b-en

- OECD (2024) "Defining AI incidents and related terms" OECD Artificial Intelligence Papers, No. 16, OECD Publishing, Paris. https://doi.org/10.1787/d1a8d965-en

- OpenAI (2023) GPT-4 System Card. https://cdn.openai.com/papers/gpt-4-system-card.pdf

- OpenAI (2024) GPT-4 Technical Report. https://arxiv.org/pdf/2303.08774 Padmakumar, V. et al. (2024) Does writing with language models reduce content diversity? ICLR.

- https://arxiv.org/pdf/2309.05196 Park, P. et. al. (2024) AI deception: A survey of examples, risks, and potential solutions. Patterns, 5(5).

- arXiv. https://arxiv.org/pdf/2308.14752

Partnership on AI (2023) Building a Glossary for Synthetic Media Transparency Methods, Part 1: Indirect Disclosure. https://partnershiponai.org/glossary-for-synthetic-media-transparency-methods-part-1indirect-disclosure/

Qu, Y. et al. (2023) Unsafe Diffusion: On the Generation of Unsafe Images and Hateful Memes From TextTo-Image Models. arXiv. https://arxiv.org/pdf/2305.13873

Rafat, K. et al. (2023) Mitigating carbon footprint for knowledge distillation based deep learning model compression. PLOS One. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0285668

Said, I. et al. (2022) Nonconsensual Distribution of Intimate Images: Exploring the Role of Legal Attitudes in Victimization and Perpetration. Sage. https://journals.sagepub.com/doi/full/10.1177/08862605221122834#bibr47-08862605221122834

Sandbrink, J. (2023) Artificial intelligence and biological misuse: Differentiating risks of language models and biological design tools. arXiv. https://arxiv.org/pdf/2306.13952

Satariano, A. et al. (2023) The People Onscreen Are Fake. The Disinformation Is Real. New York Times. https://www.nytimes.com/2023/02/07/technology/artificial-intelligence-training-deepfake.html

Schaul, K. et al. (2024) Inside the secret list of websites that make AI like ChatGPT sound smart. Washington Post. https://www.washingtonpost.com/technology/interactive/2023/ai-chatbot-learning/

Scheurer, J. et al. (2023) Technical report: Large language models can strategically deceive their users when put under pressure. arXiv. https://arxiv.org/abs/2311.07590

Shelby, R. et al. (2023) Sociotechnical Harms of Algorithmic Systems: Scoping a Taxonomy for Harm Reduction. arXiv. https://arxiv.org/pdf/2210.05791

Shevlane, T. et al. (2023) Model evaluation for extreme risks. arXiv. https://arxiv.org/pdf/2305.15324 Shumailov, I. et al. (2023) The curse of recursion: training on generated data makes models forget. arXiv. https://arxiv.org/pdf/2305.17493v2

Smith, A. et al. (2023) Hallucination or Confabulation? Neuroanatomy as metaphor in Large Language Models. PLOS Digital Health. https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000388

Soice, E. et al. (2023) Can large language models democratize access to dual-use biotechnology? arXiv. https://arxiv.org/abs/2306.03809

Solaiman, I. et al. (2023) The Gradient of Generative AI Release: Methods and Considerations. arXiv. https://arxiv.org/abs/2302.04844

Staab, R. et al. (2023) Beyond Memorization: Violating Privacy via Inference With Large Language Models. arXiv. https://arxiv.org/pdf/2310.07298

Stanford, S. et al. (2023) Whose Opinions Do Language Models Reflect? arXiv. https://arxiv.org/pdf/2303.17548

Strubell, E. et al. (2019) Energy and Policy Considerations for Deep Learning in NLP. arXiv. https://arxiv.org/pdf/1906.02243

The White House (2016) Circular No. A-130, Managing Information as a Strategic Resource. https://www.whitehouse.gov/wpcontent/uploads/legacy_drupal_files/omb/circulars/A130/a130revised.pdf

The White House (2023) Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence. https://www.whitehouse.gov/briefing-room/presidentialactions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-ofartificial-intelligence/

The White House (2022) Roadmap for Researchers on Priorities Related to Information Integrity Research and Development. https://www.whitehouse.gov/wp-content/uploads/2022/12/RoadmapInformation-Integrity-RD-2022.pdf?

Thiel, D. (2023) Investigation Finds AI Image Generation Models Trained on Child Abuse. Stanford Cyber Policy Center. https://cyber.fsi.stanford.edu/news/investigation-finds-ai-image-generation-modelstrained-child-abuse

Tirrell, L. (2017) Toxic Speech: Toward an Epidemiology of Discursive Harm. Philosophical Topics, 45(2), 139-162. https://www.jstor.org/stable/26529441

Tufekci, Z. (2015) Algorithmic Harms Beyond Facebook and Google: Emergent Challenges of Computational Agency. Colorado Technology Law Journal. https://ctlj.colorado.edu/wpcontent/uploads/2015/08/Tufekci-final.pdf

Turri, V. et al. (2023) Why We Need to Know More: Exploring the State of AI Incident Documentation Practices. AAAI/ACM Conference on AI, Ethics, and Society. https://dl.acm.org/doi/fullHtml/10.1145/3600211.3604700

Urbina, F. et al. (2022) Dual use of artificial-intelligence-powered drug discovery. Nature Machine Intelligence. https://www.nature.com/articles/s42256-022-00465-9

- Wang, X. et al. (2023) Energy and Carbon Considerations of Fine-Tuning BERT. ACL Anthology. https://aclanthology.org/2023.findings-emnlp.607.pdf

- Wang, Y. et al. (2023) Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs. arXiv. https://arxiv.org/pdf/2308.13387

Wardle, C. et al. (2017) Information Disorder: Toward an interdisciplinary framework for research and policy making. Council of Europe. https://rm.coe.int/information-disorder-toward-an-interdisciplinaryframework-for-researc/168076277c

Weatherbed, J. (2024) Trolls have flooded X with graphic Taylor Swift AI fakes. The Verge. https://www.theverge.com/2024/1/25/24050334/x-twitter-taylor-swift-ai-fake-images-trending

Wei, J. et al. (2024) Long Form Factuality in Large Language Models. arXiv. https://arxiv.org/pdf/2403.18802

- Weidinger, L. et al. (2021) Ethical and social risks of harm from Language Models. arXiv. https://arxiv.org/pdf/2112.04359 Weidinger, L. et al. (2023) Sociotechnical Safety Evaluation of Generative AI Systems. arXiv. https://arxiv.org/pdf/2310.11986

- Weidinger, L. et al. (2022) Taxonomy of Risks posed by Language Models. FAccT ’22. https://dl.acm.org/doi/pdf/10.1145/3531146.3533088

West, D. (2023) AI poses disproportionate risks to women. Brookings. https://www.brookings.edu/articles/ai-poses-disproportionate-risks-to-women/

Wu, K. et al. (2024) How well do LLMs cite relevant medical references? An evaluation framework and analyses. arXiv. https://arxiv.org/pdf/2402.02008

Yin, L. et al. (2024) OpenAI’s GPT Is A Recruiter’s Dream Tool. Tests Show There’s Racial Bias. Bloomberg.

- https://www.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/

Yu, Z. et al. (March 2024) Don’t Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models. arXiv. https://arxiv.org/html/2403.17336v1

Zaugg, I. et al. (2022) Digitally-disadvantaged languages. Policy Review. https://policyreview.info/pdf/policyreview-2022-2-1654.pdf

Zhang, Y. et al. (2023) Human favoritism, not AI aversion: People’s perceptions (and bias) toward generative AI, human experts, and human–GAI collaboration in persuasive content generation. Judgment and Decision Making. https://www.cambridge.org/core/journals/judgment-and-decisionmaking/article/human-favoritism-not-ai-aversion-peoples-perceptions-and-bias-toward-generative-aihuman-experts-and-humangai-collaboration-in-persuasive-contentgeneration/419C4BD9CE82673EAF1D8F6C350C4FA8

Zhang, Y. et al. (2023) Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models.

- arXiv. https://arxiv.org/pdf/2309.01219

Zhao, X. et al. (2023) Provable Robust Watermarking for AI-Generated Text. Semantic Scholar. https://www.semanticscholar.org/paper/Provable-Robust-Watermarking-for-AI-Generated-Text-ZhaoAnanth/75b68d0903af9d9f6e47ce3cf7e1a7d27ec811dc
