from pprint import pprint as pp

slownik_osob = {
    'facet': {
        'imie': 'Jan',
        'nazwisko': 'Nowak',
        'data_ur': '22.02.1977',
        'zawod': 'elektryk',
        'zainteresowania': [
            'piłka nożna',
            'wspinaczka',
            'kino francuskie'],
        'fikcyjny_stan_konta': 9.99
    },

    'baba': {
        'imie': 'Anna',
        'nazwisko': 'Nowak',
        'data_ur': '02.09.1997',
        'zawod': 'kucharka',
        'zainteresowania': [
            'programowanie',
            'kuchnia włoska',
            'fizyka kwantowa'],
        'fikcyjny_stan_konta': 9999.99
    },

    'sąsiad': {
        'imie': 'Kaziu',
        'nazwisko': 'Kowalski',
        'data_ur': '01.06.1987',
        'zawod': 'bez zawodu',
        'zainteresowania': [
            'łapanie much',
            'dłubanie w nosie'],
        'fikcyjny_stan_konta': 99999.99
    }
}
# 1. zdublowanie stanu konta
slownik_osob['baba']['fikcyjny_stan_konta'] = slownik_osob['baba']['fikcyjny_stan_konta']*2

# 2. dodanie zainteresowań kobiecie
slownik_osob['baba']['zainteresowania'].append('wspinaczka')
slownik_osob['baba']['zainteresowania'].append('nurkowanie')
slownik_osob['baba']['zainteresowania'] += ['muzyka klasyczna', 'Python']

# 3. zmiana nazwiska u kobiety
slownik_osob['baba']['nazwisko'] = 'Kiepska'

# # 4. dołożenie wszystkim drugiego imienia
slownik_osob['baba']['drugie imie'] = 'Hermenegilda'
slownik_osob['facet']['drugie imie'] = 'Kwiryn'
slownik_osob['sąsiad']['drugie imie'] = 'Brajan'

# 5. stworzenie nowego klucza z wiekiem
slownik_osob['baba']['wiek'] = 20
slownik_osob['facet']['wiek'] = 40
slownik_osob['sąsiad']['wiek'] = 30

# 6. dodanie wykształcenia
slownik_osob['baba']['wyksztalcenie'] = 'zawodowe'
slownik_osob['facet']['wyksztalcenie'] = 'jakies'
slownik_osob['sąsiad']['wyksztalcenie'] = 'trudno powedzieć'

# 7. usunięcie daty urodzenia
del slownik_osob['facet']['data_ur']
del slownik_osob['baba']['data_ur']
del slownik_osob['sąsiad']['data_ur']


pp(slownik_osob['facet'])
pp(slownik_osob['baba'])
pp(slownik_osob['sąsiad'])
