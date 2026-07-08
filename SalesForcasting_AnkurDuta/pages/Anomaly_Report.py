import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Anomaly Report",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Sales Anomaly Report")

st.markdown("""
Detect unusual weekly sales using:

- Isolation Forest
- Rolling Z-Score
""")

df = pd.read_csv("data/Anomaly_result.csv")

df["Week"] = pd.to_datetime(df["Week"])

st.sidebar.header("Anomaly Filter")

method = st.sidebar.selectbox(
    "Detection Method",
    [
        "Isolation Forest",
        "Z-Score",
        "Both"
    ]
)


if method == "Isolation Forest":

    anomalies = df[
        df["Isolation_Label"] == -1
    ]

elif method == "Z-Score":

    anomalies = df[
        df["Z_Anomaly"] == True
    ]

else:

    anomalies = df[
        (df["Isolation_Label"] == -1) |
        (df["Z_Anomaly"] == True)
    ]

c1, c2, c3 = st.columns(3)

c1.metric(
    "🚨 Total Anomalies",
    len(anomalies)
)

c2.metric(
    "Highest Sales",
    f"${anomalies['Sales'].max():,.0f}"
)

c3.metric(
    "Lowest Sales",
    f"${anomalies['Sales'].min():,.0f}"
)

fig = go.Figure()

# Weekly Sales

fig.add_trace(

    go.Scatter(

        x=df["Week"],

        y=df["Sales"],

        mode="lines",

        name="Weekly Sales",

        line=dict(width=3)

    )

)

# Anomalies

fig.add_trace(

    go.Scatter(

        x=anomalies["Week"],

        y=anomalies["Sales"],

        mode="markers",

        marker=dict(

            size=14,

            color="red",

            symbol="x"

        ),

        name="Anomaly"

    )

)

fig.update_layout(

    title="Weekly Sales with Detected Anomalies",

    xaxis_title="Week",

    yaxis_title="Sales",

    template="plotly_white",

    height=600

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📋 Detected Anomalies")

table = anomalies[
    [
        "Week",
        "Sales",
        "Isolation_Label",
        "Z_Anomaly"
    ]
]

st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)

st.info(f"""
### 📌 Business Insight

A total of **{len(anomalies)} anomalous weeks** were detected using
**{method}**.

These unusual sales values may correspond to:

- Seasonal demand
- Festival promotions
- Clearance sales
- Supply chain disruptions
- Unexpected market behaviour

Further business investigation is recommended before making inventory decisions.
""")

st.download_button(

    "📥 Download Anomaly Report",

    table.to_csv(index=False),

    file_name="anomaly_report.csv",

    mime="text/csv"

)