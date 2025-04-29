import requests


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
#
# # Response codes
# # 1XX: Hold on
# # 2XX: here You go
# # 3XX: go away
# # 4XX: You screwed up
# # 5XX: I screwed up
#
# # print(response.status_code)
#
# response.raise_for_status()
#
# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)
MY_LAT = 51.507351
MY_LNG = -0.127758
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
data = response.json()
sunset_time = data['results']['sunset']
sunrise_time = data['results']['sunrise']
print(sunrise_time)
print(sunset_time)
print(sunrise_time.split("T")[1].split(":")[0])
print(sunset_time.split("T")[1].split(":")[0])

