# Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
# odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna);
# obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
# zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)


plik = input("Wybierz 1, aby otworzyć plik 'x.txt'. \n"
             "Wybierz 2, aby otworzyć plik 'y.txt'. \n"
             "Wybierz 3, aby otworzyć plik 'z.txt'. \n")

if plik == '1':
    plik = 'x'
elif plik == '2':
    plik = 'y'
elif plik == '3':
    plik = 'z'


def odczytaj_plik(plik):
    plik = open(plik + '.txt', 'r')
    dane = plik.read()
    plik.close()
    print(dane)


try:
    odczytaj_plik(plik)

except FileNotFoundError:
    print('Wybierz 1, 2 lub 3.')
