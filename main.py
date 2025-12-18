import requests
from datetime import date
from email_sender import send_email

API_KEY = "7f38ced1aeda423294e57b50ee73ff9f"

TODAY_DATE = date.today().strftime("%Y-%m-$d")


def make_html_msg(news_func):
    def wrapper(*args, **kwargs):
        todays_news = news_func(*args, **kwargs)

        msg = ""
        for news in todays_news:
            msg += f"<b>{news["title"]}</b><br>" \
                f"{news["desc"]}<br>" \
                f"{news["url"]}<br><br><br>"

        return msg
    return wrapper


@make_html_msg
def fetch_news(topic: str, from_date: str = TODAY_DATE, n_news = 15) -> list:

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
            "url": article["url"]
        }
        news_list.append(news)

    return news_list


if __name__ == "__main__":
    msg = fetch_news("RAM")
    send_email("Today's News", msg)
