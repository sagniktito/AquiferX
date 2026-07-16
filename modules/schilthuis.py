"""
schilthuis.py

Implementation of Schilthuis steady-state aquifer model.

Reference:
Schilthuis (1936) developed a steady-state water influx
model assuming constant aquifer pressure support.

Equation:

dWe/dt = C * (Pi - P)

We = cumulative water influx
"""

import numpy as np

from modules.utils import validate_positive


def schilthuis_influx_rate(
    pressure,
    initial_pressure,
    aquifer_constant
):
    """
    Calculate instantaneous water influx rate.

    Parameters
    ----------
    pressure : array-like
        Reservoir pressure history (psi)

    initial_pressure : float
        Initial reservoir pressure (psi)

    aquifer_constant : float
        Aquifer productivity constant

    Returns
    -------
    numpy.ndarray
        Water influx rate (rb/year)
    """

    validate_positive(
        aquifer_constant,
        "Aquifer constant"
    )

    pressure = np.asarray(
        pressure
    )

    pressure_difference = (
        initial_pressure -
        pressure
    )

    influx_rate = (
        aquifer_constant *
        pressure_difference
    )

    return influx_rate



def schilthuis_influx(
    pressure,
    initial_pressure,
    aquifer_constant,
    time=None
):
    """
    Calculate cumulative water influx.

    Parameters
    ----------
    pressure : array-like
        Reservoir pressure history (psi)

    initial_pressure : float
        Initial reservoir pressure (psi)

    aquifer_constant : float
        Aquifer constant

    time : array-like, optional
        Time vector (years)

    Returns
    -------
    numpy.ndarray
        Cumulative water influx (rb)
    """

    influx_rate = schilthuis_influx_rate(
        pressure,
        initial_pressure,
        aquifer_constant
    )


    if time is None:

        time = np.arange(
            1,
            len(influx_rate)+1
        )


    time = np.asarray(
        time
    )


    cumulative_influx = np.cumsum(
        influx_rate *
        np.gradient(time)
    )


    return cumulative_influx