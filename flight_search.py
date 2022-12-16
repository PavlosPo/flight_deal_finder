# It generates the city's code. Saves it on the google sheet online.
from data_manager import DataManager


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.check_if_empyt()
        pass

    # Checks if the city code in the google sheet is empty or not
    def check_if_empyt(self):
        # Retrieve data
        current_data = DataManager().data  # List of Cities

        # Create dictionary of data
        for index, current_city in enumerate(current_data):
            if current_city['iataCode'] == '' or current_city['iataCode'] is None:
                # Current city has not a iataCode
                current_data[index]['iataCode'] = "TESTING"
        print(current_data)
        pass

    pass

