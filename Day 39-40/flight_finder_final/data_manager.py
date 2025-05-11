import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
BEARER_TOKEN = os.getenv("SHEETY_TOKEN")


class DataManager:
    """Handles Google Sheets data operations via Sheety API."""

    def __init__(self):
        self.bearer_headers = {
            "Authorization": f"Bearer {BEARER_TOKEN}"
        }
        self.destination_data = []
        self.customer_data = []

    def get_desired_flight_data(self):
        """Retrieve the destination cities, their IATA codes, and threshold prices."""
        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=self.bearer_headers)
        response.raise_for_status()
        self.destination_data = response.json().get("prices", [])
        return self.destination_data

    def update_iata_code(self):
        """Update IATA codes in the spreadsheet if they are missing."""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            response.raise_for_status()

    def get_customer_emails(self):
        """Retrieve customer emails who want to receive flight notifications."""
        response = requests.get(SHEETY_USERS_ENDPOINT, headers=self.bearer_headers)
        response.raise_for_status()
        self.customer_data = response.json().get("users", [])
        return self.customer_data