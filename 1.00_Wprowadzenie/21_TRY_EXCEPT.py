# Trolle
# Try/Except

# def czy_to_cyfra(tekst):
#     if isinstance(tekst, (float, int)):
#         return tekst
#     if not isinstance(tekst, str):
#         return False
#     tekst = tekst.replace(',', '.')
#     try:
#         float(tekst)
#         return tekst
#     except ValueError:
#         return False

# def czy_ala_ma_kota(wiek_ali):
#     wiek_ali = czy_ala_ma_kota(wiek_ali)
#     if wiek_ali and wiek_ali < 18 or wiek_ali > 40:
#         return True
#     return False
#
#
# czy_ala_ma_kota(25.5)


def pobierz_float(dane):
    while True:
        try:
            return float(input(dane))
        except ValueError:
            print('Podaj liczbę!')


waga = pobierz_float('Podaj wage: ')
wzrost = pobierz_float('Podaj wzrost w metrach: ')
bmi = str(round((waga/wzrost**2), 2))

print('BMI wynosi = ' + bmi)

