import requests
from pprint import pprint

API_KEY = 'c2925b8558b4b95e05e2b3702bba7b31'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city


weather_data = requests.get(base_url).json()

pprint(weather_data)
