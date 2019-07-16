import config
import sys
import time
from datetime import datetime
import os
from enum import IntFlag

sys.path.append(config.UTILS_PATH)
sys.path.append(config.MODELS_PATH)

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
validator = Validator(rules)
class Colors(IntFlag):
  BLUE = 1
  RED = 2


print(Colors.BLUE == 1)
print(Colors.BLUE.name == 'blue')
print(Colors.BLUE)
print(Colors.RED)