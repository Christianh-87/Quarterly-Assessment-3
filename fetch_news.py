# fetch_news.py
import requests
from config import NEWS_API_KEY

def fetch_latest_news(topic="technology", num_articles=5):
    """
    Fetch the latest news articles from NewsAPI for a given topic.
    Prints the title and URL of each article.
    """

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,               # keyword or topic
        "language": "en",         # English articles
        "sortBy": "publishedAt",  # newest first
        "pageSize": num_articles, # number of articles
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print("Error fetching news:", data.get("message"))
        return

    articles = data.get("articles", [])
    print(f"\nTop {len(articles)} articles about '{topic}':\n")

    for i, article in enumerate(articles, start=1):
        title = article.get("title", "No title available")
        url = article.get("url", "No URL available")
        print(f"{i}. {title}\n   {url}\n")

# Run directly for quick testing
if __name__ == "__main__":
    fetch_latest_news("technology", 5)
