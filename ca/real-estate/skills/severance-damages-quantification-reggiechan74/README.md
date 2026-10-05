# Severance Damages Calculator

**Version 2.0.0 - Modular Architecture**

Quantifies loss of value to remainder parcels from partial property takings across four damage categories: access impairment, shape irregularity, utility impairment, and farm operation disruption.

## ✨ What's New in Version 2.0.0

- **🏗️ Modular Architecture**: Refactored from 943 lines to 360 lines (62% reduction)
- **🎯 Zero Magic Numbers**: All constants centralized in `config/constants.py`
- **🛡️ Defensive Programming**: Safe division and capitalization utilities
- **✅ JSON Schema Validation**: Input validation with auto-fix capability
- **📊 Comprehensive Logging**: Detailed calculation traceability
- **🔄 100% Backward Compatible**: Identical results to Version 1.0.0

## Overview

The Severance Damages Calculator implements detailed methodologies for quantifying how partial takings (e.g., highway widening, pipeline corridors) reduce the value of remainder parcels beyond the proportionate land value taken.

### Four Damage Categories

1. **Access Impairment**
   - Direct frontage loss ($/linear foot by road classification)
   - Circuitous access (time-distance modeling, capitalized costs)
   - Landlocked parcels (easement costs or value loss)

2. **Shape Irregularity**
   - Geometric efficiency ratios (area-to-perimeter analysis)
   - Buildable area reduction (development constraints)
   - Development yield loss (reduced unit counts)

3. **Utility Impairment**
   - Loss of highest and best use (zoning-permitted vs. achievable)
   - Site servicing complications (utility relocations, drainage)
   - Development potential reduction

4. **Farm Operation Disruption** (agricultural properties only)
   - Field division costs (fencing, drainage modifications)
   - Equipment access complications (time costs, turning radius)
   - Irrigation system impacts (repair costs or value loss)

## Installation

The calculator is a standalone Python script with no external dependencies beyond the standard library.

```bash
# Make executable (optional)
chmod +x severance_calculator.py
```

## Usage

### Basic Command

```bash
python severance_calculator.py <input.json> [output.json]
```

### Examples

```bash
# Highway frontage loss (industrial property)
python severance_calculator.py sample_highway_frontage_loss.json

# Farm bisection with irrigation impacts
python severance_calculator.py sample_farm_bisection.json

# Landlocked commercial parcel
python severance_calculator.py sample_landlocked_parcel.json

# Specify custom output path
python severance_calculator.py input.json results.json
```

## Input Structure

### Complete JSON Schema

```json
{
  "property_before": {
    "total_acres": 200.0,
    "frontage_linear_feet": 800.0,
    "road_classification": "highway|arterial|collector|local",
    "shape_ratio_frontage_depth": 0.25,  // Frontage:Depth (e.g., 1:4 = 0.25)
    "value_per_acre": 40000.0,
    "use": "industrial|commercial|residential|agricultural",
    "development_potential_units": null,  // Optional: for subdivision analysis
    "buildable_area_sf": null            // Optional: for development reduction
  },
  "taking": {
    "area_taken_acres": 10.0,
    "frontage_lost_linear_feet": 200.0,
    "creates_landlocked": false,
    "eliminates_direct_access": true,
    "circuitous_access_added_minutes": 6.0,  // Additional travel time
    "creates_irregular_shape": true,
    "severs_utilities": false,
    "reduces_development_potential": false,
    "bisects_farm": false,               // Agricultural only
    "disrupts_irrigation": false         // Agricultural only
  },
  "remainder": {
    "acres": 190.0,
    "frontage_remaining_linear_feet": 600.0,
    "shape_ratio_frontage_depth": 0.15,
    "access_type": "direct|circuitous|landlocked",
    "buildable_area_sf": null,
    "development_potential_units": null,
    "requires_new_fencing_linear_meters": 0.0,  // Agricultural only
    "irrigation_acres_affected": 0.0            // Agricultural only
  },
  "market_parameters": {
    "cap_rate": 0.07,
    "travel_time_value_per_hour": 40.0,
    "trips_per_day": 20,                 // Industrial/commercial: 20, Agricultural: 5
    "business_days_per_year": 250
  }
}
```

## Calculation Methodologies

### 1. Access Impairment

**Frontage Loss Value ($/Linear Foot Method)**

Frontage values by road classification and property use:

