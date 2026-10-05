#!/usr/bin/env python3
"""
Severance Damages Calculator - Quantifies Loss of Value to Remainder Parcels

Calculates severance damages from partial property takings across four categories:
1. Access Impairment (frontage loss, circuitous access, landlocked parcels)
2. Shape Irregularity (geometric efficiency, buildable area reduction)
3. Utility Impairment (highest and best use loss, development potential reduction)
4. Farm Operation Disruption (field division, equipment access, irrigation impacts)

Author: Claude Code
Version: 1.0.0
Date: 2025-11-15
"""

import json
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path
from datetime import date
import math


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class PropertyBefore:
    """Property characteristics before the taking"""
    total_acres: float
    frontage_linear_feet: float
    road_classification: str  # "highway", "arterial", "collector", "local"
    shape_ratio_frontage_depth: float  # Frontage:Depth ratio (e.g., 1:4 = 0.25)
    value_per_acre: float
    use: str  # "industrial", "commercial", "residential", "agricultural"

    # Optional development details
    development_potential_units: Optional[int] = None
    buildable_area_sf: Optional[int] = None

    def total_value(self) -> float:
        """Calculate total property value before taking"""
        return self.total_acres * self.value_per_acre


@dataclass
class Taking:
    """Details of the partial taking"""
    area_taken_acres: float
    frontage_lost_linear_feet: float
    creates_landlocked: bool

    # Access impacts
    eliminates_direct_access: bool = False
    circuitous_access_added_minutes: float = 0.0

    # Shape impacts
    creates_irregular_shape: bool = False

    # Utility impacts
    severs_utilities: bool = False
    reduces_development_potential: bool = False

    # Farm operation impacts (if agricultural)
    bisects_farm: bool = False
    disrupts_irrigation: bool = False


@dataclass
class Remainder:
    """Remainder parcel characteristics after taking"""
    acres: float
    frontage_remaining_linear_feet: float
    shape_ratio_frontage_depth: float
    access_type: str  # "direct", "circuitous", "landlocked"

    # Development potential after taking
    buildable_area_sf: Optional[int] = None
    development_potential_units: Optional[int] = None

    # Farm operation details (if agricultural)
    requires_new_fencing_linear_meters: float = 0.0
    irrigation_acres_affected: float = 0.0


@dataclass
class MarketParameters:
    """Market assumptions for calculations"""
    cap_rate: float  # Capitalization rate for income losses
    travel_time_value_per_hour: float = 40.0  # $/hour for time-distance modeling
    trips_per_day: int = 20  # For industrial/commercial properties
    business_days_per_year: int = 250

    # Frontage value by road classification ($/linear foot)
    frontage_values: Dict[str, Dict[str, tuple]] = field(default_factory=lambda: {
        "highway": {
            "commercial": (500, 1500),
            "industrial": (300, 800),
            "residential": (150, 400),
            "agricultural": (50, 150)
        },
        "arterial": {
            "commercial": (300, 800),
            "industrial": (200, 500),
            "residential": (100, 250),
            "agricultural": (30, 100)
        },
        "collector": {
            "commercial": (150, 400),
            "industrial": (100, 300),
            "residential": (50, 150),
            "agricultural": (20, 60)
        },
        "local": {
            "residential": (25, 75),
            "agricultural": (10, 30),
            "commercial": (50, 150),
            "industrial": (40, 120)
        }
    })

    # Shape inefficiency value impacts
    shape_efficiency_discounts: Dict[str, float] = field(default_factory=lambda: {
        "high": 0.02,        # 0.8-1.0 efficiency index
        "moderate": 0.08,    # 0.6-0.8 efficiency index
        "low": 0.15,         # 0.4-0.6 efficiency index
        "very_low": 0.30     # <0.4 efficiency index
    })


