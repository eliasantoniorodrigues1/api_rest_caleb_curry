import requests

BASE = 'http://127.0.0.1:5000/'

drink = [{"name": "Cola", "description": "Delicious"}]

response = requests.put(f"drinks/{drink[0]}")
print(response)