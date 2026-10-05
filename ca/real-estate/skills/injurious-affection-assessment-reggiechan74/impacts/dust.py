"""
Dust and air quality impact calculations for injurious affection assessment

Calculates damages from construction dust including:
- Cleaning cost estimates based on impact zone
- Cleaning frequency by severity
- Health impact costs for severe long-duration scenarios

Based on air quality assessment methodologies and property damage claims.
"""

import logging
from models.property_data import PropertyDetails, ConstructionActivity
from models.market_parameters import MarketParameters
from models.impact_results import DustImpactResult
from config.constants import CONSTANTS

logger = logging.getLogger(__name__)


def assess_dust_impact(
    property_details: PropertyDetails,
    construction: ConstructionActivity,
    params: MarketParameters
) -> DustImpactResult:
    """
    Assess dust impact and calculate cleaning costs

    Methodology:
    1. Determine cleaning frequency based on impact zone (high/moderate/low)
    2. Select cleaning cost by property type (residential vs. commercial)
    3. Calculate number of cleanings over construction period
    4. Add health impact costs for severe scenarios

    Args:
        property_details: Property characteristics
        construction: Construction activities
        params: Market parameters

    Returns:
        DustImpactResult with cleaning cost estimates
    """
    logger.info("Assessing dust impact...")

    impact_zone = construction.dust_impact_zone

    # Determine cleaning frequency and cost
    if impact_zone == 'high':
        cleaning_frequency_weeks = params.high_impact_cleaning_frequency_weeks
    elif impact_zone == 'moderate':
        cleaning_frequency_weeks = params.moderate_impact_cleaning_frequency_weeks
    else:  # low
        cleaning_frequency_weeks = params.low_impact_cleaning_frequency_weeks

    # Select cleaning cost by property type
    if property_details.property_type == 'residential':
        cleaning_cost = params.residential_cleaning_cost
    else:
        cleaning_cost = params.commercial_cleaning_cost

    # Calculate number of cleanings
    duration_weeks = construction.duration_months * CONSTANTS.AVERAGE_WEEKS_PER_MONTH
    number_of_cleanings = int(duration_weeks / cleaning_frequency_weeks)

    # Total cleaning costs
    total_cleaning_cost = (
        cleaning_cost *
        number_of_cleanings *
        property_details.number_of_units
    )

    logger.info(
        f"  {impact_zone} impact zone: {number_of_cleanings} cleanings @ "
        f"${cleaning_cost:,.2f} × {property_details.number_of_units} units"
    )

    # Health impacts (only for severe cases in high impact zones)
    health_impact_cost = 0.0
    if (impact_zone == 'high' and
        property_details.property_type == 'residential' and
        construction.duration_months >= CONSTANTS.HEALTH_IMPACT_MIN_DURATION_MONTHS):
        # Conservative estimate for potential health impacts
        health_impact_cost = (
            CONSTANTS.HEALTH_IMPACT_COST_PER_UNIT *
            property_details.number_of_units
        )
        logger.info(
            f"  Health impact cost: ${health_impact_cost:,.2f} "
            f"(high impact + long duration: {construction.duration_months} months)"
        )

    total_dust_damage = total_cleaning_cost + health_impact_cost

    logger.info(f"  Total dust damage: ${total_dust_damage:,.2f}")

    return DustImpactResult(
        impact_zone=impact_zone,
        cleaning_frequency_weeks=cleaning_frequency_weeks,
        cleaning_cost_per_event=cleaning_cost,
        number_of_cleanings=number_of_cleanings,
        total_dust_damage=total_dust_damage,
        health_impact_cost=health_impact_cost
    )