@dataclass
class AccessDamages:
    """Calculated access impairment damages"""
    frontage_loss_value: float = 0.0
    circuitous_access_cost: float = 0.0
    landlocked_remedy_cost: float = 0.0

    total_access_damages: float = 0.0

    # Calculation details
    frontage_rate_used: float = 0.0
    annual_time_cost: float = 0.0
    capitalized_time_cost: float = 0.0

    def calculate_total(self) -> float:
        """Calculate total access damages"""
        self.total_access_damages = (
            self.frontage_loss_value +
            self.circuitous_access_cost +
            self.landlocked_remedy_cost
        )
        return self.total_access_damages


@dataclass
class ShapeDamages:
    """Calculated shape irregularity damages"""
    geometric_inefficiency_value: float = 0.0
    buildable_area_reduction_value: float = 0.0
    development_yield_loss: float = 0.0

    total_shape_damages: float = 0.0

    # Calculation details
    efficiency_index_before: float = 1.0
    efficiency_index_after: float = 1.0
    efficiency_category: str = "high"
    value_discount_pct: float = 0.0

    def calculate_total(self) -> float:
        """Calculate total shape damages"""
        self.total_shape_damages = (
            self.geometric_inefficiency_value +
            self.buildable_area_reduction_value +
            self.development_yield_loss
        )
        return self.total_shape_damages


@dataclass
class UtilityDamages:
    """Calculated utility impairment damages"""
    highest_best_use_loss: float = 0.0
    development_potential_reduction: float = 0.0
    site_servicing_costs: float = 0.0

    total_utility_damages: float = 0.0

    # Calculation details
    hbu_before: str = ""
    hbu_after: str = ""
    units_before: int = 0
    units_after: int = 0

    def calculate_total(self) -> float:
        """Calculate total utility damages"""
        self.total_utility_damages = (
            self.highest_best_use_loss +
            self.development_potential_reduction +
            self.site_servicing_costs
        )
        return self.total_utility_damages


@dataclass
class FarmDamages:
    """Calculated farm operation disruption damages"""
    field_division_costs: float = 0.0
    equipment_access_complications: float = 0.0
    irrigation_system_impacts: float = 0.0

    total_farm_damages: float = 0.0

    # Calculation details
    fencing_cost: float = 0.0
    drainage_modifications: float = 0.0
    annual_equipment_time_cost: float = 0.0
    irrigation_repair_cost: float = 0.0

    def calculate_total(self) -> float:
        """Calculate total farm damages"""
        self.total_farm_damages = (
            self.field_division_costs +
            self.equipment_access_complications +
            self.irrigation_system_impacts
        )
        return self.total_farm_damages


@dataclass
class SeveranceDamagesSummary:
    """Complete severance damages calculation results"""
    property_before: PropertyBefore
    taking: Taking
    remainder: Remainder
    market_parameters: MarketParameters

    access_damages: AccessDamages
    shape_damages: ShapeDamages
    utility_damages: UtilityDamages
    farm_damages: FarmDamages

    total_severance_damages: float = 0.0

    # Before/after market values
    before_value_total: float = 0.0
    before_value_taken: float = 0.0
    before_value_remainder_proportionate: float = 0.0
    after_value_remainder: float = 0.0

    analysis_date: date = field(default_factory=date.today)
    analysis_notes: List[str] = field(default_factory=list)

    def calculate_totals(self):
        """Calculate all totals and reconciliation"""
        self.access_damages.calculate_total()
        self.shape_damages.calculate_total()
        self.utility_damages.calculate_total()
        self.farm_damages.calculate_total()

        self.total_severance_damages = (
            self.access_damages.total_access_damages +
            self.shape_damages.total_shape_damages +
            self.utility_damages.total_utility_damages +
            self.farm_damages.total_farm_damages
        )

        # Calculate before/after values
        self.before_value_total = self.property_before.total_value()
        self.before_value_taken = (
            self.taking.area_taken_acres * self.property_before.value_per_acre
        )
        self.before_value_remainder_proportionate = (
            self.remainder.acres * self.property_before.value_per_acre
        )
        self.after_value_remainder = (
            self.before_value_remainder_proportionate - self.total_severance_damages
        )

        return self


