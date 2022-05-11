import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = ""          # Your alphavantage.co API Key
NEWS_API_KEY = ""           # Your newsapi.org API Key

TWILIO_ACCOUNT_SID = ""     # Your Twilio account sid
TWILIO_AUTH_TOKEN = ""      # Your Twilio account auth token
TWILIO_NUMBER = ""          # Your Twilio number
RECIPIENT_NUMBER = ""       # Your number (verified with twilio)


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday, get news.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
diff_percent = round(((difference / yesterday_closing_price) * 100), 2)
up_down = "🔺 +" if diff_percent > 0 else "🔻 "

if abs(diff_percent) > 5:
    # Get the first 3 news pieces for the COMPANY_NAME from the News API
    news_parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "sortBy": "publishedAt",
        "pageSize": 1,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in articles]
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for article in formatted_articles:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=article,
                from_=TWILIO_NUMBER,
                to=RECIPIENT_NUMBER
            )

        print(message.status)
