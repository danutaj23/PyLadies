# Napisz funkcję, która znajdzie liczbę odważników o wadze A aby zrównoważyć szalę wagi
# z odważnikami o wadze B.
# Przykład działania:
# >>> odwazniki(2, 8) 4, 1
# >>> odwazniki(4, 6) 3, 2

from math import gcd


def odwazniki (waga_a, waga_b):
    if waga_a == waga_b:
        return 1, 1
    elif waga_a != waga_b:
        nwd = gcd(waga_a, waga_b)       # nwd -> najwiekszy wspolny dzielnik
        ilosc_odwaznikow_a = waga_b/nwd
        ilosc_odwaznikow_b = waga_a/nwd
    return ilosc_odwaznikow_a, ilosc_odwaznikow_b


print(odwazniki(2, 8))
print(odwazniki(4, 6))
print(odwazniki(3, 3))
