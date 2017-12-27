# # lista
#
# lista_x = ['Kasia', 'Jan']
# lista_y = [1, 3, 5, 7]
#
# # dodanie elementu w liście
# lista_x.append('Natalia')
# print(lista_x)
#
# # wypisyeanie elementu z listy
# print(lista_x[0])
#
# # usunięcie elementu z listy
# lista_x.pop(1)
# lista_x.remove('Kasia')

lista_osob = [
    [input('Imie: '), input('Wiek: ')],
    [input('Imie: '), input('Wiek: ')],
    [input('Imie: '), input('Wiek: ')],
]

# lista osób
print(lista_osob)

# tylko imiona
print(lista_osob[0][0], lista_osob[1][0], lista_osob[2][0])

# tylko wiek
print(lista_osob[0][1], lista_osob[1][1], lista_osob[2][1])

# każda osoba osobno
print(lista_osob[0])
print(lista_osob[1])
print(lista_osob[2])



