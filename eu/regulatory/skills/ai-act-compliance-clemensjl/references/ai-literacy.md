# AI literacy — Art 4

Basis: Regulation (EU) 2024/1689 Art 4, as replaced by Regulation (EU) 2026/1744 Art 1(5). Applicable since **2 February 2025**.

This is the only obligation in the Regulation that binds **every provider and every deployer of every AI system**, at every risk class, with no threshold and no exception. It is also the one most often missed, because it does not attach to a classification.

## Current text

Art 4 as replaced:

> 1. Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used. This obligation does not require providers or deployers to guarantee any specific level of AI literacy of any individual.
>
> 2. The Commission and the Member States shall support and facilitate the efforts of providers and deployers of AI systems, in particular SMEs, in fulfilling their obligation under paragraph 1 of this Article. For that purpose, the Commission shall publish practical examples of how to comply with that obligation on the single information platform referred to in Article 62(3), point (b).
>
> 3. The Board shall adopt recommendations, taking into account European competence frameworks, to support the Commission and Member States in the promotion of AI literacy required under paragraph 1, including by setting out common objectives.

## What changed in 2026, and what did not

The original Art 4 required providers and deployers to "take measures to their best extent to **ensure** a sufficient level of AI literacy of their staff". The replacement changes the standard from **ensure a sufficient level** to **take measures to support the development** of AI literacy, and adds an explicit disclaimer that no specific level need be guaranteed for any individual.

Recital 8 of Reg (EU) 2026/1744 gives the reason: stringent obligations to *ensure* a sufficient level were not suitable for all types of providers and deployers, and created disproportionate compliance burden particularly for smaller enterprises.

What did **not** change:

- The obligation still exists, and still binds every provider and deployer.
- It still covers "other persons dealing with the operation and use of AI systems on their behalf" — contractors, agency staff, outsourced support teams.
- It is still contextual: calibrated to the audience's technical knowledge, experience, education and training, to the context of use, and to the persons or groups **on whom** the systems are used.
- Member States still lay down penalties under Art 99(1) for infringements of the Regulation by operators; Art 99(3), (4) and (5) do not set a specific tier for Art 4, so the residual national regime applies.

`AI literacy` is defined in Art 3(56): skills, knowledge and understanding that allow providers, deployers and affected persons, taking into account their respective rights and obligations, to make an informed deployment of AI systems, as well as to gain awareness about the opportunities and risks of AI and possible harm it can cause.

## A defensible minimal programme

The obligation is one of means, not result. A programme that a market surveillance authority can inspect needs to be documented, differentiated and dated. Six elements:

1. **A register of AI systems in use**, with role (provider or deployer), risk class, and the population that operates or is affected by each. This is the same inventory as in `artefacts-records.md`; the literacy programme is scoped from it, not from headcount.
2. **Audience segmentation**, with different content per group. At minimum four: everyone; people who operate an AI system in their work; people who build or configure AI systems; people who exercise human oversight over a high-risk system. The last group has a separate, stricter basis in Art 26(2) — necessary competence, training and authority — and must not be collapsed into general awareness training.
3. **Content per segment**, tied to what the person actually does:
   - everyone: what AI systems the organisation uses, what they can and cannot do, the internal acceptable-use rules, how to escalate a suspected malfunction or harm;
   - operators: the intended purpose and known limitations of the specific system, the instructions for use, the escalation path under Art 26(5), what the logs record;
   - builders: classification triggers under Arts 5, 6 and 50, the Art 25 role flip, documentation duties;
   - oversight personnel: automation bias, how to interpret outputs, how to override, how to stop the system (Art 14(4)(b), (c), (d), (e)).
4. **Delivery and record**: date, audience, content version, attendance, and the material itself retained. Undated training is not evidence.
5. **Refresh trigger**, not just an annual cadence: a new AI system, a substantial modification, a model swap, a new risk class, a serious incident.
6. **Ownership**: a named person accountable for the programme, and a named person per system who can answer what it does.

Sources that can be cited as reference points rather than invented: the Commission is required under Art 4(2) to publish practical examples on the single information platform under Art 62(3)(b) — the AI Act Service Desk; the Board is to adopt recommendations under Art 4(3) taking into account European competence frameworks, with the Digital Competence Framework for Citizens (DigComp) and the AI Literacy Framework for Primary and Secondary Education named in recital 8 of Reg (EU) 2026/1744. [[UNVERIFIED: whether the Commission's practical examples under Art 4(2) and the Board's recommendations under Art 4(3) have been published as at 2026-08-05]]

## What does not discharge Art 4

- A clause in the employment contract.
- A one-off all-hands presentation with no record.
- An acceptable-use policy on the intranet, unaccompanied by any measure to develop understanding.
- Vendor-supplied product training alone, where the vendor's material covers the tool but not the organisation's own AI systems, limitations and escalation paths.
- Training only the engineers, where non-engineers operate the systems.

## Boundary

This file covers Art 4 only. Training obligations that arise elsewhere are separate and stricter: Art 26(2) competence, training and authority for human oversight of high-risk systems; Art 14(4) design duties on the provider so that oversight persons **can** understand and intervene; Art 9(5)(c) provision of training to deployers as a risk management measure.

## Checkpoints

- [ ] Art 4 treated as applying to every AI system in the organisation, including minimal-risk ones
- [ ] Contractors and outsourced staff who operate AI systems included
- [ ] Audience segments defined, with different content per segment
- [ ] Human oversight personnel trained under Art 26(2) separately from general awareness
- [ ] Every session dated, with audience, content version and attendance recorded
- [ ] Refresh triggered by new systems, model swaps, substantial modifications and incidents, not only by calendar
- [ ] Named owner for the programme and per system
- [ ] No claim made that any specific literacy level is guaranteed — the amended Art 4(1) expressly does not require it
