"""
Shared calculation utilities with defensive programming

These utility functions provide safe mathematical operations
to prevent division by zero and other calculation errors.
"""

import logging

logger = logging.getLogger(__name__)


def safe_divide(
    numerator: float,
    denominator: float,
    default: float = 0.0
) -> float:
    """
    Safely divide two numbers, returning default if denominator is zero

    Args:
        numerator: The numerator
        denominator: The denominator
        default: Value to return if denominator is zero (default: 0.0)

    Returns:
        float: Result of division or default value

    Examples:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        0.0
        >>> safe_divide(10, 0, default=999.0)
        999.0
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
    Capitalize an annual cost to present value using cap rate

    Uses fallback multiplier if cap rate is zero or negative.

    Args:
        annual_cost: Annual cost to capitalize
        cap_rate: Capitalization rate (decimal, e.g., 0.07 for 7%)
        fallback_multiple: Multiple to use if cap_rate <= 0 (default: 10.0)

    Returns:
        float: Capitalized present value

    Examples:
        >>> capitalize_annual_cost(10000, 0.07)
        142857.14
        >>> capitalize_annual_cost(10000, 0.0)
        100000.0  # Uses 10x fallback
        >>> capitalize_annual_cost(10000, 0.0, fallback_multiple=12.0)
        120000.0
    """
    if cap_rate <= 0:
        logger.warning(
            f"Cap rate is {cap_rate:.4f} (invalid). "
            f"Using fallback {fallback_multiple}x multiple instead."
        )
        return annual_cost * fallback_multiple

    capitalized = annual_cost / cap_rate

    logger.debug(
        f"Capitalized ${annual_cost:,.2f} at {cap_rate:.2%} = ${capitalized:,.2f}"
    )

    return capitalized


def calculate_percentage_change(
    before_value: float,
    after_value: float
) -> float:
    """
    Calculate percentage change between two values

    Args:
        before_value: Original value
        after_value: New value

    Returns:
        float: Percentage change (decimal, e.g., 0.25 for 25% increase)

    Examples:
        >>> calculate_percentage_change(100, 125)
        0.25
        >>> calculate_percentage_change(100, 75)
        -0.25
        >>> calculate_percentage_change(0, 100)
        0.0  # Safe default when before_value is zero
    """
    if before_value == 0:
        logger.warning(
            "Cannot calculate percentage change with zero base value. "
            "Returning 0.0"
        )
        return 0.0

    return (after_value - before_value) / before_value


def convert_sq_m_to_acres(square_meters: float) -> float:
    """
    Convert square meters to acres

    Args:
        square_meters: Area in square meters

    Returns:
        float: Area in acres
    """
    SQ_M_PER_ACRE = 4046.86
    return square_meters / SQ_M_PER_ACRE


def convert_sq_ft_to_acres(square_feet: float) -> float:
    """
    Convert square feet to acres

    Args:
        square_feet: Area in square feet

    Returns:
        float: Area in acres
    """
    SQ_FT_PER_ACRE = 43560.0
    return square_feet / SQ_FT_PER_ACRE


def convert_acres_to_sq_ft(acres: float) -> float:
    """
    Convert acres to square feet

    Args:
        acres: Area in acres

    Returns:
        float: Area in square feet
    """
    SQ_FT_PER_ACRE = 43560.0
    return acres * SQ_FT_PER_ACRE


def convert_acres_to_sq_m(acres: float) -> float:
    """
    Convert acres to square meters

    Args:
        acres: Area in acres

    Returns:
        float: Area in square meters
    """
    SQ_M_PER_ACRE = 4046.86
    return acres * SQ_M_PER_ACRE
