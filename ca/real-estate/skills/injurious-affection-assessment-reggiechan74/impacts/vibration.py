"""
Vibration damage assessment for injurious affection

Calculates damages from construction vibration including:
- PPV (Peak Particle Velocity) threshold analysis
- Cosmetic vs. structural damage classification
- Repair cost estimates

Based on vibration damage criteria and construction monitoring standards.
"""

import logging
from models.property_data import ConstructionActivity
from models.market_parameters import MarketParameters
from models.impact_results import VibrationImpactResult
from config.constants import CONSTANTS

logger = logging.getLogger(__name__)


def assess_vibration_impact(
    construction: ConstructionActivity,
    params: MarketParameters
) -> VibrationImpactResult:
    """
    Assess vibration damage and estimate repair costs

    PPV (Peak Particle Velocity) thresholds:
    - Cosmetic damage: 5-12 mm/s (plaster cracks, minor damage)
    - Structural damage: >12 mm/s (structural cracks, significant damage)

    Args:
        construction: Construction activities
        params: Market parameters

    Returns:
        VibrationImpactResult with damage assessment
    """
    logger.info("Assessing vibration impact...")

    ppv = construction.vibration_ppv_mms

    damage_threshold = "none"
    repair_cost = 0.0

    if ppv >= CONSTANTS.STRUCTURAL_DAMAGE_THRESHOLD_MMS:
        damage_threshold = "structural"
        repair_cost = (
            params.cosmetic_repair_cost_per_incident *
            params.structural_repair_multiplier
        )
        logger.warning(
            f"  STRUCTURAL damage threshold exceeded: {ppv:.1f} mm/s "
            f"(threshold: {CONSTANTS.STRUCTURAL_DAMAGE_THRESHOLD_MMS} mm/s)"
        )
        logger.info(f"  Estimated repair cost: ${repair_cost:,.2f}")

    elif ppv >= CONSTANTS.COSMETIC_DAMAGE_THRESHOLD_MMS:
        damage_threshold = "cosmetic"
        repair_cost = params.cosmetic_repair_cost_per_incident
        logger.info(
            f"  Cosmetic damage threshold exceeded: {ppv:.1f} mm/s "
            f"(threshold: {CONSTANTS.COSMETIC_DAMAGE_THRESHOLD_MMS} mm/s)"
        )
        logger.info(f"  Estimated repair cost: ${repair_cost:,.2f}")

    else:
        logger.info(
            f"  No vibration damage: {ppv:.1f} mm/s "
            f"(below threshold: {CONSTANTS.COSMETIC_DAMAGE_THRESHOLD_MMS} mm/s)"
        )

    return VibrationImpactResult(
        peak_particle_velocity_mms=ppv,
        damage_threshold=damage_threshold,
        repair_cost_estimate=repair_cost,
        total_vibration_damage=repair_cost
    )
