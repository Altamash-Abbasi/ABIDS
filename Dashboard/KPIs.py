import sys, os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'Data', 'SuperStoreOrders.csv')

from Scripts.data_cleaning import load_clean
from Scripts.kpi_engine import compute_kpis

df = load_clean(csv_path)

total_revenue, total_profit, profit_margin = compute_kpis(df)

st.title("Executive KPIs")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Total Profit", f"{total_profit:,.0f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")