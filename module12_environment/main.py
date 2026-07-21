import requests

print("installed successfully")
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Server:", response.headers.get("Server"))