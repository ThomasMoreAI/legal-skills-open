---
name: environmental-law-judicialmind
title: Environmental Law
description: Environmental law skill for environmental regulations and compliance. Use when the user needs assistance with EPA compliance, environmental permits, contamination, CERCLA, Clean Air Act, Clean Water Act, NEPA, or ESG matters. Triggers on keywords like "environmental", "EPA", "pollution", "contamination", "hazardous waste", "CERCLA", "Superfund", "Clean Air", "Clean Water", "NEPA", "remediation", "permit", "ESG".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/environmental-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
sources:
- title: Cercla Liability
  path: references/cercla-liability.md
- title: Due Diligence
  path: references/due-diligence.md
- title: Permitting Guide
  path: references/permitting-guide.md
---

# Environmental Law

This skill provides expert guidance for environmental regulatory compliance, transactions, and litigation.

## Core Capabilities

### 1. Environmental Compliance
- Permitting
- Regulatory compliance
- Reporting requirements
- Audit protocols

### 2. Contaminated Properties
- Site assessment
- Remediation
- Liability allocation
- Brownfields redevelopment

### 3. Transactional Due Diligence
- Environmental assessments
- Liability allocation
- Representations and warranties
- Indemnification

### 4. Environmental Litigation
- Enforcement defense
- Cost recovery
- Citizen suits
- Toxic torts

## Major Environmental Statutes

### Federal Environmental Laws
| Statute | Agency | Focus |
|---------|--------|-------|
| CERCLA (Superfund) | EPA | Hazardous substance cleanup |
| RCRA | EPA | Hazardous waste management |
| Clean Air Act | EPA | Air quality standards |
| Clean Water Act | EPA | Water pollution control |
| NEPA | Various | Environmental review |
| TSCA | EPA | Chemical substances |
| EPCRA | EPA | Emergency planning, reporting |
| SDWA | EPA | Drinking water |
| ESA | FWS/NMFS | Endangered species |
| FIFRA | EPA | Pesticides |

## CERCLA (Superfund)

### Potentially Responsible Parties (PRPs)
1. **Current owners/operators** of facility
2. **Past owners/operators** at time of disposal
3. **Arrangers** (generators who arranged for disposal)
4. **Transporters** who selected the site

### Liability Framework
- **Strict liability**: No fault required
- **Joint and several**: One party can be liable for all
- **Retroactive**: Applies to past disposal

### Defenses and Exemptions
| Defense | Requirements |
|---------|--------------|
| Innocent landowner | No knowledge, appropriate inquiry |
| Bona fide prospective purchaser | Post-disposal acquisition, due diligence |
| Contiguous property owner | Contamination from neighboring property |
| Third-party defense | No contractual relationship, due care |
| Security interest | Holding security, not participating |
| Act of God | Unforeseeable natural disaster |
| Act of war | War-related cause |

### Response Actions
**Removal**: Short-term, emergency cleanup
**Remedial**: Long-term, permanent remedy

### CERCLA Liability Allocation
- **Orphan shares**: Cost of insolvent/defunct parties
- **Contribution**: §113(f) action among PRPs
- **Cost recovery**: §107(a) action against PRPs
- **Private party actions**: Recovery of response costs

## RCRA (Hazardous Waste)

### Cradle-to-Grave Regulation
```
Generation → Transportation → Treatment/Storage/Disposal
```

### Hazardous Waste Characteristics
| Characteristic | Code | Test |
|----------------|------|------|
| Ignitability | D001 | Flash point < 140°F |
| Corrosivity | D002 | pH ≤ 2 or ≥ 12.5 |
| Reactivity | D003 | Unstable, explosive |
| Toxicity | D004-D043 | TCLP test |

### Listed Wastes
- **F List**: Non-specific source
- **K List**: Source-specific
- **P List**: Acute hazardous (commercial chemicals)
- **U List**: Toxic (commercial chemicals)

### Generator Categories
| Category | Generation Rate | Requirements |
|----------|-----------------|--------------|
| Large Quantity | > 1,000 kg/month | Full RCRA compliance |
| Small Quantity | 100-1,000 kg/month | Modified requirements |
| Very Small Quantity | < 100 kg/month | Reduced requirements |

### TSD Facility Requirements
- Permit (Part A and Part B)
- Financial assurance
- Groundwater monitoring
- Closure/post-closure care
- Contingency planning
- Personnel training

## Clean Air Act

