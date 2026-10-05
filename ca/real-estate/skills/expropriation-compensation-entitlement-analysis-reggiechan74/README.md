# Expropriation Compensation Calculator

**Ontario Expropriations Act** - Legal entitlement to compensation analysis

## Overview

Calculates legal entitlement to expropriation compensation under the Ontario Expropriations Act, including:

1. **Market Value (s.13 OEA)**
   - Valuation date determination (earlier of Form 7 service or plan registration)
   - Highest and best use valuation
   - Special purchaser premium exclusion

2. **Disturbance Damages (s.18 OEA)**
   - Moving costs and relocation expenses
   - Business losses (revenue losses during reasonable relocation period)
   - Professional fees (legal, appraisal, accounting)
   - Temporary accommodation costs
   - Trade fixtures (depreciated value, NOT salvage value)

3. **Injurious Affection (s.18(2) OEA)**
   - Construction impacts (s.18(2)(a) - temporary): Noise, dust, vibration, traffic
   - Permanent use impacts (s.18(2)(b) - capitalized): Ongoing noise, visual obstruction, privacy loss, stigma

4. **Interest Calculation**
   - Pre-judgment interest from valuation date to payment
   - Current Ontario statutory rate: 3.0% annual

5. **OEA Compliance Validation**
   - Identifies compensable vs. non-compensable items
   - Flags goodwill claims (NON-compensable under s.18(3))
   - Validates but-for test, reasonableness, foreseeability

## Legal Framework

### Market Value (s.13 OEA)

**Principle**: Fair market value = price willing buyer and willing seller agree in open market

**Valuation Date Rule (s.13(2))**: Earlier of:
- Form 7 notice of expropriation service date, OR
- Expropriation plan registration date

**Highest and Best Use**: Property valued at optimal legal use (zoning-permitted), not current use

**Special Purchaser Premium**: **EXCLUDED** - Premium unique buyer would pay above general market (e.g., assemblage, strategic location)

**Example**:
- Current use: Farm ($10,000/acre)
- Zoning: Industrial
- Highest and best use: Industrial development ($120,000/acre)
- **Entitlement**: Industrial value (highest and best use), NOT farm value

### Disturbance Damages (s.18 OEA)

**Legal Tests**:
1. **Causation (But-For Test)**: "But for the expropriation, would owner have incurred this cost?"
2. **Reasonableness**: Owner has duty to mitigate - no gold-plated solutions
3. **Foreseeability**: More liberal than tort - broadly foreseeable consequences compensable

**Compensable Items**:
- Moving costs (professional movers, packing, storage)
- Business relocation (revenue losses during **reasonable relocation period** - typically 6-12 months)
- Professional fees (legal, appraisal, accounting at **reasonable rates**)
- Temporary accommodation (apartment preferred over hotel - mitigation duty)
- Trade fixtures (depreciated replacement cost)
- Re-establishment costs (signage, marketing, permits)

