import requests
import os


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.data = data["data"][0]

    def prep_data(self):
        flight_data = {
            "city": self.data["cityTo"],
            "iataCode": self.data["cityCodeTo"],
            "lowestPrice": self.data["price"]
        }

        return flight_data
