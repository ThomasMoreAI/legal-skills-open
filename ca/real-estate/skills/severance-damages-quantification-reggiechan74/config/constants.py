"""
Centralized calculation constants for severance damages

All hardcoded values are consolidated here to eliminate magic numbers
and enable easy configuration for different markets/jurisdictions.
"""

from dataclasses import dataclass


@dataclass
class CalculationConstants:
    """All hardcoded calculation values centralized in one location"""

    # =========================================================================
    # EASEMENT VALUATION CONSTANTS
    # =========================================================================
    EASEMENT_PERCENTAGE_OF_FEE: float = 0.12  # 12% of fee simple value
    EASEMENT_LEGAL_COSTS: float = 25000.0  # Legal fees for easement acquisition
    EASEMENT_SURVEY_COSTS: float = 8000.0  # Survey costs
    DEFAULT_EASEMENT_WIDTH_M: float = 20.0  # Default easement width in meters
    DEFAULT_EASEMENT_LENGTH_M: float = 200.0  # Default easement length in meters

    # =========================================================================
    # DEVELOPMENT VALUE CONSTANTS
    # =========================================================================
    BUILDABLE_VALUE_COMMERCIAL_PER_SF: float = 250.0  # $/sf for commercial buildable area
    BUILDABLE_VALUE_RESIDENTIAL_PER_SF: float = 150.0  # $/sf for residential buildable area
    INDUSTRIAL_LOT_VALUE_PER_UNIT: float = 500000.0  # Value per industrial lot/unit
    RESIDENTIAL_UNIT_VALUE: float = 150000.0  # Value per residential dwelling unit

    # =========================================================================
    # UTILITY RELOCATION COSTS
    # =========================================================================
    WATER_COST_PER_METER: float = 500.0  # $/m for water line relocation
    SEWER_COST_PER_METER: float = 800.0  # $/m for sewer line relocation
    DRAINAGE_ENGINEERING_COST: float = 195000.0  # Engineering + construction for drainage
    DEFAULT_UTILITY_RELOCATION_LENGTH_M: float = 400.0  # Default utility relocation distance

    # =========================================================================
    # AGRICULTURAL / FARM OPERATION COSTS
    # =========================================================================
    FENCING_COST_PER_METER: float = 20.0  # $/m for page wire fencing (livestock)
    TILE_DRAINAGE_PER_METER: float = 15.0  # $/m for tile drainage installation
    DRAINAGE_ENGINEERING_FARM: float = 8000.0  # Engineering for farm drainage modifications
    TILE_INSTALLATION_LENGTH_M: float = 1500.0  # Typical tile drainage length for bisected farm
    EQUIPMENT_OPERATOR_COST_PER_HOUR: float = 150.0  # $/hour for farm equipment + operator
    EQUIPMENT_CROSSINGS_PER_YEAR: int = 30  # Annual equipment crossings for bisected farm
    IRRIGATION_REPAIR_COST: float = 180000.0  # Cost to repair/relocate irrigation system
    IRRIGATION_PREMIUM_PER_ACRE: float = 2000.0  # Value premium for irrigated land

    # =========================================================================
    # DEFAULT MARKET PARAMETERS
    # =========================================================================
    DEFAULT_CAP_RATE: float = 0.07  # 7% capitalization rate
    DEFAULT_CAPITALIZATION_MULTIPLE: float = 10.0  # Fallback multiple when cap_rate = 0
    DEFAULT_TRAVEL_TIME_VALUE: float = 40.0  # $/hour for time-distance modeling
    DEFAULT_TRIPS_PER_DAY: int = 20  # Default trips per day (commercial/industrial)
    DEFAULT_BUSINESS_DAYS_PER_YEAR: int = 250  # Standard business operating days

    # =========================================================================
    # SHAPE EFFICIENCY THRESHOLDS
    # =========================================================================
    # Efficiency index categories (compared to perfect square)
    SHAPE_EFFICIENCY_HIGH: float = 0.8  # ≥0.8 = high efficiency
    SHAPE_EFFICIENCY_MODERATE: float = 0.6  # 0.6-0.8 = moderate efficiency
    SHAPE_EFFICIENCY_LOW: float = 0.4  # 0.4-0.6 = low efficiency
    # <0.4 = very low efficiency

    # Landlocked parcels (zero frontage) get fixed low efficiency
    LANDLOCKED_EFFICIENCY_INDEX: float = 0.2

    # =========================================================================
    # SHAPE INEFFICIENCY VALUE DISCOUNTS
    # =========================================================================
    # Percentage discounts applied to remainder value based on shape efficiency
    SHAPE_DISCOUNT_HIGH: float = 0.02  # 2% discount for high efficiency (0.8-1.0)
    SHAPE_DISCOUNT_MODERATE: float = 0.08  # 8% discount for moderate efficiency (0.6-0.8)
    SHAPE_DISCOUNT_LOW: float = 0.15  # 15% discount for low efficiency (0.4-0.6)
    SHAPE_DISCOUNT_VERY_LOW: float = 0.30  # 30% discount for very low efficiency (<0.4)

    # =========================================================================
    # UTILITY IMPAIRMENT DEFAULTS
    # =========================================================================
    DEVELOPMENT_POTENTIAL_REDUCTION_DISCOUNT: float = 0.10  # 10% discount when dev potential reduced

    # =========================================================================
    # CONVERSION FACTORS
    # =========================================================================
    SQ_FT_PER_ACRE: float = 43560.0  # Square feet per acre
    SQ_M_PER_ACRE: float = 4046.86  # Square meters per acre
    MINUTES_PER_HOUR: float = 60.0  # Minutes per hour


# Global instance (singleton pattern)
CONSTANTS = CalculationConstants()
