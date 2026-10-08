# AI Policy, Privacy & Governance

<!-- Canonical source for: DESE AI guidance, federal AI landscape, district AI policy development, academic integrity, AI data privacy, AI equity, responsible AI framework, AI governance -->
<!-- Last content review: 2026-03 -->

```mermaid
graph TD
    FED["Federal Landscape<br/>DOE, Executive Orders, DOL"]
    DESE["Missouri DESE<br/>AI Guidance v1.0"]
    MSBA["MSBA Model Policies"]
    
    FED --> DESE
    DESE --> MSBA
    DESE --> DIST

    subgraph "District Policy Development"
        DIST["District AI Task Force"]
        DIST --> POLICY["Draft AI Policy"]
        POLICY --> BOARD["Board Adoption"]
        BOARD --> IMPL["Implement & Train"]
        IMPL --> REVIEW["Annual Review"]
        REVIEW --> POLICY
    end

    subgraph "Policy Domains"
        INTEGRITY["Academic<br/>Integrity"]
        PRIVACY["Data Privacy<br/>FERPA / COPPA"]
        EQUITY["Equity &<br/>Access"]
        RESPONSIBLE["Responsible<br/>AI Framework"]
        SB68["SB 68<br/>Device Ban"]
    end

    MSBA --> DIST
    POLICY --> INTEGRITY
    POLICY --> PRIVACY
    POLICY --> EQUITY
    POLICY --> RESPONSIBLE
    POLICY --> SB68

    style DESE fill:#4a90d9,color:#fff
    style FED fill:#6c757d,color:#fff
    style BOARD fill:#5cb85c,color:#fff
    style PRIVACY fill:#d9534f,color:#fff
```

## Table of Contents
1. Missouri DESE AI Guidance
2. Federal AI in Education Landscape
3. AI Policy Development for Districts
4. AI and Academic Integrity
5. AI and Student Data Privacy
6. AI and Equity
7. Responsible AI Use Framework
8. AI Governance & Oversight
9. SB 68 Device Ban Interaction

---

## 1. Missouri DESE AI Guidance

### Overview
In 2025, DESE released its first formal guidance document for AI in education: *Artificial Intelligence Guidance for Local Education Agencies* (Version 1.0, 2025-26 school year). The document was developed by Missouri's Computer Science Advisory Council.

### DESE's Core Principles
- AI should **enhance, not replace** teacher work and human relationships
- Teachers must remain the **primary decision-makers** in the classroom
- AI tools must always be used **under human supervision**
- Districts should implement AI **gradually and thoughtfully**
- AI use must align with **Missouri Learning Standards** and current assessment frameworks

### DESE's Key Recommendations
| Area | Guidance |
|------|---------|
| **Human oversight** | Always have a human review AI-generated content for bias and accuracy |
| **Teacher role** | Teachers must continue to be the main decision-makers |
| **Cybersecurity** | Maintain strong cybersecurity practices when using AI tools |
| **Fairness** | Ensure AI tools don't reinforce bias or widen learning gaps |
| **Data privacy** | Student data privacy protections apply to all AI tools |
| **Professional development** | Districts should provide PD on assessing AI-generated content and using AI to enhance learning |
| **Local control** | Under Missouri law, each district develops its own AI policies and procedures |

### DESE's Identified Benefits of AI
- Creating practice problems and exercises
- Brainstorming and refining student writing
- Serving as a personalized tutor
- Providing immediate feedback on student work
- Individualizing instruction (cited Blue Springs elementary as an example)
- Supporting differentiated learning

### DESE's Identified Challenges
- Risk of copyright infringement and plagiarism
- Inaccuracy and hallucination in AI outputs
- Over-reliance and dependency
- Loss of human interaction
- Concerns about cheating and academic integrity
- Students unable to learn content for themselves

### Additional Missouri Policy Resources
- **MSBA (Missouri School Boards Association):** AI toolkit incorporating safety, equity, and human supervision
- **Missouri Consultants for Education (MCE):** sample AI policies for districts
- **PRiME Center (SLU):** policy brief on AI in Missouri schools with equity recommendations
- **Reference:** Gowe, S., & Morris, N. (2025). "Artificial intelligence (AI) in Missouri schools: Policy landscape and recommendations for equitable integration." Policy Research in Missouri Education, 7(23).

---

## 2. Federal AI in Education Landscape

### U.S. Department of Education
The U.S. Department of Education has taken several actions on AI in education:

**Dear Colleague Letter (2025):** guidance on leveraging federal grant funds for responsible AI integration, addressing:
- AI for personalized and differentiated instruction
- AI for college and career pathway exploration, advising, and navigation
- Principles for responsible AI adoption
- User privacy protections
- Teaching students about appropriate AI use
- Engaging parents in decisions about AI deployment

