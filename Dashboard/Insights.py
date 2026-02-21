import sys, os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'Data', 'SuperStoreOrders.csv')

from Scripts.data_cleaning import load_clean
from Scripts.insights import insights

df = load_clean(csv_path)

top_customers, profit_region, loss_region, category_analyse, worst_category, worst_region = insights(df)

st.title("Business Insights")

st.header("Top Customers")
st.dataframe(top_customers)

st.header("Most Profitable Regions")
st.dataframe(profit_region)

st.header("Loss Making Regions")
st.dataframe(loss_region)

st.header("Category Analysis")
st.dataframe(category_analyse)