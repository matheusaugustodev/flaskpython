import requests

api_url = 'http://127.0.0.1:5000/user'

response = requests.get(api_url)

json_response = response.json()

print(json_response)