import streamlit as st
import numpy as np

from modules.schilthuis import schilthuis_influx
from modules.utils import (
    create_pressure_profile,
    create_time_array
)
from modules.plots import sensitivity_plot


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Sensitivity Analysis",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Sensitivity Analysis")

st.markdown("""
Investigate how different reservoir parameters affect
predicted cumulative water influx using the
Schilthuis Steady-State Model.
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
# Sensitivity Parameter
# --------------------------------------------------

st.header("Sensitivity Study")

parameter = st.selectbox(
    "Parameter",
    [
        "Aquifer Constant",
        "Final Pressure"
    ]
)

# --------------------------------------------------
# Aquifer Constant
# --------------------------------------------------

if parameter == "Aquifer Constant":

    values = np.arange(
        1000,
        11000,
        1000
    )

    final_influx = []

    for value in values:

        We = schilthuis_influx(
            pressure,
            Pi,
            value,
            time
        )

        final_influx.append(
            We[-1]
        )

# --------------------------------------------------
# Final Pressure
# --------------------------------------------------

else:

    values = np.arange(
        1800,
        3100,
        100
    )

    final_influx = []

    for value in values:

        p = create_pressure_profile(
            Pi,
            value,
            years
        )

        We = schilthuis_influx(
            p,
            Pi,
            5000,
            time
        )

        final_influx.append(
            We[-1]
        )

# --------------------------------------------------
# Plot
# --------------------------------------------------

fig = sensitivity_plot(
    values,
    final_influx,
    parameter
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Results Table
# --------------------------------------------------

st.subheader("Sensitivity Results")

results = {

    parameter: values,

    "Final Water Influx (rb)": final_influx

}

st.dataframe(
    results,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Observation
# --------------------------------------------------

if parameter == "Aquifer Constant":

    st.info(
        """
Increasing the aquifer constant increases the
predicted cumulative water influx, indicating
stronger aquifer support.
"""
    )

else:

    st.info(
        """
Lower reservoir pressure leads to larger pressure
drawdown and therefore higher cumulative water
influx.
"""
    )