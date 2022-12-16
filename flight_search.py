# It generates the city's code. Saves it on the google sheet online.
from data_manager import DataManager


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    # Checks if the city code in the google sheet is empty or not
    def Check_if_Empyt(self):
        # Retrieve data
        current_data = DataManager().data  # List of Cities
        for current_city in current_data:
            if current_city['iataCode'] == '' or None:
                # Current city has not a iataCode
                # TODO: FIll the empty cells with the str "TESTING"

                # TODO: Fill the city code online
                pass

        pass

    pass

