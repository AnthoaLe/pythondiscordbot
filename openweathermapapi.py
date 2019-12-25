# openweathermapapi.py

import os
from dotenv import load_dotenv

import json, requests, sys

load_dotenv()
key = os.getenv('OPEN_WEATHER_API_KEY')

def requestWeatherData(zipCode : str) -> str:
    openWeatherMapURL = f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode},us&appid={key}"
    requestURL = requests.get(openWeatherMapURL)
    if (requestURL.status_code == 404):
        return f"Entered zip code does not exist. Entered zip code was: {zipCode}"
    return str(requestURL.json())