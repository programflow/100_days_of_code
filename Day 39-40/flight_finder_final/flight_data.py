class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date,
                 origin_city="N/A", destination_city="N/A"):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.origin_city = origin_city
        self.destination_city = destination_city


def find_cheapest_flight(data):
    """
    Given the raw flight data from Amadeus API, returns a FlightData object
    representing the cheapest round-trip flight.
    """
    if not data or "data" not in data or not data["data"]:
        print("⚠️ No flight data provided.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest = None
    lowest_price = float("inf")

    for flight in data["data"]:
        try:
            price = float(flight["price"]["grandTotal"])
            origin_seg = flight["itineraries"][0]["segments"][0]
            return_seg = flight["itineraries"][1]["segments"][0]

            origin_code = origin_seg["departure"]["iataCode"]
            dest_code = origin_seg["arrival"]["iataCode"]
            out_date = origin_seg["departure"]["at"].split("T")[0]
            return_date = return_seg["departure"]["at"].split("T")[0]

            origin_city = origin_seg["departure"].get("terminal", "Unknown City")
            dest_city = origin_seg["arrival"].get("terminal", "Unknown City")

            if price < lowest_price:
                lowest_price = price
                cheapest = FlightData(
                    price, origin_code, dest_code, out_date, return_date,
                    origin_city=origin_city,
                    destination_city=dest_city
                )

        except (KeyError, IndexError, TypeError, ValueError):
            continue

    if cheapest:
        print(f"💸 Lowest price to {cheapest.destination_airport}: ${cheapest.price}")
        return cheapest
    else:
        print("⚠️ No valid flights found.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")