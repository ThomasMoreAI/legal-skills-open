"""
Farm operation disruption damage calculations

Calculates damages specific to agricultural properties:
1. Field division costs (fencing, drainage modifications)
2. Equipment access complications (additional travel time, capitalized)
3. Irrigation system impacts (repair/replacement or value loss)

USPAP 2024 Compliant
"""

import logging

from models.property_data import PropertyBefore, Taking, Remainder
from models.market_parameters import MarketParameters
from models.damage_results import FarmDamages
from config.constants import CONSTANTS
from utils.calculations import capitalize_annual_cost

logger = logging.getLogger(__name__)


def calculate_farm_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> FarmDamages:
    """
    Calculate farm operation disruption damages (agricultural use only)

    Evaluates three types of farm damages:
    1. Field division costs (fencing + drainage modifications)
    2. Equipment access complications (time cost, capitalized)
    3. Irrigation system impacts (repair cost or value loss)

    Args:
        property_before: Property characteristics before taking
        taking: Details of the partial taking
        remainder: Remainder parcel characteristics
        market_params: Market parameters and assumptions

    Returns:
        FarmDamages: Complete farm damage calculations
    """
    logger.info("=" * 60)
    logger.info("CALCULATING FARM OPERATION DAMAGES")
    logger.info("=" * 60)

    damages = FarmDamages()

    # Only calculate for agricultural properties
    if property_before.use != "agricultural":
        logger.info("Property use is not agricultural - no farm damages")
        logger.info("=" * 60)
        return damages

    # 1. Field division costs
    if taking.bisects_farm and remainder.requires_new_fencing_linear_meters > 0:
        logger.info("1. Field Division Costs")

        # Fencing costs (page wire for livestock)
        damages.fencing_cost = (
            remainder.requires_new_fencing_linear_meters *
            CONSTANTS.FENCING_COST_PER_METER
        )

        logger.info(
            f"   Fencing: {remainder.requires_new_fencing_linear_meters:.0f}m × "
            f"${CONSTANTS.FENCING_COST_PER_METER:.0f}/m = ${damages.fencing_cost:,.2f}"
        )

        # Drainage modifications (typical for bisected farm)
        tile_cost = (
            CONSTANTS.TILE_INSTALLATION_LENGTH_M *
            CONSTANTS.TILE_DRAINAGE_PER_METER
        )
        damages.drainage_modifications = (
            CONSTANTS.DRAINAGE_ENGINEERING_FARM + tile_cost
        )

        logger.info(
            f"   Drainage engineering: ${CONSTANTS.DRAINAGE_ENGINEERING_FARM:,.2f}"
        )
        logger.info(
            f"   Tile installation: {CONSTANTS.TILE_INSTALLATION_LENGTH_M:.0f}m × "
            f"${CONSTANTS.TILE_DRAINAGE_PER_METER:.0f}/m = ${tile_cost:,.2f}"
        )

        damages.field_division_costs = (
            damages.fencing_cost + damages.drainage_modifications
        )

        logger.info(
            f"   Total field division: ${damages.field_division_costs:,.2f}"
        )

    # 2. Equipment access complications
    if taking.bisects_farm and taking.circuitous_access_added_minutes > 0:
        logger.info("2. Equipment Access Complications")

        # Equipment crossing time cost
        hours_per_crossing = (
            (taking.circuitous_access_added_minutes * 2) /  # Round trip
            CONSTANTS.MINUTES_PER_HOUR
        )

        damages.annual_equipment_time_cost = (
            CONSTANTS.EQUIPMENT_CROSSINGS_PER_YEAR *
            hours_per_crossing *
            CONSTANTS.EQUIPMENT_OPERATOR_COST_PER_HOUR
        )

        logger.info(
            f"   Annual cost: {CONSTANTS.EQUIPMENT_CROSSINGS_PER_YEAR} crossings × "
            f"{hours_per_crossing:.2f} hrs × "
            f"${CONSTANTS.EQUIPMENT_OPERATOR_COST_PER_HOUR:.0f}/hr = "
            f"${damages.annual_equipment_time_cost:,.2f}/yr"
        )

        # Capitalize
        damages.equipment_access_complications = capitalize_annual_cost(
            annual_cost=damages.annual_equipment_time_cost,
            cap_rate=market_params.cap_rate,
            fallback_multiple=CONSTANTS.DEFAULT_CAPITALIZATION_MULTIPLE
        )

        logger.info(
            f"   Capitalized at {market_params.cap_rate:.2%}: "
            f"${damages.equipment_access_complications:,.2f}"
        )

    # 3. Irrigation system impacts
    if taking.disrupts_irrigation and remainder.irrigation_acres_affected > 0:
        logger.info("3. Irrigation System Impacts")

        # Cost to repair irrigation (pump station, distribution lines)
        damages.irrigation_repair_cost = CONSTANTS.IRRIGATION_REPAIR_COST

        # Alternative: value loss approach
        irrigation_premium_per_acre = CONSTANTS.IRRIGATION_PREMIUM_PER_ACRE
        value_loss = (
            remainder.irrigation_acres_affected *
            irrigation_premium_per_acre
        )

        logger.info(
            f"   Repair cost: ${damages.irrigation_repair_cost:,.2f}"
        )
        logger.info(
            f"   Value loss: {remainder.irrigation_acres_affected:.1f} acres × "
            f"${irrigation_premium_per_acre:,.0f}/acre = ${value_loss:,.2f}"
        )

        # Use lower of cost-to-cure or value loss
        damages.irrigation_system_impacts = min(
            damages.irrigation_repair_cost,
            value_loss
        )

        logger.info(
            f"   Using lower of two: ${damages.irrigation_system_impacts:,.2f}"
        )

    # Calculate total
    damages.calculate_total()

    logger.info("=" * 60)
    logger.info(f"TOTAL FARM DAMAGES: ${damages.total_farm_damages:,.2f}")
    logger.info("=" * 60)

    return damages
