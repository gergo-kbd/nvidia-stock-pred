import pandas as pd

df = pd.read_csv("nvidia_stock_2015_to_2024.csv", names = ['index','date','open','high','low','close','adjclose','volume'])

print(df.head())