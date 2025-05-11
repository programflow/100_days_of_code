import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

BEARER_TOKEN = os.environ.get("SHEETY_TOKEN")

# This calss is going


class DataManager:
    """ This class is responsible for managing the data for google sheets via sheety."""
    def __init__(self):
        # This Sets up authorization header for sheety
        self.bearer_headers = {
            "Authorization": f"Bearer {BEARER_TOKEN}"
        }
        self.sheet_data = {}
        self.customer_data = {}

    def get_desired_flight_data(self):
        """ This method will get the datta from the prices spreadsheet containing:
        # (1) city
        # (2) iata code
        # (3) price threshold

        The method should return a list of dictionaries representing the desired flight location data.
        """
        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=self.bearer_headers)
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
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            print(response.json())

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.bearer_headers)
        customer_data = response.json()['users']
        pprint(customer_data)

data_manager = DataManager()
data_manager.get_customer_emails()






