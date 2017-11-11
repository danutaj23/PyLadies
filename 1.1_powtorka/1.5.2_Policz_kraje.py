# Wyświetl wszystkie kraje niebędące w Afryce (Africa).

from countries import countries

for country in countries:
    if country["subregion"] != "Africa":
        print(country["name"]["official"])
