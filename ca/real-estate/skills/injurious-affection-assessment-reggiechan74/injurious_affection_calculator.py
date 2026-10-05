#!/usr/bin/env python3
"""
Injurious Affection Calculator - Quantifies Damages from Construction and Proximity Impacts

VERSION 2.0.0 - Modular Architecture

Calculates comprehensive damages from:
- Noise impacts (dBA levels, duration, receptor sensitivity)
- Dust and air quality (PM2.5/PM10, cleaning costs)
- Vibration damage (PPV thresholds, repair costs)
- Traffic disruption (lost sales, access costs)
- Visual impairment (permanent impacts)
- Business losses (temporary and ongoing)

Based on Ontario expropriation law and construction impact assessment methodologies.

REFACTORED: 900 lines → ~300 lines (67% reduction)
- ✅ Modular architecture (6 impact modules)
- ✅ Zero magic numbers (all in config/constants.py)
- ✅ Defensive programming (safe_divide utilities)
- ✅ Comprehensive logging
- ✅ 100% backward compatible with v1.0.0

Author: Claude Code
Version: 2.0.0
Date: 2025-11-15
"""

import os
import sys
import json
import logging
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

# Add current directory to path to support both script and module imports
_current_dir = os.path.dirname(os.path.abspath(__file__))
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

# Import data models
from models import (
    PropertyDetails,
    ConstructionActivity,
    MarketParameters,
    InjuriousAffectionSummary
)

