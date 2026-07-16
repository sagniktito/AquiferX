import streamlit as st

from modules.schilthuis import schilthuis_influx
from modules.pot_aquifer import pot_aquifer_influx
from modules.hurst_modified import hurst_water_influx

from modules.utils import (
    create_pressure_profile,
    create_time_array
)

from modules.plots import compare_models_plot

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Model Comparison",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Aquifer Model Comparison")

st.markdown("""
Compare the cumulative water influx predicted by the
implemented analytical aquifer models under identical
reservoir conditions.
""")

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

time = create_time_array(years)

pressure = create_pressure_profile(
    Pi,
    Pf,
    years
)

st.divider()

# --------------------------------------------------
# Aquifer Parameters
# --------------------------------------------------

st.header("Aquifer Properties")

c1, c2 = st.columns(2)

with c1:

    C = st.number_input(
        "Aquifer Constant (C)",
        value=5000.0
    )

    a = st.number_input(
        "Hurst Constant (a)",
        value=1.5
    )

with c2:

    volume = st.number_input(
        "Aquifer Volume (rb)",
        value=1e8,
        format="%.0f"
    )

    phi = st.number_input(
        "Porosity",
        value=0.25
    )

Ct = st.number_input(
    "Total Compressibility",
    value=5e-6,
    format="%.2e"
)

st.divider()

# --------------------------------------------------
# Calculations
# --------------------------------------------------

schil = schilthuis_influx(
    pressure,
    Pi,
    C,
    time
)

pot = pot_aquifer_influx(
    pressure,
    Pi,
    volume,
    phi,
    Ct
)

hurst = hurst_water_influx(
    pressure,
    Pi,
    C,
    a,
    time
)

# --------------------------------------------------
# Plot
# --------------------------------------------------

st.header("Comparison Plot")

fig = compare_models_plot(
    time,
    schil,
    pot,
    hurst
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Results
# --------------------------------------------------

st.header("Comparison Summary")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Schilthuis",
        f"{schil[-1]:,.0f} rb"
    )

with col2:

    st.metric(
        "Pot Aquifer",
        f"{pot[-1]:,.0f} rb"
    )

with col3:

    st.metric(
        "Hurst Modified",
        f"{hurst[-1]:,.0f} rb"
    )

st.divider()

summary = {
    "Model": [
        "Schilthuis",
        "Pot Aquifer",
        "Hurst Modified"
    ],
    "Final Water Influx (rb)": [
        schil[-1],
        pot[-1],
        hurst[-1]
    ]
}

st.dataframe(
    summary,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Notes
# --------------------------------------------------

with st.expander("Engineering Notes"):

    st.markdown("""
- **Schilthuis** assumes steady-state aquifer support.

- **Pot Aquifer** models a finite aquifer with limited water storage.

- **Hurst Modified** improves the steady-state model by incorporating a time-dependent drainage radius.

These models provide different estimates of cumulative water influx depending on the assumed aquifer behavior.
""")