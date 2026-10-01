---
name: inst-legal-aid-routing-sboghossian
title: Inst — Legal Aid Routing
description: Use when a user cannot afford a lawyer or explicitly asks about free legal help, pro bono services, or legal aid programs across MENA jurisdictions (KSA, UAE, LB, EG) and international organizations (UNHCR, NGOs). Routes consumers and vulnerable individuals to the appropriate government legal aid scheme, bar association clinic, court-appointed counsel program, or specialized aid organization based on geography, legal issue type, and vulnerability profile. P1 access-to-justice function; activates when income or vulnerability flags are present.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/inst/inst-legal-aid-routing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Inst — Legal Aid Routing

## Purpose

Legal aid routing connects individuals who cannot access paid legal counsel to free or subsidized services: government legal aid schemes, bar association clinics, court-appointed defense, specialized NGOs, and international organizations. This skill is a core access-to-justice function — it operates whenever Louis detects that a user's legal need is urgent and affordability or vulnerability is a barrier.

---

## When to use this

- User explicitly says they cannot afford a lawyer
- User asks "where can I get free legal help" or equivalent in Arabic, French, English
- Matter involves an individual (not a business) facing housing eviction, criminal charge, domestic violence, wage theft, or immigration status
- User is identified (or self-identifies) as a refugee, asylum seeker, or stateless person
- Emergency flag: user mentions detention, arrest, imminent deportation, or physical safety risk
- Downstream from [[justice-human-handoff]] when handoff requires a free resource

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| User's country / emirate / governorate | Yes | Determines which programs apply |
| Legal issue type | Yes | Family / housing / criminal / labor / immigration / other |
| User vulnerability profile | Yes | Low-income / refugee / DV victim / detained / minor |
| Urgency level | Yes | Emergency (24h) / Standard (days-weeks) |
| Language preference | Optional | Arabic / English / French; affects which resources to surface |

---

## Logic

### Step 1: Jurisdiction detection
Map user location to available programs:
- **KSA** → Ministry of Justice legal aid + bar-appointed counsel + specialized programs
- **UAE** → Ministry of Justice legal aid + emirate-level centers + Dubai/Abu Dhabi mediation
- **LB** → Beirut Bar + Tripoli Bar clinics + NGO ecosystem
- **EG** → Egyptian Bar Syndicate bureaus + NGO + court-appointed defense
- **Cross-border / stateless** → UNHCR regional offices + international human rights organizations

### Step 2: Issue type categorization
| Issue Type | Priority Programs |
|---|---|
| Criminal defense (detained) | Court-appointed counsel; emergency bar duty solicitor |
| Family (divorce, custody, domestic violence) | Bar clinics; DV shelters with legal arms; family courts' free advice desks |
| Housing / eviction | Tenancy courts' mediation services; bar clinics; community legal centers |
| Labor / wage theft | Ministry of Labor complaints; labor court free representation (KSA, UAE) |
| Immigration / asylum / refugee | UNHCR + IOM + local partners; specialized immigration legal aid |
| Consumer / debt | Bar clinics; financial ombudsman (UAE: Central Bank; KSA: SAMA) |

### Step 3: Vulnerability amplifiers
Increase routing priority and surface emergency contacts when:
- User mentions physical danger, abuse, or threats
- User is a minor (under 18)
- User is detained or facing imminent court appearance
- User is a refugee or stateless (route to UNHCR first)
- User has language barrier beyond Arabic/French/English

### Step 4: Resource output
Return structured list:
1. Primary resource (most suitable program)
2. Secondary resource (backup / alternative)
3. Emergency hotline if urgency = emergency
4. Intake steps (documents needed, how to apply)
5. Estimated wait time where known

---

## MENA legal aid programs reference

### KSA
| Program | Provider | Eligibility | Scope |
|---|---|---|---|
| MOJ Legal Aid | Ministry of Justice | Low-income; court-determined | Civil, personal status, criminal defense |
| Bar-appointed counsel | Saudi Bar Association | Criminal cases; court mandate | Criminal defense |
| HRSD labor mediation | Ministry of HR & Social Dev. | Workers in employment disputes | Labor complaints, wage recovery |
| Family protection centers | Ministry of Social Affairs | DV victims + families | Family law + protection orders |

