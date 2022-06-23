import os
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/lym/quantium-starter-repo/data/combined_csv.csv')
df['sales'] = df['price'] * df['quantity']
df=df.query("product != 'pink morsel'")
df.drop(['price','quantity','product'], axis=1, inplace=True)
for col in df.columns:
    print(col)

