slownik_osob = {
    'facet': {
        'imie': 'Jan',
        'nazwisko': 'Nowak',
        'data_ur': '22.02.1999',
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
        'data_ur': '02.09.1998',
        'zawod': 'kucharka',
        'zainteresowania': [
            'programowanie',
            'kuchania włoska',
            'fizyka kwantowa'],
        'fikcyjny_stan_konta': 9999.99
    },

    'sąsiad': {
        'imie': 'Kaziu',
        'nazwisko': 'Kowalski',
        'data_ur': '02.09.1988',
        'zawod': 'bez zawodu',
        'zainteresowania': [
            'łapanie much',
            'dłubanie w nosie'],
        'fikcyjny_stan_konta': 99999.99
    }
}

slownik_osob['sąsiad']['fikcyjny_stan_konta'] +=1111

print(slownik_osob['sąsiad'])

