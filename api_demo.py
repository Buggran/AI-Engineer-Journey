import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

# print(response)
data = response.json()
print(data["name"])