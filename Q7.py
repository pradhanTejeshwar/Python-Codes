import pandas as pd
df=pd.read_csv('COVID Data.csv')
avg=df['Price'].mean()
count=df['Price'].count()
print('Avg of Price: ' +str(avg))
print('Total Data: ' +str(count))
df3=pd.read_csv('COVID Data.csv')
gc = df3.groupby(['State/UnionTerritory','Confirmed']).sum()
print(gc)