import requests
resp = requests.get('http://py.net/health')
print(resp.json)