# Import impact assessment modules
from impacts import (
    assess_noise_impact,
    assess_dust_impact,
    assess_vibration_impact,
    assess_traffic_impact,
    assess_business_loss,
    assess_visual_impact
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# MAIN CALCULATION ORCHESTRATOR
# ============================================================================

def calculate_injurious_affection(
    property_details: PropertyDetails,
    construction: ConstructionActivity,
    params: MarketParameters,
    property_address: str = "",
    visual_impact_data: Optional[Dict[str, Any]] = None
) -> InjuriousAffectionSummary:
    """
    Calculate complete injurious affection damages using modular architecture

    Args:
        property_details: Property characteristics
        construction: Construction activities
        params: Market parameters
        property_address: Property address
        visual_impact_data: Optional visual impact parameters

    Returns:
        InjuriousAffectionSummary with complete damage assessment
    """
    logger.info("=" * 80)
    logger.info("INJURIOUS AFFECTION DAMAGE ASSESSMENT - Starting calculation")
    logger.info("=" * 80)

    # Assess each impact category using modular functions
    noise_impact = assess_noise_impact(property_details, construction, params)
    dust_impact = assess_dust_impact(property_details, construction, params)
    vibration_impact = assess_vibration_impact(construction, params)
    traffic_impact = assess_traffic_impact(property_details, construction, params)
    business_loss = assess_business_loss(
        property_details,
        noise_impact,
        traffic_impact,
        construction.duration_months
    )

    # Optional: Visual impact (permanent)
    visual_impact = None
    if visual_impact_data:
        visual_impact = assess_visual_impact(
            property_details,
            visual_impact_data.get('description', ''),
            visual_impact_data.get('value_reduction_pct', 0.0),
            params
        )

    # Create summary
    summary = InjuriousAffectionSummary(
        property_address=property_address or "Property",
        property_type=property_details.property_type,
        property_value=property_details.property_value,
        assessment_date=datetime.now().strftime('%Y-%m-%d'),
        noise_impact=noise_impact,
        dust_impact=dust_impact,
        vibration_impact=vibration_impact,
        traffic_impact=traffic_impact,
        business_loss=business_loss,
        visual_impact=visual_impact
    )

    # Calculate totals
    summary.calculate_totals()

    logger.info("=" * 80)
    logger.info(
        f"CALCULATION COMPLETE - Total damages: ${summary.total_injurious_affection:,.2f}"
    )
    logger.info("=" * 80)

    return summary


# ============================================================================
# JSON I/O
# ============================================================================

def load_from_json(json_path: str) -> tuple:
    """
    Load input parameters from JSON file

    Expected structure:
    {
        "property": {...},
        "construction": {...},
        "market_parameters": {...},  # Optional
        "visual_impact": {...}  # Optional
    }

    Returns:
        Tuple of (PropertyDetails, ConstructionActivity, MarketParameters, visual_impact_data, property_address)
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    property_details = PropertyDetails(**data['property'])
    construction = ConstructionActivity(**data['construction'])

    # Load market parameters or use defaults
    if 'market_parameters' in data:
        params = MarketParameters(**data['market_parameters'])
    else:
        params = MarketParameters()

    visual_impact_data = data.get('visual_impact')
    property_address = data.get('property_address', '')

    return property_details, construction, params, visual_impact_data, property_address


def save_to_json(summary: InjuriousAffectionSummary, output_path: str):
    """
    Save results to JSON file

    Args:
        summary: InjuriousAffectionSummary results
        output_path: Path to output JSON file
    """
    # Convert to dictionary
    results_dict = asdict(summary)

    with open(output_path, 'w') as f:
        json.dump(results_dict, f, indent=2)


# ============================================================================
# COMMAND-LINE INTERFACE
# ============================================================================

def main():
    """Command-line interface for injurious affection calculator"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Injurious Affection Calculator v2.0.0 - Construction Impact Assessment'
    )
    parser.add_argument(
        'input_json',
        help='Path to input JSON file with property and construction data'
    )
    parser.add_argument(
        '--output',
        help='Path to output JSON file (default: auto-generated)',
        default=None
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Print detailed results to console'
    )

    args = parser.parse_args()

    # Load inputs
    print(f"Loading parameters from {args.input_json}...")
    property_details, construction, params, visual_impact_data, property_address = load_from_json(args.input_json)
    print(f"  ✓ Loaded property: {property_details.property_type}")
    print(f"  ✓ Construction duration: {construction.duration_months} months")

    # Calculate damages
    print("\nCalculating injurious affection damages...")
    summary = calculate_injurious_affection(
        property_details,
        construction,
        params,
        property_address,
        visual_impact_data
    )

    # Generate output filename if not provided
    if args.output is None:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        args.output = f'injurious_affection_results_{timestamp}.json'

    # Save results
    print(f"\nSaving results to {args.output}...")
    save_to_json(summary, args.output)
    print("  ✓ Results saved")

    # Print summary
    print("\n" + "=" * 80)
    print("INJURIOUS AFFECTION DAMAGE ASSESSMENT")
    print("=" * 80)
    print(f"Property: {summary.property_address}")
    print(f"Property Type: {summary.property_type}")
    print(f"Property Value: ${summary.property_value:,.2f}")
    print(f"Assessment Date: {summary.assessment_date}")
    print()

    print("TEMPORARY DAMAGES (Construction Period):")
    print("-" * 80)
    print(f"1. Noise Impact:")
    print(f"   Noise Level: {summary.noise_impact.noise_level_at_property_dba:.1f} dBA")
    print(f"   Severity: {summary.noise_impact.impact_severity}")
    print(f"   Rent Reduction: {summary.noise_impact.rent_reduction_pct * 100:.1f}%")
    print(f"   Total Damage: ${summary.noise_impact.total_noise_damage:,.2f}")
    print()

    print(f"2. Dust Impact:")
    print(f"   Impact Zone: {summary.dust_impact.impact_zone}")
    print(f"   Cleanings Required: {summary.dust_impact.number_of_cleanings}")
    print(f"   Cost per Cleaning: ${summary.dust_impact.cleaning_cost_per_event:,.2f}")
    if summary.dust_impact.health_impact_cost > 0:
        print(f"   Health Impact Cost: ${summary.dust_impact.health_impact_cost:,.2f}")
    print(f"   Total Damage: ${summary.dust_impact.total_dust_damage:,.2f}")
    print()

    print(f"3. Vibration Impact:")
    print(f"   Peak Particle Velocity: {summary.vibration_impact.peak_particle_velocity_mms:.1f} mm/s")
    print(f"   Damage Threshold: {summary.vibration_impact.damage_threshold}")
    if summary.vibration_impact.total_vibration_damage > 0:
        print(f"   Repair Cost: ${summary.vibration_impact.repair_cost_estimate:,.2f}")
    print(f"   Total Damage: ${summary.vibration_impact.total_vibration_damage:,.2f}")
    print()

    print(f"4. Traffic Disruption:")
    if summary.traffic_impact.total_traffic_damage > 0:
        print(f"   Traffic Reduction: {summary.traffic_impact.traffic_reduction_pct * 100:.1f}%")
        print(f"   Lost Sales (Daily): ${summary.traffic_impact.lost_sales_daily:,.2f}")
        print(f"   Lost Profit (Daily): ${summary.traffic_impact.lost_profit_daily:,.2f}")
    print(f"   Total Damage: ${summary.traffic_impact.total_traffic_damage:,.2f}")
    print()

    print(f"5. Business Losses:")
    if summary.business_loss.total_business_loss > 0:
        print(f"   Revenue Reduction: {summary.business_loss.revenue_reduction_pct * 100:.1f}%")
        print(f"   Lost Profit (Monthly): ${summary.business_loss.lost_profit_monthly:,.2f}")
        if summary.business_loss.mitigation_efforts:
            print(f"   Mitigation Efforts: {', '.join(summary.business_loss.mitigation_efforts)}")
    print(f"   Total Damage: ${summary.business_loss.total_business_loss:,.2f}")
    print()

    if summary.visual_impact:
        print("PERMANENT DAMAGES:")
        print("-" * 80)
        print(f"Visual Impact: {summary.visual_impact.visual_impact_description}")
        print(f"Value Reduction: {summary.visual_impact.property_value_reduction_pct * 100:.1f}%")
        print(f"Capitalized Impact: ${summary.visual_impact.capitalized_impact:,.2f}")
        print()

    print("TOTAL DAMAGES:")
    print("-" * 80)
    print(f"Temporary Damages: ${summary.total_temporary_damages:,.2f}")
    print(f"Permanent Damages: ${summary.total_permanent_damages:,.2f}")
    print(f"TOTAL INJURIOUS AFFECTION: ${summary.total_injurious_affection:,.2f}")
    print()

    if args.verbose:
        print("DAMAGE BREAKDOWN BY CATEGORY:")
        print("-" * 80)
        for category, amount in summary.damages_by_category.items():
            pct_of_total = (amount / summary.total_injurious_affection * 100) if summary.total_injurious_affection > 0 else 0
            print(f"{category:20s}: ${amount:12,.2f}  ({pct_of_total:5.1f}%)")
        print()

        if summary.noise_impact.equipment_breakdown:
            print("NOISE EQUIPMENT BREAKDOWN:")
            print("-" * 80)
            for equip in summary.noise_impact.equipment_breakdown:
                print(f"{equip['equipment_type']:20s}: {equip['dba_at_15m']:5.1f} dBA @ 15m → "
                      f"{equip['dba_at_property']:5.1f} dBA @ property "
                      f"({equip['hours_per_day']:.1f} hrs/day)")

    print("=" * 80)
    print(f"\n✓ Assessment complete. Results saved to {args.output}")


if __name__ == '__main__':
    main()
