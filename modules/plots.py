"""
plots.py

Plotly visualization functions for WaterDriveX.
"""

import plotly.graph_objects as go


def water_influx_plot(time, water_influx):
    """
    Plot cumulative water influx.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=time,
            y=water_influx,
            mode="lines+markers",
            name="Water Influx"
        )
    )

    fig.update_layout(
        title="Cumulative Water Influx",
        xaxis_title="Time (Years)",
        yaxis_title="Water Influx (rb)",
        template="plotly_white",
        hovermode="x unified"
    )

    return fig


def pressure_plot(time, pressure):
    """
    Plot reservoir pressure decline.
    """

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

    return fig


def compare_models_plot(
    time,
    schilthuis,
    pot,
    hurst
):
    """
    Compare all implemented aquifer models.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=time,
            y=schilthuis,
            mode="lines+markers",
            name="Schilthuis"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=time,
            y=pot,
            mode="lines+markers",
            name="Pot Aquifer"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=time,
            y=hurst,
            mode="lines+markers",
            name="Hurst Modified"
        )
    )

    fig.update_layout(
        title="Aquifer Model Comparison",
        xaxis_title="Time (Years)",
        yaxis_title="Water Influx (rb)",
        template="plotly_white",
        hovermode="x unified"
    )

    return fig


def havlena_odeh_plot(E, F, We):
    """
    Havlena-Odeh diagnostic plot.

    X-axis : Total Expansion (E)

    Y-axis : F - We
    """

    y = [
        f - w
        for f, w in zip(F, We)
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=E,
            y=y,
            mode="markers+lines",
            name="Havlena-Odeh"
        )
    )

    fig.update_layout(
        title="Havlena-Odeh Diagnostic",
        xaxis_title="Expansion Term (E)",
        yaxis_title="F - We",
        template="plotly_white"
    )

    return fig


def sensitivity_plot(
    x,
    y,
    parameter_name
):
    """
    Plot sensitivity analysis.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines+markers",
            name=parameter_name
        )
    )

    fig.update_layout(
        title=f"Sensitivity Analysis: {parameter_name}",
        xaxis_title=parameter_name,
        yaxis_title="Water Influx (rb)",
        template="plotly_white",
        hovermode="x unified"
    )

    return fig