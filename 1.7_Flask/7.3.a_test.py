import requests

save_result = requests.post(
    'http://localhost:5000/user/jakisuser/set-password',
    json={"password": "jakieshaslo"}
)
print(save_result.text)




