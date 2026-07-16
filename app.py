import streamlit as st
import plotly.graph_objects as go

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="WaterDriveX",
    page_icon="🌊",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🌊 WaterDriveX")

st.sidebar.success("Version 1.0")

st.sidebar.markdown("""
### Navigation

🏠 Home

🌊 Water Influx

🛢 Material Balance

📊 Model Comparison

⚙ Sensitivity Analysis
""")

st.sidebar.info(
    "Use the page selector in the sidebar to navigate between modules."
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🌊 WaterDriveX")

st.subheader(
    "Interactive Reservoir Engineering Toolkit"
)

st.markdown(
"""
WaterDriveX is an educational reservoir engineering application developed
using **Python**, **Streamlit**, **NumPy**, and **Plotly**.

The application demonstrates classical reservoir engineering techniques for
aquifer-supported reservoirs through an interactive graphical interface.
"""
)

st.divider()

# --------------------------------------------------
# Features
# --------------------------------------------------

st.header("🚀 Features")

c1, c2 = st.columns(2)

with c1:

    st.success("""
### 🌊 Water Influx

- Schilthuis Steady-State
- Pot Aquifer
- Hurst Modified Steady-State
""")

with c2:

    st.success("""
### 🛢 Material Balance

- Underground Withdrawal
- Expansion Terms
- Havlena-Odeh Method
- OOIP Estimation
""")

c3, c4 = st.columns(2)

with c3:

    st.success("""
### 📊 Model Comparison

Compare the implemented
aquifer models using the
same reservoir conditions.
""")

with c4:

    st.success("""
### ⚙ Sensitivity Analysis

Study the influence of
reservoir parameters on
predicted water influx.
""")

st.divider()

# --------------------------------------------------
# Example Reservoir Dashboard
# --------------------------------------------------

st.header("📈 Example Reservoir")

st.caption(
    "Example values are provided for demonstration purposes."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Initial Pressure",
        "3500 psi"
    )

with col2:
    st.metric(
        "Current Pressure",
        "2350 psi"
    )

with col3:
    st.metric(
        "Estimated OOIP",
        "25 MMSTB"
    )

with col4:
    st.metric(
        "Recovery Factor",
        "42%"
    )

# --------------------------------------------------
# Pressure Plot
# --------------------------------------------------

time = list(range(11))

pressure = [
    3500,
    3400,
    3280,
    3150,
    3000,
    2850,
    2700,
    2600,
    2500,
    2420,
    2350
]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=time,
        y=pressure,
        mode="lines+markers",
        name="Pressure"
    )
)

fig.update_layout(
    title="Reservoir Pressure Decline",
    xaxis_title="Time (Years)",
    yaxis_title="Pressure (psi)",
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.header("🛠 Workflow")

st.markdown("""
1. 🌊 Calculate water influx using the selected aquifer model.

2. 🛢 Estimate Original Oil In Place (OOIP) using Material Balance.

3. 📊 Compare the predictions of different aquifer models.

4. ⚙ Perform sensitivity analysis by varying reservoir parameters.
""")

st.divider()

# --------------------------------------------------
# About
# --------------------------------------------------

st.header("ℹ️ About")

st.write("""
**WaterDriveX** is intended for educational use and demonstrates
classical analytical methods used in reservoir engineering.

Current Version Includes:

- Schilthuis Steady-State Model
- Pot Aquifer Model
- Hurst Modified Steady-State Model
- Material Balance Analysis
- Aquifer Model Comparison
- Sensitivity Analysis
""")

st.divider()

st.caption(
    "WaterDriveX • Version 1.0 • Developed using Python, Streamlit and Plotly"
)