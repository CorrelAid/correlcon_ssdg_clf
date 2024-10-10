import requests

url = "https://zenodo.org/records/7523032/files/sdg_knowledge_hub.csv?download=1"

response = requests.get(url)

if response.status_code == 200:
    with open("data/sdg_knowledge_hub.csv", "wb") as f:
        f.write(response.content)
