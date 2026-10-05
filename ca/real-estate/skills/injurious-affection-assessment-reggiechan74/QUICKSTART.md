# Injurious Affection Calculator - Quick Start Guide

## What Does This Calculator Do?

Quantifies construction and proximity damages for expropriation claims:
- **Noise impacts** (dBA modeling with distance attenuation)
- **Dust/air quality** (cleaning costs, health impacts)
- **Vibration damage** (PPV thresholds, repair costs)
- **Traffic disruption** (lost sales, access costs)
- **Business losses** (revenue reduction)
- **Visual impairment** (permanent value loss)

## 5-Minute Quick Start

### 1. Run a Sample Calculation

```bash
cd ${CLAUDE_PLUGIN_ROOT}/skills/injurious-affection-assessment

# Test residential property with construction impacts
python3 injurious_affection_calculator.py sample_residential_construction_impact.json --verbose
```

**Result:** $28,260 total damages from 6-month construction (noise + dust + vibration)

### 2. Run Commercial Example

```bash
# Test restaurant with traffic disruption
python3 injurious_affection_calculator.py sample_commercial_traffic_impact.json --verbose
```

**Result:** $220,759 total damages (temporary construction + permanent visual impact)

### 3. Run Industrial Example

```bash
# Test industrial facility with minimal impact
python3 injurious_affection_calculator.py sample_industrial_minimal_impact.json --verbose
```

**Result:** $9,600 total damages (dust cleaning only)

## Three Sample Scenarios

### Scenario 1: Residential Duplex - Pile Driving
- **Property:** 2-unit residential, $850K value
- **Impact:** Severe noise (86.5 dBA), high dust, cosmetic vibration
- **Duration:** 6 months
- **Damages:** $28,260 (noise 20% | dust 71% | vibration 9%)

### Scenario 2: Commercial Restaurant - Traffic Loss
- **Property:** Restaurant, $1.2M value, $800K annual revenue
- **Impact:** Severe noise, 35% traffic reduction, permanent visual obstruction
- **Duration:** 9 months + permanent
- **Damages:** $220,759 (traffic 38% | visual 43% | noise 3% | dust 9%)

### Scenario 3: Industrial Manufacturing - Minimal Impact
- **Property:** Industrial facility, $3.5M value
- **Impact:** Below threshold noise, low dust
- **Duration:** 12 months
- **Damages:** $9,600 (dust cleaning only)

## Key Calculation Rules

### Noise (6 dBA per doubling rule)
```
Noise at distance D = Noise at 15m - (6 × log₂(D/15))

Example: Pile driver 95 dBA at 15m → 86.5 dBA at 40m
```

**Thresholds:**
- Residential: Severe >75 dBA (20% rent reduction), Moderate 65-75 dBA (7.5%)
- Commercial: Severe >80 dBA (12.5% rent reduction), Moderate 70-80 dBA (5.5%)
- Industrial: Impact only if >85 dBA (3% rent reduction)

### Dust Zones
- **High** (0-50m): Weekly cleaning
- **Moderate** (50-150m): Bi-weekly cleaning
- **Low** (150-300m): Monthly cleaning

### Vibration (PPV thresholds)
- **Cosmetic:** 5-12 mm/s → $2,500 repair
- **Structural:** >12 mm/s → $25,000 repair

### Traffic (Commercial only)
```
Lost profit = Baseline traffic × Traffic reduction % × Conversion × Avg sale × Margin
Default: 2% conversion, $45 avg sale, 40% margin
```

## Customizing Your Calculation

### Create Your Input JSON

```json
{
  "property_address": "Your Property Address",
  "property": {
    "property_type": "residential",  // or "commercial", "industrial"
    "property_value": 850000,
    "rental_income_monthly": 2400,
    "distance_to_construction_m": 40,
    "number_of_units": 2
  },
  "construction": {
    "duration_months": 6,
    "equipment": [
      {
        "equipment_type": "pile_driver",
        "dba_at_15m": 95,
        "hours_per_day": 4,
        "days_per_week": 5
      }
    ],
    "dust_impact_zone": "high",  // or "moderate", "low"
    "vibration_ppv_mms": 8.5,
    "traffic_reduction_pct": 0.0
  }
}
```

