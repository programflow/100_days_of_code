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
    "originLocationCode" : "LAX",
    "destinationLocationCode" : "SXF",
    "departureDate": "2025-05-06",
    "adults": 1,
    "nonStop": True
}




class FlightSearch:
    """This class is responsible for talking to the Flight Search API.
    The method _get_new_token is used to get a token in order to query the Flight Search API. The tokens expire
    typically in 30mins (1799secs)."""
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        self._token = self._get_new_token()


    def _get_new_token(self):
        """ The header requires some specific information, The body requires:
        (1) "grant_type",
        (2) "client_id",
        (3) "client_secret
        in order to get a new token. This method should return a new token as a string"""

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
        print(response.json())
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")

        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        """
        This method gets the IATA code for the given city name.
        """
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

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = "true"):
        # print(f"Using this token to check_flight() {self._token}"
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": is_direct,
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(
            url=FLIGHT_ENDPOINT,
            params=query,
            headers=headers)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        return response.json()