# ============================================================================
# ACCESS IMPAIRMENT CALCULATIONS
# ============================================================================

def calculate_frontage_loss_value(
    frontage_lost_lf: float,
    road_classification: str,
    property_use: str,
    market_params: MarketParameters
) -> tuple[float, float]:
    """
    Calculate value loss from loss of road frontage

    Returns:
        tuple: (frontage_loss_value, rate_used_per_lf)
    """
    if frontage_lost_lf <= 0:
        return 0.0, 0.0

    # Get frontage value range for this road class and use
    try:
        value_range = market_params.frontage_values[road_classification][property_use]
        # Use midpoint of range
        rate_per_lf = (value_range[0] + value_range[1]) / 2
    except KeyError:
        # Default to low end if combination not found
        rate_per_lf = 50.0

    frontage_value = frontage_lost_lf * rate_per_lf

    return frontage_value, rate_per_lf


def calculate_circuitous_access_cost(
    added_travel_minutes: float,
    trips_per_day: int,
    business_days_per_year: int,
    travel_time_value_per_hour: float,
    cap_rate: float
) -> tuple[float, float]:
    """
    Calculate capitalized cost of circuitous access using time-distance modeling

    Returns:
        tuple: (capitalized_cost, annual_time_cost)
    """
    if added_travel_minutes <= 0:
        return 0.0, 0.0

    # Annual time cost
    hours_per_trip = added_travel_minutes / 60.0
    annual_trips = trips_per_day * business_days_per_year
    annual_time_cost = annual_trips * hours_per_trip * travel_time_value_per_hour

    # Capitalize to present value
    if cap_rate <= 0:
        capitalized_cost = annual_time_cost * 10  # Default 10x multiple
    else:
        capitalized_cost = annual_time_cost / cap_rate

    return capitalized_cost, annual_time_cost


def calculate_landlocked_remedy_cost(
    remainder_acres: float,
    value_per_acre: float,
    easement_width_meters: float = 20.0,
    easement_length_meters: float = 200.0
) -> float:
    """
    Calculate cost to cure landlocked parcel (easement acquisition)

    Uses cost-to-cure methodology (easement + legal costs)
    Alternative: 50-80% value loss if no easement obtainable
    """
    # Easement value: 12% of fee simple value for affected land
    easement_acres = (easement_width_meters * easement_length_meters) / 4046.86  # sq m to acres
    easement_value = easement_acres * value_per_acre * 0.12

    # Transaction costs
    legal_costs = 25000.0
    survey_costs = 8000.0

    total_remedy_cost = easement_value + legal_costs + survey_costs

    return total_remedy_cost


def calculate_access_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> AccessDamages:
    """Calculate all access impairment damages"""
    damages = AccessDamages()

    # 1. Frontage loss value ($/linear foot method)
    if taking.frontage_lost_linear_feet > 0:
        damages.frontage_loss_value, damages.frontage_rate_used = (
            calculate_frontage_loss_value(
                frontage_lost_lf=taking.frontage_lost_linear_feet,
                road_classification=property_before.road_classification,
                property_use=property_before.use,
                market_params=market_params
            )
        )

    # 2. Circuitous access cost (time-distance modeling)
    if taking.eliminates_direct_access and taking.circuitous_access_added_minutes > 0:
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

    # 3. Landlocked parcel remedy cost
    if taking.creates_landlocked or remainder.access_type == "landlocked":
        damages.landlocked_remedy_cost = calculate_landlocked_remedy_cost(
            remainder_acres=remainder.acres,
            value_per_acre=property_before.value_per_acre
        )

    damages.calculate_total()
    return damages


# ============================================================================
# SHAPE IRREGULARITY CALCULATIONS
# ============================================================================

