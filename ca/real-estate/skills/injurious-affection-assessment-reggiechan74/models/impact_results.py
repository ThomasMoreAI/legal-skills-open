"""
Result data structures for injurious affection impact assessments
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class NoiseImpactResult:
    """
    Results from noise impact assessment
    """
    noise_level_at_property_dba: float
    impact_severity: str  # "none", "moderate", "severe"
    rent_reduction_pct: float
    duration_months: float
    monthly_rental_loss: float
    total_noise_damage: float
    equipment_breakdown: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class DustImpactResult:
    """
    Results from dust impact assessment
    """
    impact_zone: str  # "high", "moderate", "low"
    cleaning_frequency_weeks: int
    cleaning_cost_per_event: float
    number_of_cleanings: int
    total_dust_damage: float
    health_impact_cost: float = 0.0  # Additional health-related costs


@dataclass
class VibrationImpactResult:
    """
    Results from vibration damage assessment
    """
    peak_particle_velocity_mms: float
    damage_threshold: str  # "none", "cosmetic", "structural"
    repair_cost_estimate: float
    total_vibration_damage: float


@dataclass
class TrafficImpactResult:
    """
    Results from traffic disruption assessment
    """
    traffic_reduction_pct: float
    baseline_traffic_daily: float
    lost_traffic_daily: float
    lost_sales_daily: float
    lost_profit_daily: float
    duration_months: float
    total_traffic_damage: float


@dataclass
class BusinessLossResult:
    """
    Results from business loss assessment
    """
    baseline_revenue_monthly: float
    revenue_reduction_pct: float
    lost_revenue_monthly: float
    lost_profit_monthly: float
    duration_months: float
    total_business_loss: float
    mitigation_efforts: List[str] = field(default_factory=list)


@dataclass
class VisualImpactResult:
    """
    Results from permanent visual impact assessment
    """
    visual_impact_description: str
    property_value_reduction_pct: float
    permanent_value_loss: float
    capitalized_impact: float


@dataclass
class InjuriousAffectionSummary:
    """
    Complete summary of all injurious affection damages
    """
    # Input details
    property_address: str
    property_type: str
    property_value: float
    assessment_date: str

    # Impact results
    noise_impact: NoiseImpactResult
    dust_impact: DustImpactResult
    vibration_impact: VibrationImpactResult
    traffic_impact: TrafficImpactResult
    business_loss: BusinessLossResult
    visual_impact: Optional[VisualImpactResult] = None

    # Total damages
    total_temporary_damages: float = 0.0
    total_permanent_damages: float = 0.0
    total_injurious_affection: float = 0.0

    # Breakdown by category
    damages_by_category: Dict[str, float] = field(default_factory=dict)

    def calculate_totals(self):
        """Calculate total damages across all categories"""
        # Temporary damages (construction period)
        self.total_temporary_damages = (
            self.noise_impact.total_noise_damage +
            self.dust_impact.total_dust_damage +
            self.vibration_impact.total_vibration_damage +
            self.traffic_impact.total_traffic_damage +
            self.business_loss.total_business_loss
        )

        # Permanent damages
        self.total_permanent_damages = 0.0
        if self.visual_impact:
            self.total_permanent_damages = self.visual_impact.capitalized_impact

        # Total injurious affection
        self.total_injurious_affection = (
            self.total_temporary_damages +
            self.total_permanent_damages
        )

        # Category breakdown
        self.damages_by_category = {
            'noise': self.noise_impact.total_noise_damage,
            'dust': self.dust_impact.total_dust_damage,
            'vibration': self.vibration_impact.total_vibration_damage,
            'traffic': self.traffic_impact.total_traffic_damage,
            'business_loss': self.business_loss.total_business_loss,
            'visual_permanent': self.total_permanent_damages
        }
