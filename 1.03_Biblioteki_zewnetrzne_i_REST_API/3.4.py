# Korzystając z API http://py.net/ po pobraniu klucza API (api_key)
# ustaw status swojego użytkownika (/user_status/set) i sprawdź status innych (/user_status)
# w szczególności koleżanki/kolegi obok.

import requests
resp1 = requests.post(
    'http://py.net/auth',
    json={
        "name": "my_name",
        "password": "qwe"
    }
)
resp2 = requests.post(
    'http://py.net/user_status/set',
    json={
        "api_key": resp1.json()["api_key"],
        "status": "LoremIpsum"
    }
)
print(resp2.json())

resp3 = requests.get('http://py.net/user_status/')
print(resp3.json()['my_name'])
print(resp3.json()['WeronikaF'])

