#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint

from data_manager import DataManager

sheet = DataManager()
sheet_data = sheet.data
pprint(sheet_data)
