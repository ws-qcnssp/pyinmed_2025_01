import pandas as pd

df = pd.read_csv('life_expectancy.csv')
dane = df[['YEAR','REGION','SEX','Numeric']]
# maska = dane['REGION'] == 'GLOBAL'
# dane = dane[maska]
# dane = dane.query('REGION == "GLOBAL"')
dane = dane[dane['REGION'] == 'GLOBAL']
print(dane)

