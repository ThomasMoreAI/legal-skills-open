"""
Acoustic calculation utilities for noise impact assessment

Provides noise attenuation modeling based on distance and inverse square law.
"""

import logging
import math
from config.constants import CONSTANTS

logger = logging.getLogger(__name__)


def calculate_noise_attenuation(dba_at_15m: float, distance_m: float) -> float:
    """
    Calculate noise level at distance using 6 dBA per doubling rule

    Uses acoustic inverse square law:
    - Each doubling of distance reduces noise by 6 dBA
    - Reference distance is 15 meters

    Args:
        dba_at_15m: Noise level at 15 meters (dBA)
        distance_m: Distance to receptor (meters)

    Returns:
        Noise level at receptor distance (dBA)

    Raises:
        ValueError: If distance is not positive

    Example:
        >>> calculate_noise_attenuation(90.0, 30.0)  # 30m is 2x 15m
        84.0  # 90 - 6 = 84 dBA
    """
    if distance_m <= 0:
        raise ValueError(f"Distance must be positive: {distance_m}")

    # Number of doublings from reference distance (15m) to target distance
    # Each doubling reduces noise by 6 dBA
    doublings = math.log2(distance_m / CONSTANTS.NOISE_REFERENCE_DISTANCE_M)
    attenuation = CONSTANTS.NOISE_ATTENUATION_DB_PER_DOUBLING * doublings

    noise_at_distance = dba_at_15m - attenuation

    # Floor at minimum noise level (can't go below 0 dBA)
    result = max(CONSTANTS.MIN_NOISE_LEVEL_DBA, noise_at_distance)

    logger.debug(
        f"Noise attenuation: {dba_at_15m:.1f} dBA @ 15m → "
        f"{result:.1f} dBA @ {distance_m:.1f}m "
        f"({doublings:.2f} doublings, {attenuation:.1f} dBA reduction)"
    )

    return result


def combine_noise_sources_energetic(noise_levels_dba: list[float]) -> float:
    """
    Combine multiple noise sources using energetic addition

    Noise levels combine logarithmically, not linearly:
    L_total = 10 * log10(sum(10^(L_i/10)))

    Args:
        noise_levels_dba: List of noise levels in dBA

    Returns:
        Combined noise level (dBA)

    Example:
        >>> combine_noise_sources_energetic([80.0, 80.0])
        83.0  # Two equal sources increase level by 3 dBA
    """
    if not noise_levels_dba:
        return 0.0

    # Convert dBA to linear energy, sum, convert back
    energy_sum = sum(10 ** (level / 10.0) for level in noise_levels_dba)
    combined_dba = 10.0 * math.log10(energy_sum)

    logger.debug(
        f"Combined {len(noise_levels_dba)} noise sources: "
        f"{noise_levels_dba} → {combined_dba:.1f} dBA"
    )

    return combined_dba
