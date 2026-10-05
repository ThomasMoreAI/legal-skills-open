"""
Property and construction data models for injurious affection assessment
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Literal


@dataclass
class PropertyDetails:
    """
    Property characteristics for impact assessment
    """
    property_type: Literal['residential', 'commercial', 'industrial']
    property_value: float  # Market value ($)
    rental_income_monthly: float = 0.0  # Monthly rental income ($)
    distance_to_construction_m: float = 0.0  # Distance to construction (meters)
    number_of_units: int = 1  # For multi-unit residential
    business_type: Optional[str] = None  # e.g., "restaurant", "retail", "office"
    annual_revenue: float = 0.0  # For business loss calculations
    background_noise_dba: float = 50.0  # Ambient noise level (dBA)


@dataclass
class ConstructionActivity:
    """
    Construction activities causing impacts
    """
    duration_months: float  # Total construction duration
    equipment: List[Dict[str, Any]] = field(default_factory=list)  # Equipment list
    dust_impact_zone: Literal['high', 'moderate', 'low'] = 'moderate'
    vibration_ppv_mms: float = 0.0  # Peak particle velocity (mm/s)
    traffic_reduction_pct: float = 0.0  # % reduction in traffic/access
    construction_hours_per_day: int = 8  # Hours per day
    night_work: bool = False  # Construction during night hours


@dataclass
class NoiseEquipment:
    """
    Individual equipment noise characteristics
    """
    equipment_type: str  # e.g., "pile_driver", "jackhammer"
    dba_at_15m: float  # Sound level at 15 meters
    hours_per_day: float  # Operating hours per day
    days_per_week: int = 5  # Operating days per week
