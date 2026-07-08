import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler

# ------------------------------------------------
# Page Config
# ------------------------------------------------

st.set_page_config(
    page_title="Demand Segmentation",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Product Demand Segmentation")

st.markdown("""
Analyze product demand using **K-Means Clustering** based on:

- 💰 Total Sales
- 📈 Growth Rate
- 📊 Sales Volatility
- 🛒 Average Order Value
""")

# ------------------------------------------------
# Load Data
# ------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/clusters_result.csv")

df = load_data()

# ------------------------------------------------
# Sidebar
# ------------------------------------------------

st.sidebar.header("🎯 Cluster Filter")

clusters = sorted(df["Cluster"].unique())

selected = st.sidebar.multiselect(
    "Select Cluster",
    clusters,
    default=clusters
)

filtered = df[df["Cluster"].isin(selected)]

if filtered.empty:
    st.warning("Please select at least one cluster.")
    st.stop()

# ------------------------------------------------
# KPI Cards
# ------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "📦 Sub Categories",
    filtered["Sub-Category"].nunique()
)

c2.metric(
    "🎯 Clusters",
    filtered["Cluster"].nunique()
)

c3.metric(
    "💰 Total Sales",
    f"${filtered['TotalSales'].sum():,.0f}"
)

c4.metric(
    "📈 Avg Growth",
    f"{filtered['GrowthRate'].mean():.2f}%"
)

st.divider()

# ------------------------------------------------
# PCA Scatter Plot
# ------------------------------------------------

scatter_fig = px.scatter(
    filtered,
    x="PC1",
    y="PC2",
    color=filtered["Cluster"].astype(str),
    size="TotalSales",
    hover_name="Sub-Category",
    title="Demand Segmentation using PCA",
    height=650,
    labels={"color": "Cluster"}
)

scatter_fig.update_layout(
    template="plotly_white",
    legend_title="Cluster"
)

st.plotly_chart(
    scatter_fig,
    use_container_width=True
)

st.divider()

# ------------------------------------------------
# Cluster Profile
# ------------------------------------------------

cluster_profile = (
    filtered.groupby("Cluster")[
        [
            "TotalSales",
            "GrowthRate",
            "Volatility",
            "AverageOrderValue"
        ]
    ]
    .mean()
    .reset_index()
)

metrics = [
    "TotalSales",
    "GrowthRate",
    "Volatility",
    "AverageOrderValue"
]

scaler = MinMaxScaler()

cluster_profile[metrics] = scaler.fit_transform(
    cluster_profile[metrics]
)

cluster_names = {
    0: "🟢 High Volume, Stable Demand",
    1: "🟡 Low Volume, High Volatility",
    2: "🔵 Growing Demand",
    3: "🔴 Declining Demand"
}

# ------------------------------------------------
# Radar Chart
# ------------------------------------------------

radar_fig = go.Figure()

categories = [
    "Total Sales",
    "Growth Rate",
    "Volatility",
    "Average Order Value"
]

for _, row in cluster_profile.iterrows():

    values = [
        row["TotalSales"],
        row["GrowthRate"],
        row["Volatility"],
        row["AverageOrderValue"]
    ]

    # Close polygon
    values += values[:1]
    theta = categories + [categories[0]]

    radar_fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=theta,
            fill="toself",
            name=cluster_names.get(
                int(row["Cluster"]),
                f"Cluster {int(row['Cluster'])}"
            )
        )
    )

radar_fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1]
        )
    ),
    title="Cluster Comparison Across Business Metrics",
    template="plotly_white",
    height=650
)

st.plotly_chart(
    radar_fig,
    use_container_width=True
)

st.success("""
### 📊 Business Interpretation

- 🟢 Larger radar area → Strong overall business performance
- 📈 High Growth Rate → Expanding demand
- 💰 High Total Sales → Major revenue contributors
- 📦 High Volatility → Requires careful inventory planning
- 🛒 High Average Order Value → Premium product segment
""")

st.divider()

# ------------------------------------------------
# Products per Cluster
# ------------------------------------------------

cluster_count = (
    filtered
    .groupby("Cluster")
    .size()
    .reset_index(name="Products")
)

bar_fig = px.bar(
    cluster_count,
    x="Cluster",
    y="Products",
    text="Products",
    color="Cluster",
    title="Products in Each Cluster"
)

bar_fig.update_layout(
    template="plotly_white",
    showlegend=False
)

st.plotly_chart(
    bar_fig,
    use_container_width=True
)

st.divider()

# ------------------------------------------------
# Search
# ------------------------------------------------

search = st.text_input(
    "🔍 Search Sub Category"
)

table = filtered.copy()

if search:
    table = table[
        table["Sub-Category"]
        .str.contains(search, case=False, na=False)
    ]

st.subheader("📋 Cluster Details")

st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ------------------------------------------------
# Stocking Strategy
# ------------------------------------------------

st.subheader("📦 Inventory Strategy")

strategies = {

0:
"""
### 🟢 High Volume, Stable Demand

- Maintain high inventory levels
- Frequent replenishment
- Low stock-out tolerance
- Prioritize availability
""",

1:
"""
### 🟡 Low Volume, High Volatility

- Maintain safety stock
- Monitor demand weekly
- Avoid overstocking
- Forecast frequently
""",

2:
"""
### 🔵 Growing Demand

- Increase inventory gradually
- Expand procurement
- Watch seasonal trends
- Improve supplier coordination
""",

3:
"""
### 🔴 Declining Demand

- Reduce inventory
- Run promotional campaigns
- Minimize purchasing
- Prevent dead stock
"""
}

for cluster in selected:
    if cluster in strategies:
        st.info(strategies[cluster])

st.divider()

# ------------------------------------------------
# Download
# ------------------------------------------------

st.download_button(
    "📥 Download Cluster Report",
    data=table.to_csv(index=False).encode("utf-8"),
    file_name="cluster_report.csv",
    mime="text/csv"
)