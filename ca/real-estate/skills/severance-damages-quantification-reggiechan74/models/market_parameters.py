"""
Market parameters model for severance damages calculator

This dataclass stores market assumptions used in various calculations,
including capitalization rates, frontage values, and shape efficiency discounts.
"""

from dataclasses import dataclass, field
from typing import Dict


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
