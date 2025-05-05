import requests

sheety_endpoint = "https://api.sheety.co/2c421bd56502b283265aacb755fccccd/flightDeals/prices"



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(sheety_endpoint)
        self.data = self.response.json()
        print(self.data)

    def get_desired_flight_price(self):
        for desired_flight in self.data["prices"]:
            desired_flight_city = desired_flight["city"]
            desired_flight_price = desired_flight["lowestPrice"]
            print(desired_flight_city, desired_flight_price)

    def post_iata_code(self):
        for i in range(len(self.data["prices"])):
            if self.data["prices"][i]["city"] == "Paris":
                self.data["prices"][i]["iataCode"] ="testing"

        print(self.data)






data_manager = DataManager()

data_manager.post_iata_code()