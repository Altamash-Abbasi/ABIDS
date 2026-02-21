import sys, os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'Data', 'SuperStoreOrders.csv')

from Scripts.data_cleaning import load_clean
from Scripts.leakage_detector import detect_profit_leakage
from Scripts.recommendation_engine import generate_recommendation

df = load_clean(csv_path)

product_analysis, _, _, _ = detect_profit_leakage(df)
recommendations = generate_recommendation(product_analysis)

st.title("AI Recommendations")

for r in recommendations[:15]:
    st.write(f"Product: {r[0]} | Category: {r[1]} | Action: {r[2]}")