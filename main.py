import requests
from datetime import date

API_KEY = "7f38ced1aeda423294e57b50ee73ff9f"

TODAY_DATE = date.today().strftime("%Y-%m-$d")


def get_news_by_topic(topic: str, from_date: ... = TODAY_DATE) -> list:

    URL = f"https://newsapi.org/v2/everything?q={topic}" \
          f"&from={from_date}&sortBy=popularity&apiKey={API_KEY}"

    res = requests.get(URL)
    data = res.json()
    articles = data["articles"][:10]
    
    news_list = []

    for article in articles:
        news = {
            "title": article["title"],
            "content": article["content"],
            "source": article["source"]["name"],
            "url": article["url"]
        }
        news_list.append(news)

    return news_list


if __name__ == "__main__":
    todays_news = get_news_by_topic("Microsoft")
    news1 = todays_news[0]
    print(news1)
