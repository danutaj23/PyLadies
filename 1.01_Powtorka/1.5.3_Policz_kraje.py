# Wyświetl wszystkie kraje, które mają więcej niż jedną walutę (currency) oraz wypisz te waluty.

from countries import countries

for country in countries:
    if len(country["currency"]) > 1:
        print(country["name"]["official"])
        for waluta in country["currency"]:
            print(waluta)
