import requests
from datetime import datetime, timedelta

reminders = []

def set_reminder(text):
    reminder_time = datetime.now() + timedelta(minutes=1)  # Simplified example
    reminders.append((reminder_time, text))
    return "Reminder set!"

def get_weather():
    api_key = "your_openweather_api_key"
    location = "your_location"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(weather_url)
    weather_data = response.json()
    weather = weather_data['weather'][0]['description']
    return f"The weather is currently {weather}"

def general_query(query):
    api_key = "your_wolframalpha_api_key"
    query_url = f"http://api.wolframalpha.com/v1/result?i={query}&appid={api_key}"
    response = requests.get(query_url)
    return response.text
