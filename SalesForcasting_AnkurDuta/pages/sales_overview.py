import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.paths import DATA_DIR
# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Sales Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Overview Dashboard")

# ---------------------------------
# Load Data
# ---------------------------------

df = load_data()

# ---------------------------------
# Sidebar Filters
# ---------------------------------

st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories))
]

# ---------------------------------
# KPI Cards
# ---------------------------------

total_sales = filtered_df["Sales"].sum()

total_orders = filtered_df["Order ID"].nunique()

average_order = filtered_df["Sales"].mean()

total_customers = filtered_df["Customer ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "📦 Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "🛒 Avg Order Value",
    f"${average_order:,.2f}"
)

col4.metric(
    "👥 Customers",
    f"{total_customers:,}"
)

st.divider()

# ---------------------------------
# Sales by Year
# ---------------------------------

yearly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.year)["Sales"]
    .sum()
    .reset_index()
)

yearly_sales.columns = ["Year", "Sales"]

fig_year = px.bar(
    yearly_sales,
    x="Year",
    y="Sales",
    text_auto=True,
    title="Total Sales by Year"
)

fig_year.update_layout(
    xaxis_title="Year",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_year,
    use_container_width=True
)

# ---------------------------------
# Monthly Sales Trend
# ---------------------------------

monthly_sales = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

fig_month = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig_month.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

# ---------------------------------
# Sales by Region
# ---------------------------------

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig_region = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales by Region"
)

# ---------------------------------
# Sales by Category
# ---------------------------------

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig_category = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    text_auto=True,
    title="Sales by Category"
)

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

