import random

liczba = random.randint(1, 100)
ilosc_strzalow = 0

print('Wybierz liczbę pomiędzy 1, a 100. Masz 5 strzałów.')

while ilosc_strzalow < 5:
    print('Strzelaj!')
    strzal = input()
    strzal = int(strzal)

    ilosc_strzalow = ilosc_strzalow + 1

    if strzal < liczba:
        print('Twoja liczba jest za niska.')

    if strzal > liczba:
        print('Twoja liczba jest za wysoka.')

    if strzal == liczba:
        break

if strzal == liczba:
    ilosc_strzalow = str(ilosc_strzalow)
    print('Gratuluję! Zgadłeś w ' + ilosc_strzalow + ' podejściach!')

if strzal != liczba:
    liczba = str(liczba)
    print('Nie zgadłeś. To była liczba ' + liczba)

