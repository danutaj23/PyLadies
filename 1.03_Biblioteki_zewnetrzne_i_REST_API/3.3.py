# Korzystając z API http://py.net/ pobierz klucz API (api_key) - zaloguj się (/auth).

import requests
resp = requests.post(
    'http://py.net/auth',
    json={
        'name': "my_name",
        'password': "qwe"
    }
)
print(resp.json())

