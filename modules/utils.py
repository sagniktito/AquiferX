"""
utils.py

Utility functions used throughout WaterDriveX.
"""

import numpy as np


def pressure_drop(
    initial_pressure,
    current_pressure
):
    """
    Calculate pressure drop.

    Parameters
    ----------
    initial_pressure : float

    current_pressure : float

    Returns
    -------
    float
    """

    return initial_pressure - current_pressure


def cumulative_sum(values):
    """
    Calculate cumulative sum.

    Parameters
    ----------
    values : array-like

    Returns
    -------
    numpy.ndarray
    """

    return np.cumsum(values)


def validate_positive(
    value,
    name
):
    """
    Ensure a parameter is positive.

    Parameters
    ----------
    value : float

    name : str

    Raises
    ------
    ValueError
    """

    if value <= 0:
        raise ValueError(
            f"{name} must be greater than zero."
        )


def percentage(
    numerator,
    denominator
):
    """
    Calculate percentage safely.
    """

    if denominator == 0:
        return 0.0

    return (
        numerator /
        denominator
    ) * 100


def create_pressure_profile(
    initial_pressure,
    final_pressure,
    steps
):
    """
    Generate a linear pressure decline profile.

    Parameters
    ----------
    initial_pressure : float

    final_pressure : float

    steps : int

    Returns
    -------
    numpy.ndarray
    """

    return np.linspace(
        initial_pressure,
        final_pressure,
        steps
    )


def create_time_array(
    years
):
    """
    Generate simulation time.

    Parameters
    ----------
    years : int

    Returns
    -------
    numpy.ndarray
    """

    return np.arange(
        1,
        years + 1
    )


def format_large_number(value):
    """
    Format large numbers for display.
    """

    if abs(value) >= 1e9:
        return f"{value/1e9:.2f} B"

    if abs(value) >= 1e6:
        return f"{value/1e6:.2f} M"

    if abs(value) >= 1e3:
        return f"{value/1e3:.2f} K"

    return f"{value:.2f}"