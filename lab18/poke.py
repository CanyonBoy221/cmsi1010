from urllib import response
import requests

name = input("Enter the name of a Pokémon: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{name}"
response = requests.get(url, timeout=15)
if response.status_code != 200:
    raise ValueError(f"API error: {response.status_code}")
data = response.json()
print(f"Name: {data['name'].title()} is at index {data['id']}.")
