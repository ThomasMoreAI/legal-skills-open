"""
Utility impairment damage calculations

Calculates damages from utility/infrastructure impacts:
1. Site servicing costs (water, sewer, drainage relocation)
2. Development potential reduction (highest and best use downgrade)

USPAP 2024 Compliant
"""

import logging

from models.property_data import PropertyBefore, Taking, Remainder
from models.market_parameters import MarketParameters
from models.damage_results import UtilityDamages
from config.constants import CONSTANTS

logger = logging.getLogger(__name__)


def calculate_utility_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> UtilityDamages:
    """
    Calculate utility impairment damages

    Evaluates two types of utility damages:
    1. Site servicing costs (water/sewer/drainage relocation)
    2. Development potential reduction (not already captured in shape damages)

    Args:
        property_before: Property characteristics before taking
        taking: Details of the partial taking
        remainder: Remainder parcel characteristics
        market_params: Market parameters and assumptions

    Returns:
        UtilityDamages: Complete utility damage calculations
    """
    logger.info("=" * 60)
    logger.info("CALCULATING UTILITY DAMAGES")
    logger.info("=" * 60)

    damages = UtilityDamages()

    # 1. Site servicing costs (if utilities severed)
    if taking.severs_utilities:
        logger.info("1. Utilities Severed - Calculating relocation costs")

        # Utility relocation costs
        water_sewer_length_m = CONSTANTS.DEFAULT_UTILITY_RELOCATION_LENGTH_M

        water_cost = water_sewer_length_m * CONSTANTS.WATER_COST_PER_METER
        sewer_cost = water_sewer_length_m * CONSTANTS.SEWER_COST_PER_METER
        drainage_cost = CONSTANTS.DRAINAGE_ENGINEERING_COST

        damages.site_servicing_costs = water_cost + sewer_cost + drainage_cost

        logger.info(
            f"   Water relocation: {water_sewer_length_m:.0f}m × "
            f"${CONSTANTS.WATER_COST_PER_METER:.0f}/m = ${water_cost:,.2f}"
        )
        logger.info(
            f"   Sewer relocation: {water_sewer_length_m:.0f}m × "
            f"${CONSTANTS.SEWER_COST_PER_METER:.0f}/m = ${sewer_cost:,.2f}"
        )
        logger.info(
            f"   Drainage engineering: ${drainage_cost:,.2f}"
        )
        logger.info(
            f"   Total site servicing: ${damages.site_servicing_costs:,.2f}"
        )

    # 2. Development potential reduction
    # Only calculate here if not already captured in shape damages
    if taking.reduces_development_potential and not taking.creates_irregular_shape:
        logger.info(
            "2. Development Potential Reduced (not captured in shape damages)"
        )

        # Apply modest discount for reduced development potential
        remainder_base_value = remainder.acres * property_before.value_per_acre
        damages.development_potential_reduction = (
            remainder_base_value *
            CONSTANTS.DEVELOPMENT_POTENTIAL_REDUCTION_DISCOUNT
        )

        logger.info(
            f"   Base value: ${remainder_base_value:,.2f} × "
            f"{CONSTANTS.DEVELOPMENT_POTENTIAL_REDUCTION_DISCOUNT:.1%} = "
            f"${damages.development_potential_reduction:,.2f}"
        )
    elif taking.reduces_development_potential and taking.creates_irregular_shape:
        logger.info(
            "2. Development Potential Reduced (already captured in shape damages)"
        )

    # Calculate total
    damages.calculate_total()

    logger.info("=" * 60)
    logger.info(f"TOTAL UTILITY DAMAGES: ${damages.total_utility_damages:,.2f}")
    logger.info("=" * 60)

    return damages
