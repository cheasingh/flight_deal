# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

from tqdm import tqdm

data_point = DataManager()
d = data_point.get_data()
notification = NotificationManager()

changes_detected = []


for i in tqdm(d["prices"]):
    flight = FlightSearch()
    by_city = flight.search(i["iataCode"], ddate="15/03/2021")
    flight_data = FlightData(data=by_city)

    if i["lowestPrice"] > flight_data.prep_data()["lowestPrice"]:
        data = {
            "price": {
                "lowestPrice": flight_data.prep_data()["lowestPrice"]
            }
        }
        data_point.update_data(i["id"], data=data)
        to_use_data = flight_data.prep_data()
        to_use_data["prev_price"] = i["lowestPrice"]
        changes_detected.append(to_use_data)


if len(changes_detected) > 0:
    message = notification.send_sms(changes_detected)

    print("lower price detected, message sent 😊") if message == None else print(
        "error occurred")
else:
    print("no lower price detected 😞")
