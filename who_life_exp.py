import pandas as pd

df = pd.read_csv('life_expectancy.csv')
print(df[['YEAR','REGION','SEX','Numeric']])

