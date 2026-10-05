"""
Market parameters for injurious affection valuation

This module provides default market parameters that can be overridden via JSON input.
All defaults are sourced from config/constants.py for centralized management.
"""

from dataclasses import dataclass
from config.constants import CONSTANTS


@dataclass
class MarketParameters:
    """
    Market parameters for valuation

    Provides default values for all market assumptions used in damage calculations.
    Can be overridden via JSON input for market-specific adjustments.
    """
    # Noise impact thresholds (dBA)
    residential_moderate_threshold_dba: float = CONSTANTS.RESIDENTIAL_MODERATE_THRESHOLD_DBA
    residential_severe_threshold_dba: float = CONSTANTS.RESIDENTIAL_SEVERE_THRESHOLD_DBA
    commercial_moderate_threshold_dba: float = CONSTANTS.COMMERCIAL_MODERATE_THRESHOLD_DBA
    commercial_severe_threshold_dba: float = CONSTANTS.COMMERCIAL_SEVERE_THRESHOLD_DBA
    industrial_threshold_dba: float = CONSTANTS.INDUSTRIAL_THRESHOLD_DBA

    # Rent reduction percentages
    residential_moderate_rent_reduction_pct: float = CONSTANTS.RESIDENTIAL_MODERATE_RENT_REDUCTION_PCT
    residential_severe_rent_reduction_pct: float = CONSTANTS.RESIDENTIAL_SEVERE_RENT_REDUCTION_PCT
    commercial_moderate_rent_reduction_pct: float = CONSTANTS.COMMERCIAL_MODERATE_RENT_REDUCTION_PCT
    commercial_severe_rent_reduction_pct: float = CONSTANTS.COMMERCIAL_SEVERE_RENT_REDUCTION_PCT

    # Dust cleaning costs
    residential_cleaning_cost: float = CONSTANTS.RESIDENTIAL_CLEANING_COST
    commercial_cleaning_cost: float = CONSTANTS.COMMERCIAL_CLEANING_COST
    high_impact_cleaning_frequency_weeks: int = CONSTANTS.HIGH_IMPACT_CLEANING_FREQUENCY_WEEKS
    moderate_impact_cleaning_frequency_weeks: int = CONSTANTS.MODERATE_IMPACT_CLEANING_FREQUENCY_WEEKS
    low_impact_cleaning_frequency_weeks: int = CONSTANTS.LOW_IMPACT_CLEANING_FREQUENCY_WEEKS

    # Vibration repair costs
    cosmetic_repair_cost_per_incident: float = CONSTANTS.COSMETIC_REPAIR_COST
    structural_repair_multiplier: float = CONSTANTS.STRUCTURAL_REPAIR_MULTIPLIER

    # Traffic disruption parameters
    sales_conversion_rate: float = CONSTANTS.DEFAULT_SALES_CONVERSION_RATE
    average_transaction_value: float = CONSTANTS.DEFAULT_TRANSACTION_VALUE
    gross_margin_pct: float = CONSTANTS.DEFAULT_GROSS_MARGIN_PCT

    # Capitalization rate for permanent impacts
    capitalization_rate: float = CONSTANTS.DEFAULT_CAP_RATE
