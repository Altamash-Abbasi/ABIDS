import sys
import os
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Add the project root to Python path so Scripts can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'Data', 'SuperStoreOrders.csv')

# ------------------ IMPORT MODULES ------------------
from Scripts.data_cleaning import load_clean
from Scripts.kpi_engine import compute_kpis
from Scripts.leakage_detector import detect_profit_leakage
from Scripts.recommendation_engine import generate_recommendation
from Scripts.insights import insights
from Scripts.executive_summary import generate_executive_summary

# ------------------ LOAD DATA ------------------
df = load_clean(csv_path)


# ================= INTERFACE =================

def interface(df):

    # ---------------- KPIs ----------------
    total_revenue, total_profit, profit_margin = compute_kpis(df)

    st.title("📊 ABIDS — Automated Business Intelligence And Decision System")
    st.markdown("---")

    st.subheader("Executive KPIs")
    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Revenue", f"{total_revenue:,.0f}")
    col2.metric("📈 Total Profit", f"{total_profit:,.0f}")
    col3.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

    # ---------------- PROFIT TREND ----------------
    st.markdown("### 📅 Profit Trend Over Time")

    trend_fig = px.line(
        df.sort_values("order_date"),
        x="order_date",
        y="profit",
        markers=True,
        title="Profit Over Time"
    )

    st.plotly_chart(trend_fig, use_container_width=True)

    # ---------------- SALES vs PROFIT ----------------
    st.markdown("### 💡 Sales vs Profit Relationship")

    scatter_fig = px.scatter(
    df,
    x="sales",
    y="profit",
    color="category",
    hover_data=["region"],
    title="Sales vs Profit by Category"
    )

    st.plotly_chart(scatter_fig, use_container_width=True)

    st.markdown("---")

    # ---------------- LEAKAGE ----------------
    product_analysis, high_risk, watchlist, top = detect_profit_leakage(df)

    st.header("🚨 Profit Leakage Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("High Risk Products")
        st.dataframe(high_risk.head(10), hide_index=True)

    with col2:
        st.subheader("Watchlist Products")
        st.dataframe(watchlist.head(10), hide_index=True)

    st.subheader("Top Loss Making Products")

    loss_fig = px.bar(
        top,
        x="profit",
        y="product_name",
        orientation="h",
        title="Top Loss Making Products"
    )

    st.plotly_chart(loss_fig, use_container_width=True)

    st.markdown("---")

    # ---------------- RECOMMENDATIONS ----------------
    recommendations = generate_recommendation(product_analysis)

    st.header("📌 Recommendations")

    for r in recommendations[:10]:
        st.write(f"Product: {r[0]} | Category: {r[1]} | Action: {r[2]}")

    st.markdown("---")

    # ---------------- INSIGHTS ----------------
    top_customer, profit_region, loss_region, category, loss_per, leak_regions = insights(df)

    st.header("📊 Business Insights")

    # ----- Top Customers -----
    st.subheader("🏆 Top Customers by Profit")

    st.dataframe(top_customer, hide_index=True)

    cust_fig = px.bar(
        top_customer,
        x="customer_name",
        y="profit",
        color="profit",
        title="Top Customers Contribution"
    )

    st.plotly_chart(cust_fig, use_container_width=True)

    # ----- Regions -----
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌍 Most Profitable Regions")

        reg_fig = px.bar(
            profit_region,
            x="region",
            y="profit",
            color="profit",
            title="Profit by Region"
        )

        st.plotly_chart(reg_fig, use_container_width=True)

    with col2:
        st.subheader("⚠️ Loss Making Regions")

        loss_fig = px.bar(
            loss_region,
            x="region",
            y="profit",
            color="profit",
            title="Loss by Region"
        )

        st.plotly_chart(loss_fig, use_container_width=True)

    # ----- Category -----
    st.subheader("📦 Category Performance")

    cat_fig = px.pie(
        category,
        values="profit",
        names="category",
        hole=0.5,
        title="Profit Contribution by Category"
    )

    st.plotly_chart(cat_fig, use_container_width=True)

    # ----- Leakage Regions -----
    st.subheader("⚡ High Sales but Low Profit Regions")

    st.dataframe(leak_regions, hide_index=True)

    st.markdown("---")

    # ---------------- EXECUTIVE SUMMARY ----------------

    matrics_dict = {
        "Total Revenue": total_revenue,
        "Total Profit": total_profit,
        "Profit Margin": profit_margin,
        "Top Customer": top_customer.head(1).to_dict(),
        "Most Profitable Region": profit_region.head(1).to_dict(),
        "Loss Making Region": loss_region.head(1).to_dict(),
        "Worst Category Loss %": loss_per
    }

    if st.button("Generate AI Executive Summary"):
        with st.spinner("Generating strategic insights..."):
            summary = generate_executive_summary(matrics_dict)
            st.subheader("AI Executive Summary")
            st.write(summary)


# ================= FILE UPLOAD =================

file = st.file_uploader("Upload a CSV file", type="csv")
st.write("CSV must contain columns: order_date, region, category, sales, profit, discount")

if file is not None:
    try:
        df = load_clean(file)
        st.success("File uploaded successfully")
    except:
        st.error("Invalid file format or missing required columns")
        st.stop()
else:
    df = load_clean(csv_path)

# ================= SIDEBAR FILTERS =================

st.sidebar.header("🎛 Filters")

regions = sorted(df["region"].dropna().unique())
categories = sorted(df["category"].dropna().unique())

selected_regions = st.sidebar.multiselect("Select Region", regions, default=regions)
selected_categories = st.sidebar.multiselect("Select Category", categories, default=categories)

filtered_df = df[
    (df["region"].isin(selected_regions)) &
    (df["category"].isin(selected_categories))
]

# ================= RENDER =================

interface(filtered_df)

st.caption(
    f"Filtered by Region: {', '.join(selected_regions)} | "
    f"Category: {', '.join(selected_categories)}"
)