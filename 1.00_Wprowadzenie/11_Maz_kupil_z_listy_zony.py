lista_zony = [input('1 produkt z listy żony: '),
              input('2 produkt z listy żony: '),
              input('3 produkt z listy żony: ')]
lista_meza = [input('1 produkt zakupiony przez męża: '),
              input('2 produkt zakupiony przez męża: '),
              input('3 produkt zakupiony przez męża: ')]

maz_kupil = []
if lista_zony[0] in lista_meza:
    maz_kupil.append(lista_zony[0])
if lista_zony[1] in lista_meza:
    maz_kupil.append(lista_zony[1])
if lista_zony[2] in lista_meza:
    maz_kupil.append(lista_zony[2])
print('Mąż kupił z listy żony: ' + str(maz_kupil))

maz_kupil_nadmiar = []
if lista_meza[0] not in lista_zony:
    maz_kupil_nadmiar.append(lista_meza[0])
if lista_meza[1] not in lista_zony:
    maz_kupil_nadmiar.append(lista_meza[1])
if lista_meza[2] not in lista_zony:
    maz_kupil_nadmiar.append(lista_meza[2])
print('Mąż kupił nadmiarowo: ' + str(maz_kupil_nadmiar))


