# abs(-12)
# round(12.1233222)
# round(12.1212334,2)


waga = float(input('Podaj wage: '))
wzrost = float(input('Podaj wzrost w metrach: '))

bmi = round((waga/wzrost**2), 2)

print('bmi wynosi =' + str(bmi))
