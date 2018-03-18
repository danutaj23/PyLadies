# Napisz funkcję, która policzy wszystkie samogłoski w tekście.
# Przykład działania
# >>> policz_samogloski("Ala ma kota") 5
# >>> policz_samogloski("Pies psu niedzwiedziem") 9

def policz_samogloski(zdanie):
    x = 0
    zdanie = zdanie.lower()
    for litera in zdanie:
        samogloski = "aeiouyąęó"
        if litera in samogloski:
            x += 1
    return x


print(policz_samogloski("Ala ma kota"))
print(policz_samogloski("Pies psu niedzwiedziem"))