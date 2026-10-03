# DPIA Template (Article 35)

A Data Protection Impact Assessment is required when processing is "likely to result in a high risk to the rights and freedoms of natural persons" (Art. 35(1)). When in doubt, do one — the cost is low and the documentation is reusable.

## When a DPIA is mandatory (Art. 35(3) + EDPB)

- Systematic and extensive evaluation including profiling with legal/significant effects.
- Large-scale processing of special category data or criminal data.
- Systematic monitoring of publicly accessible areas on a large scale.
- EDPB's nine criteria (likely high-risk if ≥2 apply): evaluation/scoring; automated decision-making with legal effect; systematic monitoring; sensitive data; large scale; matching/combining datasets; data on vulnerable subjects; innovative use of technology; preventing data subjects from exercising rights.

National DPAs publish lists of processing operations that *always* require a DPIA. Check the relevant DPA's list.

## DPIA template sections

1. **Description of processing**
   - Nature: what data, what operations
   - Scope: data subject categories and counts, geographic scope
   - Context: relationship with subjects, public expectations
   - Purposes: business goals, lawful basis (link to Article 6 / 9)
2. **Necessity and proportionality**
   - Why is the processing necessary for the purpose?
   - Can the purpose be achieved with less data, less identifiability, shorter retention?
   - Lawful basis justification + LIA if applicable.
3. **Consultation**
   - Internal: DPO opinion, security, legal, product
   - External: data subjects (where appropriate); regulator (if Art. 36 prior consultation required)
4. **Risk assessment** (per risk):
   - Source of risk
   - Nature of potential harm
   - Likelihood (low / medium / high)
   - Severity (low / medium / high)
   - Overall risk rating
5. **Measures to address risks**
   - Technical: pseudonymisation, encryption, access controls, deletion automation
   - Organisational: training, contracts, governance
   - Demonstrate residual risk is acceptable
6. **Sign-off**
   - DPO advice (Art. 35(2))
   - Approver (controller representative)
   - Date and review schedule

## Article 36 — prior consultation

If, after the DPIA, residual risk remains *high*, the controller must consult the supervisory authority *before* processing. DPA response time: typically 8 weeks (extendable).

## Common DPIA scenarios

| Scenario | Why a DPIA |
|---|---|
| AI candidate-screening tool | Profiling + automated decision-making with legal/significant effect |
| Workplace monitoring software | Systematic monitoring + employer/employee imbalance |
| Health-tech app collecting symptoms | Special category data at scale |
| Marketing analytics combining first-party + third-party data | Matching/combining datasets, often without expectation |
| Smart-camera analytics in a retail store | Systematic monitoring of public areas |

## Living document

DPIAs are not "one and done." Re-assess when:

- Purpose or scope changes
- New data sources added
- New vendors added
- Risk landscape shifts (incident, regulator guidance, new tech)
- Annual minimum review

Link the DPIA to the corresponding ROPA entry (`references/ropa-template.md`) so they evolve together.
