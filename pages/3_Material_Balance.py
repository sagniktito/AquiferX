import streamlit as st
import numpy as np
import pandas as pd

from modules.material_balance import (
    underground_withdrawal,
    oil_expansion,
    formation_water_expansion,
    total_expansion,
    havlena_odeh,
    recovery_factor
)

from modules.plots import havlena_odeh_plot


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Material Balance",
    page_icon="🛢️",
    layout="wide"
)


st.title("🛢 Material Balance Analysis")

st.markdown(
"""
Estimate **Original Oil In Place (OOIP)** using
Material Balance Equation and Havlena-Odeh analysis.
"""
)

st.divider()


# --------------------------------------------------
# History Input
# --------------------------------------------------

st.header("📋 Reservoir Production History")

st.write(
"""
Enter reservoir history values.
Each row represents a pressure survey period.
"""
)


default_data = pd.DataFrame({

    "Pressure (psi)": [
        3500,
        3300,
        3100,
        2900,
        2700
    ],

    "Np (STB)": [
        0,
        500000,
        1200000,
        2200000,
        3500000
    ],

    "Gp (SCF)": [
        0,
        1e8,
        2.5e8,
        5e8,
        8e8
    ],

    "Wp (STB)": [
        0,
        10000,
        25000,
        50000,
        80000
    ]

})


history = st.data_editor(
    default_data,
    num_rows="dynamic",
    use_container_width=True
)


st.divider()


# --------------------------------------------------
# PVT Inputs
# --------------------------------------------------

st.header("🧪 PVT Properties")


c1, c2, c3 = st.columns(3)


with c1:

    Bo = st.number_input(
        "Bo",
        value=1.25
    )

    Boi = st.number_input(
        "Boi",
        value=1.15
    )


with c2:

    Bg = st.number_input(
        "Bg",
        value=0.005
    )

    Rs = st.number_input(
        "Rs",
        value=500.0
    )


with c3:

    Rsi = st.number_input(
        "Rsi",
        value=600.0
    )

    Bw = st.number_input(
        "Bw",
        value=1.02
    )


st.divider()


# --------------------------------------------------
# Rock Properties
# --------------------------------------------------

st.header("🪨 Rock & Water Properties")


c1, c2, c3 = st.columns(3)


with c1:

    Pi = st.number_input(
        "Initial Pressure (psi)",
        value=3500.0
    )


with c2:

    Cf = st.number_input(
        "Rock Compressibility",
        value=5e-6,
        format="%.2e"
    )


with c3:

    Cw = st.number_input(
        "Water Compressibility",
        value=3e-6,
        format="%.2e"
    )


Swi = st.number_input(
    "Initial Water Saturation",
    value=0.25
)


st.divider()


# --------------------------------------------------
# Water Influx
# --------------------------------------------------

st.header("🌊 Aquifer Support")

use_water = st.checkbox(
    "Include Water Influx"
)


if use_water:

    We_value = st.number_input(
        "Final Cumulative Water Influx (rb)",
        value=5000000.0
    )

else:

    We_value = 0.0



# --------------------------------------------------
# Calculations
# --------------------------------------------------

if st.button("Run Material Balance"):


    pressure = np.array(
        history["Pressure (psi)"]
    )


    Np = np.array(
        history["Np (STB)"]
    )


    Gp = np.array(
        history["Gp (SCF)"]
    )


    Wp = np.array(
        history["Wp (STB)"]
    )


    F = underground_withdrawal(
        Np,
        Bo,
        Gp,
        Bg,
        Wp,
        Bw
    )


    Eo = oil_expansion(
        Bo,
        Boi,
        Rs,
        Rsi,
        Bg
    )


    Efw = formation_water_expansion(
        Cf,
        Cw,
        Swi,
        Pi,
        pressure
    )


    E = total_expansion(
        Eo,
        Efw
    )


    We = np.linspace(
        0,
        We_value,
        len(F)
    )


    result = havlena_odeh(
        F,
        E,
        We
    )


    OOIP = result["OOIP"]


    RF = recovery_factor(
        Np[-1],
        OOIP
    )


    st.divider()


    st.header("📊 Results")


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "OOIP",
            f"{OOIP/1e6:.2f} MMSTB"
        )


    with c2:

        st.metric(
            "Recovery Factor",
            f"{RF:.2f}%"
        )


    with c3:

        st.metric(
            "Havlena-Odeh R²",
            f"{result['R2']:.3f}"
        )


    st.divider()


    fig = havlena_odeh_plot(
        E,
        F,
        We
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader("Regression Results")


    st.write(
        {
            "Slope (OOIP)": result["Slope"],
            "Intercept": result["Intercept"],
            "R²": result["R2"]
        }
    )