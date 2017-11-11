# Korzystając z API http://py.net/ zarejestruj się (/register)
# pamiętaj że może być tylko jeden użytkownik pod daną nazwą (name)


import requests
resp = requests.post(
    'http://py.net/register',
    json={
        'name': "my_name",
        'password': "qwe"
    }
)
print(resp.json())