def calculate_shape_efficiency_index(
    acres: float,
    frontage_lf: float,
    depth_lf: float = None,
    frontage_depth_ratio: float = None
) -> float:
    """
    Calculate shape efficiency index (1.0 = perfect square)

    Uses area-to-perimeter ratio compared to ideal square
    """
    # Handle landlocked parcels (no frontage)
    if frontage_lf == 0 or (frontage_depth_ratio is not None and frontage_depth_ratio == 0):
        # Cannot calculate efficiency for landlocked parcel
        # Return very low efficiency index
        return 0.2

    if frontage_depth_ratio is not None:
        # Calculate depth from ratio (frontage:depth, e.g., 1:4 = 0.25)
        depth_lf = frontage_lf / frontage_depth_ratio
    elif depth_lf is None:
        # Assume square if not specified
        area_sf = acres * 43560
        depth_lf = area_sf / frontage_lf

    # Calculate actual perimeter
    actual_perimeter = 2 * (frontage_lf + depth_lf)

    # Calculate ideal square perimeter for same area
    area_sf = acres * 43560
    side_length = math.sqrt(area_sf)
    ideal_perimeter = 4 * side_length

    # Efficiency index = (actual A/P) / (ideal A/P)
    actual_ratio = area_sf / actual_perimeter
    ideal_ratio = area_sf / ideal_perimeter

    efficiency_index = actual_ratio / ideal_ratio

    return efficiency_index


def categorize_shape_efficiency(efficiency_index: float) -> str:
    """Categorize shape efficiency into standard ranges"""
    if efficiency_index >= 0.8:
        return "high"
    elif efficiency_index >= 0.6:
        return "moderate"
    elif efficiency_index >= 0.4:
        return "low"
    else:
        return "very_low"


def calculate_shape_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> ShapeDamages:
    """Calculate all shape irregularity damages"""
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

    # 2. Categorize and apply discount
    damages.efficiency_category = categorize_shape_efficiency(
        damages.efficiency_index_after
    )
    damages.value_discount_pct = market_params.shape_efficiency_discounts[
        damages.efficiency_category
    ]

    # 3. Calculate geometric inefficiency value loss
    if taking.creates_irregular_shape:
        remainder_base_value = remainder.acres * property_before.value_per_acre
        damages.geometric_inefficiency_value = (
            remainder_base_value * damages.value_discount_pct
        )

    # 4. Buildable area reduction (if development details provided)
    if (property_before.buildable_area_sf and
        remainder.buildable_area_sf and
        remainder.buildable_area_sf < property_before.buildable_area_sf):

        # Calculate proportionate buildable area expected
        proportionate_buildable = (
            property_before.buildable_area_sf *
            (remainder.acres / property_before.total_acres)
        )

        # Value loss from reduced buildable area
        buildable_reduction_sf = proportionate_buildable - remainder.buildable_area_sf

        # Assume $250/sf value for lost buildable area (commercial/industrial)
        value_per_buildable_sf = 250.0 if property_before.use in ["commercial", "industrial"] else 150.0

        damages.buildable_area_reduction_value = (
            buildable_reduction_sf * value_per_buildable_sf
        )

    # 5. Development yield loss (if unit counts provided)
    if (property_before.development_potential_units and
        remainder.development_potential_units):

        # Calculate proportionate units expected
        proportionate_units = int(
            property_before.development_potential_units *
            (remainder.acres / property_before.total_acres)
        )

        # Value loss from reduced unit yield
        unit_reduction = proportionate_units - remainder.development_potential_units

        if unit_reduction > 0:
            # Assume $150K per residential unit, $500K per industrial lot
            value_per_unit = 500000.0 if property_before.use == "industrial" else 150000.0

            damages.development_yield_loss = unit_reduction * value_per_unit

    damages.calculate_total()
    return damages


# ============================================================================
# UTILITY IMPAIRMENT CALCULATIONS
# ============================================================================

