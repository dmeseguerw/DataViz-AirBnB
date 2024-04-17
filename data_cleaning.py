import pandas as pd
import numpy as np

df = pd.read_csv("data/listings.csv")

columns = df.columns

for col in columns:
    nan_vals = df[col].isna().sum()
    print(col,nan_vals)
    
