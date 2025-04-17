from dotenv import load_dotenv
from dotenv import dotenv_values

import requests

# fetch from API URL 

url = "https://rickandmortyapi.com/api"
response = requests.get(url)
print(response)
load_dotenv()
# api_key = dotenv_values().get("API_KEY")
# print(api_key)


