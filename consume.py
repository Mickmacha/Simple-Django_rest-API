import requests
respoonse = requests.get('http://localhost:8000/beverages')
print(respoonse.json())