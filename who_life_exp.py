import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('life_expectancy.csv')
dane = df[['YEAR','REGION','SEX','Numeric']]
# maska = dane['REGION'] == 'GLOBAL'
# dane = dane[maska]
# dane = dane.query('REGION == "GLOBAL"')
dane = dane[dane['REGION'] == 'GLOBAL']
print(dane)

dane_m = dane.query('SEX == "MLE"')
dane_k = dane.query('SEX == "FMLE"')

plt.scatter(dane_m['YEAR'], dane_m['Numeric'])
plt.scatter(dane_k['YEAR'], dane_k['Numeric'])
plt.show()