**NON-Compensable Items (s.18(3))**:
- **Goodwill** - Intangible value (customer base, reputation, brand) - owner can rebuild at new location
- **Ongoing business losses** - After reasonable relocation period (owner's duty to rebuild)
- **Special purchaser premium** - Unique buyer value above market

### Injurious Affection (s.18(2) OEA)

**s.18(2)(a) - Construction Impacts (Temporary)**:
- Noise, dust, vibration from construction process
- Traffic disruption, parking loss during construction
- Business losses during construction period
- **Quantification**: Lump-sum for construction duration

**s.18(2)(b) - Permanent Use Impacts (Capitalized)**:
- Ongoing noise from highway/transit operation
- Visual obstruction (elevated structure blocks view)
- Privacy loss (highway adjacent to backyard)
- Stigma (EMF perception near transmission line)
- **Quantification**: Before value - After value = Permanent capital loss
- **Antrim Four-Part Test** required:
  1. Authorized public work
  2. Exercise of statutory powers
  3. Diminished market value
  4. Special (property-specific), not general public inconvenience

## Usage

### Command Line

```bash
# Basic usage
python expropriation_calculator.py sample_commercial_expropriation.json

# Specify output file
python expropriation_calculator.py sample_commercial_expropriation.json results.json
```

### Input JSON Structure

```json
{
  "property": {
    "address": "2550 Industrial Avenue, Mississauga, ON",
    "area_acres": 50.0,
    "market_value": 1500000.00,
    "zoning": "Employment Commercial (EC)",
    "highest_and_best_use": "Commercial development",

    "valuation_date": "2024-01-15",
    "form_7_service_date": "2024-01-15",
    "plan_registration_date": "2024-02-01",

    "special_purchaser_premium": 250000.00,
    "special_purchaser_notes": "Adjacent owner assemblage premium - excluded"
  },

  "disturbance_damages": {
    "moving_costs": 25000.00,
    "packing_materials": 3000.00,
    "storage_costs": 8000.00,

    "business_losses": {
      "revenue_loss_months": 6,
      "monthly_revenue": 50000.00,
      "profit_margin_pct": 20.0,
      "fixed_costs_monthly": 15000.00,
      "signage_and_marketing": 12000.00,
      "permits_and_licenses": 5000.00,
      "equipment_reinstallation": 18000.00,
      "trade_fixtures_depreciated_value": 75000.00,
      "goodwill_claimed": 150000.00
    },

    "professional_fees": {
      "legal": 30000.00,
      "appraisal": 15000.00,
      "accounting": 5000.00
    },

    "temporary_accommodation_months": 3,
    "accommodation_cost_monthly": 3000.00,

    "construction_impacts": {
      "noise": 8000.00,
      "dust": 3000.00,
      "vibration": 5000.00,
      "traffic_disruption": 4000.00,
      "duration_months": 12
    },

    "permanent_impacts": {
      "noise_value_loss": 45000.00,
      "visual_obstruction": 25000.00,
      "privacy_loss": 15000.00,
      "stigma_value_loss": 0.00
    }
  },

  "payment_details": {
    "payment_date": "2025-01-15",
    "interest_rate_annual_pct": 3.0
  }
}
```

### Output Structure

```json
{
  "analysis_date": "2025-11-15",
  "property_details": {
    "address": "2550 Industrial Avenue, Mississauga, ON",
    "area_acres": 50.0,
    "market_value": 1500000.0,
    "valuation_date": "2024-01-15"
  },
  "compensation_breakdown": {
    "market_value": 1500000.0,
    "disturbance_damages": {
      "moving_costs": 36000.0,
      "business_losses_compensable": 260000.0,
      "business_losses_non_compensable": 150000.0,
      "professional_fees": 50000.0,
      "temporary_accommodation": 9000.0,
      "construction_impacts_temporary": 20000.0,
      "permanent_impacts_capitalized": 85000.0,
      "total": 460000.0
    },
    "subtotal_before_interest": 1960000.0,
    "interest": {
      "interest_amount": 58961.10,
      "days": 366,
      "rate_annual_pct": 3.0
    },
    "total_compensation": 2018961.10
  },
  "compliance": {
    "compensable_items": [
      "✓ Market value: $1,500,000.00 at valuation date January 15, 2024",
      "✓ Business losses: $260,000.00 (limited to 6 month reasonable relocation period)",
      "✓ Construction impacts (s.18(2)(a)): $20,000.00 (12 month temporary impact)",
      "✓ Permanent impacts (s.18(2)(b)): $85,000.00 (Antrim four-part test)"
    ],
    "non_compensable_items": [
      "✗ Special purchaser premium excluded: $250,000.00",
      "✗ Goodwill NON-compensable: $150,000.00 (s.18(3) OEA)"
    ]
  }
}
```

## Sample Scenarios

### 1. Commercial Expropriation (with Business Losses)

**File**: `sample_commercial_expropriation.json`

**Scenario**:
- 50-acre commercial property
- Market value: $1.5M (highest and best use: commercial development)
- Special purchaser premium: $250K (excluded)
- Business losses: 6-month relocation period
- Goodwill claimed: $150K (NON-compensable)
- Construction impacts: 12 months
- Permanent highway noise impacts

**Result**: $2,018,961.10 total compensation

**Key Findings**:
- Market value at highest and best use (NOT current farm value)
- Business losses limited to 6-month reasonable relocation period
- Goodwill excluded under s.18(3)
- Special purchaser premium excluded
- Interest: $58,961 (366 days @ 3%)

### 2. Residential Expropriation (No Business)

**File**: `sample_residential_expropriation.json`

**Scenario**:
- 0.25-acre residential property
- Market value: $850K
- No business losses
- Moving and temporary accommodation costs
- 18-month construction period
- Permanent noise and privacy impacts from new highway

**Result**: $1,040,080.14 total compensation

**Key Findings**:
- Residential relocation disturbance
- No business losses (pure residential)
- Substantial permanent impacts (highway proximity)
- Interest: $22,580 (270 days @ 3%)

## Implementation Details

### Python Calculator Features

1. **Data Validation**
   - Valuation date validation (earlier of Form 7 or plan registration)
   - Market value and area validation
   - Interest rate validation (0-100%)

2. **Business Loss Calculation**
   - Revenue loss formula: (Lost revenue × profit margin) + Fixed costs
   - Limited to reasonable relocation period
   - Separate tracking of compensable vs. non-compensable (goodwill)

3. **Interest Calculation**
   - Simple interest: Principal × Rate × (Days / 365)
   - From valuation date to payment date
   - Current Ontario statutory rate: 3.0%

4. **OEA Compliance Checking**
   - But-for test validation
   - Reasonableness assessment (mitigation duty)
   - Foreseeability analysis
   - Antrim four-part test for injurious affection

5. **Output Generation**
   - Detailed compensation breakdown
   - Compensable vs. non-compensable items
   - OEA compliance validation
   - JSON export for further analysis

## Common Scenarios

### Valuation Date Determination

**Scenario 1**: Form 7 served first
- Form 7 service: January 15, 2024
- Plan registration: February 1, 2024
- **Valuation date**: January 15, 2024 (earlier date)

**Scenario 2**: Plan registered first
- Plan registration: May 15, 2024
- Form 7 service: June 1, 2024
- **Valuation date**: May 15, 2024 (earlier date)

### Highest and Best Use

**Example**: Agricultural land zoned industrial
- Current use: Farm ($10,000/acre)
- Zoning: Industrial
- Services available: Yes
- Market demand: Strong
- **Highest and best use**: Industrial development
- **Entitlement**: Industrial value ($120,000/acre)
- **NOT compensated**: Farm value

### Business Losses - Compensable Period

**Example**: Restaurant relocation
- Closure period: 3 weeks
- Customer base rebuild: 4 months
- **Reasonable relocation period**: 6 months
- **Compensable**: Revenue losses for 6 months
- **NOT compensable**: Ongoing losses after 6 months (duty to rebuild)

### Goodwill - NON-Compensable

**Rule**: s.18(3) OEA excludes "loss of goodwill or any other intangible"

**Examples (NON-compensable)**:
- Lost customer base
- Brand recognition in neighborhood
- Business reputation
- Referral relationships

**Rationale**: Intangible, owner can rebuild at new location

## Legal References

- **Ontario Expropriations Act, R.S.O. 1990, c. E.26**
- **s.13**: Market value determination
- **s.13(2)**: Valuation date (earlier of notice or plan registration)
- **s.18**: Disturbance damages entitlement
- **s.18(2)(a)**: Construction impacts (temporary)
- **s.18(2)(b)**: Permanent use impacts
- **s.18(3)**: Goodwill and intangibles NON-compensable

- **Antrim Truck Centre Ltd. v. Ontario (Transportation), 2005 SCC 31**
  - Four-part test for injurious affection
  - Special vs. general damage distinction

## Integration with Skill

This calculator integrates with the `expropriation-compensation-entitlement-analysis` skill to provide:

1. **Legal Framework**: SKILL.md provides detailed legal analysis
2. **Quantification**: Calculator quantifies compensation amounts
3. **Compliance**: Validates OEA compliance and identifies non-compensable items
4. **Documentation**: Generates comprehensive analysis reports

**Workflow**:
1. User provides expropriation scenario (JSON)
2. Calculator quantifies market value, disturbance, interest
3. Skill validates legal entitlement and compliance
4. Output: Complete compensation analysis with OEA compliance validation

## Author

**Claude Code**
Version: 1.0.0
Date: 2025-11-15

Built for the expropriation-compensation-entitlement-analysis skill following Ontario Expropriations Act legal framework.