def calculate_utility_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> UtilityDamages:
    """Calculate utility impairment damages"""
    damages = UtilityDamages()

    # 1. Site servicing costs (if utilities severed)
    if taking.severs_utilities:
        # Typical utility relocation costs
        water_sewer_length_m = 400.0  # Assume 400m relocation
        water_cost = water_sewer_length_m * 500.0  # $500/m
        sewer_cost = water_sewer_length_m * 800.0  # $800/m
        drainage_cost = 195000.0  # Engineering + construction

        damages.site_servicing_costs = water_cost + sewer_cost + drainage_cost

    # 2. Development potential reduction (captured in shape damages typically)
    # Only calculate here if not already captured
    if taking.reduces_development_potential and not taking.creates_irregular_shape:
        # Apply modest discount for reduced development potential
        remainder_base_value = remainder.acres * property_before.value_per_acre
        damages.development_potential_reduction = remainder_base_value * 0.10  # 10%

    damages.calculate_total()
    return damages


# ============================================================================
# FARM OPERATION DISRUPTION CALCULATIONS
# ============================================================================

def calculate_farm_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> FarmDamages:
    """Calculate farm operation disruption damages (agricultural use only)"""
    damages = FarmDamages()

    if property_before.use != "agricultural":
        return damages

    # 1. Field division costs
    if taking.bisects_farm and remainder.requires_new_fencing_linear_meters > 0:
        # Fencing costs (page wire for livestock)
        fencing_rate = 20.0  # $/linear meter
        damages.fencing_cost = remainder.requires_new_fencing_linear_meters * fencing_rate

        # Drainage modifications (typical for bisected farm)
        drainage_engineering = 8000.0
        tile_installation_length_m = 1500.0
        tile_rate = 15.0  # $/m
        damages.drainage_modifications = drainage_engineering + (tile_installation_length_m * tile_rate)

        damages.field_division_costs = damages.fencing_cost + damages.drainage_modifications

    # 2. Equipment access complications
    if taking.bisects_farm and taking.circuitous_access_added_minutes > 0:
        # Equipment crossing time cost
        crossings_per_year = 30
        hours_per_crossing = (taking.circuitous_access_added_minutes * 2) / 60.0  # Round trip
        equipment_operator_cost = 150.0  # $/hour

        damages.annual_equipment_time_cost = (
            crossings_per_year * hours_per_crossing * equipment_operator_cost
        )

        # Capitalize
        if market_params.cap_rate > 0:
            damages.equipment_access_complications = (
                damages.annual_equipment_time_cost / market_params.cap_rate
            )
        else:
            damages.equipment_access_complications = damages.annual_equipment_time_cost * 10

    # 3. Irrigation system impacts
    if taking.disrupts_irrigation and remainder.irrigation_acres_affected > 0:
        # Cost to repair irrigation (pump station, distribution lines)
        damages.irrigation_repair_cost = 180000.0

        # Alternative: value loss approach
        irrigation_premium_per_acre = 2000.0
        value_loss = remainder.irrigation_acres_affected * irrigation_premium_per_acre

        # Use lower of cost-to-cure or value loss
        damages.irrigation_system_impacts = min(damages.irrigation_repair_cost, value_loss)

    damages.calculate_total()
    return damages


# ============================================================================
# MAIN CALCULATION FUNCTION
# ============================================================================

def calculate_severance_damages(
    property_before: PropertyBefore,
    taking: Taking,
    remainder: Remainder,
    market_params: MarketParameters
) -> SeveranceDamagesSummary:
    """
    Calculate complete severance damages analysis

    Returns:
        SeveranceDamagesSummary with all damage categories calculated
    """
    # Calculate each damage category
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
        f"Taking: {taking.area_taken_acres:.1f} acres ({taking.area_taken_acres/property_before.total_acres*100:.1f}%)"
    )
    summary.analysis_notes.append(
        f"Remainder: {remainder.acres:.1f} acres with {remainder.access_type} access"
    )
    summary.analysis_notes.append(
        f"Total severance damages: ${summary.total_severance_damages:,.2f}"
    )

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
