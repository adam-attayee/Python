# the goal of this app is to send an SMS if the closing stock price of a given company moves by more than 5% from the previous closing day.
# in addition to notifying the user the percentage change in price, it should also provide 3 recent news articles (headline and description only)  

import requests
from twilio.rest import Client


def get_articles(company):
    news_data_parameters = {
        "q": company,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_data_parameters)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"][:3]

    article_dict = [
        {articles[0]["title"]: articles[0]["description"]},
        {articles[1]["title"]: articles[1]["description"]},
        {articles[2]["title"]: articles[2]["description"]}
    ]

    return article_dict


def send_alert(change, ticker, headline, brief):
    if change >= 5:
        emoji = "🔺"
    else:
        emoji = "🔻"

    account_sid = "[ACCOUNT_SID]"
    auth_token = "[AUTH_TOKEN]"

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"{ticker}:{emoji}{abs(change)}%\nHeadline: {headline}\nBrief: {brief}",
        from_='+123456789',
        to='+123456789'
    )

    return message.status


STOCK_API_KEY = "[SOTCK_API_KEY]"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "[NEWS_API_KEY]"

stock_data_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_data_parameters)
response.raise_for_status()
stock_data = response.json()

dates = list(stock_data["Time Series (Daily)"])[0:2]

yesterday_close = float(stock_data["Time Series (Daily)"][dates[0]]["4. close"])
before_yesterday_close = float(stock_data["Time Series (Daily)"][dates[1]]["4. close"])

change_in_price = round((yesterday_close/before_yesterday_close - 1) * 100, 2)

if abs(change_in_price) > 5:
    articles = get_articles(COMPANY_NAME)
    for article in articles:
        for title in article:
            send_alert(change_in_price, STOCK, title, article[title])
