import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from numpy.polynomial.polynomial import polyfit

df = pd.read_csv('life_expectancy.csv')
dane = df[['YEAR','REGION','SEX','Numeric']]
# maska = dane['REGION'] == 'GLOBAL'
# dane = dane[maska]
dane = dane.query('REGION == "GLOBAL"')
# dane = dane[dane['REGION'] == 'GLOBAL']
print(dane)

dane_m = dane.query('SEX == "MLE"').sort_values('YEAR')
dane_k = dane.query('SEX == "FMLE"').sort_values('YEAR')

c_m, b_m, a_m = polyfit(dane_m['YEAR'], dane_m['Numeric'], 2)
c_k, b_k, a_k = polyfit(dane_k['YEAR'], dane_k['Numeric'], 2)

print(f'Dopasowana funkcja dla mężczyzn: f(x) = {a_m} * x**2 + {b_m} * x + {c_m}')
print(f'Dopasowana funkcja dla kobiet: f(x) = {a_k} * x**2 + {b_k} * x + {c_k}')

m_2030 = a_m * 2030**2 + b_m*2030 + c_m
print(f"Oczekiwana długość życia mężczyzn w 2030: {m_2030}")

plt.scatter(dane_m['YEAR'], dane_m['Numeric'], label='Mężczyźni')
plt.scatter(dane_k['YEAR'], dane_k['Numeric'], label='Kobiety')
plt.plot(dane_m['YEAR'], a_m * dane_m['YEAR']**2 + b_m * dane_m['YEAR'] + c_m)
plt.plot(dane_k['YEAR'], a_k * dane_k['YEAR']**2 + b_k * dane_k['YEAR'] + c_k)
plt.legend()
plt.title('Długość życia wg WHO - Globalne')
plt.xlabel('Rok')
plt.ylabel('Długość życia (lata)')

wielomian_m = Polynomial([c_m, b_m, a_m])
pochodna_m = wielomian_m.deriv()
ekstremum_m = pochodna_m.roots()
print(f"ekstremum dla mężczyzn: {ekstremum_m}")

plt.show()