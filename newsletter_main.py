# newsletter_main.py
from summarize_articles import summarize_article
from send_email import send_newsletter
from config import NEWS_API_KEY
import requests

def generate_newsletter(topic_list=None, num_articles=5):
    """
    Fetches recent country music news, focusing on Zach Bryan and related artists.
    Uses broader search parameters to improve result coverage.
    """
    if topic_list is None:
        topic_list = [
            '"Zach Bryan"',
            '"Morgan Wallen"',
            '"Luke Combs"',
            '"Tyler Childers"',
            '"Cody Johnson"',
            '"Lainey Wilson"',
            '"country music"',
            '"country concert"',
            '"country artist"',
            '"CMA Awards"',
            '"country album"',
            '"country song release"'
        ]

    print("Fetching latest country music news...")

    # Loosened query string and sorting method
    query = " OR ".join(topic_list)

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "sortBy": "relevancy",  # use relevancy instead of publishedAt for better match
        "pageSize": num_articles + 3,  # fetch a few extra in case some are filtered
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(url, params=params).json()

    if response.get("status") != "ok":
        print("API error:", response)
        return "<p>Error retrieving country music news.</p>"

    articles = response.get("articles", [])
    print(f"Fetched {len(articles)} articles before filtering.")

    # Filter out irrelevant or off-topic content
    filtered_articles = []
    for article in articles:
        title = (article.get("title") or "").lower()
        description = (article.get("description") or "").lower()

        if any(keyword.lower().replace('"', "") in title + description
               for keyword in ["zach bryan", "country", "morgan wallen", "luke combs", "tyler childers"]):
            filtered_articles.append(article)

    print(f"After filtering: {len(filtered_articles)} relevant articles found.")

    if not filtered_articles:
        return "<p>No recent country music stories were found today.</p>"

    html = "<h2>Country Music Newsletter</h2>"
    html += "<p>Here are today's latest stories and headlines from the world of country music:</p><hr>"

    for article in filtered_articles[:num_articles]:
        title = article.get("title", "No title available")
        description = article.get("description", "No description provided.")
        url = article.get("url", "")
        source = article.get("source", {}).get("name", "Unknown Source")

        print(f"Summarizing: {title[:70]}...")

        try:
            summary = summarize_article(title, url, description)
        except Exception as e:
            summary = f"(Error summarizing this article: {e})"

        html += f"""
        <h3>{title}</h3>
        <p><strong>Source:</strong> {source}</p>
        <p><strong>Summary:</strong> {summary}</p>
        <p><a href="{url}">Read full article</a></p>
        <hr>
        """

    html += "<p><em>Generated automatically by your AI-Powered Country Music Newsletter application.</em></p>"
    return html


if __name__ == "__main__":
    from config import EMAIL_ADDRESS
    print("Generating newsletter...")
    html_content = generate_newsletter(num_articles=5)
    print("\nSending email...\n")
    send_newsletter(
        recipient_email=EMAIL_ADDRESS,
        subject="AI-Powered Country Music Newsletter",
        html_content=html_content
    )
