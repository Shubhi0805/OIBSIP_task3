import requests
import tkinter as tk
from tkinter import ttk
import sys

def get_weather_data(location, api_key):
    """Fetches weather data for a given location using the OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        sys.exit()

def display_weather_data(data):
    """Displays weather data in a user-friendly format."""
    temp_kelvin = data['main']['temp']
    temp_celsius = round(temp_kelvin - 273.15, 2)
    humidity = data['main']['humidity']
    conditions = data['weather'][0]['description']

    weather_label.config(text=f"Temperature: {temp_celsius}°C\nHumidity: {humidity}%\nConditions: {conditions}")

def search_weather():
    location = location_entry.get()
    api_key = "your_api_key_here"
    data = get_weather_data(location, api_key)

    if data:
        display_weather_data(data)

root = tk.Tk()
root.title("Weather App")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

location_label = ttk.Label(frame, text="Enter a city or ZIP code:")
location_label.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky=tk.W)

location_entry = ttk.Entry(frame, width=20)
location_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky=tk.E)

search_button = ttk.Button(frame, text="Search", command=search_weather)
search_button.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky=tk.EW)

weather_label = ttk.Label(frame, text="")
weather_label.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky=tk.W)

root.mainloop()