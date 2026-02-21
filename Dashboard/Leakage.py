import sys, os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'Data', 'SuperStoreOrders.csv')

from Scripts.data_cleaning import load_clean
from Scripts.leakage_detector import detect_profit_leakage

df = load_clean(csv_path)

product_analysis, high_risk, watchlist, top = detect_profit_leakage(df)

st.title("Profit Leakage Analysis")

st.header("High Risk Products")
st.dataframe(high_risk.head(10))

st.header("Watchlist Products")
st.dataframe(watchlist.head(10))

st.header("Top Loss Making Products")
st.dataframe(top)