import os
import requests

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/top-headlines" \
    "?country=us&category=business&" \
    "apiKey=" + api_key

# Make request
r = requests.get(url)

# Get dictionary with data
content = r.json()

# Access article titles and description 
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
