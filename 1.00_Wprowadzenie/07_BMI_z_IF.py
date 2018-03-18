# logika

waga = float(input('Podaj wage: '))
wzrost = float(input('Podaj wzrost w metrach: '))

bmi = round((waga/wzrost**2),2)

if bmi < 20:
    wynik = "Masz niedowagę."
if bmi >= 20 and bmi <= 25:
    wynik = "Waga w normie."
if bmi > 25:
    wynik = "Masz nadwagę!!!"

print('BMI wynosi = ' + str(bmi) + '. ' + wynik)
