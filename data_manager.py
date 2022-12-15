import os
import requests

SHEET_HEADERS = {
    "Authorization": os.environ["SHEET_AUTHORIZATION"],
    "Content-Type": "application/json",
}
SHEET_ENDPOINT = "https://api.sheety.co/be61e1838b9166a7c340361536e14c49/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = ''
        self.get_data()

    def get_data(self):
        self.data = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADERS).json()
        return self.data

