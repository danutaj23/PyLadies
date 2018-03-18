# Zmodyfikuj pętle do liczenia BMI żeby samo liczenie było funcją któą wypisze nam
# stan użytkownika (parametry przekazane w funkcji)

waga = float(input('Podaj wage: '))
wzrost = float(input('Podaj wzrost w metrach: '))


def oblicz_bmi(waga, wzrost):
    bmi = round((waga / wzrost ** 2), 2)
    if bmi < 20:
        wynik = "Masz niedowage."
    elif 20 <= bmi < 25:
        wynik = "Waga w normie."
    else:
        wynik = "Masz nadwage!!!"
    print('BMI wynosi = ' + str(bmi) + '. ' + wynik)


oblicz_bmi(waga, wzrost)






