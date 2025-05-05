
import requests
import os

def fetch_related_news(ticker):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("articles", [])[:3]
    except Exception as e:
        print("❌ News fetch error:", e)
        return []
