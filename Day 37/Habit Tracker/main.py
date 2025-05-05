import requests
from datetime import datetime, timedelta

from aiohttp.web_routedef import delete

USERNAME = "fl0werb019000"
TOKEN = "lksadj39lfjas83foj10"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}
# Create account: only use once
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)
# print(response.status_code)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

# --------------------------------------------create Graph ---------------------------------------------#
graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "minutes",
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


#-----------------------------------------Create Pixel --------------------------------------------------#
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.today()
yesterday = today - timedelta(days=1)
day = yesterday.strftime("%Y%m%d")
print(day)
pixel_upload = {
    "date": day,
    "quantity": "0"
}

# response = requests.post(pixel_creation_endpoint, json=pixel_upload, headers=headers)
# print(response.text)
#-----------------------------------------Update Pixel --------------------------------------------------#
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day}"
pixel_update = {
    "quantity": "120",
}

response = requests.put(pixel_update_endpoint, json=pixel_update, headers=headers)
print(response.text)

# ------------------------------ delete pixel --- --------------------------------------------------------#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day}"
# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)