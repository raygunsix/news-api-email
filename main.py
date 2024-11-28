import os
import requests

# https://newsapi.org

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/top-headlines" \
    "?country=us&category=business&" \
    "apiKey=" + api_key

r = requests.get(url)
content = r.text
print(content)