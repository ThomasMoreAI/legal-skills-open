# Questionnaire Domain Library & Contract Clause Bank

## Questionnaire design principles
Scale by tier (Tier 1: full domains + evidence; Tier 3: ~25 screening questions). Every question: (a) closed question, (b) evidence request, (c) framework citation. Never reproduce licensed SIG content (Shared Assessments SIG 2026: Core ~600+ questions for critical vendors, Lite ~125–130 baseline; issuers license it, responders don't) — generate original questions in the same domain-organised style.

## Domain library (generate questions from these)
1. **Governance & programme** — security policy ownership, framework certifications held (ISO 27001 cert scope + SoA, SOC 2 period + categories), cyber insurance.
2. **Access control** — MFA coverage (workforce + privileged + remote), joiner/mover/leaver SLAs, privileged access management, customer-data access model and logging.
3. **Data protection** — encryption in transit/at rest (key management), data locations/residency options, segregation model, retention and deletion (incl. backups), test-data practices.
4. **Application & infrastructure security** — SDLC controls, dependency/SBOM practice, vulnerability management SLAs (crit/high patch windows), penetration test cadence + summary sharing, cloud hardening baseline.
5. **Detection & response** — 24/7 monitoring, incident response plan + testing, CUSTOMER NOTIFICATION SLA and channel, breach history (3 years).
6. **Resilience** — RTO/RPO, backup architecture + restore testing, DR test results, status page and incident comms.
7. **Sub-processors / fourth parties** — list + locations, change notification lead time, flow-down of equivalent obligations, concentration on hyperscalers.
8. **Integration risk** — OAuth scopes requested, token storage/rotation, webhook security, least-privilege API design (post-Salesloft Drift, treat OAuth grants as Tier-1 questions for any integrated SaaS).
9. **People** — screening, security training, insider risk, secure remote work.
10. **Compliance specifics** — per applicable regime: GDPR Art. 28 terms + transfer mechanisms; HIPAA BAA willingness; PCI AOC/ROC; DORA Art. 30 acceptance for critical functions.

## Contract security addendum clause bank (tier-scaled)
1. Security programme aligned to a named framework, no material degradation during term.
2. Certifications/reports: annual SOC 2 Type II (or ISO cert + SoA) delivery within N days of issuance; right to review exceptions and require remediation plans.
3. Breach/incident notification: notify without undue delay and no later than [24–72h] of confirming an incident affecting customer data; cooperation with the customer's regulatory clocks (GDPR 72h, HIPAA 60-day outer bound, DORA/NIS2 support).
4. Sub-processors: current list, [30]-day advance change notice, objection right, equivalent flow-down, liability retained.
5. Access control: MFA for all access to customer data; personnel screening; least privilege; access logs preserved [12] months and available on request.
6. Data handling: encryption standards, locations, no use beyond services (incl. no model training without written consent), return + certified deletion within [30] days of termination incl. backup expiry timeline.
7. Audit rights: questionnaire annually; on-site/virtual audit on reasonable notice (or reliance on independent reports + right of inquiry); regulator access where the customer is DORA/NIS2/HIPAA regulated (DORA Art. 30(3) full set for critical/important functions).
8. Vulnerability management: crit/high remediation windows; pen test summaries on request.
9. Business continuity: RTO/RPO commitments; DR testing; termination assistance for [90–180] days.
10. Liability: security/privacy breach carve-out or super-cap at [2–5×] fees (negotiation guidance, not legal advice).
