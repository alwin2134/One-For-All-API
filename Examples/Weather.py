import requests

url = "https://one-for-all-api.onrender.com/api/weather"
params = {
    "api": "YOUR_Openweathermap_API_KEY",
    "location": "New York"
}
response = requests.get(url, params=params)
weather_data = response.json()
print(weather_data)
