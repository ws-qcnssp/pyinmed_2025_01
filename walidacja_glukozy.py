# Walidacja stężenia glukozy we krwi 
# wartość wejściowa - podać w terminalu
# mg/dL - 70 - 100 
# mmol/L - 3.9 - 5.6
# 1. sprawdzić, z którego zakresu podajemy wartość - wartość 40 graniczna
# 2. zweryfikować poziom i go wypisać razem z jednostką i wartością

wartosc = input('Wprowadź stężenie glukozy we krwi: ')
# jednostka = 'mmol/l'

# print('Wpisana wartość:', wartosc, 'jednostka:', jednostka)
# print('Wpisana wartość: ' + wartosc + ', jednostka: ' + jednostka)
# print('Wpisana wartość: {}, jednostka: {}'.format(wartosc, jednostka))
# print(f'Wpisana wartość: {wartosc}, jednostka: {jednostka}')

wartosc = round(float(wartosc),2) # kowersja na liczbę
print(f'Wprowadzona wartość stężenia: {wartosc}')

if wartosc > 40:
    jednostka = 'mg/dL'
elif wartosc > 0:
    jednostka = 'mmol/L'
else:
    print('Wartość nie może być ujemna')
    # jednostka = 'N/A'
    exit()

print(f'Znaleziona jednostka: {jednostka}')

if jednostka == 'mg/dL':
    dolny_limit = 70
    gorny_limit = 100
else:
    dolny_limit = 3.9
    gorny_limit = 5.6

print(f'Limity: {dolny_limit} do {gorny_limit}')

if wartosc < dolny_limit:
    wynik = 'poniżej normy'
elif wartosc <= gorny_limit:
    wynik = 'w normie'
else:
    wynik = 'powyżej normy'

print(f'Wynik: {wynik}')