# Korzystając z API http://py.net/ sprubój użyc querry stringów (query_string)

# import requests
# resp = requests.get('http://py.net/query_string')
# print(resp.json())

import requests
resp = requests.get("http://py.net/query_string?name=my_name&cokolwiek=cos")
print(resp.json())
