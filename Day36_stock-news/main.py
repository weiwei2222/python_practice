import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "84NLS95W5UKBO82B"
NEW_API_KEY = "70885df144054e5ab34894f67a9cfaa0"
TWILIO_SID = "ACa6b94891b9b7ce4010064bf5373003dc"
TWILIO_AUTH_TOKEN = "5b96b00fddfd3fc7763efe803a49845f"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# data_list = []
# for (key, value) in data.items():
#     data_list.append(value)
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down =None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
print(difference)


diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


if abs(diff_percent) > 4:
    new_params = {
        "apiKey": NEW_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)


formatted_articles = [f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['description']}. \nBrief: {article['description']}" for article in three_articles]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+17473023823",
        to="+16147722442"
    )

