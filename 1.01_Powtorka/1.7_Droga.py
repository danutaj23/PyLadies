# Napisz funkcję, która policzy drogę pokonaną przez samochód w czasie t i przyspieszeniu a
# z opcjonalną prędkością początkową, domyślnie równą 0.
# >>> droga(5, 5) 62.5
# >>> droga(10, 10, vs=100) 1500

# czas - t
# przyspieszenie - a
# predkosc poczatkowa - v0
# droga - s


def policz_droge (t, a, v0=0):

    s = v0 * t + (a * (t**2)) / 2
    return s


print(policz_droge(5, 5))
print(policz_droge(10, 10, 100))