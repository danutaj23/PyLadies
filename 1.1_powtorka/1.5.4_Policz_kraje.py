# Wyświetl wszystkie kraje i ich stolice, jeśli stolica zaczyna się od litery W.

from countries import countries

for country in countries:
    if country["capital"][:1] == "W":
        print("Kraj: " + country["name"]["official"] + ", Stolica: " + country["capital"])

