import requests

# Your API key
api_key = "kHC0ZA8OTTTX3qEedAZBwK105fS3ZVyi"
base_url = "http://dataservice.accuweather.com/"

# Get location key
def get_location_key(city_name):
    location_url = f"{base_url}locations/v1/cities/search?apikey={api_key}&q={city_name}"
    
    try:
        # Adding timeout to avoid hanging indefinitely
        response = requests.get(location_url, timeout=10)  # Timeout added here
        
        if response.status_code == 200:
            data = response.json()
            if data:  # Check if data exists
                location_key = data[0]["Key"]
                return location_key
            else:
                print(f"City '{city_name}' not found. Please try again with a valid city name.")
                return None
        else:
            print("Error fetching location key.")
            return None
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Get weather using location key
def get_weather(location_key, unit="imperial"):
    weather_url = f"{base_url}currentconditions/v1/{location_key}?apikey={api_key}&language=en-us&details=true"
    
    try:
        # Adding timeout to avoid hanging indefinitely
        response = requests.get(weather_url, timeout=10)  # Timeout added here
        
        if response.status_code == 200:
            data = response.json()
            if data:
                weather = data[0]
                if unit == "metric":  # For Celsius
                    temperature = weather["Temperature"]["Metric"]["Value"]
                else:  # Default to Fahrenheit
                    temperature = weather["Temperature"]["Imperial"]["Value"]
                description = weather["WeatherText"]
                return temperature, description
            else:
                print("Error: Could not retrieve weather data.")
                return None
        else:
            print("Error fetching weather data.")
            return None
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
        return None
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
        return None

# Main driver function to run the app
def run_weather_app():
    while True:
        city_name = input("Enter city name (or type 'exit' to quit): ")
        
        if city_name.lower() == 'exit':
            print("Exiting the weather app.")
            break
        
        location_key = get_location_key(city_name)

        if location_key:
            unit_choice = input("Would you like the temperature in Celsius (C) or Fahrenheit (F)? ").strip().lower()
            if unit_choice == 'c':
                  # Celsius
                unit = "metric"
            else:
                 # Fahrenheit
                unit = "imperial" 
            
            temperature, description = get_weather(location_key, unit)
            if temperature and description:
                if unit == "metric":
                    print(f"The current temperature in {city_name} is {temperature}°C with {description}.")
                else:
                    print(f"The current temperature in {city_name} is {temperature}°F with {description}.")
                break
            else:
                print("Could not fetch weather data.")
                break
        else:
            continue

# Run the weather app
run_weather_app()
