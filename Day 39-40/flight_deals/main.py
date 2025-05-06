from data_manager import DataManager
from flight_search import FlightSearch
import time

data_manager = DataManager()
sheet_data = data_manager.get_desired_flight_data()
print(sheet_data)
flight_search = FlightSearch()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(3)

print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_iata_code()