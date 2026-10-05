"""
Centralized calculation constants for injurious affection calculator

All magic numbers and configuration parameters centralized here for easy modification
and professional configuration management.

Based on Ontario expropriation law, construction impact methodologies, and industry standards.
"""

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class CalculationConstants:
    """All hardcoded values centralized in one location"""

    # =========================================================================
    # NOISE IMPACT THRESHOLDS (dBA)
    # =========================================================================
    # Residential property noise thresholds
    RESIDENTIAL_MODERATE_THRESHOLD_DBA: float = 65.0  # Moderate impact threshold
    RESIDENTIAL_SEVERE_THRESHOLD_DBA: float = 75.0    # Severe impact threshold

    # Commercial property noise thresholds
    COMMERCIAL_MODERATE_THRESHOLD_DBA: float = 70.0   # Moderate impact threshold
    COMMERCIAL_SEVERE_THRESHOLD_DBA: float = 80.0     # Severe impact threshold

    # Industrial property noise threshold
    INDUSTRIAL_THRESHOLD_DBA: float = 85.0            # Industrial threshold
    INDUSTRIAL_MODERATE_RENT_REDUCTION_PCT: float = 0.03  # 3% for industrial

    # Background noise level
    DEFAULT_BACKGROUND_NOISE_DBA: float = 50.0        # Typical ambient noise

    # =========================================================================
    # RENT REDUCTION PERCENTAGES
    # =========================================================================
    # Residential rent reduction by severity
    RESIDENTIAL_MODERATE_RENT_REDUCTION_PCT: float = 0.075  # 7.5%
    RESIDENTIAL_SEVERE_RENT_REDUCTION_PCT: float = 0.20     # 20%

    # Commercial rent reduction by severity
    COMMERCIAL_MODERATE_RENT_REDUCTION_PCT: float = 0.055   # 5.5%
    COMMERCIAL_SEVERE_RENT_REDUCTION_PCT: float = 0.125     # 12.5%

    # Night work multiplier (more severe impact)
    NIGHT_WORK_MULTIPLIER: float = 1.5                      # 1.5x for night work

    # Maximum rent reduction cap
    MAX_RENT_REDUCTION_PCT: float = 0.30                    # Cap at 30%

    # =========================================================================
    # DUST CLEANING COSTS
    # =========================================================================
    # Cleaning cost per event by property type
    RESIDENTIAL_CLEANING_COST: float = 200.0                # Per cleaning event
    COMMERCIAL_CLEANING_COST: float = 1000.0                # Per cleaning event

    # Cleaning frequency by impact zone (weeks)
    HIGH_IMPACT_CLEANING_FREQUENCY_WEEKS: int = 1           # Weekly
    MODERATE_IMPACT_CLEANING_FREQUENCY_WEEKS: int = 2       # Bi-weekly
    LOW_IMPACT_CLEANING_FREQUENCY_WEEKS: int = 4            # Monthly

    # Health impact costs (severe long-duration scenarios)
    HEALTH_IMPACT_COST_PER_UNIT: float = 5000.0             # Per residential unit
    HEALTH_IMPACT_MIN_DURATION_MONTHS: float = 6.0          # Minimum duration for health impacts

    # =========================================================================
    # VIBRATION THRESHOLDS AND COSTS
    # =========================================================================
    # PPV (Peak Particle Velocity) thresholds in mm/s
    COSMETIC_DAMAGE_THRESHOLD_MMS: float = 5.0              # Cosmetic damage threshold
    STRUCTURAL_DAMAGE_THRESHOLD_MMS: float = 12.0           # Structural damage threshold

    # Repair costs
    COSMETIC_REPAIR_COST: float = 2500.0                    # Base cosmetic repair cost
    STRUCTURAL_REPAIR_MULTIPLIER: float = 10.0              # Structural is 10x cosmetic

    # =========================================================================
    # TRAFFIC / BUSINESS PARAMETERS
    # =========================================================================
    # Traffic to sales conversion
    DEFAULT_SALES_CONVERSION_RATE: float = 0.02             # 2% of traffic converts
    DEFAULT_TRANSACTION_VALUE: float = 50.0                 # Average transaction
    DEFAULT_GROSS_MARGIN_PCT: float = 0.40                  # 40% gross margin

    # Default traffic estimate (when no revenue data available)
    DEFAULT_BASELINE_TRAFFIC_DAILY: float = 1000.0          # Default daily traffic

    # Business loss estimation (conservative proxy)
    BUSINESS_LOSS_REVENUE_REDUCTION_MULTIPLIER: float = 0.5  # 50% of noise impact

    # =========================================================================
    # VISUAL IMPACT PARAMETERS
    # =========================================================================
    # Visual impact property value reduction percentages (not currently used - input driven)
    MINOR_VISUAL_IMPACT_PCT: float = 0.02                   # 2% minor impact
    MODERATE_VISUAL_IMPACT_PCT: float = 0.05                # 5% moderate impact
    SEVERE_VISUAL_IMPACT_PCT: float = 0.10                  # 10% severe impact

    # =========================================================================
    # CAPITALIZATION AND TIME PARAMETERS
    # =========================================================================
    # Capitalization rate for permanent impacts
    DEFAULT_CAP_RATE: float = 0.08                          # 8% capitalization rate

    # Time conversion factors
    MONTHS_PER_YEAR: int = 12
    WEEKS_PER_YEAR: int = 52
    DAYS_PER_YEAR: int = 365
    BUSINESS_DAYS_PER_YEAR: int = 250
    AVERAGE_WEEKS_PER_MONTH: float = 4.33                   # 52/12
    AVERAGE_DAYS_PER_MONTH: float = 30.42                   # 365/12

    # =========================================================================
    # ACOUSTIC CALCULATIONS
    # =========================================================================
    # Noise attenuation parameters
    NOISE_REFERENCE_DISTANCE_M: float = 15.0                # Reference measurement distance
    NOISE_ATTENUATION_DB_PER_DOUBLING: float = 6.0          # dB reduction per distance doubling
    MIN_NOISE_LEVEL_DBA: float = 0.0                        # Minimum noise level (floor)

    # =========================================================================
    # MITIGATION THRESHOLDS
    # =========================================================================
    # Revenue reduction threshold for recommended mitigation
    MITIGATION_REVENUE_REDUCTION_THRESHOLD: float = 0.10    # 10% reduction triggers recommendations


