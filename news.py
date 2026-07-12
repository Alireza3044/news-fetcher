from datetime import date
from decouple import config
import requests

API_KEY = config("API_KEY")


class News:
    def fetch_news(self, topic: str, from_date: str | None = None,
                 n_news: int = 10) -> list[str]:
        if from_date is None:
            from_date = date.today().strftime("%Y-%m-%d")
        URL = f"https://newsapi.org/v2/everything?q={topic}" \
              f"&from={from_date}&sortBy=popularity&searchIn=title" \
              f"&language=en&pageSize={n_news + 1}&apiKey={API_KEY}"

        res = requests.get(URL)
        data = res.json()
        articles = data["articles"]

        news_list = []
        for article in articles:
            news_list.append({
                "title": article["title"],
                "desc": article["description"],
                "url": article["url"]
            })
        return news_list

    @staticmethod
    def make_html(news_list: list[str]) -> str:
        msg = ""
        for news in news_list:
            msg += f"<p><b>{news["title"]}</b></p><p>{news["desc"]}</p>" \
                   f"<p>{news["url"]}</p><br>"
        return msg
