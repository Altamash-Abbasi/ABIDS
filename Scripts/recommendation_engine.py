def generate_recommendation(product_analysis):
    recommendations=[]

    for product,row in product_analysis.iterrows():

        if row["risk_category"]=="HIGH_RISK":
            
            if row["discount"]>product_analysis["discount"].mean():
                action="Reduce discount - heavy discount causing loss"
            
            elif row["profit_margin"]<0:
                action="Re-evaluate pricing or supplier cost"
            
            else:
                action="consider dis-continuing or repositioning the product"
        elif row["risk_category"]=="WATCHLIST":
            action="Monitor performance and optimize pricing/marketing"
        
        else:
            action="Maintain current strategy"
        
        recommendations.append((product,row["risk_category"],action))
    
    return recommendations