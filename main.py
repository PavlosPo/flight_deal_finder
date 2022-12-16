#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os

from data_manager import DataManager

print(os.getenv("SHEET_AUTORIZATION"))
sheet_data = DataManager()
print(sheet_data.data)
