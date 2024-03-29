import config
import sys
import time
from datetime import datetime
import os
from enum import IntFlag
import re 

sys.path.append(config.UTILS_PATH)
sys.path.append(config.MODELS_PATH)
from date_to_mysql_format import date_to_mysql_format
from validator import is_int
# from database import Database
# from bicycle_trips import BicycleTrip
# from station import Station
from validator import Validator
# from csv_month_loader import CSVMonthLoader

# bicycle_controller = BicycleTrip()
# station_controller = Station()

rules = {
  "Genero_Usuario": "is_required|has_exact_length,1",
  "Edad_Usuario": "is_required|is_int",
  "Bici": "is_required|is_int",
  "Ciclo_Estacion_Retiro": "is_int",
  "Fecha_Retiro": "is_date_in_mysql_format",
  "Hora_Retiro": "is_hour_in_mysql_format|is_valid_hour",
  "Ciclo_Estacion_Arribo": "is_int",
  "Fecha_Arribo": "is_date_in_mysql_format",
  "Hora_Arribo": "is_hour_in_mysql_format|is_valid_hour"
}

obj = {
  "Genero_Usuario": "hola",
  "Bici": "45ss",
  "Ciclo_Estacion_Arribo": 22.23
}

print(round(time.time(), 2))
print(round(time.time()))