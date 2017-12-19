plec = input('Jakiej jesteś płci? k/m: \n')
waga = float(input('Podaj wage: \n'))
wzrost = float(input('Podaj wzrost w metrach: \n'))
bmi = round((waga / wzrost ** 2), 2)

if plec == 'k':
    if bmi < 16.5:
        wynik = "Masz anoreksję!"
    elif 16.5 <= bmi < 20:
        wynik = "Masz niedowagę."
    elif 20 <= bmi < 25:
        wynik = "Waga w normie."
    elif 25 <= bmi < 30:
        wynik = "Masz nadwagę."
    else:
        wynik = "Otyłość!!!"
else:
    if bmi < 18.5:
        wynik = "Masz anoreksję!"
    elif 18.5 <= bmi < 22.5:
        wynik = "Masz niedowagę."
    elif 22.5 <= bmi < 27.5:
        wynik = "Waga w normie."
    elif 27.5 <= bmi < 32.5:
        wynik = "Masz nadwagę."
    else:
        wynik = "Otyłość!!!"

print('BMI wynosi = ' + str(bmi) + '. ' + wynik)
