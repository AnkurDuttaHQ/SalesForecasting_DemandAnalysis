import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Forecast Explorer",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Forecast Explorer")

st.markdown(
    "Explore **3-month sales forecasts** for different categories and regions using the **Prophet forecasting model**."
)

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

overall = pd.read_csv("data/overall_prophet_forecast.csv")
furniture = pd.read_csv("data/furniture_forecast.csv")
technology = pd.read_csv("data/technology_forecast.csv")
office = pd.read_csv("data/office_forecast.csv")
west = pd.read_csv("data/west_forecast.csv")
east = pd.read_csv("data/east_forecast.csv")

comparison = pd.read_csv("data/model_comparison.csv")

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.header("Forecast Settings")

forecast_type = st.sidebar.radio(
    "Forecast Type",
    ["Category", "Region"]
)

if forecast_type == "Category":

    selection = st.sidebar.selectbox(
        "Category",
        ["Furniture", "Technology", "Office Supplies"]
    )

else:

    selection = st.sidebar.selectbox(
        "Region",
        ["West", "East"]
    )

months = st.sidebar.slider(
    "Forecast Horizon",
    1,
    3,
    3
)

# ----------------------------------------------------
# Dataset Selection
# ----------------------------------------------------

datasets = {
    "Furniture": furniture,
    "Technology": technology,
    "Office Supplies": office,
    "West": west,
    "East": east,
}

forecast = datasets.get(selection, overall).head(months)

# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

prophet = comparison[
    comparison["Model"] == "Prophet"
].iloc[0]

forecast_sales = forecast["yhat"].sum()

avg_forecast = forecast["yhat"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🤖 Best Model",
    prophet["Model"]
)

c2.metric(
    "📉 MAE",
    f"{prophet['MAE']:.2f}"
)

c3.metric(
    "📈 RMSE",
    f"{prophet['RMSE']:.2f}"
)

c4.metric(
    "💰 Forecast Sales",
    f"${forecast_sales:,.0f}"
)

st.divider()

# ----------------------------------------------------
# Interactive Forecast Chart
# ----------------------------------------------------

fig = go.Figure()

# Confidence Band

fig.add_trace(

    go.Scatter(

        x=forecast["ds"],

        y=forecast["yhat_upper"],

        line=dict(width=0),

        showlegend=False,

        hoverinfo="skip"

    )

)

fig.add_trace(

    go.Scatter(

        x=forecast["ds"],

        y=forecast["yhat_lower"],

        fill="tonexty",

        fillcolor="rgba(0,176,246,0.20)",

        line=dict(width=0),

        name="Confidence Interval",

        hoverinfo="skip"

    )

)

# Forecast Line

fig.add_trace(

    go.Scatter(

        x=forecast["ds"],

        y=forecast["yhat"],

        mode="lines+markers",

        name="Forecast",

        line=dict(width=4)

    )

)

fig.update_layout(

    title=f"{selection} Forecast",

    xaxis_title="Month",

    yaxis_title="Forecasted Sales",

    template="plotly_white",

    height=550

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------------------------
# Forecast Summary
# ----------------------------------------------------

st.subheader("📅 Forecast Summary")

summary = forecast.copy()

summary["Forecasted Sales"] = summary["yhat"].round(2)

summary = summary[
    [
        "ds",
        "Forecasted Sales",
        "yhat_lower",
        "yhat_upper"
    ]
]

summary.columns = [

    "Forecast Month",

    "Forecast Sales",

    "Lower Bound",

    "Upper Bound"

]

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# ----------------------------------------------------
# Business Insight
# ----------------------------------------------------

st.info(
    f"""
**Business Insight**

Based on the Prophet model, **{selection}** is expected to generate approximately
**${forecast_sales:,.0f}** over the next **{months} month(s)**.

The shaded blue region represents the prediction confidence interval.
A wider band indicates greater uncertainty in the forecast.
"""
)

# ----------------------------------------------------
# Download
# ----------------------------------------------------

st.download_button(
    "📥 Download Forecast CSV",
    summary.to_csv(index=False),
    file_name=f"{selection}_forecast.csv",
    mime="text/csv"
)