# Ministry of Innovation 2023 AI Policy: 12 Principles

Source: "Responsible Innovation: Israel's Policy on Artificial Intelligence Regulation and Ethics", Ministry of Innovation, Science and Technology with the Ministry of Justice, published December 2023. The document carries no day-level date.

The policy sets Israel's "Responsible Innovation" framework: voluntary, sector-based, risk-proportional. It is not a statute. It guides how government should regulate AI and how developers and operators should build and deploy it.

## Six Regulatory Principles

These are quoted from the policy. They apply to government and regulators, not to private developers directly. Include them in compliance docs to show alignment with national policy direction. Earlier versions of this file paraphrased them and got three of the six wrong; do not re-paraphrase.

### 1. Empowering sector-specific regulators
The need for regulation in a particular sector is assessed by that sector's regulator, based on concrete needs and adapted to the sector's existing regulatory environment. This is favoured over broad horizontal legislation, though such efforts must stay consistent with a uniform government policy through dedicated coordination mechanisms, and the need for horizontal legislation is to be reassessed periodically. Implication: identify your sector regulator first; it, not a general AI authority, sets your obligations.

### 2. International interoperability of frameworks
Israeli regulation should stay consistent with the approaches of leading countries and international organisations, so far as possible, to reduce cross-border regulatory barriers. Implication: policies you adopt from the OECD or the EU AI Act will generally be recognised by Israeli regulators.

### 3. Risk-based approach
Regulation is adapted to the risks posed by the type of technology, weighed against potential benefits and applied mitigations, in the context of the specific use. It should come from the regulator's own risk-management process and should direct the private sector to adopt a risk-management approach too. Implication: a low-risk chatbot and a medical-diagnosis system sit under different regimes even inside Israel.

### 4. Incremental development and regulatory experimentation
Regulation should be incremental and adaptable alongside technological development, using regulatory experimentation tools including pilot projects and sandboxes. Implication: expect sandbox routes before binding rules, and treat participation as a compliance asset.

### 5. Soft regulation
Enabling regulation is favoured where possible, including non-binding ethical principles, standards, recommendations for voluntary adoption, and supervised and unsupervised self-regulation. Implication: today's voluntary standard is tomorrow's expectation; posture accordingly.

### 6. Multistakeholder cooperation
Regulation should result from cooperation with experts and stakeholders, including industry with an emphasis on micro, small and medium enterprises, academia, civil society organisations and the public. Implication: consultations are a real channel; watch for them and respond.

## Six Ethical Principles

The policy states these are based on the OECD AI Principles with adjustments, and that they are NOT legally binding on regulators or organisations and are not a tool for legal interpretation. They reflect elements to consider in developing and using AI and in drafting regulation.

These apply directly to developers and operators. Map each principle to concrete controls in your AI system.

### 1. AI to promote growth, sustainable development and Israeli leadership in innovation
The use of trustworthy AI should be a means to encourage growth, sustainable development and social well-being, and to advance Israeli leadership in AI innovation.
Concrete controls:
- State the business and societal purpose the system serves, in the model card
- Record the benefit case alongside the risk case, so proportionality can be argued

### 2. Human-centric AI
Concrete controls:
- Human oversight role defined with authority to override model outputs
- Fundamental rights impact assessment (similar to a fundamental rights DPIA)
- Appeal mechanism for affected individuals
- No system design that undermines dignity, autonomy, or free choice

### 3. Equality and non-discrimination
Concrete controls:
- Bias testing on protected categories (gender, ethnicity, religion, age, disability)
- Fairness metric documented per use case (demographic parity, equalized odds, or domain-specific)
- Mitigation plan for identified bias
- Periodic re-testing on live data

### 4. Transparency and explainability
Concrete controls:
- Users notified they are interacting with AI
- Synthetic content labeled
- Model card published with capabilities and limits
- Explanation of automated decisions where legally required or ethically warranted

### 5. Reliability, robustness, security and safety
Concrete controls:
- Test coverage across expected inputs and adversarial edges
- Red-teaming for GenAI systems
- Performance monitoring in production with drift detection
- Safe fallback behavior when confidence is low

### 6. Accountability
Developers, operators and users of AI should be accountable for the proper functioning of AI systems and for implementing the other ethical principles, including adopting generally accepted risk-management approaches.
Concrete controls:
- Clear owner for each AI system (named role, not just team)
- Incident response plan with escalation path
- Audit trail of training data, model versions, deployments
- Vendor accountability clauses for third-party models
- A named risk-management approach the organisation actually follows

## How to Use This in Documentation

For each AI system, create a short alignment statement mapping the six ethical principles to specific controls. Attach it to your internal governance file and include it in customer-facing AI risk review responses. Reference the policy by its full title, "Responsible Innovation: Israel's Policy on Artificial Intelligence Regulation and Ethics", and by its December 2023 publication month. It has no day-level date.

## What's Next (2026 and beyond)

The policy proposes an AI Policy Coordination Center, to be established with the Ministry of Justice as an expert inter-agency body. Its listed functions are advising sectoral regulators, promoting inter-agency coordination, leading horizontal implementation and updating the policy, advising the government and monitoring implementation, leading Israel's representation in international forums on AI regulation and standards, publishing information and tools on responsible AI innovation, and establishing consultation forums.

**Do not attribute to the Center a deliverable it has not published.** Earlier versions of this file named a "Risk Management Toolbox" with impact-assessment templates and transparency-report patterns, and a "National AI Ethics Committee". Neither appears in the policy and neither was verifiable. Track the Center's actual publications alongside those of the PPA, Bank of Israel and the Ministry of Health.

None of this changes the voluntary, sector-based baseline established in 2023.
