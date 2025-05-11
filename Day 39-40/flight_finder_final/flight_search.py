import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    """Handles flight and IATA code lookups using the Amadeus API."""

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        """Fetch a new OAuth2 token from the Amadeus API."""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        response.raise_for_status()
        token = response.json().get("access_token")

        print("🔐 Token acquired.")
        return token

    def get_destination_code(self, city_name):
        """Fetch the IATA code for a given city name."""
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }

        response = requests.get(IATA_ENDPOINT, headers=headers, params=params)
        try:
            return response.json()["data"][0]["iataCode"]
        except (IndexError, KeyError):
            print(f"⚠️ No airport code found for '{city_name}'.")
            return "N/A"

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct="true"):
        """Search for available flight offers."""
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": is_direct.lower() == "true",
            "max": 25,
            "currencyCode": "USD"
        }

        response = requests.get(FLIGHT_ENDPOINT, headers=headers, params=params)
        if response.status_code != 200:
            print(f"❌ Error fetching flights: {response.status_code} {response.text}")
            return []

        try:
            return response.json()["data"]
        except (KeyError, ValueError):
            print("⚠️ Unexpected API response structure.")
            return []