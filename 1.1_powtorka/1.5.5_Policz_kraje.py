# Znajdź kraj o największej powierzchni i wyświetl jego nazwę i powierzchnię.

from countries import countries

najwieksza_powierzchnia = 0
for country in countries:
    powierzchnia = country["area"]
    if powierzchnia > najwieksza_powierzchnia:
        najwieksza_powierzchnia = powierzchnia
        najwiekszy_kraj = country["name"]["official"]
print("Największy kraj: ", najwiekszy_kraj, " Powierzchnia: ", najwieksza_powierzchnia)