# Global singleton instance
CONSTANTS = CalculationConstants()


def get_constants() -> CalculationConstants:
    """
    Get global constants instance

    Returns:
        CalculationConstants: Global configuration constants
    """
    return CONSTANTS


def validate_constants():
    """
    Validate that all constants are within reasonable ranges

    Raises:
        ValueError: If any constant is out of acceptable range
    """
    c = CONSTANTS

    # Validate noise thresholds
    if not (0 < c.RESIDENTIAL_MODERATE_THRESHOLD_DBA < c.RESIDENTIAL_SEVERE_THRESHOLD_DBA):
        raise ValueError("Residential noise thresholds must be positive and ascending")

    if not (0 < c.COMMERCIAL_MODERATE_THRESHOLD_DBA < c.COMMERCIAL_SEVERE_THRESHOLD_DBA):
        raise ValueError("Commercial noise thresholds must be positive and ascending")

    # Validate percentages (0-100%)
    percentages = [
        c.RESIDENTIAL_MODERATE_RENT_REDUCTION_PCT,
        c.RESIDENTIAL_SEVERE_RENT_REDUCTION_PCT,
        c.COMMERCIAL_MODERATE_RENT_REDUCTION_PCT,
        c.COMMERCIAL_SEVERE_RENT_REDUCTION_PCT,
        c.MAX_RENT_REDUCTION_PCT,
        c.DEFAULT_SALES_CONVERSION_RATE,
        c.DEFAULT_GROSS_MARGIN_PCT,
    ]
    for pct in percentages:
        if not (0 <= pct <= 1.0):
            raise ValueError(f"Percentage out of range [0, 1.0]: {pct}")

    # Validate vibration thresholds
    if not (0 < c.COSMETIC_DAMAGE_THRESHOLD_MMS < c.STRUCTURAL_DAMAGE_THRESHOLD_MMS):
        raise ValueError("Vibration thresholds must be positive and ascending")

    # Validate costs (must be positive)
    costs = [
        c.RESIDENTIAL_CLEANING_COST,
        c.COMMERCIAL_CLEANING_COST,
        c.COSMETIC_REPAIR_COST,
        c.DEFAULT_TRANSACTION_VALUE,
    ]
    for cost in costs:
        if cost <= 0:
            raise ValueError(f"Cost must be positive: {cost}")

    logger.info("✓ All constants validated successfully")


# Run validation on import
try:
    validate_constants()
except ValueError as e:
    logger.error(f"Constants validation failed: {e}")
    raise
