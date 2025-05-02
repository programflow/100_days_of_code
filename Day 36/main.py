

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
import os
import datetime as dt
import smtplib
import unicodedata

from email.message import EmailMessage

# Get import dates using datetime
today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = today - dt.timedelta(days=2)
formatted_yesterday =yesterday.strftime("%Y-%m-%d")
formatted_db_yesterday =day_before_yesterday.strftime("%Y-%m-%d")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_vantage_api_key = "api_key"
ap_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "interval" : "5min",
    "apikey" : alpha_vantage_api_key
}
av_url = "https://www.alphavantage.co/query?"
av_response = requests.get(av_url, params=ap_parameters)
data = av_response.json()



yesterday_close = float(data["Time Series (Daily)"][formatted_yesterday]["4. close"])
db_yesterday_close = float(data["Time Series (Daily)"][formatted_db_yesterday]["4. close"])
percent_change = (yesterday_close - db_yesterday_close)/db_yesterday_close *100




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api_key = "<news api key>"

new_parameters ={
    "q" : "tesla",
    "searchIn" : "title",
    "from" : formatted_yesterday,
    "sortBy" : "publishedAt",
    "language" : "en",
    "apikey" : news_api_key
}

news_url = "https://newsapi.org/v2/everything"
news_response = requests.get(news_url, params=new_parameters)
news_data = news_response.json()
articles = news_data['articles'][0:3]

formatted_text = [f"Headline: {article['title']}. \nBrief: {article['description']}"for article in articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
MY_EMAIL = "<email address>"
MY_PASSWORD = "<google pass>"
MY_PHONE = "<phone number>"

CARRIERS = {
    "spectrum": "@mypixmessages.com",
    "verizon": "@mms.att.net",
    "tmobile" : "@tmomail.net",
}
def clean_sms_text(text, limit=100):
    safe_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

    safe_text = " ".join(safe_text.strip().split())
    return safe_text[:limit]

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (MY_EMAIL, MY_PASSWORD)

    msg = EmailMessage()
    msg["From"] = MY_EMAIL
    msg["To"] = recipient
    msg.set_content(message, charset="utf-8")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(auth[0], auth[1])
        server.send_message(msg)

if abs(percent_change) >=5:
    for message in formatted_text:
        formatted_message = clean_sms_text(message)
        send_message(MY_PHONE, "spectrum", formatted_message)


