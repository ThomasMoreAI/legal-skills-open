# EU AI Act Risk Classification

## Table of Contents
1. [Prohibited Practices (Art. 5)](#prohibited-practices)
2. [High-Risk AI Systems (Annex III)](#high-risk-ai-systems)
3. [Limited Risk (Art. 50)](#limited-risk)
4. [Minimal Risk](#minimal-risk)
5. [Classification Decision Tree](#classification-decision-tree)

---

## Prohibited Practices

Article 5 bans the following AI practices (in force since February 2, 2025):

1. **Subliminal manipulation**: AI that deploys subliminal techniques beyond a person's consciousness to materially distort behavior, causing significant harm
2. **Exploitation of vulnerabilities**: AI targeting specific groups (age, disability, social/economic situation) to distort their behavior in a harmful way
3. **Social scoring**: AI evaluating/classifying people based on social behavior or personal characteristics, leading to detrimental treatment unrelated to the context in which data was generated
4. **Real-time remote biometric identification** in publicly accessible spaces for law enforcement (with narrow exceptions)
5. **Emotion recognition** in workplaces and educational institutions (with exceptions for medical/safety reasons)
6. **Untargeted scraping** of facial images from internet or CCTV to build facial recognition databases
7. **Biometric categorization** inferring race, political opinions, trade union membership, religious beliefs, sex life or sexual orientation (with narrow law enforcement exceptions)
8. **Individual risk assessment for criminal offenses** based solely on profiling or personality traits (except as supplement to human assessment based on objective facts)

## High-Risk AI Systems

Annex III lists the categories. An AI system is high-risk if it falls into one of these areas AND poses a significant risk of harm:

### Category 1: Biometrics (where permitted)
- Remote biometric identification (non-real-time)
- Biometric categorization by sensitive attributes
- Emotion recognition systems

### Category 2: Critical infrastructure
- Safety components of critical infrastructure (water, gas, heating, electricity, transport)
- Road traffic management
- Supply of water, gas, heating, electricity

### Category 3: Education and vocational training
- Determining access to or assignment in educational institutions
- Evaluating learning outcomes
- Assessing the appropriate level of education
- Monitoring prohibited behavior during tests

### Category 4: Employment and workers management
- Recruitment and selection (CV screening, interview assessment)
- Decisions on promotion, termination, task allocation
- Monitoring and evaluating performance and behavior

### Category 5: Access to essential services
- Creditworthiness assessment / credit scoring
- Risk assessment for life and health insurance
- Eligibility evaluation for public benefits and services
- Dispatching emergency first response services
- Risk assessment and pricing for natural persons in life/health insurance

### Category 6: Law enforcement
- Individual risk assessment (assessing risk of offending/reoffending)
- Polygraphs and similar tools
- Evaluating evidence reliability
- Profiling in criminal investigations

### Category 7: Migration, asylum and border control
- Polygraphs and similar tools during interviews
- Risk assessment (security, irregular migration, health risks)
- Assisting in examination of applications for asylum/visa/residence
- Detecting/identifying/recognizing persons in border management

### Category 8: Administration of justice
- AI systems assisting judicial authorities in researching, interpreting facts and law
- AI systems applying the law to concrete facts

**Important exception (Art. 6(3))**: An AI system in an Annex III area is NOT high-risk if it does not pose a significant risk of harm to health, safety, or fundamental rights, specifically if:
- It performs a narrow procedural task
- It improves the result of a previously completed human activity
- It detects decision-making patterns without replacing human assessment
- It performs a preparatory task to an assessment relevant for the Annex III use cases

This exception is important for informational tools and data presentation systems.

## Limited Risk

Article 50 applies to AI systems that:
- **Interact directly with people** (chatbots, virtual assistants) → must disclose AI nature
- **Generate or manipulate content** (text, images, audio, video) → must mark content as AI-generated
- **Generate deepfakes** → must disclose artificial origin
- **Perform emotion recognition or biometric categorization** → must inform affected individuals

## Minimal Risk

All other AI systems. No specific obligations under the AI Act, but:
- AI literacy (Art. 4) still applies to any organization using AI
- Voluntary codes of conduct are encouraged (Art. 95)
- GPAI model obligations (Chapter V) apply to the model provider regardless of downstream risk classification

## Classification Decision Tree

```
Is the AI system in Article 5 prohibited list?
├─ YES → PROHIBITED. Must not be deployed.
└─ NO → Continue

Does the AI system fall into an Annex III category?
├─ YES → Does it pose significant risk of harm? (check Art. 6(3) exception)
│   ├─ YES → HIGH-RISK
│   └─ NO (narrow procedural, preparatory, or pattern-detection task) → Continue
└─ NO → Continue

Does the AI system interact with people, generate content, or detect emotions?
├─ YES → LIMITED RISK (Art. 50 transparency obligations)
└─ NO → MINIMAL RISK (only Art. 4 AI literacy applies)
```
