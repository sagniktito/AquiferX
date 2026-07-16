#  AquiferX

An interactive **reservoir engineering toolkit** developed using **Python** and **Streamlit** for analytical steady state water influx modelling and material balance analysis.

---

## Features

- Schilthuis Steady-State Aquifer Model
- Pot Aquifer Model
- Hurst Modified Steady-State Model
- Material Balance Equation (MBE)
- Aquifer Model Comparison
- Sensitivity Analysis
- Interactive Plotly Visualizations

---

## Application Structure

```text
AquiferX/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── material_balance.py
│   ├── schilthuis.py
│   ├── pot_aquifer.py
│   ├── hurst_modified.py
│   ├── plots.py
│   └── utils.py
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Water_Influx.py
│   ├── 3_Material_Balance.py
│   ├── 4_Model_Comparison.py
│   └── 5_Sensitivity.py
│
└── assets/
    └── logo.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sagniktito/AquiferX.git
```

Navigate into the project:

```bash
cd AquiferX
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Technologies

- Python
- Streamlit
- NumPy
- Pandas
- Plotly

---

## Engineering Methods

- Schilthuis Steady-State Water Influx Model
- Pot Aquifer Model
- Hurst Modified Steady-State Model
- Material Balance Equation
- Havlena-Odeh Method

---

## Project Purpose

AquiferX was developed as an educational reservoir engineering application to demonstrate classical analytical methods for aquifer-supported reservoirs through an interactive interface.

---

## Author

**Sagnik Das**

B.Tech Petroleum Engineering

Indian Institute of Technology (ISM) Dhanbad
