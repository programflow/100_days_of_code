API_KEY = "A1vx7NKFnBeUNLaTbYHquFKY3kTqStlp"
API_SECRET = "0aeXEWkijpgLhdtB"

BASE_URL = "test.api.amadeus.com/v2"

POST_ATTACHMENT = "/shopping/flight-offers"
POST_PARAMS = {}

GET_ATTACHMENT = "/shopping/flight-offers"
GET_PARAMS = {
    "originLocationCode" : "SYD",
    "destinationLocationCode" : "BKK",
    "departureDate": "2025-05-05",
    "adults": 1,
    "nonStop": False
}




class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    pass