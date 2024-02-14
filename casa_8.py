import pandas as pd
df= pd.read_csv('big-mac-full-index.csv')


for x,r in df.iterrows():
    print(r['name'],r['local_price'],r['currency_code'])

print(df.apply(lambda row: row['name']+" "+ str(row['local_price']) +" "+ str(row['currency_code']), axis=1))