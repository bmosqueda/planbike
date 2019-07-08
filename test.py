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

bicycle_controller = BicycleTrip()
station_controller = Station()

hola = 3
mundo = f'mundo_{hola}'

print(mundo)