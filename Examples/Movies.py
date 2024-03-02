import requests

url = "https://one-for-all-api.onrender.com/api/movies"
params = {
    "apiKey": "YOUR_API_KEY",
    "query": "Inception"
}
response = requests.get(url, params=params)
movie_details = response.json()
print(movie_details)
