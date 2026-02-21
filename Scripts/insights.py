def insights(df):
    #top customers
    top_customer=df.groupby("customer_name").agg({
        "profit":"sum"
    })
    top_customer=top_customer.sort_values("profit",ascending=False).head()



    #Most profit and loss making regions
    region=df.groupby("region").agg({
        "profit":"sum"
    })
    profit_region=region.sort_values("profit",ascending=False).head()
    loss_region=region.sort_values("profit").head()



    #category wise analysis
    category=df.groupby("category").agg({
        "sales":"sum",
        "profit":"sum",
        "quantity":"sum",
        "discount":"mean"
    })
    category["profit_margin"]=(category["profit"]/category["sales"])*100
    t_sale=category["sales"].sum()
    t_profit=category["profit"].sum()
    category["sale_share"]=(category["sales"]/t_sale)*100
    category["profit share"]=(category["profit"]/t_profit)*100



    #worst performing category
    loss_category=category.sort_values("profit").head(1)
    loss_df = df[df["profit"] < 0]["profit"].sum()
    loss_per=(loss_category["profit"]/loss_df)*100

    
    #high share share but low profit share region
    region = df.groupby("region").agg({
    "sales": "sum",
    "profit": "sum"
    })

    # totals
    total_sales = region["sales"].sum()
    total_profit = region["profit"].sum()

    # percentages
    region["sales_pct"] = (region["sales"] / total_sales) * 100
    region["profit_pct"] = (region["profit"] / total_profit) * 100

    # averages
    sales_avg = region["sales_pct"].mean()
    profit_avg = region["profit_pct"].mean()

    # leakage regions
    leak_regions = region[
    (region["sales_pct"] > sales_avg) &
    (region["profit_pct"] < profit_avg)
    ].head(1)

    return top_customer,profit_region,loss_region,category,loss_per,leak_regions