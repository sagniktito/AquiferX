"""
hurst_modified.py

Hurst Modified Steady-State Aquifer Model.

Hurst (1943) modified the Schilthuis steady-state
model by considering that the apparent aquifer radius
increases with time.

Equation:

ew = C * (Pi - P) / ln(a*t)

where:

ew = water influx rate
C  = aquifer constant
a  = Hurst constant
t  = time
"""


import numpy as np

from modules.utils import validate_positive



def hurst_influx_rate(
    pressure,
    initial_pressure,
    aquifer_constant,
    hurst_constant,
    time
):
    """
    Calculate water influx rate using
    Hurst modified steady-state model.

    Parameters
    ----------
    pressure : array-like
        Reservoir pressure history (psi)

    initial_pressure : float
        Initial reservoir pressure (psi)

    aquifer_constant : float
        Aquifer constant

    hurst_constant : float
        Hurst parameter (a)

    time : array-like
        Time history (years)


    Returns
    -------
    numpy.ndarray

        Water influx rate (rb/year)
    """


    validate_positive(
        aquifer_constant,
        "Aquifer constant"
    )

    validate_positive(
        hurst_constant,
        "Hurst constant"
    )


    pressure = np.asarray(
        pressure
    )

    time = np.asarray(
        time
    )


    # Avoid ln(0)
    time = np.maximum(
        time,
        1e-6
    )


    pressure_difference = (
        initial_pressure -
        pressure
    )


    denominator = np.log(
        hurst_constant *
        time
    )


    # Prevent division errors
    denominator = np.where(
        denominator == 0,
        1e-6,
        denominator
    )


    influx_rate = (
        aquifer_constant *
        pressure_difference
        /
        denominator
    )


    return influx_rate



def cumulative_water_influx(
    influx_rate,
    time
):
    """
    Calculate cumulative water influx
    from influx rate using numerical integration.

    Parameters
    ----------
    influx_rate : array-like
        Water influx rate

    time : array-like
        Time history


    Returns
    -------
    numpy.ndarray

        Cumulative water influx (rb)
    """


    influx_rate = np.asarray(
        influx_rate
    )

    time = np.asarray(
        time
    )


    cumulative = np.zeros(
        len(influx_rate)
    )


    for i in range(
        1,
        len(influx_rate)
    ):

        dt = (
            time[i]
            -
            time[i-1]
        )

        cumulative[i] = (
            cumulative[i-1]
            +
            influx_rate[i]
            *
            dt
        )


    return cumulative



def hurst_water_influx(
    pressure,
    initial_pressure,
    aquifer_constant,
    hurst_constant,
    time
):
    """
    Complete Hurst model calculation.

    Returns cumulative water influx.
    """


    rate = hurst_influx_rate(
        pressure,
        initial_pressure,
        aquifer_constant,
        hurst_constant,
        time
    )


    We = cumulative_water_influx(
        rate,
        time
    )


    return We