# Wczytaj plik i stwórz słownik w którym kluczem będzie imię (i nazwisko)
# a wartością będzie słownik z kluczami kolor oczu i wzrost
# Przykład: {"Yoda": {"height": 66, "eyes": "brown"}}

file = open('py1.2.txt')
dictionary = {}

for data in file:
    name = data[data.find(' ') + 1:data.find(' has')]
    eyes = data[data.find('has ') + 4:data.find(' and')]
    height = data[data.find(' is ') + 3:data.find(' cm')]

    dictionary['Name'] = name
    dictionary['Eyes'] = eyes
    dictionary['Height'] = height

    print(dictionary)

file.close()
