''' 
- Accuweather API project for Simple Syllabus
- Checks location by city e.g., Sarasota, Tampa, etc.
- Prompts the user to enter a city.
- Asks user to enter a specific metric (Celsius or Fahrenheit).
- Returns the current weather status of the city.
@author Sebastian Mark
'''

import tkinter as tk
from tkinter import messagebox
import requests

# AccuWeather API setup
api_key = "kHC0ZA8OTTTX3qEedAZBwK105fS3ZVyi"
base_url = "http://dataservice.accuweather.com/"

def get_location_key(city_name):
    location_url = f"{base_url}locations/v1/cities/search?apikey={api_key}&q={city_name}"
    try:
        response = requests.get(location_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]["Key"]
            else:
                return None
        else:
            return None
    except Exception as error:
        print(f"Error: {error}")
        return None


def get_weather(location_key, unit):
    weather_url = f"{base_url}currentconditions/v1/{location_key}?apikey={api_key}&details=true"
    try:
        response = requests.get(weather_url, timeout=10) # Times out after 10 seconds if no input is made
        if response.status_code == 200:
            data = response.json() # Json data
            if data:
                temperature = data[0]["Temperature"]["Metric" if unit == "Celsius" else "Imperial"]["Value"]
                description = data[0]["WeatherText"]
                return temperature, description
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def fetch_weather():
    city = city_entry.get()
    unit = unit_var.get()
    if not city: # Error handling 
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    location_key = get_location_key(city)
    if not location_key: # Return an error message back to the user if the city if not found
        messagebox.showerror("Error", f"City '{city}' not found.")
        return

    temperature, description = get_weather(location_key, unit)
    if temperature is not None: # Returns the current temperture 
        result = f"The current temperature in {city} is {temperature}{('C' if unit == 'Celsius' else 'F')} with {description.lower()} weather."
        messagebox.showinfo("Weather Info", result)
    else:
        messagebox.showerror("Error", "Failed to retrieve weather data.")

# GUI Setup
window = tk.Tk()
window.title("Weather App")

# Set the window size to make it bigger (e.g., 600x400 pixels)
window.geometry("600x400")

# Add GUI components
tk.Label(window, text="Enter City:").pack(pady=10)  # Added padding for spacing
city_entry = tk.Entry(window)
city_entry.pack(pady=5)

unit_var = tk.StringVar(value="Celsius")
tk.Label(window, text="Select Unit:").pack(pady=10)

# User metric/imperial unit selection
tk.Radiobutton(window, text="Celsius", variable=unit_var, value="Celsius").pack()
tk.Radiobutton(window, text="Fahrenheit", variable=unit_var, value="Fahrenheit").pack()

tk.Button(window, text="Get Weather", command=fetch_weather).pack(pady=20)

# Main driver function
window.mainloop()
