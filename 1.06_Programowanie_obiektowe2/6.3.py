# Stwórz klasę DokładnyZegar, która dziedziczy po Zegar
# i która jeszcze będzie przyjmowała opcjonalnie milisekundy.


class Czas:
    def __init__(self, godziny=0, minuty=0, sekundy=0):
        self.g = godziny
        self.m = minuty
        self.s = sekundy


class Zegar(Czas):
    def __init__(self, format_czasu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_czasu = format_czasu


class DokladnyZegar(Zegar):
    def __init__(self, *args, milisekundy=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.ms = milisekundy


zeg = DokladnyZegar('12h', 10, minuty=11, sekundy=12, milisekundy=13)
print(zeg.g)
print(zeg.m)
print(zeg.s)
print(zeg.ms)
print(zeg.format_czasu)

