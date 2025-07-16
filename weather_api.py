import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API")

def get_weather(city):
    if not API_KEY:
        return "Weather API key missing."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {temp}°C with {desc}."
    elif response.status_code == 404:
        return "City not found in weather API."
    elif response.status_code == 401:
        return "Invalid Weather API key."
    else:
        return "Unable to fetch weather data."
