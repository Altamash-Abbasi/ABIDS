from Scripts.data_cleaning import load_clean
from Scripts.kpi_engine import compute_kpis
from Scripts.leakage_detector import detect_profit_leakage
from Scripts.recommendation_engine import generate_recommendation

df=load_clean(r"D:\ai_venv\ai_venv\ABIDS\Data\SuperStoreOrders.csv")
compute_kpis(df)

product_analysis,high_risk,watchlist=detect_profit_leakage(df)

recommendation=generate_recommendation(product_analysis)

print("Recommendations")
for r in recommendation[:10]:
    print(r)
