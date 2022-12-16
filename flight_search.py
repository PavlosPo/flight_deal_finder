# generates the corresponding IATA Codes for each City.
import requests
import os

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
KIWI_PARAMETERS = {
    "term": None,  # We need to find it
    "location_types": "city",
    "limit": 1
}
KIWI_HEADERS = {
    "apikey": os.getenv('KIWI_API'),
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name) -> str:
        KIWI_PARAMETERS['term'] = city_name
        response = requests.get(url=KIWI_ENDPOINT, params=KIWI_PARAMETERS, headers=KIWI_HEADERS)
        response.raise_for_status()
        city_code = response.json()['locations'][0]['code']
        return city_code
