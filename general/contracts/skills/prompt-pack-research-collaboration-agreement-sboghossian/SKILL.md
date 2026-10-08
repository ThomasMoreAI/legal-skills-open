---
name: prompt-pack-research-collaboration-agreement-sboghossian
title: Research Collaboration Agreement
description: Use when two or more institutions or companies need to formalize a joint research arrangement, covering research scope, funding contributions, personnel, IP ownership (background IP, foreground IP, and jointly developed IP), publication rights, and commercialization terms. Particularly relevant for MENA universities, government research centers, and companies collaborating with international partners, where IP ownership and technology transfer rules intersect with local R&D incentive frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-research-collaboration-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Research Collaboration Agreement

## When to use this

Use this skill when:
- A university research center and a company are entering a sponsored research or collaborative research arrangement.
- Two companies are jointly developing a new technology or product, with both contributing researchers, resources, and know-how.
- A government-funded research institute (e.g., UAE's ADNOC Research Centre, Saudi Aramco research partnerships, KAUST collaborations) is partnering with a private-sector entity.
- A startup is receiving research services from a university lab and wants to ensure IP ownership is clearly allocated.
- An existing collaboration needs a formal agreement to replace a letter of intent or MOU.

**Note on related documents:** For a pure IP license (one party grants rights to use existing IP), use [[prompt-pack-technology-licensing-agreement]] instead. For transfer of IP ownership (one party permanently transfers technology), use [[prompt-pack-technology-transfer-agreement]]. This skill covers the collaborative development scenario where new IP is being created jointly.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Identity and type of each collaborating party** | University vs. company vs. government body — each has different IP ownership rules | Ask; university IP policies vary dramatically |
| **Description of the research project** | Defines scope of collaboration and what IP may be created | Ask |
| **Funding structure** | Who pays what, how, and whether this is sponsored research (company funds university work) or co-funded | Ask; affects IP ownership defaults |
| **Existing IP each party brings (Background IP)** | Must be identified to avoid disputes about whether new IP built on it is jointly owned | Ask each party to list their relevant Background IP categories |
| **Jurisdiction(s)** | IP law (patent, copyright, know-how protection), governing law, and enforcement differ materially | Ask; for MENA parties, default to UAE if the lead institution is UAE-based |

## Optional inputs

- **Publication embargo period** — researchers want to publish; industry partners want to protect patentability and trade secrets; negotiate before drafting.
- **Commercialization model** — licensing vs. spinout vs. assignment; affects how foreground IP rights are structured.
- **Student/researcher IP rights** — universities must ensure the agreement does not assign individual researchers' IP without their consent per applicable employment/academic policy.
- **Export control compliance** — if the technology falls under dual-use controls (ITAR, EAR, EU dual-use Regulation), the agreement must restrict access and transfer accordingly.

## Document structure

1. **Recitals / Background** — state each party's expertise, the complementarity of contributions, and the purpose of the collaboration.

2. **Definitions** — critical for this document type:
   - **Background IP**: IP owned or controlled by a party before the collaboration or developed outside it; typically licensed in for project use only.
   - **Foreground IP** (Project IP): IP created in the course of the research project.
   - **Jointly Developed IP**: Foreground IP to which both parties have made inventive/creative contributions.
   - **Solely Developed IP**: Foreground IP created solely by one party's personnel.
   - **Know-how**: unpatented technical knowledge, methods, processes, and data generated in the project.
   - **Publication**: any academic paper, conference presentation, thesis, or public disclosure of results.

3. **Scope of collaboration**
   - Detailed description of the research project (attach a Work Plan or Research Plan as Schedule 1).
   - Each party's obligations and contributions (personnel, resources, facilities, data).
   - Project governance: Joint Steering Committee (JSC) composition, meeting frequency, decision-making, deadlock resolution.
   - Milestones and deliverables schedule.

4. **Funding and financial terms**
   - Amount and payment schedule (lump sum, milestone-linked, or quarterly installments).
   - Permitted use of funding (direct research costs only vs. indirect/overhead recovery).
   - Reporting obligations (financial reports, audit rights).
   - VAT / tax treatment.
   - What happens to unspent funds on termination.

5. **Intellectual property — the core provision**

   ### Background IP
   - Each party retains ownership of its Background IP.
   - Each party grants the other a non-exclusive, royalty-free license to use its Background IP solely for the purposes of the project.
   - Background IP license does not extend to commercialization; separate license negotiation required.

   ### Foreground IP — Solely Developed
   - IP created solely by Party A's personnel: owned by Party A (standard university position: university owns; company position: they want ownership or exclusive license).
   - Negotiate: for sponsored research, companies often require ownership of all Foreground IP or an exclusive license back; universities may insist on retaining ownership with an exclusive license to the sponsor.
   - Common compromise: university retains ownership; company gets an exclusive commercialization license in a defined field/territory for a defined period.

   ### Foreground IP — Jointly Developed
   - Owned jointly by both parties in proportion to inventive contribution (or 50/50 by default in many civil-law jurisdictions).
   - **Civil-law trap (UAE, LB, EG, FR):** In civil-law systems, a co-owner of jointly owned IP can exploit the IP independently without the other co-owner's consent (unlike English law where co-owners need consent). Address this explicitly: require the other party's written consent before any commercialization of Jointly Developed IP, or structure it as an undivided interest with defined commercialization governance.
   - Commercialization of Jointly Developed IP: managed by which party? With what revenue split?

   ### Patents and Registrations
   - Who files patents on Foreground IP? Inventor-named party typically files; costs shared.
   - Which countries to file in?
   - Right to prosecute: if the owning party abandons a patent application, the other party may step in.

   ### Know-how and Data
   - Ownership of raw data generated in the project.
   - Access rights post-project.
   - Data management plan (GDPR / UAE PDPL if personal data involved).

6. **Publication rights**
   - University party typically has the right to publish research results.
   - Company party typically wants a pre-publication review period to:
     - File patent applications before public disclosure (patentability is destroyed by prior publication in most jurisdictions).
     - Identify and redact trade secrets.
   - Standard embargo: 30–90 days (company review) before submission; 6 months before publication is a longer negotiated position.
   - University retains the right to publish even if company objects, after the embargo period — but may need to redact company confidential information.

7. **Confidentiality**
   - Project-specific confidentiality obligations.
   - Interplay with Background IP confidentiality: background IP disclosed for project purposes is confidential even if not separately marked.
   - Post-termination survival period: typically 3–5 years.

8. **Term and termination**
   - Fixed term aligned with the Research Plan duration.
   - Right to terminate for material breach (with cure period).
   - Right to terminate for convenience (with notice and financial consequences).
   - Effect of termination on IP: each party retains rights in IP developed before termination; wind-down obligations.

9. **Representations and warranties**
   - Each party: has authority to enter; Background IP does not infringe third-party rights to its knowledge; personnel assigned to the project are appropriately qualified.
   - University: IP policy permits this type of agreement; student/researcher assignments in place.

10. **Liability and indemnification**
    - Mutual cap on indirect/consequential damages.
    - Mutual indemnity for third-party IP infringement claims arising from Background IP.
    - No indemnity for claims arising from one party's own negligence or breach.

11. **Governing law, dispute resolution, and jurisdiction** — per jurisdiction preference; arbitration typically preferred for cross-border collaborations.

12. **Schedules**
    - Schedule 1: Research Plan and Work Packages
    - Schedule 2: Background IP list (each party's)
    - Schedule 3: Financial terms and budget
    - Schedule 4: Joint Steering Committee terms of reference

## Jurisdictional notes

### UAE
- UAE Federal Law No. 38 of 2021 on Copyright and Related Rights and Patent Law Federal Law No. 11 of 2021 govern IP ownership.
- UAE Patent Law: ownership of IP created by an employee in the course of employment belongs to the employer unless the contract provides otherwise. Adapt for contractor/researcher relationships accordingly.
- No academic research exemption equivalent to the Bayh-Dole Act (US) or UK Lambert Toolkit; university IP policies vary; check each UAE university's IP commercialization policy.

### KSA
- Saudi Patent Law (Royal Decree M/27 of 2004, amended): employer owns IP created by employee in the course of employment.
- King Abdulaziz City for Science and Technology (KACST) has specific IP protocols for government-funded research.
- KAUST (King Abdullah University of Science and Technology) has an established IP and commercialization policy; reference it for agreements involving KAUST researchers.

### EU
- EU research collaborations often use the "Lambert Toolkit" model agreements (UK) or ERA-NET / Horizon Europe model consortium agreements.
- The Horizon Europe Grant Agreement requires specific IP management plans; model consortium agreements are available from the European Commission.
- GDPR applies to any personal data processed in the research.

### UK
- UK Lambert Agreements (Lambert Model Agreements) are standard for university-industry collaborations; consider whether to adopt them for UK-institution parties.
- Employee inventor rights under the Patents Act 1977: employee may claim compensation if the invention is of outstanding benefit to the employer.

## Drafting standards

- The IP ownership provisions are the most negotiated and most important section; spend the most drafting effort here.
- Always define Background IP by reference to a schedule, not just generically — disputes about what is "background" vs. "foreground" are common and expensive.
- Use the term "Foreground IP" consistently; do not mix with "project IP," "new IP," "collaboration IP" — choose one term and use it throughout.
- For civil-law parties: address the co-ownership exploitation issue explicitly rather than relying on default civil-law rules (which allow co-owners to exploit independently).
- Include a data management plan or reference to one — increasingly required by funders and regulators.

## Common mistakes

- **Vague scope of collaboration.** If the Work Plan is not attached and the scope is not bounded, disputes arise about which IP is in-scope Foreground IP and which is out-of-scope Background IP.
- **No patent filing procedure.** The agreement must answer: who files, who pays, what is the deadline before publication destroys patentability?
- **Ignoring student IP rights.** PhD students' IP may not be automatically assigned to the university; check the university's policy and whether students need to sign separate IP assignments.
- **Publication embargo too short.** 30 days is often insufficient for a patent application to be filed; 90 days is more realistic; 6 months is safest.
- **No commercialization governance for Jointly Developed IP.** Leaving "we will agree in good faith" for commercialization terms is a recipe for deadlock.

## Related skills

- [[prompt-pack-technology-licensing-agreement]]
- [[prompt-pack-technology-transfer-agreement]]
- [[prompt-pack-software-license-agreement]]
- [[prompt-pack-standard-nda]]
- [[heuristic-always-state-jurisdiction-first]]
