import requests

url = "https://one-for-all-api.onrender.com/api/news"
params = {
    "apiKey": "YOUR_API_KEY",
    "sources": "CNN,BBC",
    "category": "business",
    "country": "us"
}
response = requests.get(url, params=params)
news_articles = response.json()
print(news_articles)