### National Ambient Air Quality Standards (NAAQS)
| Pollutant | Criteria |
|-----------|----------|
| Ozone | Ground-level smog |
| Particulate Matter (PM2.5, PM10) | Particle pollution |
| Carbon Monoxide | Combustion emissions |
| Sulfur Dioxide | Fossil fuel burning |
| Nitrogen Dioxide | Vehicle/power plant emissions |
| Lead | Industrial emissions |

### Permitting Programs
| Program | Applicability | Key Features |
|---------|---------------|--------------|
| Title V | Major sources | Operating permits, annual fees |
| PSD | New major sources in attainment areas | BACT, ambient analysis |
| NSR | New/modified major sources in non-attainment | LAER, offsets |
| Minor NSR | Minor sources | State-specific |

### Mobile Source Standards
- Tier 3 vehicle standards
- Heavy-duty vehicle standards
- Renewable fuel standards
- Fuel quality standards

## Clean Water Act

### NPDES Permits
**Point Source Discharges** to waters of the US require permit

**Permit Requirements**:
- Technology-based limits (BAT, BCT, BPT)
- Water quality-based limits
- Monitoring and reporting
- Best management practices

### Categories of Dischargers
| Category | Requirements |
|----------|--------------|
| Direct industrial | Individual NPDES permit |
| Indirect industrial | Pretreatment, categorical standards |
| Municipal | POTW permit, pretreatment program |
| Stormwater | General or individual permit |

### Stormwater Permits
**Coverage Required**:
- Construction (> 1 acre disturbance)
- Industrial facilities (SIC codes)
- Municipal separate storm sewer systems (MS4s)

**Requirements**:
- SWPPP (Stormwater Pollution Prevention Plan)
- BMPs (Best Management Practices)
- Monitoring
- Inspections

### Wetlands (Section 404)
**Jurisdictional Wetlands**:
- Waters of the US
- Adjacent wetlands
- Other waters meeting connectivity test (*Sackett*)

**Permit Types**:
- Individual permits (complex projects)
- General permits (routine activities)
- Nationwide permits (specific categories)

## NEPA

### NEPA Review Process
```
Proposed Federal Action →
Categorical Exclusion? (No significant impact) →
Environmental Assessment (EA) →
FONSI (Finding of No Significant Impact)? →
Environmental Impact Statement (EIS) →
Record of Decision (ROD)
```

### EIS Requirements
1. Purpose and need
2. Alternatives analysis (including no action)
3. Affected environment
4. Environmental consequences
5. Mitigation measures
6. Public comment and response

### Triggers for NEPA
- Federal agency action
- Federal funding
- Federal permits
- Federal property

## Environmental Due Diligence

### Phase I Environmental Site Assessment (ASTM E1527-21)
**Purpose**: Identify recognized environmental conditions (RECs)

**Components**:
- Records review
- Site reconnaissance
- Interviews
- Report

**Findings Categories**:
- **REC**: Recognized Environmental Condition
- **CREC**: Controlled REC (addressed but controls required)
- **HREC**: Historical REC (no longer significant)
- **De minimis**: Not significant

### Phase II Assessment
**Purpose**: Confirm or rule out RECs through sampling

**May Include**:
- Soil sampling
- Groundwater sampling
- Soil gas analysis
- Building materials testing

### Transaction Considerations
| Issue | Approach |
|-------|----------|
| Known contamination | Remediation escrow, indemnity |
| Unknown contamination | Environmental insurance |
| Regulatory compliance | Permit transfer, compliance audit |
| Historical operations | Records review, Phase I |

## ESG and Climate

### ESG Reporting Frameworks
| Framework | Focus |
|-----------|-------|
| SEC Climate Rules | Public company disclosure |
| TCFD | Climate-related financial risks |
| GRI | Comprehensive sustainability |
| SASB | Industry-specific metrics |
| CDP | Carbon disclosure |

### Climate Risk Categories
- **Physical risks**: Extreme weather, sea level rise
- **Transition risks**: Policy, technology, market shifts
- **Regulatory risks**: Emissions standards, carbon pricing

### Emissions Categories
| Scope | Description |
|-------|-------------|
| Scope 1 | Direct emissions from owned sources |
| Scope 2 | Indirect from purchased energy |
| Scope 3 | Value chain emissions |

## Integration with Other Skills

- **real-estate**: Environmental issues in transactions
- **corporate-ma**: Environmental due diligence
- **litigation**: Environmental enforcement defense
- **compliance-tracking**: Permit and reporting compliance
- **regulatory-compliance**: Multi-media compliance

## Reference Files

For detailed guidance:
- `references/cercla-liability.md` - Superfund liability analysis
- `references/permitting-guide.md` - Environmental permit requirements
- `references/due-diligence.md` - Phase I/II ESA procedures
