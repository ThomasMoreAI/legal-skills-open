---
name: draft-sla-sboghossian
title: Service Level Agreement (SLA)
description: Use when drafting a Service Level Agreement specifying measurable performance commitments, uptime guarantees, response and resolution times, service credits, and exclusions. Typically attached as a schedule to an MSA or SOW, or incorporated into a cloud/SaaS subscription agreement. Addresses the core commercial tension between provider-side credit-as-sole-remedy and client-side termination rights for sustained underperformance. Applies across technology, managed services, outsourcing, and infrastructure agreements in any jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-sla
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Service Level Agreement (SLA)

An SLA translates the service provider's performance commitments into measurable, contractually binding obligations tied to consequences (service credits, termination rights) when those commitments are not met. Without an SLA, "high availability" and "prompt support" are marketing claims, not legal obligations.

## When to use this

- Cloud infrastructure, SaaS, or managed IT services
- Outsourced business processes (BPO, legal process outsourcing, finance function)
- Telecommunications and connectivity services
- Data center colocation
- Customer support and helpdesk services
- Any services contract where downtime, response speed, or quality thresholds matter commercially

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Service description | Defines what is being measured; vague descriptions = measurement disputes | Must provide; refer to SOW if this is a schedule |
| Availability / uptime target | The core commitment; industry standard by tier below | 99.9% unless agreed otherwise |
| Response time SLA | How quickly the provider acknowledges an incident | Varies by priority tier |
| Resolution time SLA | How quickly the incident is resolved | Varies by priority tier |
| Measurement methodology | How uptime is measured; who provides the data | Provider's monitoring tool, with right for Client to audit |
| Service credit formula | What the Client gets if the SLA is missed | Graduated by miss severity |
| Exclusions | Events outside Provider's control | Planned maintenance (with notice), force majeure, Client-caused outages |

## Standard Uptime Tiers

| SLA target | Allowed downtime per month | Annual downtime allowance | Typical use |
|---|---|---|---|
| 99.5% | ~3.65 hours | ~43.8 hours | Basic services; non-critical |
| 99.9% ("three nines") | ~43 minutes | ~8.7 hours | Standard SaaS / cloud |
| 99.95% | ~22 minutes | ~4.4 hours | Business-critical applications |
| 99.99% ("four nines") | ~4.4 minutes | ~52 minutes | Mission-critical; financial / healthcare |
| 99.999% ("five nines") | ~26 seconds | ~5 minutes | Telco-grade; real-time financial |

Downtime calculation methodology matters as much as the target: is it measured as a rolling 30-day window, a calendar month, or an average over a quarter? Provider's own monitoring vs independent third-party tool? Define this precisely.

## Incident Priority Classification

| Priority | Definition | Response time (target) | Resolution time (target) |
|---|---|---|---|
| P1 — Critical | Complete service outage; all users affected | 15 minutes | 4 hours |
| P2 — High | Major feature unavailable; significant user impact | 1 hour | 8 hours |
| P3 — Medium | Feature degraded; workaround available | 4 hours | 48 hours |
| P4 — Low | Minor issue; cosmetic or informational | 1 business day | 10 business days |

Response time = time from incident report to first substantive acknowledgment by Provider.
Resolution time = time from incident report to full restoration or accepted workaround.

## Document Structure

### 1. Service Description
Reference the relevant SOW or describe the service in enough detail to scope what is and is not covered. SaaS application, API endpoints, data pipeline, support desk — specify each component separately if they have different SLA targets.

### 2. Service Levels

