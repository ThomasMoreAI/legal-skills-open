"""
Visual impact assessment for injurious affection (permanent impacts)

Calculates permanent damages from visual impairment including:
- Property value reduction from permanent structures/changes
- Capitalization of permanent losses

Based on property valuation methodologies and view impact case law.
"""

import logging
from models.property_data import PropertyDetails
from models.market_parameters import MarketParameters
from models.impact_results import VisualImpactResult

logger = logging.getLogger(__name__)


def assess_visual_impact(
    property_details: PropertyDetails,
    visual_impact_description: str,
    value_reduction_pct: float,
    params: MarketParameters
) -> VisualImpactResult:
    """
    Assess permanent visual impact damages

    Methodology:
    1. Calculate permanent value loss (% of property value)
    2. Capitalize as permanent damage
       (In this case, capitalized impact = permanent value loss,
        since value reduction is already a present value concept)

    Args:
        property_details: Property characteristics
        visual_impact_description: Description of visual impact
        value_reduction_pct: Estimated property value reduction (decimal)
        params: Market parameters

    Returns:
        VisualImpactResult with capitalized permanent damages

    Example:
        - Property value: $500,000
        - Visual impact: 5% reduction
        - Permanent value loss: $25,000
        - Capitalized impact: $25,000
    """
    logger.info("Assessing visual impact...")

    permanent_value_loss = property_details.property_value * value_reduction_pct

    # Capitalize as permanent annual loss
    # Annual loss = Value reduction × Cap rate
    # Total capitalized = Annual loss / Cap rate = Value reduction
    # (Net effect: capitalized impact = permanent value loss)
    capitalized_impact = permanent_value_loss

    logger.info(
        f"  Visual impact: \"{visual_impact_description}\""
    )
    logger.info(
        f"  Property value reduction: {value_reduction_pct * 100:.1f}% "
        f"(${permanent_value_loss:,.2f})"
    )
    logger.info(
        f"  Capitalized permanent damage: ${capitalized_impact:,.2f}"
    )

    return VisualImpactResult(
        visual_impact_description=visual_impact_description,
        property_value_reduction_pct=value_reduction_pct,
        permanent_value_loss=permanent_value_loss,
        capitalized_impact=capitalized_impact
    )
