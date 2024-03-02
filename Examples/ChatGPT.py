import requests

url = "https://one-for-all-api.onrender.com/api/chatgpt"
params = {
    "api": "YOUR_OpenAI_API_KEY",
    "prompt": "Tell me a joke."
}
response = requests.get(url, params=params)
chat_response = response.json()
print(chat_response)
