# Stwórz klasę Czas, której konstruktor (__init__) będzie brał trzy opcjonalne argumenty:
# godzinę, minuty, sekundy i zapisywal je w odpowiednich zmiennych (np. 'h', 'godz', 'hour') w klasie.


class Czas:
    def __init__(self, godziny=0, minuty=0, sekundy=0):
        self.g = godziny
        self.m = minuty
        self.s = sekundy


n_czas = Czas(10, 11, 12)
print(n_czas.g)
print(n_czas.m)
print(n_czas.s)
