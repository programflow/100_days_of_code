import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


SHEETY_ENDPOINT = "https://api.sheety.co/2c421bd56502b283265aacb755fccccd/flightDeals/prices"
BEARER_TOKEN = os.environ.get("SHEETY_TOKEN")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.bearer_headers = {
            "Authorization": f"Bearer {BEARER_TOKEN}"
        }
        self.sheet_data = {}

    def get_desired_flight_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=self.bearer_headers)
        data = response.json()
        self.sheet_data = data['prices']
        pprint(self.sheet_data)
        return self.sheet_data


    def update_iata_code(self):

        for city in self.sheet_data:

            new_data = {
                "price" : {
                    "iataCode" : city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            print(response.json())





