import os
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth


get_endpoint = "https://api.sheety.co/e7b6e23181315cf9ee92d6462b9e1e62/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        #self.sheet_endpoint = "https://docs.google.com/spreadsheets/d/1q6jxmAHeXv4TqL5lZuG-kBgJEN9oUcSfy5j60ej51Sw/edit"
        self._user = "shryesm"
        self._password = "shryes@19"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=get_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        #pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{get_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)