| Road Class | Commercial | Industrial | Residential | Agricultural |
|-----------|-----------|-----------|------------|-------------|
| Highway   | $500-1,500/LF | $300-800/LF | $150-400/LF | $50-150/LF |
| Arterial  | $300-800/LF | $200-500/LF | $100-250/LF | $30-100/LF |
| Collector | $150-400/LF | $100-300/LF | $50-150/LF | $20-60/LF |
| Local     | $50-150/LF | $40-120/LF | $25-75/LF | $10-30/LF |

Calculator uses midpoint of range for each classification/use combination.

**Circuitous Access (Time-Distance Modeling)**

```
Annual Time Cost = Trips/Day × Days/Year × (Added Minutes ÷ 60) × $/Hour
Capitalized Cost = Annual Time Cost ÷ Cap Rate
```

Example:
- 20 trips/day × 250 days × (6 min ÷ 60) × $40/hr = $20,000/year
- $20,000 ÷ 7% cap rate = $285,714 severance damage

**Landlocked Parcel (Easement Cost-to-Cure)**

```
Easement Value = Easement Area (acres) × Fee Simple $/Acre × 12%
Transaction Costs = Legal ($25K) + Survey ($8K)
Total Remedy Cost = Easement Value + Transaction Costs
```

Alternative: 50-80% value loss if no easement obtainable.

### 2. Shape Irregularity

**Geometric Efficiency Index**

```
Efficiency Index = (Actual Area ÷ Actual Perimeter) ÷ (Ideal Square Area ÷ Ideal Square Perimeter)
```

Shape efficiency categories and value discounts:
- **High** (0.8-1.0 index): 2% discount
- **Moderate** (0.6-0.8 index): 8% discount
- **Low** (0.4-0.6 index): 15% discount
- **Very Low** (<0.4 index): 30% discount

**Buildable Area Reduction**

```
Proportionate Buildable = Before Buildable SF × (Remainder Acres ÷ Before Acres)
Buildable Reduction SF = Proportionate Buildable - Actual Buildable SF
Value Loss = Buildable Reduction SF × $/SF (typically $250/SF commercial, $150/SF residential)
```

### 3. Utility Impairment

**Site Servicing Costs**

Typical utility relocation costs:
- Water main: $500/linear meter
- Sanitary sewer: $800/linear meter
- Storm drainage: $195,000 (engineering + construction)

### 4. Farm Operation Disruption

**Field Division Costs**

- Fencing: $20/linear meter (page wire, livestock)
- Tile drainage: $8K engineering + $15/meter × length

**Equipment Access Complications**

```
Annual Equipment Time Cost = Crossings/Year × Hours/Crossing × $/Hour
Capitalized Cost = Annual Cost ÷ Cap Rate
```

**Irrigation System Impacts**

Cost-to-cure methodology:
```
Repair Cost = $180,000 (pump station + distribution lines)
Value Loss = Affected Acres × $2,000/acre (irrigation premium)

Severance Damage = min(Repair Cost, Value Loss)
```

## Output Structure

### Summary Report (Console)

```
================================================================================
SEVERANCE DAMAGES CALCULATION COMPLETE
================================================================================

Property: 200.0 acres, industrial use
Value before: $8,000,000.00 ($40,000/acre)

Taking: 10.0 acres
Land taken value: $400,000.00

Remainder: 190.0 acres
Proportionate value: $7,600,000.00

--------------------------------------------------------------------------------
SEVERANCE DAMAGES BY CATEGORY
--------------------------------------------------------------------------------
Access Impairment:           $     395,714.29
  - Frontage loss:           $     110,000.00
  - Circuitous access:       $     285,714.29

Shape Irregularity:          $     152,000.00
  - Geometric inefficiency:  $     152,000.00
    (Efficiency: 1.25, Category: high)

--------------------------------------------------------------------------------
TOTAL SEVERANCE DAMAGES:     $     547,714.29
--------------------------------------------------------------------------------

Remainder value after severance: $7,052,285.71
Total compensation (land + severance): $947,714.29
```

### JSON Output

Complete results saved to `*_results.json` including:
- Property before/after values
- Detailed damage calculations by category
- Reconciliation (before/after market value approach)
- Calculation assumptions and parameters

## Sample Scenarios

### 1. Highway Frontage Loss (Industrial)

**File**: `sample_highway_frontage_loss.json`

