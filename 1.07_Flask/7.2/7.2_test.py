import requests

save_result = requests.post(
    "http://localhost:5000/current-status",
    json={"status": "starting"}
)
print(save_result.text)

read_result = requests.get(
    "http://localhost:5000/current-status"
)
print(read_result.text)
