"""
Access impairment damage calculations

Calculates three types of access damages:
1. Frontage loss value ($/linear foot method by road classification)
2. Circuitous access cost (time-distance modeling, capitalized)
3. Landlocked remedy cost (easement acquisition + legal fees)

USPAP 2024 Compliant
"""

from typing import Tuple
import logging

from models.property_data import PropertyBefore, Taking, Remainder
from models.market_parameters import MarketParameters
from models.damage_results import AccessDamages
from config.constants import CONSTANTS
from utils.calculations import capitalize_annual_cost, convert_sq_m_to_acres

logger = logging.getLogger(__name__)


def calculate_frontage_loss_value(
    frontage_lost_lf: float,
    road_classification: str,
    property_use: str,
    market_params: MarketParameters
) -> Tuple[float, float]:
    """
    Calculate value loss from loss of road frontage using $/linear foot method

    Args:
        frontage_lost_lf: Frontage lost in linear feet
        road_classification: Road type ("highway", "arterial", "collector", "local")
        property_use: Property use ("industrial", "commercial", "residential", "agricultural")
        market_params: Market parameters including frontage values

    Returns:
        tuple: (frontage_loss_value, rate_used_per_lf)
    """
    if frontage_lost_lf <= 0:
        logger.debug("No frontage lost, returning zero value")
        return 0.0, 0.0

    # Get frontage value range for this road class and use combination
    try:
        value_range = market_params.frontage_values[road_classification][property_use]
        # Use midpoint of range
        rate_per_lf = (value_range[0] + value_range[1]) / 2
        logger.debug(
            f"Frontage rate for {road_classification} / {property_use}: "
            f"${value_range[0]:.0f}-${value_range[1]:.0f}/LF (using ${rate_per_lf:.0f}/LF)"
        )
    except KeyError:
        # Default to low end if combination not found
        rate_per_lf = 50.0
        logger.warning(
            f"No frontage value found for {road_classification} / {property_use}. "
            f"Using default ${rate_per_lf:.0f}/LF"
        )

    frontage_value = frontage_lost_lf * rate_per_lf

    logger.info(
        f"Frontage loss: {frontage_lost_lf:.1f} LF × ${rate_per_lf:.0f}/LF = ${frontage_value:,.2f}"
    )

    return frontage_value, rate_per_lf


def calculate_circuitous_access_cost(
    added_travel_minutes: float,
    trips_per_day: int,
    business_days_per_year: int,
    travel_time_value_per_hour: float,
    cap_rate: float
) -> Tuple[float, float]:
    """
    Calculate capitalized cost of circuitous access using time-distance modeling

    Args:
        added_travel_minutes: Additional travel time in minutes per trip
        trips_per_day: Number of trips per day
        business_days_per_year: Business operating days per year
        travel_time_value_per_hour: Value of time in dollars per hour
        cap_rate: Capitalization rate (decimal)

    Returns:
        tuple: (capitalized_cost, annual_time_cost)
    """
    if added_travel_minutes <= 0:
        logger.debug("No additional travel time, returning zero cost")
        return 0.0, 0.0

    # Calculate annual time cost
    hours_per_trip = added_travel_minutes / CONSTANTS.MINUTES_PER_HOUR
    annual_trips = trips_per_day * business_days_per_year
    annual_time_cost = annual_trips * hours_per_trip * travel_time_value_per_hour

    logger.debug(
        f"Time cost calculation: {added_travel_minutes:.1f} min/trip × "
        f"{trips_per_day} trips/day × {business_days_per_year} days/yr × "
        f"${travel_time_value_per_hour:.0f}/hr = ${annual_time_cost:,.2f}/yr"
    )

    # Capitalize to present value
    capitalized_cost = capitalize_annual_cost(
        annual_cost=annual_time_cost,
        cap_rate=cap_rate,
        fallback_multiple=CONSTANTS.DEFAULT_CAPITALIZATION_MULTIPLE
    )

    logger.info(
        f"Circuitous access cost: ${annual_time_cost:,.2f}/yr capitalized at "
        f"{cap_rate:.2%} = ${capitalized_cost:,.2f}"
    )

    return capitalized_cost, annual_time_cost


