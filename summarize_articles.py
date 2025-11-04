# summarize_articles.py
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_article(title, url, description):
    """
    Uses OpenAI's model to generate a short, email-friendly summary.
    """
    prompt = (
        f"Summarize this news article into 3-5 concise sentences suitable for a professional newsletter.\n\n"
        f"Title: {title}\n"
        f"Description: {description}\n"
        f"URL: {url}\n\n"
        f"Summary:"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a concise, professional newsletter editor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.5,
    )

    summary = response.choices[0].message.content.strip()
    return summary


# Quick manual test
if __name__ == "__main__":
    test_title = "The Stallman Paradox: How Web3 Became the Ultimate Open Source Theater"
    test_desc = (
        "An article exploring how open source ideals intersect with Web3’s decentralized vision, "
        "analyzing tensions between freedom and monetization."
    )
    test_url = "https://paragraph.com/@holonic-horizons/the-stallman-paradox-how-web3-became-the-ultimate-open-source-theater"

    print("Generating summary...\n")
    print(summarize_article(test_title, test_url, test_desc))
