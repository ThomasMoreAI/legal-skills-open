# Access to Education

**A comprehensive Missouri K-12 education navigator powered by AI.**

Answers questions, generates documents, and walks through complex processes for students, parents, teachers, specialists, principals, school staff, and district administrators -- grounded in Missouri law (RSMo 160-178), IDEA, ESSA, and DESE guidance.

[![Version](https://img.shields.io/badge/version-7.1.0-blue)]()
[![Files](https://img.shields.io/badge/files-71-green)]()
[![Words](https://img.shields.io/badge/words-120%2C759-orange)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

```mermaid
graph TD
    A[User Query] --> B{Role Detection}
    B --> C[Student]
    B --> D[Parent]
    B --> E[Teacher]
    B --> F[Specialist]
    B --> G[Principal]
    B --> H[Staff]
    B --> I[District Admin]
    C & D & E & F & G & H & I --> J{Quick Answer?}
    J -->|Yes| K[Immediate Response]
    J -->|No| L[Load Reference Files]
    L --> M{Need a Document?}
    M -->|Yes| N[templates/]
    M -->|No| O{Need Calculation?}
    O -->|Yes| P[scripts/calculators.md]
    O -->|No| Q[Role-Adapted Answer]
    N & P & Q --> R[Response with Citations]
```

---

## What It Does

| Capability | Details |
|-----------|---------|
| **Role-adaptive answers** | Detects who is asking (student, parent, teacher, specialist, principal, staff, admin) and shapes the tone, structure, and depth accordingly |
| **Quick-answer layer** | 35+ instant answers to the most common questions -- no lookup needed |
| **22 slash commands** | `/rights`, `/graduation`, `/letter`, `/iep-check`, `/crisis`, `/comply`, `/retire`, and more |
| **50+ document templates** | Parent letters, IEP checklists, CSIP plans, safety plans, lesson plans, board presentations |
| **5 calculators** | PSRS retirement, A+ eligibility, graduation credits, SPED timelines, funding estimates |
| **5 decision trees** | Learning disability evaluation, suspension/expulsion, IEP vs 504, A+ troubleshooting, complaint mechanism |
| **Bilingual support** | Full Spanish parent rights guide and bilingual response mode |
| **70+ verified URLs** | Direct links to DESE portals, federal resources, and Missouri-specific tools |

---

## Quick Start

**New to this?** See the **[Getting Started Guide](GETTING_STARTED.md)** for detailed step-by-step setup instructions.

### Option 1: Claude Code (recommended)

Clone the repo and open it in [Claude Code](https://claude.ai/code). The `CLAUDE.md` file activates the skill automatically.

```bash
git clone https://github.com/dougdevitre/access-to-education.git
cd access-to-education
claude
```

Then just ask a question:

```
> My child was suspended for 10 days. What are our rights?
> /graduation
> Can I retire? I'm 52 with 30 years in.
> Mi hijo necesita una evaluacion. Que hago?
```

### Option 2: Claude Project

1. Create a new [Claude Project](https://claude.ai)
2. Paste the contents of `SKILL.md` as the **custom instructions**
3. Upload everything in `references/`, `templates/`, `scripts/`, and `examples/` as **project knowledge**
4. Start chatting

### Option 3: API / Custom Integration

Use `MANIFEST.json` as the routing layer. It maps every topic to its canonical reference file, making it straightforward to build retrieval-augmented generation (RAG) pipelines or chatbot backends.

---

## Commands

Users can type these commands or just describe what they need in natural language.

| Command | What it does |
|---------|-------------|
| `/start` | New user intake -- detects role, explains capabilities |
| `/rights` | Parent rights lookup by topic |
| `/letter [type]` | Generate a parent letter (evaluation, records, IEP meeting, dispute, 504) |
| `/graduation [name]` | Walk through a graduation credit audit |
| `/iep-check` | IEP compliance checklist review |
| `/policy [type]` | Draft a district policy (AI, discipline, bullying, attendance, device) |
| `/csip` | Build a Comprehensive School Improvement Plan |
| `/safety-plan` | Build an Emergency Operations Plan |
| `/threat` | Document a threat assessment (CSTAG) |
| `/comply [month]` | Show compliance deadlines for a given month |
| `/crisis [type]` | Crisis response protocol -- immediate action steps first |
| `/lookup [statute]` | Look up a Missouri education statute |
| `/retire` | PSRS/PEERS retirement eligibility calculator |
| `/a-plus` | A+ eligibility troubleshooting |
| `/translate [text]` | Translate education content to Spanish |
| `/compare [X vs Y]` | Compare two processes (e.g., IEP vs 504) |
| `/district [name]` | Look up a Missouri school district |
| `/enroll [situation]` | Enrollment for special situations (homeless, foster, military) |
| `/data [report]` | Data reporting help by MOSIS cycle |
| `/pd [topic]` | Professional development guidance |
| `/walkthrough [journey]` | Step-by-step scenario walkthrough |
| `/evaluate [topic]` | Quick evaluation on any topic |

---

## Repository Structure

```
access-to-education/
|
|-- SKILL.md                     # Core behavioral system (the "operating system")
|-- CLAUDE.md                    # Auto-activates the skill in Claude Code
|-- MANIFEST.json                # Machine-readable index of all files and topics
|-- CANONICAL_OWNERS.md          # Which file owns which topic (prevents duplication)
|-- LAST_VERIFIED.md             # Data verification log with sources and dates
|-- CHANGELOG.md                 # Version history
|
|-- commands/
|   `-- COMMANDS.md              # 22 slash command definitions
|
|-- references/
|   |-- roles/                   # 7 files -- one per audience
|   |   |-- students.md          #   Graduation, A+, discipline, FERPA, attendance
|   |   |-- teachers.md          #   Certification, MEES, tenure, PD, salary
|   |   |-- specialists.md       #   IEP, 504, IDEA categories, ELL, FBA, transition
|   |   |-- building-leaders.md  #   CSIP, staff eval, safety, Title I ops
|   |   |-- school-staff.md      #   Paraprofessionals, nurses, bus, mandated reporting
|   |   |-- administrators.md    #   MSIP 6, funding, board, ESSA, charter
|   |   `-- school-counseling.md #   ASCA model, caseload, college advising
|   |
|   |-- operations/              # 10 files -- how schools run
|   |   |-- assessments.md       #   MAP, EOC, ACT, WIDA, accommodations
|   |   |-- crisis-emergency.md  #   EOP, active threat, drills, reunification
|   |   |-- discipline-behavior.md # PBIS, restorative, bullying, seclusion
|   |   |-- health-wellness.md   #   Mental health, SEL, suicide prevention
|   |   |-- technology-digital-learning.md # 1:1, CIPA, SB 68 device ban
|   |   |-- athletics-activities.md #  MSHSAA, concussion, Title IX athletics
|   |   |-- career-pathways.md   #   CTE, dual credit, apprenticeships
|   |   |-- data-reporting.md    #   MOSIS, Core Data, APR
|   |   |-- facilities-operations.md # ADA, capital planning, lead/asbestos
|   |   `-- school-culture-climate.md # Surveys, belonging, equity audit
|   |
|   |-- compliance/              # 5 files -- law, policy, funding, deadlines
|   |   |-- mo-education-law.md  #   RSMo 160-178, DESE rules, case law
|   |   |-- compliance-calendar.md # Month-by-month requirements
|   |   |-- governance-policy.md #   Board policy, Sunshine Law, superintendent eval
|   |   |-- funding-programs.md  #   State formula, Title I-IV, Perkins, E-Rate
|   |   `-- equity-access.md     #   McKinney-Vento, foster, migrant, Title IX
|   |
|   |-- programs/                # 8 files -- populations and programs
|   |   |-- special-populations.md # Military, immigrant, teen parents, LGBTQ+
|   |   |-- early-childhood.md   #   Pre-K, Head Start, First Steps, PAT
|   |   |-- alternative-education.md # Virtual/MOCAP, homebound, GED, credit recovery
|   |   |-- family-community.md  #   Engagement, community schools, volunteers
|   |   |-- educator-workforce.md #  PSRS/PEERS, shortages, loan forgiveness
|   |   |-- professional-learning.md # PLCs, coaching, micro-credentials
|   |   |-- rural-education.md   #   Consolidation, 4-day week, shared services
|   |   `-- mo-districts-regions.md # District lookup, RPDC regions, demographics
|   |
|   |-- ai-in-education/         # AI in schools
|   |   |-- INDEX.md             #   Router -- read this first
|   |   |-- ai-teaching-learning.md # AI for instruction, tutoring, communication
|   |   |-- ai-policy-governance.md # DESE guidance, academic integrity, privacy
|   |   `-- ai-literacy-career.md   # K-12 AI literacy, PD, career readiness
|   |
|   |-- curriculum-instruction/  # Standards and teaching
|   |   |-- INDEX.md             #   Router -- read this first
|   |   |-- mo-learning-standards.md # ELA, math, science, SS, fine arts, CS
|   |   `-- instructional-practice.md # Science of Reading, differentiation, SBG
|   |
|   |-- special-needs/           # Disability-specific depth
|   |   |-- INDEX.md             #   Router -- read this first
|   |   |-- vision-impairment.md #   Braille, TVI, O&M, CVI, MSB, ECC
|   |   |-- hearing-impairment.md #  ASL, cochlear implants, interpreters, MSD
|   |   `-- motor-impairment.md  #   OT, PT, adaptive PE, AT, wheelchair access
|   |
|   |-- glossary.md              # 150+ education acronyms and terms
|   |-- faq.md                   # Top 10 pre-built answers per role
|   |-- links-and-resources.md   # 70+ verified URLs
|   |-- scenario-walkthroughs.md # 10 complete journey narratives
|   |-- mo-data-tables.md        # 17 structured lookup tables
|   `-- guia-padres-espanol.md   # Full Spanish parent rights guide
|
|-- templates/                   # 50+ document templates by role
|   |-- parent/                  #   5 letter templates (eval, records, IEP, dispute, 504)
|   |-- admin/                   #   CSIP, AI policy, safety plan, threat assessment, + 8 more
|   |-- specialist/              #   IEP checklist, 504 plan, FBA
|   |-- teacher/                 #   Lesson plan, PD growth plan
|   |-- counselor/               #   Graduation audit, college planning, crisis screening
|   `-- staff/                   #   Mandated reporter, new employee orientation
|
|-- scripts/
|   `-- calculators.md           # 5 calculators (retirement, A+, credits, timelines, funding)
|
|-- examples/
|   `-- sample-outputs.md        # 8 example responses showing target quality (all roles)
|
`-- evals/
    `-- test-cases.json          # 30 test cases across all roles for validation
```

---

## How It Works

The system follows an 11-step process defined in `SKILL.md`:

1. **Detect the role** -- identify who is asking
2. **Check quick-answer layer** -- if it's a common factual question, answer immediately
3. **Apply role recipe** -- shape tone, structure, and depth for the audience
4. **Route to reference files** -- only load files when depth is needed
5. **Reach for templates** -- when the user wants to build a document
6. **Apply guardrails** -- sensitive topics get caveats or redirects
7. **Hand off** -- when the question leaves education, acknowledge and redirect
8. **Walk decision trees** -- for multi-step processes with branching logic
9. **Anticipate follow-ups** -- proactively ask the one question most likely to change the answer
10. **Generate documents** -- produce actual letters, plans, and forms
11. **Respond bilingually** -- Spanish support with English legal terms preserved

---

## Example Interactions

**Parent asking about suspension rights:**
> "My son was suspended for 10 days and the principal said it might be extended. He has ADHD and a 504 plan. What are my rights?"

The system responds with: immediate rights under RSMo 167.161, the MDR requirement before extension, the two MDR questions, what happens under each outcome, specific next steps with exact language to use, and an offer to draft the request letter.

**Teacher asking about retirement:**
> "I'm 52 with 30 years in. Can I retire?"

The system calculates Rule of 80 (52 + 30 = 82), confirms eligibility, estimates the benefit at 75% of final average salary, flags the Social Security/WEP issue, and directs to PSRS.

**Spanish-speaking parent:**
> "Mi hijo necesita ayuda en la escuela pero no se por donde empezar."

The system responds entirely in Spanish, includes English legal terms in parentheses, explains the evaluation request process, provides letter language in both languages, and notes the right to an interpreter at school meetings.

---

## Data Integrity

All facts are sourced and tracked:

- **Missouri statutes** (RSMo) verified as of 2025-08
- **Federal law** (IDEA, ESSA, FERPA, Title IX) verified as of 2025-08
- **DESE guidance** verified as of 2026-03
- **Volatile data points** (enrollment, contribution rates, scholarship amounts) tracked with source and date in `LAST_VERIFIED.md`
- **Quarterly review cycle** for high-volatility items; annual for medium; 5-year for low
- **Legislative review** due after each Missouri session (next: June 2026)

See `LAST_VERIFIED.md` for the full verification log.

---

## Contributing

Each topic has a single canonical owner file (see `CANONICAL_OWNERS.md`). To update a fact:

1. Find the canonical file for the topic
2. Update the fact with the new source and date
3. Update `LAST_VERIFIED.md` with the verification date
4. Cross-references in other files will point back to the canonical file

### Content Guidelines

- Cite statutes precisely (e.g., RSMo 167.161, IDEA SS300.301)
- Frame legal content as educational information, not legal advice
- Keep files under 500 lines
- Use the existing voice: calm, professional, practical, child-centered, equity-conscious

---

## Version History

| Version | Date | Highlights |
|---------|------|-----------|
| 7.1.0 | 2026-03-28 | Repo restructure, CLAUDE.md for Claude Code activation |
| 7.0.0 | 2026-03-28 | Pod architecture, 22 commands, 50+ templates, calculators, evals |
| 6.0.0 | 2026-03-28 | Decision trees, follow-up anticipation, document generation, Spanish support |
| 5.0.0 | 2026-03-28 | Operating system refactor, role recipes, guardrails, quality checklist |
| 4.0.0 | 2026-03-28 | AI in education (DESE guidance, federal landscape, 20 sections) |
| 3.0.0 | 2026-03-28 | 9 new domains (counseling, governance, crisis, PD, culture, compliance calendar) |
| 2.0.0 | 2026-03-28 | 12 new domains (early childhood, athletics, health, CTE, rural, and more) |
| 1.0.0 | 2026-03-28 | Initial release (11 files, core domains) |

See `CHANGELOG.md` for full details.

---

## Maintainer

**Doug Devitre** -- [dougdevitre](https://github.com/dougdevitre)
