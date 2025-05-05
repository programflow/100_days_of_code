import requests
import os
from twilio.rest import Client
parameters = {
    "lat" : 33.396561,
    "lon" : -84.589981,
    "appid" : "f7904d933588b663632adae8554e3a7a",
    "cnt" : 4
}
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast?"

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data['list']:
    condition_code = weather['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella!")