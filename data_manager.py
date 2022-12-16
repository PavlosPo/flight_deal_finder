import os
import requests

SHEET_ENDPOINT = "https://api.sheety.co/be61e1838b9166a7c340361536e14c49/flightDeals/prices"
SHEET_HEADERS = {
    "Authorization": "Bearer #################################",
    "Content-Type": "application/json",
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Gets the data
        self.data = None
        self.get_data()

    # Data fetch
    def get_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADERS)
        response.raise_for_status()
        self.data = response.json()['prices']

    # Updates data in each city/id
    def update_data(self, updated_data: list):
        # Get the ids so we can update the corresponding id
        # Updates each row of data per loop
        for current_city in updated_data:
            current_city_id = current_city['id']
            data_to_upload = {'price': current_city}  # Formats it the way Sheety wants to.
            requests.put(url=f"{SHEET_ENDPOINT}/{current_city_id}", json=data_to_upload, headers=SHEET_HEADERS)

