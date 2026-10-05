"""
Noise impact damage calculations for injurious affection assessment

Calculates damages from construction noise including:
- Noise attenuation modeling (distance-based)
- Impact severity classification (moderate vs. severe)
- Rent reduction calculations (temporary loss)
- Night work impact multipliers

Based on Ontario environmental noise guidelines and expropriation case law.
"""

import logging
from models.property_data import PropertyDetails, ConstructionActivity, NoiseEquipment
from models.market_parameters import MarketParameters
from models.impact_results import NoiseImpactResult
from config.constants import CONSTANTS
from utils.acoustic import calculate_noise_attenuation

logger = logging.getLogger(__name__)


def assess_noise_impact(
    property_details: PropertyDetails,
    construction: ConstructionActivity,
    params: MarketParameters
) -> NoiseImpactResult:
    """
    Assess noise impact and calculate damages

    Methodology:
    1. Calculate noise at property from each piece of equipment
    2. Determine impact severity based on property type and noise level
    3. Apply rent reduction percentages with night work multiplier
    4. Calculate total damages over construction duration

    Args:
        property_details: Property characteristics
        construction: Construction activities
        params: Market parameters

    Returns:
        NoiseImpactResult with detailed assessment
    """
    logger.info("Assessing noise impact...")

    equipment_breakdown = []
    max_noise_level = property_details.background_noise_dba

    # Calculate noise from each piece of equipment
    for equip_data in construction.equipment:
        equip = NoiseEquipment(**equip_data)

        noise_at_property = calculate_noise_attenuation(
            equip.dba_at_15m,
            property_details.distance_to_construction_m
        )

        equipment_breakdown.append({
            'equipment_type': equip.equipment_type,
            'dba_at_15m': equip.dba_at_15m,
            'dba_at_property': noise_at_property,
            'hours_per_day': equip.hours_per_day,
            'days_per_week': equip.days_per_week
        })

        # Use maximum noise level (worst case)
        max_noise_level = max(max_noise_level, noise_at_property)

        logger.debug(
            f"  {equip.equipment_type}: {equip.dba_at_15m:.1f} dBA @ 15m → "
            f"{noise_at_property:.1f} dBA @ property"
        )

    # Determine impact severity based on property type
    impact_severity = "none"
    rent_reduction_pct = 0.0

    if property_details.property_type == 'residential':
        # Check for night work (more severe impact)
        night_multiplier = CONSTANTS.NIGHT_WORK_MULTIPLIER if construction.night_work else 1.0

        if max_noise_level >= params.residential_severe_threshold_dba:
            impact_severity = "severe"
            rent_reduction_pct = params.residential_severe_rent_reduction_pct * night_multiplier
        elif max_noise_level >= params.residential_moderate_threshold_dba:
            impact_severity = "moderate"
            rent_reduction_pct = params.residential_moderate_rent_reduction_pct * night_multiplier

        logger.info(
            f"  Residential property: {max_noise_level:.1f} dBA → {impact_severity} impact "
            f"({rent_reduction_pct * 100:.1f}% rent reduction)"
        )

    elif property_details.property_type == 'commercial':
        if max_noise_level >= params.commercial_severe_threshold_dba:
            impact_severity = "severe"
            rent_reduction_pct = params.commercial_severe_rent_reduction_pct
        elif max_noise_level >= params.commercial_moderate_threshold_dba:
            impact_severity = "moderate"
            rent_reduction_pct = params.commercial_moderate_rent_reduction_pct

        logger.info(
            f"  Commercial property: {max_noise_level:.1f} dBA → {impact_severity} impact "
            f"({rent_reduction_pct * 100:.1f}% rent reduction)"
        )

    elif property_details.property_type == 'industrial':
        if max_noise_level >= params.industrial_threshold_dba:
            impact_severity = "moderate"
            rent_reduction_pct = CONSTANTS.INDUSTRIAL_MODERATE_RENT_REDUCTION_PCT

        logger.info(
            f"  Industrial property: {max_noise_level:.1f} dBA → {impact_severity} impact "
            f"({rent_reduction_pct * 100:.1f}% rent reduction)"
        )

    # Cap reduction at reasonable maximum
    rent_reduction_pct = min(rent_reduction_pct, CONSTANTS.MAX_RENT_REDUCTION_PCT)

    # Calculate monetary damages
    monthly_rental_loss = (
        property_details.rental_income_monthly *
        property_details.number_of_units *
        rent_reduction_pct
    )

    total_noise_damage = monthly_rental_loss * construction.duration_months

    logger.info(
        f"  Total noise damage: ${total_noise_damage:,.2f} "
        f"(${monthly_rental_loss:,.2f}/month × {construction.duration_months} months)"
    )

    return NoiseImpactResult(
        noise_level_at_property_dba=max_noise_level,
        impact_severity=impact_severity,
        rent_reduction_pct=rent_reduction_pct,
        duration_months=construction.duration_months,
        monthly_rental_loss=monthly_rental_loss,
        total_noise_damage=total_noise_damage,
        equipment_breakdown=equipment_breakdown
    )
