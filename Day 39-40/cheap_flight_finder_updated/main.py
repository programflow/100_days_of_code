import time
from datetime import datetime, timedelta

# These are the custom methods
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# -------------------------------------------- Retrieve Spreadsheet Data --------------------------------------------- #
data_manager = DataManager()
sheet_data = data_manager.get_desired_flight_data()


# --------------------------------------- Get Destination IATA code for Spreadsheet ---------------------------------- #
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")
data_manager.destination_data = sheet_data
data_manager.update_iata_code()
data_manager.customer_data = data_manager.get_customer_emails()




# ------------------------------------------ Send Notification via Signal -------------------------------------------- #
notification_manager = NotificationManager()

# Set up query search dates
tomorrow = datetime.today() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))


for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flights is None:
        flights = flight_search.search_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct = "false"
        )
    cheapest_flight = find_cheapest_flight(flights)
    print(cheapest_flight)
    if cheapest_flight.price !="N/A" or int(cheapest_flight.price) <= int(destination["lowestPrice"]):
        message = (f"Low price Alert to {destination['city']}! Only £{cheapest_flight.price} to "
                   f"fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on "
                   f"{cheapest_flight.out_date} until {cheapest_flight.return_date}")

        notification_manager.send_message(message)
        notification_manager.send_email(message,data_manager.customer_data)




    # Slowing down requests to avoid rate limit
    time.sleep(2)