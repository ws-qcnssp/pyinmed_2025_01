with open('life_expectancy.csv', 'r') as plik:
    linijki = plik.readlines()
    kolumny = linijki[0].split(',')
    print(kolumny[:3])
