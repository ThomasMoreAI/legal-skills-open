"""
Shape irregularity damage calculations

Calculates damages from geometric inefficiency and reduced development potential:
1. Geometric inefficiency value (area-to-perimeter ratio analysis)
2. Buildable area reduction (loss of usable development area)
3. Development yield loss (reduction in developable units/lots)

USPAP 2024 Compliant
"""

import math
import logging

from models.property_data import PropertyBefore, Taking, Remainder
from models.market_parameters import MarketParameters
from models.damage_results import ShapeDamages
from config.constants import CONSTANTS
from utils.calculations import safe_divide, convert_acres_to_sq_ft

logger = logging.getLogger(__name__)


def calculate_shape_efficiency_index(
    acres: float,
    frontage_lf: float,
    depth_lf: float = None,
    frontage_depth_ratio: float = None
) -> float:
    """
    Calculate shape efficiency index (1.0 = perfect square)

    Uses area-to-perimeter ratio compared to ideal square parcel.
    Lower values indicate less efficient (more irregular) shapes.

    Args:
        acres: Parcel area in acres
        frontage_lf: Frontage in linear feet
        depth_lf: Depth in linear feet (optional if ratio provided)
        frontage_depth_ratio: Frontage:Depth ratio (e.g., 1:4 = 0.25)

    Returns:
        float: Efficiency index (0.0-1.0, where 1.0 is perfect square)
    """
    # Handle landlocked parcels (no frontage)
    if frontage_lf == 0 or (frontage_depth_ratio is not None and frontage_depth_ratio == 0):
        logger.warning(
            "Landlocked parcel detected (zero frontage). "
            f"Using fixed efficiency index of {CONSTANTS.LANDLOCKED_EFFICIENCY_INDEX}"
        )
        return CONSTANTS.LANDLOCKED_EFFICIENCY_INDEX

    # Calculate depth if not provided directly
    if frontage_depth_ratio is not None:
        # Calculate depth from ratio (frontage:depth, e.g., 1:4 = 0.25)
        depth_lf = safe_divide(
            frontage_lf,
            frontage_depth_ratio,
            default=frontage_lf  # Assume square if division fails
        )
    elif depth_lf is None:
        # Assume rectangular and calculate depth from area
        area_sf = convert_acres_to_sq_ft(acres)
        depth_lf = safe_divide(
            area_sf,
            frontage_lf,
            default=math.sqrt(area_sf)  # Assume square if division fails
        )

    # Calculate actual perimeter
    actual_perimeter = 2 * (frontage_lf + depth_lf)

    # Calculate ideal square perimeter for same area
    area_sf = convert_acres_to_sq_ft(acres)
    side_length = math.sqrt(area_sf)
    ideal_perimeter = 4 * side_length

    # Efficiency index = (actual A/P) / (ideal A/P)
    # Higher ratio = more efficient shape
    actual_ratio = safe_divide(area_sf, actual_perimeter, default=0.0)
    ideal_ratio = safe_divide(area_sf, ideal_perimeter, default=1.0)

    efficiency_index = safe_divide(actual_ratio, ideal_ratio, default=1.0)

    logger.debug(
        f"Shape efficiency: {acres:.2f} acres, {frontage_lf:.0f}' frontage, "
        f"{depth_lf:.0f}' depth → {efficiency_index:.3f} index"
    )

    return efficiency_index


def categorize_shape_efficiency(efficiency_index: float) -> str:
    """
    Categorize shape efficiency into standard ranges

    Categories:
    - high: ≥0.8 (near-square, very efficient)
    - moderate: 0.6-0.8 (rectangular, moderately efficient)
    - low: 0.4-0.6 (irregular, less efficient)
    - very_low: <0.4 (highly irregular, inefficient)

    Args:
        efficiency_index: Efficiency index from calculate_shape_efficiency_index

    Returns:
        str: Category ("high", "moderate", "low", "very_low")
    """
    if efficiency_index >= CONSTANTS.SHAPE_EFFICIENCY_HIGH:
        return "high"
    elif efficiency_index >= CONSTANTS.SHAPE_EFFICIENCY_MODERATE:
        return "moderate"
    elif efficiency_index >= CONSTANTS.SHAPE_EFFICIENCY_LOW:
        return "low"
    else:
        return "very_low"


