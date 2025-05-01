import requests
import os
import smtplib

CARRIERS = {
    "spectrum": "@mypixmessages.com",
    "veriozon": "@mms.att.net",
    "tmobile" : "@tmomail.net",
}

MY_EMAIL = "johndoedothough@gmail.com"
MY_PASSWORD = "phbeoypovugbianb"
MY_PHONE = "8182793945"

account_sid = "AC77f9d80be0bb30d908d8823716064a50"
auth_token = "5459cc81413e521509090de57989f070"

def send_message(phone_number,carrier,message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (MY_EMAIL, MY_PASSWORD)
    server = smtplib.SMTP("smtp.gmail.com")  # Ex. Using gmail, port 587 may need updated if using different host
    server.starttls()
    server.login(auth[0], auth[1])
    server.sendmail(auth[0], recipient, message)

parameters = {
    "lat" : 33.396561,
    "lon" : -84.589981,
    "appid" : "f7904d933588b663632adae8554e3a7a",
    "cnt" : 4
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data["list"]:
    condition_code = weather["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    text_message = "It's going to rain today. Bring an umbrella."
    send_message(MY_PHONE, "tmobile", text_message)
else:
    text_message = "It's sunny today. Don't worry about an Umbrella Squook."