**Supplemental Grantmaking Priority (2025):** Secretary McMahon proposed AI in education as a supplemental priority for discretionary grants:
- Integrating AI literacy into teaching practices
- Expanding AI and computer science education K-12
- Supporting professional development for educators on AI and CS
- Using AI to personalize learning and differentiate instruction
- Using AI to enhance classroom efficiency and reduce administrative burden

### Executive Orders
- Executive Order on Removing Barriers to American Leadership in Artificial Intelligence
- AI literacy and workforce readiness as national priorities

### U.S. Department of Labor AI Literacy Framework (2026)
DOL published an AI Literacy Framework defining foundational knowledge areas for workers, job seekers, students, and employers — relevant to career readiness and workforce development programs.

### National Landscape (2026)
- 31+ state departments of education have released AI guidance
- States like Ohio (HB 96) and Tennessee (SB 1711) have enacted legislation requiring districts to adopt AI policies
- 52+ bills across 25 states address AI in classroom instruction (FutureEd 2026 tracker)
- Trend shifting from guidance → governance/enforcement

---


## 8. AI Policy Development for Districts

### DESE's Approach: Local Control
Missouri law allows each district to develop its own AI policies. DESE provides guidance, not mandates. Districts should develop comprehensive AI policies rather than ad-hoc reactions.

### Seven-Step Policy Development Process (Referenced in DESE Guidance)
1. **Convene an AI Task Force** — teachers, administrators, technology staff, counselors, parents, students (secondary), board members, community partners
2. **Assess current state** — what AI tools are already being used? by whom? for what? with what oversight?
3. **Review guidance** — DESE guidance, MSBA model policies, MCE samples, peer district policies, national frameworks (TeachAI, CoSN, ISTE)
4. **Draft policy** — address all key areas (see policy framework below)
5. **Gather stakeholder input** — feedback from staff, parents, students, community
6. **Board adoption** — present policy for first reading, public comment, second reading, vote
7. **Implement, train, and revise** — professional development, student education, annual policy review

### AI Policy Framework (Key Areas to Address)
| Policy Area | Key Questions |
|-------------|-------------|
| **Scope** | Which AI tools are covered? (generative AI, adaptive platforms, automated systems) Who is covered? (students, teachers, staff, administrators) |
| **Acceptable use** | What AI uses are allowed, encouraged, or prohibited? By role? By grade level? |
| **Academic integrity** | How must students disclose AI use? What constitutes misuse? What are consequences? How are assignments designed to maintain integrity? |
| **Data privacy** | How are AI vendor agreements reviewed for FERPA/COPPA compliance? What data can be entered into AI tools? What data cannot? (no student PII in public AI tools) |
| **Procurement** | How are AI tools vetted before adoption? Who approves new tools? What privacy/bias review is required? |
| **Bias and equity** | How will the district monitor AI tools for bias? How will equitable access be ensured? |
| **Professional development** | What training is required before staff use AI? What ongoing PD is provided? |
| **Student AI literacy** | How will students learn about AI (curriculum, digital citizenship)? At what grade levels? |
| **Transparency** | How will the district communicate AI use to parents and community? What opt-out rights exist? |
| **Prohibited uses** | What uses are prohibited? (e.g., AI-generated IEP goals without specialist review, AI-only grading of subjective work, AI for disciplinary decisions, AI-generated content presented as original student work without disclosure) |
| **Review cycle** | How often will the policy be reviewed and updated? (annually recommended, given pace of change) |

### Missouri District Examples
Several Missouri districts are developing AI policies:
- **Blue Springs:** early adopter of AI in elementary instruction (individualized instruction highlighted by DESE Deputy Commissioner)
- **Carl Junction:** formed a learning group with student, teacher, and parent input to develop guidelines
- Districts across the state are adapting MSBA model policies and DESE guidance to local contexts

---

## 9. AI and Academic Integrity

### The Challenge
Generative AI can produce essays, solve math problems, write code, and create presentations — making traditional assessments vulnerable to academic dishonesty.

### Policy Approaches (Spectrum)
| Approach | Description | When Appropriate |
|----------|-----------|----------------|
| **Ban** | No AI use allowed on any assignment | Rarely recommended as standalone policy (students use AI outside school regardless) |
| **Restricted** | AI use prohibited on specific assignments; allowed on others with disclosure | Most common current approach |
| **Integrated** | AI use expected and taught as a skill; assignments designed for AI-enhanced work | Emerging best practice for many tasks |
| **Transparent** | Students must document their AI use (what tool, what prompts, what was AI-generated vs. human-generated) | Recommended across all approaches |