def calculate_shape_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> ShapeDamages:
    """
    Calculate all shape irregularity damages

    Evaluates three types of shape damages:
    1. Geometric inefficiency value (shape ratio analysis)
    2. Buildable area reduction (loss of usable development area)
    3. Development yield loss (reduction in units/lots)

    Args:
        property_before: Property characteristics before taking
        taking: Details of the partial taking
        remainder: Remainder parcel characteristics
        market_params: Market parameters and assumptions

    Returns:
        ShapeDamages: Complete shape damage calculations
    """
    logger.info("=" * 60)
    logger.info("CALCULATING SHAPE DAMAGES")
    logger.info("=" * 60)

    damages = ShapeDamages()

    # 1. Calculate efficiency indices
    damages.efficiency_index_before = calculate_shape_efficiency_index(
        acres=property_before.total_acres,
        frontage_lf=property_before.frontage_linear_feet,
        frontage_depth_ratio=property_before.shape_ratio_frontage_depth
    )

    damages.efficiency_index_after = calculate_shape_efficiency_index(
        acres=remainder.acres,
        frontage_lf=remainder.frontage_remaining_linear_feet,
        frontage_depth_ratio=remainder.shape_ratio_frontage_depth
    )

    logger.info(
        f"Shape efficiency: Before {damages.efficiency_index_before:.3f} → "
        f"After {damages.efficiency_index_after:.3f}"
    )

    # 2. Categorize and apply discount
    damages.efficiency_category = categorize_shape_efficiency(
        damages.efficiency_index_after
    )
    damages.value_discount_pct = market_params.shape_efficiency_discounts[
        damages.efficiency_category
    ]

    logger.info(
        f"Efficiency category: {damages.efficiency_category} "
        f"(discount: {damages.value_discount_pct:.1%})"
    )

    # 3. Calculate geometric inefficiency value loss
    if taking.creates_irregular_shape:
        remainder_base_value = remainder.acres * property_before.value_per_acre
        damages.geometric_inefficiency_value = (
            remainder_base_value * damages.value_discount_pct
        )
        logger.info(
            f"1. Geometric Inefficiency: ${remainder_base_value:,.2f} × "
            f"{damages.value_discount_pct:.1%} = ${damages.geometric_inefficiency_value:,.2f}"
        )

    # 4. Buildable area reduction (if development details provided)
    if (property_before.buildable_area_sf and
        remainder.buildable_area_sf and
        remainder.buildable_area_sf < property_before.buildable_area_sf):

        # Calculate proportionate buildable area expected
        proportionate_buildable = (
            property_before.buildable_area_sf *
            safe_divide(remainder.acres, property_before.total_acres, default=1.0)
        )

        # Value loss from reduced buildable area
        buildable_reduction_sf = proportionate_buildable - remainder.buildable_area_sf

        if buildable_reduction_sf > 0:
            # Use appropriate value per buildable SF based on use
            if property_before.use in ["commercial", "industrial"]:
                value_per_buildable_sf = CONSTANTS.BUILDABLE_VALUE_COMMERCIAL_PER_SF
            else:
                value_per_buildable_sf = CONSTANTS.BUILDABLE_VALUE_RESIDENTIAL_PER_SF

            damages.buildable_area_reduction_value = (
                buildable_reduction_sf * value_per_buildable_sf
            )

            logger.info(
                f"2. Buildable Area Reduction: {buildable_reduction_sf:,.0f} SF × "
                f"${value_per_buildable_sf:.0f}/SF = "
                f"${damages.buildable_area_reduction_value:,.2f}"
            )

    # 5. Development yield loss (if unit counts provided)
    if (property_before.development_potential_units and
        remainder.development_potential_units):

        # Calculate proportionate units expected
        proportionate_units = int(
            property_before.development_potential_units *
            safe_divide(remainder.acres, property_before.total_acres, default=1.0)
        )

        # Value loss from reduced unit yield
        unit_reduction = proportionate_units - remainder.development_potential_units

        if unit_reduction > 0:
            # Use appropriate value per unit based on use
            if property_before.use == "industrial":
                value_per_unit = CONSTANTS.INDUSTRIAL_LOT_VALUE_PER_UNIT
            else:
                value_per_unit = CONSTANTS.RESIDENTIAL_UNIT_VALUE

            damages.development_yield_loss = unit_reduction * value_per_unit

            logger.info(
                f"3. Development Yield Loss: {unit_reduction} units × "
                f"${value_per_unit:,.0f}/unit = "
                f"${damages.development_yield_loss:,.2f}"
            )

    # Calculate total
    damages.calculate_total()

    logger.info("=" * 60)
    logger.info(f"TOTAL SHAPE DAMAGES: ${damages.total_shape_damages:,.2f}")
    logger.info("=" * 60)

    return damages
