import pandas as pd

def detect_profit_leakage(df):

    product=df.groupby("product_name").agg({
        "sales":"sum",
        "profit":"sum",
        "quantity":"sum",
        "discount":"mean"
    })

    product["profit_margin"]=(product["profit"]/product["sales"])*100

    #benchmarks for finding loss making product with high sales

    sale_median=product["sales"].median()
    discount_avg=product["discount"].mean()
    margin_avg=product["profit_margin"].mean()
    
    def compute_risk(row):
        score=0

        #high revenue but poor margin
        if row["sales"]>sale_median and row["profit_margin"]<margin_avg:
            score+=2
        
        #negative profit
        if row["profit"]<0:
            score+=3
        
        #heavy discount
        if row["discount"]>discount_avg:
            score+=1

        return score
    
    product["risk_score"]=product.apply(compute_risk,axis=1)

    #classification of product

    def classify(score):
        if score>=4:
            return "HIGH_RISK"
        elif score>=2:
            return "WATCHLIST"
        else:
            return "HEALTHY"
    product["risk_category"]=product["risk_score"].apply(classify)

    #output

    high_risk=product[product["risk_category"]=="HIGH_RISK"]
    watchlist=product[product["risk_category"]=="WATCHLIST"]

    print("High Risks Product")
    print(high_risk.sort_values("risk_score",ascending=False).head())

    print("Watchlist Products")
    print(watchlist.sort_values("risk_score",ascending=False).head())

    return product,high_risk,watchlist