import requests

# API key for OpenWeatherMap
api_key = "YOUR_API_KEY_HERE"

# City for which you want to get the weather data
city = "New York, US"

# Construct the API URL
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Fetch the weather data
response = requests.get(api_url)

# Parse the JSON response
weather_data = response.json()

# Print the weather data
print(weather_data)
