import requests

url = "https://one-for-all-api.onrender.com/api/getMarketData"
params = {
    "symbols": "AAPL,GOOGL,MSFT"
}
response = requests.get(url, params=params)
market_data = response.json()
print(market_data)
