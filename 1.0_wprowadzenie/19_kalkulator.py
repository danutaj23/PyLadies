# def moja_funkcja(a, b):
#     c = a + b
#     print("Wynik: " + str(c))
#
# moja_funkcja(4, 6)

# POTEGOWANIE **kwargs
# def potegowanie(a, b=2):
#     c = a ** b
#     print('Liczba ' + str(a) + ' do ' + str(b) + ' jest liczba: ' + str(c))
# potegowanie(4)
# potegowanie(2, b=10)

# ZADANIE
# zmienic powyższą funkcję, aby można było wybrać rodzaj działania słowami:
# dodawanie, odejmowanie, mnożenie, dzielenie, z domyślym dodawaniem.
# Przykład użycia:
# moje_dzialanie(2, 3, dzialanie='mnozenie')


def kalkulator(a, b, dzialanie ='dodawanie'):
    if dzialanie == 'odejmowanie':
        wynik = a - b
        print('Wybrałeś ' + dzialanie + ', wynik to: ' + str(wynik))
    elif dzialanie == 'mnożenie':
        wynik = a * b
        print('Wybrałeś ' + dzialanie + ', wynik to: ' + str(wynik))
    elif dzialanie == 'dzielenie':
        wynik = a / b
        print('Wybrałeś ' + dzialanie + ', wynik to: ' + str(wynik))
    else:
        wynik = a + b
        print('Wybrałeś ' + dzialanie + ', wynik to: ' + str(wynik))


kalkulator(1, 2)
kalkulator(2, 1, 'odejmowanie')
kalkulator(2, 3, 'mnożenie')
kalkulator(6, 3, 'dzielenie')
