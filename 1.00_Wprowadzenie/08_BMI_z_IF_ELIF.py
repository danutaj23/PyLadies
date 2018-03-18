# if x== "a":
#     print ('1')
# elif x == "b"
#     print('2')
# else:
#     print('3')

waga = float(input('Podaj wage: '))
wzrost = float(input('Podaj wzrost w metrach: '))

bmi = round((waga/wzrost**2), 2)

if bmi < 20:
    wynik = "Masz niedowagę"
elif bmi >= 20 and bmi <= 25:
    wynik = "Waga w normie"
else:
    wynik = "Masz nadwagę!!!"

print('BMI wynosi = ' + str(bmi) + '. ' + wynik)

