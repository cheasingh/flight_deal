import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):

        self.param = {
            "apikey": os.environ["TEQ_API"],
            "fly_from": "PNH"
        }

        self.endpoint = "https://tequila-api.kiwi.com/v2/search"

    def search(self, destination, ddate, **kwarge):

        self.param["fly_to"] = destination
        self.param["date_from"] = ddate

        if kwarge:
            self.param["date_to"] = kwarge["rdate"]

        r = requests.get(self.endpoint, self.param)

        return r.json()
