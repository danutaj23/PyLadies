# Korzystając z API http://py.net/ spróbuj użyc querry stringów (query_string)

import requests
resp = requests.get("http://py.net/query_string?name=my_name&cokolwiek=cos")
print(resp.json())
