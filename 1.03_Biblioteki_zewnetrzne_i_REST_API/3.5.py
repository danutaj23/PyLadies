# Korzystając z API http://py.net/ ściągnij i zapisz na dysku losowe zdjęcia kotów (/cat)

import requests
resp = requests.get('http://py.net/cat')
with open('cat.jpg', 'wb') as file:
    file.write(resp.content)
