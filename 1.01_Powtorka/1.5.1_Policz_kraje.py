# Wyświetl wszystkie kraje w Ameryce Północnej. (Northern America).

from countries import countries

for country in countries:
    if country["subregion"] == "Northern America":
        print(country["name"]["official"])