### Assignment Design for the AI Era
Rather than trying to "catch" AI use, design assignments that are AI-resistant or AI-enhanced:

**AI-Resistant Assignments:**
- In-class handwritten essays (timed, observed)
- Oral presentations and Socratic seminars
- Lab work and hands-on demonstrations
- Portfolio-based assessment with process documentation
- Reflective journals on personal experience
- Collaborative problem-solving (observed)
- Authentic assessments tied to specific classroom experiences
- Multi-draft writing with tracked revisions and conferences

**AI-Enhanced Assignments:**
- "Use AI to generate a first draft, then critically evaluate and revise — submit both versions with analysis"
- "Compare your solution to an AI-generated solution — which is better and why?"
- "Use AI to research a topic, then fact-check every claim with primary sources"
- "Prompt AI three different ways to solve this problem — evaluate which approach is best"
- "Create an AI-generated product, then write a reflective critique of its quality"

### Detection
- AI detection tools (Turnitin, GPTZero, Originality.ai) are **unreliable** — high false positive rates, especially for ELL students and students with certain writing styles
- **Do not rely on AI detection tools** as sole evidence of academic dishonesty
- Better approach: know your students' writing, require process evidence (drafts, outlines, conferences), use authentic assessments

### Updating Academic Integrity Policies
Districts should update honor codes and academic integrity policies to:
- Define what constitutes acceptable vs. unacceptable AI use
- Require disclosure of AI assistance (what tool, what prompts, what portions)
- Distinguish between using AI as a tool (acceptable) and submitting AI work as one's own (unacceptable)
- Specify consequences for violations (aligned to existing academic integrity framework)
- Apply equitably (students with more AI access at home should not have an unfair advantage)

---

## 10. AI and Student Data Privacy

### FERPA and AI
| Rule | AI Application |
|------|---------------|
| **Student PII** | Never enter student personally identifiable information (names, IDs, grades, disability status, behavioral records) into public AI tools (ChatGPT, Gemini, etc.) |
| **Vendor agreements** | AI tools that access student data must be covered by FERPA-compliant data privacy agreements |
| **School official exception** | AI vendors may qualify as "school officials" if proper agreements are in place (direct control, legitimate educational interest, no re-disclosure) |
| **Directory information** | AI tools processing student directory information must comply with district directory information policies and opt-out rights |

### COPPA and AI
- AI tools used by students under 13 must comply with COPPA
- Schools may consent on behalf of parents for educational purposes (but must understand what data is collected)
- AI tools must not collect more data than necessary for the educational purpose
- Parents must be informed about AI tools used in classrooms

### RSMo 161.096 (Missouri Student Data Privacy)
- Prohibits use of student data for commercial purposes
- Requires transparency about data collection
- Applies to all technology vendors, including AI providers

### Practical Data Privacy Guidelines for AI
1. **Never enter student PII into public AI tools** — no names, IDs, grades, IEP information, behavioral records, or health information
2. **Use de-identified data** when using AI for analysis — remove all identifiers before processing
3. **Vet all AI tools** through the district's technology procurement process before classroom use
4. **Require data privacy agreements** with all AI vendors
5. **Train staff** on what data can and cannot be entered into AI tools
6. **Maintain a list** of approved AI tools (and communicate to staff and families)
7. **Review AI tool privacy policies** — where is data stored? who has access? is it used to train models? when is it deleted?
8. **Inform parents** about AI tools used in classrooms and their data practices

---

## 11. AI and Equity

### Equity Concerns
| Concern | Description |
|---------|-----------|
| **Access gap** | Students with home internet, devices, and paid AI tool access have advantages over students without |
| **Algorithmic bias** | AI models trained on biased data may produce biased outputs (racial, gender, socioeconomic, linguistic) |
| **Language bias** | AI tools perform better in English than in other languages; may disadvantage ELL students |
| **Cultural bias** | AI-generated content may reflect dominant cultural perspectives and underrepresent diverse viewpoints |
| **Detection bias** | AI detection tools have higher false positive rates for ELL students and non-native English speakers |
| **Disability access** | Not all AI tools are accessible to students with disabilities (screen reader compatibility, alternative input) |
| **Digital literacy gap** | Students from higher-income families may have more AI literacy from home exposure |

