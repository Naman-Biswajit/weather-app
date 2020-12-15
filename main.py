import dotenv
import os
import requests
from pprint import pprint as show

dotenv.load_dotenv()

url = "https://community-open-weather-map.p.rapidapi.com/weather"


city = input("Enter you city Name: ")
country = input("Enter you Country Name: ")

querystring = {"q":f"{city},{country}","mode":"xml, html"}

headers = {
    'x-rapidapi-key': str(os.environ.get('api_key')),
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
show(response.__dict__)