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

import glob
my_path = '/home/bmosqueda/Downloads/BIKE/Code/'

files = glob.glob(my_path + "*.sql")

for file in files:
  # Aquí dentro usar la función para leer imágenes
  # Hacer las modificaciones a la imagen 
  # Guardar la imagen