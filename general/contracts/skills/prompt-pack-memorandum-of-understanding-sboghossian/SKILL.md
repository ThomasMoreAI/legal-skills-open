---
name: prompt-pack-memorandum-of-understanding-sboghossian
title: Memorandum of Understanding
description: Use when drafting a memorandum of understanding (MOU) recording the intention of parties to collaborate on a project, partnership, or institutional arrangement. Carefully distinguishes binding from non-binding provisions, outlines responsibilities and timeline, and sets the path to a definitive agreement. Common in government-to-government, institutional, and early-stage commercial contexts across MENA and GCC where an MOU carries significant cultural and business weight.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-memorandum-of-understanding
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Memorandum of Understanding

## When to use this

Use this skill when parties want to document their shared intention to pursue a collaboration, project, or relationship without creating full contractual obligations at this stage. The MOU is particularly common in:
- Government-to-government and institution-to-institution arrangements
- Early-stage commercial partnerships where definitive terms are still being negotiated
- Agreements between companies that are part of the same group or ecosystem
- Academic, research, and public-private partnership collaborations

**MOU vs LOI**: An MOU tends to be less transactional and more relational — it describes a collaboration framework rather than specific economic terms. Use [[prompt-pack-letter-of-intent]] for M&A or investment transactions with specific price terms. MOUs are culturally significant in MENA business practice and are often treated by parties as morally binding even if legally non-binding.

Triggers:
- "Draft an MOU between [Company A] and [Company B] to cooperate on [project]."
- "We need a memorandum of understanding with a government ministry."
- "We want to record our intention to partner before we finalize the legal structure."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Party names and descriptions | Identifies the parties and their roles | Ask user |
| Collaboration / project description | Describes what the parties intend to do together | Ask user |
| Responsibilities of each party | Core substance of the MOU | Ask user |
| Timeline | Milestones toward definitive agreement | Ask user |
| Governing law | Determines which provisions can be binding | Ask user |

## Optional inputs

- Whether any provisions must be binding (confidentiality, exclusivity, governing law)
- Path to a definitive agreement and proposed form (JV agreement, MSA, etc.)
- Funding contributions (if any at MOU stage)
- Dispute resolution mechanism (even for non-binding MOUs, a dispute resolution clause is useful)
- Whether Arabic language version is required (critical for MOUs with government entities in UAE, KSA, LB, EG)

## Document structure

### Preamble
- Date, parties (full legal names, addresses, registration details)
- Brief description of each party's business / institutional role
- Statement of purpose: "The Parties wish to set out their mutual understanding of and intentions with respect to [describe the collaboration]."

### Recitals
- "Whereas [Party A] is [description];"
- "Whereas [Party B] is [description];"
- "Whereas the Parties wish to [describe the intended collaboration] and to record their shared intentions in this Memorandum of Understanding;"
- "Now therefore, the Parties agree as follows:" (even for a non-binding MOU, this framing is conventional)

### Article 1: Purpose
A clear, concise statement of the purpose of the MOU:
- The Parties intend to [describe the collaboration: explore a joint venture / develop a shared technology platform / cooperate on regulatory engagement / etc.]
- The MOU describes the general framework for the Parties' collaboration; it is not intended to create binding legal obligations except as expressly stated

### Article 2: Scope of Collaboration
Define the scope of the intended collaboration:
- Subject matter: what the parties will work on together
- Geographic scope
- Duration of the collaboration period described in this MOU
- Activities specifically included and (if clarity requires) activities specifically excluded

### Article 3: Responsibilities
Describe what each party undertakes to do (expressed as intentions, not obligations, unless a specific provision is meant to be binding):

**[Party A] will / intends to**:
- [Responsibility 1]
- [Responsibility 2]

**[Party B] will / intends to**:
- [Responsibility 1]
- [Responsibility 2]

**Joint responsibilities**:
- Regular coordination meetings: [frequency, format]
- Joint steering committee (if appropriate): composition, decision-making
- Communications: designated contact persons at each party

### Article 4: Timeline and Milestones
| Milestone | Target date | Responsible party |
|---|---|---|
| Execution of this MOU | [Date] | Both |
| Completion of [feasibility study / pilot / scoping exercise] | [Date] | [Party] |
| Decision point: proceed to definitive agreement or not | [Date] | Both |
| Target execution of definitive agreement | [Date] | Both |

