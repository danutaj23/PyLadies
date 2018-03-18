# Stwórz klasę Zegar, która dziedziczy po Czas, a konstruktor (__init__)
# będzie brał obowiązkowo parametr format (12H lub 24H) oprócz tych co Czas.


class Czas:
    def __init__(self, godziny=0, minuty=0, sekundy=0):
        self.g = godziny
        self.m = minuty
        self.s = sekundy


class Zegar(Czas):
    def __init__(self, format_czasu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_czasu = format_czasu


zeg = Zegar('12h', 10, minuty=11, sekundy=12)
print(zeg.g)
print(zeg.m)
print(zeg.s)
print(zeg.format_czasu)