### UAE
| Program | Provider | Eligibility | Scope |
|---|---|---|---|
| MOJ Legal Aid | Federal MOJ | UAE nationals + residents; means test | Civil, family, criminal |
| Dubai Legal Aid | Dubai Courts | Low-income; Dubai residents | All civil + family matters |
| Abu Dhabi Judicial Dept. | ADJD | Low-income; Abu Dhabi | Civil, family, criminal |
| DIFC Courts Pro Bono | DIFC Courts | Parties before DIFC Courts; means test | Commercial, employment |
| DV / shelter services | Ewaa Foundation (Abu Dhabi); Dubai Shelter | DV victims | Immediate shelter + legal referral |

### Lebanon
| Program | Provider | Eligibility | Scope |
|---|---|---|---|
| BBA Legal Aid Committee | Beirut Bar Association | Low-income; Beirut + Mount Lebanon | Civil, family, criminal |
| TBA Legal Aid | Tripoli Bar Association | Low-income; North + Bekaa | Civil, family, criminal |
| UNHCR Lebanon | UNHCR + legal partners | Refugees, asylum seekers | Status determination, documentation |
| Insan Association | Lebanese NGO | Migrant workers, DV victims | Labor, DV, immigration |
| Legal Agenda | Lebanese NGO | Public interest cases | Rights litigation |

### Egypt
| Program | Provider | Eligibility | Scope |
|---|---|---|---|
| Syndicate Legal Aid Bureau | Egyptian Bar Syndicate | Low-income; means-tested | Civil, family, criminal |
| Judicial Ministry aid | MOJ | Criminal cases; court mandate | Criminal defense |
| CEWLA | NGO | Women + children | Family, DV, inheritance |
| UNHCR Egypt | UNHCR + partners | Refugees + asylum seekers | Status determination, legal orientation |
| Refugee Legal Aid | RLA (Cairo) | Refugees in Egypt | Status, documentation, detention |

### International / cross-border
- **UNHCR**: refugee status determination, protection, country-of-asylum legal orientation
- **IOM**: migration-related legal assistance, stranded migrant support
- **Human Rights Watch / Amnesty**: documentation, not direct legal aid
- **Terre des Hommes**: child protection legal support

---

## Emergency protocols

If urgency = emergency (arrest, detention, imminent deportation, active DV, self-harm):
1. Surface emergency hotline number first (before any routing)
2. Advise user of their immediate rights (right to remain silent, right to counsel, right to notify family)
3. Provide duty-solicitor / on-call bar contact for jurisdiction
4. Only then provide full legal aid routing
5. Log handoff flag for [[justice-human-handoff]]

---

## Output format

```json
{
  "jurisdiction": "UAE-Dubai",
  "issue_type": "labor",
  "urgency": "standard",
  "primary_resource": {
    "name": "Dubai Courts Legal Aid",
    "contact": "800-COURTS (26877)",
    "url": "https://www.dc.gov.ae/",
    "intake_docs": ["Emirates ID", "Proof of income", "Employment contract"]
  },
  "secondary_resource": { ... },
  "emergency_hotline": null,
  "notes": "Labour disputes may also be filed directly via MOHRE (1800 60); faster for wage recovery claims.",
  "caveat": "Program availability and eligibility criteria change; verify directly with the organization."
}
```

---

## Limits

- Louis provides routing and orientation only — it does not provide legal representation
- Program eligibility thresholds and capacity change frequently; always advise users to call/visit to confirm
- For matters requiring immediate court appearances, always escalate to [[justice-human-handoff]]

---

## Related skills

- [[inst-eg-bar-syndicate]]
- [[inst-lb-bar-association-integration]]
- [[intel-a2j-gap]]
- [[justice-human-handoff]]
- [[inst-notary-integration-mena]]
