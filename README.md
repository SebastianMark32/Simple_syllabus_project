# Simple Syllabus AccuWeather Python API Project

## **Overview**
This Python application interacts with the AccuWeather API to fetch and display weather information for a given city. Users can input a city name, choose the unit for temperature (Celsius or Fahrenheit), and get the current weather details, such as temperature, weather description, humidity, and wind speed.

## **Features**
* Fetches weather data based on city input.
* Displays current weather, temperature, and description.
* Supports temperature units in Celsius or Fahrenheit.
* Handles API errors and invalid city names.

* ## **Prerequisites**

Ensure that Python 3.x and pip are installed on your machine.

### Installing Python & pip
1. Download Python from [python.org](https://www.python.org/downloads/).
2. During installation, check the box to add Python to your PATH.
3. After installation, you can verify Python and pip installation by running:
   ```bash
   python --version
   pip --version

## **Dependencies**

* `requests`– For making HTTP requests to the AccuWeather API.

You can manually install the required dependencies if the `requirements.txt` file is not provided:

## **API Key Setup**
   
 You’ll need an API key to access the AccuWeather API. You can obtain it from the [AccuWeather API](https://developer.accuweather.com/). After obtaining your API key:
 
1. Create a file called `config.py` in the project directory.
2. Add the following line to store your API key:
3. 3. Or copy and paste your own API key. 
   ```python
   api_key = "your_api_key_here"


## **Usage**
1. Run the program:
   
python simple_syllabus_project.py

2. The program will prompt you for:
- **City Name**: Enter the name of the city (e.g., "Sarasota").
- **Unit (Celsius or Fahrenheit)**: Choose between Celsius or Fahrenheit for temperature.

## Example
```bash
Enter a city name: Sarasota
Enter the unit (Celsius or Fahrenheit): Celsius
The current temperature in Sarasota is 25°C with Sunny weather.