### Equity-Centered AI Practices
- Provide equitable access to AI tools in school (don't assume home access)
- Select AI tools evaluated for accessibility (WCAG 2.1 compliance)
- Monitor AI-generated content for bias before using with students
- Teach students to critically evaluate AI outputs for bias
- Don't penalize students who lack AI access outside school
- Ensure AI tools support multilingual learners (translation, language scaffolding)
- Review discipline and grading data for disparate impact of AI-related policies
- Include diverse stakeholders in AI policy development

---


## 15. Responsible AI Use Framework

### DESE-Aligned Responsible Use Principles
1. **Human in the loop** — every AI output reviewed by a qualified human before use
2. **Transparency** — disclose when AI is used; be honest about its role
3. **Accuracy** — verify all AI-generated content against reliable sources
4. **Privacy** — protect student data; never enter PII into public AI tools
5. **Equity** — ensure AI benefits all students; monitor for bias and access gaps
6. **Integrity** — maintain academic honesty; disclose AI assistance
7. **Safety** — age-appropriate AI exposure; content filtering; monitoring
8. **Agency** — develop student capacity to use AI critically, not dependently
9. **Relationships** — AI supplements human connection; never replaces it
10. **Continuous learning** — policies, practices, and skills evolve as technology evolves

### AI Acceptable Use Policy (Template Elements)
An AI AUP should supplement (or be integrated into) the existing technology AUP:
- Definition of AI tools covered
- Approved tools list (maintained by district technology department)
- Roles and permissions (student vs. teacher vs. administrator)
- Data privacy rules (what can/cannot be entered)
- Academic integrity expectations (disclosure requirements)
- Consequences for misuse
- Student and parent acknowledgment
- Annual review commitment

---


## 20. AI Governance & Oversight

### District-Level Governance
| Structure | Role |
|-----------|------|
| **AI Task Force / Committee** | Develop and review AI policy; recommend tools; address emerging issues |
| **Technology Director** | Vet AI tools for privacy and security; manage approved tools list; ensure infrastructure readiness |
| **Curriculum Director** | Align AI integration to Missouri Learning Standards; oversee AI literacy curriculum |
| **Building Principals** | Monitor AI use in buildings; support teacher PD; address academic integrity |
| **School Board** | Adopt AI policy; provide oversight; allocate resources |

### State-Level Governance
- **DESE:** issues guidance, provides PD, integrates AI into CS standards framework
- **DESE Computer Science Advisory Council:** developed the AI guidance; advises on AI in education
- **MSBA:** provides model AI policies for districts
- **Missouri General Assembly:** may enact legislation on AI in education (monitor annual session)

### National Governance Resources
| Organization | Resource |
|-------------|---------|
| **TeachAI (teachai.org)** | AI Guidance for Schools Toolkit — comprehensive framework |
| **CoSN (Consortium for School Networking)** | AI guidance for school technology leaders |
| **ISTE** | AI standards and competencies for students and educators |
| **CCSSO (Council of Chief State School Officers)** | State-level AI policy coordination |
| **AI for Education (aiforeducation.io)** | State-by-state guidance tracker, prompts, frameworks |

### Annual Policy Review
Given the rapid pace of AI development, AI policies should be reviewed and updated **at least annually**:
- What new AI tools have emerged?
- What new risks have been identified?
- What has worked/not worked in implementation?
- What does updated research say?
- What new state or federal guidance has been issued?
- What feedback have stakeholders provided?

---

## 9. SB 68 Device Ban Interaction

### Missouri Senate Bill 68 (Signed July 9, 2025)
Governor Kehoe signed SB 68 enacting a statewide ban on electronic communication devices in Missouri public and charter schools beginning with the 2025-26 academic year.

### Implications for AI in Education
| Area | Impact |
|------|--------|
| **Student device access** | Personal phones/devices restricted during school day; AI access shifts entirely to school-provided devices |
| **1:1 programs** | School-issued devices (Chromebooks, iPads) remain the primary student access point for approved AI tools |
| **BYOD programs** | BYOD models may need restructuring depending on how districts implement SB 68 |
| **AI tool access** | Students access AI tools only through district-managed devices with filtering and monitoring |
| **Equity impact** | Levels the playing field — all students access AI through school devices rather than personal devices with varying capabilities |
| **Policy alignment** | District AI policies must be updated to reflect SB 68 device restrictions |
| **Enforcement** | Districts must establish confiscation/storage procedures; AI policy enforcement simplified when access is device-controlled |

### Policy Coordination
Districts should ensure their AI Acceptable Use Policy and SB 68 implementation procedures are aligned and do not create contradictions. The device ban may simplify AI governance by channeling all student AI access through managed, filtered school devices.

---

→ For AI-enhanced teaching workflows, tutoring, and communication: see ai-in-education/ai-teaching-learning.md
→ For AI literacy curriculum, PD, tools, and career readiness: see ai-in-education/ai-literacy-career.md
