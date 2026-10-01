# TPRM Cross-Framework Control Mapping

## ISO/IEC 27001:2022 Annex A (5.19–5.23)
- **5.19 Information security in supplier relationships** — processes to manage security risks from use of supplier products/services; the programme-level control (policy, tiering, inventory).
- **5.20 Addressing information security within supplier agreements** — relevant security requirements established and agreed with each supplier (contract addenda).
- **5.21 Managing information security in the ICT supply chain** — extend requirements down the ICT product/service supply chain (fourth parties, components).
- **5.22 Monitoring, review and change management of supplier services** — ongoing monitoring, service review, handling supplier-side changes.
- **5.23 Information security for use of cloud services** — acquisition, use, management and EXIT from cloud services per requirements.

## SOC 2 — CC9.2
"The entity assesses and manages risks associated with vendors and business partners." Points of focus include establishing vendor requirements, assessing vendor risk, assigning accountability, communication and exception handling, performance assessment, and termination procedures — a complete TPRM lifecycle in one criterion.

## NIS2 — Art. 21(2)(d) and 21(3)
Supply chain security as one of the ten minimum measures, "including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." Art. 21(3): take into account vulnerabilities specific to each direct supplier and the overall quality of products and cybersecurity practices, including secure development. Practical reference: ENISA Technical Implementation Guidance v1.0 (June 2025).

## DORA — Chapter V (financial entities)
- **Art. 28**: ICT third-party risk as part of ICT risk management; strategy on ICT third-party risk; **Register of Information (Art. 28(3))** covering all ICT third-party contractual arrangements (first regulator submissions April 2025); pre-contract due diligence; exit strategies for critical/important functions (Art. 28(8)).
- **Art. 29**: concentration risk — including how easily the provider can be substituted and multi-vendor dependencies.
- **Art. 30**: mandatory contract provisions (30(2) all arrangements: service descriptions, data locations, protection, access/audit, termination rights; 30(3) enhanced for critical/important functions: full audit and access rights, exit assistance, TLPT participation, notice periods).
- **Arts. 31+**: EU oversight of designated **CTPPs** — first list published November 18, 2025 (major cloud providers included). If your vendor is a CTPP, note it in the register and concentration analysis.

## HIPAA — Business Associates
- **45 CFR 164.308(b)(1)**: a covered entity may permit a business associate to create/receive/maintain/transmit ePHI only with satisfactory assurances (a BAA); **164.308(b)(2)** extends the same requirement between BAs and subcontractors — the chain flows down.
- **45 CFR 164.314(a)**: BAA content — BA complies with the Security Rule; ensures subcontractors agree to the same; reports security incidents (and breaches per 164.410).
- A GDPR DPA does not satisfy HIPAA; health-data vendors need a BAA (and vice versa).

## GDPR — Art. 28
Processor engagements need a binding contract covering: documented instructions; confidentiality; Art. 32 security; sub-processor authorisation (28(2): specific or general written authorisation with objection opportunity) and identical flow-down (28(4)); assistance with data subject rights and Arts. 32–36; deletion/return at end; audits and inspections. Processor remains fully liable to the controller for sub-processor failures.

## Using this table
When a customer asks "what do we have to do about vendors," identify their applicable frameworks first, then present the union of obligations with the strictest interpretation as the programme baseline — one TPRM programme, many citations.
