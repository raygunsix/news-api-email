import os
import requests
from send_email import send_email

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/top-headlines?" \
    "country=us&" \
    "category=business&" \
    "language=en&" \
    "apiKey=" + api_key

# Make request
r = requests.get(url, timeout=10)

# Get dictionary with data
content = r.json()

raw_message = ""

# Access article titles and description 
for article in content["articles"][:20]:
    raw_message = raw_message + f"""
{article["title"]}
{article["description"]}
{article["url"]}
"""

# Build email

# Backslash and LB required when including subject in email text
message = f"""\
Subject: Daily News

{raw_message}
"""

send_email(message)