def calculate_landlocked_remedy_cost(
    remainder_acres: float,
    value_per_acre: float,
    easement_width_meters: float = None,
    easement_length_meters: float = None
) -> float:
    """
    Calculate cost to cure landlocked parcel via easement acquisition

    Uses cost-to-cure methodology (easement value + legal/survey costs).
    Alternative approach: 50-80% value loss if no easement obtainable.

    Args:
        remainder_acres: Size of remainder parcel in acres
        value_per_acre: Value per acre of land
        easement_width_meters: Width of easement needed (default: 20m)
        easement_length_meters: Length of easement needed (default: 200m)

    Returns:
        float: Total cost to cure landlocked condition
    """
    # Use defaults if not specified
    if easement_width_meters is None:
        easement_width_meters = CONSTANTS.DEFAULT_EASEMENT_WIDTH_M
    if easement_length_meters is None:
        easement_length_meters = CONSTANTS.DEFAULT_EASEMENT_LENGTH_M

    # Calculate easement area
    easement_sq_m = easement_width_meters * easement_length_meters
    easement_acres = convert_sq_m_to_acres(easement_sq_m)

    # Easement value: percentage of fee simple value for affected land
    easement_value = (
        easement_acres *
        value_per_acre *
        CONSTANTS.EASEMENT_PERCENTAGE_OF_FEE
    )

    logger.debug(
        f"Easement: {easement_width_meters:.0f}m × {easement_length_meters:.0f}m = "
        f"{easement_sq_m:.0f} sq m ({easement_acres:.2f} acres) × "
        f"${value_per_acre:,.0f}/acre × {CONSTANTS.EASEMENT_PERCENTAGE_OF_FEE:.0%} = "
        f"${easement_value:,.2f}"
    )

    # Transaction costs
    total_remedy_cost = (
        easement_value +
        CONSTANTS.EASEMENT_LEGAL_COSTS +
        CONSTANTS.EASEMENT_SURVEY_COSTS
    )

    logger.info(
        f"Landlocked remedy cost: Easement ${easement_value:,.2f} + "
        f"Legal ${CONSTANTS.EASEMENT_LEGAL_COSTS:,.2f} + "
        f"Survey ${CONSTANTS.EASEMENT_SURVEY_COSTS:,.2f} = "
        f"${total_remedy_cost:,.2f}"
    )

    return total_remedy_cost


def calculate_access_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> AccessDamages:
    """
    Calculate all access impairment damages

    Evaluates three types of access damages:
    1. Frontage loss value ($/LF method)
    2. Circuitous access cost (time-distance, capitalized)
    3. Landlocked remedy cost (cost-to-cure)

    Args:
        property_before: Property characteristics before taking
        taking: Details of the partial taking
        remainder: Remainder parcel characteristics
        market_params: Market parameters and assumptions

    Returns:
        AccessDamages: Complete access damage calculations
    """
    logger.info("=" * 60)
    logger.info("CALCULATING ACCESS DAMAGES")
    logger.info("=" * 60)

    damages = AccessDamages()

    # 1. Frontage loss value ($/linear foot method)
    if taking.frontage_lost_linear_feet > 0:
        logger.info(f"1. Frontage Loss: {taking.frontage_lost_linear_feet:.1f} LF lost")
        try:
            damages.frontage_loss_value, damages.frontage_rate_used = (
                calculate_frontage_loss_value(
                    frontage_lost_lf=taking.frontage_lost_linear_feet,
                    road_classification=property_before.road_classification,
                    property_use=property_before.use,
                    market_params=market_params
                )
            )
        except Exception as e:
            logger.error(f"Error calculating frontage loss: {e}")
            raise

    # 2. Circuitous access cost (time-distance modeling)
    if taking.eliminates_direct_access and taking.circuitous_access_added_minutes > 0:
        logger.info(
            f"2. Circuitous Access: +{taking.circuitous_access_added_minutes:.1f} min/trip"
        )
        try:
            damages.circuitous_access_cost, damages.annual_time_cost = (
                calculate_circuitous_access_cost(
                    added_travel_minutes=taking.circuitous_access_added_minutes,
                    trips_per_day=market_params.trips_per_day,
                    business_days_per_year=market_params.business_days_per_year,
                    travel_time_value_per_hour=market_params.travel_time_value_per_hour,
                    cap_rate=market_params.cap_rate
                )
            )
            damages.capitalized_time_cost = damages.circuitous_access_cost
        except Exception as e:
            logger.error(f"Error calculating circuitous access cost: {e}")
            raise

    # 3. Landlocked parcel remedy cost
    if taking.creates_landlocked or remainder.access_type == "landlocked":
        logger.info("3. Landlocked Parcel: Cost to cure via easement acquisition")
        try:
            damages.landlocked_remedy_cost = calculate_landlocked_remedy_cost(
                remainder_acres=remainder.acres,
                value_per_acre=property_before.value_per_acre
            )
        except Exception as e:
            logger.error(f"Error calculating landlocked remedy cost: {e}")
            raise

    # Calculate total
    damages.calculate_total()

    logger.info("=" * 60)
    logger.info(f"TOTAL ACCESS DAMAGES: ${damages.total_access_damages:,.2f}")
    logger.info("=" * 60)

    return damages
