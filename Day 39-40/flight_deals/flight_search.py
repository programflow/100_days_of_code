import os
import requests
from dotenv import load_dotenv
from data_manager import DataManager
load_dotenv()


FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
POST_PARAMS = {}


GET_PARAMS = {
    "originLocationCode" : "SYD",
    "destinationLocationCode" : "BKK",
    "departureDate": "2025-05-05",
    "adults": 1,
    "nonStop": False
}




class FlightSearch:

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        self._token = self._get_new_token()
    #This class is responsible for talking to the Flight Search API.

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")

        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        query = {
            "keyword": city_name,
            "max" : "2",
            "include": "AIRPORTS"
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not found"

        return code



