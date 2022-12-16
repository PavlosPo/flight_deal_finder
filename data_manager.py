import os
import requests
SHEET_ENDPOINT = "https://api.sheety.co/be61e1838b9166a7c340361536e14c49/flightDeals/prices"
SHEET_HEADERS = {
    "Authorization": os.getenv(key='SHEET_AUTHORIZATION'),
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
        self.data = response.json()
        return self.data

