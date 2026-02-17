import sys
import os
import streamlit as st

# Add the project root to Python path so Scripts can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Base directory for this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct absolute path to the CSV file
csv_path = os.path.join(BASE_DIR, '..', 'Data', 'SuperStoreOrders.csv')

# ------------------ IMPORT MODULES ------------------
from Scripts.data_cleaning import load_clean
from Scripts.kpi_engine import compute_kpis
from Scripts.leakage_detector import detect_profit_leakage
from Scripts.recommendation_engine import generate_recommendation

# ------------------ LOAD DATA ------------------
df = load_clean(csv_path)  # ✅ Use the absolute path

# ------------------ KPIs ------------------
total_revenue, total_profit, profit_margin = compute_kpis(df)

st.title("ABIDS — Automated Business Intelligence Dashboard")

st.header("Executive KPIs")
st.metric("Total Revenue", f"{total_revenue:,.0f}")
st.metric("Total Profit", f"{total_profit:,.0f}")
st.metric("Profit Margin", f"{profit_margin:.2f}%")

# ------------------ LEAKAGE ------------------
product_analysis, high_risk, watchlist = detect_profit_leakage(df)

st.header("High Risk Products")
st.dataframe(high_risk.head(10))

st.header("Watchlist Products")
st.dataframe(watchlist.head(10))

# ------------------ RECOMMENDATIONS ------------------
recommendations = generate_recommendation(product_analysis)

st.header("Recommendations")

for r in recommendations[:10]:
    st.write(f"Product: {r[0]} | Category: {r[1]} | Action: {r[2]}")
