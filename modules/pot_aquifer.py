"""
pot_aquifer.py

Finite Pot Aquifer Model.

The aquifer is treated as a finite storage tank.
Water influx occurs due to expansion of aquifer water
and pore volume reduction during pressure decline.

Equation:

We = Va * phi * Ct * (Pi - P)

Where:

We  = cumulative water influx (rb)
Va  = aquifer bulk volume (rb)
phi = aquifer porosity
Ct  = total compressibility (1/psi)
Pi  = initial pressure
P   = reservoir pressure
"""

import numpy as np

from modules.utils import validate_positive



def pot_aquifer_influx(
    pressure,
    initial_pressure,
    aquifer_volume,
    porosity,
    compressibility
):
    """
    Calculate cumulative water influx
    using Pot Aquifer model.

    Parameters
    ----------
    pressure : array-like
        Reservoir pressure history (psi)

    initial_pressure : float
        Initial reservoir pressure (psi)

    aquifer_volume : float
        Aquifer bulk volume (rb)

    porosity : float
        Aquifer porosity fraction

    compressibility : float
        Total aquifer compressibility (1/psi)


    Returns
    -------
    numpy.ndarray

        Cumulative water influx (rb)
    """

    validate_positive(
        aquifer_volume,
        "Aquifer volume"
    )

    validate_positive(
        porosity,
        "Porosity"
    )

    validate_positive(
        compressibility,
        "Compressibility"
    )


    pressure = np.asarray(
        pressure
    )


    pressure_drop = (
        initial_pressure -
        pressure
    )


    pore_volume = (
        aquifer_volume *
        porosity
    )


    water_influx = (
        pore_volume *
        compressibility *
        pressure_drop
    )


    return water_influx



def pot_aquifer_influx_rate(
    pressure,
    initial_pressure,
    aquifer_volume,
    porosity,
    compressibility,
    time
):
    """
    Calculate instantaneous water influx rate.

    Uses numerical derivative:

    ew = dWe/dt

    Parameters
    ----------
    pressure : array
        Pressure history

    time : array
        Time history


    Returns
    -------
    numpy.ndarray

        Water influx rate
    """


    We = pot_aquifer_influx(
        pressure,
        initial_pressure,
        aquifer_volume,
        porosity,
        compressibility
    )


    rate = np.gradient(
        We,
        time
    )


    return rate