import pandas as pd

df=pd.read_csv('dev.csv')	
print(df.head())
print(df.describe())
print(df.info())
print('changed')
	