"""
Traffic disruption impact assessment for injurious affection

Calculates damages from traffic reduction during construction including:
- Lost traffic estimation (from revenue data)
- Sales conversion modeling
- Lost profit calculations

Only applicable to commercial properties (retail, restaurant, service businesses).
"""

import logging
from models.property_data import PropertyDetails, ConstructionActivity
from models.market_parameters import MarketParameters
from models.impact_results import TrafficImpactResult
from config.constants import CONSTANTS
from utils.calculations import safe_divide

logger = logging.getLogger(__name__)


def assess_traffic_impact(
    property_details: PropertyDetails,
    construction: ConstructionActivity,
    params: MarketParameters
) -> TrafficImpactResult:
    """
    Assess traffic disruption and calculate lost sales

    Only applicable to commercial/retail properties where foot traffic drives sales.

    Methodology:
    1. Estimate baseline traffic from annual revenue (or use default)
    2. Calculate lost traffic from reduction percentage
    3. Convert lost traffic to lost sales using conversion rate
    4. Calculate lost profit using gross margin
    5. Total over construction period

    Args:
        property_details: Property characteristics
        construction: Construction activities
        params: Market parameters

    Returns:
        TrafficImpactResult with lost sales estimates
    """
    logger.info("Assessing traffic impact...")

    if property_details.property_type != 'commercial':
        # No traffic impact for non-commercial
        logger.info("  No traffic impact (non-commercial property)")
        return TrafficImpactResult(
            traffic_reduction_pct=0.0,
            baseline_traffic_daily=0.0,
            lost_traffic_daily=0.0,
            lost_sales_daily=0.0,
            lost_profit_daily=0.0,
            duration_months=0.0,
            total_traffic_damage=0.0
        )

    # Estimate baseline traffic from annual revenue
    # Working backwards: Revenue = Traffic × Conversion × Avg Transaction
    baseline_annual_sales = property_details.annual_revenue

    if baseline_annual_sales > 0:
        baseline_daily_sales = safe_divide(
            baseline_annual_sales,
            CONSTANTS.DAYS_PER_YEAR,
            default=0.0
        )
        baseline_daily_transactions = safe_divide(
            baseline_daily_sales,
            params.average_transaction_value,
            default=0.0
        )
        baseline_traffic_daily = safe_divide(
            baseline_daily_transactions,
            params.sales_conversion_rate,
            default=CONSTANTS.DEFAULT_BASELINE_TRAFFIC_DAILY
        )
        logger.info(
            f"  Baseline traffic estimated from revenue: {baseline_traffic_daily:.0f} visitors/day"
        )
    else:
        # Use default estimate if no revenue provided
        baseline_traffic_daily = CONSTANTS.DEFAULT_BASELINE_TRAFFIC_DAILY
        logger.info(
            f"  Using default baseline traffic: {baseline_traffic_daily:.0f} visitors/day "
            "(no revenue data provided)"
        )

    # Calculate lost traffic
    lost_traffic_daily = baseline_traffic_daily * construction.traffic_reduction_pct

    # Convert to lost sales
    lost_transactions = lost_traffic_daily * params.sales_conversion_rate
    lost_sales_daily = lost_transactions * params.average_transaction_value

    # Calculate lost profit (margin × sales)
    lost_profit_daily = lost_sales_daily * params.gross_margin_pct

    # Total over construction period
    days_in_period = construction.duration_months * CONSTANTS.AVERAGE_DAYS_PER_MONTH
    total_traffic_damage = lost_profit_daily * days_in_period

    logger.info(
        f"  Traffic reduction: {construction.traffic_reduction_pct * 100:.1f}% "
        f"({lost_traffic_daily:.0f} visitors/day)"
    )
    logger.info(
        f"  Lost profit: ${lost_profit_daily:,.2f}/day × {days_in_period:.0f} days = "
        f"${total_traffic_damage:,.2f}"
    )

    return TrafficImpactResult(
        traffic_reduction_pct=construction.traffic_reduction_pct,
        baseline_traffic_daily=baseline_traffic_daily,
        lost_traffic_daily=lost_traffic_daily,
        lost_sales_daily=lost_sales_daily,
        lost_profit_daily=lost_profit_daily,
        duration_months=construction.duration_months,
        total_traffic_damage=total_traffic_damage
    )
