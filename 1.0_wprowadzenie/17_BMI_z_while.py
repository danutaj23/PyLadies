petla = True
while petla:
    waga = float(input('Podaj wage: '))
    wzrost = float(input('Podaj wzrost w metrach: '))
    bmi = round((waga/wzrost**2), 2)

    if bmi < 20:
        wynik = "Masz niedowage."
    elif 20 <= bmi < 25:
        wynik = "Waga w normie."
    else:
        wynik = "Masz nadwage!!!"

    print('BMI wynosi = ' + str(bmi) + '. ' + wynik)

    pytanie = input('Czy chcesz zakończyć? t/n ')
    if pytanie == 't':
        petla = False