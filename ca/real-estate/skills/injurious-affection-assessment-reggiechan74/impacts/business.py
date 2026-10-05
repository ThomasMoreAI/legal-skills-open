"""
Business loss assessment for injurious affection

Calculates overall business losses from combined impacts including:
- Revenue reduction from noise/disruption
- Lost profit calculations
- Mitigation recommendations

Note: Traffic impact is calculated separately to avoid double-counting.
"""

import logging
from models.property_data import PropertyDetails
from models.impact_results import NoiseImpactResult, TrafficImpactResult, BusinessLossResult
from config.constants import CONSTANTS
from utils.calculations import safe_divide

logger = logging.getLogger(__name__)


def assess_business_loss(
    property_details: PropertyDetails,
    noise_impact: NoiseImpactResult,
    traffic_impact: TrafficImpactResult,
    duration_months: float
) -> BusinessLossResult:
    """
    Assess overall business losses from combined impacts

    Methodology:
    1. Use noise impact as proxy for general revenue reduction
       (Conservative: 50% of rent reduction applied to revenue)
    2. Calculate lost profit using gross margin
    3. Suggest mitigation strategies if impact is severe

    Note: Traffic impact is already calculated separately and not included here
    to avoid double-counting.

    Args:
        property_details: Property characteristics
        noise_impact: Noise impact results
        traffic_impact: Traffic impact results (for logging only)
        duration_months: Construction duration in months

    Returns:
        BusinessLossResult with total business loss
    """
    logger.info("Assessing business loss...")

    baseline_revenue_monthly = safe_divide(
        property_details.annual_revenue,
        CONSTANTS.MONTHS_PER_YEAR,
        default=0.0
    )

    # Estimate revenue reduction from noise impact
    # (Conservative: use half of rent reduction as proxy for revenue impact)
    noise_revenue_reduction_pct = (
        noise_impact.rent_reduction_pct *
        CONSTANTS.BUSINESS_LOSS_REVENUE_REDUCTION_MULTIPLIER
    )

    # Traffic already captured separately, so use noise as baseline
    revenue_reduction_pct = noise_revenue_reduction_pct

    lost_revenue_monthly = baseline_revenue_monthly * revenue_reduction_pct

    # Assume standard gross margin from constants
    lost_profit_monthly = lost_revenue_monthly * CONSTANTS.DEFAULT_GROSS_MARGIN_PCT

    total_business_loss = lost_profit_monthly * duration_months

    logger.info(
        f"  Revenue reduction: {revenue_reduction_pct * 100:.1f}% "
        f"(noise impact proxy)"
    )
    logger.info(
        f"  Lost profit: ${lost_profit_monthly:,.2f}/month × {duration_months} months = "
        f"${total_business_loss:,.2f}"
    )

    # Note: Traffic impact is already calculated separately to avoid double-counting
    if traffic_impact.total_traffic_damage > 0:
        logger.info(
            f"  Note: Traffic impact (${traffic_impact.total_traffic_damage:,.2f}) "
            "calculated separately"
        )

    mitigation_efforts = []
    if revenue_reduction_pct > CONSTANTS.MITIGATION_REVENUE_REDUCTION_THRESHOLD:
        mitigation_efforts.append("Signage to maintain customer awareness")
        mitigation_efforts.append("Extended hours to capture lost traffic")
        logger.info(
            f"  Mitigation recommended: Revenue reduction > "
            f"{CONSTANTS.MITIGATION_REVENUE_REDUCTION_THRESHOLD * 100:.0f}%"
        )

    return BusinessLossResult(
        baseline_revenue_monthly=baseline_revenue_monthly,
        revenue_reduction_pct=revenue_reduction_pct,
        lost_revenue_monthly=lost_revenue_monthly,
        lost_profit_monthly=lost_profit_monthly,
        duration_months=duration_months,
        total_business_loss=total_business_loss,
        mitigation_efforts=mitigation_efforts
    )
