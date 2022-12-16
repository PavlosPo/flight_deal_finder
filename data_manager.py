import os
import requests
from flight_search import FlightSearch

SHEET_ENDPOINT = "https://api.sheety.co/be61e1838b9166a7c340361536e14c49/flightDeals/prices"
SHEET_HEADERS = {
    "Authorization": os.getenv('SHEET_AUTHORIZATION'),
    "Content-Type": "application/json",
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Gets the data
        self.data = None
        self.get_data()  # Fetch the online dataset
        self.update_empty_iotcodes()  # Updates the data argument with str 'TESTING'
        self.upload_data()  # Uploads all data if id is not specified, else only the specified id

    # Data fetch
    def get_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADERS)
        response.raise_for_status()
        self.data = response.json()['prices']

    # Locally updates the data
    def update_empty_iotcodes(self):
        for index, current_city in enumerate(self.data):
            if current_city['iataCode'] == '':
                # Current city has not a iataCode
                self.data[index]['iataCode'] = "TESTING"

    # Updates data online
    def upload_data(self, given_id=None):  # uploads the current data online.
        # Updates each row of data per loop
        if given_id is None:
            for current_city in self.data:
                current_city_id = current_city['id']
                data_to_upload = {'price': current_city}  # Formats it the way Sheety wants to.
                requests.put(url=f"{SHEET_ENDPOINT}/{current_city_id}", json=data_to_upload, headers=SHEET_HEADERS)
        elif given_id is not None:
            current_city_id = given_id
            current_city_data = self.data[given_id - 2]  # The first id is 2, so the first element of list is 2 - 2
            data_to_upload = {'price': current_city_data}  # Formats it the way Sheety wants to.
            requests.put(url=f"{SHEET_ENDPOINT}/{current_city_id}", json=data_to_upload, headers=SHEET_HEADERS)

    def upload_city_codes(self):

        pass