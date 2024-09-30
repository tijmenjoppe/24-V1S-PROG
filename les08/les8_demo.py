import pprint

import requests

# Zie https://www.omdbapi.com/
OMDB_API_KEY = "465d41bf"

resource = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i=tt1285016"
response = requests.get(resource)
data = response.json()

pprint.PrettyPrinter(indent=4)
# pprint.pprint(data)

for key in ['Title', 'Plot']:
    print(key, ":", data[key])

while True:
    film = input("Geef een filmtitel: ")

    resource = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={film}"
    response = requests.get(resource)
    data = response.json()

    for key in ['Title', 'Plot']:
        print(key, ":", data[key])
