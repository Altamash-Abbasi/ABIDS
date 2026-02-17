import numpy as np
import pandas as pd

def load_clean(path):
    df=pd.read_csv(path)
    df.columns=df.columns.str.strip().str.lower()
    df["order_date"]=pd.to_datetime(df["order_date"],dayfirst=True, errors="coerce")
    df["ship_date"]=pd.to_datetime(df["ship_date"],dayfirst=True, errors="coerce")
    return df
