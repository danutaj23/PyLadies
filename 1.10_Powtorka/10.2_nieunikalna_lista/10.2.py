# Napisz algorytm, który na wejście przyjmie listę zawierającą tylko stringi i integery.
# Zwróci listą zawierającą tylko powtarzające się wartości, nie zmieniając ich kolejności.
# Przykład: [1, 2, 3, 1, 3] 1 i 3 nie są unikalne, więc wynikiem będzie [1, 3, 1, 3].


lista = [1, 2, 3, 1, 3, 'a', 'a']


def lista_nieunikalna(lista):
    nowa_lista = []
    for element in lista:
        if lista.count(element) > 1:
            nowa_lista.append(element)

    return print(nowa_lista)


lista_nieunikalna(lista)


# lista = [1, 2, 3, 1, 3, 'a', 'a']
# lista_nieunikalna = set([x for x in l if l.count(x) > 1])
# print(lista_nieunikalna)