import requests

url = "https://zenodo.org/records/11441197/files/osdg-community-data-v2024-04-01.csv?download=1"

response = requests.get(url)

if response.status_code == 200:
    with open("data/osdg-community-data-v2024-04-01.csv", "wb") as f:
        f.write(response.content)
