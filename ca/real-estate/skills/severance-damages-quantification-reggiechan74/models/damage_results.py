"""
Damage result models for severance damages calculator

These dataclasses store calculated damages across four categories:
1. Access Impairment
2. Shape Irregularity
3. Utility Impairment
4. Farm Operation Disruption
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List

from .property_data import PropertyBefore, Taking, Remainder
from .market_parameters import MarketParameters


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
