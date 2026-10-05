# Severance Damages Calculator - Refactoring & Enhancement Plan

## Executive Summary

Transform the severance damages calculator from a functional but fragile single-file script into a production-grade, modular, fully-tested calculation engine suitable for professional appraisal work.

**Duration**: 3-5 days (phased implementation)
**Effort**: ~20-30 hours
**Risk**: Low (maintain backward compatibility)
**Priority**: High (critical calculation accuracy for expropriation work)

---

## Table of Contents

1. [Current State Analysis](#current-state-analysis)
2. [Goals & Success Criteria](#goals--success-criteria)
3. [Proposed Architecture](#proposed-architecture)
4. [Implementation Phases](#implementation-phases)
5. [File Structure](#file-structure)
6. [Testing Strategy](#testing-strategy)
7. [Validation & Schema](#validation--schema)
8. [Documentation Updates](#documentation-updates)
9. [Risk Mitigation](#risk-mitigation)
10. [Timeline & Milestones](#timeline--milestones)

---

## Current State Analysis

### File Metrics
- **Size**: 943 lines (manageable, but can be improved)
- **Functions/Classes**: 22 (good modularity)
- **Type Coverage**: ~95% (excellent)
- **Test Coverage**: 0% ❌ (critical gap)
- **Input Validation**: 0% ❌ (critical gap)

### Strengths to Preserve
✅ Clean dataclass architecture
✅ Strong type hinting
✅ Modular calculation functions
✅ Good domain expertise (4 damage categories)
✅ JSON I/O infrastructure
✅ CLI interface

### Critical Issues to Fix
❌ No unit tests (high risk for financial calculations)
❌ No input validation (crashes on malformed input)
❌ 15+ magic numbers scattered in code
❌ Division by zero risks (6+ locations)
❌ No JSON schema
❌ Minimal error handling
❌ No logging/audit trail

### Code Quality Issues
⚠️ Magic numbers in calculation functions
⚠️ Hardcoded constants (should be configurable)
⚠️ Inconsistent default handling
⚠️ Limited calculation methodology documentation
⚠️ No sensitivity analysis capability

---

## Goals & Success Criteria

### Primary Goals

**1. Production Hardening**
- ✅ 90%+ unit test coverage
- ✅ 100% input validation with JSON schema
- ✅ Zero unhandled exceptions
- ✅ Comprehensive error messages

**2. Code Quality**
- ✅ All magic numbers centralized in configuration
- ✅ All division operations protected
- ✅ Consistent error handling patterns
- ✅ Logging throughout calculation pipeline

**3. Maintainability**
- ✅ Modular architecture (separate files for each category)
- ✅ Clear separation of concerns
- ✅ Comprehensive documentation
- ✅ Easy to extend (new damage categories, property types)

**4. Professional Features**
- ✅ Automated validation script with auto-fix
- ✅ Sensitivity analysis capability
- ✅ Detailed calculation explanations
- ✅ Audit trail generation

### Success Criteria

| Metric | Current | Target | Verification |
|--------|---------|--------|--------------|
| **Test Coverage** | 0% | 90%+ | `pytest --cov` |
| **Input Validation** | None | 100% | JSON schema + tests |
| **Error Handling** | 10% | 95%+ | Code review + tests |
| **Magic Numbers** | 15+ | 0 | Grep for hardcoded floats |
| **Documentation** | Partial | Complete | README + docstrings |
| **SKILL.md Integration** | None | Full | Skill activation works |

---

## Proposed Architecture

### Modular Structure

```
severance-damages-quantification/
├── severance_calculator.py          # Main orchestrator (300 lines)
├── config/
│   ├── __init__.py
│   ├── constants.py                 # All magic numbers centralized
│   └── market_parameters.py         # Market assumption structures
├── damages/
│   ├── __init__.py
│   ├── access.py                    # Access impairment calculations (200 lines)
│   ├── shape.py                     # Shape irregularity calculations (200 lines)
│   ├── utility.py                   # Utility impairment calculations (150 lines)
│   └── farm.py                      # Farm operation disruption (150 lines)
├── models/
│   ├── __init__.py
│   ├── property_data.py             # PropertyBefore, Taking, Remainder dataclasses
│   └── damage_results.py            # Damage result dataclasses
├── utils/
│   ├── __init__.py
│   ├── validation.py                # Input validation utilities
│   └── calculations.py              # Shared calculation utilities
├── tests/
│   ├── __init__.py
│   ├── test_access_damages.py       # 6 tests
│   ├── test_shape_damages.py        # 6 tests
│   ├── test_utility_damages.py      # 4 tests
│   ├── test_farm_damages.py         # 4 tests
│   ├── test_integration.py          # 5 tests (end-to-end)
│   └── fixtures/                    # Test data JSON files
│       ├── highway_frontage_loss.json
│       ├── landlocked_parcel.json
│       ├── irregular_shape.json
│       ├── farm_bisection.json
│       └── combined_damages.json
├── severance_input_schema.json      # JSON Schema for validation
├── validate_severance.py            # Validation script with auto-fix
├── SCHEMA_DOCUMENTATION.md          # Schema reference
├── VALIDATOR_README.md              # Validation guide
└── SKILL.md                         # Updated with calculator integration
```

### Data Flow

```
Input JSON
    ↓
Validation (schema + auto-fix)
    ↓
Parsing (models/property_data.py)
    ↓
Main Calculator (severance_calculator.py)
    ↓
Damage Modules (damages/*)
    ├── access.py
    ├── shape.py
    ├── utility.py
    └── farm.py
    ↓
Results Assembly (models/damage_results.py)
    ↓
Output (JSON + CLI report)
```

---

## Implementation Phases

### Phase 1: Foundation (Day 1 - 6 hours)

**Goal**: Set up modular structure and centralize configuration

**Tasks**:

1.1. **Create Directory Structure**
```bash
mkdir -p config damages models utils tests tests/fixtures
touch config/__init__.py damages/__init__.py models/__init__.py utils/__init__.py tests/__init__.py
```

1.2. **Extract Configuration** (config/constants.py)
```python
"""Centralized calculation constants for severance damages"""

from dataclasses import dataclass

@dataclass
class CalculationConstants:
    """All hardcoded values centralized here"""

    # Easement valuation
    EASEMENT_PERCENTAGE_OF_FEE: float = 0.12
    EASEMENT_LEGAL_COSTS: float = 25000.0
    EASEMENT_SURVEY_COSTS: float = 8000.0
    DEFAULT_EASEMENT_WIDTH_M: float = 20.0
    DEFAULT_EASEMENT_LENGTH_M: float = 200.0

    # Development values
    BUILDABLE_VALUE_COMMERCIAL_PER_SF: float = 250.0
    BUILDABLE_VALUE_RESIDENTIAL_PER_SF: float = 150.0
    INDUSTRIAL_LOT_VALUE_PER_UNIT: float = 500000.0
    RESIDENTIAL_UNIT_VALUE: float = 150000.0

    # Utility relocation
    WATER_COST_PER_METER: float = 500.0
    SEWER_COST_PER_METER: float = 800.0
    DRAINAGE_ENGINEERING_COST: float = 195000.0
    DEFAULT_UTILITY_RELOCATION_LENGTH_M: float = 400.0

    # Agricultural
    FENCING_COST_PER_METER: float = 20.0
    TILE_DRAINAGE_PER_METER: float = 15.0
    DRAINAGE_ENGINEERING_FARM: float = 8000.0
    TILE_INSTALLATION_LENGTH_M: float = 1500.0
    EQUIPMENT_OPERATOR_COST_PER_HOUR: float = 150.0
    EQUIPMENT_CROSSINGS_PER_YEAR: int = 30
    IRRIGATION_REPAIR_COST: float = 180000.0
    IRRIGATION_PREMIUM_PER_ACRE: float = 2000.0

    # Defaults for missing market parameters
    DEFAULT_CAP_RATE: float = 0.07
    DEFAULT_CAPITALIZATION_MULTIPLE: float = 10.0  # Used when cap_rate = 0
    DEFAULT_TRAVEL_TIME_VALUE: float = 40.0
    DEFAULT_TRIPS_PER_DAY: int = 20
    DEFAULT_BUSINESS_DAYS_PER_YEAR: int = 250

    # Shape efficiency thresholds
    SHAPE_EFFICIENCY_HIGH: float = 0.8
    SHAPE_EFFICIENCY_MODERATE: float = 0.6
    SHAPE_EFFICIENCY_LOW: float = 0.4
    LANDLOCKED_EFFICIENCY_INDEX: float = 0.2
```

1.3. **Extract Data Models** (models/property_data.py, models/damage_results.py)
- Move all dataclasses to dedicated model files
- Keep backward compatibility

1.4. **Create Shared Utilities** (utils/calculations.py)
```python
"""Shared calculation utilities with defensive programming"""

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divide two numbers, returning default if denominator is zero"""
    if denominator == 0:
        return default
    return numerator / denominator

def capitalize_annual_cost(
    annual_cost: float,
    cap_rate: float,
    fallback_multiple: float = 10.0
) -> float:
    """Capitalize an annual cost to present value"""
    if cap_rate <= 0:
        return annual_cost * fallback_multiple
    return annual_cost / cap_rate
```

**Deliverables**:
- ✅ Directory structure created
- ✅ config/constants.py with all magic numbers
- ✅ models/ with dataclasses
- ✅ utils/ with safe calculation utilities
- ✅ All files have proper imports and `__init__.py`

**Validation**: Run existing code with `from config.constants import CalculationConstants`

---

### Phase 2: Modularize Calculations (Day 1-2 - 8 hours)

**Goal**: Extract calculation functions into separate modules

**Tasks**:

2.1. **Create damages/access.py** (~200 lines)
```python
"""Access impairment damage calculations

Calculates three types of access damages:
1. Frontage loss value ($/linear foot method)
2. Circuitous access cost (time-distance modeling, capitalized)
3. Landlocked remedy cost (easement acquisition + legal)

USPAP 2024 Compliant
"""

from typing import Tuple
from ..models.property_data import PropertyBefore, Taking, Remainder
from ..models.damage_results import AccessDamages
from ..config.constants import CalculationConstants
from ..config.market_parameters import MarketParameters
from ..utils.calculations import safe_divide, capitalize_annual_cost
import logging

logger = logging.getLogger(__name__)

def calculate_frontage_loss_value(...) -> Tuple[float, float]:
    """Calculate value loss from frontage reduction"""
    # Implementation with logging
    logger.debug(f"Calculating frontage loss: {frontage_lost_lf:.1f} LF on {road_classification} for {property_use}")
    # ... calculation ...
    logger.info(f"Frontage loss value: ${frontage_value:,.2f} at ${rate_per_lf:.0f}/LF")
    return frontage_value, rate_per_lf

def calculate_circuitous_access_cost(...) -> Tuple[float, float]:
    """Calculate capitalized cost of circuitous access"""
    # Implementation with safe_divide and capitalize_annual_cost
    # ...

def calculate_landlocked_remedy_cost(...) -> float:
    """Calculate cost to cure landlocked parcel"""
    # Implementation using CalculationConstants
    # ...

def calculate_access_damages(...) -> AccessDamages:
    """Main orchestrator for access damage calculations"""
    logger.info("Calculating access damages...")
    damages = AccessDamages()

    # Call sub-functions with error handling
    try:
        if taking.frontage_lost_linear_feet > 0:
            damages.frontage_loss_value, damages.frontage_rate_used = (
                calculate_frontage_loss_value(...)
            )
    except Exception as e:
        logger.error(f"Error calculating frontage loss: {e}")
        raise

    # ... rest of calculations ...

    damages.calculate_total()
    logger.info(f"Total access damages: ${damages.total_access_damages:,.2f}")
    return damages
```

2.2. **Create damages/shape.py** (~200 lines)
- Extract shape efficiency calculations
- Add defensive checks for division by zero
- Use constants from config

2.3. **Create damages/utility.py** (~150 lines)
- Extract utility impairment calculations
- Use constants for utility costs

2.4. **Create damages/farm.py** (~150 lines)
- Extract farm operation disruption calculations
- Use constants for agricultural costs

2.5. **Update Main Calculator** (severance_calculator.py)
```python
"""Severance Damages Calculator - Main Orchestrator (REFACTORED)"""

from damages import access, shape, utility, farm
from models.property_data import PropertyBefore, Taking, Remainder
from models.damage_results import SeveranceDamagesSummary
from config.market_parameters import MarketParameters
import logging

logger = logging.getLogger(__name__)

def calculate_severance_damages(...) -> SeveranceDamagesSummary:
    """Calculate complete severance damages (MODULAR VERSION)"""
    logger.info(f"Starting severance calculation for {property_before.total_acres:.1f} acre property")

    # Calculate each category using modules
    access_damages = access.calculate_access_damages(
        property_before, taking, remainder, market_params
    )

    shape_damages = shape.calculate_shape_damages(
        property_before, taking, remainder, market_params
    )

    utility_damages = utility.calculate_utility_damages(
        property_before, taking, remainder, market_params
    )

    farm_damages = farm.calculate_farm_damages(
        property_before, taking, remainder, market_params
    )

    # Assemble summary
    summary = SeveranceDamagesSummary(...)
    summary.calculate_totals()

    logger.info(f"Total severance damages: ${summary.total_severance_damages:,.2f}")
    return summary
```

**Deliverables**:
- ✅ damages/access.py (200 lines)
- ✅ damages/shape.py (200 lines)
- ✅ damages/utility.py (150 lines)
- ✅ damages/farm.py (150 lines)
- ✅ Main calculator reduced to ~300 lines (orchestration only)
- ✅ All modules use centralized constants
- ✅ All division operations protected
- ✅ Logging added throughout

**Validation**: Run existing sample JSON files, verify same output

---

### Phase 3: Testing Infrastructure (Day 2-3 - 10 hours)

**Goal**: Achieve 90%+ test coverage

**Tasks**:

3.1. **Create Test Fixtures** (tests/fixtures/)

**highway_frontage_loss.json**:
```json
{
  "property_before": {
    "total_acres": 5.0,
    "frontage_linear_feet": 400.0,
    "road_classification": "highway",
    "shape_ratio_frontage_depth": 0.25,
    "value_per_acre": 150000.0,
    "use": "commercial"
  },
  "taking": {
    "area_taken_acres": 0.8,
    "frontage_lost_linear_feet": 100.0,
    "creates_landlocked": false,
    "eliminates_direct_access": false,
    "creates_irregular_shape": false
  },
  "remainder": {
    "acres": 4.2,
    "frontage_remaining_linear_feet": 300.0,
    "shape_ratio_frontage_depth": 0.25,
    "access_type": "direct"
  },
  "market_parameters": {
    "cap_rate": 0.07
  }
}
```

**landlocked_parcel.json**: Parcel with no frontage after taking
**irregular_shape.json**: Taking creates severe shape inefficiency
**farm_bisection.json**: Agricultural property bisected by corridor
**combined_damages.json**: Multiple damage categories

3.2. **Create Unit Tests** (tests/test_access_damages.py)
```python
"""Unit tests for access damage calculations"""

import pytest
from damages import access
from models.property_data import PropertyBefore, Taking, Remainder
from config.market_parameters import MarketParameters
from config.constants import CalculationConstants

class TestFrontageLossCalculation:
    """Test frontage loss value calculations"""

    def test_highway_commercial_frontage_loss(self):
        """Test frontage loss on highway for commercial property"""
        frontage_value, rate = access.calculate_frontage_loss_value(
            frontage_lost_lf=100.0,
            road_classification="highway",
            property_use="commercial",
            market_params=MarketParameters(cap_rate=0.07)
        )

        # Highway commercial range: $500-1500/lf, should use midpoint $1000/lf
        assert rate == 1000.0
        assert frontage_value == 100000.0

    def test_local_residential_frontage_loss(self):
        """Test frontage loss on local road for residential property"""
        frontage_value, rate = access.calculate_frontage_loss_value(
            frontage_lost_lf=50.0,
            road_classification="local",
            property_use="residential",
            market_params=MarketParameters(cap_rate=0.07)
        )

        # Local residential range: $25-75/lf, should use midpoint $50/lf
        assert rate == 50.0
        assert frontage_value == 2500.0

    def test_zero_frontage_loss(self):
        """Test that zero frontage returns zero value"""
        frontage_value, rate = access.calculate_frontage_loss_value(
            frontage_lost_lf=0.0,
            road_classification="highway",
            property_use="commercial",
            market_params=MarketParameters(cap_rate=0.07)
        )

        assert frontage_value == 0.0
        assert rate == 0.0

class TestCircuitousAccessCost:
    """Test circuitous access cost calculations"""

    def test_time_distance_capitalization(self):
        """Test capitalization of annual time cost"""
        cap_cost, annual_cost = access.calculate_circuitous_access_cost(
            added_travel_minutes=5.0,
            trips_per_day=20,
            business_days_per_year=250,
            travel_time_value_per_hour=40.0,
            cap_rate=0.07
        )

        # 5 minutes = 1/12 hour per trip
        # 20 trips/day * 250 days = 5,000 trips/year
        # Annual: 5,000 * (1/12) * $40 = $16,666.67
        # Capitalized: $16,666.67 / 0.07 = $238,095.24
        assert abs(annual_cost - 16666.67) < 1.0
        assert abs(cap_cost - 238095.24) < 1.0

    def test_zero_cap_rate_fallback(self):
        """Test fallback to 10x multiple when cap rate is zero"""
        cap_cost, annual_cost = access.calculate_circuitous_access_cost(
            added_travel_minutes=5.0,
            trips_per_day=20,
            business_days_per_year=250,
            travel_time_value_per_hour=40.0,
            cap_rate=0.0
        )

        # Should use 10x multiple fallback
        assert cap_cost == annual_cost * 10

class TestLandlockedRemedyCost:
    """Test landlocked parcel remedy cost calculations"""

    def test_easement_acquisition_cost(self):
        """Test cost to acquire easement for landlocked parcel"""
        remedy_cost = access.calculate_landlocked_remedy_cost(
            remainder_acres=10.0,
            value_per_acre=100000.0,
            easement_width_meters=20.0,
            easement_length_meters=200.0
        )

        # Easement area: 20m * 200m = 4,000 sq m = 0.988 acres
        # Easement value: 0.988 * $100,000 * 0.12 = $11,856
        # Legal costs: $25,000
        # Survey costs: $8,000
        # Total: $44,856
        expected = (4000 / 4046.86) * 100000.0 * 0.12 + 25000.0 + 8000.0
        assert abs(remedy_cost - expected) < 100.0

class TestAccessDamagesIntegration:
    """Integration tests for complete access damage calculations"""

    def test_frontage_loss_only(self):
        """Test scenario with only frontage loss"""
        # Load from fixture
        # ... test implementation ...

    def test_landlocked_parcel(self):
        """Test complete landlocked parcel scenario"""
        # ... test implementation ...
```

3.3. **Create Shape Damage Tests** (tests/test_shape_damages.py)
```python
class TestShapeEfficiencyIndex:
    """Test shape efficiency index calculations"""

    def test_perfect_square(self):
        """Perfect square should have efficiency index of 1.0"""
        # 10 acres = 435,600 sq ft
        # Perfect square: 660 ft x 660 ft
        efficiency = shape.calculate_shape_efficiency_index(
            acres=10.0,
            frontage_lf=660.0,
            frontage_depth_ratio=1.0  # Square ratio
        )
        assert abs(efficiency - 1.0) < 0.01

    def test_rectangular_1_to_4(self):
        """1:4 frontage:depth ratio (common commercial)"""
        # ... test implementation ...

    def test_landlocked_parcel(self):
        """Landlocked parcel (zero frontage) returns low efficiency"""
        efficiency = shape.calculate_shape_efficiency_index(
            acres=5.0,
            frontage_lf=0.0,
            frontage_depth_ratio=0.0
        )
        assert efficiency == 0.2  # Defined low efficiency for landlocked

    def test_zero_division_protection(self):
        """Ensure no division by zero errors"""
        # Test edge cases that could cause division by zero
        # ... test implementation ...
```

3.4. **Create Utility & Farm Tests** (tests/test_utility_damages.py, tests/test_farm_damages.py)

3.5. **Create Integration Tests** (tests/test_integration.py)
```python
"""End-to-end integration tests"""

import json
from pathlib import Path
from severance_calculator import calculate_severance_damages, load_from_json

class TestEndToEndCalculations:
    """Test complete calculations from JSON to results"""

    def test_highway_frontage_loss_scenario(self):
        """Test complete calculation for highway frontage loss"""
        # Load fixture
        prop_before, taking, remainder, market = load_from_json(
            "tests/fixtures/highway_frontage_loss.json"
        )

        # Calculate
        summary = calculate_severance_damages(
            prop_before, taking, remainder, market
        )

        # Verify results
        assert summary.total_severance_damages > 0
        assert summary.access_damages.total_access_damages > 0
        assert summary.after_value_remainder < summary.before_value_remainder_proportionate

        # Verify reconciliation
        total_comp = summary.before_value_taken + summary.total_severance_damages
        assert total_comp > summary.before_value_taken

    def test_combined_damages_scenario(self):
        """Test scenario with multiple damage categories"""
        # ... test implementation ...
```

**Test Coverage Target**:
```
damages/access.py      95% coverage (19/20 functions)
damages/shape.py       92% coverage (18/19 functions)
damages/utility.py     88% coverage (8/9 functions)
damages/farm.py        90% coverage (9/10 functions)
Overall:               90%+ coverage
```

**Deliverables**:
- ✅ 5 test fixture JSON files
- ✅ tests/test_access_damages.py (6 tests)
- ✅ tests/test_shape_damages.py (6 tests)
- ✅ tests/test_utility_damages.py (4 tests)
- ✅ tests/test_farm_damages.py (4 tests)
- ✅ tests/test_integration.py (5 tests)
- ✅ pytest.ini configuration
- ✅ All tests passing

**Validation**: `pytest --cov=. --cov-report=html` shows 90%+ coverage

---

### Phase 4: Validation & Schema (Day 3 - 4 hours)

**Goal**: Add JSON schema and validation script with auto-fix

**Tasks**:

4.1. **Create JSON Schema** (severance_input_schema.json)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://vp-real-estate.com/schemas/severance-damages-input.json",
  "title": "Severance Damages Calculation Input",
  "description": "Input schema for partial taking severance damage calculations",
  "type": "object",
  "required": ["property_before", "taking", "remainder"],
  "properties": {
    "property_before": {
      "type": "object",
      "required": ["total_acres", "frontage_linear_feet", "road_classification",
                   "shape_ratio_frontage_depth", "value_per_acre", "use"],
      "properties": {
        "total_acres": {
          "type": "number",
          "minimum": 0,
          "maximum": 10000,
          "description": "Total land area before taking in acres"
        },
        "frontage_linear_feet": {
          "type": "number",
          "minimum": 0,
          "maximum": 10000,
          "description": "Road frontage before taking in linear feet"
        },
        "road_classification": {
          "type": "string",
          "enum": ["highway", "arterial", "collector", "local"],
          "description": "Road type classification"
        },
        "shape_ratio_frontage_depth": {
          "type": "number",
          "minimum": 0,
          "maximum": 5.0,
          "description": "Frontage to depth ratio (e.g., 1:4 = 0.25)"
        },
        "value_per_acre": {
          "type": "number",
          "minimum": 0,
          "maximum": 10000000,
          "description": "Market value per acre in dollars"
        },
        "use": {
          "type": "string",
          "enum": ["industrial", "commercial", "residential", "agricultural"],
          "description": "Primary property use classification"
        },
        "development_potential_units": {
          "type": "integer",
          "minimum": 0,
          "description": "Potential development units (lots, dwelling units)"
        },
        "buildable_area_sf": {
          "type": "integer",
          "minimum": 0,
          "description": "Buildable area in square feet"
        }
      }
    },
    "taking": {
      "type": "object",
      "required": ["area_taken_acres", "frontage_lost_linear_feet", "creates_landlocked"],
      "properties": {
        "area_taken_acres": {
          "type": "number",
          "minimum": 0,
          "description": "Area acquired/expropriated in acres"
        },
        "frontage_lost_linear_feet": {
          "type": "number",
          "minimum": 0,
          "description": "Frontage lost to taking in linear feet"
        },
        "creates_landlocked": {
          "type": "boolean",
          "description": "Taking creates landlocked parcel"
        },
        "eliminates_direct_access": {
          "type": "boolean",
          "description": "Taking eliminates direct road access"
        },
        "circuitous_access_added_minutes": {
          "type": "number",
          "minimum": 0,
          "maximum": 120,
          "description": "Additional travel time in minutes"
        },
        "creates_irregular_shape": {
          "type": "boolean",
          "description": "Taking creates irregular parcel shape"
        },
        "severs_utilities": {
          "type": "boolean",
          "description": "Taking severs utility services"
        },
        "reduces_development_potential": {
          "type": "boolean",
          "description": "Taking reduces development potential"
        },
        "bisects_farm": {
          "type": "boolean",
          "description": "Taking bisects farm operation (agricultural only)"
        },
        "disrupts_irrigation": {
          "type": "boolean",
          "description": "Taking disrupts irrigation system (agricultural only)"
        }
      }
    },
    "remainder": {
      "type": "object",
      "required": ["acres", "frontage_remaining_linear_feet",
                   "shape_ratio_frontage_depth", "access_type"],
      "properties": {
        "acres": {
          "type": "number",
          "minimum": 0,
          "description": "Remainder parcel area in acres"
        },
        "frontage_remaining_linear_feet": {
          "type": "number",
          "minimum": 0,
          "description": "Remaining road frontage in linear feet"
        },
        "shape_ratio_frontage_depth": {
          "type": "number",
          "minimum": 0,
          "description": "Frontage to depth ratio after taking"
        },
        "access_type": {
          "type": "string",
          "enum": ["direct", "circuitous", "landlocked"],
          "description": "Type of access remaining"
        },
        "buildable_area_sf": {
          "type": "integer",
          "minimum": 0,
          "description": "Remaining buildable area in square feet"
        },
        "development_potential_units": {
          "type": "integer",
          "minimum": 0,
          "description": "Remaining development potential in units"
        },
        "requires_new_fencing_linear_meters": {
          "type": "number",
          "minimum": 0,
          "description": "New fencing required in linear meters (agricultural)"
        },
        "irrigation_acres_affected": {
          "type": "number",
          "minimum": 0,
          "description": "Acres affected by irrigation disruption (agricultural)"
        }
      }
    },
    "market_parameters": {
      "type": "object",
      "required": ["cap_rate"],
      "properties": {
        "cap_rate": {
          "type": "number",
          "minimum": 0,
          "maximum": 0.20,
          "description": "Market capitalization rate (decimal)"
        },
        "travel_time_value_per_hour": {
          "type": "number",
          "minimum": 0,
          "description": "Value of travel time in $/hour"
        },
        "trips_per_day": {
          "type": "integer",
          "minimum": 0,
          "description": "Average trips per day for access cost modeling"
        },
        "business_days_per_year": {
          "type": "integer",
          "minimum": 0,
          "maximum": 365,
          "description": "Business operating days per year"
        }
      },
      "additionalProperties": true
    }
  }
}
```

4.2. **Create Validation Script** (validate_severance.py)
```python
#!/usr/bin/env python3
"""
Severance Damages JSON Validation Script

Similar to validate_comparables.py for comparable sales calculator.
Validates LLM-extracted or manually-created severance damage inputs.
"""
# Implementation similar to validate_comparables.py but for severance schema
```

4.3. **Create Documentation**
- SCHEMA_DOCUMENTATION.md (field reference)
- VALIDATOR_README.md (usage guide)

**Deliverables**:
- ✅ severance_input_schema.json (complete schema)
- ✅ validate_severance.py (validation script with auto-fix)
- ✅ SCHEMA_DOCUMENTATION.md
- ✅ VALIDATOR_README.md
- ✅ Validation tests passing

**Validation**: `python validate_severance.py tests/fixtures/highway_frontage_loss.json`

---

### Phase 5: Documentation & Integration (Day 3-4 - 4 hours)

**Goal**: Update all documentation and integrate with SKILL.md

**Tasks**:

5.1. **Update SKILL.md**
```markdown
# Severance Damages Quantification Skill

Expert in quantifying loss of value to remainder parcels from partial property takings.

## Overview

Calculates severance damages across four categories:
1. **Access Impairment** - Frontage loss, circuitous access, landlocked remedy
2. **Shape Irregularity** - Geometric inefficiency, buildable area reduction
3. **Utility Impairment** - Highest/best use loss, site servicing costs
4. **Farm Operation Disruption** - Field division, equipment access, irrigation

## Calculation Methodology

### Before/After Appraisal Method
```
Total Compensation = Land Taken Value + Severance Damages

Where:
- Land Taken Value = Area Taken × Unit Value
- Severance Damages = Before Value (Remainder) - After Value (Remainder)
```

### Damage Categories

**1. Access Impairment**
- Frontage loss: $/linear foot method by road classification
- Circuitous access: Time-distance modeling, capitalized
- Landlocked remedy: Cost-to-cure (easement acquisition + legal)

**2. Shape Irregularity**
- Geometric efficiency index (area-to-perimeter ratio)
- Buildable area reduction analysis
- Development yield loss quantification

**3. Utility Impairment**
- Site servicing cost-to-cure
- Development potential reduction
- Highest and best use downgrade

**4. Farm Operation Disruption** (Agricultural only)
- Field division costs (fencing, drainage)
- Equipment access complications (capitalized time)
- Irrigation system repair/replacement

## Calculator Usage

### Command Line

```bash
# Basic calculation
python severance_calculator.py input.json

# Specify output location
python severance_calculator.py input.json results.json

# With validation
python validate_severance.py input.json --fix --output clean.json
python severance_calculator.py clean.json
```

### Python API

```python
from severance_calculator import calculate_severance_damages, load_from_json

# Load from JSON
property_before, taking, remainder, market = load_from_json("input.json")

# Calculate
summary = calculate_severance_damages(
    property_before, taking, remainder, market
)

# Access results
print(f"Total severance damages: ${summary.total_severance_damages:,.2f}")
print(f"Access damages: ${summary.access_damages.total_access_damages:,.2f}")
print(f"Shape damages: ${summary.shape_damages.total_shape_damages:,.2f}")
```

## Input Format

See `severance_input_schema.json` for complete schema.

**Minimal Example**:
```json
{
  "property_before": {
    "total_acres": 10.0,
    "frontage_linear_feet": 500.0,
    "road_classification": "highway",
    "shape_ratio_frontage_depth": 0.25,
    "value_per_acre": 150000.0,
    "use": "commercial"
  },
  "taking": {
    "area_taken_acres": 1.5,
    "frontage_lost_linear_feet": 100.0,
    "creates_landlocked": false
  },
  "remainder": {
    "acres": 8.5,
    "frontage_remaining_linear_feet": 400.0,
    "shape_ratio_frontage_depth": 0.20,
    "access_type": "direct"
  },
  "market_parameters": {
    "cap_rate": 0.07
  }
}
```

## Sample Scenarios

The skill includes 5 tested scenarios:

1. **highway_frontage_loss.json** - Highway frontage reduction
2. **landlocked_parcel.json** - Complete access loss
3. **irregular_shape.json** - Severe shape inefficiency
4. **farm_bisection.json** - Agricultural corridor impact
5. **combined_damages.json** - Multiple damage categories

## Skill Activation

This skill activates when you:
- Mention "severance damages", "partial taking", or "remainder parcel"
- Request expropriation impact analysis
- Ask about access loss, shape inefficiency, or farm bisection
- Reference corridor acquisitions (transmission lines, pipelines, rail)

## Key Methodologies

### Frontage Valuation
Rates by road classification and use ($/linear foot):
- Highway commercial: $500-1,500/LF
- Highway industrial: $300-800/LF
- Arterial commercial: $300-800/LF
- Local residential: $25-75/LF

### Shape Efficiency Index
Based on area-to-perimeter ratio compared to perfect square:
- High efficiency (≥0.8): 2% discount
- Moderate efficiency (0.6-0.8): 8% discount
- Low efficiency (0.4-0.6): 15% discount
- Very low efficiency (<0.4): 30% discount

### Capitalization
Ongoing costs capitalized to present value:
- Cap Rate Method: Annual Cost ÷ Cap Rate
- Fallback: 10x annual cost if cap rate unavailable

## Compliance

- ✅ USPAP 2024 compliant
- ✅ CUSPAP 2024 compliant
- ✅ Canadian expropriation law framework
- ✅ Ontario Expropriations Act methodology

## Files

```
severance-damages-quantification/
├── severance_calculator.py      # Main calculator
├── damages/                     # Modular calculation modules
│   ├── access.py
│   ├── shape.py
│   ├── utility.py
│   └── farm.py
├── tests/                       # 25 unit tests (90% coverage)
├── severance_input_schema.json  # JSON Schema
├── validate_severance.py        # Validation with auto-fix
└── SKILL.md                     # This file
```

## Expert Guidance

When using this skill for professional appraisal work:

1. **Verify Inputs**: Use `validate_severance.py` to catch data issues
2. **Document Methodology**: Calculator includes detailed explanations
3. **Test Sensitivity**: Consider range of market parameters
4. **Professional Judgment**: Calculator provides baseline; adjust for unique factors
5. **Legal Review**: Severance damages are legal claims; consult with legal counsel

## Advanced Features

### Sensitivity Analysis
```python
# Run with different cap rates
for cap_rate in [0.05, 0.07, 0.09]:
    market.cap_rate = cap_rate
    summary = calculate_severance_damages(...)
    print(f"Cap rate {cap_rate:.1%}: ${summary.total_severance_damages:,.2f}")
```

### Custom Constants
```python
from config.constants import CalculationConstants

# Override defaults
constants = CalculationConstants()
constants.EASEMENT_LEGAL_COSTS = 30000.0  # Higher legal market
constants.FENCING_COST_PER_METER = 25.0   # Premium fencing
```

## References

- Appraisal of Real Estate, 15th Edition (Appraisal Institute)
- Ontario Expropriations Act, R.S.O. 1990, c. E.26
- USPAP 2024-2025 Edition
- CUSPAP 2024 Edition
- The Appraisal of Partial Interests (AI, 2016)
```

5.2. **Create README.md**
```markdown
# Severance Damages Calculator

Production-grade calculator for quantifying loss of value to remainder parcels from partial property takings.

## Quick Start

```bash
# Install dependencies
pip install jsonschema pytest pytest-cov

# Run calculation
python severance_calculator.py tests/fixtures/highway_frontage_loss.json

# Run tests
pytest tests/ --cov=. --cov-report=html

# Validate input
python validate_severance.py your_input.json --fix --output clean.json
```

[... rest of README ...]
```

5.3. **Update .gitignore**
```
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.coverage
htmlcov/
*_results.json
```

**Deliverables**:
- ✅ SKILL.md updated with calculator integration
- ✅ README.md created
- ✅ .gitignore updated
- ✅ All documentation cross-referenced

**Validation**: Skill activates correctly when keywords mentioned

---

### Phase 6: Final Testing & Polish (Day 4-5 - 4 hours)

**Goal**: End-to-end validation, performance testing, edge cases

**Tasks**:

6.1. **Edge Case Testing**
- Zero frontage (landlocked)
- Zero cap rate (fallback testing)
- Massive properties (10,000 acres)
- Tiny properties (0.1 acres)
- 100% taking (entire property)
- Multiple property types

6.2. **Performance Testing**
```python
import time

def test_calculation_performance():
    """Calculation should complete in < 100ms"""
    start = time.time()
    summary = calculate_severance_damages(...)
    elapsed = time.time() - start
    assert elapsed < 0.1  # 100ms threshold
```

6.3. **Error Message Quality**
```python
def test_error_messages():
    """Verify user-friendly error messages"""
    try:
        load_from_json("nonexistent.json")
    except FileNotFoundError as e:
        assert "Input file not found" in str(e)
        assert "nonexistent.json" in str(e)
```

6.4. **Backward Compatibility**
- Run all original sample files
- Verify outputs match original (within rounding)
- Confirm CLI interface unchanged

**Deliverables**:
- ✅ 10 edge case tests passing
- ✅ Performance under 100ms
- ✅ Error messages user-friendly
- ✅ 100% backward compatibility

**Validation**: Original workflows still work

---

## File Structure (Final)

```
severance-damages-quantification/
├── severance_calculator.py          # Main orchestrator (300 lines) ✅ REFACTORED
├── config/
│   ├── __init__.py
│   ├── constants.py                 # Centralized magic numbers
│   └── market_parameters.py         # MarketParameters dataclass
├── damages/
│   ├── __init__.py
│   ├── access.py                    # Access impairment (200 lines)
│   ├── shape.py                     # Shape irregularity (200 lines)
│   ├── utility.py                   # Utility impairment (150 lines)
│   └── farm.py                      # Farm disruption (150 lines)
├── models/
│   ├── __init__.py
│   ├── property_data.py             # PropertyBefore, Taking, Remainder
│   └── damage_results.py            # Damage result dataclasses
├── utils/
│   ├── __init__.py
│   ├── validation.py                # Input validation utilities
│   └── calculations.py              # Shared math utilities (safe_divide, etc.)
├── tests/
│   ├── __init__.py
│   ├── test_access_damages.py       # 6 tests
│   ├── test_shape_damages.py        # 6 tests
│   ├── test_utility_damages.py      # 4 tests
│   ├── test_farm_damages.py         # 4 tests
│   ├── test_integration.py          # 5 tests
│   └── fixtures/
│       ├── highway_frontage_loss.json
│       ├── landlocked_parcel.json
│       ├── irregular_shape.json
│       ├── farm_bisection.json
│       └── combined_damages.json
├── severance_input_schema.json      # JSON Schema for validation
├── validate_severance.py            # Validation script with auto-fix
├── SCHEMA_DOCUMENTATION.md          # Schema field reference
├── VALIDATOR_README.md              # Validation usage guide
├── REFACTORING_PLAN.md             # This document
├── SKILL.md                         # Skill documentation ✅ UPDATED
├── README.md                        # Project README ✅ NEW
├── pytest.ini                       # Pytest configuration
└── .gitignore                       # Git ignore patterns

Total Files: 30+
Total Lines: ~2,500 (from 943 monolithic)
Test Coverage: 90%+
Magic Numbers: 0 (all centralized)
```

---

## Testing Strategy

### Test Categories

**Unit Tests** (20 tests)
- damages/access.py: 6 tests
- damages/shape.py: 6 tests
- damages/utility.py: 4 tests
- damages/farm.py: 4 tests

**Integration Tests** (5 tests)
- End-to-end JSON → calculation → output
- Each test fixture scenario

**Validation Tests** (5 tests)
- Schema validation
- Auto-fix functionality
- Error handling

**Performance Tests** (2 tests)
- Calculation speed
- Memory usage

**Edge Case Tests** (10 tests)
- Zero frontage
- Zero cap rate
- Extreme values
- Missing optional fields
- Invalid enum values
- Division by zero scenarios

### Coverage Goals

| Module | Target | Actual |
|--------|--------|--------|
| damages/access.py | 90% | TBD |
| damages/shape.py | 90% | TBD |
| damages/utility.py | 85% | TBD |
| damages/farm.py | 90% | TBD |
| utils/calculations.py | 100% | TBD |
| utils/validation.py | 95% | TBD |
| **Overall** | **90%** | **TBD** |

---

## Risk Mitigation

### Technical Risks

**Risk 1: Breaking Changes**
- **Mitigation**: Maintain backward compatibility
- **Test**: Run original samples, compare outputs
- **Rollback**: Keep original in git history

**Risk 2: Calculation Errors**
- **Mitigation**: Comprehensive unit tests
- **Test**: Verify against manual calculations
- **Validation**: Cross-check with original implementation

**Risk 3: Performance Degradation**
- **Mitigation**: Performance tests
- **Benchmark**: < 100ms per calculation
- **Optimization**: Profile if needed

**Risk 4: Integration Issues**
- **Mitigation**: Test with SKILL.md activation
- **Test**: Verify skill loads correctly
- **Fallback**: Keep activation keywords consistent

### Process Risks

**Risk 1: Timeline Overrun**
- **Mitigation**: Phased implementation
- **Checkpoint**: Each phase independently valuable
- **Adjustment**: Can defer Phase 6 if needed

**Risk 2: Scope Creep**
- **Mitigation**: Strict phase boundaries
- **Control**: No new features during refactor
- **Defer**: Enhancement requests to backlog

---

## Timeline & Milestones

### Week 1: Core Refactoring

**Day 1** (6-8 hours)
- ✅ Phase 1: Foundation (directory structure, config extraction)
- ✅ Phase 2: Modularization (extract calculation modules)
- **Milestone**: Code compiles and runs

**Day 2-3** (12-14 hours)
- ✅ Phase 3: Testing Infrastructure (25 tests)
- ✅ Phase 4: Validation & Schema
- **Milestone**: 90% test coverage, schema validation working

**Day 4** (4-6 hours)
- ✅ Phase 5: Documentation & Integration
- **Milestone**: SKILL.md updated, README complete

**Day 5** (2-4 hours)
- ✅ Phase 6: Final Testing & Polish
- **Milestone**: Production ready

### Total Effort: 24-32 hours (3-5 days)

---

## Success Metrics

### Code Quality Metrics

| Metric | Before | Target | Verification |
|--------|--------|--------|--------------|
| **Test Coverage** | 0% | 90%+ | pytest --cov |
| **Magic Numbers** | 15+ | 0 | grep -r "\b[0-9]\+\.[0-9]\+\b" |
| **Input Validation** | None | 100% | Schema + tests |
| **Error Handling** | 10% | 95%+ | Code review |
| **File Size (main)** | 943 lines | ~300 lines | wc -l |
| **Module Count** | 1 | 15+ | ls -R |
| **Documentation** | Partial | Complete | Review |

### Functional Metrics

- ✅ All original calculations produce same results (±$0.01)
- ✅ All sample files process successfully
- ✅ Validation script catches 100% of schema violations
- ✅ Auto-fix corrects 80%+ of common issues
- ✅ Performance < 100ms per calculation
- ✅ Zero unhandled exceptions

### Professional Metrics

- ✅ SKILL.md integration complete
- ✅ Calculator activates on keyword triggers
- ✅ Calculation methodology documented
- ✅ References to USPAP/CUSPAP included
- ✅ Sample scenarios tested
- ✅ Professional report output

---

## Post-Refactoring Enhancements (Future)

These are **NOT** part of the refactoring plan but identified for future:

### Phase 7: Advanced Features (Future)
- PDF report generation
- Sensitivity analysis module
- Chart generation (value impact visualization)
- Excel export for appraisal reports
- Batch processing (multiple scenarios)

### Phase 8: Additional Property Types (Future)
- Retail property algorithms
- Multi-family property algorithms
- Mixed-use property calculations

### Phase 9: AI Integration (Future)
- LLM extraction from expropriation notices
- Automated scenario generation
- Natural language report writing

---

## Appendix A: Comparison to Comparable Sales Refactoring

### Similarities

Both refactorings follow same pattern:
1. ✅ Modular architecture (separate calculation files)
2. ✅ Centralized configuration
3. ✅ Comprehensive testing (90%+ coverage)
4. ✅ JSON schema validation
5. ✅ Auto-fix validation script
6. ✅ Documentation updates

### Differences

| Aspect | Comparable Sales | Severance Damages |
|--------|------------------|-------------------|
| **Initial Size** | 2,023 lines | 943 lines |
| **Reduction** | 63% (→740 lines) | 68% (→300 lines) |
| **Modules** | 7 adjustment types | 4 damage categories |
| **Complexity** | Higher (49 adjustments) | Lower (4 categories) |
| **Data Structure** | Dicts | Dataclasses ✅ |
| **Refactor Time** | ~20 hours | ~25 hours (est.) |

### Lessons Learned from Comparable Sales

1. ✅ **Do comprehensive planning first** (this document)
2. ✅ **Fix division by zero early** (caused issues)
3. ✅ **Test during refactor** (not after)
4. ✅ **Keep original samples** (for regression testing)
5. ✅ **Document as you go** (easier than retroactive)

---

## Appendix B: Command Reference

### Development Commands

```bash
# Create directory structure
mkdir -p config damages models utils tests tests/fixtures

# Run tests
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html

# Run single test file
pytest tests/test_access_damages.py -v

# Run validation
python validate_severance.py input.json
python validate_severance.py input.json --fix --output clean.json

# Run calculator
python severance_calculator.py input.json
python severance_calculator.py input.json results.json

# Check coverage
coverage run -m pytest tests/
coverage report
coverage html

# Lint code
pylint damages/ models/ config/ utils/
mypy --strict damages/ models/ config/ utils/

# Find magic numbers
grep -rn "[0-9]\+\.[0-9]\+" damages/ models/ config/
```

### Git Workflow

```bash
# Create feature branch
git checkout -b refactor/severance-calculator

# Commit after each phase
git add .
git commit -m "refactor(severance): Phase 1 - foundation and config extraction"
git commit -m "refactor(severance): Phase 2 - modularize calculations"
git commit -m "test(severance): Phase 3 - add comprehensive test suite"
git commit -m "feat(severance): Phase 4 - add validation and schema"
git commit -m "docs(severance): Phase 5 - update documentation"
git commit -m "refactor(severance): Phase 6 - final polish and edge cases"

# Push to remote
git push origin refactor/severance-calculator
```

---

## Appendix C: Code Migration Checklist

### Pre-Refactoring
- [ ] Review current implementation
- [ ] Document all magic numbers
- [ ] Identify division operations
- [ ] List all calculation functions
- [ ] Create test scenarios
- [ ] Backup original file

### Phase 1: Foundation
- [ ] Create directory structure
- [ ] Create config/constants.py
- [ ] Create config/market_parameters.py
- [ ] Create models/property_data.py
- [ ] Create models/damage_results.py
- [ ] Create utils/calculations.py
- [ ] Test imports work

### Phase 2: Modularization
- [ ] Extract damages/access.py
- [ ] Extract damages/shape.py
- [ ] Extract damages/utility.py
- [ ] Extract damages/farm.py
- [ ] Update main calculator imports
- [ ] Update function calls
- [ ] Add logging throughout
- [ ] Test original samples

### Phase 3: Testing
- [ ] Create test fixtures (5 files)
- [ ] Write test_access_damages.py (6 tests)
- [ ] Write test_shape_damages.py (6 tests)
- [ ] Write test_utility_damages.py (4 tests)
- [ ] Write test_farm_damages.py (4 tests)
- [ ] Write test_integration.py (5 tests)
- [ ] Configure pytest.ini
- [ ] Run coverage analysis

### Phase 4: Validation
- [ ] Create severance_input_schema.json
- [ ] Write validate_severance.py
- [ ] Test schema validation
- [ ] Test auto-fix functionality
- [ ] Create SCHEMA_DOCUMENTATION.md
- [ ] Create VALIDATOR_README.md

### Phase 5: Documentation
- [ ] Update SKILL.md
- [ ] Create README.md
- [ ] Update .gitignore
- [ ] Cross-reference docs
- [ ] Test skill activation

### Phase 6: Final Testing
- [ ] Run edge case tests
- [ ] Run performance tests
- [ ] Verify backward compatibility
- [ ] Check error messages
- [ ] Final code review

### Post-Refactoring
- [ ] Tag release (v2.0.0)
- [ ] Archive original (git tag v1.0.0)
- [ ] Update skill index
- [ ] Notify users of update

---

## Conclusion

This refactoring plan transforms the severance damages calculator from a functional script into a production-grade calculation engine with:

✅ **90%+ test coverage** (from 0%)
✅ **100% input validation** (from none)
✅ **Modular architecture** (4 damage modules)
✅ **Zero magic numbers** (all centralized)
✅ **Comprehensive documentation**
✅ **Professional features** (schema, validation, auto-fix)

**Timeline**: 3-5 days (24-32 hours)
**Risk**: Low (backward compatible)
**Value**: High (production hardening for financial calculations)

The refactoring follows proven patterns from the comparable sales calculator refactoring while addressing severance-specific requirements. Upon completion, the calculator will be suitable for professional appraisal work with confidence in accuracy, reliability, and maintainability.

---

**Document Version**: 1.0.0
**Date**: 2025-01-15
**Author**: Claude Code
**Status**: Ready for Implementation
