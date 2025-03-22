import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from numpy.polynomial.polynomial import polyfit

df = pd.read_csv('life_expectancy.csv')
dane = df[['YEAR','REGION','SEX','Numeric']]
# maska = dane['REGION'] == 'GLOBAL'
# dane = dane[maska]
# dane = dane.query('REGION == "GLOBAL"')
dane = dane[dane['REGION'] == 'GLOBAL']
print(dane)

dane_m = dane.query('SEX == "MLE"')
dane_k = dane.query('SEX == "FMLE"')

b_m, a_m = polyfit(dane_m['YEAR'], dane_m['Numeric'], 1)
b_k, a_k = polyfit(dane_k['YEAR'], dane_k['Numeric'], 1)

print(f'Dopasowana funkcja dla mężczyzn: f(x) = {a_m} * x + {b_m}')

plt.scatter(dane_m['YEAR'], dane_m['Numeric'], label='Mężczyźni')
plt.scatter(dane_k['YEAR'], dane_k['Numeric'], label='Kobiety')
plt.legend()
plt.title('Długość życia wg WHO - Globalne')
plt.xlabel('Rok')
plt.ylabel('Długość życia (lata)')

plt.show()