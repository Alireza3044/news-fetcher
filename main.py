import requests
from datetime import date
from email_sender import send_email

API_KEY = "7f38ced1aeda423294e57b50ee73ff9f"

TODAY_DATE = date.today().strftime("%Y-%m-$d")


def get_news(topic: str, from_date: ... = TODAY_DATE, n_news = 10) -> list:

    URL = f"https://newsapi.org/v2/everything?q={topic}" \
          f"&from={from_date}&sortBy=popularity&searchIn=title" \
          f"&language=en&pageSize={n_news + 1}&apiKey={API_KEY}"

    res = requests.get(URL)
    data = res.json()
    articles = data["articles"]

    news_list = []

    for article in articles:
        news = {
            "title": article["title"],
            "desc": article["description"],
            "content": article["content"],
            "source": article["source"]["name"],
            "url": article["url"]
        }
        news_list.append(news)

    return news_list


if __name__ == "__main__":
    todays_news = get_news("Samsung")
    news2 = todays_news[2]

    send_email(news2["title"], f"{news2["desc"]}\n\n\nNews by: {news2["source"]}\n\n{news2["url"]}")