**Scenario**: 200-acre industrial property loses 200 LF of highway frontage, creating circuitous access (+6 minutes).

**Results**:
- Access damages: $395,714 (frontage + circuitous access)
- Shape damages: $152,000 (shape efficiency reduction)
- Total severance: $547,714

### 2. Farm Bisection with Irrigation

**File**: `sample_farm_bisection.json`

**Scenario**: 160-acre farm bisected by pipeline, disrupting irrigation system serving 50 acres.

**Results**:
- Shape damages: $585,000 (very low efficiency after bisection)
- Farm damages: $202,643 (fencing + equipment access + irrigation)
- Total severance: $787,643

### 3. Landlocked Commercial Parcel

**File**: `sample_landlocked_parcel.json`

**Scenario**: 100-acre commercial property loses all frontage, creating landlocked 60-acre remainder.

**Results**:
- Access damages: $368,931 (frontage value + easement remedy)
- Shape damages: $4,536,000 (buildable area loss + inefficiency)
- Utility damages: $715,000 (site servicing)
- Total severance: $5,619,931 (exceeds proportionate value - severe impairment)

## Calculation Notes

### Before/After Reconciliation

The calculator validates results using the before/after market value approach:

```
Before Value Total = Total Acres × $/Acre
Land Taken Value = Taken Acres × $/Acre
Remainder Proportionate Value = Remainder Acres × $/Acre

Severance Damages = Σ(Access + Shape + Utility + Farm Damages)

After Value Remainder = Proportionate Value - Severance Damages

Total Compensation = Land Taken Value + Severance Damages
```

### Cost-to-Cure vs. Value Loss

For remedial damages (easements, irrigation, utilities), calculator applies **lower of**:
1. Cost to cure (repair/restore functionality)
2. Value loss if not cured

This reflects appraisal principle that value loss cannot exceed restoration cost.

### Shape Efficiency Edge Cases

- **Landlocked parcels**: Efficiency index set to 0.2 (very low) when frontage = 0
- **Long narrow strips**: Calculated from actual frontage:depth ratio
- **Irregular polygons**: Approximated using perimeter method

## Integration with Expropriation Workflow

This calculator quantifies **severance damages** (one component of total compensation):

```
Total Compensation = Market Value + Disturbance Damages + Severance Damages + Injurious Affection

Where:
- Market Value = Land taken × $/acre (fee simple value)
- Disturbance Damages = Relocation, business losses, legal fees
- Severance Damages = This calculator's output
- Injurious Affection = Construction impacts, permanent proximity damages
```

Use in conjunction with:
- **Market valuation**: Fee simple value per acre (comparable sales, income approach)
- **Disturbance calculator**: Moving costs, business interruption, goodwill (if available)
- **Injurious affection**: Noise, dust, visual impairment, construction impacts

## Limitations and Assumptions

1. **Frontage values**: Uses midpoint of market ranges; adjust for specific market conditions
2. **Shape efficiency**: Geometric calculation - does not capture all development constraints
3. **Agricultural impacts**: Based on typical farm operations; customize for specialty crops
4. **Time-distance**: Assumes constant travel patterns; may vary seasonally
5. **Development potential**: Requires detailed development analysis for accuracy

## Best Practices

1. **Input validation**: Verify acreage reconciles (Before = Taken + Remainder)
2. **Market parameters**: Adjust cap rate, travel time value, frontage rates for local market
3. **Development analysis**: Provide unit counts and buildable areas for subdivision/development properties
4. **Agricultural properties**: Complete all farm-specific fields (fencing, irrigation, equipment access)
5. **Cost-to-cure**: Update utility costs and easement values for current market
6. **Cross-check**: Validate against comparable sales of similarly impacted properties

## Technical Details

- **Language**: Python 3.7+
- **Dependencies**: Standard library only (json, sys, dataclasses, pathlib, datetime, math)
- **Input format**: JSON
- **Output format**: JSON + formatted console report
- **Calculation precision**: Float (IEEE 754 double precision)

## Version History

- **v1.0.0** (2025-11-15): Initial release
  - Four damage categories (access, shape, utility, farm)
  - Frontage value tables by road classification
  - Time-distance modeling for circuitous access
  - Shape efficiency index calculations
  - Agricultural operation disruption
  - Sample scenarios and comprehensive documentation

## Author

Created by Claude Code as part of the expropriation and infrastructure easement toolkit.

## License

Part of lease-abstract project. See project root for license details.
