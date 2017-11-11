# Napisz funkcję, która policzy słowa w tekście. Każde słowo jest oddzielone spacją.
# Przykład działania
# >>> policz_slowa("Ala ma kota") 3
# >>> policz_slowa("Pies psu niedzwiedziem, bo tak") 5


def ile_wyrazow(zdanie):
    wyrazy = zdanie.split(" ")
    return len(wyrazy)


print(ile_wyrazow("Ala ma kota."))
print(ile_wyrazow("Pies psu niedzwiedziem, bo tak."))