For each service metric, specify:
- Target (numerical)
- Measurement window (calendar month / rolling 28-day window)
- Measurement method (monitoring tool, ticket timestamps, synthetic probes)
- Reporting (monthly report from Provider; raw data on request; Client's right to audit the measurement methodology)

### 3. Service Credits

Credit formula (graduated):
| Availability (monthly) | Credit (% of monthly fees) |
|---|---|
| ≥99.9% | 0% |
| 99.0%–99.9% | 5% |
| 98.0%–99.0% | 10% |
| 95.0%–98.0% | 20% |
| <95.0% | 25% |

Credits are applied against the next invoice. They are calculated on the fees attributable to the affected service component, not total contract value, unless otherwise agreed.

### 4. Credit Cap and Application

- **Credit cap**: maximum credits in any calendar month (typically 25–30% of monthly fees for that service)
- **Application method**: auto-credit vs claim-based (Client must submit a credit request within 30 days of the miss); auto-credit is more Client-friendly
- **Exclusivity question** (see critical section below)

### 5. Termination Right for Sustained Underperformance

Client's right to terminate without cause penalty if SLA is materially and persistently missed:
- Trigger: SLA below [X%] for [3] consecutive calendar months
- Process: Client gives written notice; Provider has 30 days to cure; if not cured, Client may terminate and receive pro-rated refund of prepaid fees
- This clause is strongly resisted by Providers but is critical for Clients in long-term contracts

### 6. Exclusions

Events that pause or toll SLA measurement:
- Scheduled maintenance (typically 4–8 hours per month, with 72-hour notice; some contracts allow weekend-only maintenance windows)
- Force majeure events (war, natural disaster, pandemic — define per the principal agreement)
- Client-caused outages (Client's infrastructure failure, Client configuration errors, Client-requested changes)
- Third-party service failures outside Provider's control (upstream ISP, third-party APIs); limit this exclusion — if Provider chose the third-party dependency, it should bear the risk
- DDoS attacks (typically excluded for the first 30 minutes; Provider must have mitigation)

### 7. Reporting

- Monthly SLA report: delivered within 5 business days of month-end; must include uptime %, incident log (P1/P2), credit calculation if applicable
- Incident post-mortems: root cause analysis for each P1 incident within 5 business days of resolution
- Annual SLA review: parties review SLA targets and methodology annually; either party may propose adjustments; changes require written agreement

### 8. Governing Law and Dispute Resolution

Same as the principal MSA; disputes on SLA calculations first to a designated technical escalation contact, then to the dispute resolution process in the MSA.

## Critical Commercial Tension: Credits vs Termination

| Position | Provider's preference | Client's preference |
|---|---|---|
| Credits as remedy | Credits are the **sole and exclusive** remedy for SLA misses; Provider not liable for consequential loss | Credits are one remedy; Client may also claim damages for losses caused by the outage |
| Credit cap | Capped at 25% of monthly fees; credits may not exceed actual loss | No cap; credits should reflect real impact |
| Termination right | No termination right for SLA misses alone | Termination right after 3 consecutive months of material miss |
| Credit window | Client must claim within 30 days | Auto-credit; no claim period |

**Negotiation guidance**: for mission-critical services, Client should insist on: (a) rejection of "sole and exclusive remedy" language (or at minimum a carve-out for gross negligence and wilful misconduct), (b) a termination right after sustained underperformance, and (c) auto-credit with no claim period.

## Jurisdictional Notes

### MENA context
UAE and KSA do not have specific SLA legislation. SLAs are enforced as ordinary contract terms. UAE Federal Decree-Law 5/1985 (Civil Transactions Law, "UAE Civil Code") and KSA's rules on performance of obligations apply. Under UAE civil law, a limitation of liability (credits as sole remedy) may be challenged if it is found to be unconscionable or contrary to public order — though courts generally uphold commercial parties' bargains.

### EU / GDPR
Where the service involves personal data, the SLA must be read alongside the Data Processing Agreement (DPA). Article 32 GDPR imposes a duty on processors to implement appropriate technical and organizational security measures; SLA uptime and incident response times feed into this duty.

### DIFC / ADGM
English-law contract principles apply. Limitation of liability clauses are enforceable subject to DIFC Contract Law restrictions on unreasonable exclusion clauses for death / personal injury.

## Common Mistakes

- **Uptime defined over wrong period** — monthly measurement produces credits for a 3-day outage; annual measurement can absorb a significant outage without triggering credits; monthly is Client-standard
- **"Commercially reasonable efforts" response time** — not measurable; always use objective time commitments
- **No incident priority definitions** — without a classification system, every outage is disputed
- **Maintenance window not capped** — "reasonable maintenance windows" without a monthly hour cap gives Provider unlimited downtime excuse
- **No post-mortem obligation** — P1 incidents without root-cause analysis repeat

## Related skills

- [[draft-msa]]
- [[draft-sow]]
- [[draft-sow-extension]]
- [[review-msa-client-side]]
- [[draft-schedule-annex-builder]]
