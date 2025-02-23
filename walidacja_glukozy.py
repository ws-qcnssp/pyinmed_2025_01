# Walidacja stężenia glukozy we krwi 
# wartość wejściowa - podać w terminalu
# mg/dL - 70 - 100 
# mmol/L - 3.9 - 5.6
# 1. sprawdzić, z którego zakresu podajemy wartość - wartość 40 graniczna
# 2. zweryfikować poziom i go wypisać razem z jednostką i wartością

wartosc = input('Wprowadź stężenie glukozy we krwi: ')
jednostka = 'mmol/l'

print('Wpisana wartość:', wartosc, 'jednostka:', jednostka)
print('Wpisana wartość: ' + wartosc + ', jednostka: ' + jednostka)
print('Wpisana wartość: {}, jednostka: {}'.format(wartosc, jednostka))
print(f'Wpisana wartość: {wartosc}, jednostka: {jednostka}')
