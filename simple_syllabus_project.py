''' 
- Accuweather API project for Simple Syllabus
- Checks location by city e.g., Sarasota, Tampa, etc.
- Prompts the user to enter a city.
- Asks user to enter a specific metric (Celsius or Fahrenheit).
- Returns the current weather status of the city.
@author Sebastian Mark
'''

import requests

# API key 
api_key = "kHC0ZA8OTTTX3qEedAZBwK105fS3ZVyi"
base_url = "http://dataservice.accuweather.com/"

# Function to retrieve the location key for a given city name
def get_location_key(city_name):
    location_url = f"{base_url}locations/v1/cities/search?apikey={api_key}&q={city_name}"

    # Attempt to fetch location data with a timeout to handle unresponsiveness
    try: 
        response = requests.get(location_url, timeout=20)
        if response.status_code == 200:
            data = response.json()
            # Check if the response contains data and retrieve the location key
            if data:
                location_key = data[0]["Key"]  # Access the key for the location from the API response
                return location_key
            else:
                print(f"City '{city_name}' not found. Please try again with a valid city name.")
                return None
        else:
            print("Cannot find location key")
            return None
    # Handle timeout exceptions when the request takes too long
    except requests.exceptions.Timeout:
        print("This request timed out. Please try again with another input.")
        return None
    # Handle general request errors (e.g., network issues)
    except requests.exceptions.RequestException as error:
        print(f"An error has occurred, please try again: {error}")
        return None

# Function to fetch weather data based on location key and selected unit (Celsius or Fahrenheit)
def get_weather(location_key, unit="imperial"):
    weather_url = f"{base_url}currentconditions/v1/{location_key}?apikey={api_key}&language=en-us&details=true"
    
    try:
        # Make a request to get weather data with a timeout to prevent hanging
        response = requests.get(weather_url, timeout=20)
        if response.status_code == 200:
            data = response.json()
            if data:
                weather = data[0]  # Access the first element of the JSON response
                # Choose temperature based on user's unit preference
                if unit == "metric":
                    temperature = weather["Temperature"]["Metric"]["Value"]  # Celsius
                else:
                    temperature = weather["Temperature"]["Imperial"]["Value"]  # Fahrenheit
                description = weather["WeatherText"]  # Weather description (e.g., "Sunny")
                return temperature, description
            else:
                print("Could not find the weather data.")
                return None
        else:
            print("Error, cannot find weather data")
            return None
    # Handle timeout exceptions for weather data requests
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
        return None
    # Handle general request exceptions for weather data
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
        return None

# Main driver function to run the Accuweather app
def run_app():
    while True:
        # Taking input from the user for city name
        city_name = input("Enter city name (or type 'exit' to quit): ")
        
        # Check if the user wants to exit the application
        if city_name.lower() == 'exit':
            print("Exiting the app. Please check the spelling or capitalization.")
            # Exit the while loop
            break
        
        # Fetch the location key using the entered city name
        location_key = get_location_key(city_name)
        if location_key:
            # Ask user for the preferred unit (Celsius or Fahrenheit)
            unit_choice = input("Would you like the temperature in Celsius (C) or Fahrenheit (F)? ").strip().lower()
            
            # Determine the unit system based on user input
            if unit_choice == 'c':
                unit = 'metric'  # Metric system (Celsius)
            else:
                unit = "imperial"  # Imperial system (Fahrenheit)
            
            # Fetch the weather data based on the location key and selected unit
            temperature, description = get_weather(location_key, unit)
            
            if temperature and description:
                # Display the temperature and weather description based on the unit
                if unit == "metric":
                    print(f"The current temperature in {city_name} is {temperature}°C with {description}.")
                else:
                    print(f"The current temperature in {city_name} is {temperature}°F with {description}.")
                break  # Exit the loop after successfully fetching the weather data
            else:
                # If weather data could not be fetched, display an error message
                print("Could not fetch weather data.")
                break  # Exit the loop
        else:
            continue  # Retry if location key is not found

# Calling the main driver function to start the app
run_app()
