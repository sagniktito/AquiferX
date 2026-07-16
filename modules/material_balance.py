"""
material_balance.py

Material Balance Equation (MBE) utilities.

Includes:

- Underground withdrawal calculation
- Expansion terms
- Havlena-Odeh analysis
- OOIP estimation
"""


import numpy as np

from modules.utils import validate_positive



# --------------------------------------------------
# Underground Withdrawal
# --------------------------------------------------

def underground_withdrawal(
    Np,
    Bo,
    Gp,
    Bg,
    Wp=0,
    Bw=1
):
    """
    Calculate underground withdrawal.

    F = NpBo + GpBg + WpBw


    Parameters
    ----------
    Np : float
        Cumulative oil production (STB)

    Bo : float
        Oil formation volume factor

    Gp : float
        Gas production (SCF)

    Bg : float
        Gas formation volume factor

    Wp : float
        Water production

    Bw : float
        Water formation volume factor


    Returns
    -------
    float
        Underground withdrawal
    """

    return (
        Np * Bo
        +
        Gp * Bg
        +
        Wp * Bw
    )



# --------------------------------------------------
# Oil Expansion
# --------------------------------------------------

def oil_expansion(
    Bo,
    Boi,
    Rs,
    Rsi,
    Bg
):
    """
    Oil expansion term.

    Eo = (Bo-Boi)+(Rsi-Rs)Bg
    """


    return (
        (Bo - Boi)
        +
        (Rsi - Rs) * Bg
    )



# --------------------------------------------------
# Formation and Water Expansion
# --------------------------------------------------

def formation_water_expansion(
    Cf,
    Cw,
    Swi,
    Pi,
    pressure
):
    """
    Rock and connate water expansion.

    Efw = (Cf + Cw*Swi)(Pi-P)
    """


    pressure = np.asarray(
        pressure
    )


    return (
        (
            Cf
            +
            Cw * Swi
        )
        *
        (
            Pi-pressure
        )
    )



# --------------------------------------------------
# Total Expansion
# --------------------------------------------------

def total_expansion(
    Eo,
    Efw,
    Eg=0
):
    """
    Total reservoir expansion.

    E = Eo + Efw + Eg
    """


    return (
        Eo
        +
        Efw
        +
        Eg
    )



# --------------------------------------------------
# Havlena-Odeh
# --------------------------------------------------

def havlena_odeh(
    F,
    E,
    We=None
):
    """
    Havlena-Odeh straight line method.

    Relationship:

    F - We = N * E


    Returns
    -------
    dict

    OOIP
    slope
    intercept
    R2
    """

    F = np.asarray(F)

    E = np.asarray(E)


    if We is None:

        We = np.zeros(
            len(F)
        )

    else:

        We = np.asarray(
            We
        )


    y = F - We


    slope, intercept = np.polyfit(
        E,
        y,
        1
    )


    y_pred = (
        slope * E
        +
        intercept
    )


    ss_res = np.sum(
        (
            y-y_pred
        )**2
    )


    ss_tot = np.sum(
        (
            y-np.mean(y)
        )**2
    )


    if ss_tot == 0:

        r2 = 0

    else:

        r2 = (
            1 -
            ss_res/ss_tot
        )


    return {

        "OOIP": slope,

        "Slope": slope,

        "Intercept": intercept,

        "R2": r2,

        "Predicted": y_pred

    }



# --------------------------------------------------
# Recovery Factor
# --------------------------------------------------

def recovery_factor(
    Np,
    OOIP
):
    """
    Calculate recovery factor (%).
    """

    if OOIP <= 0:

        return 0


    return (
        Np/OOIP
    )*100