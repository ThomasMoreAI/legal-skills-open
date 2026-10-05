"""
Property data models for severance damages calculator

These dataclasses represent the before/after property characteristics
for partial taking severance damage calculations.
"""

from dataclasses import dataclass
from typing import Optional


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
