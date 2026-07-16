import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="WaterDriveX",
    page_icon="🌊",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🌊 WaterDriveX")

st.subheader("Water Influx & Material Balance Analysis Toolkit")

st.markdown(
    """
WaterDriveX is an interactive Streamlit application developed to study
aquifer-supported reservoirs using classical reservoir engineering methods.

The application currently includes:

- Water Influx Models
- Material Balance Analysis
- Aquifer Model Comparison
- Sensitivity Analysis
"""
)

st.divider()

# --------------------------------------------------
# Feature Cards
# --------------------------------------------------

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
### 🌊 Water Influx

- Schilthuis Steady-State
- Pot Aquifer
- Hurst Modified Steady-State
"""
    )

with col2:

    st.info(
        """
### 🛢 Material Balance

- Underground Withdrawal
- Expansion Terms
- Havlena-Odeh Method
- OOIP Estimation
"""
    )

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.header("📈 Workflow")

st.markdown(
"""
1. Select a Water Influx Model.

2. Enter reservoir and aquifer properties.

3. Calculate cumulative water influx.

4. Perform Material Balance Analysis.

5. Compare aquifer models.

6. Study parameter sensitivity.
"""
)

st.divider()

# --------------------------------------------------
# Available Modules
# --------------------------------------------------

st.header("📂 Application Modules")

st.success("🌊 Water Influx")

st.write(
"""
Evaluate cumulative water influx using:

- Schilthuis Model
- Pot Aquifer Model
- Hurst Modified Steady-State Model
"""
)

st.success("🛢 Material Balance")

st.write(
"""
Estimate:

- Underground Withdrawal (F)
- Expansion Terms
- Original Oil In Place (OOIP)
"""
)

st.success("📊 Model Comparison")

st.write(
"""
Compare all implemented aquifer models
using the same reservoir conditions.
"""
)

st.success("⚙ Sensitivity Analysis")

st.write(
"""
Observe the influence of aquifer and
reservoir parameters on water influx.
"""
)

st.divider()

# --------------------------------------------------
# Project Information
# --------------------------------------------------

st.header("ℹ️ About")

st.write(
"""
**Developer**

Sagnik Das

B.Tech Petroleum Engineering

Indian Institute of Technology (ISM) Dhanbad
"""
)

st.write(
"""
This project was developed as an educational
reservoir engineering toolkit using:

- Python
- Streamlit
- NumPy
- Plotly
"""
)

st.divider()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("WaterDriveX")

st.sidebar.info(
"""
Navigate using the pages on the left.

Recommended order:

1. Home

2. Water Influx

3. Material Balance

4. Model Comparison

5. Sensitivity Analysis
"""
)

st.sidebar.success("Version 1.0")