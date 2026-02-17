import numpy as np
import pandas as pd

def compute_kpis(df):
    df["profit"] = pd.to_numeric(df["profit"].astype(str).str.replace(",", ""), errors="coerce")
    df["sales"] = pd.to_numeric(df["sales"].astype(str).str.replace(",", ""), errors="coerce")
    total_revenue=df["sales"].sum()
    total_profit=df["profit"].sum()
    profit_margin=(total_profit/total_revenue)*100
    print("total revenue:",total_revenue)
    print("total revenue:",total_revenue)
    print("profit margin",profit_margin)
    return total_revenue,total_profit,profit_margin
