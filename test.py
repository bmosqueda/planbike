import config
import sys
import time
from datetime import datetime
import os

sys.path.append(config.UTILS_PATH)
sys.path.append(config.MODELS_PATH)

from validator import is_int
from database import Database
from bicycle_trips import BicycleTrip
from station import Station
from validator import Validator
from csv_month_loader import CSVMonthLoader

bicycle_controller = BicycleTrip()
station_controller = Station()

loader = CSVMonthLoader()
file = '/home/bmosqueda/Downloads/BIKE/Resources/Datasets/hola.csv'
loader.load(file)