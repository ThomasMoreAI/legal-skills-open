"""
Shared calculation utilities for injurious affection assessment

Provides defensive programming utilities to prevent division by zero and other
common calculation errors.
"""

import logging

logger = logging.getLogger(__name__)


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, returning default if denominator is zero

    Args:
        numerator: Numerator value
        denominator: Denominator value
        default: Default value to return if denominator is zero

    Returns:
        Result of division, or default if denominator is zero
    """
    if denominator == 0:
        logger.warning(
            f"Division by zero attempted: {numerator} / {denominator}. "
            f"Returning default: {default}"
        )
        return default

    return numerator / denominator


def capitalize_annual_cost(
    annual_cost: float,
    cap_rate: float,
    fallback_multiple: float = 10.0
) -> float:
    """
    Capitalize annual cost to present value using capitalization rate

    Uses income approach: PV = Annual Cost / Cap Rate

    Args:
        annual_cost: Annual recurring cost ($)
        cap_rate: Capitalization rate (decimal, e.g., 0.08 for 8%)
        fallback_multiple: Fallback multiplier if cap_rate is invalid (default: 10.0)

    Returns:
        Capitalized present value of annual cost

    Example:
        >>> capitalize_annual_cost(10000, 0.08)
        125000.0
    """
    if cap_rate <= 0:
        logger.warning(
            f"Invalid capitalization rate: {cap_rate}. "
            f"Using fallback multiplier: {fallback_multiple}"
        )
        return annual_cost * fallback_multiple

    return annual_cost / cap_rate


def calculate_percentage(part: float, total: float, default: float = 0.0) -> float:
    """
    Calculate percentage of part to total, safely handling zero total

    Args:
        part: Part value
        total: Total value
        default: Default percentage if total is zero

    Returns:
        Percentage (0-100 scale), or default if total is zero

    Example:
        >>> calculate_percentage(25, 100)
        25.0
    """
    if total == 0:
        return default

    return (part / total) * 100.0


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp value to be within [min_value, max_value] range

    Args:
        value: Value to clamp
        min_value: Minimum allowed value
        max_value: Maximum allowed value

    Returns:
        Clamped value

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    return max(min_value, min(max_value, value))