### Article 5: Funding and Resources (if applicable)
- If each party bears its own costs: state explicitly "Each Party shall bear its own costs and expenses in connection with activities under this MOU unless separately agreed in writing."
- If there is a shared budget at MOU stage: describe it precisely.
- Note: commitments of significant expenditure should be in the definitive agreement, not the MOU.

### Article 6: Confidentiality (BINDING)
This clause should be binding. Include:
- Each party will keep confidential all information received from the other party under this MOU.
- Standard exclusions: publicly available information, independently developed, required by law.
- Duration: during MOU term plus [2 / 3] years.
- If a separate NDA is already in effect, cross-reference it here.

### Article 7: Intellectual Property
- IP created under activities described in this MOU: state whether jointly owned or owned by the creating party.
- Background IP: each party retains its own background IP.
- This article may be deliberately short at MOU stage, with full IP provisions reserved for the definitive agreement.

### Article 8: Non-Binding Nature and Exceptions
**This clause is critical.** Draft with care:

"This Memorandum of Understanding, except for the provisions of Article 6 (Confidentiality), Article [X] (Governing Law), and Article [X] (Dispute Resolution), does not constitute a legally binding agreement and creates no legal obligation on either Party. No Party shall have the right to compel the other Party to enter into any definitive agreement on the basis of this MOU."

List each binding article explicitly. Do not leave any ambiguity.

### Article 9: Path to Definitive Agreement
- The Parties intend to negotiate in good faith toward a definitive [Joint Venture Agreement / Master Services Agreement / other] by [target date].
- The definitive agreement will supersede this MOU.
- If the Parties cannot agree on the terms of a definitive agreement by [date], either Party may give written notice terminating this MOU.

### Article 10: Governing Law and Dispute Resolution (BINDING)
- Governing law — specify; this provision should be binding.
- Dispute resolution: the parties agree to attempt to resolve any dispute through good faith negotiation; if unresolved in [30] days, refer to [mediation / arbitration / courts].

### Article 11: Term and Termination
- MOU is effective from the date of execution and continues until [specific date / execution of definitive agreement / written notice by either party].
- Either party may terminate on [30-day] written notice.
- Confidentiality obligations survive termination.

### Article 12: General
- Entire agreement (within the non-binding scope of the MOU)
- Amendments: only in writing signed by authorized representatives of both parties
- No waiver; counterparts; language (Arabic and English — state which prevails)
- No agency, partnership, or employment relationship created by the MOU

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **UAE** | MOUs with UAE government entities or federal institutions often require Arabic language version; parties may treat the MOU as morally and commercially binding even if it is legally non-binding. Registration with courts or notarization is not standard for commercial MOUs. |
| **KSA** | MOUs with Saudi government ministries (e.g., under Vision 2030 partnership frameworks) are treated with high seriousness; include a clear Arabic version. |
| **France (civil law)** | Courts may find pre-contractual liability (obligation de négociation de bonne foi) if a party withdraws from negotiations after an MOU without legitimate reason. Keep the non-binding language strong. |
| **DIFC / ADGM** | Common-law approach; explicit non-binding language and the binding article list are highly effective. |
| **Lebanon** | Lebanese courts generally respect the non-binding character if it is clearly stated; however, reliance on MOU commitments can in certain circumstances support a damages claim. |

**Arabic language note**: For MOUs with government entities in UAE, KSA, or Lebanon, an Arabic version is often required for official purposes and should be prepared by a certified legal translator. Include a "in case of conflict" clause specifying which language version prevails.

## Common mistakes

- **Vague non-binding disclaimer**: "This MOU is not a contract" is not sufficient in all civil-law jurisdictions. Explicitly list which provisions are binding; do not rely on a general disclaimer.
- **Creating obligations that look like a contract**: language such as "Party A shall deliver X by [date]" creates contractual obligations even in a document labeled "MOU." Use "Party A intends to" or "it is expected that Party A will."
- **Omitting the path-to-definitive-agreement section**: without a timeline and a sunset clause, MOUs can persist indefinitely without either party advancing to a formal structure.
- **No Arabic version for government counterparties**: a unilingual English MOU with a UAE ministry will not be accepted for formal recording and may be treated as non-existent.

## Related skills

- [[prompt-pack-letter-of-intent]]
- [[prompt-pack-joint-venture-agreement]]
- [[prompt-pack-master-services-agreement]]
- [[prompt-pack-nda-strength-check]]
- [[heuristic-always-state-jurisdiction-first]]
