#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests,os
API_KEY = "tpUdpHxxkyiNEgjzG6YT3XHrEXE2052N"
API_SECRET = "Jpn0dUM9WNeM3AeH"
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()