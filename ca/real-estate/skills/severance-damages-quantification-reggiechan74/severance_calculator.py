#!/usr/bin/env python3
"""
Severance Damages Calculator - Quantifies Loss of Value to Remainder Parcels (REFACTORED)

Calculates severance damages from partial property takings across four categories:
1. Access Impairment (frontage loss, circuitous access, landlocked parcels)
2. Shape Irregularity (geometric efficiency, buildable area reduction)
3. Utility Impairment (highest and best use loss, development potential reduction)
4. Farm Operation Disruption (field division, equipment access, irrigation impacts)

Author: Claude Code
Version: 2.0.0 (Refactored - Modular Architecture)
Date: 2025-11-15
"""

import json
import sys
import logging
from pathlib import Path

# Fix imports for both script execution and module imports
import os
_current_dir = os.path.dirname(os.path.abspath(__file__))
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

# Import data models
from models import (
    PropertyBefore,
    Taking,
    Remainder,
    MarketParameters,
    SeveranceDamagesSummary
)

# Import damage calculation modules
from damages import (
    calculate_access_damages,
    calculate_shape_damages,
    calculate_utility_damages,
    calculate_farm_damages
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

logger = logging.getLogger(__name__)


# ============================================================================
# MAIN CALCULATION FUNCTION (MODULAR VERSION)
# ============================================================================

def calculate_severance_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> SeveranceDamagesSummary:
    """
    Calculate complete severance damages analysis using modular calculation functions

    This orchestrator function delegates to specialized modules for each damage category:
    - damages.access: Access impairment calculations
    - damages.shape: Shape irregularity calculations
    - damages.utility: Utility impairment calculations
    - damages.farm: Farm operation disruption calculations

    Args:
        property_before: Property characteristics before taking
        taking: Details of the partial taking
        remainder: Remainder parcel characteristics
        market_params: Market parameters and assumptions

    Returns:
        SeveranceDamagesSummary: Complete severance damages with all categories calculated
    """
    logger.info("\n" + "=" * 80)
    logger.info("SEVERANCE DAMAGES CALCULATION")
    logger.info(f"Property: {property_before.total_acres:.1f} acres, {property_before.use} use")
    logger.info(f"Taking: {taking.area_taken_acres:.1f} acres")
    logger.info(f"Remainder: {remainder.acres:.1f} acres")
    logger.info("=" * 80 + "\n")

    # Calculate each damage category using modular functions
    access_damages = calculate_access_damages(
        property_before, taking, remainder, market_params
    )

    shape_damages = calculate_shape_damages(
        property_before, taking, remainder, market_params
    )

    utility_damages = calculate_utility_damages(
        property_before, taking, remainder, market_params
    )

    farm_damages = calculate_farm_damages(
        property_before, taking, remainder, market_params
    )

    # Create summary
    summary = SeveranceDamagesSummary(
        property_before=property_before,
        taking=taking,
        remainder=remainder,
        market_parameters=market_params,
        access_damages=access_damages,
        shape_damages=shape_damages,
        utility_damages=utility_damages,
        farm_damages=farm_damages
    )

    # Calculate totals and reconciliation
    summary.calculate_totals()

    # Add analysis notes
    summary.analysis_notes.append(
        f"Property: {property_before.total_acres:.1f} acres, {property_before.use} use"
    )
    summary.analysis_notes.append(
        f"Taking: {taking.area_taken_acres:.1f} acres "
        f"({taking.area_taken_acres/property_before.total_acres*100:.1f}%)"
    )
    summary.analysis_notes.append(
        f"Remainder: {remainder.acres:.1f} acres with {remainder.access_type} access"
    )
    summary.analysis_notes.append(
        f"Total severance damages: ${summary.total_severance_damages:,.2f}"
    )

    logger.info("\n" + "=" * 80)
    logger.info("CALCULATION COMPLETE")
    logger.info(f"Total Severance Damages: ${summary.total_severance_damages:,.2f}")
    logger.info("=" * 80 + "\n")

    return summary


# ============================================================================
# JSON INPUT/OUTPUT
# ============================================================================

def load_from_json(json_path: str) -> tuple:
    """Load severance calculation from JSON file"""
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Parse property before
    prop_data = data["property_before"]
    property_before = PropertyBefore(
        total_acres=float(prop_data["total_acres"]),
        frontage_linear_feet=float(prop_data["frontage_linear_feet"]),
        road_classification=prop_data["road_classification"],
        shape_ratio_frontage_depth=float(prop_data["shape_ratio_frontage_depth"]),
        value_per_acre=float(prop_data["value_per_acre"]),
        use=prop_data["use"],
        development_potential_units=prop_data.get("development_potential_units"),
        buildable_area_sf=prop_data.get("buildable_area_sf")
    )

    # Parse taking
    take_data = data["taking"]
    taking = Taking(
        area_taken_acres=float(take_data["area_taken_acres"]),
        frontage_lost_linear_feet=float(take_data["frontage_lost_linear_feet"]),
        creates_landlocked=take_data["creates_landlocked"],
        eliminates_direct_access=take_data.get("eliminates_direct_access", False),
        circuitous_access_added_minutes=float(take_data.get("circuitous_access_added_minutes", 0.0)),
        creates_irregular_shape=take_data.get("creates_irregular_shape", False),
        severs_utilities=take_data.get("severs_utilities", False),
        reduces_development_potential=take_data.get("reduces_development_potential", False),
        bisects_farm=take_data.get("bisects_farm", False),
        disrupts_irrigation=take_data.get("disrupts_irrigation", False)
    )

    # Parse remainder
    rem_data = data["remainder"]
    remainder = Remainder(
        acres=float(rem_data["acres"]),
        frontage_remaining_linear_feet=float(rem_data["frontage_remaining_linear_feet"]),
        shape_ratio_frontage_depth=float(rem_data["shape_ratio_frontage_depth"]),
        access_type=rem_data["access_type"],
        buildable_area_sf=rem_data.get("buildable_area_sf"),
        development_potential_units=rem_data.get("development_potential_units"),
        requires_new_fencing_linear_meters=float(rem_data.get("requires_new_fencing_linear_meters", 0.0)),
        irrigation_acres_affected=float(rem_data.get("irrigation_acres_affected", 0.0))
    )

    # Parse market parameters
    mkt_data = data.get("market_parameters", {})
    market_params = MarketParameters(
        cap_rate=float(mkt_data.get("cap_rate", 0.07)),
        travel_time_value_per_hour=float(mkt_data.get("travel_time_value_per_hour", 40.0)),
        trips_per_day=int(mkt_data.get("trips_per_day", 20)),
        business_days_per_year=int(mkt_data.get("business_days_per_year", 250))
    )

    return property_before, taking, remainder, market_params


def save_to_json(summary: SeveranceDamagesSummary, output_path: str):
    """Save calculation results to JSON file"""

    output = {
        "analysis_date": summary.analysis_date.isoformat(),
        "property_before": {
            "total_acres": summary.property_before.total_acres,
            "frontage_linear_feet": summary.property_before.frontage_linear_feet,
            "road_classification": summary.property_before.road_classification,
            "use": summary.property_before.use,
            "value_per_acre": summary.property_before.value_per_acre,
            "total_value": summary.before_value_total
        },
        "taking": {
            "area_taken_acres": summary.taking.area_taken_acres,
            "frontage_lost_linear_feet": summary.taking.frontage_lost_linear_feet,
            "value_of_land_taken": summary.before_value_taken
        },
        "remainder": {
            "acres": summary.remainder.acres,
            "frontage_remaining_linear_feet": summary.remainder.frontage_remaining_linear_feet,
            "access_type": summary.remainder.access_type,
            "proportionate_value": summary.before_value_remainder_proportionate,
            "actual_value_after_severance": summary.after_value_remainder
        },
        "severance_damages": {
            "access_impairment": {
                "frontage_loss_value": summary.access_damages.frontage_loss_value,
                "frontage_rate_per_lf": summary.access_damages.frontage_rate_used,
                "circuitous_access_cost": summary.access_damages.circuitous_access_cost,
                "annual_time_cost": summary.access_damages.annual_time_cost,
                "landlocked_remedy_cost": summary.access_damages.landlocked_remedy_cost,
                "total": summary.access_damages.total_access_damages
            },
            "shape_irregularity": {
                "efficiency_index_before": summary.shape_damages.efficiency_index_before,
                "efficiency_index_after": summary.shape_damages.efficiency_index_after,
                "efficiency_category": summary.shape_damages.efficiency_category,
                "value_discount_pct": summary.shape_damages.value_discount_pct,
                "geometric_inefficiency_value": summary.shape_damages.geometric_inefficiency_value,
                "buildable_area_reduction": summary.shape_damages.buildable_area_reduction_value,
                "development_yield_loss": summary.shape_damages.development_yield_loss,
                "total": summary.shape_damages.total_shape_damages
            },
            "utility_impairment": {
                "site_servicing_costs": summary.utility_damages.site_servicing_costs,
                "development_potential_reduction": summary.utility_damages.development_potential_reduction,
                "total": summary.utility_damages.total_utility_damages
            },
            "farm_operation_disruption": {
                "fencing_cost": summary.farm_damages.fencing_cost,
                "drainage_modifications": summary.farm_damages.drainage_modifications,
                "field_division_costs": summary.farm_damages.field_division_costs,
                "equipment_access_complications": summary.farm_damages.equipment_access_complications,
                "irrigation_system_impacts": summary.farm_damages.irrigation_system_impacts,
                "total": summary.farm_damages.total_farm_damages
            },
            "total_severance_damages": summary.total_severance_damages
        },
        "reconciliation": {
            "before_total_value": summary.before_value_total,
            "land_taken_value": summary.before_value_taken,
            "remainder_proportionate_value": summary.before_value_remainder_proportionate,
            "severance_damages": summary.total_severance_damages,
            "remainder_value_after_severance": summary.after_value_remainder,
            "total_compensation": summary.before_value_taken + summary.total_severance_damages
        },
        "analysis_notes": summary.analysis_notes
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)


# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

def main():
    """Command-line interface for severance damages calculator"""
    if len(sys.argv) < 2:
        print("Usage: python severance_calculator.py <input.json> [output.json]")
        print("\nExample:")
        print("  python severance_calculator.py sample_highway_frontage_loss.json")
        print("  python severance_calculator.py input.json results.json")
        sys.exit(1)

    input_path = sys.argv[1]

    # Generate output path
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        output_path = str(Path(input_path).with_suffix('')) + "_results.json"

    print(f"Loading severance scenario from: {input_path}")
    property_before, taking, remainder, market_params = load_from_json(input_path)

    print(f"Calculating severance damages...")
    summary = calculate_severance_damages(
        property_before, taking, remainder, market_params
    )

    print(f"Saving results to: {output_path}")
    save_to_json(summary, output_path)

    print(f"\n{'='*80}")
    print("SEVERANCE DAMAGES CALCULATION COMPLETE")
    print(f"{'='*80}\n")

    print(f"Property: {property_before.total_acres:.1f} acres, {property_before.use} use")
    print(f"Value before: ${summary.before_value_total:,.2f} (${property_before.value_per_acre:,.0f}/acre)")
    print(f"\nTaking: {taking.area_taken_acres:.1f} acres")
    print(f"Land taken value: ${summary.before_value_taken:,.2f}")
    print(f"\nRemainder: {remainder.acres:.1f} acres")
    print(f"Proportionate value: ${summary.before_value_remainder_proportionate:,.2f}")

    print(f"\n{'-'*80}")
    print("SEVERANCE DAMAGES BY CATEGORY")
    print(f"{'-'*80}")
    print(f"Access Impairment:           ${summary.access_damages.total_access_damages:>15,.2f}")
    if summary.access_damages.frontage_loss_value > 0:
        print(f"  - Frontage loss:           ${summary.access_damages.frontage_loss_value:>15,.2f}")
    if summary.access_damages.circuitous_access_cost > 0:
        print(f"  - Circuitous access:       ${summary.access_damages.circuitous_access_cost:>15,.2f}")
    if summary.access_damages.landlocked_remedy_cost > 0:
        print(f"  - Landlocked remedy:       ${summary.access_damages.landlocked_remedy_cost:>15,.2f}")

    print(f"\nShape Irregularity:          ${summary.shape_damages.total_shape_damages:>15,.2f}")
    if summary.shape_damages.geometric_inefficiency_value > 0:
        print(f"  - Geometric inefficiency:  ${summary.shape_damages.geometric_inefficiency_value:>15,.2f}")
        print(f"    (Efficiency: {summary.shape_damages.efficiency_index_after:.2f}, Category: {summary.shape_damages.efficiency_category})")
    if summary.shape_damages.buildable_area_reduction_value > 0:
        print(f"  - Buildable area loss:     ${summary.shape_damages.buildable_area_reduction_value:>15,.2f}")
    if summary.shape_damages.development_yield_loss > 0:
        print(f"  - Development yield loss:  ${summary.shape_damages.development_yield_loss:>15,.2f}")

    print(f"\nUtility Impairment:          ${summary.utility_damages.total_utility_damages:>15,.2f}")
    if summary.utility_damages.site_servicing_costs > 0:
        print(f"  - Site servicing costs:    ${summary.utility_damages.site_servicing_costs:>15,.2f}")

    if summary.farm_damages.total_farm_damages > 0:
        print(f"\nFarm Operation Disruption:   ${summary.farm_damages.total_farm_damages:>15,.2f}")
        if summary.farm_damages.field_division_costs > 0:
            print(f"  - Field division costs:    ${summary.farm_damages.field_division_costs:>15,.2f}")
        if summary.farm_damages.equipment_access_complications > 0:
            print(f"  - Equipment access:        ${summary.farm_damages.equipment_access_complications:>15,.2f}")
        if summary.farm_damages.irrigation_system_impacts > 0:
            print(f"  - Irrigation impacts:      ${summary.farm_damages.irrigation_system_impacts:>15,.2f}")

    print(f"\n{'-'*80}")
    print(f"TOTAL SEVERANCE DAMAGES:     ${summary.total_severance_damages:>15,.2f}")
    print(f"{'-'*80}")

    print(f"\nRemainder value after severance: ${summary.after_value_remainder:,.2f}")
    print(f"Total compensation (land + severance): ${summary.before_value_taken + summary.total_severance_damages:,.2f}")

    print(f"\n{'-'*80}\n")


if __name__ == '__main__':
    main()