### Run Your Calculation

```bash
python3 injurious_affection_calculator.py your_input.json --verbose --output your_results.json
```

## Common Equipment Noise Levels (at 15m)

| Equipment | dBA |
|-----------|-----|
| Impact pile driver | 95-105 |
| Jackhammer | 85-95 |
| Heavy trucks | 80-90 |
| Excavator | 75-85 |
| Concrete mixer | 75-85 |
| Generator | 70-80 |

## Understanding Results

### Console Output
- Summary of all impact categories
- Total temporary vs. permanent damages
- Breakdown by category (% of total)
- Equipment-specific noise calculations

### JSON Output File
```json
{
  "total_injurious_affection": 28260.0,
  "total_temporary_damages": 28260.0,
  "total_permanent_damages": 0.0,
  "damages_by_category": {
    "noise": 5760.0,
    "dust": 20000.0,
    "vibration": 2500,
    "traffic": 0.0,
    "business_loss": 0.0,
    "visual_permanent": 0.0
  }
}
```

## When to Use Each Property Type

### Residential
- Single-family homes, apartments, condos
- Sensitive to noise (especially night work)
- Health impacts considered for prolonged exposure
- **Key metric:** Rent reduction during construction

### Commercial
- Retail, restaurants, offices
- Traffic disruption is critical for customer-facing businesses
- Moderate noise tolerance
- **Key metrics:** Lost sales + rent reduction

### Industrial
- Warehouses, manufacturing, distribution
- High noise tolerance (85+ dBA threshold)
- Minimal impact unless very severe
- **Key metric:** Operational disruption (rarely significant)

## Adding Permanent Visual Impact

For structures that remain after construction (elevated guideways, towers):

```json
{
  "visual_impact": {
    "description": "Permanent view obstruction from elevated guideway",
    "value_reduction_pct": 0.08  // 8% property value reduction
  }
}
```

**Capitalization:** Direct property value loss = $1,200,000 × 8% = $96,000

## Tips for Accurate Assessment

1. **Measure distance accurately** - Noise attenuation is distance-sensitive
2. **Use worst-case equipment** - Pile drivers create highest impacts
3. **Consider construction timing** - Night work = 1.5× residential impact
4. **Document traffic baselines** - For commercial, estimate daily foot traffic
5. **Get expert appraisals** - For visual impact percentage

## Integration with Expropriation Claims

This calculator provides **Item 2: Injurious Affection** component of total compensation:

1. Market value of land taken
2. **Injurious affection** (this calculator)
3. Disturbance damages
4. Special damages

**Total Compensation = Sum of all components**

## Command-Line Options

```bash
# Basic usage
python3 injurious_affection_calculator.py input.json

# Verbose output (detailed breakdown)
python3 injurious_affection_calculator.py input.json --verbose

# Custom output file
python3 injurious_affection_calculator.py input.json --output my_results.json

# All options together
python3 injurious_affection_calculator.py input.json --verbose --output results.json
```

## Next Steps

1. **Review samples:** Examine the 3 sample input files
2. **Modify a sample:** Change values to match your scenario
3. **Run calculation:** Test with your modified input
4. **Review README.md:** For detailed methodology
5. **Check SKILL.md:** For technical depth and case law

## Files in This Directory

- `injurious_affection_calculator.py` - Main calculator (standalone, no dependencies)
- `sample_residential_construction_impact.json` - Residential example
- `sample_commercial_traffic_impact.json` - Commercial example
- `sample_industrial_minimal_impact.json` - Industrial example
- `README.md` - Complete documentation
- `SKILL.md` - Technical methodology and case law
- `QUICKSTART.md` - This file

## Support

Questions? Review the sample files and README.md. All calculation methodologies are documented with formulas and examples.
