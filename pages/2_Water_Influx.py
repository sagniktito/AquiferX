import streamlit as st
import numpy as np

from modules.schilthuis import schilthuis_influx
from modules.pot_aquifer import pot_aquifer_influx
from modules.hurst_modified import hurst_water_influx

from modules.plots import water_influx_plot
from modules.utils import (
    create_pressure_profile,
    create_time_array
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Water Influx",
    page_icon="🌊",
    layout="wide"
)


st.title("🌊 Water Influx Analysis")

st.markdown(
"""
Calculate cumulative water influx using classical
analytical aquifer models.
"""
)


st.divider()


# --------------------------------------------------
# Reservoir Inputs
# --------------------------------------------------

st.header("Reservoir Conditions")


col1, col2 = st.columns(2)


with col1:

    Pi = st.number_input(
        "Initial Pressure (psi)",
        value=3500.0
    )


with col2:

    Pf = st.number_input(
        "Final Pressure (psi)",
        value=2500.0
    )


years = st.slider(
    "Simulation Time (Years)",
    5,
    30,
    10
)


time = create_time_array(
    years
)


pressure = create_pressure_profile(
    Pi,
    Pf,
    years
)



st.divider()


# --------------------------------------------------
# Model Selection
# --------------------------------------------------

st.header("Select Aquifer Model")


model = st.selectbox(
    "Aquifer Model",
    [
        "Schilthuis",
        "Pot Aquifer",
        "Hurst Modified"
    ]
)



# --------------------------------------------------
# Calculations
# --------------------------------------------------


if model == "Schilthuis":


    C = st.number_input(
        "Aquifer Constant (C)",
        value=5000.0
    )


    We = schilthuis_influx(
        pressure,
        Pi,
        C,
        time
    )



elif model == "Pot Aquifer":


    volume = st.number_input(
        "Aquifer Volume (rb)",
        value=1e8
    )


    phi = st.number_input(
        "Aquifer Porosity",
        value=0.25
    )


    Ct = st.number_input(
        "Total Compressibility",
        value=5e-6,
        format="%.2e"
    )


    We = pot_aquifer_influx(
        pressure,
        Pi,
        volume,
        phi,
        Ct
    )



else:


    C = st.number_input(
        "Aquifer Constant (C)",
        value=5000.0
    )


    a = st.number_input(
        "Hurst Constant (a)",
        value=1.5
    )


    We = hurst_water_influx(
        pressure,
        Pi,
        C,
        a,
        time
    )



st.divider()


# --------------------------------------------------
# Results
# --------------------------------------------------

st.header("Results")


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Final Water Influx",
        f"{We[-1]:,.0f} rb"
    )


with col2:

    st.metric(
        "Pressure Drop",
        f"{Pi-Pf:.0f} psi"
    )



st.divider()


# --------------------------------------------------
# Plot
# --------------------------------------------------

fig = water_influx_plot(
    time,
    We
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# --------------------------------------------------
# Data
# --------------------------------------------------

st.subheader("Calculated Data")


data = {

    "Time (Years)": time,

    "Pressure (psi)": pressure,

    "Water Influx (rb)": We

}


st.dataframe(
    data,
    use_container_width=True
)