# Znajdź kraj, który graniczy z największą ilością innych krajów (borders) i wyświetl jego nazwę oraz ilość granic

from countries import countries

ile_granic = 0
kraj_najwiecej_granic = ""
for country in countries:
    granice = len(country["borders"])
    if granice > ile_granic:
        ile_granic = granice
        kraj_najwiecej_granic = country["name"]["official"]
print("Kraj, który graniczy z największą ilością innych krajów: ", kraj_najwiecej_granic,
      " Ilość granic: ", ile_granic)