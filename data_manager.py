import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.param = []
        self.header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['SHEETY_API']}"
        }
        self.endpoint = "https://api.sheety.co/602d3144698ef6a7bb0b27f473462826/flightDeals/prices"

    def get_data(self):
        r = requests.get(self.endpoint, headers=self.header)
        return r.json()

    def update_data(self, id, data):
        r = requests.put(
            self.endpoint+f"/{str(id)}", json=data, headers=self.header)

        return r.status_code
